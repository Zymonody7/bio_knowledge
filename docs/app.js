const bundleUrl = "./data/site_bundle.json";

const state = {
  papers: [],
  filtered: [],
  summary: {},
  digest: "",
  embeddings: { dimensions: 0 },
  selectedPaperId: null,
  activeGroup: "",
};

const heroStatsEl = document.querySelector("#hero-stats");
const digestPreviewEl = document.querySelector("#digest-preview");
const groupListEl = document.querySelector("#group-list");
const paperListEl = document.querySelector("#paper-list");
const paperItemTemplate = document.querySelector("#paper-item-template");
const paperCountEl = document.querySelector("#paper-count");
const searchInput = document.querySelector("#search-input");
const topicFilter = document.querySelector("#topic-filter");
const sourceFilter = document.querySelector("#source-filter");
const categoryFilter = document.querySelector("#category-filter");
const detailMetaEl = document.querySelector("#detail-meta");
const detailTitleEl = document.querySelector("#detail-title");
const detailLinkEl = document.querySelector("#detail-link");
const detailTagsEl = document.querySelector("#detail-tags");
const detailImportanceEl = document.querySelector("#detail-importance");
const detailRelevanceEl = document.querySelector("#detail-relevance");
const detailNoveltyEl = document.querySelector("#detail-novelty");
const detailTimesSeenEl = document.querySelector("#detail-times-seen");
const detailWhyEl = document.querySelector("#detail-why");
const detailAbstractEl = document.querySelector("#detail-abstract");
const askForm = document.querySelector("#ask-form");
const questionInput = document.querySelector("#question-input");
const askStatus = document.querySelector("#ask-status");
const answerCard = document.querySelector("#answer-card");
const answerBody = document.querySelector("#answer-body");

const tokenize = (text) => (text.toLowerCase().match(/[a-zA-Z0-9_+-]{2,}/g) || []);

const cosine = (left, right) => {
  if (!left?.length || !right?.length || left.length !== right.length) return 0;
  let score = 0;
  for (let i = 0; i < left.length; i += 1) score += left[i] * right[i];
  return score;
};

const localEmbed = (text, dimensions) => {
  const vec = new Array(dimensions).fill(0);
  const tokens = tokenize(text);
  for (const token of tokens) {
    let hash = 2166136261;
    for (let i = 0; i < token.length; i += 1) {
      hash ^= token.charCodeAt(i);
      hash = Math.imul(hash, 16777619);
    }
    const index = Math.abs(hash) % dimensions;
    const sign = hash % 2 === 0 ? 1 : -1;
    vec[index] += sign * (1 + Math.min(token.length, 12) / 12);
  }
  const norm = Math.sqrt(vec.reduce((acc, value) => acc + value * value, 0));
  return norm === 0 ? vec : vec.map((value) => value / norm);
};

const lexicalScore = (query, text) => {
  const queryTokens = new Set(tokenize(query));
  const textTokens = new Set(tokenize(text));
  if (!queryTokens.size || !textTokens.size) return 0;
  let overlap = 0;
  for (const token of queryTokens) {
    if (textTokens.has(token)) overlap += 1;
  }
  return overlap / queryTokens.size;
};

function escapeHtml(value = "") {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;");
}

function markdownToHtml(markdown = "") {
  let html = escapeHtml(markdown);
  html = html.replace(/^### (.*)$/gm, "<h3>$1</h3>");
  html = html.replace(/^## (.*)$/gm, "<h2>$1</h2>");
  html = html.replace(/^# (.*)$/gm, "<h1>$1</h1>");
  html = html.replace(/^> (.*)$/gm, "<blockquote>$1</blockquote>");
  html = html.replace(/`([^`]+)`/g, "<code>$1</code>");
  html = html.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  html = html.replace(/\n- (.*?)(?=\n|$)/g, "\n<li>$1</li>");
  html = html.replace(/(<li>.*<\/li>)/gs, "<ul>$1</ul>");
  html = html.replace(/\n{2,}/g, "</p><p>");
  html = `<p>${html}</p>`;
  html = html.replace(/<p><h/g, "<h").replace(/<\/h([1-3])><\/p>/g, "</h$1>");
  html = html.replace(/<p><ul>/g, "<ul>").replace(/<\/ul><\/p>/g, "</ul>");
  html = html.replace(/<p><blockquote>/g, "<blockquote>").replace(/<\/blockquote><\/p>/g, "</blockquote>");
  html = html.replace(/<p><\/p>/g, "");
  return html;
}

function paperLabel(paper) {
  return `${paper.source} / ${paper.date.slice(0, 10)} / ${paper.category}`;
}

function getSelectedPaper() {
  return state.papers.find((paper) => paper.paper_id === state.selectedPaperId) || null;
}

function populateFilters() {
  const topics = new Set();
  const sources = new Set();
  const categories = new Set();

  for (const paper of state.papers) {
    paper.matched_topics.forEach((topic) => topics.add(topic));
    if (paper.source) sources.add(paper.source);
    if (paper.category) categories.add(paper.category);
  }

  for (const [select, items] of [
    [topicFilter, [...topics].sort()],
    [sourceFilter, [...sources].sort()],
    [categoryFilter, [...categories].sort()],
  ]) {
    for (const item of items) {
      const option = document.createElement("option");
      option.value = item;
      option.textContent = item;
      select.appendChild(option);
    }
  }
}

function renderHero() {
  const sources = Object.entries(state.summary.sources || {}).map(([key, value]) => `${key} ${value}`);
  const topics = Object.entries(state.summary.topics || {})
    .sort((a, b) => b[1] - a[1])
    .slice(0, 5)
    .map(([key, value]) => `${key} ${value}`);

  heroStatsEl.innerHTML = "";
  [`累计论文 ${state.summary.total_papers || 0}`, `最近新增 ${state.summary.last_run_count || 0}`, ...sources.slice(0, 3), ...topics].forEach((item) => {
    const tag = document.createElement("span");
    tag.textContent = item;
    heroStatsEl.appendChild(tag);
  });

  digestPreviewEl.innerHTML = markdownToHtml(state.digest.slice(0, 1500) || "暂无摘要。");
}

function buildGroups() {
  const groups = new Map();
  groups.set("", { label: "全部", count: state.filtered.length });
  for (const paper of state.filtered) {
    const key = paper.category || "general";
    const current = groups.get(key) || { label: key, count: 0 };
    current.count += 1;
    groups.set(key, current);
  }
  return [...groups.entries()];
}

function renderGroups() {
  groupListEl.innerHTML = "";
  buildGroups().forEach(([key, group]) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = `group-pill${state.activeGroup === key ? " active" : ""}`;
    button.textContent = `${group.label} ${group.count}`;
    button.addEventListener("click", () => {
      state.activeGroup = key;
      renderGroups();
      renderPaperList();
    });
    groupListEl.appendChild(button);
  });
}

function applyFilters() {
  const q = searchInput.value.trim().toLowerCase();
  const topic = topicFilter.value;
  const source = sourceFilter.value;
  const category = categoryFilter.value;

  state.filtered = state.papers.filter((paper) => {
    const haystack = [paper.title, paper.abstract, paper.why_it_matters, paper.category, paper.source, ...paper.matched_topics].join("\n").toLowerCase();
    if (q && !haystack.includes(q)) return false;
    if (topic && !paper.matched_topics.includes(topic)) return false;
    if (source && paper.source !== source) return false;
    if (category && paper.category !== category) return false;
    return true;
  });

  if (state.activeGroup) {
    const hasActiveGroup = state.filtered.some((paper) => paper.category === state.activeGroup);
    if (!hasActiveGroup) state.activeGroup = "";
  }

  const selectedStillVisible = state.filtered.some((paper) => paper.paper_id === state.selectedPaperId);
  if (!selectedStillVisible) {
    state.selectedPaperId = state.filtered[0]?.paper_id || null;
  }

  renderGroups();
  renderPaperList();
  renderDetail();
}

function renderPaperList() {
  paperListEl.innerHTML = "";
  const visible = state.activeGroup ? state.filtered.filter((paper) => paper.category === state.activeGroup) : state.filtered;
  paperCountEl.textContent = `${visible.length} 篇`;

  visible.forEach((paper) => {
    const node = paperItemTemplate.content.firstElementChild.cloneNode(true);
    node.classList.toggle("active", paper.paper_id === state.selectedPaperId);
    node.querySelector(".paper-item-meta").textContent = paperLabel(paper);
    node.querySelector(".paper-item-title").textContent = paper.title;
    const tags = node.querySelector(".paper-item-tags");
    paper.matched_topics.slice(0, 3).forEach((topic) => {
      const chip = document.createElement("span");
      chip.textContent = topic;
      tags.appendChild(chip);
    });
    node.addEventListener("click", () => {
      state.selectedPaperId = paper.paper_id;
      renderPaperList();
      renderDetail();
    });
    paperListEl.appendChild(node);
  });
}

function renderDetail() {
  const paper = getSelectedPaper();
  if (!paper) {
    detailMetaEl.textContent = "";
    detailTitleEl.textContent = "当前没有符合筛选条件的论文";
    detailLinkEl.href = "#";
    detailTagsEl.innerHTML = "";
    detailWhyEl.innerHTML = markdownToHtml("可以放宽左侧过滤条件，或者直接在右下角提问知识库。");
    detailAbstractEl.innerHTML = "";
    return;
  }

  detailMetaEl.textContent = paperLabel(paper);
  detailTitleEl.textContent = paper.title;
  detailLinkEl.href = paper.url;
  detailImportanceEl.textContent = paper.importance_score;
  detailRelevanceEl.textContent = paper.relevance_score;
  detailNoveltyEl.textContent = paper.novelty_score;
  detailTimesSeenEl.textContent = paper.times_seen;
  detailTagsEl.innerHTML = "";
  [
    ...paper.matched_topics,
    `source:${paper.source}`,
    `category:${paper.category}`,
  ].forEach((tag) => {
    const chip = document.createElement("span");
    chip.textContent = tag;
    detailTagsEl.appendChild(chip);
  });

  const whyMarkdown = [
    `**来源**：${paper.source}`,
    `**为什么值得看**：${paper.why_it_matters}`,
    `**你可以优先关注**：任务定义、数据来源、评价方式、是否能落到真实 workflow。`,
  ].join("\n\n");
  detailWhyEl.innerHTML = markdownToHtml(whyMarkdown);
  detailAbstractEl.innerHTML = markdownToHtml(paper.abstract || "暂无摘要。");
}

function buildDetailedAnswer(query, hits, selectedPaper) {
  if (!hits.length) {
    return markdownToHtml("## 结论\n当前知识库里没有明显相关的论文。\n\n## 建议\n- 放宽问题中的限定词\n- 直接搜 protein / gene / clinical / agent / llm 等核心词");
  }

  const top = hits[0];
  const focused = selectedPaper ? `当前右侧焦点论文是 **${selectedPaper.title}**，所以回答会优先对照它。` : "当前没有指定焦点论文，回答基于整个知识库的召回结果。";
  const evidence = hits.slice(0, 3).map((hit, index) => {
    const reasons = [
      `semantic=${hit.semantic.toFixed(3)}`,
      `lexical=${hit.lexical.toFixed(3)}`,
      `topics=${hit.matched_topics.join(", ") || "无"}`,
      `source=${hit.source}`,
    ].join(" | ");
    return `${index + 1}. **${hit.title}**\n   - ${reasons}\n   - ${hit.why_it_matters}`;
  }).join("\n");

  const suggestions = [
    top.matched_topics.includes("foundation_model_agent") ? "继续追踪它是否定义了可复用的 agent/llm workflow，而不只是泛泛提到 AI。" : "继续追踪它和 foundation model / agent 的结合是否只是表层概念，还是进入了任务设计。",
    top.category === "clinical_application" ? "重点看临床验证样本量、是否有 prospective validation、是否能嵌入真实实验室流程。" : "重点看是否提供可迁移的方法、可复现实验设置和开放资源。",
    "如果你下一步想做知识库问答或选题判断，可以再问：这篇工作对应的数据、模型、评测、临床价值分别是什么？",
  ].map((item) => `- ${item}`).join("\n");

  const compare = selectedPaper && selectedPaper.paper_id !== top.paper_id
    ? `## 与当前焦点论文对照\n当前焦点论文 **${selectedPaper.title}** 更偏 **${selectedPaper.category}**；本次问题最相关的是 **${top.title}**，更偏 **${top.category}**。一个更接近你当前问法，一个更接近你正在看的上下文，建议对比两者的任务边界和实际落地性。`
    : "";

  const markdown = [
    "## 结论",
    `最相关的是 **${top.title}**。它之所以排在最前，是因为与问题在向量语义和显式关键词上都更接近，并且与 **${top.matched_topics.join("、") || "当前研究主题"}** 有更强连接。`,
    "",
    "## 回答范围",
    focused,
    "",
    "## 证据",
    evidence,
    "",
    compare,
    "",
    "## 下一步建议",
    suggestions,
  ].filter(Boolean).join("\n");

  return markdownToHtml(markdown);
}

function answerQuestion(query) {
  const dimensions = state.embeddings.dimensions || 256;
  const queryVector = localEmbed(query, dimensions);
  const selected = getSelectedPaper();
  const candidates = state.papers
    .map((paper) => {
      const semantic = cosine(queryVector, paper.embedding || []);
      const lexical = lexicalScore(query, paper.search_text || "");
      const focusBoost = selected && selected.paper_id === paper.paper_id ? 0.08 : 0;
      const score = semantic * 0.62 + lexical * 0.28 + focusBoost + paper.importance_score * 0.02;
      return { ...paper, score, semantic, lexical };
    })
    .sort((a, b) => b.score - a.score)
    .slice(0, 5);

  return buildDetailedAnswer(query, candidates, selected);
}

async function bootstrap() {
  const response = await fetch(bundleUrl, { cache: "no-store" });
  const bundle = await response.json();
  state.papers = bundle.papers || [];
  state.filtered = [...state.papers];
  state.summary = bundle.summary || {};
  state.digest = bundle.digest_markdown || "";
  state.embeddings = bundle.embedding || {};
  state.selectedPaperId = state.papers[0]?.paper_id || null;

  populateFilters();
  renderHero();
  renderGroups();
  renderPaperList();
  renderDetail();
}

[searchInput, topicFilter, sourceFilter, categoryFilter].forEach((el) => {
  el.addEventListener("input", applyFilters);
  el.addEventListener("change", applyFilters);
});

askForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const query = questionInput.value.trim();
  if (!query) return;
  askStatus.textContent = "正在生成详细解读";
  answerBody.innerHTML = answerQuestion(query);
  answerCard.classList.remove("hidden");
  askStatus.textContent = "已结合当前焦点论文和知识库召回结果";
});

bootstrap().catch((error) => {
  digestPreviewEl.innerHTML = markdownToHtml(`加载失败：${error.message}`);
});
