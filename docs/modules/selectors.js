import { state } from "./state.js";

export function getSelectedPaper() {
  return state.papers.find((paper) => paper.paper_id === state.selectedPaperId) || null;
}

export function paperLabel(paper) {
  return `${paper.source} / ${paper.date.slice(0, 10)} / rel ${paper.relevance_score} / nov ${paper.novelty_score}`;
}

export function visiblePapers() {
  const base = state.activeGroup === "__favorites__"
    ? state.filtered.filter((paper) => state.favorites[paper.paper_id])
    : state.activeGroup
      ? state.filtered.filter((paper) => paper.category === state.activeGroup)
      : state.filtered;

  const sorted = [...base];
  sorted.sort((left, right) => {
    switch (state.sortBy) {
      case "date_desc":
        return right.date.localeCompare(left.date) || right.importance_score - left.importance_score;
      case "date_asc":
        return left.date.localeCompare(right.date) || right.importance_score - left.importance_score;
      case "relevance_desc":
        return right.relevance_score - left.relevance_score || right.novelty_score - left.novelty_score || right.date.localeCompare(left.date);
      case "novelty_desc":
        return right.novelty_score - left.novelty_score || right.relevance_score - left.relevance_score || right.date.localeCompare(left.date);
      case "importance":
      default:
        return right.importance_score - left.importance_score || right.relevance_score - left.relevance_score || right.date.localeCompare(left.date);
    }
  });
  return sorted;
}
