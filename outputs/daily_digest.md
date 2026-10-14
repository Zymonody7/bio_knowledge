# 每日论文监控日报 (2026-10-14)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 17 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：429 Client Error: Unknown Error
- PubMed：成功，命中 27 篇
- bioRxiv：成功，命中 17 篇
- medRxiv：成功，命中 15 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [Evaluation of six generative large language models answering pre-analytical questions in medical microbiology.](https://pubmed.ncbi.nlm.nih.gov/42869292/)
  来源：PubMed | 日期：2026-10-13 | 相关度：7.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have the potential to be integrated into diagnostics workflows, yet their reliability in pre-analytical diagnostic stewardship remains uncertain. We aimed to evaluate the performance of six L...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [AI-assisted identification of potential treatment injury from inpatient discharge summaries: an early-stage sociotechnical evaluation in a New Zealand district hospital](https://www.medrxiv.org/content/10.64898/2026.10.09.26365175v1)
  来源：medRxiv | 日期：2026-10-13 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Objectives: To assess the feasibility and early performance of an AI-assisted screening workflow that reviews inpatient discharge summaries to identify potential treatment injuries for clinician review and, where appropr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [AmyloCore-ML: AI/Machine Learning Enabled Identification of Amyloid Fibril Core Regions Using Protein Language Models](https://www.biorxiv.org/content/10.64898/2026.09.25.754455v2)
  来源：bioRxiv | 日期：2026-10-12 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Identification of amyloid forming regions in proteins remains central to understanding of their aggregation behaviour, which are central to various neurodegenerative and systemic disorders. Many predictors have been desi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [IVA, a locally deployable Intelligent Variant Analyser based on a small language model for complete case-level and trio-based genomic interpretation.](https://www.medrxiv.org/content/10.64898/2026.10.07.26364945v1)
  来源：medRxiv | 日期：2026-10-13 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Background: Recent work has brought large language models (LLMs) into clinical variant interpretation. In most existing approaches, the model is confined to text-level operations, retrieving, extracting, compacting, and ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Spatial proteomics identifies altered thick ascending limb cells as drivers of kidney disease through uromodulin retention](https://www.biorxiv.org/content/10.64898/2026.10.09.756985v1)
  来源：bioRxiv | 日期：2026-10-12 | 相关度：5.05 | 新颖度：5.25
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：Chronic kidney disease (CKD) is increasingly prevalent and is a leading cause of mortality. Recent transcriptomic studies have identified the persistence of injury-induced renal tubular epithelial cell states, yet the ce...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [RadKev: An Open-Weight Decision Model for Radiology](https://www.medrxiv.org/content/10.64898/2026.10.07.26364991v1)
  来源：medRxiv | 日期：2026-10-13 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Background: Many radiology decisions, such as whether a report describes a finding or how urgently a study should be read, are choices among a fixed set of answers. Decision models return a probability for each permitted...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### 数据集 / Benchmark

- [GLARE: Genomic Language model for Automated Repetitive Element classification](https://www.biorxiv.org/content/10.64898/2026.10.06.757139v1)
  来源：bioRxiv | 日期：2026-10-11 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Reliable classification of transposable elements (TEs) is important for genome annotation and evolutionary analysis, yet remains challenging: TE families differ widely across taxa, reference databases label them inconsis...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [ClinStigma: A Clinician-Guided Framework for Developing Synthetic Benchmarks of Contextual Stigmatizing Language in Clinical Documentation](https://www.medrxiv.org/content/10.64898/2026.10.10.26365233v1)
  来源：medRxiv | 日期：2026-10-12 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Objective Large language models (LLMs) are increasingly used to generate, summarize, and evaluate clinical documentation, yet standardized methods for evaluating nuanced, context-dependent clinical language remain limite...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Global statistical constraint and local partner-sensitive inference support dynamic, open-ended verbal coordination](https://www.biorxiv.org/content/10.64898/2026.10.03.756413v1)
  来源：bioRxiv | 日期：2026-10-11 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Effective verbal communication requires individuals to align their communicative intentions through the precise use of utterances, yet how this is achieved in dynamic, open-ended communication remains unclear. Combining ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [An Expert-Curated Benchmark for Frontier and Local LLMs Querying a Biomedical Knowledge Graph](https://www.biorxiv.org/content/10.64898/2026.10.04.756532v1)
  来源：bioRxiv | 日期：2026-10-11 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：We combine GeneNetwork's 1TB structured database with its metadata as an RDF graph and an associated literature corpus. We benchmark frontier and local LLMs querying it through four architectures: document, graph and age...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [AI-Driven Design of Next-Generation Immunoinformatics Multi-Epitope Subunit Vaccine Targeting the Most Virulent Mpox Proteome: A Structural and Kinetic Validation Framework](https://www.biorxiv.org/content/10.64898/2026.10.04.756542v1)
  来源：bioRxiv | 日期：2026-10-11 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：The resurgence of the Mpox virus (MPXV) highlights the urgent need for scalable, mutation-resistant countermeasures. Slow development timelines hinder traditional empirical vaccine discovery, while conventional vaccinolo...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Autonomous AI agents discover reverse transcriptases with tandem repeat arrays](https://www.biorxiv.org/content/10.64898/2026.10.05.755809v1)
  来源：bioRxiv | 日期：2026-10-11 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Metagenomic databases hold vast quantities of unexplored genetic material that can seed tools for biotechnology and medicine, but discovery is limited by our ability to examine sequence data at scale. Here, we show that ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Sequence context decodes multi-state conformational heterogeneity from crystallographic B-factors](https://www.biorxiv.org/content/10.64898/2025.12.05.692009v3)
  来源：bioRxiv | 日期：2026-10-11 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Protein function is governed by conformational ensembles, yet the overwhelming majority of experimentally determined structures capture only static snapshots, leaving the multi-state heterogeneity that underlies biologic...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Multimodal Machine Learning-Based Clinical and Genomic Prognostic Factors for Progression-Free Survival in Metastatic Breast Cancer Using Phase III MONALEESA Trials](https://www.medrxiv.org/content/10.64898/2026.10.09.26364892v1)
  来源：medRxiv | 日期：2026-10-13 | 相关度：3.05 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Purpose: Cyclin-dependent kinase 4/6 inhibitors in combination with endocrine therapy have become widely adopted as a first-line treatment approach for hormone receptor-positive (HR+)/human epidermal growth factor recept...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CodonBench: separating gene context, exon position, and variant-specific component in synonymous-variant classification](https://www.biorxiv.org/content/10.64898/2026.08.12.744371v2)
  来源：bioRxiv | 日期：2026-10-11 | 相关度：2.65 | 新颖度：0.75
  匹配主题：sequencing_bioinformatics
  中文摘要：Background. A synonymous variant leaves the protein unchanged, so a classifier that still separates pathogenic from benign examples must be reading something beyond the protein. Such variants test cleanly what a codon-le...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Representing biological concepts as directions in foundation model embeddings](https://www.biorxiv.org/content/10.64898/2026.10.10.758204v1)
  来源：bioRxiv | 日期：2026-10-12 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Biological foundation models encode rich information about protein structure, function, and cellular state in high-dimensional embeddings, but accessing specific biological properties typically relies on additional, task...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Artificial Intelligence in Prediction and Diagnosis of Fetal Growth Restriction: A Systematic Review.](https://pubmed.ncbi.nlm.nih.gov/42862457/)
  来源：PubMed | 日期：2026-10-12 | 相关度：3.75 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：This systematic review evaluates evidence on artificial intelligence (AI) and machine learning (ML) models for prediction and diagnosis of fetal growth restriction (FGR). The authors searched PubMed, Scopus, Embase, Web ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
