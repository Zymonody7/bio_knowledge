# 每日论文监控日报 (2026-11-23)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 16 篇新论文。

## 抓取状态

- arXiv：成功，命中 10 篇
- PubMed：成功，命中 27 篇
- bioRxiv：失败，命中 0 篇，错误：('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
- medRxiv：成功，命中 5 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [GenNA: Conditional generation of nucleotide sequences guided by natural language annotations.](https://pubmed.ncbi.nlm.nih.gov/43050525/)
  来源：PubMed | 日期：2026-11-20 | 相关度：8.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Deciphering the mapping between biomolecular sequences and complex biological functions is a central challenge in genomics. While existing generative nucleotide models capture sequence distributions, they lack explicit a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A report-supervised EEG-language foundation model enables broad, interactive clinical interpretation](https://www.medrxiv.org/content/10.64898/2026.11.18.26368408v1)
  来源：medRxiv | 日期：2026-11-20 | 相关度：7.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Medical AI for complex signals such as electroencephalography (EEG) relies on costly expert annotations and predefined diagnostic labels that fail to capture the richness and nuance of clinical interpretation. Whether mo...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HealthFound: a health world model for quantitative reasoning on longitudinal health profiles](https://www.medrxiv.org/content/10.64898/2026.10.03.26364142v2)
  来源：medRxiv | 日期：2026-11-22 | 相关度：7.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Medical large language models have shown promise in medical knowledge retrieval and clinical reasoning but remain limited in quantitative reasoning over longitudinal health data, partly due to the lack of effective data ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Auditable Financial Knowledge Graphs: Schema-Driven Construction and Intrinsic Quality Evaluation](http://arxiv.org/abs/2611.27835v1)
  来源：arXiv | 日期：2026-11-20 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Financial documents combine narrative disclosures, accounting metrics, corporate structures, management commentary, and time-dependent facts, making them difficult to represent using conventional chunk-based retrieval-au...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [ChildAI-Gov: An Evidence-Linked AI System for Assessing EdTech Policies Against Children's Digital Rights](http://arxiv.org/abs/2611.27799v1)
  来源：arXiv | 日期：2026-11-20 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：We present ChildAI-Gov, an explainable AI system for assessing whether education-technology (EdTech) policies respect children's digital rights. Generative AI is reaching children's education faster than its governance c...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Detecting Word-Substitution Poisoning of a RAG Knowledge Base with Relative Entropy and Runtime Verification](http://arxiv.org/abs/2611.27410v1)
  来源：arXiv | 日期：2026-11-20 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：A retrieval-augmented generation (RAG) system answers questions using passages it retrieves from a knowledge base, so users must trust that knowledge base. We study an attacker who quietly edits existing passages by swap...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [A Hybrid Large Language Model and Diffusion Framework for Rational Promoter Design.](https://pubmed.ncbi.nlm.nih.gov/43061963/)
  来源：PubMed | 日期：2026-11-20 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：High-performance promoters are essential tools for precisely regulating gene expression, yet their rational design within the vast combinatorial sequence space remains a major challenge. Here, we present a hybrid framewo...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Language as the Interface: Foundation-Model Contrastive Learning Links Transcriptomes and Electrophysiology](http://arxiv.org/abs/2609.37024v2)
  来源：arXiv | 日期：2026-09-29 | 相关度：7.1 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Integrating transcriptomic and electrophysiological data is essential for building multimodal foundation models for neuroscience. Patch-seq provides paired measurements of gene expression and intrinsic electrophysiology ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [When Visually Rich Documents Meet Multi-Vector Retrieval for Region-level Retrieval-Augmented Generation](http://arxiv.org/abs/2611.27542v1)
  来源：arXiv | 日期：2026-11-20 | 相关度：2.1 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Visually rich documents (VRDs) convey knowledge through textual, visual, and layout information that text-centric Retrieval-Augmented Generation (Text-RAG) struggles to fully exploit. Recent Vision-RAG approaches enable ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [GAAMA: Graph Augmented Associative Memory for Agents](http://arxiv.org/abs/2603.27910v4)
  来源：arXiv | 日期：2026-03-29 | 相关度：2.1 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：AI agents that talk with users across many sessions need long-term memory to stay coherent and personalized. Existing approaches use either flat retrieval-augmented generation (RAG) that ignores how memories connect, or ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [FusionGDB 3.0: integrating breakpoints, generating personalized sequences, and inferring tumorigenic scenarios for human fusion genes.](https://pubmed.ncbi.nlm.nih.gov/43059400/)
  来源：PubMed | 日期：2026-11-20 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：FusionGDB has served diverse biological, health, and clinical research communities as a unique functional annotation knowledgebase of human fusion genes. In this study, we report an updated resource of human fusion gene ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Poisoning Attacks and Collaborative Defense Framework for LightRAG-Based Construction Regulation Knowledge](http://arxiv.org/abs/2611.27460v1)
  来源：arXiv | 日期：2026-11-20 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) is widely used in construction, yet the security of building-regulation knowledge bases has received little study. This thesis reports a pre-registered experiment on one fully instrum...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [CogRec: Structure-Cognitive Fast-and-Slow Reasoning for Generative Recommendation](http://arxiv.org/abs/2607.24402v3)
  来源：arXiv | 日期：2026-07-27 | 相关度：2.05 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Generative recommendation reformulates next-item prediction as identifier sequence generation, yet existing methods mainly treat the generated identifiers as target sequences to be memorized, leaving their hierarchical a...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Do Alice and Bob Dream of the Oracle? Wishful Cryptanalysis](http://arxiv.org/abs/2611.27729v1)
  来源：arXiv | 日期：2026-11-20 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：For two millennia, offense and defense have forged cryptographic security boundaries. Tools automated calculation and search, while humans drove discovery. Foundation models now mark a shift from automated computation to...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Artificial Intelligence in Screening and Early Detection of Prostate Cancer.](https://pubmed.ncbi.nlm.nih.gov/43064602/)
  来源：PubMed | 日期：2026-11-20 | 相关度：3.75 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence (AI) is transforming prostate cancer screening and early detection through the integration of clinical-risk calculators, magnetic resonance imaging (MRI), digital pathology, genomics, biomarkers, ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [From Technical Performance to Clinical Impact: Challenges and Opportunities for AI Modelling of CKD Progression.](https://pubmed.ncbi.nlm.nih.gov/43066646/)
  来源：PubMed | 日期：2026-11-21 | 相关度：3.75 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Chronic kidney disease (CKD) is a major global health burden, with highly heterogeneous trajectories ranging from long-term stability to rapid progression towards kidney failure and kidney replacement therapy. Accurate p...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
