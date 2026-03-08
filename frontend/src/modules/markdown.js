import { escapeHtml } from "./utils.js";

export function markdownToHtml(markdown = "") {
  let html = escapeHtml(markdown);
  html = html.replace(/\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g, '<a href="$2" target="_blank" rel="noreferrer">$1</a>');
  html = html.replace(/^### (.*)$/gm, "<h3>$1</h3>");
  html = html.replace(/^## (.*)$/gm, "<h2>$1</h2>");
  html = html.replace(/^# (.*)$/gm, "<h1>$1</h1>");
  html = html.replace(/^> (.*)$/gm, "<blockquote>$1</blockquote>");
  html = html.replace(/`([^`]+)`/g, "<code>$1</code>");
  html = html.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  html = html.replace(/\n- (.*?)(?=\n|$)/g, "\n<li>$1</li>");
  html = html.replace(/\n\d+\. (.*?)(?=\n|$)/g, "\n<li>$1</li>");
  html = html.replace(/(<li>.*?<\/li>)/gs, "<ul>$1</ul>");
  html = html.replace(/\n{2,}/g, "</p><p>");
  html = `<p>${html}</p>`;
  html = html.replace(/<p><h/g, "<h").replace(/<\/h([1-3])><\/p>/g, "</h$1>");
  html = html.replace(/<p><ul>/g, "<ul>").replace(/<\/ul><\/p>/g, "</ul>");
  html = html.replace(/<p><blockquote>/g, "<blockquote>").replace(/<\/blockquote><\/p>/g, "</blockquote>");
  html = html.replace(/<p><\/p>/g, "");
  return html;
}
