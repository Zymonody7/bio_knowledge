# 每日论文监控日报 (2026-06-02)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 64 篇新论文。

## 抓取状态

- arXiv：成功，命中 46 篇
- PubMed：成功，命中 180 篇
- bioRxiv：成功，命中 23 篇
- medRxiv：成功，命中 12 篇

## 最值得看

### Foundation Model / Agent

- [Multi-Agent AI for Chest Radiography: A Sequential Segmentation and LLM-Driven Consultative Tool for Medical Training](https://www.medrxiv.org/content/10.64898/2026.05.29.26354432v1)
  来源：medRxiv | 日期：2026-06-01 | 相关度：8.9 | 新颖度：6.2
  匹配主题：foundation_model_agent
  中文摘要：Background: Traditional diagnostic models lack explainability, while multimodal language models prone to hallucination remain unsafe for medical education. An interactive, risk-free artificial intelligence framework is r...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TrafficRAG: A Multimodal RAG Framework for Traffic Accident Liability Determination](http://arxiv.org/abs/2606.01737v1)
  来源：arXiv | 日期：2026-06-01 | 相关度：7.9 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Traffic accident liability analysis is a critical yet challenging task in intelligent transportation and legal assistance. Existing methods often suffer from low efficiency, subjective judgment, and inconsistent analysis...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [PRIME: An evaluation framework for protein representation inference and generalization in viral mutation space.](https://pubmed.ncbi.nlm.nih.gov/42215857/)
  来源：PubMed | 日期：2026-05-30 | 相关度：10.0 | 新颖度：1.75
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Protein language models (PLMs) have revolutionized protein fitness prediction, yet their application to rapidly evolving viral pathogens is often confounded by extreme sequence homology. This homology leads to "data leak...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Predicting host-pathogen interactions using a proteome-scale language model](https://www.biorxiv.org/content/10.64898/2026.05.29.728699v1)
  来源：bioRxiv | 日期：2026-05-31 | 相关度：8.4 | 新颖度：6.0
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：ProteomeLM is a proteome-scale language model trained on proteomes spanning the tree of life to reconstruct masked protein embeddings from proteome context within each species. Its attention coefficients capture protein-...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

## 可追踪

### Foundation Model / Agent

- [Agent Role Structure and Operating Characteristics in Large Language Model Clinical Classification: A Comparative Study of Specialist and Deliberative Multi-Agent Protocols](https://www.medrxiv.org/content/10.64898/2026.02.22.26346818v4)
  来源：medRxiv | 日期：2026-05-31 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly considered in clinical decision support, yet the architectural effects of role decomposition within multi-agent systems remain poorly isolated. Prior comparisons of single-ag...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Towards A Foundation Model for Clinical Voice Biomarkers](https://www.medrxiv.org/content/10.64898/2026.05.28.26354346v1)
  来源：medRxiv | 日期：2026-05-30 | 相关度：7.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Vocal biomarkers, encompassing voice and speech, have largely been developed for individual conditions in isolation, limiting their generalizability across diseases and recording settings. To address this, we introduce V...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SeGA-GNN: Semantically Gated Augmented Graph Neural Networks for Wearable-Based Emotion Detection](https://www.medrxiv.org/content/10.64898/2026.05.29.26354434v1)
  来源：medRxiv | 日期：2026-06-01 | 相关度：6.8 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Background: Wearable technologies enable scalable and continuous monitoring of emotional states through passive sensing of physiological and behavioral signals. However, conventional learning approaches often struggle to...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Med.ai ASK: an agentic system for biomedical question answering.](https://pubmed.ncbi.nlm.nih.gov/41911379/)
  来源：PubMed | 日期：2026-06-01 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Intelligent agent-driven research co-pilots, leveraging advances in generative AI, are transforming how scientists access biomedical knowledge. This paper presents Med.ai ASK, an agentic question-answering system designe...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [UniD$^3$: A Knowledge Graph-Enhanced RAG Framework for Drug-Disease Discovery and Reasoning](http://arxiv.org/abs/2606.01394v1)
  来源：arXiv | 日期：2026-05-31 | 相关度：6.15 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Systematic characterization of drug-disease relationships is essential for drug discovery and repurposing, yet is hindered by the heterogeneity and rapid growth of biomedical literature. Existing datasets rely on labor-i...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Principle-Evolvable Scientific Discovery via Uncertainty Minimization](http://arxiv.org/abs/2602.06448v2)
  来源：arXiv | 日期：2026-02-06 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Model (LLM)-based scientific agents have accelerated scientific discovery, yet they often suffer from significant inefficiencies due to adherence to fixed initial priors. Existing approaches predominantly ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Self-Healing Agentic Orchestrators for Reliable Tool-Augmented Large Language Model Systems](http://arxiv.org/abs/2606.01416v1)
  来源：arXiv | 日期：2026-05-31 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Tool-augmented large language model (LLM) agents rely on orchestration layers that coordinate planning, retrieval, tool invocation, validation, memory, and recovery. In these systems, failures arise not only from model e...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Language-Native Materials Processing Design by Lightly Structured Text Database and Reasoning Large Language Model](http://arxiv.org/abs/2509.06093v4)
  来源：arXiv | 日期：2025-09-07 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Materials synthesis procedures are predominantly documented as narrative text in papers, protocols, and laboratory records, placing them beyond the reach of conventional data-driven optimization frameworks. This language...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Algorithmic Versus Expert Rankings of Large Language Models in Peritoneal Dialysis Prescription Review: A Trap-Embedded Synthetic Benchmark](https://www.medrxiv.org/content/10.64898/2026.05.28.26354383v1)
  来源：medRxiv | 日期：2026-06-01 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Background: Clinical LLM benchmarks rarely test whether algorithmic rankings agree with expert clinical judgment. We developed a trap-embedded peritoneal dialysis (PD) benchmark comparing multiple scoring constructs with...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Plausibility Is Not Prediction: Contrastive Evidence for LLM-Based Cellular Perturbation Reasoning](http://arxiv.org/abs/2606.01042v1)
  来源：arXiv | 日期：2026-05-31 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Perturbation experiments are central to understanding cellular mechanisms, but remain costly and sparse, motivating prediction of gene expression responses for unobserved conditions. A promising recent direction leverage...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CacheRAG: A Semantic Caching System for Retrieval-Augmented Generation in Knowledge Graph Question Answering](http://arxiv.org/abs/2604.26176v2)
  来源：arXiv | 日期：2026-04-28 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：The integration of Large Language Models (LLMs) with Retrieval-Augmented Generation (RAG) has significantly advanced Knowledge Graph Question Answering (KGQA). However, existing LLM-driven KGQA systems act as stateless p...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EvoPool: Evolutionary Programmatic Annotation for Label-Efficient Specialized Supervision](http://arxiv.org/abs/2606.01617v1)
  来源：arXiv | 日期：2026-06-01 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Large language models excel at general tasks but underperform smaller supervised models in specialized, high-stakes domains where training labels are costly. We address this regime with EvoPool, an evolutionary multi-age...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SHERLOCK: Towards Dynamic Knowledge Adaptation in LLM-enhanced E-commerce Risk Management](http://arxiv.org/abs/2510.08948v4)
  来源：arXiv | 日期：2025-10-10 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Effective e-commerce risk management requires in-depth case investigations to identify emerging fraud patterns in highly adversarial environments. However, manual investigation typically requires analyzing the associatio...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Reproducible and shareable bioinformatics pipelines from natural-language prompts](https://www.biorxiv.org/content/10.64898/2026.05.28.719125v1)
  来源：bioRxiv | 日期：2026-06-01 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly used to generate bioinformatics pipelines and to carry out analyses from natural-language prompts. However, the resulting analyses are often difficult to reproduce across ses...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Lighting the Way for BRIGHT: Reproducible Baselines with Anserini, Pyserini, and RankLLM](http://arxiv.org/abs/2509.02558v2)
  来源：arXiv | 日期：2025-09-02 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval benchmarks for large language models (LLMs) should reflect the long, reasoning-intensive queries typical of retrieval-augmented generation (RAG). We present a systematic study of BRIGHT, a reasoning-focused ret...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Beyond Static Dialogues: Benchmarking Realistic, Heterogeneous, and Evolving Long-Term Memory](http://arxiv.org/abs/2605.31086v2)
  来源：arXiv | 日期：2026-05-29 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：In existing memory benchmarks for Large Language Models (LLMs), the evaluated dialogue sessions often lack long-term semantic consistency, and the underlying personas tend to be flat and static. Furthermore, in real-worl...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [RAG-driven Multi-Agent LLM Framework with Task Decomposition for Beyond 5G Auto-Configuration](http://arxiv.org/abs/2606.01222v1)
  来源：arXiv | 日期：2026-05-31 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：While Large Language Models (LLMs) offer a promising path toward intent-driven network management by translating natural language human intents into machine-readable configurations, they often suffer from hallucinations ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ES-Merging: Biological MLLM Merging via Embedding Space Signals](http://arxiv.org/abs/2603.14405v2)
  来源：arXiv | 日期：2026-03-15 | 相关度：6.1 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Biological multimodal large language models (MLLMs) have emerged as powerful foundation models for scientific discovery. However, existing models are specialized to a single modality, limiting their ability to solve inhe...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Comparison of AI protein structure ensemble prediction tools](https://www.biorxiv.org/content/10.64898/2026.05.29.728804v1)
  来源：bioRxiv | 日期：2026-05-30 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Multiple AI prediction tools for protein structural ensembles have recently been released, building on the much heralded advances from AlphaFold, large language models, and other machine-learning approaches. Here we repo...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Self-Revising Discovery Systems for Science: A Categorical Framework for Agentic Artificial Intelligence](http://arxiv.org/abs/2606.01444v1)
  来源：arXiv | 日期：2026-05-31 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Scientific discovery is not only answer generation but revision of the representational regime in which evidence, artifacts, operations, and verifiers are typed. We develop a category-theoretic account of agentic discove...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Efficient RAG with Intent-Aware Retrieval and Semantics-Preserving Chunking](http://arxiv.org/abs/2606.01240v1)
  来源：arXiv | 日期：2026-05-31 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：The demand for powerful instruction following and reasoning capability of large language models (LLMs) has promoted rapid development of retrieval-augmented generation (RAG). The RAG system assists LLM generation by retr...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Understanding LoRA as Knowledge Memory: An Empirical Analysis](http://arxiv.org/abs/2603.01097v3)
  来源：arXiv | 日期：2026-03-01 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Continuous knowledge updating for pre-trained large language models (LLMs) is increasingly necessary yet remains challenging. Although inference-time methods like In-Context Learning (ICL) and Retrieval-Augmented Generat...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Advances and challenges in the application of metagenomic sequencing for the diagnosis and treatment of infectious diseases: from pathogen spectrum identification to personalized antimicrobial strategies.](https://pubmed.ncbi.nlm.nih.gov/41764831/)
  来源：PubMed | 日期：2026-06-01 | 相关度：7.25 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：Infectious diseases remain a major global public health concern, demanding rapid and accurate identification of pathogens. Although conventional diagnostic methods such as culture, PCR, and immunological assays are widel...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Relationship Extraction for Adverse Drug Events in Clinical Notes Using Large Language Models](https://www.medrxiv.org/content/10.64898/2026.05.28.26354362v1)
  来源：medRxiv | 日期：2026-06-01 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Background: Adverse drug events (ADEs) are a critical indicator of patient safety but are often documented only in free-text clinical notes. The potential of recent advances in natural language processing (NLP), particul...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [A Foundation Model for the Cancer Genome](https://www.biorxiv.org/content/10.64898/2026.05.27.728319v1)
  来源：bioRxiv | 日期：2026-06-01 | 相关度：4.35 | 新颖度：5.75
  匹配主题：sequencing_bioinformatics, application_monitoring
  中文摘要：Cancer is a disease of the genome, in which somatic mutations and copy-number alterations determine tumour identity, clinical behaviour, and response to therapy. Consortium-scale sequencing has profiled hundreds of thous...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [REBot: From RAG to CatRAG with Semantic Enrichment and Graph Routing](http://arxiv.org/abs/2510.01800v3)
  来源：arXiv | 日期：2025-10-02 | 相关度：2.1 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Academic regulation advising is essential for helping students interpret and comply with institutional policies, yet building effective systems requires domain specific regulatory resources. To address this challenge, we...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond AI as Assistants: Toward Autonomous Discovery in Cosmology](http://arxiv.org/abs/2605.14791v2)
  来源：arXiv | 日期：2026-05-14 | 相关度：2.1 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Recent advances in artificial intelligence (AI) agents are pushing AI beyond tools toward autonomous scientific discovery. We discuss two complementary agentic systems for cosmology: \texttt{CMBEvolve}, which targets tas...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MemoNoveltyAgent: A Historical Research Memory-Aware Agent Workflow for Paper Novelty Assessment](http://arxiv.org/abs/2603.20884v2)
  来源：arXiv | 日期：2026-03-21 | 相关度：2.1 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：To alleviate the heavy burden of paper screening, researchers increasingly rely on existing AI agents, such as AI reviewers or DeepResearch, for paper evaluation and novelty assessment. However, lacking specialized mecha...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SpatialDataAgent: Autonomous Spatial Omics Data Curation at Decade Scale](https://www.biorxiv.org/content/10.64898/2026.05.27.727615v1)
  来源：bioRxiv | 日期：2026-05-30 | 相关度：1.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Fragmented metadata in spatial omics archives has rendered large volumes of multimodal molecular-histological data inaccessible as 'dark data'. Here, we introduce SpatialDataAgent, an agentic workflow for autonomous spat...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Science Earth: Towards A Planet-Scale Operating System for AI-Native Scientific Discovery](http://arxiv.org/abs/2606.01316v1)
  来源：arXiv | 日期：2026-05-31 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Scientific discovery demands intelligence, perseverance, and serendipity across vast search spaces. Today, top scientific capabilities remain siloed--one AI system for biological analysis, another for clinical reasoning,...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [When Knowledge Is Not Free: Cost-Aware Evidence Selection in Retrieval-Augmented Generation](http://arxiv.org/abs/2606.02245v1)
  来源：arXiv | 日期：2026-06-01 | 相关度：1.4 | 新颖度：7.28
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) typically assumes that external knowledge is free, but many high-quality sources are paywalled, licensed, restricted, or otherwise costly to access. We introduce cost-aware RAG, a set...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RA-LWLM: Retrieval-Augmented In-Context Localization with Wireless Foundation Models](http://arxiv.org/abs/2606.01899v1)
  来源：arXiv | 日期：2026-06-01 | 相关度：1.4 | 新颖度：6.44
  匹配主题：未命中具体主题
  中文摘要：Wireless localization is a fundamental capability of sixth-generation (6G) networks. Conventional model-based methods require accurate modeling of the propagation environment and degrade in complex multipath and non-line...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SparseX: Efficient Segment-Level KV Cache Sharing for Interleaved LLM Serving](http://arxiv.org/abs/2606.01751v1)
  来源：arXiv | 日期：2026-06-01 | 相关度：1.4 | 新颖度：5.54
  匹配主题：未命中具体主题
  中文摘要：In long-context LLM serving, the prefill stage often dominates time-to-first-token and computational cost. Although Prefix Cache in vLLM/PagedAttention has been widely used to reuse identical prompt prefixes, repeated co...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CVEvolve: Autonomous Algorithm Discovery for Unstructured Scientific Data Processing](http://arxiv.org/abs/2605.11359v3)
  来源：arXiv | 日期：2026-05-12 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Scientific data processing often requires task-specific algorithms or AI models, creating a barrier for domain scientists who need to analyze their data but may not have extensive computing or image-processing expertise....
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SIRI: Self-Internalizing Reinforcement Learning with Intrinsic Skills for LLM Agent Training](http://arxiv.org/abs/2606.02355v1)
  来源：arXiv | 日期：2026-06-01 | 相关度：0.7 | 新颖度：6.76
  匹配主题：未命中具体主题
  中文摘要：Long-horizon LLM agents can benefit from reusable skills, yet existing skill-based methods often rely on external skill generators during training or persistent skill retrieval at inference, increasing engineering comple...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Scaling Search Relevance: Augmenting App Store Ranking with LLM-Generated Judgments](http://arxiv.org/abs/2602.23234v4)
  来源：arXiv | 日期：2026-02-26 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Large-scale commercial search systems optimize for relevance to drive successful sessions that help users find what they are looking for. To maximize relevance, we leverage two complementary objectives: behavioral releva...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [MINA: linear probes reveal coding-sequence family signal in frozen DNA encoders](https://www.biorxiv.org/content/10.64898/2026.05.25.727711v2)
  来源：bioRxiv | 日期：2026-05-30 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：MotivationFrozen DNA encoders are often used as genomic feature extractors, but downstream fine-tuning does not show what information is already linearly accessible in their unchanged embeddings. We introduce MINA (Model...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Evolutionary constraints improve protein large language model predictions for protein stability, binding regions and epistasis](https://www.biorxiv.org/content/10.64898/2026.05.22.726784v2)
  来源：bioRxiv | 日期：2026-06-01 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Our understanding of protein function and evolution is largely based on the relationship between amino acid sequence and overall fold, now effectively captured by computational models. Yet predicting how mutations--shape...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Transfer learning with pre-trained language models for protein expression level prediction in Escherichia coli .](https://pubmed.ncbi.nlm.nih.gov/41438772/)
  来源：PubMed | 日期：2026-06-01 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Accurately predicting recombinant protein expression in Escherichia coli remains a long-standing challenge due to the multifactorial nature of gene regulation and translation. Existing computational approaches typically ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Integrating protein and DNA embeddings for improving genome-wide transcription factor binding site prediction.](https://pubmed.ncbi.nlm.nih.gov/42099803/)
  来源：PubMed | 日期：2026-06-01 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Transcription factors (TFs) regulate gene expression by binding to specific DNA sites on genome, making accurate TF binding site prediction critical for understanding gene regulation and downstream phenotypes. Almost all...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Big data in multiple sclerosis.](https://pubmed.ncbi.nlm.nih.gov/41925198/)
  来源：PubMed | 日期：2026-06-01 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：本综述总结了利用多源大数据和先进分析技术在多发性硬化症（MS）领域取得的关键进展。源自MS大数据的真实世界证据（RWE）显著优化了治疗策略，重新定义了疾病进展概念，并完善了预后模型。RWE强调了早期强化治疗相较于阶梯治疗的长期获益，揭示了减量治疗的风险及妊娠期管理的重要性。此外，研究明确了特定高效疗法的有效性与安全性差异，以及换药的关键预测因子。RWE还强调了“独立于复发活动的进展”（PIRA）是导致成人和儿童MS残疾及长期不良预后的核...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Seeing Through the MiRAGE: Evaluating Multimodal Retrieval Augmented Generation](http://arxiv.org/abs/2510.24870v2)
  来源：arXiv | 日期：2025-10-28 | 相关度：2.1 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：We introduce MiRAGE, an evaluation framework for retrieval-augmented generation (RAG) from multimodal sources. As audiovisual media becomes a prevalent source of information online, it is essential for RAG systems to int...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Field-ready portable rapid nucleic acid test for tuberculosis detection and drug-resistance profiling in resource-limited settings](https://www.medrxiv.org/content/10.64898/2026.05.29.26354438v1)
  来源：medRxiv | 日期：2026-06-01 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Tuberculosis (TB) remains one of the deadliest infectious diseases, with over a million deaths annually and a growing threat from multidrug-resistant strains (MDR-TB). A major bottleneck in controlling TB is the lack of ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AI-Guided Structure-Aware Modeling and Thermal Proteomics Reveal Direct Demethylzeylasteral-ACLY Interaction](https://www.biorxiv.org/content/10.64898/2026.04.07.717093v2)
  来源：bioRxiv | 日期：2026-06-01 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：鉴定生物活性天然产物的直接分子靶点是化学生物学的核心挑战。本研究提出了一种集成实验与计算的闭环框架，结合基质增强热蛋白质组学与整体图神经网络（HoloGNN），用于系统地筛选并验证蛋白质-配体相互作用。HoloGNN 在 PDBbind 数据集基准测试中达到了当前最先进（SOTA）的性能。研究人员将该框架应用于 50 种结构多样的天然产物，成功鉴定出去甲基扁蒴藤素（Demethylzeylasteral）是 ACLY（三磷酸腺苷柠檬酸裂...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Thermoregulation and associated disorders: 3PM-guided holistic approach bridging innovative and traditional Chinese medicine.](https://pubmed.ncbi.nlm.nih.gov/42179458/)
  来源：PubMed | 日期：2026-06-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Accurately performed thermoregulation is life-important for the human body. Therefore, a relatively narrow temperature range of 36.5-37 °C, which all our biochemical reactions are adapted to, is rigorously kept by the bo...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Privacy Policy Enforcement Guardrails for Data-Sensitive Retrieval-Augmented Generation](http://arxiv.org/abs/2605.17034v2)
  来源：arXiv | 日期：2026-05-16 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Standard PII filters often miss contextual data leakage in RAG systems, such as non-regulated attribute clusters that collectively identify individuals. We introduce a Privacy Policy Enforcement (PPE) framework using dua...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [TechGraphRAG: An Agentic Graph-Augmented RAG Framework for Technical Literature Reasoning](http://arxiv.org/abs/2606.01613v1)
  来源：arXiv | 日期：2026-06-01 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：This paper presents an agentic retrieval-augmented generation (RAG) framework for domain-specific technical reasoning support, instantiated over a curated corpus of approximately 2,100 academic papers in intelligent tire...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RoboDream: Compositional World Models for Scalable Robot Data Synthesis](http://arxiv.org/abs/2606.02577v1)
  来源：arXiv | 日期：2026-06-01 | 相关度：0.7 | 新颖度：7.25
  匹配主题：未命中具体主题
  中文摘要：Scaling robot learning requires large-scale, diverse demonstrations, yet real-world data collection via teleoperation remains prohibitively expensive and time-consuming. While video diffusion models offer a promising ave...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [LongLive-RAG: A General Retrieval-Augmented Framework for Long Video Generation](http://arxiv.org/abs/2606.02553v1)
  来源：arXiv | 日期：2026-06-01 | 相关度：0.7 | 新颖度：7.23
  匹配主题：未命中具体主题
  中文摘要：Autoregressive (AR) video diffusion enables variable-length synthesis, but long-horizon generation often suffers from accumulated errors and identity drift. For efficiency, existing methods commonly adopt sliding-window ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Retrieve What's Missing: Coverage-Maximizing Retrieval for Consistent Long Video Generation](http://arxiv.org/abs/2606.02479v1)
  来源：arXiv | 日期：2026-06-01 | 相关度：0.7 | 新颖度：7.06
  匹配主题：未命中具体主题
  中文摘要：Maintaining long-term geometric consistency remains challenging for long-horizon autoregressive video generation. Memory-augmented generative models address this by retrieving historical frames, but their effectiveness d...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Differentially Private Datastore Generation for Retrieval-Augmented Inference](http://arxiv.org/abs/2606.01413v1)
  来源：arXiv | 日期：2026-05-31 | 相关度：0.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：It is crucial for modern on-device AI systems that rely on retrieval-augmented inference to release and share datastores without compromising individual privacy. This can be achieved using Differential Privacy (DP), whic...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Self-Conditioned Positional HNSW for Overlap-Aware Retrieval in Chunked-Document RAG Systems: Method and Industrial Evidence-Quality Audit](http://arxiv.org/abs/2606.01542v1)
  来源：arXiv | 日期：2026-06-01 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Chunked-document retrieval is a common component of retrieval-augmented generation (RAG) systems. Documents are split into overlapping chunks, embedded, and indexed with approximate nearest-neighbor search such as hierar...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Artificial intelligence in combating challenges in antimicrobial resistance: a narrative review.](https://pubmed.ncbi.nlm.nih.gov/41859321/)
  来源：PubMed | 日期：2026-06-01 | 相关度：6.15 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：Antimicrobial resistance (AMR) is a major global health challenge that threatens the effective prevention and treatment of infections. It arises from increasing resistance rates, limited diagnostic capacity, inappropriat...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [AI-driven big data analysis and predictive modeling of infectious disease immunity: from correlates to causal, multiscale understanding.](https://pubmed.ncbi.nlm.nih.gov/42217024/)
  来源：PubMed | 日期：2026-05-30 | 相关度：5.65 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：The ability to reliably predict protective immunity against infectious diseases remains a central challenge in immunology, vaccine development, and public health. Despite major advances in immunological measurement, immu...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [From risk to resilience: A narrative review on strengthening veterinary clinical biosecurity to prevent healthcare-associated infections.](https://pubmed.ncbi.nlm.nih.gov/42025907/)
  来源：PubMed | 日期：2026-06-01 | 相关度：4.45 | 新颖度：0.25
  匹配主题：pathogenomics, application_monitoring
  中文摘要：Veterinary clinical biosecurity is key to preventing infectious diseases in animal clinics, particularly when there is high patient turnover, a mix of species, close contact among animals, or immunocompromised patients t...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial Intelligence in Oncology: Clinical Applications, Challenges, and Opportunities.](https://pubmed.ncbi.nlm.nih.gov/42214043/)
  来源：PubMed | 日期：2026-06-01 | 相关度：3.75 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence (AI) is reshaping cancer research and clinical oncology by enabling large-scale analysis of complex biomedical data. Although early AI efforts focused on single-modality tasks such as imaging inte...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Integrating multi-omics data and artificial intelligence for personalized medicine in glioblastoma.](https://pubmed.ncbi.nlm.nih.gov/41921727/)
  来源：PubMed | 日期：2026-06-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Glioblastoma (GBM) is one of the most lethal primary brain tumors and is characterized by profound molecular heterogeneity, rapid progression, and limited therapeutic responsiveness. Traditional diagnostic and treatment ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [RCEM: Embedder Equipped with Query Rewriting Skill for Robust Conversational Search in Distributional Shift](http://arxiv.org/abs/2606.01697v1)
  来源：arXiv | 日期：2026-06-01 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Conversational search has become increasingly important in retrieval-augmented generation (RAG) systems, where users interact with AI assistants through multi-turn conversations containing context-dependent queries. We p...
  为什么值得看：RCEM: Embedder Equipped with Query Rewri 与你的主题有弱匹配，暂时保留作低优先级跟踪。

- [The Neuromorphic Supremacy](http://arxiv.org/abs/2606.01841v1)
  来源：arXiv | 日期：2026-06-01 | 相关度：0.7 | 新颖度：6.06
  匹配主题：未命中具体主题
  中文摘要：Live neural systems demonstrate remarkable capabilities to learn new behavior and patterns from mere few examples and are known to operate robustly under severe sensory noise. These capabilities, however, remain largely ...
  为什么值得看：The Neuromorphic Supremacy 与你的主题有弱匹配，暂时保留作低优先级跟踪。

- [DiscourseFlip: An Oblique Discourse-Level Opinion Manipulation Attack against Black-box Retrieval-Augmented Generation](http://arxiv.org/abs/2606.01212v1)
  来源：arXiv | 日期：2026-05-31 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) systems are widely deployed and increasingly influential, but their reliance on external corpora exposes new security risks from poisoned retrieval content. Existing RAG attacks are l...
  为什么值得看：DiscourseFlip: An Oblique Discourse-Leve 与你的主题有弱匹配，暂时保留作低优先级跟踪。
