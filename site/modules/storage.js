import { STORAGE_PREFIX } from "./config.js";

export function saveJson(key, value) {
  localStorage.setItem(`${STORAGE_PREFIX}:${key}`, JSON.stringify(value));
}

export function loadJson(key, fallback) {
  try {
    const raw = localStorage.getItem(`${STORAGE_PREFIX}:${key}`);
    return raw ? JSON.parse(raw) : fallback;
  } catch {
    return fallback;
  }
}
