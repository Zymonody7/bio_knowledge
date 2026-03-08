export function detailAnalysisMarkdown(paper, notes) {
  const intersections = [];
  if (/protein|proteomics|nanobody/i.test(`${paper.title} ${paper.abstract}`)) intersections.push("protein / proteomics");
  if (/gene|genomic|genomics|transcript/i.test(`${paper.title} ${paper.abstract}`)) intersections.push("gene / genomics");
  if (/clinical|patient|diagnosis|microbiology/i.test(`${paper.title} ${paper.abstract}`)) intersections.push("clinical / microbiology");
  if (/agent|llm|language model|foundation model|multimodal/i.test(`${paper.title} ${paper.abstract}`)) intersections.push("AI / LLM / Agent");

  return [
    `**来源**：${paper.source}`,
    `**为什么值得看**：${paper.why_it_matters}`,
    `**与你的研究交叉点**：${intersections.length ? intersections.join("、") : "当前更偏传统生信/病原方向，但可以继续判断是否能接到 AI workflow。"}`,
    `**建议重点读**：数据类型、蛋白质/基因层信号、临床样本设置、是否存在 agent/llm 可切入点、评价指标是否贴近真实流程。`,
    notes[paper.paper_id] ? `**你的备注**：${notes[paper.paper_id]}` : "",
  ].filter(Boolean).join("\n\n");
}

export function buildDetailedAnswerMarkdown(query, hits, selectedPaper) {
  if (!hits.length) {
    return "## 结论\n当前知识库里没有明显相关的论文。\n\n## 建议\n- 放宽限定词\n- 改问 protein / gene / clinical / agent / llm 等核心轴线\n- 也可以直接点左侧分类树查看最近论文";
  }

  const top = hits[0];
  const scope = selectedPaper
    ? `当前焦点论文是 **${selectedPaper.title}**。下面会优先对照它，再补充整个知识库中的相近论文。`
    : "当前未锁定具体论文，下面基于整个知识库回答。";

  const evidence = hits.slice(0, 4).map((hit, index) => [
    `${index + 1}. **${hit.title}**`,
    `   - 来源：${hit.source}｜日期：${hit.date.slice(0, 10)}｜类别：${hit.category}`,
    `   - 匹配主题：${hit.matched_topics.join("、") || "无"}`,
    `   - 检索得分：semantic=${hit.semantic.toFixed(3)} / lexical=${hit.lexical.toFixed(3)} / final=${hit.score.toFixed(3)}`,
    `   - 解释：${hit.why_it_matters}`,
  ].join("\n")).join("\n");

  const interpretation = [
    top.matched_topics.includes("foundation_model_agent")
      ? "这批结果里已经出现了和 AI / LLM / Agent 更接近的信号，值得继续判断它们是否只是提及模型，还是已经进入任务设计、评测和自动化 workflow。"
      : "这批结果更偏病原生信和临床监测本体，AI/LLM/Agent 结合点可能还需要你再问更具体的问题，例如 `protein language model`、`clinical agent`、`genomics rag`。",
    /protein|proteomics|nanobody/i.test(`${top.title} ${top.abstract}`)
      ? "从蛋白质角度看，这批结果可能适合延展到 protein foundation model、结构功能预测或抗原/抗体相关任务。"
      : "从蛋白质角度看，当前召回里强信号还不够，可以继续追踪 protein language model、proteomics biomarker 和 host-pathogen protein interaction。",
    /gene|genomic|transcript/i.test(`${top.title} ${top.abstract}`)
      ? "从基因/组学角度看，这批结果更容易接到 gene regulation、variant interpretation、clinical genomics pipeline。"
      : "从基因/组学角度看，建议再搜 host response transcriptomics、gene function prediction、clinical genomics agent。",
    top.category === "clinical_application"
      ? "临床价值上，重点看它是否触达真实实验室流程、报告输出、样本周转时间和前瞻性验证。"
      : "临床价值上，目前更像方法或资源储备，需要再判断能否转成真实诊断或监测流程。",
  ].map((item) => `- ${item}`).join("\n");

  const followups = [
    "- 这批论文里哪篇最适合做知识库或 benchmark 基座？",
    "- 哪篇工作最容易接入 agent / report generation / clinical copilot？",
    "- 蛋白质、基因、临床三个维度分别能提炼出哪些可追踪方向？",
  ].join("\n");

  return [
    "## 结论",
    `最相关的是 **${top.title}**。它与当前问题在语义和关键词上都更接近，并且在 **${top.matched_topics.join("、") || "当前主题"}** 维度上信号最强。`,
    "",
    "## 回答范围",
    scope,
    "",
    "## 证据",
    evidence,
    "",
    "## 深入解读",
    interpretation,
    "",
    "## 建议继续追问",
    followups,
  ].join("\n");
}

export function buildContextForRemote(query, hits, selectedPaper) {
  const selectedBlock = selectedPaper
    ? `当前焦点论文：\n标题：${selectedPaper.title}\n来源：${selectedPaper.source}\n分类：${selectedPaper.category}\n主题：${selectedPaper.matched_topics.join(", ")}\n摘要：${selectedPaper.abstract}\n为什么重要：${selectedPaper.why_it_matters}`
    : "当前没有焦点论文。";

  const hitBlocks = hits.map((hit, index) => [
    `[候选 ${index + 1}]`,
    `标题：${hit.title}`,
    `来源：${hit.source}`,
    `日期：${hit.date}`,
    `分类：${hit.category}`,
    `主题：${hit.matched_topics.join(", ")}`,
    `摘要：${hit.abstract}`,
    `为什么重要：${hit.why_it_matters}`,
    `得分：${hit.score.toFixed(3)}`,
  ].join("\n")).join("\n\n");

  return {
    system: "你是病原生信、蛋白质/基因组学、临床微生物学与AI/LLM/Agent交叉领域的研究助手。必须只根据给定上下文回答，用中文输出，结构清晰，解释具体，不要编造未提供的论文信息。",
    user: [
      `用户问题：${query}`,
      "",
      selectedBlock,
      "",
      "召回候选论文：",
      hitBlocks,
      "",
      "请按以下结构回答：1. 结论 2. 与 protein/gene/clinical/AI-LLM-Agent 的关系 3. 最相关论文逐篇解读 4. 风险与不足 5. 下一步建议。",
    ].join("\n"),
  };
}
