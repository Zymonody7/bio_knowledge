# 每日论文监控日报 (2026-10-25)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 22 篇新论文。

## 抓取状态

- arXiv：成功，命中 15 篇
- PubMed：成功，命中 25 篇
- bioRxiv：成功，命中 8 篇
- medRxiv：成功，命中 8 篇

## 最值得看

### Foundation Model / Agent

- [Trion-1: Unifying Language, Protein Sequence, and Structure with Diffusion Language Models](http://arxiv.org/abs/2610.31215v1)
  来源：arXiv | 日期：2026-10-22 | 相关度：10.0 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：We envision a general-purpose protein foundation model as a unified, interactive model of sequence, structure, and function, capable of understanding, generation, and cross-modal translation while retaining the instructi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [ChatT2: An Adaptive Framework for Developing a Large Language Model-Based Agent for Natural Product Domain Research](http://arxiv.org/abs/2609.25620v2)
  来源：arXiv | 日期：2026-09-22 | 相关度：8.85 | 新颖度：1.0
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Scientific investigations into microbial natural products (NPs) present significant challenges for novices, largely due to the complexity of microbial systems, biochemical diversity, technical skill requirements, and the...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TabAgent: Distilling LLM Agent Components into Cheap Classifiers](http://arxiv.org/abs/2602.16429v3)
  来源：arXiv | 日期：2026-02-18 | 相关度：6.55 | 新颖度：1.7
  匹配主题：foundation_model_agent
  中文摘要：Agentic systems, AI architectures that autonomously execute multi-step workflows to achieve complex goals, are often built using repeated large language model (LLM) calls for closed-set decision tasks such as routing, sh...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery](http://arxiv.org/abs/2606.06473v2)
  来源：arXiv | 日期：2026-06-04 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large language model (LLM) agents are increasingly applied to long-horizon tasks such as scientific discovery and machine learning engineering (MLE), where sustained self-evolution becomes a key capability. However, exis...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Population-scale drug target and variant prioritization with Varformer](https://www.biorxiv.org/content/10.64898/2026.10.16.759653v1)
  来源：bioRxiv | 日期：2026-10-22 | 相关度：3.75 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Human genetic variation is a powerful driver of therapeutic target prioritization, yet current models struggle to aggregate variable numbers of variants per gene and are bottlenecked by the scarcity of validated targets....
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [MouseGPT: A Large-scale Vision-Language Model for Mouse Behavior Analysis](https://www.biorxiv.org/content/10.1101/2025.03.27.645630v2)
  来源：bioRxiv | 日期：2026-10-23 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Analyzing animal behavior is crucial in neuroscience, yet deciphering its intricate dynamics remains challenging. Traditional machine vision approaches detect spontaneous behaviors but are constrained by limited interpre...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [A moving target: non-stationary selection governs unsupervised prediction of viral fitness](https://www.biorxiv.org/content/10.64898/2026.09.17.752359v2)
  来源：bioRxiv | 日期：2026-10-22 | 相关度：10.0 | 新颖度：1.0
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Anticipating how mutations change viral fitness is central to genomic surveillance and vaccine design. However, the phenotypic data behind the most accurate supervised variant-effect predictors is unavailable for most em...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [NeoGen-BC: A synergistic framework combining generative protein language models and multi-window deep learning for designing shared neoantigens in breast cancer.](https://pubmed.ncbi.nlm.nih.gov/42721858/)
  来源：PubMed | 日期：2026-10-22 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Breast cancer, particularly hormone receptor-positive (HR + ) and triple-negative (TNBC) subtypes, is often immunologically "cold," limiting immunotherapy efficacy. Neoantigen-based vaccines hold promise but face challen...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Drug-centric knowledge graph: representing therapeutic modality, pharmacology and multiscale biology](https://www.biorxiv.org/content/10.64898/2026.10.15.759051v2)
  来源：bioRxiv | 日期：2026-10-22 | 相关度：7.1 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Biomedical knowledge graphs link targets to mechanisms, diseases and phenotypes, but target-centered representations omit much of what distinguishes therapeutic interventions. We introduce a drug-centric knowledge graph,...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Identifying cohorts at elevated risk of cancers using generative modeling of patient health states](https://www.medrxiv.org/content/10.64898/2026.09.09.26362676v4)
  来源：medRxiv | 日期：2026-10-24 | 相关度：7.8 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：While large language models are powerful generators of new text, forecasting disease progression from longitudinal health histories remains a challenging problem. We introduce GenEHR, an autoregressive generative model t...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Non-generative readout with few-label calibration versus LoRA fine-tuning of a large language model for ASA physical status classification: accuracy, speed, cost and label efficiency in three data sources](https://www.medrxiv.org/content/10.64898/2026.10.20.26366028v1)
  来源：medRxiv | 日期：2026-10-22 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Background. The American Society of Anesthesiologists Physical Status (ASA-PS) class underpins perioperative risk communication, but its assignment is subjective. Generative large language models (LLMs) are slow and cost...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [From clinician review to measurable human oversight of AI-drafted paediatric discharge documents](https://www.medrxiv.org/content/10.64898/2026.10.20.26365977v1)
  来源：medRxiv | 日期：2026-10-22 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) now draft clinical documents that clinicians validate before release. Whether review intercepts generation errors is rarely measured, because edit counts and document ratings cannot show what...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Retrieval-Augmented Online Textual Memory for Episodic Memory Video Question Answering](http://arxiv.org/abs/2610.31284v1)
  来源：arXiv | 日期：2026-10-22 | 相关度：6.1 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Long egocentric videos pose a central challenge for multimodal language models: the visual stream must be compressed into a memory representation that can be searched efficiently while still preserving the evidence neede...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Semantics Delivery Network: Rethinking Web Retrieval Infrastructure for LLM Agents](http://arxiv.org/abs/2609.22486v2)
  来源：arXiv | 日期：2026-09-18 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) increasingly ground their answers in proprietary data and live web content through both single-shot retrieval-augmented generation (RAG) and multi-turn agentic search. Yet the web path they u...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Automated standardization of legacy biomedical metadata using an ontology-constrained LLM agent.](https://pubmed.ncbi.nlm.nih.gov/42918280/)
  来源：PubMed | 日期：2026-10-23 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Descriptive scientific metadata in public repositories are often incomplete and inconsistent with community standards and ontologies, limiting data FAIRness. Large language models (LLMs) offer a promising approach to aut...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [POI Recommendation with LLM-Augmented Multi-Graph Learning and Contrastive Alignment](http://arxiv.org/abs/2608.16407v2)
  来源：arXiv | 日期：2026-08-17 | 相关度：2.75 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Point-of-interest (POI) recommendation models based on graph neural networks achieve strong performance by propagating collaborative signals over user-item interactions, yet they struggle with the cold-start problem, whe...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ADAPT for Science: A Multi-Agent System for Self-Evolving Scientific Optimization](http://arxiv.org/abs/2610.30851v1)
  来源：arXiv | 日期：2026-10-22 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Scientific discovery often requires identifying a small number of high-performing designs in vast, constrained search spaces. This is difficult when evaluations are costly, feasible solutions are sparse, parameters are s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [IndoNutriQA: An Indonesian Clinical Nutrition Question Answering Benchmark](http://arxiv.org/abs/2610.31256v1)
  来源：arXiv | 日期：2026-10-22 | 相关度：4.45 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Clinical Question Answering (QA) underpins Clinical Intelligent Decision Support Systems, but progress is severely limited for low-resource languages such as Indonesian by the absence of public domain-specific data. We i...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [How Ground Truth Shapes Retrieval Scores: Evidence-Aware Evaluation of a Retrieval-Augmented Generation System for Breast Lesions](http://arxiv.org/abs/2610.31606v1)
  来源：arXiv | 日期：2026-10-22 | 相关度：2.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Purpose: To describe an evidence-aware retrieval evaluation protocol for a clinical retrieval-augmented generation (RAG) system over breast lesion management literature, addressing the dependence of retrieval scores on a...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [SoundnessBench: Can Your AI Scientist Really Tell Good Research Ideas from Bad Ones?](http://arxiv.org/abs/2605.30329v2)
  来源：arXiv | 日期：2026-05-28 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Autonomous AI research agents aim to speed up scientific discovery by automating the research pipeline from hypothesis generation to peer review. However, existing benchmarks rarely test a fundamental bottleneck whether ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Beyond Better Models: Barriers and a Path Forward in Generalisable TCR Antigen Specificity Prediction](https://www.biorxiv.org/content/10.64898/2026.10.12.758456v2)
  来源：bioRxiv | 日期：2026-10-22 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：T cells are at the centre of adaptive immunity, protecting the organism against infection and cancer. T cell receptors (TCRs), expressed on the surface of T cells, enable the recognition of target cells through interacti...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [From Structured Records to Patient Narratives: Preserving Clinical Alignment in LLM-Generated Health Summaries](http://arxiv.org/abs/2610.31467v1)
  来源：arXiv | 日期：2026-10-22 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：As wearable and digital health systems increasingly generate longitudinal physiological records, communicating these observations in patient-accessible language remains a significant challenge. Large Language Models (LLM...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
