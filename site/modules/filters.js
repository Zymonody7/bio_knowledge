import { state } from "./state.js";
import { dom } from "./dom.js";

export function populateFilters() {
  const topics = new Set();
  const sources = new Set();
  const categories = new Set();

  for (const paper of state.papers) {
    paper.matched_topics.forEach((topic) => topics.add(topic));
    if (paper.source) sources.add(paper.source);
    if (paper.category) categories.add(paper.category);
  }

  for (const [select, items] of [
    [dom.topicFilter, [...topics].sort()],
    [dom.sourceFilter, [...sources].sort()],
    [dom.categoryFilter, [...categories].sort()],
  ]) {
    for (const item of items) {
      const option = document.createElement("option");
      option.value = item;
      option.textContent = item;
      select.appendChild(option);
    }
  }
}

export function applyFilters() {
  const query = dom.searchInput.value.trim().toLowerCase();
  state.sortBy = dom.sortFilter.value || "importance";
  const topic = dom.topicFilter.value;
  const source = dom.sourceFilter.value;
  const category = dom.categoryFilter.value;

  state.filtered = state.papers.filter((paper) => {
    const haystack = [
      paper.title,
      paper.abstract,
      paper.abstract_zh,
      paper.analysis_zh,
      paper.why_it_matters,
      paper.category,
      paper.source,
      ...paper.matched_topics,
    ].join("\n").toLowerCase();
    if (query && !haystack.includes(query)) return false;
    if (topic && !paper.matched_topics.includes(topic)) return false;
    if (source && paper.source !== source) return false;
    if (category && paper.category !== category) return false;
    if (state.treeFilter.kind === "source" && state.treeFilter.value && paper.source !== state.treeFilter.value) return false;
    if (state.treeFilter.kind === "year" && state.treeFilter.value && !paper.date.startsWith(state.treeFilter.value)) return false;
    if (state.treeFilter.kind === "topic" && state.treeFilter.value && !paper.matched_topics.includes(state.treeFilter.value)) return false;
    return true;
  });

  const selectedStillVisible = state.filtered.some((paper) => paper.paper_id === state.selectedPaperId);
  if (!selectedStillVisible) state.selectedPaperId = state.filtered[0]?.paper_id || null;
}
