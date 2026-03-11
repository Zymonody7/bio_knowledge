import { loadBundle } from "./data.js";
import { dom } from "./dom.js";
import { applyFilters, populateFilters } from "./filters.js";
import { loadPreferences, persistFavorites, persistLlmSettings, persistNotes } from "./preferences.js";
import { renderDetail, renderGroups, renderHero, renderPaperList, renderTrees } from "./render.js";
import { state } from "./state.js";
import { containWheelScroll, debounce } from "./utils.js";
import { submitQuestion } from "./chat.js";


function renderAll() {
  applyFilters();
  renderHero();
  renderGroups((group) => {
    state.activeGroup = group;
    renderAll();
  });
  renderTrees((kind, value) => {
    state.treeFilter = kind ? { kind, value } : { kind: "", value: "" };
    renderAll();
  });
  renderPaperList((paperId) => {
    state.selectedPaperId = paperId;
    renderPaperList((nextPaperId) => {
      state.selectedPaperId = nextPaperId;
      renderDetail();
    });
    renderDetail();
  });
  renderDetail();
}

function bindEvents() {
  [dom.digestPreview, dom.paperList, dom.notesInput].forEach((element) => containWheelScroll(element));

  [dom.searchInput, dom.sortFilter, dom.topicFilter, dom.sourceFilter, dom.categoryFilter].forEach((element) => {
    element.addEventListener("input", renderAll);
    element.addEventListener("change", renderAll);
  });

  dom.favoriteToggle.addEventListener("click", () => {
    const current = state.selectedPaperId;
    if (!current) return;
    state.favorites[current] = !state.favorites[current];
    persistFavorites();
    renderAll();
  });

  dom.notesInput.addEventListener("input", debounce(() => {
    const current = state.selectedPaperId;
    if (!current) return;
    state.notes[current] = dom.notesInput.value.trim();
    persistNotes();
    dom.notesStatus.textContent = "已保存到浏览器本地";
  }, 300));

  [dom.llmMode, dom.llmBaseUrl, dom.llmModel, dom.llmApiKey].forEach((element) => {
    element.addEventListener("input", persistLlmSettings);
    element.addEventListener("change", persistLlmSettings);
  });

  dom.askForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const query = dom.questionInput.value.trim();
    if (!query) return;
    dom.askStatus.textContent = state.llm.mode === "remote" ? "正在调用外接 LLM" : "正在生成详细解读";
    try {
      dom.answerBody.innerHTML = await submitQuestion(query);
      dom.answerCard.classList.remove("hidden");
      dom.askStatus.textContent = state.llm.mode === "remote" ? "已使用外接 LLM 回答" : "已结合当前论文和知识库生成详细解读";
    } catch (error) {
      dom.answerBody.innerHTML = `<div class="markdown-body"><h2>出错</h2><p>${error.message}</p></div>`;
      dom.answerCard.classList.remove("hidden");
      dom.askStatus.textContent = "请求失败";
    }
  });
}

export async function bootstrap() {
  try {
    await loadBundle();
    loadPreferences();
    populateFilters();
    bindEvents();
    renderAll();
  } catch (error) {
    dom.digestPreview.innerHTML = `<div class="markdown-body"><p>加载失败：${error.message}</p></div>`;
  }
}
