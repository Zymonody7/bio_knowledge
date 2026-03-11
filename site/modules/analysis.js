export function detailAnalysisMarkdown(paper, notes) {
  if (paper.analysis_zh) {
    return [
      paper.analysis_zh.trim(),
      notes[paper.paper_id] ? `\n## 你的备注\n${notes[paper.paper_id]}` : "",
    ].filter(Boolean).join("\n");
  }

  return [
    "## 当前状态",
    "这篇论文还没有生成可用的 AI 解读。",
    "",
    "## 原因",
    "- 当前站点没有拿到远程 LLM 富化结果。",
    "- 为了避免继续显示空话和模板废话，这里不再输出占位解读。",
    "",
    "## 现在该看什么",
    "- 先读下方中文摘要；如果中文摘要也为空，再直接读原始摘要。",
    "- 优先看任务定义、数据来源、模型方法、实验结果和局限。",
    notes[paper.paper_id] ? `\n## 你的备注\n${notes[paper.paper_id]}` : "",
  ].filter(Boolean).join("\n");

  const intersections = [];
  if (/protein|proteomics|nanobody/i.test(`${paper.title} ${paper.abstract}`)) intersections.push("protein / proteomics");
  if (/gene|genomic|genomics|transcript/i.test(`${paper.title} ${paper.abstract}`)) intersections.push("gene / genomics");
  if (/clinical|patient|diagnosis|microbiology/i.test(`${paper.title} ${paper.abstract}`)) intersections.push("clinical / microbiology");
  if (/agent|llm|language model|foundation model|multimodal/i.test(`${paper.title} ${paper.abstract}`)) intersections.push("AI / LLM / Agent");
  const relevanceInterpretation = paper.relevance_score >= 7
    ? "这篇论文和当前知识库的 AI 生信主轴高度一致。"
    : paper.relevance_score >= 5
      ? "这篇论文与当前方向中度相关，值得看其任务设计和技术路线。"
      : "这篇论文和主轴存在交叉，但更适合作为边缘参考或扩展阅读。";
  const noveltyInterpretation = paper.novelty_score >= 7
    ? "新颖度较高，通常意味着它较新，或者方法/任务设定有明显新信号。"
    : paper.novelty_score >= 4
      ? "新颖度中等，值得重点确认它到底是新数据、新模型还是旧问题的新包装。"
      : "新颖度偏低，更适合当作背景材料或已有方向的补充。";

  const readChecklist = [
    "任务定义是否真正需要 LLM / agent / language model，而不是仅在摘要里点名。",
    "数据来源是否贴近真实实验或临床场景，是否有明确输入输出和评测标准。",
    "如果是 protein / gene / genomics 方向，是否能复用为下游 benchmark、知识库或 workflow 模块。",
    "如果是临床或病原方向，是否涉及样本流转、报告生成、决策支持或 surveillance 场景。",
  ];

  const risks = [];
  if (!/llm|language model|foundation model|agent|transformer|rag|gpt/i.test(`${paper.title} ${paper.abstract}`)) {
    risks.push("标题和摘要里没有特别强的 AI 关键词，可能只是弱交叉。");
  }
  if (!/clinical|patient|hospital|sample|cohort|diagnosis|microbiology/i.test(`${paper.title} ${paper.abstract}`)) {
    risks.push("临床落地信号不强，可能更偏方法或基础研究。");
  }
  if (!/benchmark|dataset|evaluation|f1|auc|accuracy|validation/i.test(`${paper.title} ${paper.abstract}`)) {
    risks.push("评测或验证描述不充分，读的时候要特别留意实验设计。");
  }

  return [
    "### 总体判断",
    `${paper.why_it_matters}`,
    "",
    "### 相关度与新颖度",
    `- 综合分：**${paper.importance_score ?? "-"}**`,
    `- 相关度：**${paper.relevance_score}**。${relevanceInterpretation}`,
    `- 新颖度：**${paper.novelty_score}**。${noveltyInterpretation}`,
    `- 来源：**${paper.source}**，日期：**${paper.date.slice(0, 10)}**，类别：**${paper.category}**`,
    "",
    "### 与你的研究交叉点",
    intersections.length
      ? `这篇论文和你的关注轴线交叉在：**${intersections.join("、")}**。`
      : "这篇论文和你的研究主线交叉有限，更像外围参考。",
    "",
    "### 读论文时建议重点看",
    ...readChecklist.map((item) => `- ${item}`),
    "",
    "### 风险与不足",
    ...(risks.length ? risks.map((item) => `- ${item}`) : ["- 摘要层面没有特别明显的红旗，值得进原文确认实验和评测细节。"]),
    "",
    "### 可以怎么用",
    `- 如果你在做知识库：可提炼它的任务定义、数据结构、评测指标和可复用术语。`,
    `- 如果你在做模型：重点看它是否提供了 prompt / pipeline / feature engineering / benchmark 设计线索。`,
    `- 如果你在做产品：重点看能否映射到报告生成、检索增强、自动标注或临床决策支持。`,
    notes[paper.paper_id] ? `\n### 你的备注\n${notes[paper.paper_id]}` : "",
  ].filter(Boolean).join("\n");
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
    ? `当前焦点论文：\n标题：${selectedPaper.title}\n来源：${selectedPaper.source}\n分类：${selectedPaper.category}\n主题：${selectedPaper.matched_topics.join(", ")}\n中文摘要：${selectedPaper.abstract_zh || ""}\n英文摘要：${selectedPaper.abstract}\n为什么重要：${selectedPaper.why_it_matters}\n已有中文解读：${selectedPaper.analysis_zh || ""}`
    : "当前没有焦点论文。";

  const hitBlocks = hits.map((hit, index) => [
    `[候选 ${index + 1}]`,
    `标题：${hit.title}`,
    `来源：${hit.source}`,
    `日期：${hit.date}`,
    `分类：${hit.category}`,
    `主题：${hit.matched_topics.join(", ")}`,
    `中文摘要：${hit.abstract_zh || ""}`,
    `摘要：${hit.abstract}`,
    `为什么重要：${hit.why_it_matters}`,
    `已有中文解读：${hit.analysis_zh || ""}`,
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
