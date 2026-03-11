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

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [OPENXRD: A Comprehensive Benchmark Framework for LLM/MLLM XRD Question Answering](http://arxiv.org/abs/2507.09155v2)
  来源：arXiv | 日期：2025-07-12 | 相关度：7.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：We introduce OPENXRD, a comprehensive benchmarking framework for evaluating large language models (LLMs) and multimodal LLMs (MLLMs) in crystallography question answering. The framework measures context assimilation, or ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DEO: Training-Free Direct Embedding Optimization for Negation-Aware Retrieval](http://arxiv.org/abs/2603.09185v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：7.5 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) have enabled diverse retrieval methods. However, existing retrieval methods often fail to accurately retrieve results for negation ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CMMR-VLN: Vision-and-Language Navigation via Continual Multimodal Memory Retrieval](http://arxiv.org/abs/2603.07997v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：6.8 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Although large language models (LLMs) are introduced into vision-and-language navigation (VLN) to improve instruction comprehension and generalization, existing LLM- based VLN lacks the ability to selectively recall and ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MITRA: An AI Assistant for Knowledge Retrieval in Physics Collaborations](http://arxiv.org/abs/2603.09800v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：6.55 | 新颖度：2.67
  匹配主题：foundation_model_agent
  中文摘要：Large-scale scientific collaborations, such as the Compact Muon Solenoid (CMS) at CERN, produce a vast and ever-growing corpus of internal documentation. Navigating this complex information landscape presents a significa...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HDLxGraph: Bridging Large Language Models and HDL Repositories via HDL Graph Databases](http://arxiv.org/abs/2505.15701v2)
  来源：arXiv | 日期：2025-05-21 | 相关度：6.55 | 新颖度：2.2
  匹配主题：foundation_model_agent
  中文摘要：Retrieval Augmented Generation (RAG) is an essential agent for Large Language Model (LLM) aided Description Language (HDL) tasks, addressing the challenges of limited training data and prohibitively long prompts. However...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LongAudio-RAG: Event-Grounded Question Answering over Multi-Hour Long Audio](http://arxiv.org/abs/2602.14612v3)
  来源：arXiv | 日期：2026-02-16 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Long-duration audio is increasingly common in industrial and consumer settings, yet reviewing multi-hour recordings is impractical, motivating systems that answer natural-language queries with precise temporal grounding ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [BRIDGE: Benchmark for multi-hop Reasoning In long multimodal Documents with Grounded Evidence](http://arxiv.org/abs/2603.07931v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：6.8 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Multi-hop question answering (QA) is widely used to evaluate the reasoning capabilities of large language models, yet most benchmarks focus on final answer correctness and overlook intermediate reasoning, especially in l...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [AI Agents, Language, Deep Learning and the Next Revolution in Science](http://arxiv.org/abs/2603.07940v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：8.5 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Modern science is reaching a critical inflection point. Instruments across disciplines, from particle physics and astronomy to genomics and climate modeling, now produce data of such scale, diversity, and interdependence...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MMGraphRAG: Bridging Vision and Language with Interpretable Multimodal Knowledge Graphs](http://arxiv.org/abs/2507.20804v2)
  来源：arXiv | 日期：2025-07-28 | 相关度：6.8 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) often suffer from hallucinations, which Retrieval-Augmented Generation (RAG) and GraphRAG mitigate by incorporating external knowledge and knowledge graphs (KGs). However, GraphRAG remains te...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [EmbC-Test: How to Speed Up Embedded Software Testing Using LLMs and RAG](http://arxiv.org/abs/2603.09497v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：6.15 | 新颖度：1.47
  匹配主题：foundation_model_agent
  中文摘要：Manual development of automatic tests for embedded C software is a strenuous and time-consuming task that does not scale well. With the accelerating pace of software release cycles, verification increasingly becomes the ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [A context-augmented large language model for accurate precision oncology medicine recommendations.](https://pubmed.ncbi.nlm.nih.gov/41544626/)
  来源：PubMed | 日期：2026-03-09 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：The rapid expansion of molecularly informed therapies in oncology, coupled with evolving regulatory food and drug administration (FDA) approvals, poses a challenge for oncologists seeking to integrate precision oncology ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Fanar-Sadiq: A Multi-Agent Architecture for Grounded Islamic QA](http://arxiv.org/abs/2603.08501v2)
  来源：arXiv | 日期：2026-03-09 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) can answer religious knowledge queries fluently, yet they often hallucinate and misattribute sources, which is especially consequential in Islamic settings where users expect grounding in can...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Can Parents and Patients Understand Myopia Using Large Language Model-Based Chatbots?](https://www.medrxiv.org/content/10.64898/2026.03.09.26347905v1)
  来源：medRxiv | 日期：2026-03-10 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Purpose: This study aimed to compare the reliability of myopia-related information from AI chatbots using a set of commonly asked questions by parents and patients on myopia, which is an emerging disease of the 21st-cent...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Accelerating Exploratory Clinical Research: An LLM-Powered Framework for Cross-Study Data Harmonization and Natural Language Querying](https://www.medrxiv.org/content/10.64898/2026.03.04.26345603v1)
  来源：medRxiv | 日期：2026-03-09 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Clinical research depends on high quality data that is standardized, accessible and interoperable. Yet evolving data standards over time and variations in their implementation hinder the secondary use of clinical trial d...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Epistemic Closure: Autonomous Mechanism Completion for Physically Consistent Simulation](http://arxiv.org/abs/2603.09756v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：5.45 | 新颖度：1.88
  匹配主题：foundation_model_agent
  中文摘要：The integration of Large Language Models (LLMs) into scientific discovery is currently hindered by the Implicit Context problem, where governing equations extracted from literature contain invisible thermodynamic assumpt...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evaluation of LLMs in retrieving food and nutritional context for RAG systems](http://arxiv.org/abs/2603.09704v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：5.45 | 新颖度：1.76
  匹配主题：foundation_model_agent
  中文摘要：In this article, we evaluate four Large Language Models (LLMs) and their effectiveness at retrieving data within a specialized Retrieval-Augmented Generation (RAG) system, using a comprehensive food composition database....
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Towards Robust Retrieval-Augmented Generation Based on Knowledge Graph: A Comparative Analysis](http://arxiv.org/abs/2603.05698v2)
  来源：arXiv | 日期：2026-03-05 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) was introduced to enhance the capabilities of Large Language Models (LLMs) beyond their encoded prior knowledge. This is achieved by providing LLMs with an external source of knowledg...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery](http://arxiv.org/abs/2603.08127v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：The increasing adoption of Large Language Models (LLMs) has enabled AI scientists to perform complex end-to-end scientific discovery tasks requiring coordination of specialized roles, including idea generation and experi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond Relevance: On the Relationship Between Retrieval and RAG Information Coverage](http://arxiv.org/abs/2603.08819v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：3.45 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) systems combine document retrieval with a generative model to address complex information seeking tasks like report generation. While the relationship between retrieval quality and ge...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AutoAgent: Evolving Cognition and Elastic Memory Orchestration for Adaptive Agents](http://arxiv.org/abs/2603.09716v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：2.1 | 新颖度：2.54
  匹配主题：未命中具体主题
  中文摘要：Autonomous agent frameworks still struggle to reconcile long-term experiential learning with real-time, context-sensitive decision-making. In practice, this gap appears as static cognition, rigid workflow dependence, and...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [World2Mind: Cognition Toolkit for Allocentric Spatial Reasoning in Foundation Models](http://arxiv.org/abs/2603.09774v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：2.05 | 新颖度：2.17
  匹配主题：foundation_model_agent
  中文摘要：稳健的空间推理是当前多模态基础模型（MFMs）面临的核心挑战。现有方法常因过度拟合3D定位数据的统计捷径或局限于2D视觉感知，导致在未知场景中的推理准确性与泛化能力受限。受生物智能空间认知映射机制启发，我们提出了World2Mind，一个无需训练的空间智能工具包。该工具包利用3D重建和实例分割模型构建结构化的空间认知地图，使MFMs能够主动获取感兴趣地标与路径的目标空间知识。为提供稳健的几何拓扑先验，World2Mind合成了异向空间树...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Quantifying the Accuracy and Cost Impact of Design Decisions in Budget-Constrained Agentic LLM Search](http://arxiv.org/abs/2603.08877v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：1.4 | 新颖度：1.5
  匹配主题：未命中具体主题
  中文摘要：代理检索增强生成（Agentic RAG）系统通过结合迭代搜索、规划提示和检索后端来解决复杂问题，但在实际部署中，工具调用次数和生成 Token 数通常受到严格的预算限制。本研究针对固定约束下搜索深度、检索策略和生成预算对准确性与成本的影响进行了受控测量研究。研究引入了“预算受限代理搜索”（BCAS），这是一种模型无关的评估框架，能够实时显示剩余预算并管控工具使用。通过在 6 种大语言模型（LLMs）和 3 个问答基准测试上进行对比实验...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Routing without Forgetting](http://arxiv.org/abs/2603.09576v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：0.7 | 新颖度：1.7
  匹配主题：未命中具体主题
  中文摘要：Transformer 的持续学习通常采用参数高效适配方法（如 Prompt、Adapter 或 LoRA），但在在线持续学习（OCL）场景下，由于数据以非平稳流形式到达且样本仅出现一次，依赖梯度更新的适配方法难以奏效。本文将持续学习重新定义为路由问题，提出了“不遗忘路由”（RwF）架构。RwF 受到现代 Hopfield 网络的启发，在 Transformer 中集成了基于能量的关联检索层。该方法不依赖存储或合并特定任务的 Promp...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Learning Hierarchical Knowledge in Text-Rich Networks with Taxonomy-Informed Representation Learning](http://arxiv.org/abs/2603.08159v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：层级知识结构在现实世界中广泛存在，对于从粗到细组织语义信息至关重要。虽然此类结构已应用于分类系统和生物医学本体，但在文本丰富网络（TRN）中，节点包含丰富文本且边编码语义关系，其层级潜力尚未得到充分挖掘。现有 TRN 学习方法多侧重于扁平语义建模，忽视了文档中嵌入的层级语义。为此，本研究提出 TIER（层级分类信息驱动的表示学习）。TIER 首先通过相似性引导的对比学习构建聚类友好的嵌入空间，随后执行层级 K-Means 并利用大语言模...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Explainable Innovation Engine: Dual-Tree Agent-RAG with Methods-as-Nodes and Verifiable Write-Back](http://arxiv.org/abs/2603.09192v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）虽能提升事实准确性，但多数系统依赖扁平的文本块检索，且对多步合成过程的控制有限。本研究提出一种“可解释创新引擎”，将知识单元从传统的文本块升级为“方法节点（methods-as-nodes）”。该引擎维护两个核心结构：用于可追溯推导的加权方法溯源树，以及用于高效自顶向下导航的层次聚类抽象树。在推理阶段，策略智能体选择显式的合成算子（如归纳、演绎、类比）来构建新的方法节点，并记录可审计的执行轨迹。随后，验证器-评分器...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Retrieval-Augmented Anatomical Guidance for Text-to-CT Generation](http://arxiv.org/abs/2603.08305v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Text-conditioned generative models for volumetric medical imaging provide semantic control but lack explicit anatomical guidance, often resulting in outputs that are spatially ambiguous or anatomically inconsistent. In c...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [RexDrug: Reliable Multi-Drug Combination Extraction through Reasoning-Enhanced LLMs](http://arxiv.org/abs/2603.08166v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Automated Drug Combination Extraction (DCE) from large-scale biomedical literature is crucial for advancing precision medicine and pharmacological research. However, existing relation extraction methods primarily focus o...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Overview of the TREC 2025 Retrieval Augmented Generation (RAG) Track](http://arxiv.org/abs/2603.09891v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：1.4 | 新颖度：2.19
  匹配主题：未命中具体主题
  中文摘要：第二届 TREC 检索增强生成（RAG）赛道旨在推进整合检索与生成技术的系统研究，以解决复杂的现实世界信息需求。在 2024 年首届赛道的基础上，本届挑战赛引入了长篇、多句的叙述性查询，以更好地反映深度搜索任务中日益增长的推理驱动响应需求。参赛者需设计结合检索与生成的流水线，同时确保透明度和事实依据。该赛道利用 MS MARCO V2.1 语料库，并采用多层评估框架，涵盖相关性评估、回答完整性、归因验证和一致性分析。通过强调多维叙述和来...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [The Virtuous Cycle: AI-Powered Vector Search and Vector Search-Augmented AI](http://arxiv.org/abs/2603.09347v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：6.15 | 新颖度：1.05
  匹配主题：foundation_model_agent
  中文摘要：Modern AI and vector search are rapidly converging, forming a promising research frontier in intelligent information systems. On one hand, advances in AI have substantially improved the semantic accuracy and efficiency o...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Reverse Distillation: Consistently Scaling Protein Language Model Representations](http://arxiv.org/abs/2603.07710v1)
  来源：arXiv | 日期：2026-03-08 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Unlike the predictable scaling laws in natural language processing and computer vision, protein language models (PLMs) scale poorly: for many tasks, models within the same family plateau or even decrease in performance, ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Enhancing Retrieval-Augmented Generation with Entity Linking for Educational Platforms](http://arxiv.org/abs/2512.05967v2)
  来源：arXiv | 日期：2025-12-05 | 相关度：5.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：In the era of Large Language Models (LLMs), Retrieval-Augmented Generation (RAG) architectures are gaining significant attention for their ability to ground language generation in reliable knowledge sources. Despite thei...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SPD-RAG: Sub-Agent Per Document Retrieval-Augmented Generation](http://arxiv.org/abs/2603.08329v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Answering complex, real-world queries often requires synthesizing facts scattered across vast document corpora. In these settings, standard retrieval-augmented generation (RAG) pipelines suffer from incomplete evidence c...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [TaSR-RAG: Taxonomy-guided Structured Reasoning for Retrieval-Augmented Generation](http://arxiv.org/abs/2603.09341v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：4.75 | 新颖度：1.02
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) helps large language models (LLMs) answer knowledge-intensive and time-sensitive questions by conditioning generation on external evidence. However, most RAG systems still retrieve un...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Amortized Phylodynamic Inference with Neural Bayes Estimators and Recursive Neural Networks](http://arxiv.org/abs/2603.08345v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：2.6 | 新颖度：0.25
  匹配主题：sequencing_bioinformatics
  中文摘要：Phylodynamics is used to estimate epidemic dynamics from phylogenetic trees or genomic sequences of pathogens, but the likelihood calculations needed can be challenging for complex models. We present a neural Bayes estim...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [LooComp: Leverage Leave-One-Out Strategy to Encoder-only Transformer for Efficient Query-aware Context Compression](http://arxiv.org/abs/2603.09222v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：2.1 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：高效的上下文压缩对于提升问答系统的准确性与可扩展性至关重要。在检索增强生成（RAG）场景下，上下文需具备快速、紧凑且精确的特点，以确保线索充足并降低大语言模型（LLM）阅读器的推理成本。本文提出 LooComp，一种基于边际（margin-based）的查询驱动上下文剪枝框架。该方法通过衡量省略特定句子时线索丰富度的变化（即留一法策略），识别对回答查询至关重要的核心句子。模型基于轻量级仅编码器（encoder-only）Transfor...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Flow Matching Meets Biology and Life Science: A Survey](http://arxiv.org/abs/2507.17731v2)
  来源：arXiv | 日期：2025-07-23 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：过去十年，生成式建模（如生成对抗网络、掩码自编码器和扩散模型）显著改变了生物学研究，在分子设计、蛋白质生成、催化发现和药物研发等领域取得了突破性进展。近期，流匹配（Flow Matching）作为一种比扩散模型更强大且高效的替代方案脱颖而出，在生物与生命科学领域的应用兴趣日益增长。本文提供了关于流匹配及其在生物领域应用的首次全面综述。文章首先系统回顾了流匹配的基础理论及其变体，随后将其应用归纳为三大核心领域：生物序列建模、分子生成与设计...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Human-AI Collaboration for Scaling Agile Regression Testing: An Agentic-AI Teammate from Manual to Automated Testing](http://arxiv.org/abs/2603.08190v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：敏捷开发组织日益依赖自动化回归测试以维持高质量交付。然而，随着系统扩展和需求演进，出现了一个持续性的瓶颈：测试规范的产出速度超过了其转化为可执行脚本的速度，导致手动工作量堆积和发布延迟。本研究与西门子旗下的 Hacon 公司合作，提出了一种基于智能体（Agentic AI）的方法，旨在直接从验证过的规范中生成系统级测试脚本，从而在不牺牲人工监督的前提下加速自动化进程。该方案采用了集成到 Hacon 敏捷工作流中的检索增强（RAG）多智能...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Understand Then Memory: A Cognitive Gist-Driven RAG Framework with Global Semantic Diffusion](http://arxiv.org/abs/2602.15895v2)
  来源：arXiv | 日期：2026-02-11 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）通过引入外部知识缓解大语言模型（LLM）的幻觉问题，但现有框架中离散的文本表示常导致语义完整性缺失和检索偏差。受人类情景记忆机制启发，本研究提出 CogitoRAG 框架。在离线索引阶段，该框架将非结构化语料推演为要义记忆语料（gist memory corpora），并构建集成实体、关系事实和记忆节点的超维知识图谱。在线检索阶段，查询分解模块将复杂查询拆解为子查询，模拟人类认知过程。随后，实体扩散模块利用结构相关...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Multi-Agent Off-World Exploration for Sparse Evidence Discovery via Gaussian Belief Mapping and Dual-Domain Coverage](http://arxiv.org/abs/2603.07650v1)
  来源：arXiv | 日期：2026-03-08 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：地外多机器人探测面临目标稀疏、感知受限、地形危险及通信受限等严峻挑战。许多具有科学价值的线索在视觉上具有模糊性，通常需要近距离观察，因此高效且安全的信息路径规划（IPP）至关重要。现有方法多依赖预定义的感兴趣区域（AOI），但这可能存在偏差或不完整，且对地形风险的处理通常仅采用软惩罚，难以规避不可恢复的危险区域。为此，本研究提出一种基于高斯信念映射和双域覆盖的多智能体信息路径规划框架，专门用于稀疏证据发现。该方法维护基于高斯过程（GP）...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [InterMind: Doctor-Patient-Family Interactive Depression Assessment Empowered by Large Language Models](http://arxiv.org/abs/2409.14878v2)
  来源：arXiv | 日期：2024-09-23 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Depression poses significant challenges to patients and healthcare organizations, necessitating efficient assessment methods. Existing paradigms typically focus on a patient-doctor way that overlooks multi-role interacti...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Conversational Artificial Intelligence-Enabled Molecular Characterization of Sezary Syndrome Reveals Distinct Pathway-Level Alterations Compared with Non-Sezary Cutaneous T-Cell Lymphoma](https://www.medrxiv.org/content/10.64898/2026.03.09.26347970v1)
  来源：medRxiv | 日期：2026-03-10 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：塞扎里综合征（SS）是皮肤T细胞淋巴瘤（CTCL）的一种侵袭性白血病变体。本研究利用面向精准肿瘤学的对话式人工智能（AI）平台，对哥伦比亚大学CTCL队列（SS组n=26，非SS组n=17）的体细胞突变和临床数据进行了二次分析。结果显示，SS与非SS CTCL的肿瘤突变负荷（TMB）无显著差异（p=0.83）。通路水平分析揭示了显著的定性差异：SS在表观遗传调节因子、肿瘤抑制和细胞周期控制基因、NFAT信号传导以及凋亡/免疫调节相关基因...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
