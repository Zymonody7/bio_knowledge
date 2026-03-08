import { tokenize } from "./utils.js";

export function cosine(left, right) {
  if (!left?.length || !right?.length || left.length !== right.length) return 0;
  let score = 0;
  for (let index = 0; index < left.length; index += 1) score += left[index] * right[index];
  return score;
}

export function localEmbed(text, dimensions) {
  const vec = new Array(dimensions).fill(0);
  const tokens = tokenize(text);
  for (const token of tokens) {
    let hash = 2166136261;
    for (let index = 0; index < token.length; index += 1) {
      hash ^= token.charCodeAt(index);
      hash = Math.imul(hash, 16777619);
    }
    const outputIndex = Math.abs(hash) % dimensions;
    const sign = hash % 2 === 0 ? 1 : -1;
    vec[outputIndex] += sign * (1 + Math.min(token.length, 12) / 12);
  }
  const norm = Math.sqrt(vec.reduce((acc, value) => acc + value * value, 0));
  return norm === 0 ? vec : vec.map((value) => value / norm);
}

export function lexicalScore(query, text) {
  const queryTokens = new Set(tokenize(query));
  const textTokens = new Set(tokenize(text));
  if (!queryTokens.size || !textTokens.size) return 0;
  let overlap = 0;
  for (const token of queryTokens) {
    if (textTokens.has(token)) overlap += 1;
  }
  return overlap / queryTokens.size;
}
