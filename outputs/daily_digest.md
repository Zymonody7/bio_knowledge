# 每日论文监控日报 (2026-10-05)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 16 篇新论文。

## 抓取状态

- arXiv：成功，命中 15 篇
- PubMed：成功，命中 21 篇
- bioRxiv：成功，命中 2 篇
- medRxiv：成功，命中 5 篇

## 最值得看

### Foundation Model / Agent

- [Sentence-Level Context Sensitivity as a Training-Free Detector of Unsupported Content, Evaluated Against Trained Verifiers](http://arxiv.org/abs/2607.04223v2)
  来源：arXiv | 日期：2026-07-05 | 相关度：7.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) assistants summarize records in clinical and legal work, where one unsupported sentence can mislead a reader. The contrast between an output's likelihood with and without its source i...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [CLIMB: Confidence-Guided Complementary Evidence for Multimodal Retrieval-Augmented Generation](http://arxiv.org/abs/2610.03421v1)
  来源：arXiv | 日期：2026-10-02 | 相关度：6.8 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Multimodal large language models (MLLMs) have shown strong visual reasoning abilities, but knowledge-intensive visual question answering often requires external textual evidence beyond the image and the model's parametri...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Guideline-Augmented Multi-Agent Framework for Schema-as-Code Biomedical Named Entity Recognition](http://arxiv.org/abs/2610.02970v1)
  来源：arXiv | 日期：2026-10-02 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have shown promising potential for biomedical named entity recognition (BioNER) through instruction following and in-context learning. However, existing LLM-based BioNER methods still face tw...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Can Large Language Models Diagnose Primary Immunodeficiency from Patient-Described Symptoms?](https://www.medrxiv.org/content/10.64898/2026.05.26.26353818v2)
  来源：medRxiv | 日期：2026-10-04 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Patients with primary immunodeficiency (PI) face prolonged diagnostic delays and may increasingly turn to large language models (LLMs) to interpret their symptoms during this period. We evaluated whether an LLM could rec...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [SoftGene: Protein Language Model-Enhanced Soft Prompting for Interpretable Gene Set Annotation](http://arxiv.org/abs/2610.03029v1)
  来源：arXiv | 日期：2026-10-02 | 相关度：6.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Gene set analysis is a cornerstone of functional genomics, yet it remains labor-intensive and heavily dependent on manual curation and expert biological interpretation. While Large Language Models (LLMs) have emerged as ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Predictor-Guided Latent Space Codon Optimization for Maximizing Protein Expression](http://arxiv.org/abs/2610.03098v1)
  来源：arXiv | 日期：2026-10-02 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Codon optimization, the process of selecting synonymous codons to improve mRNA translation efficiency and protein expression, is central to therapeutic protein production and mRNA vaccines, yet it remains a hard problem....
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Digital Twin-Assisted Mapping of ICS Telemetry to ATT&CK for ICS with Evidence-Driven Dependency Reasoning](http://arxiv.org/abs/2610.02955v1)
  来源：arXiv | 日期：2026-10-02 | 相关度：6.15 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Reconstructing adversarial behavior from Industrial Control System (ICS) telemetry is difficult because process observations reveal physical changes more directly than the actions that produced them. This paper presents ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Output Language Confusion under Multilingual Prompt Contamination](http://arxiv.org/abs/2610.02926v1)
  来源：arXiv | 日期：2026-10-02 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Standard factual benchmarks assume clean monolingual prompts and exact-match scoring, two assumptions that break simultaneously in real-world multilingual deployment, from retrieval-augmented generation pipelines returni...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Investigating the Role of Reasoning-Language Alignment in Monolingual Retrieval-Augmented Generation](http://arxiv.org/abs/2610.03136v1)
  来源：arXiv | 日期：2026-10-02 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Reasoning traces improve large language models (LLMs), but current models are trained to reason mostly in English. It has been shown that forcing a model to reason in another language degrades accuracy, even when the rea...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [A kinetic-aware approach to infer metabolic variations and flux using transcriptomics and metabolomics data](https://www.biorxiv.org/content/10.64898/2026.09.27.754711v1)
  来源：bioRxiv | 日期：2026-10-02 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Assessing metabolic variations and flux quantities enable systematic understandings of metabolic shifts, reprogramming, adaptation and interactions in human diseases. However, omics-based estimation of metabolic flux and...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Auditing Protein-Protein Interaction Signals with Sparse Autoencoder Fingerprints](https://www.biorxiv.org/content/10.64898/2026.09.27.754758v1)
  来源：bioRxiv | 日期：2026-10-02 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Protein language models have become a dominant foundation for sequence-based protein-protein interaction (PPI) prediction, but their generalization remains limited under stringent evaluation, and benchmark accuracy alone...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Assessing AI and Neurologist Diagnostic Reasoning Against Neuropathological Ground Truth](https://www.medrxiv.org/content/10.64898/2026.07.07.26356930v2)
  来源：medRxiv | 日期：2026-10-03 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：BACKGROUND Accurate differential diagnosis of complex neurological disorders remains challenging due to overlapping clinical features and heterogeneous disease presentations. Although large language models (LLMs) show pr...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Multi-model LLM assessment of Quality Control Circle methodological quality: a designed-anchor reliability study](https://www.medrxiv.org/content/10.64898/2026.08.12.26360276v2)
  来源：medRxiv | 日期：2026-10-02 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Background: Quality Control Circle (QCC) reports are often reviewed qualitatively, but reviewer workload and inter-rater variability make large-scale assessment difficult. We evaluated whether multiple large language mod...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Generalizability of proteomic risk prediction across biobanks reveals dependence on phenotype definitions](https://www.medrxiv.org/content/10.64898/2026.10.01.26364038v1)
  来源：medRxiv | 日期：2026-10-02 | 相关度：4.6 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Advances in high-throughput proteomics technologies have enabled the assessment of dynamic health states across biobank-scale cohorts. Disease prediction models built on these data have higher accuracy than baseline clin...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multimodal reasoning for broadly neutralizing antibody discovery from label-free human B cell repertoires across virus families](http://arxiv.org/abs/2610.03160v1)
  来源：arXiv | 日期：2026-10-02 | 相关度：3.75 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Discovering broadly neutralizing antibodies (bnAbs) from human natural immune repertoires remains a fundamental challenge in immunology, hindered by: the extreme rarity of bnAb, incomplete understanding of their cellular...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Transcriptome-informed multi-modal AI for predicting neoadjuvant therapy response from breast cancer biopsies](http://arxiv.org/abs/2610.03693v1)
  来源：arXiv | 日期：2026-10-02 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Scarcity of labeled data limits development of deep learning biomarkers in oncology. We develop a two-stage AI model predicting pathological complete response (pCR) to neoadjuvant therapy in breast cancer. The first stag...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。
