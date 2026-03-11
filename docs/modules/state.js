export const state = {
  papers: [],
  filtered: [],
  summary: {},
  digest: "",
  embeddings: { dimensions: 0 },
  llmDefaults: {
    baseUrl: "https://api.openai.com/v1",
    model: "gpt-4.1-mini",
  },
  selectedPaperId: null,
  activeGroup: "",
  treeFilter: { kind: "", value: "" },
  sortBy: "importance",
  favorites: {},
  notes: {},
  llm: {
    mode: "local",
    baseUrl: "",
    model: "",
    apiKey: "",
  },
};
