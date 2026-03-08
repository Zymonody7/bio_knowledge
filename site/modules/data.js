import { BUNDLE_URL } from "./config.js";
import { state } from "./state.js";

export async function loadBundle() {
  const response = await fetch(BUNDLE_URL, { cache: "no-store" });
  const bundle = await response.json();
  state.papers = bundle.papers || [];
  state.filtered = [...state.papers];
  state.summary = bundle.summary || {};
  state.digest = bundle.digest_markdown || "";
  state.embeddings = bundle.embedding || {};
  state.llmDefaults = {
    ...state.llmDefaults,
    baseUrl: bundle.llm_defaults?.base_url || state.llmDefaults.baseUrl,
    model: bundle.llm_defaults?.model || state.llmDefaults.model,
  };
  state.selectedPaperId = state.papers[0]?.paper_id || null;
}
