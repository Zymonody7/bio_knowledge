# 每日论文监控日报 (2026-05-09)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 55 篇新论文。

## 抓取状态

- arXiv：成功，命中 46 篇
- PubMed：成功，命中 38 篇
- bioRxiv：成功，命中 20 篇
- medRxiv：成功，命中 7 篇

## 最值得看

### Foundation Model / Agent

- [Multi-Modal LLM based Image Captioning in ICT: Bridging the Gap Between General and Industry Domain](http://arxiv.org/abs/2601.09298v2)
  来源：arXiv | 日期：2026-01-14 | 相关度：7.9 | 新颖度：6.2
  匹配主题：foundation_model_agent
  中文摘要：In the information and communications technology (ICT) industry, training a domain-specific large language model (LLM) or constructing a retrieval-augmented generation system requires a substantial amount of high-value d...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [JARVIS: An Evidence-Grounded Retrieval System for Interpretable Deceptive Reviews Adjudication](http://arxiv.org/abs/2602.12941v2)
  来源：arXiv | 日期：2026-02-13 | 相关度：7.5 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Deceptive reviews, refer to fabricated feedback designed to artificially manipulate the perceived quality of products. Within modern e-commerce ecosystems, these reviews remain a critical governance challenge. Despite ad...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The Cost of Context: Mitigating Textual Bias in Multimodal Retrieval-Augmented Generation](http://arxiv.org/abs/2605.05594v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：7.5 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：While Multimodal Large Language Models (MLLMs) are increasingly integrated with Retrieval-Augmented Generation (RAG) to mitigate hallucinations, the introduction of external documents can conceal severe failure modes at ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Evaluating Reference-Independent Pipelines for the Detection of Spreading Organisms in Metagenomic Datasets](https://www.biorxiv.org/content/10.64898/2026.05.03.722517v1)
  来源：bioRxiv | 日期：2026-05-06 | 相关度：9.15 | 新颖度：6.25
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：The emergence of unidentified pathogens, or "Disease X," poses a significant threat to global health, necessitating the development of proactive surveillance strategies for the wildlife and human virosphere. Since novel ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [LatentRAG: Latent Reasoning and Retrieval for Efficient Agentic RAG](http://arxiv.org/abs/2605.06285v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：6.55 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：Single-step retrieval-augmented generation (RAG) provides an efficient way to incorporate external information for simple question answering tasks but struggles with complex questions. Agentic RAG extends this paradigm b...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BioTool: A Comprehensive Tool-Calling Dataset for Enhancing Biomedical Capabilities of Large Language Models](http://arxiv.org/abs/2605.05758v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Despite the success of large language models (LLMs) on general-purpose tasks, their performance in highly specialized domains such as biomedicine remains unsatisfactory. A key limitation is the inability of LLMs to effec...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SLiMNet: a deep learning model to detect short linear motifs using protein large language model representations and paired inputs](https://www.biorxiv.org/content/10.64898/2026.05.04.722713v1)
  来源：bioRxiv | 日期：2026-05-07 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Short linear motifs (SLiMs) are short (3-15 amino acids in length) segments within intrinsically disordered regions (IDRs) that mediate transient protein-protein interactions as well as other functions such as stability ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Knowledge Graphs, the Missing Link in Agentic AI-based Formal Verification](http://arxiv.org/abs/2605.06434v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in Large Language Models (LLMs) have enabled workflows that generate SystemVerilog Assertions (SVAs) from natural-language specifications, with the potential to accelerate Formal Verification (FV). Howeve...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Architecture Matters: Comparing RAG Systems under Knowledge Base Poisoning](http://arxiv.org/abs/2605.05632v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) systems are vulnerable to knowledge base poisoning, yet existing attacks have been evaluated almost exclusively against vanilla retrieve-then-generate pipelines. Architectures designe...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Prompt-engineering improves clinical safety of large language models for opioid equipotency conversion](https://www.medrxiv.org/content/10.64898/2026.05.06.26352590v1)
  来源：medRxiv | 日期：2026-05-08 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Background: Large language models (LLMs) are increasingly used in medical education and clinical decision-making, but their reliability in high-risk medication dosing remains unclear. Opioid rotation is a common task req...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MAT-Cell: A Multi-Agent Tree-Structured Reasoning Framework for Batch-Level Single-Cell Annotation](http://arxiv.org/abs/2604.06269v2)
  来源：arXiv | 日期：2026-04-07 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Automated single-cell annotation is difficult when the most abundant genes are not the most discriminative ones, or when a target state is poorly covered by a fixed reference atlas. GPTCelltype-style one-shot prompting a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Bridging LLM Reasoning and Chemical Knowledge via an Evolutionary Multi-Agent Framework for Molecular Synthesis](https://www.biorxiv.org/content/10.64898/2026.05.02.722342v1)
  来源：bioRxiv | 日期：2026-05-06 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Molecular design faces the dual challenge of navigating a vast chemical space while ensuring experimental synthesizability. Traditional models are constrained by small datasets, restricting their scalability and broader ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Cited but Not Verified: Parsing and Evaluating Source Attribution in LLM Deep Research Agents](http://arxiv.org/abs/2605.06635v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) power deep research agents that synthesize information from hundreds of web sources into cited reports, yet these citations cannot be reliably verified. Current approaches either trust models...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LLM-Driven Design Space Exploration of FPGA-based Accelerators](http://arxiv.org/abs/2605.05920v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Designing field-programmable gate array (FPGA)-based accelerators for modern artificial intelligence workloads requires navigating a large and complex hardware design space encompassing architectural parameters, dataflow...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AI CFD Scientist: Toward Open-Ended Computational Fluid Dynamics Discovery with Physics-Aware AI Agents](http://arxiv.org/abs/2605.06607v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Recent LLM-based agents have closed substantial portions of the scientific discovery loop in software-only machine-learning research, in chemistry, and in biology. Extending the same loop to high-fidelity physical simula...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CAPTAIN: a multimodal foundation model pretrained on co-assayed single-cell RNA and protein.](https://pubmed.ncbi.nlm.nih.gov/42098152/)
  来源：PubMed | 日期：2026-05-07 | 相关度：4.45 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Proteins act as the terminal effectors of cellular function, encoding the phenotypic consequences of genomic and transcriptomic programmes. Although transcriptomic profiles serve as accessible proxies, they remain incomp...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Agentic Discovery of Exchange-Correlation Density Functionals](http://arxiv.org/abs/2605.05460v1)
  来源：arXiv | 日期：2026-05-06 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：The development of accurate exchange-correlation (XC) functionals remains a longstanding challenge in density functional theory (DFT). The vast majority of XC functionals have been hand designed by human researchers comb...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [LCC-LLM: Leveraging Code-Centric Large Language Models for Malware Attribution](http://arxiv.org/abs/2605.05807v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：LLMs are increasingly explored for malware analysis; however, current LLM-based malware attribution remains limited by unsupported indicators and insufficient code-level grounding for identifying malicious and vulnerable...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [LeakDojo: Decoding the Leakage Threats of RAG Systems](http://arxiv.org/abs/2605.05818v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) enables large language models (LLMs) to leverage external knowledge, but also exposes valuable RAG databases to leakage attacks. As RAG systems grow more complex and LLMs exhibit stro...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Privacy Without Losing Place: A Paradigm for Private Retrieval in Spatial RAGs](http://arxiv.org/abs/2605.05459v1)
  来源：arXiv | 日期：2026-05-06 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：This work introduces PAS -- Privacy Anchor Substitution, a structured mechanism for enabling user location privacy in spatial retrieval-augmented generation (RAG) systems. Unlike conventional differential privacy methods...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [An LLM-driven pipeline for proteomics-based detection and structural modeling of post-translational modifications](https://www.biorxiv.org/content/10.64898/2026.05.01.722279v1)
  来源：bioRxiv | 日期：2026-05-06 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Post-translational modifications (PTMs) on proteins dynamically regulate their functions and subsequently cellular physiology. Significant advances have been made in their detection and modeling: mass spectrometry-based ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [UPhAIR: A Hybrid Pipeline for Generating Understandable Post-hoc AI Reports in Glioma IDH Mutation Status Prediction](https://www.medrxiv.org/content/10.64898/2026.05.01.26349658v1)
  来源：medRxiv | 日期：2026-05-08 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Clinical adoption of machine learning (ML) in medical imaging is limited by the lack of interpretability. To address this, we present understandable post-hoc artificial intelligence reports (UPhAIR), a pipeline designed ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Integrating protein and DNA embeddings for improving genome-wide transcription factor binding site prediction.](https://pubmed.ncbi.nlm.nih.gov/42099803/)
  来源：PubMed | 日期：2026-06-01 | 相关度：5.75 | 新颖度：9.25
  匹配主题：foundation_model_agent
  中文摘要：Transcription factors (TFs) regulate gene expression by binding to specific DNA sites on genome, making accurate TF binding site prediction critical for understanding gene regulation and downstream phenotypes. Almost all...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [How to make the most of your masked language model for protein engineering](http://arxiv.org/abs/2603.10302v2)
  来源：arXiv | 日期：2026-03-11 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：A plethora of protein language models have been released in recent years. Yet comparatively little work has addressed how to best sample from them to optimize desired biological properties. We fill this gap by proposing ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Steering Sequence Generation in Protein Language Models through Iterative Lookback Monte Carlo Sampling](https://www.biorxiv.org/content/10.64898/2026.05.01.722156v1)
  来源：bioRxiv | 日期：2026-05-07 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Protein language models (pLMs) leverage large-scale evolutionary data to generate novel sequences, but steering generation toward desired physicochemical properties without sacrificing diversity remains a major challenge...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Event-Causal RAG: A Retrieval-Augmented Generation Framework for Long Video Reasoning in Complex Scenarios](http://arxiv.org/abs/2605.06185v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Recent large vision-language models have achieved strong performance on short- and medium-length video understanding, yet they remain inadequate for ultra-long or even infinite video reasoning, where models must preserve...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Latent Abstraction for Retrieval-Augmented Generation](http://arxiv.org/abs/2604.17866v2)
  来源：arXiv | 日期：2026-04-20 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) has become a standard approach for enhancing large language models (LLMs) with external knowledge, mitigating hallucinations, and improving factuality. However, existing systems rely ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Text-Graph Synergy: A Bidirectional Verification and Completion Framework for RAG](http://arxiv.org/abs/2605.05643v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) has become a core paradigm for enhancing factual grounding and multi-hop reasoning in Large Language Models (LLMs). Traditional text-based RAG often retrieves logically irrelevant pse...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Claim-Level Transparency Analysis of LLM-Generated Diagnostic Reports: A Metabolic and Endocrine Biomarker Study](https://www.biorxiv.org/content/10.64898/2026.05.03.721751v1)
  来源：bioRxiv | 日期：2026-05-06 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models are increasingly deployed in clinical decision-support contexts, yet systematic evaluation of their factual reliability in generating patient-specific diagnostic reports remains sparse, particularly...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [DentaCoPilot: An LLM-Augmented Next-Procedure Recommender for General Dentistry, Designed for Dentist Augmentation](https://www.medrxiv.org/content/10.64898/2026.05.07.26352635v1)
  来源：medRxiv | 日期：2026-05-08 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Background. Commercial dental artificial intelligence in 2026 is overwhelmingly diagnostic: caries, calculus, periapical, and bone-level detection on radiographs. The clinically harder question that follows every diagnos...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Evolving Idea Graphs with Learnable Edits-and-Commits for Multi-Agent Scientific Ideation](http://arxiv.org/abs/2605.04922v1)
  来源：arXiv | 日期：2026-05-06 | 相关度：2.1 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：LLM-empowered multi-agent systems offer new potential to accelerate scientific discovery by generating novel research ideas. However, existing methods typically coordinate agents through temporary texts, such as drafts o...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ContextPilot: Fast Long-Context Inference via Context Reuse](http://arxiv.org/abs/2511.03475v4)
  来源：arXiv | 日期：2025-11-05 | 相关度：2.1 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：AI applications increasingly depend on long-context inference, where LLMs consume substantial context to support stronger reasoning. Common examples include retrieval-augmented generation, agent memory layers, and multi-...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BioResearcher: Scenario-Guided Multi-Agent for Translational Medicine](http://arxiv.org/abs/2605.05985v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：1.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Translational medicine turns underspecified development goals into evidence synthesis that must combine literature, trials, patents, and quantitative multi-omics analysis while preserving identifiers, uncertainty, and re...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic Retrieval-Augmented Generation for Financial Document Question Answering](http://arxiv.org/abs/2605.05409v1)
  来源：arXiv | 日期：2026-05-06 | 相关度：1.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：金融文档问答（QA）要求对企业报告中分散的结构化表格、文本叙述和脚注进行复杂的多步数值推理。现有的检索增强生成（RAG）方法多采用单次“检索-生成”范式，难以处理金融分析中常见的组合推理链。本文提出 FinAgent-RAG，一种代理式 RAG 框架，通过自验证机制编排迭代检索-推理循环，专为满足金融数值推理的精度需求而设计。该框架包含三项核心创新：(1) 采用难负样本挖掘训练的对比金融检索器，用于区分语义相似但数值不同的金融片段；(2...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BioMedArena: An Open-source Toolkit for Building and Evaluating Biomedical Deep Research Agents](http://arxiv.org/abs/2605.06177v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：1.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：构建深度研究智能体（Agent）目前面临“逐篇论文工程税”的挑战，即由于评估框架和工具注册的不一致，导致相同骨干模型在不同研究中表现出差异化的准确率，且集成新模型往往需要数周的工程量。为此，本研究推出了开源工具包 BioMedArena，旨在为生物医学研究智能体提供公平的比较平台。该工具包将生物医学智能体评估解耦为基准加载、工具暴露、工具选择、执行模式、上下文管理和评分六个层级，集成了 9 个功能家族的 147 个生物医学基准和 75 ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CAR: Query-Guided Confidence-Aware Reranking for Retrieval-Augmented Generation](http://arxiv.org/abs/2605.04495v1)
  来源：arXiv | 日期：2026-05-06 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）依赖文档排序来提供生成证据，但传统重排序方法主要优化查询与文档的相关性，而非生成的实际效用。相关文档可能引入噪声，而排名较低的文档有时能更有效地降低生成器的不确定性。本文提出 CAR（置信度感知重排序），这是一种查询引导、无需训练且即插即用的重排序框架，它将生成器置信度的变化作为文档效用的信号。CAR 通过对比“仅查询”与“查询+文档”条件下多次采样答案的语义一致性来估计置信度。显著提高置信度的文档会被提权，降低置...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [In Line with Context: Repository-Level Code Generation via Context Inlining](http://arxiv.org/abs/2601.00376v3)
  来源：arXiv | 日期：2026-01-01 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：仓库级代码生成要求模型理解整个代码库中函数、类和模块间的复杂依赖关系。针对现有检索增强生成（RAG）或上下文选择方法仅依赖表面相似性而难以捕捉深层语义依赖的问题，本文提出 InlineCoder 框架。该框架通过将未完成的函数内联到其调用图中，将复杂的仓库理解任务转化为更简单的函数级编码任务。InlineCoder 首先根据函数签名生成一个名为“锚点”的草稿补全，用于近似下游依赖并进行基于困惑度的置信度估计。随后，该锚点驱动双向内联过程...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [An Agent-Oriented Pluggable Experience-RAG Skill for Experience-Driven Retrieval Strategy Orchestration](http://arxiv.org/abs/2605.03989v2)
  来源：arXiv | 日期：2026-05-05 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）系统通常假设单一固定的检索流程足以应对异构任务，但事实性问答、多跳推理和科学验证对检索策略具有不同的偏好。本文提出 Experience-RAG Skill，这是一种面向智能体（Agent）的可插拔检索编排层，位于智能体与检索器池之间。该技术通过分析当前场景、咨询经验记忆并选择合适的检索策略，向智能体返回结构化证据。在固定候选池实验中，Experience-RAG Skill 在 BeIR/nq、BeIR/hotp...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Intentmaking and Sensemaking: Human Interaction with AI-Guided Mathematical Discovery](http://arxiv.org/abs/2605.05921v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：人工智能为科学发现提供了强大工具，但有效利用这些系统所需的交互范式仍有待探索。本文通过对11位使用AlphaEvolve（一种进化编码智能体）解决专业领域高级数学问题的专家数学家进行形成性用户研究，提出并刻画了一种被称为“意图构建”（intentmaking）的独特工作流。意图构建是指通过与系统的主动交互，不断发现、定义和完善实验目标的迭代过程。研究将其视为“意义构建”（sensemaking，即理解复杂或新颖数据的认知过程）的自然延伸...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RamanBench: A Large-Scale Benchmark for Machine Learning on Raman Spectroscopy](http://arxiv.org/abs/2605.02003v2)
  来源：arXiv | 日期：2026-05-03 | 相关度：0.7 | 新颖度：1.75
  匹配主题：未命中具体主题
  中文摘要：机器学习已改变多个科学领域，但拉曼光谱这一广泛用于无创分子分析的技术仍缺乏标准化基准。受限于数据集碎片化、评估不一致及模型难以捕捉光谱结构，该领域进展受阻。为此，我们推出了 RamanBench，这是首个大规模、完全可重复的拉曼光谱机器学习基准，包含简化的数据访问、评估协议、代码及实时排行榜。该基准统一了跨 4 个领域的 74 个数据集（其中 16 个为首次发布），涵盖 325,668 条光谱，涉及多种实验条件下的分类和回归任务。我们采...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [ChatIBD: design, safeguards, and early international use of a guideline-grounded generative AI tool for inflammatory bowel disease (IBD) professionals](https://www.medrxiv.org/content/10.64898/2026.05.06.26352526v1)
  来源：medRxiv | 日期：2026-05-07 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：本研究描述了ChatIBD的设计、运行保障及早期使用情况。ChatIBD是一个专为炎症性肠病（IBD）专业人士设计的生成式AI平台。该平台采用检索增强生成（RAG）技术，基于精选的IBD指南语料库进行问答。技术实现上，系统结合了混合语义与关键词检索、查询扩展及重排序，并强制模型仅依据检索到的材料回答并返回引用链接。安全保障措施包括集成欧洲药品管理局（EMA）的固定药物剂量信息、用户反馈捕获以及临床医生对标记输出的审查。在2025年10月...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Transforming Semi-structured Variant Assessments into Computable Clinical Assertions: A Pilot Study for AI-Assisted Curation](https://www.medrxiv.org/content/10.64898/2026.05.07.26352456v1)
  来源：medRxiv | 日期：2026-05-08 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Genomic medicine relies on expert evaluation of genomic variants, but this process is dramatically slowed by a lack of readily-accessible genomic knowledge. Although genomic knowledge resources such as ClinVar and CIViC ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [TCRTransBench: A Comprehensive Benchmark for Bidirectional TCR-Peptide Sequence Generation](http://arxiv.org/abs/2605.04762v1)
  来源：arXiv | 日期：2026-05-06 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：T-cell receptor (TCR) interactions with antigenic peptides underpin adaptive immunity and are pivotal for personalized immunotherapy and vaccine development. Despite recent progress, computational modeling of TCR-peptide...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Graph-Augmented LLMs for Swiss MP Ideology Prediction](http://arxiv.org/abs/2605.04643v1)
  来源：arXiv | 日期：2026-05-06 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Approximating the ideological position of Members of Parliament (MPs) is a fundamental task in political science, helping researchers understand legislative behavior, party alignment, and policy preferences. While Large ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [DiCLIP: Diffusion Model Enhances CLIP's Dense Knowledge for Weakly Supervised Semantic Segmentation](http://arxiv.org/abs/2605.04593v1)
  来源：arXiv | 日期：2026-05-06 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Weakly Supervised Semantic Segmentation (WSSS) with image-level labels typically leverages Class Activation Maps (CAMs) to achieve pixel-level predictions. Recently, Contrastive Language-Image Pre-training (CLIP) has bee...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MoLF: Mixture-of-Latent-Flow for Pan-Cancer Spatial Gene Expression Prediction from Histology](http://arxiv.org/abs/2602.02282v2)
  来源：arXiv | 日期：2026-02-02 | 相关度：2.4 | 新颖度：1.5
  匹配主题：未命中具体主题
  中文摘要：Inferring spatial transcriptomics (ST) from histology enables scalable histogenomic profiling, yet current methods are largely restricted to single-tissue models. This fragmentation fails to leverage biological principle...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Autoencoder/RandomForest-TabPFN for Cross-Cancer Metabolomics: Prostate and Breast Cancer Diagnosis Using Paper Spray and Ion Mobility-Mass Spectrometry Techniques.](https://pubmed.ncbi.nlm.nih.gov/42096511/)
  来源：PubMed | 日期：2026-05-07 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：准确快速的疾病诊断对前列腺癌（PC）和乳腺癌（BC）的早期干预至关重要。本研究提出了一种整合自动编码器（Autoencoder）、基于随机森林（Random Forest）的特征选择和表格先验数据拟合网络（TabPFN）的新型预测方法，用于分析癌症代谢组学数据。研究利用纸喷雾电离质谱（PSI-MS）和流动注射-行波离子迁移质谱（FI-TWIM-MS）获取了PC患者的尿液和血清样本数据，以及BC患者穿刺活检的代谢和脂质组特征。结果显示，该...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Securing the Agent: Vendor-Neutral, Multitenant Enterprise Retrieval and Tool Use](http://arxiv.org/abs/2605.05287v1)
  来源：arXiv | 日期：2026-05-06 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）和智能体 AI 系统在企业部署中日益普及，但真实的企业环境引入了多租户异构数据、严格访问控制和合规性等挑战。现有 RAG 架构存在根本性缺陷：系统仅按语义相关性而非授权权限对文档进行排序，导致租户查询可能因评分高而检索到他人的机密数据。本文形式化定义了这一差距，并分析了工具介导的泄露、多轮对话上下文积累和客户端编排绕过等安全缺陷。为此，我们提出一种分层隔离架构，结合策略感知摄取、检索时网关和共享推理，通过服务器端智...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Retrieval from Within: An Intrinsic Capability of Attention-Based Models](http://arxiv.org/abs/2605.05806v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）通常将检索和生成视为两个独立的系统。本研究探讨了基于注意力机制的编码器-解码器模型是否可以直接从其内部表示中进行检索。我们提出了 INTRA（通过注意力的内在检索）框架，在该框架中，解码器的注意力查询会对预编码的证据块进行评分，随后这些证据块被直接复用为生成的上下文。INTRA 在结构上统一了检索与生成，消除了传统 RAG 流程中常见的检索器与生成器不匹配问题。此外，该设计通过在不同查询间复用预计算的编码器状态，分...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Reinforced Informativeness Optimization for Long-Form Retrieval-Augmented Generation](http://arxiv.org/abs/2505.20825v2)
  来源：arXiv | 日期：2025-05-27 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：长篇问答（LFQA）要求从多源证据中合成连贯且具有事实依据的回复，这使得强化学习（RL）中的奖励设计变得至关重要。然而，传统的奖励机制通常基于精确匹配或唯一目标，适用于短篇问答但难以应对 LFQA，导致现有检索增强生成（RAG）系统缺乏可验证的奖励机制，存在反馈信号不稳定和优化效果不佳的问题。本文提出 RioRAG 框架，旨在实现可验证的信息量强化优化。首先，该框架将“信息量”定义为可衡量且可外部验证的 RL 目标。其次，RioRAG ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Architectural Constraints Alignment in AI-assisted, Platform-based Service Development](http://arxiv.org/abs/2605.04973v1)
  来源：arXiv | 日期：2026-05-06 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：AI辅助开发工具虽能实现服务的快速原型设计，但往往缺乏对生产环境所需的架构约束、基础设施依赖和组织标准的认知，导致生成的代码产物表现脆弱且部署性受限。本研究提出一种检索增强的脚手架方法（retrieval-augmented scaffolding），将基于平台的代码生成与智能体澄清循环（agentic clarification loops）相结合，旨在揭示并解决架构约束中的歧义。通过将模板检索与结构化交互相结合，该方法在服务脚手架搭...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Evaluating the Potential Impact of AI on Urinary Tract Infection Diagnosis in the Emergency Department Across Demographic Groups: Retrospective Cohort Study.](https://pubmed.ncbi.nlm.nih.gov/42090580/)
  来源：PubMed | 日期：2026-05-06 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：尿路感染（UTI）是急诊科（ED）的常见病，但存在严重的误诊和漏诊风险，尤其是老年群体。本研究开发了一种结合尿培养阳性预测与自然语言处理（NLP）的 AI 模型，仅利用患者就诊时的即时信息预测 UTI 诊断。研究对 2013 年至 2021 年间美国某医疗系统 9 个急诊科的 149,449 例非妊娠成年患者进行了回顾性分析。研究人员使用 Extreme Gradient Boosting（XGBoost）分类器预测尿培养阳性（≥10,...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [A Versatile AI Agent for Rare Disease Diagnosis and Risk Gene Prioritization](http://arxiv.org/abs/2605.06226v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：2.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Accurate and timely diagnosis is essential for effective treatment, particularly in the context of rare diseases. However, current diagnostic workflows often lead to prolonged assessment times and low accuracy. To addres...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial intelligence in cancer diagnostics: a primer for clinicians and scientists.](https://pubmed.ncbi.nlm.nih.gov/42097285/)
  来源：PubMed | 日期：2026-05-07 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Artificial Intelligence (AI) is rapidly transforming cancer care by enabling healthcare teams to make more accurate diagnoses, predict responses to therapy, improve outcomes, and deliver truly personalized treatment. As ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [How Does Chunking Affect Retrieval-Augmented Code Completion? A Controlled Empirical Study](http://arxiv.org/abs/2605.04763v1)
  来源：arXiv | 日期：2026-05-06 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）在代码补全中依赖分块（chunking）将源文件切分为可检索单元，但现有策略多缺乏实证支持。本研究通过受控实验评估了分块对代码补全质量的影响，涵盖四种代表性策略（函数、声明、滑动窗口、cAST）、4 种检索器、5 种生成器及 9 种参数配置，在 RepoEval 和 CrossCodeEval 两个基准上共运行 864 组实验。结果显示，分块策略对 RAG 代码补全具有显著统计学影响。出乎意料的是，基于函数的分块在...
  为什么值得看：How Does Chunking Affect Retrieval-Augme 与你的主题有弱匹配，暂时保留作低优先级跟踪。
