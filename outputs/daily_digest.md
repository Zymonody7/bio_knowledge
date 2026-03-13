# 每日论文监控日报 (2026-03-13)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 66 篇新论文。

## 抓取状态

- arXiv：成功，命中 52 篇
- PubMed：成功，命中 48 篇
- bioRxiv：成功，命中 29 篇
- medRxiv：成功，命中 9 篇

## 最值得看

### Foundation Model / Agent

- [From General-Purpose to Disease-Specific Features: Aligning LLM Embeddings on a Disease-Specific Biomedical Knowledge Graph for Drug Repurposing](https://www.biorxiv.org/content/10.64898/2026.03.07.707871v1)
  来源：bioRxiv | 日期：2026-03-10 | 相关度：7.9 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：Identifying new therapeutic uses for existing drugs is a major challenge in biomedicine, especially for complex neurodegenerative conditions such as Alzheimer disease and related dementias (ADRD), where treatment options...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ELISA: An Interpretable Hybrid Generative AI Agent for Expression-Grounded Discovery in Single-Cell Genomics](http://arxiv.org/abs/2603.11872v1)
  来源：arXiv | 日期：2026-03-12 | 相关度：7.55 | 新颖度：9.03
  匹配主题：foundation_model_agent
  中文摘要：Translating single-cell RNA sequencing (scRNA-seq) data into mechanistic biological hypotheses remains a critical bottleneck, as agentic AI systems lack direct access to transcriptomic representations while expression fo...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Can Theoretical Physics Research Benefit from Language Agents?](http://arxiv.org/abs/2506.06214v2)
  来源：arXiv | 日期：2025-06-06 | 相关度：7.5 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) are rapidly advancing across diverse domains, yet their application in theoretical physics remains inadequate. While current models show competence in mathematical reasoning and code generati...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [NeuroNarrator: A Generalist EEG-to-Text Foundation Model for Clinical Interpretation via Spectro-Spatial Grounding and Temporal State-Space Reasoning](https://www.biorxiv.org/content/10.64898/2026.03.07.707799v1)
  来源：bioRxiv | 日期：2026-03-10 | 相关度：7.15 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Electroencephalography (EEG) provides a non-invasive window into neural dynamics at high temporal resolution and plays a pivotal role in clinical neuroscience research. Despite this potential, prevailing computational ap...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Phylogeny-informed transfer learning with protein language models for epitope prediction](https://www.biorxiv.org/content/10.1101/2025.04.17.649425v3)
  来源：bioRxiv | 日期：2026-03-10 | 相关度：8.65 | 新颖度：5.75
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Generalist linear B-cell epitope predictors are typically trained on large, heterogeneous datasets, which can lead to biased representations and degraded performance for under-represented or emerging pathogens. We presen...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [KEPo: Knowledge Evolution Poison on Graph-based Retrieval-Augmented Generation](http://arxiv.org/abs/2603.11501v1)
  来源：arXiv | 日期：2026-03-12 | 相关度：6.55 | 新颖度：6.51
  匹配主题：foundation_model_agent
  中文摘要：Graph-based Retrieval-Augmented Generation (GraphRAG) constructs the Knowledge Graph (KG) from external databases to enhance the timeliness and accuracy of Large Language Model (LLM) generations.However,this reliance on ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [COMPASS: The explainable agentic framework for Sovereignty, Sustainability, Compliance, and Ethics](http://arxiv.org/abs/2603.11277v1)
  来源：arXiv | 日期：2026-03-11 | 相关度：6.55 | 新颖度：6.2
  匹配主题：foundation_model_agent
  中文摘要：The rapid proliferation of large language model (LLM)-based agentic systems raises critical concerns regarding digital sovereignty, environmental sustainability, regulatory compliance, and ethical alignment. Whilst exist...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multi-Agent Collaboration for Automated Design Exploration on High Performance Computing Systems](http://arxiv.org/abs/2603.11515v1)
  来源：arXiv | 日期：2026-03-12 | 相关度：6.55 | 新颖度：6.07
  匹配主题：foundation_model_agent
  中文摘要：Today's scientific challenges, from climate modeling to Inertial Confinement Fusion design to novel material design, require exploring huge design spaces. In order to enable high-impact scientific discovery, we need to s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback](http://arxiv.org/abs/2603.08561v3)
  来源：arXiv | 日期：2026-03-09 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Standard reinforcement learning (RL) for large language model (LLM)-based agents typically optimizes extrinsic task-success rewards, prioritizing one-off task solving over continual adaptation. As a result, agents may co...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond Max Tokens: Stealthy Resource Amplification via Tool Calling Chains in LLM Agents](http://arxiv.org/abs/2601.10955v2)
  来源：arXiv | 日期：2026-01-16 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：The agent--tool interaction loop is a critical attack surface for modern Large Language Model (LLM) agents. Existing denial-of-service (DoS) attacks typically function at the user-prompt or retrieval-augmented generation...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MITRA: An AI Assistant for Knowledge Retrieval in Physics Collaborations](http://arxiv.org/abs/2603.09800v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：6.55 | 新颖度：1.2
  匹配主题：foundation_model_agent
  中文摘要：Large-scale scientific collaborations, such as the Compact Muon Solenoid (CMS) at CERN, produce a vast and ever-growing corpus of internal documentation. Navigating this complex information landscape presents a significa...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Automated extraction and optimization of protein purification protocols using multi-agent large language models](https://www.biorxiv.org/content/10.64898/2026.03.03.709341v1)
  来源：bioRxiv | 日期：2026-03-11 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in Large Language Models (LLMs) present new opportunities for automating critical bottlenecks in scientific workflows such as literature reviews or protocol design. One such bottleneck is the purification...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [QUARE: Multi-Agent Negotiation for Balancing Quality Attributes in Requirements Engineering](http://arxiv.org/abs/2603.11890v1)
  来源：arXiv | 日期：2026-03-12 | 相关度：6.15 | 新颖度：7.83
  匹配主题：foundation_model_agent
  中文摘要：Requirements engineering (RE) is critical to software success, yet automating it remains challenging because multiple, often conflicting quality attributes must be balanced while preserving stakeholder intent. Existing L...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [GUIDES: Guidance Using Instructor-Distilled Embeddings for Pre-trained Robot Policy Enhancement](http://arxiv.org/abs/2511.03400v3)
  来源：arXiv | 日期：2025-11-05 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Pre-trained robot policies serve as the foundation of many validated robotic systems, which encapsulate extensive embodied knowledge. However, they often lack the semantic awareness characteristic of foundation models, a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evaluating transformer-based models for structural characterization of orphan proteins](https://www.biorxiv.org/content/10.64898/2026.03.10.709490v1)
  来源：bioRxiv | 日期：2026-03-12 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Transformer-based models (TBMs) are state-of-the-art deep learning architectures that predict protein structural and functional features with high accuracy. Despite methodological differences, they all rely on large prot...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DocSage: An Information Structuring Agent for Multi-Doc Multi-Entity Question Answering](http://arxiv.org/abs/2603.11798v1)
  来源：arXiv | 日期：2026-03-12 | 相关度：5.45 | 新颖度：7.24
  匹配主题：foundation_model_agent
  中文摘要：Multi-document Multi-entity Question Answering inherently demands models to track implicit logic between multiple entities across scattered documents. However, existing Large Language Models (LLMs) and Retrieval-Augmente...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Automating Skill Acquisition through Large-Scale Mining of Open-Source Agentic Repositories: A Framework for Multi-Agent Procedural Knowledge Extraction](http://arxiv.org/abs/2603.11808v1)
  来源：arXiv | 日期：2026-03-12 | 相关度：5.45 | 新颖度：6.76
  匹配主题：foundation_model_agent
  中文摘要：The transition from monolithic large language models (LLMs) to modular, skill-equipped agents represents a fundamental architectural shift in artificial intelligence deployment. While general-purpose models demonstrate r...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TURA: Tool-Augmented Unified Retrieval Agent for AI Search](http://arxiv.org/abs/2508.04604v2)
  来源：arXiv | 日期：2025-08-06 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：The advent of Large Language Models (LLMs) is transforming search engines into conversational AI search products, primarily using Retrieval-Augmented Generation (RAG) on web corpora. However, this paradigm has significan...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Truncated Step-Level Sampling with Process Rewards for Retrieval-Augmented Reasoning](http://arxiv.org/abs/2602.23440v2)
  来源：arXiv | 日期：2026-02-26 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Training large language models to reason with search engines via reinforcement learning is hindered by a fundamental credit assignment problem: existing methods such as Search-R1 provide only a sparse outcome reward afte...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [User-driven development and evaluation of an agentic framework for analysis of large pathway diagrams](https://www.biorxiv.org/content/10.64898/2026.03.10.710813v1)
  来源：bioRxiv | 日期：2026-03-12 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：As biomedical knowledge keeps growing, resources storing available information multiply and grow in size and complexity. Such resources can be in the format of molecular interaction maps, which represent cellular and mol...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CARROT: A Learned Cost-Constrained Retrieval Optimization System for RAG](http://arxiv.org/abs/2411.00744v2)
  来源：arXiv | 日期：2024-11-01 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have demonstrated impressive ability in generation and reasoning tasks but struggle with handling up-to-date knowledge, leading to inaccuracies or hallucinations. Retrieval-Augmented Generati...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Entity-Centric to Goal-Oriented Graphs: Enhancing LLM Knowledge Retrieval in Minecraft](http://arxiv.org/abs/2505.18607v2)
  来源：arXiv | 日期：2025-05-24 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) demonstrate impressive general capabilities but often struggle with step-by-step procedural reasoning, a critical challenge in complex interactive environments. While retrieval-augmented meth...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Improving Causal Gene Identification Using Large Language Models](https://www.biorxiv.org/content/10.64898/2026.03.08.710344v1)
  来源：bioRxiv | 日期：2026-03-10 | 相关度：5.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Genome-Wide Association Studies (GWAS) have successfully identified numerous loci associated with complex traits and diseases, yet pinpointing causal genes remains a significant challenge. The reliance on simple proximit...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Developing SCL2205 : A Protein Sequence-based Spatial Modelling Dataset for the Protein Language Model Frontier](https://www.biorxiv.org/content/10.64898/2026.03.08.710388v1)
  来源：bioRxiv | 日期：2026-03-10 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Deep learning (DL) has advanced computational genome annotation tasks such as protein sub-cellular localisation (SCL) prediction. Nonetheless, its potential remains underutilised, primarily because of the limited availab...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [HitAnno: Atlas-level cell type annotation based on scATAC-seq data via a hierarchical language model](https://www.biorxiv.org/content/10.64898/2026.03.10.710729v1)
  来源：bioRxiv | 日期：2026-03-12 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：The single-cell assay for transposase-accessible chromatin using sequencing (scATAC-seq) has emerged as a core technology for dissecting cellular epigenomic heterogeneity and gene regulatory programs. With the emergence ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Legal-DC: Benchmarking Retrieval-Augmented Generation for Legal Documents](http://arxiv.org/abs/2603.11772v1)
  来源：arXiv | 日期：2026-03-12 | 相关度：4.75 | 新颖度：7.39
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) has emerged as a promising technology for legal document consultation, yet its application in Chinese legal scenarios faces two key limitations: existing benchmarks lack specialized s...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [SINDI: an Efficient Index for Approximate Maximum Inner Product Search on Sparse Vectors](http://arxiv.org/abs/2509.08395v3)
  来源：arXiv | 日期：2025-09-10 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Sparse vector Maximum Inner Product Search (MIPS) is crucial in multi-path retrieval for Retrieval-Augmented Generation (RAG). Recent inverted index-based and graph-based algorithms have achieved high search accuracy wit...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Ultra-Fast Language Generation via Discrete Diffusion Divergence Instruct](http://arxiv.org/abs/2509.25035v3)
  来源：arXiv | 日期：2025-09-29 | 相关度：7.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Fast and high-quality language generation is the holy grail that people pursue in the age of AI. In this work, we introduce Discrete Diffusion Divergence Instruct (DiDi-Instruct), a training-based method that initializes...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Omics Data Discovery Agents](http://arxiv.org/abs/2603.10161v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：The biomedical literature contains a vast collection of omics studies, yet most published data remain functionally inaccessible for computational reuse. When raw data are deposited in public repositories, essential infor...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Toward Closed-loop Molecular Discovery via Language Model, Property Alignment and Strategic Search](http://arxiv.org/abs/2512.09566v3)
  来源：arXiv | 日期：2025-12-10 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Drug discovery is a time-consuming and expensive process, with traditional high-throughput and docking-based virtual screening hampered by low success rates and limited scalability. Recent advances in generative modellin...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Cyclic peptides space: The methodology of sequence selection to cover the comprehensive physical properties](https://www.biorxiv.org/content/10.64898/2026.03.10.710724v1)
  来源：bioRxiv | 日期：2026-03-12 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Cyclic peptides have emerged as a pivotal modality for next-generation therapeutics, due to their superior biocompatibility, high selectivity, and structural stability. While AI-driven peptide design has advanced rapidly...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GREmLN: A Cellular Graph Structure Aware Transcriptomics Foundation Model](https://www.biorxiv.org/content/10.1101/2025.07.03.663009v3)
  来源：bioRxiv | 日期：2026-03-10 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：AO_SCPLOWBSTRACTC_SCPLOWThe ever-increasing availability of large-scale single-cell profiles presents an opportunity to develop foundation models to capture cell properties and behavior. However, standard language models...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [QChunker: Learning Question-Aware Text Chunking for Domain RAG via Multi-Agent Debate](http://arxiv.org/abs/2603.11650v1)
  来源：arXiv | 日期：2026-03-12 | 相关度：5.45 | 新颖度：6.79
  匹配主题：foundation_model_agent
  中文摘要：The effectiveness upper bound of retrieval-augmented generation (RAG) is fundamentally constrained by the semantic integrity and information granularity of text chunks in its knowledge base. To address these challenges, ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Rapid and Interpretable AMR Diagnostics via Genomics and Cell Painting using Differential Geometry-based Directed-Simplicial Neural Networks on Multimodal Data](https://www.biorxiv.org/content/10.64898/2026.03.11.711128v1)
  来源：bioRxiv | 日期：2026-03-12 | 相关度：4.75 | 新颖度：6.0
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：Antimicrobial resistance (AMR) remains a critical global health challenge, particularly in high prevalence regions such as India, where rapid and interpretable diagnostic tools are urgently needed. To address this challe...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Advances in Pathogen Detection by Nanosensors: Biorecognition Strategies, Signal Amplification, and Platform Engineering.](https://pubmed.ncbi.nlm.nih.gov/41808396/)
  来源：PubMed | 日期：2026-03-10 | 相关度：7.75 | 新颖度：0.5
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：The escalating global threat of infectious diseases, compounded by antimicrobial resistance (AMR), calls for improved diagnostic strategies. Conventional pathogen detection techniques─culture, enzyme-linked immunosorbent...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Multi-Criteria Validation of LLM-Inferred Depression Severity from Outpatient Psychiatry Notes](https://www.medrxiv.org/content/10.64898/2026.03.11.26348066v1)
  来源：medRxiv | 日期：2026-03-12 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Background: Longitudinal measurement of depression severity in outpatient psychiatric care is limited by infrequent standardized assessments. Although psychiatric clinical notes capture illness burden and functional impa...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Can Small Language Models Use What They Retrieve? An Empirical Study of Retrieval Utilization Across Model Scale](http://arxiv.org/abs/2603.11513v1)
  来源：arXiv | 日期：2026-03-12 | 相关度：5.45 | 新颖度：5.57
  匹配主题：foundation_model_agent
  中文摘要：Retrieval augmented generation RAG is widely deployed to improve factual accuracy in language models yet it remains unclear whether smaller models of size 7B parameters or less can effectively utilize retrieved informati...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Can Parents and Patients Understand Myopia Using Large Language Model-Based Chatbots?](https://www.medrxiv.org/content/10.64898/2026.03.09.26347905v1)
  来源：medRxiv | 日期：2026-03-10 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Purpose: This study aimed to compare the reliability of myopia-related information from AI chatbots using a set of commonly asked questions by parents and patients on myopia, which is an emerging disease of the 21st-cent...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Regression vs. Medical LLMs: A Comprehensive Study for CVD and Mortality Risk Prediction](https://www.medrxiv.org/content/10.64898/2026.03.11.26347789v1)
  来源：medRxiv | 日期：2026-03-11 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Cardiovascular diseases (CVDs) remain the foremost cause of global morbidity and mortality, driving an urgent need for robust predictive tools that enable early detection and preventive intervention. Traditional regressi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evaluation of LLMs in retrieving food and nutritional context for RAG systems](http://arxiv.org/abs/2603.09704v2)
  来源：arXiv | 日期：2026-03-10 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：In this article, we evaluate four Large Language Models (LLMs) and their effectiveness at retrieving data within a specialized Retrieval-Augmented Generation (RAG) system, using a comprehensive food composition database....
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Epistemic Closure: Autonomous Mechanism Completion for Physically Consistent Simulation](http://arxiv.org/abs/2603.09756v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：The integration of Large Language Models (LLMs) into scientific discovery is currently hindered by the Implicit Context problem, where governing equations extracted from literature contain invisible thermodynamic assumpt...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ThunderAgent: A Simple, Fast and Program-Aware Agentic Inference System](http://arxiv.org/abs/2602.13692v2)
  来源：arXiv | 日期：2026-02-14 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models(LLMs) are now used to power complex multi-turn agentic workflows. Existing systems run agentic inference by loosely assembling isolated components: an LLM inference engine (e.g., vLLM) and a tool or...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond Relevance: On the Relationship Between Retrieval and RAG Information Coverage](http://arxiv.org/abs/2603.08819v2)
  来源：arXiv | 日期：2026-03-09 | 相关度：3.45 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) systems combine document retrieval with a generative model to address complex information seeking tasks like report generation. While the relationship between retrieval quality and ge...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ARK: Answer-Centric Retriever Tuning via KG-augmented Curriculum Learning](http://arxiv.org/abs/2511.16326v2)
  来源：arXiv | 日期：2025-11-20 | 相关度：2.1 | 新颖度：6.75
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) has emerged as a powerful framework for knowledge-intensive tasks, yet its effectiveness in long-context scenarios is often bottlenecked by the retriever's inability to distinguish sp...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [World2Mind: Cognition Toolkit for Allocentric Spatial Reasoning in Foundation Models](http://arxiv.org/abs/2603.09774v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：2.05 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：稳健的空间推理是当前多模态基础模型（MFMs）面临的核心挑战。现有方法常因过度拟合3D定位数据的统计捷径或局限于2D视觉感知，导致在未知场景中的推理准确性与泛化能力受限。受生物智能空间认知映射机制启发，我们提出了World2Mind，一个无需训练的空间智能工具包。该工具包利用3D重建和实例分割模型构建结构化的空间认知地图，使MFMs能够主动获取感兴趣地标与路径的目标空间知识。为提供稳健的几何拓扑先验，World2Mind合成了异向空间树...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Benchmarking zero-shot single-cell foundation model embeddings for cellular dynamics reconstruction](https://www.biorxiv.org/content/10.64898/2026.03.10.710748v1)
  来源：bioRxiv | 日期：2026-03-12 | 相关度：1.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Reconstructing cellular trajectories from time-resolved single-cell transcriptomics is fundamental to understanding processes from embryonic development to cancer progression. While single-cell foundation models (scFMs) ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Cross-Species Antimicrobial Resistance Prediction from Genomic Foundation Models](http://arxiv.org/abs/2603.11141v1)
  来源：arXiv | 日期：2026-03-11 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Cross-species antimicrobial resistance (AMR) prediction is fundamentally an out-of-distribution (OOD) generalization problem: models trained on one set of bacterial taxa must transfer to phylogenetically distinct genomes...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Statistical and structural identifiability in representation learning](http://arxiv.org/abs/2603.11970v1)
  来源：arXiv | 日期：2026-03-12 | 相关度：1.4 | 新颖度：8.29
  匹配主题：未命中具体主题
  中文摘要：Representation learning models exhibit a surprising stability in their internal representations. Whereas most prior work treats this stability as a single property, we formalize it as two distinct concepts: statistical i...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Exhaustive Circuit Mapping of a Single-Cell Foundation Model Reveals Massive Redundancy, Heavy-Tailed Hub Architecture, and Layer-Dependent Differentiation Control](http://arxiv.org/abs/2603.11940v1)
  来源：arXiv | 日期：2026-03-12 | 相关度：1.4 | 新颖度：7.72
  匹配主题：未命中具体主题
  中文摘要：本研究针对生物基础模型机械可解释性中存在的选择性特征采样偏差，对基于 Transformer 的单细胞基础模型 Geneformer 进行了详尽的电路映射。研究通过三个实验展开：首先，对第 5 层的 4065 个稀疏自编码器（SAE）特征进行详尽追踪，识别出 1,393,850 条显著下游边，较传统选择性采样扩大了 27 倍，揭示了长尾枢纽架构，其中 1.8% 的特征贡献了极高连接性，且 40% 的顶级枢纽缺乏生物学注释。其次，通过对 ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AILS-NTUA at SemEval-2026 Task 8: Evaluating Multi-Turn RAG Conversations](http://arxiv.org/abs/2603.10524v1)
  来源：arXiv | 日期：2026-03-11 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：本文介绍了 AILS-NTUA 系统在 SemEval-2026 任务 8（MTRAGEval）中的实现，该任务聚焦于多轮检索增强生成（RAG）的三个子任务：段落检索（A）、基于参考的响应生成（B）及端到端 RAG（C）。该系统基于两大核心原则构建：其一，采用“查询多样性优于检索器多样性”策略，利用 5 种互补的 LLM 查询重构技术配合单一语料库对齐的稀疏检索器，并通过方差感知嵌套倒数排名融合（RRF）进行整合；其二，构建多阶段生成流...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Context Before Code: An Experience Report on Vibe Coding in Practice](http://arxiv.org/abs/2603.11073v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：随着代码生成工具在软件开发中的普及，关于生产环境下对话式“氛围编程”（vibe coding）的实践报告仍较少。本文介绍了一个小型全栈团队的经验，通过应用上下文提示和显式架构约束，构建了两个系统：(i) 一个面向持续生产使用的多项目智能体（Agent）学习平台，支持具有结构化记忆和后台处理的隔离项目；(ii) 一个学术检索增强生成（RAG）系统，提供带引用的回答、基于角色的访问控制（RBAC）和评估跟踪。结果显示，氛围编程显著加速了系统...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [End-to-End Chatbot Evaluation with Adaptive Reasoning and Uncertainty Filtering](http://arxiv.org/abs/2603.10570v1)
  来源：arXiv | 日期：2026-03-11 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) combined with retrieval augmented generation have enabled the deployment of domain-specific chatbots, but these systems remain prone to generating unsupported or incorrect answers. Reliable e...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Overview of the TREC 2025 Retrieval Augmented Generation (RAG) Track](http://arxiv.org/abs/2603.09891v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：第二届 TREC 检索增强生成（RAG）赛道旨在推进整合检索与生成系统的研究，以解决复杂的现实信息需求。在 2024 年首届赛道的基础上，本届挑战赛引入了长篇、多句的叙述性查询，以反映深度搜索任务中日益增长的推理驱动响应需求。参赛者需设计结合检索与生成的流水线，并确保透明度和事实依据。该赛道利用 MS MARCO V2.1 语料库，采用包含相关性评估、回答完整性、归因验证和一致性分析的多层评估框架。通过强调多维叙述和归因丰富的答案（本年...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [A paired sequence language model for protein-protein interaction modeling.](https://pubmed.ncbi.nlm.nih.gov/41807423/)
  来源：PubMed | 日期：2026-03-10 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Understanding protein-protein interactions (PPIs) is crucial for deciphering cellular processes and guiding therapeutic discovery. While recent protein language models have advanced sequence-based protein representation,...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [How to make the most of your masked language model for protein engineering](http://arxiv.org/abs/2603.10302v1)
  来源：arXiv | 日期：2026-03-11 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：A plethora of protein language models have been released in recent years. Yet comparatively little work has addressed how to best sample from them to optimize desired biological properties. We fill this gap by proposing ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Reason and Verify: A Framework for Faithful Retrieval-Augmented Generation](http://arxiv.org/abs/2603.10143v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) significantly improves the factuality of Large Language Models (LLMs), yet standard pipelines often lack mechanisms to verify inter- mediate reasoning, leaving them vulnerable to hall...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MESSI: Multimodal Experiments with SyStematic Interrogation using nextflow](https://www.biorxiv.org/content/10.64898/2026.03.09.710452v1)
  来源：bioRxiv | 日期：2026-03-11 | 相关度：3.05 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Background: Multimodal biomedical studies increasingly profile multiple molecular and clinical modalities from the same samples, creating new opportunities for disease prediction and biological discovery. However, benchm...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Discovery of a Hematopoietic Manifold in scGPT Yields a Method for Extracting Performant Algorithms from Biological Foundation Model Internals](http://arxiv.org/abs/2603.10261v1)
  来源：arXiv | 日期：2026-03-10 | 相关度：1.7 | 新颖度：1.75
  匹配主题：未命中具体主题
  中文摘要：本研究从单细胞基础模型 scGPT 中发现并提取了一种紧凑的造血算法，这是已知首个通过机械可解释性（Mechanistic Interpretability）从生物基础模型中提取出的具有实用竞争力的算法。研究证明 scGPT 内部编码了具有显著发育分支结构的造血流形，并在 Tabula Sapiens 外部面板及独立多供体免疫面板上完成了零样本迁移验证。为隔离该几何结构，研究者提出了一种通用的三阶段提取法：从冻结注意力权重中直接导出算子...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MDER-DR: Multi-Hop Question Answering with Entity-Centric Summaries](http://arxiv.org/abs/2603.11223v1)
  来源：arXiv | 日期：2026-03-11 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：针对知识图谱（KG）的检索增强生成（RAG）在将文本简化为三元组时，往往会丢失重要的上下文细微差别，导致多跳问答（QA）性能下降。为此，我们提出了一种领域无关的 KG 问答框架 MDER-DR，涵盖索引与检索推理阶段。在索引阶段，MDER（映射-消歧-丰富-归约）方法生成源自上下文的三元组描述，并将其与实体级摘要整合，从而在检索阶段无需显式遍历图边缘。在检索阶段，DR（分解-解决）机制将用户查询分解为可解析的三元组，并通过迭代推理将其定...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RAGPerf: An End-to-End Benchmarking Framework for Retrieval-Augmented Generation Systems](http://arxiv.org/abs/2603.10765v1)
  来源：arXiv | 日期：2026-03-11 | 相关度：1.4 | 新颖度：1.5
  匹配主题：未命中具体主题
  中文摘要：本文设计并实现了 RAGPerf，这是一个用于表征检索增强生成（RAG）流水线系统行为的端到端基准测试框架。为了实现详细的剖析和细粒度的性能分析，RAGPerf 将 RAG 工作流解耦为嵌入、索引、检索、重排序和生成五个模块化组件。该框架允许用户配置各组件的核心参数，并评估其对端到端查询性能和质量的影响。RAGPerf 内置工作负载生成器，通过支持文本、PDF、代码和音频等多样化数据集、不同的检索与更新比例以及查询分布来模拟真实场景。它...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Structured Linked Data as a Memory Layer for Agent-Orchestrated Retrieval](http://arxiv.org/abs/2603.10700v1)
  来源：arXiv | 日期：2026-03-11 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）系统通常将文档视为扁平文本，忽略了知识图谱提供的结构化元数据和链接关系。本研究探讨了结构化链接数据（特别是 Schema.org 标记和由链接数据平台提供的可解引用实体页面）能否提升标准及智能体 RAG 系统的检索准确性和回答质量。研究在编辑、法律、旅游和电子商务四个领域开展了对照实验，采用 Vertex AI Vector Search 2.0 进行检索，并利用 Google Agent Development ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Learning Adaptive Force Control for Contact-Rich Sample Scraping with Heterogeneous Materials](http://arxiv.org/abs/2603.10979v1)
  来源：arXiv | 日期：2026-03-11 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：针对全球挑战对加速科学发现的需求，本研究提出了一种自适应力控框架，旨在解决机器人化学家在实验室环境中处理多样化化学物质（如颗粒、粉末或粘性液体）时的操作难题。研究重点在于自动化执行从试剂瓶壁刮取样本这一精细任务。该框架结合了用于稳定物理交互的底层笛卡尔阻抗控制器，以及根据感知反馈动态调整末端执行器交互力的上层强化学习（RL）智能体。研究者利用 Franka Research 3 机器人构建了仿真环境，并将异质材料建模为具有不同剥离力阈值...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Biosensing technologies for foodborne pathogen detection and healthcare: principles, emerging materials, and intelligent platforms.](https://pubmed.ncbi.nlm.nih.gov/41803510/)
  来源：PubMed | 日期：2026-03-10 | 相关度：3.45 | 新颖度：0.25
  匹配主题：pathogenomics, application_monitoring
  中文摘要：Foodborne pathogens such as Escherichia coli (E. Coli), Salmonella , and Listeria monocytogenes continue to pose a major potential threat to global public health and therefore rapid, accurate, and field-deployable detect...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Conversational Artificial Intelligence-Enabled Molecular Characterization of Sezary Syndrome Reveals Distinct Pathway-Level Alterations Compared with Non-Sezary Cutaneous T-Cell Lymphoma](https://www.medrxiv.org/content/10.64898/2026.03.09.26347970v1)
  来源：medRxiv | 日期：2026-03-10 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：塞扎里综合征（SS）是皮肤T细胞淋巴瘤（CTCL）的一种侵袭性白血病变体。本研究利用对话式人工智能（AI）精准肿瘤学平台，对哥伦比亚大学CTCL队列（SS组n=26，非SS组n=17）的体细胞突变和临床数据进行了二次分析。研究重点分析了高影响编码变异，并将其注释至关键信号通路。结果显示，SS与非SS CTCL的肿瘤突变负荷（TMB）无显著差异（p=0.83）。通路层面分析揭示，SS在表观遗传调节因子、抑癌基因、细胞周期控制、NFAT信号...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Fingerprinting Fluorescent In Situ Hybridization Enables Multiplexed Identification of Pathogenic Bacteria.](https://pubmed.ncbi.nlm.nih.gov/41810482/)
  来源：PubMed | 日期：2026-03-11 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：荧光原位杂交（FISH）是一种无需培养即可检测病原菌的高特异性技术，能同时提供病原菌丰度、形态和空间定位信息。然而，传统 FISH 灵敏度低且多重检测能力有限，限制了其广泛应用。本研究提出了一种由 DNA 自组装驱动的指纹荧光原位杂交（FinFISH）策略，用于多重病原菌检测。以呼吸道病原体为模型，FinFISH 利用 FAM、Cy3 和 Cy5 三种荧光团进行组合标记，为每种病原体生成独特的荧光指纹。该策略突破了荧光通道数量对检测通量...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Adversarial Hubness Detector: Detecting Hubness Poisoning in Retrieval-Augmented Generation Systems](http://arxiv.org/abs/2602.22427v2)
  来源：arXiv | 日期：2026-02-25 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) systems are essential to contemporary AI applications, allowing large language models to obtain external knowledge via vector similarity search. Nevertheless, these systems encounter ...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。
