export const tokenize = (text) => (text.toLowerCase().match(/[a-zA-Z0-9_+-]{2,}/g) || []);

export function escapeHtml(value = "") {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;");
}

export function debounce(fn, delay = 400) {
  let timer = null;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}

export function containWheelScroll(element) {
  if (!element) return;
  element.addEventListener(
    "wheel",
    (event) => {
      const { deltaY } = event;
      const maxScrollTop = element.scrollHeight - element.clientHeight;
      const atTop = element.scrollTop <= 0;
      const atBottom = element.scrollTop >= maxScrollTop - 1;
      const canScroll = maxScrollTop > 0;

      if (!canScroll) {
        event.preventDefault();
        return;
      }

      if ((deltaY < 0 && atTop) || (deltaY > 0 && atBottom)) {
        event.preventDefault();
      }
    },
    { passive: false },
  );
}
