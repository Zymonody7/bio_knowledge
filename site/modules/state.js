export const state = {
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
