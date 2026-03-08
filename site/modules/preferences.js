import { dom } from "./dom.js";
import { state } from "./state.js";
import { loadJson, saveJson } from "./storage.js";

export function loadPreferences() {
  state.favorites = loadJson("favorites", {});
  state.notes = loadJson("notes", {});
  state.llm = { ...state.llm, ...loadJson("llm", {}) };
  dom.llmMode.value = state.llm.mode;
  dom.llmBaseUrl.value = state.llm.baseUrl;
  dom.llmModel.value = state.llm.model;
  dom.llmApiKey.value = state.llm.apiKey;
}

export function persistLlmSettings() {
  state.llm.mode = dom.llmMode.value;
  state.llm.baseUrl = dom.llmBaseUrl.value.trim();
  state.llm.model = dom.llmModel.value.trim();
  state.llm.apiKey = dom.llmApiKey.value.trim();
  saveJson("llm", state.llm);
}

export function persistFavorites() {
  saveJson("favorites", state.favorites);
}

export function persistNotes() {
  saveJson("notes", state.notes);
}
