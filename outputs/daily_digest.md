# 每日论文监控日报 (2026-09-22)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 41 篇新论文。

## 抓取状态

- arXiv：成功，命中 39 篇
- PubMed：成功，命中 21 篇
- bioRxiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='api.biorxiv.org', port=443): Read timed out. (read timeout=60)
- medRxiv：成功，命中 14 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [PRISM-RAG: Multimodal Hypergraph Retrieval-Augmented Generation for Tobacco Product and Legislative Policy Reasoning](http://arxiv.org/abs/2609.23769v1)
  来源：arXiv | 日期：2026-09-20 | 相关度：7.9 | 新颖度：6.2
  匹配主题：foundation_model_agent
  中文摘要：The disambiguation of semantically similar statutory text across jurisdictions is a retrieval problem that existing methods do not solve. This inter-context conflict can steer generative models toward confidently produce...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [Discrete Tokenization for Multimodal LLMs: A Comprehensive Survey](http://arxiv.org/abs/2507.22920v2)
  来源：arXiv | 日期：2025-07-21 | 相关度：7.5 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：The rapid advancement of large language models (LLMs) has intensified the need for effective mechanisms to transform continuous multimodal data into discrete representations suitable for language-based processing. Discre...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Incorporating LLM Embeddings for Variation Across the Human Genome](http://arxiv.org/abs/2509.20702v3)
  来源：arXiv | 日期：2025-09-25 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in large language model (LLM) embeddings have enabled powerful representations for biological data, but most applications to date focus on gene-level information. We present one of the first systematic fr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [FinAcumen: Financial Multimodal Reasoning via Self-Evolving Experience Memory Harness](http://arxiv.org/abs/2606.17642v6)
  来源：arXiv | 日期：2026-06-16 | 相关度：6.8 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Financial multimodal reasoning requires agents to coordinate numerical computation, retrieval, visual interpretation, and temporal grounding across heterogeneous evidence sources. Existing tool-augmented agents improve e...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Discovery of Interpretable Surrogates via Agentic AI: Application to Gravitational Waves](http://arxiv.org/abs/2605.11280v2)
  来源：arXiv | 日期：2026-05-11 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Fast surrogate models for expensive simulations are now essential across the sciences, yet they typically operate as black boxes. We present \texttt{GWAgent}, a large language model (LLM)-based workflow that constructs i...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evaluating agentic simulation for local public health estimation](https://www.medrxiv.org/content/10.64898/2026.09.19.26363431v1)
  来源：medRxiv | 日期：2026-09-21 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large language model (LLM)-based generative agents can reproduce aspects of individual human behavior, but whether they can be scaled to geographically grounded populations that reproduce real-world health behaviors rema...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Large language model linguistic perplexity in childhood onset psychosis: unique features and developmental trends](https://www.medrxiv.org/content/10.64898/2026.09.17.26363314v1)
  来源：medRxiv | 日期：2026-09-20 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Objective: Child and early adolescent onset psychosis (COP) is associated with subtle changes in language linked to thought disorder, a key contributor to functional impairment. Large language models (LLM) can detect dev...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Divide by Question, Conquer by Agent: SPLIT-RAG with Question-Driven Graph Partitioning](http://arxiv.org/abs/2505.13994v3)
  来源：arXiv | 日期：2025-05-20 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) systems empower large language models (LLMs) with external knowledge, yet struggle with efficiency-accuracy trade-offs when scaling to large knowledge graphs. Existing approaches ofte...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [WorldScape Policy 2.0: Empowering Steerable World Action Modeling with Reasoning-Augmented Memory and In-Context Learning](http://arxiv.org/abs/2607.18840v2)
  来源：arXiv | 日期：2026-07-21 | 相关度：6.1 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：World Action Models (WAMs) offer a promising paradigm for robotic manipulation by jointly modeling visual state transitions and robot actions. However, existing WAMs are constrained by limited temporal context, coarse ep...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Knowledge-Graph Grounding Helps LLMs Only for Out-of-Training Knowledge: A Controlled Study on Clinical Question Answering](http://arxiv.org/abs/2606.22419v3)
  来源：arXiv | 日期：2026-06-21 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：A recent Nature Medicine study reports that general-purpose frontier LLMs outperform specialized retrieval-augmented clinical tools on medical benchmarks, and that retrieval can hurt strong models. We ask the natural fol...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The Online Health Safety Gap: Consensus Alignment Does Not Imply Safety in Peer-to-Peer Health Narratives.](https://www.medrxiv.org/content/10.64898/2026.09.18.26363448v1)
  来源：medRxiv | 日期：2026-09-21 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Online health information systems evaluate content by its alignment with medical consensus, treating that alignment as a reliable signal of safety. In peer-to-peer health discourse, that assumption fails: advice that is ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [URA-NER: A Unified Retrieval-Augmented Framework with Retrieval Alignment and Uncertainty Reduction for Low-Resource NER](http://arxiv.org/abs/2609.24372v1)
  来源：arXiv | 日期：2026-09-21 | 相关度：4.75 | 新颖度：6.9
  匹配主题：foundation_model_agent
  中文摘要：In-context learning (ICL) based on large language models (LLMs) has shown promising potential in alleviating performance bottlenecks caused by the limited availability of annotated data in Named Entity Recognition (NER)....
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LADDER: Graph-Guided Diffusion Language Models for Efficient Multi-Hop Reasoning](http://arxiv.org/abs/2609.24346v1)
  来源：arXiv | 日期：2026-09-21 | 相关度：4.75 | 新颖度：6.84
  匹配主题：foundation_model_agent
  中文摘要：Graph Retrieval-Augmented Generation (GraphRAG) has remarkably enhanced large language models on complex reasoning by leveraging structured entity topologies. However, existing frameworks heavily rely on standard autoreg...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Smarter by the Moment: Environment-Driven Dynamic Policies for Continual LLM Improvement](http://arxiv.org/abs/2609.16800v2)
  来源：arXiv | 日期：2026-09-15 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have achieved remarkable progress across diverse domains, but continual adaptation to evolving tasks and environments remains a key challenge. Existing memory-augmented approaches retrieve in...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A dual-enzymatic activity/SERS dual-mode sensor array based on BSA-Cu nanoflowers for sensitive detection of various foodborne pathogens.](https://pubmed.ncbi.nlm.nih.gov/42401476/)
  来源：PubMed | 日期：2026-09-22 | 相关度：3.8 | 新颖度：8.22
  匹配主题：foundation_model_agent, application_monitoring
  中文摘要：Rapid and accurate detection of multiple foodborne pathogens is critical for public health and food safety. Although various sensing methods exist, many still face challenges in simultaneously discriminating and quantify...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [How Do LLMs Cite? A Mechanistic Interpretation of Attribution in Retrieval-Augmented Generation](http://arxiv.org/abs/2606.28358v2)
  来源：arXiv | 日期：2026-06-09 | 相关度：6.15 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) aims to enhance the trustworthiness of Large Language Models (LLMs) by grounding their outputs in external documents, often using inline citations for verifiability. However, the fait...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Efficient LLM Distillation for Bangladesh Legal Context: A Smartphone-Compatible Retrieval-Augmented Generation Model](http://arxiv.org/abs/2609.24177v1)
  来源：arXiv | 日期：2026-09-21 | 相关度：6.15 | 新颖度：6.36
  匹配主题：foundation_model_agent
  中文摘要：Legal information in Bangladesh is inaccessible to most citizens. Statutory text is English-only, trained lawyers are concentrated in urban centres, and cloud-dependent AI fails where mobile connectivity is unreliable, a...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Beyond Similarity: Coverage-Aware Prompt Selection for Time Series Forecasting with LLMs](http://arxiv.org/abs/2609.22977v1)
  来源：arXiv | 日期：2026-09-19 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Similarity-based retrieval is the dominant rule for conditioning large language models (LLMs) in in-context learning, retrieval-augmented generation, and prompt-based time series forecasting. The rule concentrates on nea...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Controlling risks of AI in chemical science with agents](http://arxiv.org/abs/2312.06632v2)
  来源：arXiv | 日期：2023-12-11 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence is rapidly advancing scientific discovery, but this progress carries risks of misuse, such as the creation of harmful substances, or circumvention of established regulations. In this paper, we fir...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Tool-Augmented On-Policy Distillation for LLM Domain Adaptation in Sequence-Based Omics Tasks](http://arxiv.org/abs/2609.23435v1)
  来源：arXiv | 日期：2026-09-20 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Multi-omics sequences contain complex biological patterns, yet deciphering their mechanisms for automated scientific discovery remains challenging. As large language models (LLMs) interpret these sequences, evaluating bo...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Taramandal-GPT: Enhancing Astrodynamics Problem-Solving with Knowledge Retrieval and Structured Thinking](http://arxiv.org/abs/2609.24246v1)
  来源：arXiv | 日期：2026-09-21 | 相关度：5.45 | 新颖度：6.84
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have shown remarkable progress in natural language understanding, yet their effectiveness in specialized fields like astronomy and astrodynamics remains limited due to challenges in multi-ste...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Retrieval-in-the-Chain: Bootstrapping Large Language Models for Generative Retrieval](http://arxiv.org/abs/2510.13095v3)
  来源：arXiv | 日期：2025-10-15 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Generative retrieval (GR) is an emerging paradigm that leverages large language models (LLMs) to autoregressively generate document identifiers (docids) relevant to a given query. Prior works have focused on leveraging t...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Bridging Static and Agentic RAG for Taiwanese Historical Question Answering](http://arxiv.org/abs/2609.23056v1)
  来源：arXiv | 日期：2026-09-19 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Agentic retrieval-augmented generation (RAG) enables language models to adapt retrieval based on previously retrieved evidence, but it remains unclear whether such adaptive orchestration consistently outperforms well-des...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Fully Automated Abstraction of Longitudinal Breast Oncology Records with Off-The-Shelf Large Language Models](https://www.medrxiv.org/content/10.64898/2026.03.23.26349012v2)
  来源：medRxiv | 日期：2026-09-21 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Background: Manual chart abstraction is a major bottleneck in clinical research. In oncology, important outcomes such as disease recurrence and the treatment history are often only documented in clinical notes, limiting ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Reasoning Reduces the Influence of Poisoned Context in RAG](http://arxiv.org/abs/2608.17153v3)
  来源：arXiv | 日期：2026-08-17 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) improves large language models by grounding them in external evidence, but this exposes them to knowledge-poisoning attacks, where misinformation injected into retrieved documents inf...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Artificial intelligence in onco-anaesthesia: Current applications, challenges, and future directions.](https://pubmed.ncbi.nlm.nih.gov/42625971/)
  来源：PubMed | 日期：2026-09-20 | 相关度：3.75 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence (AI) is transforming onco-anaesthesia by shifting practice from reactive physiological management toward predictive and precision-based care. This review outlines current AI applications across th...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Document Retrieval-Aware Chunking (D-RAC): Universal Retrieval-Aware Ingestion of Enterprise Documents via PDF Normalization and Multimodal Markdown Conversion](http://arxiv.org/abs/2609.24220v1)
  来源：arXiv | 日期：2026-09-21 | 相关度：2.1 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) systems over enterprise knowledge bases must ingest heterogeneous document formats -- PDFs, Word documents, presentations, and scans -- whose content is locked inside complex visual l...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RADAR: Retrieval-Augmented Detector with Adversarial Refinement for Adaptive LLM-Generated Fake News Detection](http://arxiv.org/abs/2601.03981v3)
  来源：arXiv | 日期：2026-01-07 | 相关度：2.05 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：To efficiently combat the spread of LLM-generated misinformation in the news domain, we present RADAR, a Retrieval-Augmented Detector with Adversarial Refinement for adaptive LLM-generated fake news detection. Our approa...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MES: A Multi-Agent Evidence Synthesis System for Medical Decision-Making](https://www.medrxiv.org/content/10.64898/2026.09.15.26362921v1)
  来源：medRxiv | 日期：2026-09-21 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Medical evidence synthesis increasingly requires published studies, real-world clinical data and structured biomedical knowledge, yet most automated systems remain centered on literature retrieval and summarization. Here...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Graph Memory for LLM Agents: At What Cost? A Comparative Evaluation of Query, Ingest, and Update Performance Across Graph Database Engines](http://arxiv.org/abs/2609.23315v1)
  来源：arXiv | 日期：2026-09-20 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Graph databases are frequently positioned as categorically necessary for connected-data workloads, yet the systems dimension along which they actually differ - query planning, indexing, and data-readiness cost - is rarel...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond Relevance: Structured Semantic Supervision for Product Search with LLM-Augmented Annotations](http://arxiv.org/abs/2609.23646v1)
  来源：arXiv | 日期：2026-09-20 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：E-commerce search requires distinguishing products that are merely related to a query from those that directly satisfy the user's shopping intent. We augment query-product pairs with structured LLM-generated query and pr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [QLoRA Fine-Tuning of Ministral LLM for Sequence-to-Function Protein Annotation](http://arxiv.org/abs/2609.24538v1)
  来源：arXiv | 日期：2026-09-21 | 相关度：2.4 | 新颖度：6.67
  匹配主题：未命中具体主题
  中文摘要：Functional annotation of newly sequenced proteins remains a bottleneck in molecular biology: the number of sequences in public repositories grows far faster than the capacity for manual curation. Most computational appro...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Ground-Truth Subgraphs for Better Training and Evaluation of Knowledge Graph Augmented LLMs](http://arxiv.org/abs/2511.04473v3)
  来源：arXiv | 日期：2025-11-06 | 相关度：0.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval of information from graph-structured knowledge bases represents a promising direction for improving the factuality of LLMs. While various solutions have been proposed, a comparison of methods is difficult due t...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Metadata Supervised Imaging Representations for Modelling and Controlling Acquisition Variability](http://arxiv.org/abs/2607.11295v2)
  来源：arXiv | 日期：2026-07-13 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Biomedical imaging data exhibit substantial acquisition variability, where identical biological structures can appear markedly different due to differences in imaging devices, acquisition protocols, sites, and reconstruc...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Deep Generative and Graph-Based Representation Learning for Multiomics Survival Stratification in Ovarian Cancer: Secondary Analysis.](https://pubmed.ncbi.nlm.nih.gov/42766802/)
  来源：PubMed | 日期：2026-09-21 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Ovarian cancer remains one of the most lethal gynecologic malignancies, largely due to pronounced molecular heterogeneity, nonspecific clinical presentation, and frequent diagnosis at advanced stages. Multiomics profilin...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Re:CAP - Auditing Retrieval Coverage in Production RAG Pipelines](http://arxiv.org/abs/2609.24122v1)
  来源：arXiv | 日期：2026-09-21 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) is hard to monitor in production: exhaustive relevance labels do not exist for non-stationary multi-million-passage corpora that re-index in real time. As a result, retrieval quality ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [From Backlog Items to Security Guidance: Towards Continuous Security Compliance](http://arxiv.org/abs/2607.27374v2)
  来源：arXiv | 日期：2026-07-29 | 相关度：0.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Continuous software engineering in regulated domains requires engineering teams to address security throughout the development lifecycle. Yet making security requirements explicit in backlog items is still problematic. E...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Q-TIE: A Lightweight and Generalizable Re-ranking Framework for Temporal Information Retrieval](http://arxiv.org/abs/2609.23880v1)
  来源：arXiv | 日期：2026-09-20 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Temporal Information Retrieval (TIR) has been increasingly critical given the rise of Retrieval-Augmented Generation (RAG). Since temporally mismatched evidence can be highly misleading, TIR aims to retrieve documents th...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Identifying cohorts at elevated risk of cancers using generative modeling of patient health states](https://www.medrxiv.org/content/10.64898/2026.09.09.26362676v2)
  来源：medRxiv | 日期：2026-09-19 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：While large language models are powerful generators of new text, forecasting disease progression from longitudinal health histories remains a challenging problem. We introduce GenEHR, an autoregressive generative model t...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial Intelligence-Enhanced Electrocardiography for Detection and Prediction of Hypertrophic Cardiomyopathy across Monogenic and Polygenic Susceptibility](https://www.medrxiv.org/content/10.64898/2026.09.12.26362902v1)
  来源：medRxiv | 日期：2026-09-21 | 相关度：3.65 | 新颖度：5.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Background: Cascade screening increasingly identifies carriers of pathogenic or likely pathogenic sarcomere variants at risk for hypertrophic cardiomyopathy (HCM) in whom penetrance is incomplete, and surveillance relies...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Clinical and attitudinal outcomes of a personalized, multimodal lifestyle intervention for Alzheimer's disease prevention in high-risk, cognitively normal older adults in north Alabama: A pilot study](https://www.medrxiv.org/content/10.64898/2026.09.19.26363495v1)
  来源：medRxiv | 日期：2026-09-21 | 相关度：3.05 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：INTRODUCTION: Multimodal lifestyle interventions can delay or slow Alzheimer's disease (AD) in at-risk older adults, and plasma pTau217, a blood-based biomarker, now enables scalable AD risk stratification. Population-le...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
