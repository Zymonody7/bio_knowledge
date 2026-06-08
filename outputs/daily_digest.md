# 每日论文监控日报 (2026-06-08)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 24 篇新论文。

## 抓取状态

- arXiv：成功，命中 11 篇
- PubMed：成功，命中 28 篇
- bioRxiv：成功，命中 13 篇
- medRxiv：成功，命中 11 篇

## 最值得看

### Foundation Model / Agent

- [Caption Injection for Optimization in Generative Search Engine](http://arxiv.org/abs/2511.04080v3)
  来源：arXiv | 日期：2025-11-06 | 相关度：7.9 | 新颖度：6.7
  匹配主题：foundation_model_agent
  中文摘要：Generative Search Engine (GSE) leverages the Retrieval-Augmented Generation (RAG) technique and the Large Language Model (LLM) to integrate multi-source information and provide users with accurate and comprehensive respo...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MCERF: Advancing Multimodal LLM Evaluation of Engineering Documentation with Enhanced Retrieval](http://arxiv.org/abs/2604.09552v2)
  来源：arXiv | 日期：2026-01-31 | 相关度：7.9 | 新颖度：6.7
  匹配主题：foundation_model_agent
  中文摘要：Engineering rulebooks and technical standards contain multimodal information like dense text, tables, and illustrations that are challenging for retrieval augmented generation (RAG) systems. Building upon the DesignQA fr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [Clinician-Centered Evaluation of Large Language Model-Generated Discharge Summaries for Longer Hospitalizations: Insights from Hospitalists and Primary Care Physicians](https://www.medrxiv.org/content/10.64898/2026.06.03.26354858v1)
  来源：medRxiv | 日期：2026-06-05 | 相关度：7.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Although large language models (LLMs) have shown promise for discharge summary generation, their value may be greater in longer hospitalizations, where increasing documentation volume and complexity increase both clinici...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [QUARE: Quality-Aware Requirements Analysis through Multi-Agent Dialectical Negotiation](http://arxiv.org/abs/2603.11890v2)
  来源：arXiv | 日期：2026-03-12 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Automating requirements quality analysis remains challenging because multiple, often conflicting quality attributes must be balanced while preserving stakeholder intent. Existing Large-Language-Model (LLM) approaches pre...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RAVEN: Retrieval-Augmented Vulnerability Exploration Network for Memory Corruption Analysis in User Code and Binary Programs](http://arxiv.org/abs/2604.17948v2)
  来源：arXiv | 日期：2026-04-20 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have demonstrated remarkable capabilities across various cybersecurity tasks, including vulnerability classification, detection, and patching. However, their potential in automated vulnerabil...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SEEK: Steering LLM Reasoning for RAG via Internal Reasoning Sketches](http://arxiv.org/abs/2601.09402v2)
  来源：arXiv | 日期：2026-01-14 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) enhances Large Language Models (LLMs) by incorporating external knowledge into the generation process. Benefiting from the reasoning capabilities of LLMs, existing methods have levera...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Protein large language model assisted one-to-one gene homology mapping in cross-species single-cell transcriptome integration](https://www.biorxiv.org/content/10.1101/2025.10.17.683009v2)
  来源：bioRxiv | 日期：2026-06-05 | 相关度：6.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Cross-species integration of single-cell transcriptomes requires establishing gene correspondences to enable comparative analysis of expression profiles across organisms. Current approaches predominantly rely on Ensembl ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [pLM-Guided Inverse Folding for Antibody Sequence Design](https://www.biorxiv.org/content/10.64898/2026.06.04.730089v1)
  来源：bioRxiv | 日期：2026-06-06 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Inverse folding, predicting amino acid sequences from three-dimensional structures, is a foundational task in computational protein design, yet it is hindered by the scarcity of structural data, which limits model traini...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Using protein language models for pangenome construction](https://www.biorxiv.org/content/10.64898/2026.06.04.730042v1)
  来源：bioRxiv | 日期：2026-06-06 | 相关度：5.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Current pangenome construction methods rely largely on nucleotide or protein sequence alignment, limiting their ability to detect remote orthologs and semantic relations. We introduce a novel method that leverages protei...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Chromap Suite: an open-source single-binary platform for agentic multiomic RNA + ATAC profiling](https://www.biorxiv.org/content/10.64898/2026.06.02.729736v1)
  来源：bioRxiv | 日期：2026-06-06 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Background. Single-cell multiomic profiling of RNA expression and chromatin accessibility is now a standard tool for resolving regulatory state in single cells, but existing analysis toolchains have lagged. Cell Ranger A...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Quantifying Cancer Clinical Trial Eligibility Using Artificial Intelligence-Based Matching](https://www.medrxiv.org/content/10.64898/2026.06.03.26354859v1)
  来源：medRxiv | 日期：2026-06-05 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：PURPOSE: To develop and validate an artificial intelligence-enabled platform that converts unstructured cancer trial eligibility criteria into structured queries and quantifies trial eligibility across advanced/metastati...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Autonomous computational catalysis through an agentic research system](http://arxiv.org/abs/2601.13508v4)
  来源：arXiv | 日期：2026-01-20 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Autonomous agents are beginning to transform scientific research from tool-assisted workflows toward self-sustaining discovery processes. Computational catalysis provides a representative challenge, as catalyst discovery...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Surfacing Suicidal Risk Through Simulated Social Interaction: Per-Person Language Model Agents as Communicative Stress Tests](https://www.medrxiv.org/content/10.64898/2026.06.04.26354928v1)
  来源：medRxiv | 日期：2026-06-06 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Suicidal risk may be encoded in everyday communication patterns but diluted in routine digital interactions. We introduce a method for surfacing this latent signal: training per-person language model agents on individual...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond Injection Detection: A Positive-Security Prompt Firewall that Closes the Scope and PHI Gap SOTA Classifiers Miss in Healthcare](https://www.medrxiv.org/content/10.64898/2026.06.04.26354950v1)
  来源：medRxiv | 日期：2026-06-06 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models embedded in autonomous agents process trusted instructions and untrusted data in one context window, leaving them open to direct and indirect prompt injection. In healthcare this is not hypothetical...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A layer-resolved diagnostic identifies bias-driven decisions in deep neural networks](https://www.biorxiv.org/content/10.1101/2025.09.16.676625v6)
  来源：bioRxiv | 日期：2026-06-06 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Deep neural networks can remain highly confident even when the input provides limited support. However, existing approaches such as calibration and feature attribution provide complementary information about error likeli...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DentaCoPilot: An LLM-Augmented Next-Procedure Recommender for General Dentistry, Designed for Dentist Augmentation](https://www.medrxiv.org/content/10.64898/2026.05.07.26352635v2)
  来源：medRxiv | 日期：2026-06-07 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：BackgroundCommercial dental artificial intelligence in 2026 is over-whelmingly diagnostic: caries, calculus, periapical, and bone-level detection on radiographs. The clinically harder question that follows every diagno-s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SSRLive: Live Streaming Recommendation with Dynamic Semantic ID](http://arxiv.org/abs/2606.06970v1)
  来源：arXiv | 日期：2026-06-05 | 相关度：2.75 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Live streaming has emerged as one of the fastest-growing forms of online media, enabling instant content broadcasting and real-time engagement between users and streamers. Despite the effectiveness of existing recommenda...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Optimizing genomics-aware clinical agents in precision oncology.](https://pubmed.ncbi.nlm.nih.gov/42248877/)
  来源：PubMed | 日期：2026-06-05 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Agentic systems are proposed for clinical decision support, yet unrestricted tool access can undermine accountability and safety in precision oncology, where recommendations must be grounded in evolving guidelines, regul...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Constrained Dominant Sets for Multimodal Document Question Answering](http://arxiv.org/abs/2606.07252v1)
  来源：arXiv | 日期：2026-06-05 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Long multimodal document question answering is limited by which evidence reaches the reader, rather than by the quantity retrieved. In lengthy documents, findings often recur across figures, captions, and introductory se...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Performance evaluation and benchmarking across 16 large language models on a comprehensive real-world emergency department triage data set](https://www.medrxiv.org/content/10.64898/2026.05.28.26353935v1)
  来源：medRxiv | 日期：2026-06-05 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Background Emergency department (ED) triage is a high-stakes clinical decision process that determines patient prioritization and resource allocation under time pressure. Large language models (LLMs) have recently been p...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Didact: A Cross-Domain Capability Discovery System for Defence](http://arxiv.org/abs/2606.06942v1)
  来源：arXiv | 日期：2026-06-05 | 相关度：2.05 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Policymakers in defence and defence-aligned sectors must monitor rapidly evolving research alongside sector priorities relevant to operational and strategic needs. In practice, these sources are fragmented across heterog...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Compositional and interpretable representation of histology using AI foundation models and sparse autoencoders](https://www.biorxiv.org/content/10.64898/2026.06.03.725182v1)
  来源：bioRxiv | 日期：2026-06-06 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Light microscopy of tissue sections stained with hematoxylin and eosin (H&E) has been the foundation of histopathology for over 150 years and remains essential for diagnosis and research. The development of high-plex spa...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Biotherapeutic strategies for quorum quenching in Salmonella Typhi: a review.](https://pubmed.ncbi.nlm.nih.gov/42250148/)
  来源：PubMed | 日期：2026-06-06 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Quorum sensing (QS) in Salmonella enterica serovar Typhi (S. Typhi) is a cell-cell communication process mediated by molecules like Autoinducer-2 (AI-2). The production and detection of these molecules are population den...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Bootstrap Theory of Representational Emergence: Explanatory Insufficiency as a Driver of Representation Learning and World Models](http://arxiv.org/abs/2606.07303v1)
  来源：arXiv | 日期：2026-06-05 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Representation learning is central to modern machine learning, enabling transitions from handcrafted features to learned embeddings, latent spaces, foundation models, world models, and digital twins. Yet most research ex...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。
