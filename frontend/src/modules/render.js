import { dom } from "./dom.js";
import { state } from "./state.js";
import { markdownToHtml } from "./markdown.js";
import { detailAnalysisMarkdown } from "./analysis.js";
import { getSelectedPaper, paperLabel, visiblePapers } from "./selectors.js";

export function renderHero() {
  const sources = Object.entries(state.summary.sources || {}).map(([key, value]) => `${key} ${value}`);
  const topics = Object.entries(state.summary.topics || {})
    .sort((left, right) => right[1] - left[1])
    .slice(0, 5)
    .map(([key, value]) => `${key} ${value}`);
  const favoriteCount = Object.values(state.favorites).filter(Boolean).length;

  dom.heroStats.innerHTML = "";
  [`累计论文 ${state.summary.total_papers || 0}`, `最近新增 ${state.summary.last_run_count || 0}`, `收藏 ${favoriteCount}`, ...sources.slice(0, 3), ...topics].forEach((item) => {
    const tag = document.createElement("span");
    tag.textContent = item;
    dom.heroStats.appendChild(tag);
  });

  dom.digestPreview.innerHTML = markdownToHtml(state.digest.slice(0, 1800) || "暂无摘要。");
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

export function renderGroups(onSelect) {
  dom.groupList.innerHTML = "";
  buildGroups().forEach(([key, group]) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = `group-pill${state.activeGroup === key ? " active" : ""}`;
    button.textContent = `${group.label} ${group.count}`;
    button.addEventListener("click", () => onSelect(key));
    dom.groupList.appendChild(button);
  });
}

function buildTreeCounts(kind) {
  const counts = new Map();
  for (const paper of state.filtered) {
    if (kind === "source") counts.set(paper.source, (counts.get(paper.source) || 0) + 1);
    else if (kind === "year") counts.set(paper.date.slice(0, 4) || "unknown", (counts.get(paper.date.slice(0, 4) || "unknown") || 0) + 1);
    else paper.matched_topics.forEach((topic) => counts.set(topic, (counts.get(topic) || 0) + 1));
  }
  return [...counts.entries()].sort((left, right) => right[1] - left[1] || left[0].localeCompare(right[0]));
}

function renderTreeList(target, kind, onSelect) {
  target.innerHTML = "";
  const allButton = document.createElement("button");
  allButton.type = "button";
  allButton.className = `tree-item${state.treeFilter.kind === kind && !state.treeFilter.value ? " active" : ""}`;
  allButton.textContent = "全部";
  allButton.addEventListener("click", () => onSelect("", ""));
  target.appendChild(allButton);

  buildTreeCounts(kind).forEach(([value, count]) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = `tree-item${state.treeFilter.kind === kind && state.treeFilter.value === value ? " active" : ""}`;
    button.textContent = `${value} ${count}`;
    button.addEventListener("click", () => onSelect(kind, value));
    target.appendChild(button);
  });
}

export function renderTrees(onSelect) {
  renderTreeList(dom.treeSource, "source", onSelect);
  renderTreeList(dom.treeTopic, "topic", onSelect);
  renderTreeList(dom.treeYear, "year", onSelect);
}

export function renderPaperList(onSelect) {
  dom.paperList.innerHTML = "";
  const visible = visiblePapers();
  dom.paperCount.textContent = `${visible.length} 篇`;

  visible.forEach((paper) => {
    const node = dom.paperItemTemplate.content.firstElementChild.cloneNode(true);
    node.classList.toggle("active", paper.paper_id === state.selectedPaperId);
    node.querySelector(".paper-item-meta").textContent = paperLabel(paper);
    node.querySelector(".paper-item-title").textContent = `${state.favorites[paper.paper_id] ? "★ " : ""}${paper.title}`;
    const tags = node.querySelector(".paper-item-tags");
    [paper.source, ...paper.matched_topics.slice(0, 2)].forEach((tag) => {
      const chip = document.createElement("span");
      chip.textContent = tag;
      tags.appendChild(chip);
    });
    node.addEventListener("click", () => onSelect(paper.paper_id));
    dom.paperList.appendChild(node);
  });
}

export function renderDetail() {
  const paper = getSelectedPaper();
  if (!paper) {
    dom.detailMeta.textContent = "";
    dom.detailTitle.textContent = "当前没有符合筛选条件的论文";
    dom.detailLink.href = "#";
    dom.detailTags.innerHTML = "";
    dom.detailWhy.innerHTML = markdownToHtml("可以放宽左侧过滤条件，或者直接在右下角提问知识库。");
    dom.detailAbstractZh.innerHTML = "";
    dom.detailAbstract.innerHTML = "";
    dom.notesInput.value = "";
    dom.favoriteToggle.textContent = "收藏";
    return;
  }

  dom.detailMeta.textContent = paperLabel(paper);
  dom.detailTitle.textContent = paper.title;
  dom.detailLink.href = paper.url;
  dom.detailImportance.textContent = paper.importance_score;
  dom.detailRelevance.textContent = paper.relevance_score;
  dom.detailNovelty.textContent = paper.novelty_score;
  dom.detailTimesSeen.textContent = paper.times_seen;
  dom.detailTags.innerHTML = "";
  [...paper.matched_topics, `source:${paper.source}`, `category:${paper.category}`].forEach((tag) => {
    const chip = document.createElement("span");
    chip.textContent = tag;
    dom.detailTags.appendChild(chip);
  });

  dom.favoriteToggle.textContent = state.favorites[paper.paper_id] ? "取消收藏" : "收藏";
  dom.notesInput.value = state.notes[paper.paper_id] || "";
  dom.detailWhy.innerHTML = markdownToHtml(detailAnalysisMarkdown(paper, state.notes));
  dom.detailAbstractZh.innerHTML = markdownToHtml(paper.abstract_zh || "当前还没有生成中文摘要。");
  dom.detailAbstract.innerHTML = markdownToHtml(paper.abstract || "暂无原始摘要。");
}
