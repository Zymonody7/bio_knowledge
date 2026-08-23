# 每日论文监控日报 (2026-08-23)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 23 篇新论文。

## 抓取状态

- arXiv：成功，命中 11 篇
- PubMed：成功，命中 33 篇
- bioRxiv：成功，命中 10 篇
- medRxiv：成功，命中 20 篇

## 最值得看

### 方法创新

- [An AI System for Autonomous Algorithm Evolution in Drug Development](https://www.biorxiv.org/content/10.64898/2026.08.16.745117v1)
  来源：bioRxiv | 日期：2026-08-20 | 相关度：7.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence (AI) is increasingly permeating the drug development pipeline. Numerous algorithms for accelerating this multi-stage and multi-task process have been constructed, which depends heavily on expert d...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [Autonomous biomedical research with an artificial intelligence agent.](https://pubmed.ncbi.nlm.nih.gov/42424436/)
  来源：PubMed | 日期：2026-08-20 | 相关度：8.5 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Biomedical research is increasingly constrained by repetitive, fragmented workflows that slow discovery. We introduce Biomni, a general-purpose biomedical artificial intelligence agent that autonomously executes diverse ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BCIJelly: An integrated ecosystem for brain-computer interface research](https://www.biorxiv.org/content/10.64898/2026.08.13.744531v1)
  来源：bioRxiv | 日期：2026-08-20 | 相关度：6.55 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Brain-computer interface (BCI) research relies on multistage computational pipelines, but progress has been slowed by fragmented data formats, heterogeneous decoder implementations and hardware-specific deployment toolch...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MetaFemina: development and evaluation of a large language model-assisted platform for automated meta-analysis of nutritional exposures and breast, ovarian, and uterine cancer risk](https://www.medrxiv.org/content/10.64898/2026.08.18.26360713v1)
  来源：medRxiv | 日期：2026-08-21 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Objective To develop and evaluate an automated large language model (LLM)-based framework for conducting meta-analyses of nutrition-related exposures and the risk of breast, ovarian, and uterine cancers. Design We develo...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [MTS-Bench: A Manchester Triage System Benchmark for Language Model Triage Safety](https://www.medrxiv.org/content/10.64898/2026.08.04.26359651v2)
  来源：medRxiv | 日期：2026-08-21 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：BackgroundGeneral purpose language models such as ChatGPT are increasingly used by physicians and triage nurses during emergency triage. A recent study reported 51.6% undertriage of emergencies when patients queried Chat...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Retrieval-Augmented Large Language Models for Clinically Aligned Adverse Event Coding in Acute Myeloid Leukemia Clinical Trials](https://www.medrxiv.org/content/10.64898/2026.08.17.26360282v1)
  来源：medRxiv | 日期：2026-08-20 | 相关度：7.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：BackgroundAdverse event (AE) coding is essential for safety monitoring in oncology clinical trials, particularly in acute myeloid leukemia (AML), where intensive therapies are associated with frequent and heterogeneous t...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Quality, consistency, and clinical safety of AI-generated versus clinician-written clinical notes: a multi-country paired simulation study](https://www.medrxiv.org/content/10.64898/2026.08.18.26360701v1)
  来源：medRxiv | 日期：2026-08-21 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Background Ambient AI documentation tools, known as scribes, are entering routine clinical practice at scale, but the evidence comparing the notes they produce against clinician-written notes is dominated by single-site,...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [TabMedQA: From Structured Data to Question-Answer Datasets in Early Clinical Decision-Making](https://www.medrxiv.org/content/10.64898/2026.08.19.26360779v1)
  来源：medRxiv | 日期：2026-08-21 | 相关度：7.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：The rising adoption of Large Language Models (LLMs) and Retrieval Augmented Generation (RAG) in clinical general practice demands datasets that capture realistic early-stage clinical decision-making, where experts must d...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [A Human-in-the-Loop Large Language Model System Based on the Model Context Protocol for Differential Diagnosis from Electronic Medical Records and Literature](https://www.medrxiv.org/content/10.64898/2026.08.18.26359085v1)
  来源：medRxiv | 日期：2026-08-21 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Diagnostic errors, including misdiagnoses and delayed clinical diagnoses, could affect outcomes of a significant patient population, particularly individuals presenting with rare diseases or non-specific symptoms. From r...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [From Lectures to Learning Outcomes: Meaningful Integration of AI-Generated Content in Pre-Clerkship Medical Training](https://www.medrxiv.org/content/10.1101/2025.05.13.25327518v2)
  来源：medRxiv | 日期：2026-08-20 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：BackgroundLarge Language Models (LLMs) can efficiently synthesize educational content, yet few studies have evaluated standardized, LLM-powered curricular interventions and their effects on medical student learning. Meth...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Training-Free LLM-Based Recommendation with Post-LLM Item Refinement Using Collaborative Signals](http://arxiv.org/abs/2608.19665v1)
  来源：arXiv | 日期：2026-08-20 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have shown promise for training-free recommendation, but LLM-generated user interests are often too broad for fine-grained item retrieval. Existing methods incorporate collaborative filtering...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Self-Reported Side Effects Among Reddit Users Taking Nonapproved Retatrutide](https://www.medrxiv.org/content/10.64898/2026.05.28.26352819v2)
  来源：medRxiv | 日期：2026-08-21 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Gray-market retatrutide use is increasing, but patient safety experiences remain poorly characterized. This cross-sectional analysis examined Reddit posts and comments from retatrutide-specific and broader peptide or wei...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EchoTrace: Diagnosing Recursive Risks in LLM-Powered Recommender Systems](http://arxiv.org/abs/2602.07442v2)
  来源：arXiv | 日期：2026-02-07 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly integrated into recommender systems as data augmenters, profile generators, and recommendation modules. While these roles can enhance semantic understanding and recommendatio...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Memory Centric Power Allocation for Multi-Agent Embodied Question Answering](http://arxiv.org/abs/2604.17810v2)
  来源：arXiv | 日期：2026-04-20 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：This paper considers multi-agent embodied question answering (MA-EQA), which enables robot teams to answer queries based on their long-horizon observations. In contrast to existing edge resource management methods that o...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [ArkEval: Benchmarking and Evaluating Automated CodeRepair for ArkTS](http://arxiv.org/abs/2602.08866v2)
  来源：arXiv | 日期：2026-02-09 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models have transformed code generation, enabling unprecedented automation in software development. As mobile ecosystems evolve, HarmonyOS has emerged as a critical platform requiring robust development to...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Scientific Data Skills: Enabling Agent-Ready Scientific Data Services at Scale](http://arxiv.org/abs/2608.19625v1)
  来源：arXiv | 日期：2026-08-20 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Scientific data are increasingly used by AI agents, yet existing dataset representations provide limited support for autonomous discovery, interpretation, and invocation. This limitation stems from the fragmentation of s...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Efficient exploration of sequence space enables rapid generation of functional genome editors](https://www.biorxiv.org/content/10.64898/2026.08.16.745112v1)
  来源：bioRxiv | 日期：2026-08-20 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：The problem of how protein sequences translate into defined functions remains largely unsolved despite decades of progress. New methods to efficiently explore protein sequence space will help to shed light on these seque...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GridCodex: A RAG-Driven AI Framework for Power Grid Code Reasoning and Compliance](http://arxiv.org/abs/2508.12682v2)
  来源：arXiv | 日期：2025-08-18 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：The global shift towards renewable energy presents unprecedented challenges for the electricity industry, making regulatory reasoning and compliance increasingly vital. Grid codes, the regulations governing grid operatio...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Bootstrap Theory of Representational Emergence (TBER): Explanatory Insufficiency, Transition Regimes, and the Emergence of New Representational Levels](http://arxiv.org/abs/2606.07303v4)
  来源：arXiv | 日期：2026-06-05 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Representation learning is central to modern machine learning, yet most research focuses on optimizing representations after a framework has been selected. The Bootstrap Theory of Representational Emergence (TBER) addres...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Integrated evaluation of rapid diagnostic testing, genotypic-phenotypic resistance profiling, and AI-Assisted prediction models for antimicrobial stewardship and clinical outcomes in a resource-limited setting.](https://pubmed.ncbi.nlm.nih.gov/42623344/)
  来源：PubMed | 日期：2026-01-01 | 相关度：4.4 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：Antimicrobial resistance (AMR) remains a major global health concern, necessitating timely and accurate diagnostic approaches to guide appropriate therapy. Conventional antibiotic susceptibility testing (AST) is often as...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial Intelligence-Empowered Single-Cell Phenotyping for Rapid, Automated Pathogen Diagnostics.](https://pubmed.ncbi.nlm.nih.gov/42627671/)
  来源：PubMed | 日期：2026-08-21 | 相关度：2.45 | 新颖度：0.25
  匹配主题：application_monitoring
  中文摘要：Accurate bacterial identification and antimicrobial susceptibility testing (AST) are essential for timely clinical decision-making. Conventional diagnostic methods typically require 24-48 h, leading to inappropriate empi...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [TrustRAG: Blockchain-Enhanced RAG via Committee-Based Credibility Scoring](http://arxiv.org/abs/2608.20097v1)
  来源：arXiv | 日期：2026-08-20 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) lets Large Language Models (LLMs) pull in up-to-date, domain-specific information instead of relying only on what they were trained on. Yet most RAG systems still draw from centralize...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [What Makes a Good Fiqh Retriever? Answer Retrieval for Arabic Islamic Jurisprudence](http://arxiv.org/abs/2608.20246v1)
  来源：arXiv | 日期：2026-08-20 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation is used for Islamic question answering, but most systems are evaluated end-to-end, making retrieval failures difficult to isolate from generation failures. We study answer-bearing retrieval...
  为什么值得看：What Makes a Good Fiqh Retriever? Answer 与你的主题有弱匹配，暂时保留作低优先级跟踪。
