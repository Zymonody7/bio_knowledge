# 每日论文监控日报 (2026-08-31)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 15 篇新论文。

## 抓取状态

- arXiv：成功，命中 12 篇
- PubMed：成功，命中 18 篇
- bioRxiv：成功，命中 15 篇
- medRxiv：成功，命中 2 篇

## 最值得看

### Foundation Model / Agent

- [Vis-Poison: Poisoning Visual Knowledge in Multimodal Retrieval-Augmented Generation](http://arxiv.org/abs/2608.20756v2)
  来源：arXiv | 日期：2026-08-21 | 相关度：7.9 | 新颖度：6.2
  匹配主题：foundation_model_agent
  中文摘要：While multimodal retrieval-augmented generation (RAG) systems increasingly rely on images as external knowledge sources, the introduction of poisoned visual evidence can severely compromise multimodal large language mode...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [Comparing Chunking and Embedding Strategies for Turkish RAG Systems](http://arxiv.org/abs/2608.26192v2)
  来源：arXiv | 日期：2026-08-24 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation conditions a language model on chunks retrieved from a document collection. Its accuracy is therefore limited by the chunking and embedding stages that determine what can be retrieved. We c...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ProRetrieval: Learning to Orchestrate Hybrid Search via Executable Program Synthesis](http://arxiv.org/abs/2608.27017v2)
  来源：arXiv | 日期：2026-08-27 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Real-world retrieval often composes structured constraints with semantic intents over text and images through arbitrary Boolean logic. Existing hybrid pipelines such as reciprocal rank fusion or self-querying retrievers ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Vision-language encoding models reveal an image-computable food-quality dimension in human occipitotemporal cortex](https://www.biorxiv.org/content/10.64898/2026.08.25.747006v1)
  来源：bioRxiv | 日期：2026-08-28 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Perceived calorie content contributes to neural representational structure in human ventral visual cortex, yet it remains unclear whether this reflects an abstract nutritional signal or whether perceived calorie is large...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Coarse composition suffices: tabular in-context learning for multi-activity antimicrobial peptide profiling](https://www.biorxiv.org/content/10.64898/2026.08.27.747591v1)
  来源：bioRxiv | 日期：2026-08-28 | 相关度：4.7 | 新颖度：6.5
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Antimicrobial peptides (AMPs) often act against multiple pathogen classes, making multi-label activity prediction a more realistic screening target than binary antimicrobial classification. The ESCAPE benchmark formalize...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [CIViC-Fact: a proof-of-concept framework for AI-assisted verification of cancer variant interpretations](https://www.biorxiv.org/content/10.1101/2025.09.10.675443v3)
  来源：bioRxiv | 日期：2026-08-29 | 相关度：6.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Accurate interpretation of genomic variants is critical for precision oncology but remains slow and dependent on specialized expertise. Public knowledgebases such as the Clinical Interpretation of Variants in Cancer (CIV...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Reinforcement Learning Guides Generative Protein Language Models](http://arxiv.org/abs/2412.12979v4)
  来源：arXiv | 日期：2024-12-17 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Protein engineering can optimize molecules for biotechnology and therapeutics, but navigating the high-dimensional sequence landscape remains challenging. Protein language models (pLMs) have shown to to generate function...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 其他

- [CamoDocs: A Poisoning Attack Against Retrieval-Augmented Language Models Using Camouflaged Documents](http://arxiv.org/abs/2608.28389v1)
  来源：arXiv | 日期：2026-08-28 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) augments LLMs with external documents, but public or user-editable sources expose RAG systems to data poisoning: attackers can inject malicious documents to steer outputs toward targe...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [RIBOSPAN: A Long-Context RNA Foundation Model for Versatile RNA Modeling](http://arxiv.org/abs/2608.22849v2)
  来源：arXiv | 日期：2026-08-24 | 相关度：1.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Full-length RNAs, particularly messenger RNAs, often exceed the context lengths used to pretrain existing RNA foundation models, limiting complete-transcript modeling at single-nucleotide resolution. We present RIBOSPAN,...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [TRACE: A FINE-TUNED BIOMEDICAL LANGUAGE MODEL FOR DIRECTIONALLY INFORMED DRUG REPURPOSING FROM TRANSCRIPTOME-WIDE ASSOCIATION STUDIES](https://www.medrxiv.org/content/10.64898/2026.08.25.26361263v1)
  来源：medRxiv | 日期：2026-08-28 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Transcriptome-wide association studies (TWAS) can identify genes where genetically predicted gene expression is associated with disease risk, but translating those signals into therapeutic opportunities remains time-cons...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Anniemap: Vector Search for Viral Short Read Alignment](https://www.biorxiv.org/content/10.64898/2026.08.26.747390v1)
  来源：bioRxiv | 日期：2026-08-28 | 相关度：5.6 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Background: The process of aligning sequencing reads to a reference genome is a foundational step in genomic analysis, underpinning tasks from variant detection to pathogen surveillance. In viral genomics, however, this ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Data-centric feedback loops for next-generation immunotherapy development.](https://pubmed.ncbi.nlm.nih.gov/42665646/)
  来源：PubMed | 日期：2026-08-28 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Despite explosive growth in biomedical data generation, driven largely by genomics, and in computational capabilities, the probability that a candidate entering phase I ultimately reaches approval has remained stubbornly...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Digital twin-centered food safety management systems: A review of IoT, AI, and blockchain integration for bacterial pathogen control.](https://pubmed.ncbi.nlm.nih.gov/42215116/)
  来源：PubMed | 日期：2026-08-31 | 相关度：2.45 | 新颖度：8.09
  匹配主题：application_monitoring
  中文摘要：The digitalization of food safety management systems (FSMS) represents a crucial strategy for mitigating persistent pathogen contamination and foodborne disease outbreaks. The ISO 22000-based FSMS, incorporating hazard a...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A Wolf in Sheep's Clothing: Targeted Routing Hijacking in Federated RAG](http://arxiv.org/abs/2605.28112v2)
  来源：arXiv | 日期：2026-05-27 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Federated Retrieval-Augmented Generation (FedRAG) is attractive for privacy-sensitive applications because full local corpora remain on clients. As a result, routing must rely on client-provided semantic profiles, creati...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Regime-Aware Portfolio Management via Retrieval-Augmented LLM-Guided Expert Switching](http://arxiv.org/abs/2608.28252v1)
  来源：arXiv | 日期：2026-08-28 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Financial markets are inherently non-stationary, making the effectiveness of individual portfolio-management strategies highly dependent on changing market conditions. This work proposes a retrieval-augmented expert-swit...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。
