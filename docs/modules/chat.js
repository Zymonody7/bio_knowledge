import { buildContextForRemote, buildDetailedAnswerMarkdown } from "./analysis.js";
import { markdownToHtml } from "./markdown.js";
import { state } from "./state.js";
import { getSelectedPaper } from "./selectors.js";
import { cosine, lexicalScore, localEmbed } from "./retrieval.js";

export function retrieveCandidates(query) {
  const dimensions = state.embeddings.dimensions || 256;
  const queryVector = localEmbed(query, dimensions);
  const selected = getSelectedPaper();
  return state.papers
    .map((paper) => {
      const semantic = cosine(queryVector, paper.embedding || []);
      const lexical = lexicalScore(query, paper.search_text || "");
      const focusBoost = selected && selected.paper_id === paper.paper_id ? 0.08 : 0;
      const favoriteBoost = state.favorites[paper.paper_id] ? 0.04 : 0;
      const score = semantic * 0.58 + lexical * 0.26 + focusBoost + favoriteBoost + paper.importance_score * 0.02;
      return { ...paper, score, semantic, lexical };
    })
    .sort((left, right) => right.score - left.score)
    .slice(0, 6);
}

export async function answerWithRemoteLlm(query, hits, selectedPaper) {
  if (!state.llm.apiKey || !state.llm.baseUrl || !state.llm.model) {
    throw new Error("外接 LLM 需要先填写 Base URL、Model 和 API Key");
  }
  const prompt = buildContextForRemote(query, hits, selectedPaper);
  const response = await fetch(`${state.llm.baseUrl.replace(/\/$/, "")}/chat/completions`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${state.llm.apiKey}`,
    },
    body: JSON.stringify({
      model: state.llm.model,
      temperature: 0.2,
      messages: [
        { role: "system", content: prompt.system },
        { role: "user", content: prompt.user },
      ],
    }),
  });
  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`LLM 请求失败：${response.status} ${errorText}`);
  }
  const payload = await response.json();
  return payload.choices?.[0]?.message?.content?.trim() || "外接 LLM 没有返回内容。";
}

export async function submitQuestion(query) {
  const selectedPaper = getSelectedPaper();
  const hits = retrieveCandidates(query);
  if (state.llm.mode === "remote") {
    const markdown = await answerWithRemoteLlm(query, hits, selectedPaper);
    return markdownToHtml(markdown);
  }
  return markdownToHtml(buildDetailedAnswerMarkdown(query, hits, selectedPaper));
}
