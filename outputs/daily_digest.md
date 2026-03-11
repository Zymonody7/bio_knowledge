# 每日论文监控日报 (2026-03-11)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 41 篇新论文。

## 抓取状态

- arXiv：成功，命中 44 篇
- PubMed：成功，命中 29 篇
- bioRxiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='api.biorxiv.org', port=443): Read timed out. (read timeout=60)
- medRxiv：成功，命中 9 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [OPENXRD: A Comprehensive Benchmark Framework for LLM/MLLM XRD Question Answering](http://arxiv.org/abs/2507.09155v2)
  来源：arXiv | 日期：2025-07-12 | 相关度：7.5 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：We introduce OPENXRD, a comprehensive benchmarking framework for evaluating large language models (LLMs) and multimodal LLMs (MLLMs) in crystallography question answering. The framework measures context assimilation, or ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MITRA: An AI Assistant for Knowledge Retrieval in Physics Collaborations](http://arxiv.org/abs/2603.09800v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：6.55 | 新颖度：7.88
  匹配主题：foundation_model_agent
  中文摘要：Large-scale scientific collaborations, such as the Compact Muon Solenoid (CMS) at CERN, produce a vast and ever-growing corpus of internal documentation. Navigating this complex information landscape presents a significa...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [AI Agents, Language, Deep Learning and the Next Revolution in Science](http://arxiv.org/abs/2603.07940v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：8.5 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Modern science is reaching a critical inflection point. Instruments across disciplines, from particle physics and astronomy to genomics and climate modeling, now produce data of such scale, diversity, and interdependence...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [A context-augmented large language model for accurate precision oncology medicine recommendations.](https://pubmed.ncbi.nlm.nih.gov/41544626/)
  来源：PubMed | 日期：2026-03-09 | 相关度：7.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：The rapid expansion of molecularly informed therapies in oncology, coupled with evolving regulatory food and drug administration (FDA) approvals, poses a challenge for oncologists seeking to integrate precision oncology ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 可追踪

### Foundation Model / Agent

- [DEO: Training-Free Direct Embedding Optimization for Negation-Aware Retrieval](http://arxiv.org/abs/2603.09185v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：7.5 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) have enabled diverse retrieval methods. However, existing retrieval methods often fail to accurately retrieve results for negation ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CMMR-VLN: Vision-and-Language Navigation via Continual Multimodal Memory Retrieval](http://arxiv.org/abs/2603.07997v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：6.8 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Although large language models (LLMs) are introduced into vision-and-language navigation (VLN) to improve instruction comprehension and generalization, existing LLM- based VLN lacks the ability to selectively recall and ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HDLxGraph: Bridging Large Language Models and HDL Repositories via HDL Graph Databases](http://arxiv.org/abs/2505.15701v2)
  来源：arXiv | 日期：2025-05-21 | 相关度：6.55 | 新颖度：7.2
  匹配主题：foundation_model_agent
  中文摘要：Retrieval Augmented Generation (RAG) is an essential agent for Large Language Model (LLM) aided Description Language (HDL) tasks, addressing the challenges of limited training data and prohibitively long prompts. However...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LongAudio-RAG: Event-Grounded Question Answering over Multi-Hour Long Audio](http://arxiv.org/abs/2602.14612v3)
  来源：arXiv | 日期：2026-02-16 | 相关度：6.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Long-duration audio is increasingly common in industrial and consumer settings, yet reviewing multi-hour recordings is impractical, motivating systems that answer natural-language queries with precise temporal grounding ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Fanar-Sadiq: A Multi-Agent Architecture for Grounded Islamic QA](http://arxiv.org/abs/2603.08501v2)
  来源：arXiv | 日期：2026-03-09 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) can answer religious knowledge queries fluently, yet they often hallucinate and misattribute sources, which is especially consequential in Islamic settings where users expect grounding in can...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Can Parents and Patients Understand Myopia Using Large Language Model-Based Chatbots?](https://www.medrxiv.org/content/10.64898/2026.03.09.26347905v1)
  来源：medRxiv | 日期：2026-03-10 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Purpose: This study aimed to compare the reliability of myopia-related information from AI chatbots using a set of commonly asked questions by parents and patients on myopia, which is an emerging disease of the 21st-cent...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Accelerating Exploratory Clinical Research: An LLM-Powered Framework for Cross-Study Data Harmonization and Natural Language Querying](https://www.medrxiv.org/content/10.64898/2026.03.04.26345603v1)
  来源：medRxiv | 日期：2026-03-09 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Clinical research depends on high quality data that is standardized, accessible and interoperable. Yet evolving data standards over time and variations in their implementation hinder the secondary use of clinical trial d...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Epistemic Closure: Autonomous Mechanism Completion for Physically Consistent Simulation](http://arxiv.org/abs/2603.09756v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：5.45 | 新颖度：7.09
  匹配主题：foundation_model_agent
  中文摘要：The integration of Large Language Models (LLMs) into scientific discovery is currently hindered by the Implicit Context problem, where governing equations extracted from literature contain invisible thermodynamic assumpt...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evaluation of LLMs in retrieving food and nutritional context for RAG systems](http://arxiv.org/abs/2603.09704v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：5.45 | 新颖度：6.98
  匹配主题：foundation_model_agent
  中文摘要：In this article, we evaluate four Large Language Models (LLMs) and their effectiveness at retrieving data within a specialized Retrieval-Augmented Generation (RAG) system, using a comprehensive food composition database....
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Towards Robust Retrieval-Augmented Generation Based on Knowledge Graph: A Comparative Analysis](http://arxiv.org/abs/2603.05698v2)
  来源：arXiv | 日期：2026-03-05 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) was introduced to enhance the capabilities of Large Language Models (LLMs) beyond their encoded prior knowledge. This is achieved by providing LLMs with an external source of knowledg...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery](http://arxiv.org/abs/2603.08127v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：The increasing adoption of Large Language Models (LLMs) has enabled AI scientists to perform complex end-to-end scientific discovery tasks requiring coordination of specialized roles, including idea generation and experi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [BRIDGE: Benchmark for multi-hop Reasoning In long multimodal Documents with Grounded Evidence](http://arxiv.org/abs/2603.07931v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：6.8 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Multi-hop question answering (QA) is widely used to evaluate the reasoning capabilities of large language models, yet most benchmarks focus on final answer correctness and overlook intermediate reasoning, especially in l...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Retrieval-Augmented Anatomical Guidance for Text-to-CT Generation](http://arxiv.org/abs/2603.08305v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Text-conditioned generative models for volumetric medical imaging provide semantic control but lack explicit anatomical guidance, often resulting in outputs that are spatially ambiguous or anatomically inconsistent. In c...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [RexDrug: Reliable Multi-Drug Combination Extraction through Reasoning-Enhanced LLMs](http://arxiv.org/abs/2603.08166v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Automated Drug Combination Extraction (DCE) from large-scale biomedical literature is crucial for advancing precision medicine and pharmacological research. However, existing relation extraction methods primarily focus o...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [MMGraphRAG: Bridging Vision and Language with Interpretable Multimodal Knowledge Graphs](http://arxiv.org/abs/2507.20804v2)
  来源：arXiv | 日期：2025-07-28 | 相关度：6.8 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) often suffer from hallucinations, which Retrieval-Augmented Generation (RAG) and GraphRAG mitigate by incorporating external knowledge and knowledge graphs (KGs). However, GraphRAG remains te...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [EmbC-Test: How to Speed Up Embedded Software Testing Using LLMs and RAG](http://arxiv.org/abs/2603.09497v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：6.15 | 新颖度：6.68
  匹配主题：foundation_model_agent
  中文摘要：Manual development of automatic tests for embedded C software is a strenuous and time-consuming task that does not scale well. With the accelerating pace of software release cycles, verification increasingly becomes the ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [The Virtuous Cycle: AI-Powered Vector Search and Vector Search-Augmented AI](http://arxiv.org/abs/2603.09347v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：6.15 | 新颖度：6.26
  匹配主题：foundation_model_agent
  中文摘要：Modern AI and vector search are rapidly converging, forming a promising research frontier in intelligent information systems. On one hand, advances in AI have substantially improved the semantic accuracy and efficiency o...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Reverse Distillation: Consistently Scaling Protein Language Model Representations](http://arxiv.org/abs/2603.07710v1)
  来源：arXiv | 日期：2026-03-08 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Unlike the predictable scaling laws in natural language processing and computer vision, protein language models (PLMs) scale poorly: for many tasks, models within the same family plateau or even decrease in performance, ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Enhancing Retrieval-Augmented Generation with Entity Linking for Educational Platforms](http://arxiv.org/abs/2512.05967v2)
  来源：arXiv | 日期：2025-12-05 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：In the era of Large Language Models (LLMs), Retrieval-Augmented Generation (RAG) architectures are gaining significant attention for their ability to ground language generation in reliable knowledge sources. Despite thei...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SPD-RAG: Sub-Agent Per Document Retrieval-Augmented Generation](http://arxiv.org/abs/2603.08329v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Answering complex, real-world queries often requires synthesizing facts scattered across vast document corpora. In these settings, standard retrieval-augmented generation (RAG) pipelines suffer from incomplete evidence c...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [TaSR-RAG: Taxonomy-guided Structured Reasoning for Retrieval-Augmented Generation](http://arxiv.org/abs/2603.09341v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：4.75 | 新颖度：6.23
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) helps large language models (LLMs) answer knowledge-intensive and time-sensitive questions by conditioning generation on external evidence. However, most RAG systems still retrieve un...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [InterMind: Doctor-Patient-Family Interactive Depression Assessment Empowered by Large Language Models](http://arxiv.org/abs/2409.14878v2)
  来源：arXiv | 日期：2024-09-23 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Depression poses significant challenges to patients and healthcare organizations, necessitating efficient assessment methods. Existing paradigms typically focus on a patient-doctor way that overlooks multi-role interacti...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Beyond Relevance: On the Relationship Between Retrieval and RAG Information Coverage](http://arxiv.org/abs/2603.08819v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：3.45 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) systems combine document retrieval with a generative model to address complex information seeking tasks like report generation. While the relationship between retrieval quality and ge...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AutoAgent: Evolving Cognition and Elastic Memory Orchestration for Adaptive Agents](http://arxiv.org/abs/2603.09716v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：2.1 | 新颖度：7.75
  匹配主题：未命中具体主题
  中文摘要：Autonomous agent frameworks still struggle to reconcile long-term experiential learning with real-time, context-sensitive decision-making. In practice, this gap appears as static cognition, rigid workflow dependence, and...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [World2Mind: Cognition Toolkit for Allocentric Spatial Reasoning in Foundation Models](http://arxiv.org/abs/2603.09774v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：2.05 | 新颖度：7.38
  匹配主题：foundation_model_agent
  中文摘要：针对多模态基础模型（MFM）在空间推理中存在的过拟合及 2D 感知局限，本文提出 World2Mind，一种无需训练的空间智能工具包。该工具受生物空间认知机制启发，利用 3D 重建与实例分割技术构建结构化空间认知地图，使模型能主动获取地标与路径的空间知识。其核心是“异中心空间树”（AST），通过椭圆参数精确建模地标的俯视布局，提供几何拓扑先验。为应对 3D 重建的误差，设计了包含工具调用评估、模态解耦线索收集及几何-语义交织推理的三阶段...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Quantifying the Accuracy and Cost Impact of Design Decisions in Budget-Constrained Agentic LLM Search](http://arxiv.org/abs/2603.08877v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：1.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：代理检索增强生成（Agentic RAG）系统结合了迭代搜索、规划提示和检索后端，但在实际部署中面临工具调用和 Token 消耗的严格预算限制。本研究通过受控测量实验，系统评估了搜索深度、检索策略和生成预算在固定约束下对准确率与成本的影响。研究引入了“预算受限代理搜索”（BCAS）评估框架，该框架支持模型无关的预算监控与工具调用拦截。通过对 6 种大语言模型和 3 个问答基准测试的对比实验发现：准确率随搜索次数增加而提升，但存在明显的边...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Routing without Forgetting](http://arxiv.org/abs/2603.09576v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：0.7 | 新颖度：6.91
  匹配主题：未命中具体主题
  中文摘要：针对 Transformer 的持续学习，传统方法（如 Prompt、Adapter 或 LoRA）依赖梯度优化，在数据流仅观察一次的在线持续学习（OCL）中表现不佳。本文提出“不遗忘路由”（RwF）架构，将持续学习重新定义为路由问题。RwF 引入受现代 Hopfield 网络启发的能量关联检索层，无需显式任务标识或重复优化。通过在每层对 token 嵌入进行单步关联检索（基于严格凸自由能泛函的闭式解最小化），RwF 实现了输入条件下的...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Learning Hierarchical Knowledge in Text-Rich Networks with Taxonomy-Informed Representation Learning](http://arxiv.org/abs/2603.08159v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：层级知识结构在生物医学本体和检索增强生成中至关重要，但在文本丰富网络（TRNs）的建模中常被忽视。现有方法多侧重扁平语义，忽略了文档间固有的层级关系。本文提出 TIER 框架，旨在构建隐式层级分类体系并将其整合至节点表示学习中。TIER 首先利用相似性引导的对比学习构建聚类友好型嵌入空间，随后通过层级 K-Means 结合大语言模型（LLM）驱动的聚类优化，构建语义连贯的分类体系。接着，引入基于共表型相关系数（Cophenetic Co...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Explainable Innovation Engine: Dual-Tree Agent-RAG with Methods-as-Nodes and Verifiable Write-Back](http://arxiv.org/abs/2603.09192v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：针对检索增强生成（RAG）在多步合成中缺乏控制力的问题，本文提出一种“可解释创新引擎”，将知识单元从传统的文本块升级为“方法节点（methods-as-nodes）”。该引擎构建了双树结构：用于追踪推导过程的加权方法溯源树，以及用于高效导航的分层聚类抽象树。推理时，策略智能体通过显式合成算子（如归纳、演绎、类比）构建新节点，并记录可审计轨迹。验证评分层负责剔除低质量候选并回写验证节点，实现知识库的持续增长。在六个领域的专家评估显示，该方...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Overview of the TREC 2025 Retrieval Augmented Generation (RAG) Track](http://arxiv.org/abs/2603.09891v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：1.4 | 新颖度：7.4
  匹配主题：未命中具体主题
  中文摘要：2025年TREC检索增强生成（RAG）赛道是该系列的第二届，旨在推动集成检索与生成技术以解决复杂的现实信息需求。本届挑战赛引入了长篇、多句的叙述性查询，以模拟深度搜索任务中对推理驱动响应的需求。参赛者需设计结合检索与生成的流水线，并确保透明度与事实依据。该赛道利用MS MARCO V2.1语料库，采用涵盖相关性评估、响应完整性、归因验证和一致性分析的多层评估框架。通过强调多维叙述和富含归因的回答，该赛道旨在促进开发可信、上下文感知的R...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Amortized Phylodynamic Inference with Neural Bayes Estimators and Recursive Neural Networks](http://arxiv.org/abs/2603.08345v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：2.6 | 新颖度：5.25
  匹配主题：sequencing_bioinformatics
  中文摘要：Phylodynamics is used to estimate epidemic dynamics from phylogenetic trees or genomic sequences of pathogens, but the likelihood calculations needed can be challenging for complex models. We present a neural Bayes estim...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [LooComp: Leverage Leave-One-Out Strategy to Encoder-only Transformer for Efficient Query-aware Context Compression](http://arxiv.org/abs/2603.09222v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：2.1 | 新颖度：5.8
  匹配主题：未命中具体主题
  中文摘要：高效的上下文压缩对于提升问答系统的准确性与扩展性至关重要。本文提出 LooComp，一种基于留一法（Leave-One-Out, LOO）策略的查询驱动上下文剪枝框架。该方法利用轻量级 Encoder-only Transformer，通过衡量省略特定句子后线索丰富度的变化来识别对回答查询至关关键的信息。模型采用复合排序损失进行训练，确保关键句子具有显著的边际权重，而非关键句子保持中性。实验结果显示，LooComp 在保持高精确匹配（E...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Flow Matching Meets Biology and Life Science: A Survey](http://arxiv.org/abs/2507.17731v2)
  来源：arXiv | 日期：2025-07-23 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：过去十年，生成式模型（如GAN、MAE和扩散模型）在分子设计、蛋白质生成及药物研发等领域取得了突破。近期，流匹配（Flow Matching, FM）作为一种比扩散模型更高效、强大的替代方案，在生命科学领域引起广泛关注。本文首次全面综述了流匹配在生物领域的最新进展。文章系统回顾了流匹配的基础理论及其变体，并将其应用归纳为三大核心领域：生物序列建模、分子生成与设计、以及多肽与蛋白质生成。此外，本文还总结了常用的数据集和软件工具，并探讨了未...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Human-AI Collaboration for Scaling Agile Regression Testing: An Agentic-AI Teammate from Manual to Automated Testing](http://arxiv.org/abs/2603.08190v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：针对敏捷开发中测试脚本编写滞后于需求规格的瓶颈，本文与西门子旗下的Hacon合作，提出了一种基于智能体（Agentic AI）的自动化回归测试方法。该方案采用检索增强生成（RAG）和多智能体架构，直接从验证过的规格说明中生成系统级测试脚本，旨在不牺牲人工监督的前提下加速自动化进程。通过对工业制品和从业者反馈的混合方法分析，结果表明该AI队友显著提升了脚本产出效率并减少了人工编写工作量。研究强调了清晰的规格说明和人工审核对保障质量的重要性...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Understand Then Memory: A Cognitive Gist-Driven RAG Framework with Global Semantic Diffusion](http://arxiv.org/abs/2602.15895v2)
  来源：arXiv | 日期：2026-02-11 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）通过引入外部知识缓解大模型幻觉，但现有框架的离散文本表示常导致语义完整性缺失。受人类情境记忆机制启发，本文提出 CogitoRAG 框架。在离线索引阶段，该框架将非结构化语料推导为“要义记忆语料”，并构建集成实体、关系事实和记忆节点的知识图谱。在线检索阶段，通过查询分解模块将复杂问题拆解，并利用实体扩散模块在图谱上进行关联检索，结合结构相关性与实体频率奖励机制。此外，提出 CogniRank 算法，融合扩散分数与语...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Multi-Agent Off-World Exploration for Sparse Evidence Discovery via Gaussian Belief Mapping and Dual-Domain Coverage](http://arxiv.org/abs/2603.07650v1)
  来源：arXiv | 日期：2026-03-08 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：针对地外多机器人探测中目标稀疏、感知受限及地形危险等挑战，本文提出一种基于高斯信念映射和双域覆盖的多智能体信息路径规划（IPP）框架。该方法利用高斯过程（GP）维护兴趣与风险信念，并结合轨迹意图表示，支持多智能体间的协调决策。框架通过双域策略优先搜索预设兴趣区（AOI），同时保留对区外的有限探索，有效解决了AOI偏差导致的漏检问题。此外，风险感知设计平衡了信息增益与操作安全。在模拟月球环境的实验表明，该方法在不同预算和通信范围内均优于采...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Conversational Artificial Intelligence-Enabled Molecular Characterization of Sezary Syndrome Reveals Distinct Pathway-Level Alterations Compared with Non-Sezary Cutaneous T-Cell Lymphoma](https://www.medrxiv.org/content/10.64898/2026.03.09.26347970v1)
  来源：medRxiv | 日期：2026-03-10 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：塞扎里综合征（SS）是皮肤T细胞淋巴瘤（CTCL）的一种侵袭性白血病变体。本研究利用对话式人工智能（AI）精准肿瘤学平台，对哥伦比亚大学CTCL队列（26例SS和17例非SS CTCL）的体细胞突变数据进行二次分析。结果显示，SS与非SS CTCL的肿瘤突变负荷（TMB）无显著差异（p=0.83）。但在通路水平上，SS显著富集了表观遗传调节因子、抑癌基因、细胞周期控制、NFAT信号及凋亡/免疫调节相关的突变；而非SS CTCL则在MAP...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
