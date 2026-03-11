# 每日论文监控日报 (2026-03-11)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 46 篇新论文。

## 抓取状态

- arXiv：成功，命中 45 篇
- PubMed：成功，命中 25 篇
- bioRxiv：成功，命中 22 篇
- medRxiv：成功，命中 9 篇

## 最值得看

### Foundation Model / Agent

- [From General-Purpose to Disease-Specific Features: Aligning LLM Embeddings on a Disease-Specific Biomedical Knowledge Graph for Drug Repurposing](https://www.bioRxiv.org/content/10.1101/10.64898/2026.03.07.707871v1)
  来源：bioRxiv | 日期：2026-03-10 | 相关度：7.9 | 新颖度：7.0
  匹配主题：foundation_model_agent
  摘要：Identifying new therapeutic uses for existing drugs is a major challenge in biomedicine, especially for complex neurodegenerative conditions such as Alzheimer disease and related dementias (ADRD), where treatment options...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OPENXRD: A Comprehensive Benchmark Framework for LLM/MLLM XRD Question Answering](http://arxiv.org/abs/2507.09155v2)
  来源：arXiv | 日期：2025-07-12 | 相关度：7.5 | 新颖度：6.25
  匹配主题：foundation_model_agent
  摘要：We introduce OPENXRD, a comprehensive benchmarking framework for evaluating large language models (LLMs) and multimodal LLMs (MLLMs) in crystallography question answering. The framework measures context assimilation, or ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [NeuroNarrator: A Generalist EEG-to-Text Foundation Model for Clinical Interpretation via Spectro-Spatial Grounding and Temporal State-Space Reasoning](https://www.bioRxiv.org/content/10.1101/10.64898/2026.03.07.707799v1)
  来源：bioRxiv | 日期：2026-03-10 | 相关度：7.15 | 新颖度：6.75
  匹配主题：foundation_model_agent
  摘要：Electroencephalography (EEG) provides a non-invasive window into neural dynamics at high temporal resolution and plays a pivotal role in clinical neuroscience research. Despite this potential, prevailing computational ap...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MITRA: An AI Assistant for Knowledge Retrieval in Physics Collaborations](http://arxiv.org/abs/2603.09800v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：6.55 | 新颖度：8.19
  匹配主题：foundation_model_agent
  摘要：Large-scale scientific collaborations, such as the Compact Muon Solenoid (CMS) at CERN, produce a vast and ever-growing corpus of internal documentation. Navigating this complex information landscape presents a significa...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [DEO: Training-Free Direct Embedding Optimization for Negation-Aware Retrieval](http://arxiv.org/abs/2603.09185v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：7.5 | 新颖度：5.96
  匹配主题：foundation_model_agent
  摘要：Recent advances in Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) have enabled diverse retrieval methods. However, existing retrieval methods often fail to accurately retrieve results for negation ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CMMR-VLN: Vision-and-Language Navigation via Continual Multimodal Memory Retrieval](http://arxiv.org/abs/2603.07997v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：6.8 | 新颖度：0.5
  匹配主题：foundation_model_agent
  摘要：Although large language models (LLMs) are introduced into vision-and-language navigation (VLN) to improve instruction comprehension and generalization, existing LLM- based VLN lacks the ability to selectively recall and ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HDLxGraph: Bridging Large Language Models and HDL Repositories via HDL Graph Databases](http://arxiv.org/abs/2505.15701v2)
  来源：arXiv | 日期：2025-05-21 | 相关度：6.55 | 新颖度：2.2
  匹配主题：foundation_model_agent
  摘要：Retrieval Augmented Generation (RAG) is an essential agent for Large Language Model (LLM) aided Description Language (HDL) tasks, addressing the challenges of limited training data and prohibitively long prompts. However...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LongAudio-RAG: Event-Grounded Question Answering over Multi-Hour Long Audio](http://arxiv.org/abs/2602.14612v3)
  来源：arXiv | 日期：2026-02-16 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  摘要：Long-duration audio is increasingly common in industrial and consumer settings, yet reviewing multi-hour recordings is impractical, motivating systems that answer natural-language queries with precise temporal grounding ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Fanar-Sadiq: A Multi-Agent Architecture for Grounded Islamic QA](http://arxiv.org/abs/2603.08501v2)
  来源：arXiv | 日期：2026-03-09 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  摘要：Large language models (LLMs) can answer religious knowledge queries fluently, yet they often hallucinate and misattribute sources, which is especially consequential in Islamic settings where users expect grounding in can...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Can Parents and Patients Understand Myopia Using Large Language Model-Based Chatbots?](https://www.medRxiv.org/content/10.1101/10.64898/2026.03.09.26347905v1)
  来源：medRxiv | 日期：2026-03-10 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  摘要：Purpose: This study aimed to compare the reliability of myopia-related information from AI chatbots using a set of commonly asked questions by parents and patients on myopia, which is an emerging disease of the 21st-cent...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Epistemic Closure: Autonomous Mechanism Completion for Physically Consistent Simulation](http://arxiv.org/abs/2603.09756v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：5.45 | 新颖度：7.4
  匹配主题：foundation_model_agent
  摘要：The integration of Large Language Models (LLMs) into scientific discovery is currently hindered by the Implicit Context problem, where governing equations extracted from literature contain invisible thermodynamic assumpt...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evaluation of LLMs in retrieving food and nutritional context for RAG systems](http://arxiv.org/abs/2603.09704v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：5.45 | 新颖度：7.29
  匹配主题：foundation_model_agent
  摘要：In this article, we evaluate four Large Language Models (LLMs) and their effectiveness at retrieving data within a specialized Retrieval-Augmented Generation (RAG) system, using a comprehensive food composition database....
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Towards Robust Retrieval-Augmented Generation Based on Knowledge Graph: A Comparative Analysis](http://arxiv.org/abs/2603.05698v2)
  来源：arXiv | 日期：2026-03-05 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  摘要：Retrieval-Augmented Generation (RAG) was introduced to enhance the capabilities of Large Language Models (LLMs) beyond their encoded prior knowledge. This is achieved by providing LLMs with an external source of knowledg...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [BRIDGE: Benchmark for multi-hop Reasoning In long multimodal Documents with Grounded Evidence](http://arxiv.org/abs/2603.07931v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：6.8 | 新颖度：1.5
  匹配主题：foundation_model_agent
  摘要：Multi-hop question answering (QA) is widely used to evaluate the reasoning capabilities of large language models, yet most benchmarks focus on final answer correctness and overlook intermediate reasoning, especially in l...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Improving Causal Gene Identification Using Large Language Models](https://www.bioRxiv.org/content/10.1101/10.64898/2026.03.08.710344v1)
  来源：bioRxiv | 日期：2026-03-10 | 相关度：5.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  摘要：Genome-Wide Association Studies (GWAS) have successfully identified numerous loci associated with complex traits and diseases, yet pinpointing causal genes remains a significant challenge. The reliance on simple proximit...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Developing SCL2205 : A Protein Sequence-based Spatial Modelling Dataset for the Protein Language Model Frontier](https://www.bioRxiv.org/content/10.1101/10.64898/2026.03.08.710388v1)
  来源：bioRxiv | 日期：2026-03-10 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  摘要：Deep learning (DL) has advanced computational genome annotation tasks such as protein sub-cellular localisation (SCL) prediction. Nonetheless, its potential remains underutilised, primarily because of the limited availab...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [AI Agents, Language, Deep Learning and the Next Revolution in Science](http://arxiv.org/abs/2603.07940v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：8.5 | 新颖度：0.75
  匹配主题：foundation_model_agent
  摘要：Modern science is reaching a critical inflection point. Instruments across disciplines, from particle physics and astronomy to genomics and climate modeling, now produce data of such scale, diversity, and interdependence...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MMGraphRAG: Bridging Vision and Language with Interpretable Multimodal Knowledge Graphs](http://arxiv.org/abs/2507.20804v2)
  来源：arXiv | 日期：2025-07-28 | 相关度：6.8 | 新颖度：6.0
  匹配主题：foundation_model_agent
  摘要：Large Language Models (LLMs) often suffer from hallucinations, which Retrieval-Augmented Generation (RAG) and GraphRAG mitigate by incorporating external knowledge and knowledge graphs (KGs). However, GraphRAG remains te...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [EmbC-Test: How to Speed Up Embedded Software Testing Using LLMs and RAG](http://arxiv.org/abs/2603.09497v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：6.15 | 新颖度：6.99
  匹配主题：foundation_model_agent
  摘要：Manual development of automatic tests for embedded C software is a strenuous and time-consuming task that does not scale well. With the accelerating pace of software release cycles, verification increasingly becomes the ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [The Virtuous Cycle: AI-Powered Vector Search and Vector Search-Augmented AI](http://arxiv.org/abs/2603.09347v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：6.15 | 新颖度：6.57
  匹配主题：foundation_model_agent
  摘要：Modern AI and vector search are rapidly converging, forming a promising research frontier in intelligent information systems. On one hand, advances in AI have substantially improved the semantic accuracy and efficiency o...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GREmLN: A Cellular Graph Structure Aware Transcriptomics Foundation Model](https://www.bioRxiv.org/content/10.1101/10.1101/2025.07.03.663009v3)
  来源：bioRxiv | 日期：2026-03-10 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  摘要：The ever-increasing availability of large-scale single-cell profiles presents an opportunity to develop foundation models to capture cell properties and behavior. However, standard language models such as transformers be...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Enhancing Retrieval-Augmented Generation with Entity Linking for Educational Platforms](http://arxiv.org/abs/2512.05967v2)
  来源：arXiv | 日期：2025-12-05 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  摘要：In the era of Large Language Models (LLMs), Retrieval-Augmented Generation (RAG) architectures are gaining significant attention for their ability to ground language generation in reliable knowledge sources. Despite thei...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [TaSR-RAG: Taxonomy-guided Structured Reasoning for Retrieval-Augmented Generation](http://arxiv.org/abs/2603.09341v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：4.75 | 新颖度：6.54
  匹配主题：foundation_model_agent
  摘要：Retrieval-Augmented Generation (RAG) helps large language models (LLMs) answer knowledge-intensive and time-sensitive questions by conditioning generation on external evidence. However, most RAG systems still retrieve un...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [Accelerating Exploratory Clinical Research: An LLM-Powered Framework for Cross-Study Data Harmonization and Natural Language Querying](https://www.medRxiv.org/content/10.1101/10.64898/2026.03.04.26345603v1)
  来源：medRxiv | 日期：2026-03-09 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  摘要：Clinical research depends on high quality data that is standardized, accessible and interoperable. Yet evolving data standards over time and variations in their implementation hinder the secondary use of clinical trial d...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HLER: Human-in-the-Loop Economic Research via Multi-Agent Pipelines for Empirical Discovery](http://arxiv.org/abs/2603.07444v1)
  来源：arXiv | 日期：2026-03-08 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  摘要：Large language models (LLMs) have enabled agent-based systems that aim to automate scientific research workflows. Most existing approaches focus on fully autonomous discovery, where AI systems generate research ideas, co...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery](http://arxiv.org/abs/2603.08127v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  摘要：The increasing adoption of Large Language Models (LLMs) has enabled AI scientists to perform complex end-to-end scientific discovery tasks requiring coordination of specialized roles, including idea generation and experi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond Relevance: On the Relationship Between Retrieval and RAG Information Coverage](http://arxiv.org/abs/2603.08819v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：3.45 | 新颖度：6.25
  匹配主题：foundation_model_agent
  摘要：Retrieval-augmented generation (RAG) systems combine document retrieval with a generative model to address complex information seeking tasks like report generation. While the relationship between retrieval quality and ge...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AutoAgent: Evolving Cognition and Elastic Memory Orchestration for Adaptive Agents](http://arxiv.org/abs/2603.09716v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：2.1 | 新颖度：8.06
  匹配主题：未命中具体主题
  摘要：Autonomous agent frameworks still struggle to reconcile long-term experiential learning with real-time, context-sensitive decision-making. In practice, this gap appears as static cognition, rigid workflow dependence, and...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [World2Mind: Cognition Toolkit for Allocentric Spatial Reasoning in Foundation Models](http://arxiv.org/abs/2603.09774v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：2.05 | 新颖度：7.69
  匹配主题：foundation_model_agent
  摘要：Achieving robust spatial reasoning remains a fundamental challenge for current Multimodal Foundation Models (MFMs). Existing methods either overfit statistical shortcuts via 3D grounding data or remain confined to 2D vis...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Quantifying the Accuracy and Cost Impact of Design Decisions in Budget-Constrained Agentic LLM Search](http://arxiv.org/abs/2603.08877v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：1.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  摘要：Agentic Retrieval-Augmented Generation (RAG) systems combine iterative search, planning prompts, and retrieval backends, but deployed settings impose explicit budgets on tool calls and completion tokens. We present a con...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Routing without Forgetting](http://arxiv.org/abs/2603.09576v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：0.7 | 新颖度：7.23
  匹配主题：未命中具体主题
  摘要：Continual learning in transformers is commonly addressed through parameter-efficient adaptation: prompts, adapters, or LoRA modules are specialized per task while the backbone remains frozen. Although effective in contro...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Explainable Innovation Engine: Dual-Tree Agent-RAG with Methods-as-Nodes and Verifiable Write-Back](http://arxiv.org/abs/2603.09192v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：0.7 | 新颖度：5.51
  匹配主题：未命中具体主题
  摘要：Retrieval-augmented generation (RAG) improves factual grounding, yet most systems rely on flat chunk retrieval and provide limited control over multi-step synthesis. We propose an Explainable Innovation Engine that upgra...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Learning Hierarchical Knowledge in Text-Rich Networks with Taxonomy-Informed Representation Learning](http://arxiv.org/abs/2603.08159v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  摘要：Hierarchical knowledge structures are ubiquitous across real-world domains and play a vital role in organizing information from coarse to fine semantic levels. While such structures have been widely used in taxonomy syst...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Retrieval-Augmented Anatomical Guidance for Text-to-CT Generation](http://arxiv.org/abs/2603.08305v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  摘要：Text-conditioned generative models for volumetric medical imaging provide semantic control but lack explicit anatomical guidance, often resulting in outputs that are spatially ambiguous or anatomically inconsistent. In c...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [RexDrug: Reliable Multi-Drug Combination Extraction through Reasoning-Enhanced LLMs](http://arxiv.org/abs/2603.08166v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  摘要：Automated Drug Combination Extraction (DCE) from large-scale biomedical literature is crucial for advancing precision medicine and pharmacological research. However, existing relation extraction methods primarily focus o...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Overview of the TREC 2025 Retrieval Augmented Generation (RAG) Track](http://arxiv.org/abs/2603.09891v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：1.4 | 新颖度：7.71
  匹配主题：未命中具体主题
  摘要：The second edition of the TREC Retrieval Augmented Generation (RAG) Track advances research on systems that integrate retrieval and generation to address complex, real-world information needs. Building on the foundation ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Reverse Distillation: Consistently Scaling Protein Language Model Representations](http://arxiv.org/abs/2603.07710v1)
  来源：arXiv | 日期：2026-03-08 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  摘要：Unlike the predictable scaling laws in natural language processing and computer vision, protein language models (PLMs) scale poorly: for many tasks, models within the same family plateau or even decrease in performance, ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SPD-RAG: Sub-Agent Per Document Retrieval-Augmented Generation](http://arxiv.org/abs/2603.08329v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  摘要：Answering complex, real-world queries often requires synthesizing facts scattered across vast document corpora. In these settings, standard retrieval-augmented generation (RAG) pipelines suffer from incomplete evidence c...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Amortized Phylodynamic Inference with Neural Bayes Estimators and Recursive Neural Networks](http://arxiv.org/abs/2603.08345v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：2.6 | 新颖度：0.25
  匹配主题：sequencing_bioinformatics
  摘要：Phylodynamics is used to estimate epidemic dynamics from phylogenetic trees or genomic sequences of pathogens, but the likelihood calculations needed can be challenging for complex models. We present a neural Bayes estim...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [LooComp: Leverage Leave-One-Out Strategy to Encoder-only Transformer for Efficient Query-aware Context Compression](http://arxiv.org/abs/2603.09222v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：2.1 | 新颖度：6.12
  匹配主题：未命中具体主题
  摘要：Efficient context compression is crucial for improving the accuracy and scalability of question answering. For the efficiency of Retrieval Augmented Generation, context should be delivered fast, compact, and precise to e...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Flow Matching Meets Biology and Life Science: A Survey](http://arxiv.org/abs/2507.17731v2)
  来源：arXiv | 日期：2025-07-23 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  摘要：Over the past decade, advances in generative modeling, such as generative adversarial networks, masked autoencoders, and diffusion models, have significantly transformed biological research and discovery, enabling breakt...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Human-AI Collaboration for Scaling Agile Regression Testing: An Agentic-AI Teammate from Manual to Automated Testing](http://arxiv.org/abs/2603.08190v1)
  来源：arXiv | 日期：2026-03-09 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  摘要：Agile organizations increasingly rely on automated regression testing to sustain rapid, high-quality software delivery. However, as systems grow and requirements evolve, a persistent bottleneck arises: test specification...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Understand Then Memory: A Cognitive Gist-Driven RAG Framework with Global Semantic Diffusion](http://arxiv.org/abs/2602.15895v2)
  来源：arXiv | 日期：2026-02-11 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  摘要：Retrieval-Augmented Generation (RAG) effectively mitigates hallucinations in LLMs by incorporating external knowledge. However, the inherent discrete representation of text in existing frameworks often results in a loss ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Multi-Agent Off-World Exploration for Sparse Evidence Discovery via Gaussian Belief Mapping and Dual-Domain Coverage](http://arxiv.org/abs/2603.07650v1)
  来源：arXiv | 日期：2026-03-08 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  摘要：Off-world multi-robot exploration is challenged by sparse targets, limited sensing, hazardous terrain, and restricted communication. Many scientifically valuable clues are visually ambiguous and often require close-range...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [InterMind: Doctor-Patient-Family Interactive Depression Assessment Empowered by Large Language Models](http://arxiv.org/abs/2409.14878v2)
  来源：arXiv | 日期：2024-09-23 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  摘要：Depression poses significant challenges to patients and healthcare organizations, necessitating efficient assessment methods. Existing paradigms typically focus on a patient-doctor way that overlooks multi-role interacti...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Conversational Artificial Intelligence-Enabled Molecular Characterization of Sezary Syndrome Reveals Distinct Pathway-Level Alterations Compared with Non-Sezary Cutaneous T-Cell Lymphoma](https://www.medRxiv.org/content/10.1101/10.64898/2026.03.09.26347970v1)
  来源：medRxiv | 日期：2026-03-10 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  摘要：ABSTRACT Background: Sezary syndrome (SS) represents an aggressive leukemic variant of cutaneous T-cell lymphoma (CTCL) with distinct clinical behavior compared with other CTCL subtypes. While prior studies have identifi...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
