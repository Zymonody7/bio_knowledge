# 每日论文监控日报 (2026-05-25)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 17 篇新论文。

## 抓取状态

- arXiv：成功，命中 10 篇
- PubMed：成功，命中 29 篇
- bioRxiv：成功，命中 11 篇
- medRxiv：成功，命中 8 篇

## 最值得看

### 方法创新

- [Large language model inference of macromolecular complex composition via model consensus and experimental data integration](https://www.biorxiv.org/content/10.64898/2026.05.20.726735v1)
  来源：bioRxiv | 日期：2026-05-23 | 相关度：7.15 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are poised to reshape how biologists retrieve specialized knowledge at scale. Yet their performance on deep, domain-specific queries is poorly defined because much biological information resi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [Digital Registrar: A Schema-First Framework for Multi-Cancer Privacy-Preserving Pathology Abstraction via Local LLMs](https://www.medrxiv.org/content/10.1101/2025.10.21.25338475v9)
  来源：medRxiv | 日期：2026-05-23 | 相关度：8.9 | 新颖度：1.7
  匹配主题：foundation_model_agent
  中文摘要：手术病理报告包含精细的癌症诊断数据，但其自由文本格式阻碍了自动化登记和二次分析。本研究开发了“Digital Registrar”框架，其核心是基于美国病理学家协会（CAP）标准的临床本体，通过严格类型的分层架构和 DSPy 签名实现。该系统涵盖 10 种主要癌症类型，涉及 193 个登记字段，包括淋巴结组和手术切缘等复杂变量。研究利用 DSPy 框架构建了与模型无关的提取流水线，并在单块 48GB GPU 上测试了本地部署的可行性。实...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MyeGPT: an AI agent for Multiple Myeloma](https://www.medrxiv.org/content/10.64898/2026.05.14.26353252v2)
  来源：medRxiv | 日期：2026-05-23 | 相关度：7.55 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Today, advancements in our understanding of cancer biology are increasingly attributed to large-scale clinical-molecular datasets. The case in point for multiple myeloma - the second-most prevalent haematological maligna...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection](http://arxiv.org/abs/2605.23723v1)
  来源：arXiv | 日期：2026-05-22 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language model agents increasingly rely on persistent memory to store past interactions, retrieve relevant demonstrations, and improve long-horizon task execution. However, this memory mechanism also creates a prac...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Efficient and Transferable Agentic Knowledge Graph RAG via Reinforcement Learning](http://arxiv.org/abs/2509.26383v5)
  来源：arXiv | 日期：2025-09-30 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Knowledge-graph retrieval-augmented generation (KG-RAG) couples large language models (LLMs) with structured, verifiable knowledge graphs (KGs) to reduce hallucination and provide reasoning traces. However, current KG-RA...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LLM-driven design of physics-constrained constitutive models: two agents are better than one](http://arxiv.org/abs/2605.23754v1)
  来源：arXiv | 日期：2026-05-22 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Developing constitutive models that capture how materials deform under load traditionally requires years of specialized expertise in continuum mechanics, machine learning, and scientific programming. Large language model...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [NiCLIP: Neuroimaging contrastive language-image pretraining model for predicting text from brain activation images](https://www.biorxiv.org/content/10.1101/2025.06.14.659706v3)
  来源：bioRxiv | 日期：2026-05-23 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Predicting cognitive processes from brain activation maps has remained an open question within the neuroscience community for many years. Meta-analytic functional decoding methods aim to tackle this issue by providing a ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Generalist large language models complement tailor-made predictors for tumor genomics interpretation](https://www.biorxiv.org/content/10.64898/2026.05.21.726957v1)
  来源：bioRxiv | 日期：2026-05-22 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：General-purpose large language models (LLMs) are trained on large corpora to acquire broad knowledge, but whether LLMs can replace, or augment, task-specific models is unclear. We evaluated LLMs on three real-world, clin...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Fine-grained Claim-level RAG Benchmark for Law](http://arxiv.org/abs/2605.21071v3)
  来源：arXiv | 日期：2026-05-20 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：The rapid progress of large language models (LLMs) is shifting semantic search toward a question-answering paradigm, where users ask questions and LLMs generate responses. In high-stake domains such as law, retrieval-aug...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Spectra as Language: Large Language Models for Scalable Stellar Parameter and Abundance Inference](http://arxiv.org/abs/2605.22162v2)
  来源：arXiv | 日期：2026-05-21 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Stellar spectra encode key information on the physical properties and chemical compositions of stars. Accurate stellar parameter determination is essential for addressing major questions such as galaxy and stellar evolut...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A transformer-based language model reveals developmental constraint and network complexity during zebrafish embryogenesis](https://www.biorxiv.org/content/10.1101/2025.07.09.663853v3)
  来源：bioRxiv | 日期：2026-05-22 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Understanding how regulatory complexity and constraint shape organismal development remains a central challenge in biology. The developmental hourglass framework posits that mid-embryogenesis -the phylotypic stage- is a ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Contrastive Distribution Matching for Amortized Sequential Monte Carlo in Discrete Diffusion](http://arxiv.org/abs/2605.23346v1)
  来源：arXiv | 日期：2026-05-22 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Discrete diffusion models have emerged as powerful frameworks for generating structured categorical data. However, efficiently sampling from reward-tilted distributions remains a fundamental challenge. While Twisted Sequ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Anatomy-Guided Vision-Language Learning with Angular Prototype Separation for Multi-Label Video Capsule Endoscopy Classification Under Class Imbalance](http://arxiv.org/abs/2603.17879v2)
  来源：arXiv | 日期：2026-03-18 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：This work presents a multi-label temporal event detection framework for video capsule endoscopy (VCE) that addresses the extreme class imbalance inherent in the Galar dataset by combining two principal contributions: an ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 其他

- [When Is Next-Token Prediction Useful? Marginalization, Ergodicity, Mixture Identifiability, Local Sufficiency, RAG, Tools, and Programming](http://arxiv.org/abs/2605.23278v1)
  来源：arXiv | 日期：2026-05-22 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Language models trained on observed sequences are often described as learning the conditional distribution of the next token given previous tokens. This description is only conditionally correct. A model trained on reali...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Machine-Assisted Topic Analysis of Large-Scale Health Experience Data: Identifying Sociodemographic Differences and Evaluating Bias in Large Language Models](https://www.medrxiv.org/content/10.64898/2026.05.20.26353755v1)
  来源：medRxiv | 日期：2026-05-22 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Introduction: Large-scale free-text data with socio-demographic information can capture nuanced accounts of lived experience that are difficult to detect in structured measures. However, manual qualitative analysis is di...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Interpreting Omics Data Analysis with Large Language Models for Disease Target and Drug Discovery](https://www.biorxiv.org/content/10.64898/2026.04.30.721768v2)
  来源：bioRxiv | 日期：2026-05-23 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：In biomedical scientific discovery, synthesizing prior knowledge from the literature is an essential component of interpreting numerical omics data analyses for disease target identification and drug discovery. Large lan...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Vector Retrieval with Similarity and Diversity: How Hard Is It?](http://arxiv.org/abs/2407.04573v4)
  来源：arXiv | 日期：2024-07-05 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Dense vector retrieval is an important building block of modern machine learning systems, underlying applications ranging from semantic search to retrieval-augmented generation and knowledge-intensive reasoning. Beyond r...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。
