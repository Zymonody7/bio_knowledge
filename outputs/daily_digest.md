# 每日论文监控日报 (2026-10-12)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 11 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='export.arxiv.org', port=443): Read timed out. (read timeout=60)
- PubMed：成功，命中 37 篇
- bioRxiv：成功，命中 12 篇
- medRxiv：成功，命中 5 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [Multilingual Disparities in Large Language Model-Based Symptom Detection for Global Disease Surveillance: Evaluation Study.](https://pubmed.ncbi.nlm.nih.gov/42854221/)
  来源：PubMed | 日期：2026-10-09 | 相关度：8.15 | 新颖度：1.25
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：Symptom detection is essential in global disease surveillance to detect potential outbreaks, as symptoms are the first observable signs of infection. To reflect real-time ground truth conditions during pandemics, social ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Structured biological evidence enables general-purpose language models to predict bacteriophage-host interactions](https://www.biorxiv.org/content/10.64898/2026.06.10.727770v3)
  来源：bioRxiv | 日期：2026-10-09 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Biological interaction inference often requires integrating heterogeneous evidence that differs in biological meaning, provenance, specificity, and reliability. Existing computational approaches typically compress such e...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Archetype analysis of multiplexed antibody imaging reveals interpretable morphological programs in optical pooled screens](https://www.biorxiv.org/content/10.64898/2026.10.07.757470v1)
  来源：bioRxiv | 日期：2026-10-09 | 相关度：7.1 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：High-content imaging-based screens with small molecule or genetic perturbations rely on rich optical phenotypes, yet how distinct subcellular markers contribute complementary biological information remains unclear. Here,...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Protein large language model-assisted one-to-one gene homology mapping in cross-species single-cell transcriptome integration.](https://pubmed.ncbi.nlm.nih.gov/42855280/)
  来源：PubMed | 日期：2026-10-09 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Cross-species integration of single-cell transcriptomes requires establishing gene correspondences to enable comparative analysis of expression profiles across organisms. Current approaches predominantly rely on Ensembl ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Dementia Language Models: a generalizable and controllable representation of cognitive impairment](https://www.biorxiv.org/content/10.64898/2026.09.16.752129v2)
  来源：bioRxiv | 日期：2026-10-10 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：We introduce Dementia Language Models (DeLMs)--generalizable and controllable representations of cognitive impairment through language--alongside an evaluation framework for establishing their validity and clinical groun...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [KRAKEN: A provenance-tracked knowledge graph for multiomic and wellness research](https://www.biorxiv.org/content/10.64898/2026.08.18.745544v2)
  来源：bioRxiv | 日期：2026-10-09 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Existing general-purpose biomedical knowledge graphs tend to focus on disease mechanisms and drug repurposing, leaving multiomic and wellness-relevant content underrepresented. KRAKEN (Knowledge Research & Analysis Kit f...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Artificial intelligence in human microbiome research: from data integration to explainable translation.](https://pubmed.ncbi.nlm.nih.gov/42859175/)
  来源：PubMed | 日期：2026-10-10 | 相关度：2.7 | 新颖度：5.75
  匹配主题：pathogenomics
  中文摘要：The human microbiome is integral to health, metabolism, immunity, and physical protection, with dysbiosis linked to metabolic disorders, autoimmune conditions, and cancer. High-throughput sequencing has generated massive...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Position-wise Fold-Switch Prediction in Metamorphic Proteins: A Comparison of Handcrafted and Language Model Features](https://www.biorxiv.org/content/10.64898/2026.09.30.755750v2)
  来源：bioRxiv | 日期：2026-10-09 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：In this work, we focus on predicting fold-switching phenomena observed in certain protein structures. Proteins that undergo fold-switching are called metamorphic proteins. We model fold-switch prediction in proteins as a...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [The structural context of mutations in proteins predicts their effect on antibiotic resistance.](https://pubmed.ncbi.nlm.nih.gov/42852653/)
  来源：PubMed | 日期：2026-10-09 | 相关度：5.55 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：In Mycobacterium tuberculosis , a prevalent and deadly pathogen, resistance to antibiotics evolves primarily through non-synonymous mutations in proteins. Sequence-based analyses can uncover the genetic basis of antibiot...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Advancing genetic pathogenicity prediction with three-dimensional proteoform-phenotype analysis](https://www.medrxiv.org/content/10.64898/2026.10.07.26364649v1)
  来源：medRxiv | 日期：2026-10-09 | 相关度：3.65 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Ascertaining the pathogenicity and clinical relevance of genetic mutations is a longstanding challenge across human disease. This is particularly relevant for genes with many variants of unknown significance (VUS), such ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [A Zero-Shot Decision Model (Jev) Matches a Trained Classifier but Ranks Its Own Errors Worse: Calibrated, Split-Conformal Next-Procedure Recommendation in General Dentistry](https://www.medrxiv.org/content/10.64898/2026.05.07.26352635v5)
  来源：medRxiv | 日期：2026-10-10 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：On real-world dental records, procedure history predicts the next procedure category well, and a simple history-aware classical model beats every large-language-model (LLM) design we tested. We study the question that fo...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
