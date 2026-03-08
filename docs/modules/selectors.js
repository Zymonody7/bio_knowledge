import { state } from "./state.js";

export function getSelectedPaper() {
  return state.papers.find((paper) => paper.paper_id === state.selectedPaperId) || null;
}

export function paperLabel(paper) {
  return `${paper.source} / ${paper.date.slice(0, 10)} / ${paper.category}`;
}

export function visiblePapers() {
  const base = state.activeGroup === "__favorites__"
    ? state.filtered.filter((paper) => state.favorites[paper.paper_id])
    : state.activeGroup
      ? state.filtered.filter((paper) => paper.category === state.activeGroup)
      : state.filtered;
  return base;
}
