# 每日论文监控日报 (2026-11-16)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 20 篇新论文。

## 抓取状态

- arXiv：成功，命中 9 篇
- PubMed：成功，命中 30 篇
- bioRxiv：成功，命中 22 篇
- medRxiv：成功，命中 6 篇

## 最值得看

### Foundation Model / Agent

- [Development of an exploratory taxonomy of veterinary AI query types and stage-specific query preferences: an expert panel study](https://www.biorxiv.org/content/10.64898/2026.06.07.730654v2)
  来源：bioRxiv | 日期：2026-11-13 | 相关度：7.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Background/objectives: The integration of large language model (LLM)-based AI tools into veterinary clinical practice is rapidly increasing; however, veterinary-specific frameworks for organizing AI query types and exami...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [ModBERT: a DNA modification and genetic variant-aware DNA large language model](https://www.biorxiv.org/content/10.64898/2026.11.12.766258v1)
  来源：bioRxiv | 日期：2026-11-13 | 相关度：7.55 | 新颖度：7.5
  匹配主题：foundation_model_agent
  中文摘要：The development of foundation models that learn a general grammar of DNA (DNA language models) has accelerated in recent years. The vast majority of DNA large language models (LLMs), such as DNABERT-2 and Nucleotide Tran...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [MicroDUET: a dual-headed genomic foundation model for pathogen surveillance](https://www.biorxiv.org/content/10.64898/2026.11.11.765853v1)
  来源：bioRxiv | 日期：2026-11-13 | 相关度：8.75 | 新颖度：1.25
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：Pathogen genomic surveillance works from raw reads, assembled genomes and alignments, representations that are slow and costly to compare at scale. Compact embeddings from genomic language models offer an alternative, bu...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LUNA-FM: a subword foundation model for long non-coding RNAs for functional inference.](https://pubmed.ncbi.nlm.nih.gov/43023405/)
  来源：PubMed | 日期：2026-11-13 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：RNA foundation models (FMs) have shown promise for RNA identification and functional annotation. However, many use single-nucleotide tokenization, which produces long input sequences and can increase computational costs ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MeReader: An Offline, Privacy-Preserving, Progress-Aware AI Assistant for Narrative eBook Reading](http://arxiv.org/abs/2611.18513v1)
  来源：arXiv | 日期：2026-11-13 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：This paper introduces MeReader, a privacy-preserving, offline and progress-aware AI assistant designed to function as a contextual companion for narrative reading on consumer hardware. Unlike conventional Large Language ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Interpretable weight-space programming builds transparent transformers and brain encoding models](http://arxiv.org/abs/2611.18114v1)
  来源：arXiv | 日期：2026-11-13 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Neural networks are powerful predictors, yet their opacity limits their usefulness in science, where the goal is explanation rather than mere prediction. In neuroscience, for example, deep encoding models accurately pred...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [DynamicsPLM: A Dynamics-Enriched Small Protein Language Model for Protein Variant Effect Prediction](https://www.biorxiv.org/content/10.64898/2026.11.11.765945v1)
  来源：bioRxiv | 日期：2026-11-13 | 相关度：5.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Predicting how mutations impact protein function and stability remains a key challenge in computational biology. Current state-of-the-art protein language models (PLMs) primarily scale parameter size on sequence corpora ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [ViroGym: Realistic Large-Scale Benchmarks for Evaluating Viral Proteins](http://arxiv.org/abs/2603.06740v3)
  来源：arXiv | 日期：2026-03-06 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Protein language models (pLMs) have shown strong potential for zero-shot prediction of missense variant effects, yet systematic benchmarking on viral proteins remains limited, a critical gap given the need for proactive ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [SeekRBP: Leveraging Sequence-Structure Integration with Reinforcement Learning for Receptor-Binding Protein Identification](http://arxiv.org/abs/2603.04748v4)
  来源：arXiv | 日期：2026-03-05 | 相关度：7.1 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Motivation: Receptor-binding proteins (RBPs) initiate viral infection and determine host specificity, serving as key targets for phage engineering and therapy. However, the identification of RBPs is complicated by their ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Binary Patterning as a Probe of Protein Language Model Representations](https://www.biorxiv.org/content/10.64898/2026.11.11.765943v1)
  来源：bioRxiv | 日期：2026-11-13 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Do protein language models (pLMs) encode the physical rules that govern protein folding? The four-helix bundle provides a classic test case because binary patterning, the ordered placement of polar and nonpolar residues ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [Enrollees and Early Lessons from an Agentic Healthcare Platform with Physicians in the Loop](https://www.medrxiv.org/content/10.64898/2026.11.12.26367291v1)
  来源：medRxiv | 日期：2026-11-13 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Agentic healthcare platforms that combine large language models with physician oversight are growing quickly, but little is known about who uses them. We characterized 3,223 enrollees of Lotus AI, a free, physician-super...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [BenchmarkHub: an open-source platform for reproducible evaluation of large language models in healthcare](https://www.medrxiv.org/content/10.64898/2026.11.11.26367866v1)
  来源：medRxiv | 日期：2026-11-13 | 相关度：6.1 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Background: Large language models (LLMs) are solely judged by their scores on biomedical benchmarks, yet these scores are rarely reproducible since the prompts, inference settings and model builds are seldom reported. We...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Learning inhibitor interactions from protein deep mutational scanning data and deep learning models](https://www.biorxiv.org/content/10.64898/2026.11.01.763444v2)
  来源：bioRxiv | 日期：2026-11-13 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in protein language models, geometric deep learning, and structure prediction frameworks have the potential to accelerate computational drug discovery. However, it remains unclear how well these methods g...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [AI-Driven Reconstruction of Online Health Narratives Using Agent-Action-Outcome Modeling: Algorithm Development and Validation.](https://pubmed.ncbi.nlm.nih.gov/43024829/)
  来源：PubMed | 日期：2026-11-13 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：People share health experiences online as stories, not isolated facts. Most computational systems reduce these narratives to keywords or claims, overlooking the agency, causality, and interpretation that determine whethe...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Systematic Benchmarking and Optimization of Retrieval-Augmented Generation (RAG) for Clinical Phenotyping: A Type II Diabetes Case Study in an ICD-Screened Cohort](https://www.medrxiv.org/content/10.1101/2025.04.29.25326696v5)
  来源：medRxiv | 日期：2026-11-14 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Traditional EHR phenotyping methods can require substantial disease-specific development and long-term maintenance. While integrating large language models (LLMs) with Retrieval-Augmented Generation (RAG) is promising, t...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Large language models complement established workflows for mechanistic model construction and refinement in systems biology](https://www.biorxiv.org/content/10.64898/2026.11.11.766014v1)
  来源：bioRxiv | 日期：2026-11-13 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Mechanistic models provide a framework for describing, understanding, and predicting biological processes, but their development requires an interdisciplinary team with expertise in biology, mathematics, and computation....
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Toward precision nanomedicine via artificial intelligence guided design and prediction.](https://pubmed.ncbi.nlm.nih.gov/43025814/)
  来源：PubMed | 日期：2026-11-13 | 相关度：3.75 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence (AI) is advancing nanomedicine development by linking formulation variables and biological context with delivery, therapeutic efficacy, and safety. This review examines AI assisted formulation des...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Kymograph classifiers predict CMT2A disease-relevant mitochondrial motility phenotypes in iPSC motor neurons](https://www.biorxiv.org/content/10.64898/2026.03.16.712192v2)
  来源：bioRxiv | 日期：2026-11-14 | 相关度：2.65 | 新颖度：5.75
  匹配主题：sequencing_bioinformatics
  中文摘要：Charcot-Marie-Tooth disease type 2A (CMT2A) is a genetic disease characterized by autosomal dominant MFN2 mutations and dysregulated mitochondrial trafficking. While there is currently no FDA-approved CMT2A therapy, the ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [The Therapeutic Pipeline: Future Treatments and Precision Medicine.](https://pubmed.ncbi.nlm.nih.gov/43025460/)
  来源：PubMed | 日期：2026-11-13 | 相关度：3.7 | 新颖度：0.25
  匹配主题：pathogenomics
  中文摘要：rare interstitial lung diseases (ILDs) represent a heterogeneous group of disorders characterized by various pathogenic mechanisms, clinical presentations, prognoses, and therapeutic challenges. Among these, acid sphingo...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Self-Building Labs](http://arxiv.org/abs/2610.23826v3)
  来源：arXiv | 日期：2026-10-16 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Self-driving laboratories (SDLs) accelerate scientific discovery by automating experimental execution and optimization. AI agents can increasingly propose new experiments, but existing SDLs can only run the procedures th...
  为什么值得看：Self-Building Labs 与你的主题有弱匹配，暂时保留作低优先级跟踪。
