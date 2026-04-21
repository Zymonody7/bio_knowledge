# 每日论文监控日报 (2026-04-21)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 35 篇新论文。

## 抓取状态

- arXiv：成功，命中 42 篇
- PubMed：成功，命中 8 篇
- bioRxiv：失败，命中 0 篇，错误：Expecting value: line 1 column 1 (char 0)
- medRxiv：失败，命中 0 篇，错误：Expecting value: line 1 column 1 (char 0)

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [AeroRAG: Structured Multimodal Retrieval-Augmented LLM for Fine-Grained Aerial Visual Reasoning](http://arxiv.org/abs/2604.17889v1)
  来源：arXiv | 日期：2026-04-20 | 相关度：7.9 | 新颖度：7.46
  匹配主题：foundation_model_agent
  中文摘要：Despite recent progress in multimodal large language models (MLLMs), reliable visual question answering in aerial scenes remains challenging. In such scenes, task-critical evidence is often carried by small objects, expl...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Integrating Graphs, Large Language Models, and Agents: Reasoning and Retrieval](http://arxiv.org/abs/2604.15951v2)
  来源：arXiv | 日期：2026-04-17 | 相关度：7.9 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Generative AI, particularly Large Language Models, increasingly integrates graph-based representations to enhance reasoning, retrieval, and structured decision-making. Despite rapid advances, there remains limited clarit...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Retrieval-Augmented Multimodal Model for Fake News Detection](http://arxiv.org/abs/2604.18112v1)
  来源：arXiv | 日期：2026-04-20 | 相关度：7.5 | 新颖度：7.45
  匹配主题：foundation_model_agent
  中文摘要：In recent years, multimodal multidomain fake news detection has garnered increasing attention. Nevertheless, this direction presents two significant challenges: (1) Failure to Capture Cross-Instance Narrative Consistency...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Scaling Beyond Context: A Survey of Multimodal Retrieval-Augmented Generation for Document Understanding](http://arxiv.org/abs/2510.15253v3)
  来源：arXiv | 日期：2025-10-17 | 相关度：7.5 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Document understanding is critical for applications from financial analysis to scientific discovery. Current approaches, whether OCR-based pipelines feeding Large Language Models (LLMs) or native Multimodal LLMs (MLLMs),...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [MathNet: a Global Multimodal Benchmark for Mathematical Reasoning and Retrieval](http://arxiv.org/abs/2604.18584v1)
  来源：arXiv | 日期：2026-04-20 | 相关度：6.8 | 新颖度：8.78
  匹配主题：foundation_model_agent
  中文摘要：Mathematical problem solving remains a challenging test of reasoning for large language and multimodal models, yet existing benchmarks are limited in size, language coverage, and task diversity. We introduce MathNet, a h...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Applications of deep generative models to DNA reaction kinetics and to cryogenic electron microscopy](http://arxiv.org/abs/2604.16851v1)
  来源：arXiv | 日期：2026-04-18 | 相关度：7.8 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：This dissertation explores how deep generative models can advance the analysis of challenging biological problems by integrating domain knowledge with deep learning. It focuses on two areas: DNA reaction kinetics and cry...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [ScienceBoard: Evaluating Multimodal Autonomous Agents in Realistic Scientific Workflows](http://arxiv.org/abs/2505.19897v3)
  来源：arXiv | 日期：2025-05-26 | 相关度：6.8 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have extended their impact beyond Natural Language Processing, substantially fostering the development of interdisciplinary research. Recently, various LLM-based agents have been developed to...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Advanced Applications of Generative AI in Actuarial Science: Case Studies Beyond ChatGPT](http://arxiv.org/abs/2506.18942v2)
  来源：arXiv | 日期：2025-06-22 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：This article explores the potential of generative AI (GenAI) to support actuarial practice through four implemented case studies. It situates these case studies within the broader evolution of artificial intelligence in ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ArbGraph: Conflict-Aware Evidence Arbitration for Reliable Long-Form Retrieval-Augmented Generation](http://arxiv.org/abs/2604.18362v1)
  来源：arXiv | 日期：2026-04-20 | 相关度：6.15 | 新颖度：8.01
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) remains unreliable in long-form settings, where retrieved evidence is noisy or contradictory, making it difficult for RAG pipelines to maintain factual consistency. Existing approache...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Architecture Matters More Than Scale: A Comparative Study of Retrieval and Memory Augmentation for Financial QA Under SME Compute Constraints](http://arxiv.org/abs/2604.17979v1)
  来源：arXiv | 日期：2026-04-20 | 相关度：6.15 | 新颖度：7.03
  匹配主题：foundation_model_agent
  中文摘要：The rapid adoption of artificial intelligence (AI) and large language models (LLMs) is transforming financial analytics by enabling natural language interfaces for reporting, decision support, and automated reasoning. Ho...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RAVEN: Retrieval-Augmented Vulnerability Exploration Network for Memory Corruption Analysis in User Code and Binary Programs](http://arxiv.org/abs/2604.17948v1)
  来源：arXiv | 日期：2026-04-20 | 相关度：6.15 | 新颖度：6.95
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have demonstrated remarkable capabilities across various cybersecurity tasks, including vulnerability classification, detection, and patching. However, their potential in automated vulnerabil...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MASS-RAG: Multi-Agent Synthesis Retrieval-Augmented Generation](http://arxiv.org/abs/2604.18509v1)
  来源：arXiv | 日期：2026-04-20 | 相关度：5.45 | 新颖度：8.12
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are widely used in retrieval-augmented generation (RAG) to incorporate external knowledge at inference time. However, when retrieved contexts are noisy, incomplete, or heterogeneous, a single...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evaluating Multi-Hop Reasoning in RAG Systems: A Comparison of LLM-Based Retriever Evaluation Strategies](http://arxiv.org/abs/2604.18234v1)
  来源：arXiv | 日期：2026-04-20 | 相关度：5.45 | 新颖度：7.51
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) enhances large language models (LLMs) with external knowledge to answer questions more accurately. However, research on evaluating RAG systems-particularly the retriever component-rem...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [NIM4-ASR: Towards Efficient, Robust, and Customizable Real-Time LLM-Based ASR](http://arxiv.org/abs/2604.18105v1)
  来源：arXiv | 日期：2026-04-20 | 相关度：5.45 | 新颖度：7.18
  匹配主题：foundation_model_agent
  中文摘要：Integrating large language models (LLMs) into automatic speech recognition (ASR) has become a mainstream paradigm in recent years. Although existing LLM-based ASR models demonstrate impressive performance on public bench...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Is Agentic RAG worth it? An experimental comparison of RAG approaches](http://arxiv.org/abs/2601.07711v2)
  来源：arXiv | 日期：2026-01-12 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) systems are usually defined by the combination of a generator and a retrieval component that extracts textual context from a knowledge base to answer user queries. However, such basic...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Modular Representation Compression: Adapting LLMs for Efficient and Effective Recommendations](http://arxiv.org/abs/2604.18146v1)
  来源：arXiv | 日期：2026-04-20 | 相关度：4.75 | 新颖度：6.56
  匹配主题：foundation_model_agent
  中文摘要：Recently, large language models (LLMs) have advanced recommendation systems (RSs), and recent works have begun to explore how to integrate LLMs into industrial RSs. While most approaches deploy LLMs offline to generate a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ClimAgent: LLM as Agents for Autonomous Open-ended Climate Science Analysis](http://arxiv.org/abs/2604.16922v1)
  来源：arXiv | 日期：2026-04-18 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：气候研究对于缓解全球环境危机至关重要，但多尺度数据集的激增和分析工具的复杂性造成了研究瓶颈，使科学发现局限于碎片化且劳动密集型的流程。虽然大语言模型（LLM）为扩展科学专业知识提供了新范式，但现有探索多局限于简单的问答任务，忽略了专业气候科学所需的复杂物理约束和数据驱动特性。为此，我们提出了 ClimAgent，这是一个通用的自主框架，旨在执行跨气候子领域的广泛研究任务。通过集成统一的工具使用环境和严格的推理协议，ClimAgent 超...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Across Programming Language Silos: A Study on Cross-Lingual Retrieval-augmented Code Generation](http://arxiv.org/abs/2506.03535v2)
  来源：arXiv | 日期：2025-06-04 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：当前大语言模型（LLM）检索增强代码生成（RACG）的研究主要集中在单语言设置，其跨语言有效性尚未得到充分探索。在现代软件开发中，跨编程语言（PL）的代码迁移与复用是一项常见且具挑战性的任务，多语言RACG系统的重要性日益凸显。为系统研究RACG中的跨语言代码知识迁移，本研究构建了一个涵盖13种编程语言、包含近1.4万个实例的数据集。实验结果揭示了三个关键洞察：(1) 即使使用直接注入方式，RACG在不同编程语言间的知识迁移也并非易事；...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [TeleEmbedBench: A Multi-Corpus Embedding Benchmark for RAG in Telecommunications](http://arxiv.org/abs/2604.17778v1)
  来源：arXiv | 日期：2026-04-20 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly deployed in the telecommunications domain for critical tasks, relying heavily on Retrieval-Augmented Generation (RAG) to adapt general-purpose models to continuously evolving...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Learning to Extract Rational Evidence via Reinforcement Learning for Retrieval-Augmented Generation](http://arxiv.org/abs/2507.15586v7)
  来源：arXiv | 日期：2025-07-21 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：检索增强生成（RAG）能有效提升大语言模型（LLM）的准确性，但检索到的噪声会严重损害生成质量，因此亟需开发去噪机制。现有方法通常直接提取证据而缺乏深度思考，存在过滤掉关键线索且泛化能力差的风险。为此，本研究提出 EviOmni，旨在通过“先推理后提取”的模式学习提取理性证据。具体而言，EviOmni 将证据推理与证据提取整合到统一的轨迹中，并采用知识标记掩码（knowledge token masking）技术防止信息泄露。该模型通过...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [WeatherArchive-Bench: Benchmarking Retrieval-Augmented Reasoning for Historical Weather Archives](http://arxiv.org/abs/2510.05336v2)
  来源：arXiv | 日期：2025-10-06 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：历史气象档案记录了社会应对极端天气的原始叙述，对理解气候脆弱性和韧性至关重要，但其规模庞大、数字化噪声多且语言陈旧，难以转化为结构化知识。本文推出了 WeatherArchive-Bench，这是首个评估历史气象档案检索增强生成（RAG）系统的基准。该基准包含两个任务：WeatherArchive-Retrieval 评估从超过 100 万个档案新闻片段中检索相关段落的能力；WeatherArchive-Assessment 评估大语言...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [MegaRAG: Multimodal Knowledge Graph-Based Retrieval Augmented Generation](http://arxiv.org/abs/2512.20626v2)
  来源：arXiv | 日期：2025-11-26 | 相关度：7.5 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) enables large language models (LLMs) to dynamically access external information, which is powerful for answering questions over previously unseen documents. Nonetheless, they struggle...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RosettaSearch: Multi-Objective Inference-Time Search for Protein Sequence Design](http://arxiv.org/abs/2604.17175v1)
  来源：arXiv | 日期：2026-04-19 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：We introduce RosettaSearch, an inference-time multi-objective optimization approach for protein sequence optimization. We use large language models (LLMs) as a generative optimizer within a search algorithm capable of co...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Multi-Scale Reversible Chaos Game Representation: A Unified Framework for Sequence Classification](http://arxiv.org/abs/2604.18477v1)
  来源：arXiv | 日期：2026-04-20 | 相关度：5.75 | 新颖度：7.78
  匹配主题：foundation_model_agent
  中文摘要：Biological classification with interpretability remains a challenging task. For this, we introduce a novel encoding framework, Multi-Scale Reversible Chaos Game Representation (MS-RCGR), that transforms biological sequen...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Latent Abstraction for Retrieval-Augmented Generation](http://arxiv.org/abs/2604.17866v1)
  来源：arXiv | 日期：2026-04-20 | 相关度：5.45 | 新颖度：6.36
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) has become a standard approach for enhancing large language models (LLMs) with external knowledge, mitigating hallucinations, and improving factuality. However, existing systems rely ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Culinary Crossroads: A RAG Framework for Enhancing Diversity in Cross-Cultural Recipe Adaptation](http://arxiv.org/abs/2507.21934v2)
  来源：arXiv | 日期：2025-07-29 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：In cross-cultural recipe adaptation, the goal is not only to ensure cultural appropriateness and retain the original dish's essence, but also to provide diverse options for various dietary needs and preferences. Retrieva...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [DocQAC: Adaptive Trie-Guided Decoding for Effective In-Document Query Auto-Completion](http://arxiv.org/abs/2604.18257v1)
  来源：arXiv | 日期：2026-04-20 | 相关度：4.75 | 新颖度：7.79
  匹配主题：foundation_model_agent
  中文摘要：Query auto-completion (QAC) has been widely studied in the context of web search, yet remains underexplored for in-document search, which we term DocQAC. DocQAC aims to enhance search productivity within long documents b...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Procedural Knowledge at Scale Improves Reasoning](http://arxiv.org/abs/2604.01348v2)
  来源：arXiv | 日期：2026-04-01 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：测试时缩放（Test-time scaling）是提升语言模型复杂推理能力的有效手段，但现有方法多孤立处理问题，未能系统复用先前的推理轨迹，尤其是如何重构问题、选择路径及验证回溯等程序性知识。本文提出“推理记忆”（Reasoning Memory），这是一种专为推理模型设计的检索增强生成（RAG）框架，旨在规模化检索和复用程序性知识。研究者将现有的分步推理轨迹分解为独立的“子问题-子程序”对，构建了包含 3200 万条紧凑程序性知识条目...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Beyond Fine-Tuning: In-Context Learning and Chain-of-Thought for Reasoned Distractor Generation](http://arxiv.org/abs/2604.17574v1)
  来源：arXiv | 日期：2026-04-19 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：干扰项生成（DG）是一项依赖领域专家的劳动密集型任务，旨在为多项选择题生成合理但错误的选项。可靠的干扰项必须与问题语境相关，并能通过隐式推理误导受试者。虽然现有方法通过微调预训练编码器-解码器模型并结合对比学习来生成语义相关的干扰项，但往往无法捕捉专家在选择干扰项时的底层推理过程。本文探索了利用大语言模型（LLMs）的推理能力进行干扰项生成，通过无监督语义检索选择少样本示例进行上下文学习（ICL）。研究者设计了一个推理增强的 DG 框架...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 其他

- [R3A: Reinforced Reasoning for Relevance Assessment for RAG in User-Generated Content Platforms](http://arxiv.org/abs/2508.02506v2)
  来源：arXiv | 日期：2025-08-04 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：检索增强生成（RAG）在用户生成内容（UGC）平台中起着至关重要作用，但其有效性高度依赖于准确的查询-文档相关性评估。UGC平台面临两大挑战：一是由于RAG场景中用户反馈稀疏导致的意图模糊；二是非对称相关性，即相关性由局部含答案内容驱动而非全局相似性。为此，本研究提出强化推理相关性评估模型（R3A），将相关性评估分解为意图推断和证据锚定。R3A利用辅助的高点击文档推断潜在查询意图，并提取逐字证据片段来支撑相关性决策，从而降低噪声敏感性并...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Masking or Mitigating? Deconstructing the Impact of Query Rewriting on Retriever Biases in RAG](http://arxiv.org/abs/2604.06097v2)
  来源：arXiv | 日期：2026-04-07 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）系统中的稠密检索器存在多种系统性偏差，包括长度偏差、位置偏差、字面匹配偏差和重复偏差，这些偏差会严重损害检索质量。尽管查询重写（Query Rewriting）已成为 RAG 流程的标准环节，但其对上述偏差的具体影响此前尚不明确。本研究首次系统性地探讨了查询增强技术如何影响稠密检索偏差，在 6 个检索器上评估了 5 种主流方法。研究发现，简单的基于大语言模型（LLM）的重写在综合偏差降低方面效果最显著（达 54%）...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Althea: Human-AI Collaboration for Fact-Checking and Critical Reasoning](http://arxiv.org/abs/2602.11161v2)
  来源：arXiv | 日期：2025-12-29 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：互联网信息生态系统需要兼具可扩展性与认识论可信度的事实核查系统。本文介绍 Althea，这是一个检索增强系统，集成了问题生成、证据检索和结构化推理，旨在支持用户驱动的在线声明评估。在 AVeriTeC 基准测试中，Althea 实现了 0.44 的 Macro-F1 分数，优于标准验证流水线，并提升了对支持和反驳声明的辨别能力。通过一项受控用户研究和纵向调查实验（N=963），研究对比了三种交互模式：引导推理的探索模式、提供综合裁决的摘...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [AutoGraph-R1: End-to-End Reinforcement Learning for Knowledge Graph Construction](http://arxiv.org/abs/2510.15339v3)
  来源：arXiv | 日期：2025-10-17 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：构建用于检索增强生成（RAG）的高效知识图谱（KG）对于提升问答系统（QA）至关重要。然而，目前的 KG 构建过程与下游应用脱节，导致生成的图结构并非最优。为解决此问题，我们提出了 AutoGraph-R1，这是首个利用强化学习（RL）直接针对任务性能优化 KG 构建的框架。AutoGraph-R1 将图生成建模为策略学习问题，通过训练大语言模型（LLM）构造器，使其奖励函数源自该图在 RAG 流水线中的功能效用。我们设计了两种新型任务...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Semantic Entanglement in Vector-Based Retrieval: A Formal Framework and Context-Conditioned Disentanglement Pipeline for Agentic RAG Systems](http://arxiv.org/abs/2604.17677v1)
  来源：arXiv | 日期：2026-04-20 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）系统依赖向量表示的几何特性来检索上下文证据。当源文档在连续文本中交织多个主题时，标准向量化会导致语义不同的内容在嵌入空间中占据重叠区域，本文将此定义为“语义纠缠”。作者将纠缠形式化为嵌入空间中跨主题重叠的度量，并定义了纠缠指数（EI）作为定量指标。研究表明，高 EI 会限制余弦相似度检索下的 Top-K 检索精度。为此，本文提出了语义解纠缠流水线（SDP），这是一个在嵌入前重构文档的四阶段预处理框架。该框架引入了由...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 其他

- [WorldDB: A Vector Graph-of-Worlds Memory Engine with Ontology-Aware Write-Time Reconciliation](http://arxiv.org/abs/2604.18478v1)
  来源：arXiv | 日期：2026-04-20 | 相关度：0.7 | 新颖度：7.29
  匹配主题：未命中具体主题
  中文摘要：持久化内存是限制无状态聊天机器人向长期运行智能体系统转型的瓶颈。传统扁平向量检索增强生成（RAG）存在事实碎片化、跨会话身份丢失以及缺乏知识更替或矛盾处理机制的问题。本文提出 WorldDB 存储引擎，其核心包含三项创新：(i) 节点即“世界”，作为包含内部子图、本体范围和组合嵌入的递归容器；(ii) 节点采用内容寻址且不可变，通过 Merkle 树式审计追踪记录变更；(iii) 边是写入时程序，通过预设处理程序（如 on_insert...
  为什么值得看：WorldDB: A Vector Graph-of-Worlds Memory 与你的主题有弱匹配，暂时保留作低优先级跟踪。
