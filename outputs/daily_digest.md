# 每日论文监控日报 (2026-03-16)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 9 篇新论文。

## 抓取状态

- arXiv：成功，命中 7 篇
- PubMed：成功，命中 29 篇
- bioRxiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='api.biorxiv.org', port=443): Read timed out. (read timeout=60)
- medRxiv：成功，命中 7 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [Artificial intelligence-based analysis of thrombotic and infectious risk factors in peripherally inserted central catheters (PICCs).](https://pubmed.ncbi.nlm.nih.gov/41832132/)
  来源：PubMed | 日期：2026-03-13 | 相关度：7.9 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：经外周穿刺中心静脉导管（PICC）广泛用于化疗、肠外营养及抗生素治疗，但常伴随感染和血栓栓塞等延迟并发症。本研究旨在识别PICC相关感染与血栓的风险因素，采用已验证的自然语言处理程序BIBOT及大语言模型LLaMA3，对2013至2023年间PubMed收录的1896篇摘要进行自动筛选。经AI辅助内容分析，识别出343篇关于PICC并发症的原创文章，进而精选出113篇感染相关和281篇血栓相关文献。研究人工识别出20个感染风险因素（如管...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [Multimodal Protein Language Models for Enzyme Kinetic Parameters: From Substrate Recognition to Conformational Adaptation](http://arxiv.org/abs/2603.12845v1)
  来源：arXiv | 日期：2026-03-13 | 相关度：7.8 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：预测酶动力学参数（如 $k_{cat}$、$K_m$ 和 $K_i$）对于量化酶在特定生化条件下催化底物的效率至关重要。传统方法常将其简化为酶与底物间的静态兼容性问题，通过浅层操作融合表征并回归单一数值，忽略了涉及底物识别与构象适应的阶段性催化过程。本研究将动力学预测重新定义为阶段性多模态条件建模问题，并提出“酶-反应桥接适配器”（ERBA）。ERBA 通过微调将跨模态信息注入蛋白质语言模型（PLM），同时保留其生化先验。该框架包含两个...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Toward AI foundation models for epidemics: Promise, challenges, and paths forward.](https://pubmed.ncbi.nlm.nih.gov/41824492/)
  来源：PubMed | 日期：2026-03-31 | 相关度：4.4 | 新颖度：5.5
  匹配主题：pathogenomics
  中文摘要：基础模型（如 GPT、GenCast、AlphaFold）通过在大规模异构数据上预训练，已显著改变科学发现模式，但在流行病建模领域尚未实现类似转型。传统模型通常针对特定病原体，在应对如 SARS-CoV-2 等突发疫情时，往往难以快速生成见解。本文探讨了将基础模型范式扩展至流行病学的可行性，旨在构建一个能捕捉跨病原体、人群和环境的传染病动力学共享原则的单一预训练模型。该模型仅需极少数据即可微调至新环境，实现更快速的预测、推理和响应，对资...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [AutoClimDS: Climate Data Science Agentic AI -- A Knowledge Graph is All You Need](http://arxiv.org/abs/2509.21553v2)
  来源：arXiv | 日期：2025-09-25 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：气候数据科学受限于碎片化的数据源、异构格式和高技术门槛。本文提出 AutoClimDS，一个集成了精选气候知识图谱（KG）与云原生科学分析工作流的最小可行性智能体（Agentic AI）系统。该 KG 将数据集、元数据、工具和工作流统一为机器可解释的结构；AI 智能体利用生成式模型实现自然语言查询解析、自动数据发现、程序化数据获取及端到端气候分析。研究结果表明，AutoClimDS 仅凭自然语言指令即可重现已发表的科学图表和分析，完成从...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [RXNRECer Enables Fine-grained Enzymatic Function Annotation through Active Learning and Protein Language Models](http://arxiv.org/abs/2603.12694v1)
  来源：arXiv | 日期：2026-03-13 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：酶功能注释的核心挑战在于准确识别蛋白质催化的生化反应。现有方法大多依赖酶委员会（EC）编号作为中介，即先预测EC编号再检索相关反应。这种间接策略因蛋白质、EC编号与反应之间复杂的多对多映射，以及数据库更新滞后和不一致性，导致预测存在歧义。为此，我们开发了RXNRECer，这是一个基于Transformer的集成框架，可直接预测酶催化反应而无需依赖EC编号。该框架整合了蛋白质语言模型（PLM）和主动学习技术，旨在捕捉高层序列语义和细粒度的...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [Towards AI Search Paradigm](http://arxiv.org/abs/2506.17188v2)
  来源：arXiv | 日期：2025-06-20 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：本文提出了“AI搜索范式”（AI Search Paradigm），这是一个旨在模拟人类信息处理和决策过程的下一代搜索系统蓝图。该范式采用由四个大语言模型（LLM）驱动的智能体（Master、Planner、Executor和Writer）组成的模块化架构，能够动态适应从简单事实查询到复杂多阶段推理任务的全谱系信息需求。这些智能体通过协调的工作流进行动态协作，负责评估查询复杂度、将问题分解为可执行计划，并统筹工具使用、任务执行与内容合成...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [From Study Design to Executable Code: Automating Target Trial Emulation with Large Language Models](https://www.medrxiv.org/content/10.64898/2026.03.13.26348306v1)
  来源：medRxiv | 日期：2026-03-14 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：实施目标试验模拟（TTE）研究并生成端到端可执行分析代码具有极高的技术门槛。本研究开发了 THESEUS 框架，旨在将自由文本形式的研究描述转化为 OHDSI 生态系统中标准化的分析规范和可执行的 Strategus R 脚本。THESEUS 包含两个核心步骤：首先，利用大语言模型（LLM）将研究描述映射到受限的 JSON 模式中实现标准化；其次，将结构化规范转换为 R 脚本，并引入自审计循环进行错误修正。研究评估了 8 种商业 LLM...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Computational Innovations in Cancer Research and How Computing is Transforming Drug Discovery and Development: A Review.](https://pubmed.ncbi.nlm.nih.gov/41832735/)
  来源：PubMed | 日期：2026-03-13 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：癌症的复杂性与耐药性使其仍是全球主要死因。本综述重点探讨了计算机辅助药物设计（CADD）及其相关计算方法在癌症研究中的应用，涵盖药物发现、靶点识别和化合物优化。研究指出，CADD、人工智能（AI）、机器学习（ML）及量子计算正通过理性设计和预测建模，克服传统实验方法耗时耗力的局限。文中详细分析了分子对接、分子动力学、QSAR及虚拟筛选在加速先导化合物优化、预测毒性与耐药性方面的作用。针对EGFR、PARP、KRAS G12C及免疫治疗靶...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Integrative Approaches in Lung Cancer Diagnosis: Bridging Molecular Biomarkers and AI Driven Imaging.](https://pubmed.ncbi.nlm.nih.gov/41830914/)
  来源：PubMed | 日期：2026-03-14 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：传统诊断手段如X射线、CT、支气管镜及组织活检在肺癌早期检测中存在局限。本文综述了分子生物学与计算技术进展驱动的诊断范式转变，重点分析了EGFR、ALK、KRAS、BRAF、MET及PD-L1等分子生物标志物在常规诊断中的整合，以实现精准分型与疗法选择。液体活检和循环肿瘤DNA（ctDNA）为肿瘤实时监测提供了非侵入性方案。二代测序（NGS）及基因组学、转录组学、蛋白质组学等多组学方法揭示了肿瘤微环境的详细分子图谱。同时，AI（特别是机...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
