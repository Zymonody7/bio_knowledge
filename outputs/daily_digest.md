# 每日论文监控日报 (2026-04-13)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 11 篇新论文。

## 抓取状态

- arXiv：成功，命中 18 篇
- PubMed：成功，命中 21 篇
- bioRxiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='api.biorxiv.org', port=443): Read timed out. (read timeout=60)
- medRxiv：成功，命中 0 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [WisdomInterrogatory (LuWen): An Open-Source Legal Large Language Model Technical Report](http://arxiv.org/abs/2604.06737v2)
  来源：arXiv | 日期：2026-04-08 | 相关度：6.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：大语言模型在自然语言处理领域表现卓越，但在法律领域因专业术语密集、推理逻辑复杂及知识更新快等特征仍面临挑战。本文推出了“律问”（LuWen），一个基于百川（Baichuan）基础模型开发的开源中文法律大模型。该模型集成了三项核心技术：在大规模法律语料库上进行持续预训练、利用精选法律指令数据进行监督微调（SFT），以及结合全面法律知识库的检索增强生成（RAG）。研究者在法律判决预测、司法考试、法律文本摘要、法条问答及司法决策推理五项代表性...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ToolRosetta: Scalable Tool Access for Open-World Scientific Agents](http://arxiv.org/abs/2603.09290v2)
  来源：arXiv | 日期：2026-03-10 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：基于大语言模型（LLM）的智能体系统在科学发现中应用日益广泛，但其实际能力受限于狭窄且需人工维护的工具层。尽管开源仓库、软件包和 API 中存在大量科学计算能力，但这些资源难以标准化、操作化和可靠调用。本文提出 ToolRosetta 框架，通过将异构计算程序自动转换为经过验证的可调用工具，为 LLM 智能体提供可扩展的开放世界计算访问能力。ToolRosetta 集成了仓库检索、工具标准化、执行测试、迭代修复和安全感知治理。在涵盖 6...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Policy-Aware Edge LLM-RAG Framework for Internet of Battlefield Things Mission Orchestration](http://arxiv.org/abs/2604.09493v1)
  来源：arXiv | 日期：2026-04-10 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：大语言模型（LLMs）为自主信息物理系统的意图驱动控制提供了潜力，但在战场物联网（IoBT）等关键任务环境中，其直接应用面临安全性、可靠性和策略合规性的严峻挑战。本文提出了一种策略感知大语言模型检索增强生成框架（PA-LLM-RAG），专门用于边缘部署的 IoBT 任务编排。该框架集成了一个轻量级检索模块，将决策建立在操作策略和遥测数据基础上，并结合本地托管的 LLM 进行任务规划，同时引入次级 JudgeLLM 在指令执行前进行独立验...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [When LLMs Lag Behind: Knowledge Conflicts from Evolving APIs in Code Generation](http://arxiv.org/abs/2604.09515v1)
  来源：arXiv | 日期：2026-04-10 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：软件库的快速演进对大语言模型（LLMs）构成了重大挑战，其静态参数知识在训练后往往会过时。虽然检索增强生成（RAG）常用于提供最新的 API 规范，但当外部指令与模型内部参数知识冲突时，会产生“上下文-记忆冲突”。本文通过构建包含 8 个 Python 库中 270 个真实更新（涉及 API 弃用、修改和新增）的基准测试，对 API 演进下的 LLM 代码生成进行了系统性实证研究。研究评估了 4 个模型家族的 11 个模型。结果显示，在...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Biologically-Grounded Multi-Encoder Architectures as Developability Oracles for Antibody Design](http://arxiv.org/abs/2604.09369v1)
  来源：arXiv | 日期：2026-04-10 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：生成模型现已能设计数千种从头抗体序列，但生物物理表征的高昂成本限制了其向临床疗法的转化。本文提出 CrossAbSense 框架，这是一系列针对特定属性的神经预测器（oracles），通过结合冻结的蛋白质语言模型（PLM）编码器与可配置的注意力解码器构建而成。研究通过对每个属性进行超过 200 次运行的系统性超参数搜索，在包含 242 种治疗性 IgG 的 GDPa1 基准数据集上进行了验证。结果显示，CrossAbSense 在五项可...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Exploiting Web Search Tools of AI Agents for Data Exfiltration](http://arxiv.org/abs/2510.09093v2)
  来源：arXiv | 日期：2025-10-10 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：大语言模型（LLMs）现已常规用于自主执行复杂任务，包括自然语言处理和网页搜索等动态工作流。通过工具调用和检索增强生成（RAG），LLMs 能够处理和检索敏感的企业数据，但这在增强功能的同时也放大了其被滥用的风险。随着 LLMs 与外部数据源交互日益增多，间接提示注入（indirect prompt injection）成为一种关键且不断演变的攻击向量，使对手能通过操纵输入来利用模型。本研究对多种模型的间接提示注入攻击进行了系统评估，分...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [On the Representational Limits of Quantum-Inspired 1024-D Document Embeddings: An Experimental Evaluation Framework](http://arxiv.org/abs/2604.09430v1)
  来源：arXiv | 日期：2026-04-10 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：文本嵌入是现代信息检索和检索增强生成（RAG）的核心。本文提出了一个实验框架，用于构建基于重叠窗口和多尺度聚合的量子启发式 1024 维文档嵌入。该流程结合了语义投影（如 EigAngle）、电路启发式特征映射以及可选的教师-学生蒸馏，并包含指纹机制以确保可重复性。研究引入了一套混合检索诊断工具，包括 BM25 与嵌入评分之间的静态和动态插值、候选合并策略以及用于评分融合上限评估的 alpha-oracle。在涵盖技术、叙事和法律领域的...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [Facet-Level Tracing of Evidence Uncertainty and Hallucination in RAG](http://arxiv.org/abs/2604.09174v1)
  来源：arXiv | 日期：2026-04-10 | 相关度：2.75 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：检索增强生成（RAG）旨在通过检索证据减少幻觉，但即便在存在相关文档的情况下，幻觉答案依然普遍。现有的评估方法多集中在答案或段落层面，难以深入揭示生成过程中证据的利用机制。本研究提出了一种面向问答（QA）的“面级（Facet-level）”诊断框架，将每个输入问题分解为原子推理面。针对每个面，利用结合了检索相关性与基于自然语言推理（NLI）忠实度评分的“面×块（Facet x Chunk）”矩阵来评估证据的充分性与可靠性。为诊断证据使用...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HyperMem: Hypergraph Memory for Long-Term Conversations](http://arxiv.org/abs/2604.08256v2)
  来源：arXiv | 日期：2026-04-09 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：长期记忆对于对话智能体在长对话中保持连贯性、追踪持续任务和提供个性化交互至关重要。然而，现有的检索增强生成（RAG）和基于图的存储方法主要依赖成对关系，难以捕捉多个元素之间的联合依赖等高阶关联，导致检索内容碎片化。为此，我们提出了 HyperMem，一种基于超图的分层存储架构，利用超边显式建模此类关联。HyperMem 将存储结构化为主题（topics）、情节（episodes）和事实（facts）三个层面，并通过超边将相关情节及其事实...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [MAB-DQA: Addressing Query Aspect Importance in Document Question Answering with Multi-Armed Bandits](http://arxiv.org/abs/2604.08952v1)
  来源：arXiv | 日期：2026-04-10 | 相关度：2.75 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：文档问答（DQA）是文档理解的核心任务，旨在根据用户查询从文档中生成答案。由于需要解析视觉布局，近期研究多采用多模态检索增强生成（RAG）处理页面图像。然而，多模态 RAG 在处理大量图像时面临挑战，检索阶段通常仅保留极少数候选页（如 Top-4），导致信息丰富但视觉显著性较低的内容被忽略。为解决此问题，我们提出了基于多臂老虎机（MAB）的 DQA 框架（MAB-DQA），用于显式建模查询中多个隐含维度的重要性。MAB-DQA 将查询分...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 其他

- [Trans-RAG: Query-Centric Vector Transformation for Secure Cross-Organizational Retrieval](http://arxiv.org/abs/2604.09541v1)
  来源：arXiv | 日期：2026-04-10 | 相关度：2.75 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：跨组织部署的检索增强生成（RAG）系统在安全性、准确性和效率之间面临核心权衡。现有加密方法在解密过程中会暴露明文，而联邦架构则限制了资源整合并产生巨大开销。本文提出 Trans-RAG，实现了一种新型向量空间语言范式，使各组织的知识存在于数学隔离的语义空间中。其核心是 vector2Trans 技术，这是一种多阶段转换技术，允许查询通过以查询为中心的转换动态地“对齐”各组织的向量空间，在消除解密开销的同时保持原生检索效率。安全性评估显示...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。
