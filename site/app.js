const bundleUrl = "./data/site_bundle.json";

const state = {
  papers: [],
  filtered: [],
  summary: {},
  digest: "",
  embeddings: { dimensions: 0 },
};

const heroStatsEl = document.querySelector("#hero-stats");
const digestPreviewEl = document.querySelector("#digest-preview");
const paperGridEl = document.querySelector("#paper-grid");
const paperTemplate = document.querySelector("#paper-template");
const searchInput = document.querySelector("#search-input");
const topicFilter = document.querySelector("#topic-filter");
const sourceFilter = document.querySelector("#source-filter");
const categoryFilter = document.querySelector("#category-filter");
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

function escapeHtml(value) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;");
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
    .slice(0, 4)
    .map(([key, value]) => `${key} ${value}`);

  heroStatsEl.innerHTML = "";
  [
    `累计论文 ${state.summary.total_papers || 0}`,
    `最近新增 ${state.summary.last_run_count || 0}`,
    ...sources.slice(0, 3),
    ...topics,
  ].forEach((item) => {
    const tag = document.createElement("span");
    tag.textContent = item;
    heroStatsEl.appendChild(tag);
  });

  digestPreviewEl.textContent = state.digest.slice(0, 1100) || "暂无摘要。";
}

function applyFilters() {
  const q = searchInput.value.trim().toLowerCase();
  const topic = topicFilter.value;
  const source = sourceFilter.value;
  const category = categoryFilter.value;

  state.filtered = state.papers.filter((paper) => {
    const haystack = [
      paper.title,
      paper.abstract,
      paper.why_it_matters,
      paper.category,
      ...paper.matched_topics,
    ]
      .join("\n")
      .toLowerCase();

    if (q && !haystack.includes(q)) return false;
    if (topic && !paper.matched_topics.includes(topic)) return false;
    if (source && paper.source !== source) return false;
    if (category && paper.category !== category) return false;
    return true;
  });

  renderPapers();
}

function renderPapers() {
  paperGridEl.innerHTML = "";
  for (const paper of state.filtered) {
    const node = paperTemplate.content.firstElementChild.cloneNode(true);
    node.querySelector(".paper-meta").textContent = `${paper.source} / ${paper.date.slice(0, 10)} / ${paper.category}`;
    node.querySelector(".paper-title").textContent = paper.title;
    node.querySelector(".paper-summary").textContent = paper.why_it_matters;
    node.querySelector(".paper-scores").textContent = `importance ${paper.importance_score} | relevance ${paper.relevance_score} | seen ${paper.times_seen}`;
    const link = node.querySelector(".paper-link");
    link.href = paper.url;
    const tags = node.querySelector(".paper-tags");
    paper.matched_topics.forEach((topic) => {
      const chip = document.createElement("span");
      chip.textContent = topic;
      tags.appendChild(chip);
    });
    paperGridEl.appendChild(node);
  }
}

function answerQuestion(query) {
  const dimensions = state.embeddings.dimensions || 256;
  const queryVector = localEmbed(query, dimensions);
  const hits = state.papers
    .map((paper) => {
      const semantic = cosine(queryVector, paper.embedding || []);
      const lexical = lexicalScore(query, paper.search_text || "");
      const score = semantic * 0.7 + lexical * 0.3;
      return { ...paper, score, semantic, lexical };
    })
    .sort((a, b) => b.score - a.score)
    .slice(0, 4);

  const top = hits[0];
  const summary = top
    ? `最相关的是《${top.title}》，它更偏 ${top.category}，主要因为命中了 ${top.matched_topics.join("、") || "相关主题"}，并且在摘要或说明中与问题的关键词重叠较高。`
    : "当前知识库里没有明显相关的论文。";

  const bullets = hits
    .map(
      (hit) =>
        `<li><a href="${hit.url}" target="_blank" rel="noreferrer">${escapeHtml(hit.title)}</a>｜${escapeHtml(hit.source)}｜score ${hit.score.toFixed(3)}<br>${escapeHtml(hit.why_it_matters)}</li>`,
    )
    .join("");

  return `
    <p>${escapeHtml(summary)}</p>
    <p>建议继续追踪：</p>
    <ul>${bullets}</ul>
  `;
}

async function bootstrap() {
  const response = await fetch(bundleUrl, { cache: "no-store" });
  const bundle = await response.json();
  state.papers = bundle.papers || [];
  state.filtered = [...state.papers];
  state.summary = bundle.summary || {};
  state.digest = bundle.digest_markdown || "";
  state.embeddings = bundle.embedding || {};

  populateFilters();
  renderHero();
  renderPapers();
}

[searchInput, topicFilter, sourceFilter, categoryFilter].forEach((el) => {
  el.addEventListener("input", applyFilters);
  el.addEventListener("change", applyFilters);
});

askForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const query = questionInput.value.trim();
  if (!query) return;
  askStatus.textContent = "正在检索";
  const html = answerQuestion(query);
  answerBody.innerHTML = html;
  answerCard.classList.remove("hidden");
  askStatus.textContent = `已基于 ${Math.min(4, state.papers.length)} 篇候选论文回答`;
});

bootstrap().catch((error) => {
  digestPreviewEl.textContent = `加载失败：${error.message}`;
});
