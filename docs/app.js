const bundleUrl = "./data/site_bundle.json";
const STORAGE_PREFIX = "bio-knowledge-monitor";

const state = {
  papers: [],
  filtered: [],
  summary: {},
  digest: "",
  embeddings: { dimensions: 0 },
  selectedPaperId: null,
  activeGroup: "",
  treeFilter: { kind: "", value: "" },
  favorites: {},
  notes: {},
  llm: {
    mode: "local",
    baseUrl: "https://api.openai.com/v1",
    model: "gpt-4.1-mini",
    apiKey: "",
  },
};

const heroStatsEl = document.querySelector("#hero-stats");
const digestPreviewEl = document.querySelector("#digest-preview");
const groupListEl = document.querySelector("#group-list");
const treeSourceEl = document.querySelector("#tree-source");
const treeTopicEl = document.querySelector("#tree-topic");
const treeYearEl = document.querySelector("#tree-year");
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
const favoriteToggleEl = document.querySelector("#favorite-toggle");
const notesInputEl = document.querySelector("#notes-input");
const notesStatusEl = document.querySelector("#notes-status");
const askForm = document.querySelector("#ask-form");
const questionInput = document.querySelector("#question-input");
const askStatus = document.querySelector("#ask-status");
const answerCard = document.querySelector("#answer-card");
const answerBody = document.querySelector("#answer-body");
const llmModeEl = document.querySelector("#llm-mode");
const llmBaseUrlEl = document.querySelector("#llm-base-url");
const llmModelEl = document.querySelector("#llm-model");
const llmApiKeyEl = document.querySelector("#llm-api-key");

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

function saveJson(key, value) {
  localStorage.setItem(`${STORAGE_PREFIX}:${key}`, JSON.stringify(value));
}

function loadJson(key, fallback) {
  try {
    const raw = localStorage.getItem(`${STORAGE_PREFIX}:${key}`);
    return raw ? JSON.parse(raw) : fallback;
  } catch {
    return fallback;
  }
}

function markdownToHtml(markdown = "") {
  let html = escapeHtml(markdown);
  html = html.replace(/\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g, '<a href="$2" target="_blank" rel="noreferrer">$1</a>');
  html = html.replace(/^### (.*)$/gm, "<h3>$1</h3>");
  html = html.replace(/^## (.*)$/gm, "<h2>$1</h2>");
  html = html.replace(/^# (.*)$/gm, "<h1>$1</h1>");
  html = html.replace(/^> (.*)$/gm, "<blockquote>$1</blockquote>");
  html = html.replace(/`([^`]+)`/g, "<code>$1</code>");
  html = html.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  html = html.replace(/\n- (.*?)(?=\n|$)/g, "\n<li>$1</li>");
  html = html.replace(/\n\d+\. (.*?)(?=\n|$)/g, "\n<li>$1</li>");
  html = html.replace(/(<li>.*?<\/li>)/gs, "<ul>$1</ul>");
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
  const favoriteCount = Object.values(state.favorites).filter(Boolean).length;

  heroStatsEl.innerHTML = "";
  [`累计论文 ${state.summary.total_papers || 0}`, `最近新增 ${state.summary.last_run_count || 0}`, `收藏 ${favoriteCount}`, ...sources.slice(0, 3), ...topics].forEach((item) => {
    const tag = document.createElement("span");
    tag.textContent = item;
    heroStatsEl.appendChild(tag);
  });

  digestPreviewEl.innerHTML = markdownToHtml(state.digest.slice(0, 1800) || "暂无摘要。");
}

function buildGroups() {
  const groups = new Map();
  groups.set("", { label: "全部", count: state.filtered.length });
  groups.set("__favorites__", {
    label: "收藏",
    count: state.filtered.filter((paper) => state.favorites[paper.paper_id]).length,
  });
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

function buildTreeCounts(kind) {
  const counts = new Map();
  for (const paper of state.filtered) {
    if (kind === "source") {
      counts.set(paper.source, (counts.get(paper.source) || 0) + 1);
    } else if (kind === "year") {
      const year = paper.date.slice(0, 4) || "unknown";
      counts.set(year, (counts.get(year) || 0) + 1);
    } else {
      paper.matched_topics.forEach((topic) => counts.set(topic, (counts.get(topic) || 0) + 1));
    }
  }
  return [...counts.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));
}

function renderTreeList(target, kind) {
  target.innerHTML = "";
  const allButton = document.createElement("button");
  allButton.type = "button";
  allButton.className = `tree-item${state.treeFilter.kind === kind && !state.treeFilter.value ? " active" : ""}`;
  allButton.textContent = "全部";
  allButton.addEventListener("click", () => {
    state.treeFilter = { kind: "", value: "" };
    renderAll();
  });
  target.appendChild(allButton);

  buildTreeCounts(kind).forEach(([value, count]) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = `tree-item${state.treeFilter.kind === kind && state.treeFilter.value === value ? " active" : ""}`;
    button.textContent = `${value} ${count}`;
    button.addEventListener("click", () => {
      state.treeFilter = { kind, value };
      renderAll();
    });
    target.appendChild(button);
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
    if (state.treeFilter.kind === "source" && state.treeFilter.value && paper.source !== state.treeFilter.value) return false;
    if (state.treeFilter.kind === "year" && state.treeFilter.value && !paper.date.startsWith(state.treeFilter.value)) return false;
    if (state.treeFilter.kind === "topic" && state.treeFilter.value && !paper.matched_topics.includes(state.treeFilter.value)) return false;
    return true;
  });

  const selectedStillVisible = state.filtered.some((paper) => paper.paper_id === state.selectedPaperId);
  if (!selectedStillVisible) {
    state.selectedPaperId = state.filtered[0]?.paper_id || null;
  }
}

function visiblePapers() {
  const base = state.activeGroup === "__favorites__"
    ? state.filtered.filter((paper) => state.favorites[paper.paper_id])
    : state.activeGroup
      ? state.filtered.filter((paper) => paper.category === state.activeGroup)
      : state.filtered;
  return base;
}

function renderPaperList() {
  paperListEl.innerHTML = "";
  const visible = visiblePapers();
  paperCountEl.textContent = `${visible.length} 篇`;

  visible.forEach((paper) => {
    const node = paperItemTemplate.content.firstElementChild.cloneNode(true);
    node.classList.toggle("active", paper.paper_id === state.selectedPaperId);
    node.querySelector(".paper-item-meta").textContent = paperLabel(paper);
    node.querySelector(".paper-item-title").textContent = `${state.favorites[paper.paper_id] ? "★ " : ""}${paper.title}`;
    const tags = node.querySelector(".paper-item-tags");
    [paper.source, ...paper.matched_topics.slice(0, 2)].forEach((topic) => {
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

function detailAnalysisMarkdown(paper) {
  const intersections = [];
  if (/protein|proteomics|nanobody/i.test(`${paper.title} ${paper.abstract}`)) intersections.push("protein / proteomics");
  if (/gene|genomic|genomics|transcript/i.test(`${paper.title} ${paper.abstract}`)) intersections.push("gene / genomics");
  if (/clinical|patient|diagnosis|microbiology/i.test(`${paper.title} ${paper.abstract}`)) intersections.push("clinical / microbiology");
  if (/agent|llm|language model|foundation model|multimodal/i.test(`${paper.title} ${paper.abstract}`)) intersections.push("AI / LLM / Agent");

  return [
    `**来源**：${paper.source}`,
    `**为什么值得看**：${paper.why_it_matters}`,
    `**与你的研究交叉点**：${intersections.length ? intersections.join("、") : "当前更偏传统生信/病原方向，但可以继续判断是否能接到 AI workflow。"}`,
    `**建议重点读**：数据类型、蛋白质/基因层信号、临床样本设置、是否存在 agent/llm 可切入点、评价指标是否贴近真实流程。`,
    state.notes[paper.paper_id] ? `**你的备注**：${state.notes[paper.paper_id]}` : "",
  ].filter(Boolean).join("\n\n");
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
    notesInputEl.value = "";
    favoriteToggleEl.textContent = "收藏";
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

  favoriteToggleEl.textContent = state.favorites[paper.paper_id] ? "取消收藏" : "收藏";
  notesInputEl.value = state.notes[paper.paper_id] || "";
  detailWhyEl.innerHTML = markdownToHtml(detailAnalysisMarkdown(paper));
  detailAbstractEl.innerHTML = markdownToHtml(paper.abstract || "暂无摘要。");
}

function buildDetailedAnswerMarkdown(query, hits, selectedPaper) {
  if (!hits.length) {
    return "## 结论\n当前知识库里没有明显相关的论文。\n\n## 建议\n- 放宽限定词\n- 改问 protein / gene / clinical / agent / llm 等核心轴线\n- 也可以直接点左侧分类树查看最近论文";
  }

  const top = hits[0];
  const scope = selectedPaper
    ? `当前焦点论文是 **${selectedPaper.title}**。下面会优先对照它，再补充整个知识库中的相近论文。`
    : "当前未锁定具体论文，下面基于整个知识库回答。";

  const evidence = hits.slice(0, 4).map((hit, index) => [
    `${index + 1}. **${hit.title}**`,
    `   - 来源：${hit.source}｜日期：${hit.date.slice(0, 10)}｜类别：${hit.category}`,
    `   - 匹配主题：${hit.matched_topics.join("、") || "无"}`,
    `   - 检索得分：semantic=${hit.semantic.toFixed(3)} / lexical=${hit.lexical.toFixed(3)} / final=${hit.score.toFixed(3)}`,
    `   - 解释：${hit.why_it_matters}`,
  ].join("\n")).join("\n");

  const interpretation = [
    top.matched_topics.includes("foundation_model_agent")
      ? "这批结果里已经出现了和 AI / LLM / Agent 更接近的信号，值得继续判断它们是否只是提及模型，还是已经进入任务设计、评测和自动化 workflow。"
      : "这批结果更偏病原生信和临床监测本体，AI/LLM/Agent 结合点可能还需要你再问更具体的问题，例如 `protein language model`、`clinical agent`、`genomics rag`。",
    /protein|proteomics|nanobody/i.test(`${top.title} ${top.abstract}`)
      ? "从蛋白质角度看，这批结果可能适合延展到 protein foundation model、结构功能预测或抗原/抗体相关任务。"
      : "从蛋白质角度看，当前召回里强信号还不够，可以继续追踪 protein language model、proteomics biomarker 和 host-pathogen protein interaction。",
    /gene|genomic|transcript/i.test(`${top.title} ${top.abstract}`)
      ? "从基因/组学角度看，这批结果更容易接到 gene regulation、variant interpretation、clinical genomics pipeline。"
      : "从基因/组学角度看，建议再搜 host response transcriptomics、gene function prediction、clinical genomics agent。",
    top.category === "clinical_application"
      ? "临床价值上，重点看它是否触达真实实验室流程、报告输出、样本周转时间和前瞻性验证。"
      : "临床价值上，目前更像方法或资源储备，需要再判断能否转成真实诊断或监测流程。",
  ].map((item) => `- ${item}`).join("\n");

  const followups = [
    "- 这批论文里哪篇最适合做知识库或 benchmark 基座？",
    "- 哪篇工作最容易接入 agent / report generation / clinical copilot？",
    "- 蛋白质、基因、临床三个维度分别能提炼出哪些可追踪方向？",
  ].join("\n");

  return [
    "## 结论",
    `最相关的是 **${top.title}**。它与当前问题在语义和关键词上都更接近，并且在 **${top.matched_topics.join("、") || "当前主题"}** 维度上信号最强。`,
    "",
    "## 回答范围",
    scope,
    "",
    "## 证据",
    evidence,
    "",
    "## 深入解读",
    interpretation,
    "",
    "## 建议继续追问",
    followups,
  ].join("\n");
}

function buildContextForRemote(hits, selectedPaper, query) {
  const selectedBlock = selectedPaper
    ? `当前焦点论文：\n标题：${selectedPaper.title}\n来源：${selectedPaper.source}\n分类：${selectedPaper.category}\n主题：${selectedPaper.matched_topics.join(", ")}\n摘要：${selectedPaper.abstract}\n为什么重要：${selectedPaper.why_it_matters}`
    : "当前没有焦点论文。";

  const hitBlocks = hits.map((hit, index) => [
    `[候选 ${index + 1}]`,
    `标题：${hit.title}`,
    `来源：${hit.source}`,
    `日期：${hit.date}`,
    `分类：${hit.category}`,
    `主题：${hit.matched_topics.join(", ")}`,
    `摘要：${hit.abstract}`,
    `为什么重要：${hit.why_it_matters}`,
    `得分：${hit.score.toFixed(3)}`,
  ].join("\n")).join("\n\n");

  return {
    system: "你是病原生信、蛋白质/基因组学、临床微生物学与AI/LLM/Agent交叉领域的研究助手。必须只根据给定上下文回答，用中文输出，结构清晰，解释具体，不要编造未提供的论文信息。",
    user: [
      `用户问题：${query}`,
      "",
      selectedBlock,
      "",
      "召回候选论文：",
      hitBlocks,
      "",
      "请按以下结构回答：1. 结论 2. 与 protein/gene/clinical/AI-LLM-Agent 的关系 3. 最相关论文逐篇解读 4. 风险与不足 5. 下一步建议。",
    ].join("\n"),
  };
}

function retrieveCandidates(query) {
  const dimensions = state.embeddings.dimensions || 256;
  const queryVector = localEmbed(query, dimensions);
  const selected = getSelectedPaper();
  return state.papers
    .map((paper) => {
      const semantic = cosine(queryVector, paper.embedding || []);
      const lexical = lexicalScore(query, paper.search_text || "");
      const focusBoost = selected && selected.paper_id === paper.paper_id ? 0.08 : 0;
      const favoriteBoost = state.favorites[paper.paper_id] ? 0.04 : 0;
      const score = semantic * 0.58 + lexical * 0.26 + focusBoost + favoriteBoost + paper.importance_score * 0.02;
      return { ...paper, score, semantic, lexical };
    })
    .sort((a, b) => b.score - a.score)
    .slice(0, 6);
}

async function answerWithRemoteLlm(query, hits, selectedPaper) {
  if (!state.llm.apiKey || !state.llm.baseUrl || !state.llm.model) {
    throw new Error("外接 LLM 需要先填写 Base URL、Model 和 API Key");
  }
  const prompt = buildContextForRemote(hits, selectedPaper, query);
  const response = await fetch(`${state.llm.baseUrl.replace(/\/$/, "")}/chat/completions`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${state.llm.apiKey}`,
    },
    body: JSON.stringify({
      model: state.llm.model,
      temperature: 0.2,
      messages: [
        { role: "system", content: prompt.system },
        { role: "user", content: prompt.user },
      ],
    }),
  });
  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`LLM 请求失败：${response.status} ${errorText}`);
  }
  const payload = await response.json();
  return payload.choices?.[0]?.message?.content?.trim() || "外接 LLM 没有返回内容。";
}

function renderAll() {
  applyFilters();
  renderHero();
  renderGroups();
  renderTreeList(treeSourceEl, "source");
  renderTreeList(treeTopicEl, "topic");
  renderTreeList(treeYearEl, "year");
  renderPaperList();
  renderDetail();
}

function debounce(fn, delay = 400) {
  let timer = null;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}

async function submitQuestion(query) {
  const selected = getSelectedPaper();
  const hits = retrieveCandidates(query);
  if (state.llm.mode === "remote") {
    const markdown = await answerWithRemoteLlm(query, hits, selected);
    return markdownToHtml(markdown);
  }
  return markdownToHtml(buildDetailedAnswerMarkdown(query, hits, selected));
}

function loadPreferences() {
  state.favorites = loadJson("favorites", {});
  state.notes = loadJson("notes", {});
  state.llm = { ...state.llm, ...loadJson("llm", {}) };
  llmModeEl.value = state.llm.mode;
  llmBaseUrlEl.value = state.llm.baseUrl;
  llmModelEl.value = state.llm.model;
  llmApiKeyEl.value = state.llm.apiKey;
}

function persistLlmSettings() {
  state.llm.mode = llmModeEl.value;
  state.llm.baseUrl = llmBaseUrlEl.value.trim();
  state.llm.model = llmModelEl.value.trim();
  state.llm.apiKey = llmApiKeyEl.value.trim();
  saveJson("llm", state.llm);
}

async function bootstrap() {
  loadPreferences();
  const response = await fetch(bundleUrl, { cache: "no-store" });
  const bundle = await response.json();
  state.papers = bundle.papers || [];
  state.filtered = [...state.papers];
  state.summary = bundle.summary || {};
  state.digest = bundle.digest_markdown || "";
  state.embeddings = bundle.embedding || {};
  state.selectedPaperId = state.papers[0]?.paper_id || null;

  populateFilters();
  renderAll();
}

[searchInput, topicFilter, sourceFilter, categoryFilter].forEach((el) => {
  el.addEventListener("input", renderAll);
  el.addEventListener("change", renderAll);
});

favoriteToggleEl.addEventListener("click", () => {
  const paper = getSelectedPaper();
  if (!paper) return;
  state.favorites[paper.paper_id] = !state.favorites[paper.paper_id];
  saveJson("favorites", state.favorites);
  renderAll();
});

notesInputEl.addEventListener("input", debounce(() => {
  const paper = getSelectedPaper();
  if (!paper) return;
  state.notes[paper.paper_id] = notesInputEl.value.trim();
  saveJson("notes", state.notes);
  notesStatusEl.textContent = "已保存到浏览器本地";
}, 300));

[llmModeEl, llmBaseUrlEl, llmModelEl, llmApiKeyEl].forEach((el) => {
  el.addEventListener("input", persistLlmSettings);
  el.addEventListener("change", persistLlmSettings);
});

askForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const query = questionInput.value.trim();
  if (!query) return;
  askStatus.textContent = state.llm.mode === "remote" ? "正在调用外接 LLM" : "正在生成详细解读";
  try {
    answerBody.innerHTML = await submitQuestion(query);
    answerCard.classList.remove("hidden");
    askStatus.textContent = state.llm.mode === "remote" ? "已使用外接 LLM 回答" : "已结合当前论文和知识库生成详细解读";
  } catch (error) {
    answerBody.innerHTML = markdownToHtml(`## 出错\n${error.message}`);
    answerCard.classList.remove("hidden");
    askStatus.textContent = "请求失败";
  }
});

bootstrap().catch((error) => {
  digestPreviewEl.innerHTML = markdownToHtml(`加载失败：${error.message}`);
});
