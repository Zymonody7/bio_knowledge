# 每日论文监控日报 (2026-06-05)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 24 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='export.arxiv.org', port=443): Read timed out. (read timeout=60)
- PubMed：成功，命中 67 篇
- bioRxiv：成功，命中 12 篇
- medRxiv：成功，命中 16 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

今天这一档没有命中论文。

## 可追踪

### 方法创新

- [Decoding the Grammar of Protein-Protein Interaction Interfaces with Multimodal Representations](https://www.biorxiv.org/content/10.64898/2026.05.29.728739v1)
  来源：bioRxiv | 日期：2026-06-02 | 相关度：8.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Protein-protein interactions (PPI) govern essential cellular processes, making the computational identification of interacting sites a central challenge in structural biology, with important implications for protein engi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SciCore-Omics: a tri-modal foundation model unifying histology, spatial transcriptomics and language for spatial biology](https://www.biorxiv.org/content/10.64898/2026.05.30.728937v1)
  来源：bioRxiv | 日期：2026-06-03 | 相关度：5.75 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Histomorphology and spatial transcriptomics capture complementary aspects of tissue biology, but their relationships remain difficult to extract, align, and interpret at scale. Existing foundation models typically connec...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MAGI: Mechanistic Consequences of Genetic Variants via Genomic Foundation Models](https://www.biorxiv.org/content/10.64898/2026.05.31.729117v1)
  来源：bioRxiv | 日期：2026-06-03 | 相关度：5.55 | 新颖度：6.75
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Clinical variant interpretation requires mechanism-aware evidence to guide diagnosis and clarify the biological consequences of mutations. However, existing computational predictors and genomic foundation models largely ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Extracting Social Determinants of Health from Electronic Health Records: Development and Comparison of Rule-Based and Large Language Model Methods](https://www.medrxiv.org/content/10.1101/2025.11.15.25339520v3)
  来源：medRxiv | 日期：2026-06-04 | 相关度：7.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Background Social determinants of health (SDoH) are critical drivers of health outcomes but are often under-documented in structured electronic health record (EHR) data. Instead, SDoH are more commonly recorded in unstru...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [To RAG, or Not to RAG? A Comparative Evaluation of Retrieval-Augmented Generation for ICD Coding of German Tumor Diagnoses](https://www.medrxiv.org/content/10.64898/2026.05.27.26353695v1)
  来源：medRxiv | 日期：2026-06-03 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Introduction Coding tumor diagnoses from free-text clinical documentation currently requires substantial manual effort. Promising approaches for automating this process include large language mod-els (LLMs), embedding mo...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [KESOZI Digital Twin: Physics-Informed Neural Network for Independent Estimation and Prediction of Childhood Diarrheal Disease Burden in Kenya, Somaliland, and Zimbabwe](https://www.medrxiv.org/content/10.64898/2026.06.03.26354823v1)
  来源：medRxiv | 日期：2026-06-04 | 相关度：5.8 | 新颖度：5.75
  匹配主题：pathogenomics, foundation_model_agent, application_monitoring
  中文摘要：Childhood diarrheal disease remains a leading cause of morbidity and mortality among children under five years in sub-Saharan Africa, particularly in settings affected by inadequate sanitation, climate variability, malnu...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Agentic Authoring of OMOP Concept Sets from Natural Language](https://www.medrxiv.org/content/10.64898/2026.06.02.26354704v1)
  来源：medRxiv | 日期：2026-06-03 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Authoring OMOP concept sets from free-text descriptions remains a major bottleneck in scalable computable phenotyping for observational research. Existing tools support parts of this workflow but are designed primarily f...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Self-Reported Side Effects Among Reddit Users Taking Unapproved Retatrutide](https://www.medrxiv.org/content/10.64898/2026.05.28.26352819v1)
  来源：medRxiv | 日期：2026-06-03 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Gray-market retatrutide use is increasing, but patient safety experiences remain poorly characterized. This cross-sectional analysis examined Reddit posts and comments from retatrutide-specific and broader peptide or wei...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OmniCellAgent: An AI Scientist for Omic-Driven Scientific Discovery](https://www.biorxiv.org/content/10.1101/2025.07.31.667797v3)
  来源：bioRxiv | 日期：2026-06-02 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：In biomedical scientific discovery, identifying relevant omics datasets and interpreting analysis results using prior knowledge from databases and literature are essential for generating novel hypotheses. Although recent...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [MeDiCNet: Integrating Multi-scale Dynamic Convolution and Enhanced Position-Aware Transformer for DNA Methylation Site Prediction.](https://pubmed.ncbi.nlm.nih.gov/42234354/)
  来源：PubMed | 日期：2026-06-03 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：DNA methylation is a covalent modification of cytosine and adenine bases that regulates gene expression and underlies diverse biological processes and diseases. Existing computational methods often rely on fixed-scale fe...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Equitable Health Intelligence: An Open Benchmark of Multi-Population Machine Learning for Omics-Based Cancer Prognosis](https://www.biorxiv.org/content/10.64898/2026.05.29.728755v1)
  来源：bioRxiv | 日期：2026-06-02 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Purpose: Machine learning (ML) models for omics-based cancer prognosis are often trained on data from predominantly European-ancestry populations, producing biased predictions for other populations and undermining equita...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [An extensible laboratory information management system for data harmonization across research centers: The ICTS-Dashboard](https://www.medrxiv.org/content/10.64898/2026.05.31.26354439v1)
  来源：medRxiv | 日期：2026-06-02 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Abstract/SummaryO_ST_ABSBackgroundC_ST_ABSCollaborative research programs increasingly require infrastructure capable of integrating heterogeneous participant, sample, and experimental data while meeting evolving researc...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [MARRVEL-MCP: An agentic interface for Mendelian disease discovery via tool-augmented context engineering.](https://pubmed.ncbi.nlm.nih.gov/42167217/)
  来源：PubMed | 日期：2026-06-04 | 相关度：6.75 | 新颖度：0.25
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：Variant interpretation in rare diseases requires navigating multiple genomic databases, each with strict input formats, while synthesizing heterogeneous evidence. This process creates significant barriers for non-experts...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Deep learning model for predicting mRNA half-life based on 3'UTR sequences.](https://pubmed.ncbi.nlm.nih.gov/41932116/)
  来源：PubMed | 日期：2026-06-04 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：mRNA stability, quantified by half-life, is central to gene expression homeostasis and post-transcriptional regulation. Predicting mRNA half-life from 3' untranslated region (3'UTR) sequences alone, however, remains chal...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MVFAN-Kcr: A Multi-View Feature Fusion and Attention-Based Network for Lysine Crotonylation Site Identification.](https://pubmed.ncbi.nlm.nih.gov/42234353/)
  来源：PubMed | 日期：2026-06-03 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Lysine crotonylation (Kcr), as an emerging post-translational modification, plays a crucial role in core life activities such as chromatin dynamics and gene expression. To address the current limitations of Kcr site dete...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [The AFRIDIARRHEA multimodal fusion framework for Estimating the Burden of Diarrheal Diseases Among Children Under Five in Kenya, Zimbabwe, and Somaliland](https://www.medrxiv.org/content/10.64898/2026.06.01.26354632v1)
  来源：medRxiv | 日期：2026-06-02 | 相关度：4.8 | 新颖度：1.25
  匹配主题：pathogenomics, foundation_model_agent, application_monitoring
  中文摘要：Background: Accurate estimation of childhood diarrheal disease burden in Africa remains challenging because of limited surveillance, incomplete mortality data, pathogen-attribution uncertainty, and complex environmental ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Network Methods for Diagonal Integration of Unpaired Single-Cell Multi-Omics Data: A Review.](https://pubmed.ncbi.nlm.nih.gov/42234838/)
  来源：PubMed | 日期：2026-06-02 | 相关度：2.4 | 新颖度：2.0
  匹配主题：未命中具体主题
  中文摘要：Advances in single-cell sequencing have enabled multi-omics profiling at unprecedented resolution; however, mass spectrometry-based single-cell proteomics (scMS) remains inherently destructive, precluding simultaneous tr...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Hierarchical refinements of cis-regulatory inputs improve scalable gene expression prediction](https://www.biorxiv.org/content/10.64898/2026.05.31.729151v1)
  来源：bioRxiv | 日期：2026-06-02 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Deciphering the relationships between cis-regulatory elements (CREs) and target gene expression has long been a challenging problem in molecular biology. However, predicting gene expression from hundreds of candidate cis...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Seeing is making: AI visualisation and genomic prediction.](https://pubmed.ncbi.nlm.nih.gov/42242919/)
  来源：PubMed | 日期：2026-06-04 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：The integration of artificial intelligence (AI) into genomics is reshaping not only how biological data are analysed, but how genomic knowledge is produced and operationalised in clinical practice. Earlier computational ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Vermeer: Autoregressive generative modeling of microscopy predicts protein localization](https://www.biorxiv.org/content/10.64898/2026.06.01.729395v1)
  来源：bioRxiv | 日期：2026-06-02 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Fluorescent microscopy provides a rich view into how proteins localize within cells, but it remains experimentally infeasible to image human proteins across all of the different factors that can impact localization. We i...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Leveraging Digitization, Archiving and Artificial Intelligence to Re-examine Predictors of Sustained Mental Health Care Engagement in Ugandan First-Episode Psychosis Patients: A Study Protocol](https://www.medrxiv.org/content/10.64898/2026.06.02.26354672v1)
  来源：medRxiv | 日期：2026-06-03 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Background: We previously examined the burden and predictors of sustained mental health care engagement in Ugandan first episode psychosis patients by retrospective chart review methods. However, the extensive requiremen...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [A Three-Item Functional Screen for Multimodal Prognostic Triage in Mild Cognitive Impairment: Benchmarking Against Entorhinal Tau PET and Plasma p-tau217](https://www.medrxiv.org/content/10.64898/2026.06.01.26354584v1)
  来源：medRxiv | 日期：2026-06-02 | 相关度：3.05 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Importance: Broadening access to biomarker-informed risk stratification in mild cognitive impairment (MCI) has become even more critical to early assessment in Alzheimer disease given recent developments in regulatory ap...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Multimodal Ultrasound Integration Pathways and Paradigm Innovations in Precision Diagnosis and Treatment of Thyroid Cancer.](https://pubmed.ncbi.nlm.nih.gov/42230172/)
  来源：PubMed | 日期：2026-06-02 | 相关度：2.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Thyroid cancer, the fastest-growing endocrine malignancy, is shifting from morphological evaluation to molecular-functional imaging. This review systematically evaluates the translational value of multimodal ultrasound t...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Tuberculosis in households with infectious cases in Kampala city: Harnessing health data science for new insights on an ancient disease with persistent, unresolved problems.](https://pubmed.ncbi.nlm.nih.gov/42241447/)
  来源：PubMed | 日期：2026-01-01 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Tuberculosis (TB) is prevalent in Uganda and overlaps with a high rate of HIV/TB coinfection. While nearly all hospital-based TB cases in Kampala, the capital of Uganda, show clear TB symptoms, 30% or more of undiagnosed...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
