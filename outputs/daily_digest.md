# 每日论文监控日报 (2026-09-24)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 39 篇新论文。

## 抓取状态

- arXiv：成功，命中 50 篇
- PubMed：成功，命中 51 篇
- bioRxiv：失败，命中 0 篇，错误：Expecting value: line 1 column 1 (char 0)
- medRxiv：失败，命中 0 篇，错误：Expecting value: line 1 column 1 (char 0)

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [GLIMP: An Integrated Graph Neural Network-Large Language Model for Promoter Recognition.](https://pubmed.ncbi.nlm.nih.gov/42776895/)
  来源：PubMed | 日期：2026-09-21 | 相关度：8.9 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Accurate identification of DNA promoter regions is crucial for understanding gene regulation, yet remains challenging. Existing models often struggle to generalize across species or promoter types due to their inability ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [ChatT2: An Adaptive Framework for Developing a Large Language Model-Based Agent for Natural Product Domain Research](http://arxiv.org/abs/2609.25620v1)
  来源：arXiv | 日期：2026-09-22 | 相关度：8.85 | 新颖度：1.0
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Scientific investigations into microbial natural products (NPs) present significant challenges for novices, largely due to the complexity of microbial systems, biochemical diversity, technical skill requirements, and the...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Potential for Enhanced Learning in Machine Learning Classes by Using Wiki LLM Indexing](http://arxiv.org/abs/2609.25303v1)
  来源：arXiv | 日期：2026-09-21 | 相关度：7.9 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models are increasingly deployed as course-specific tutors, but their usefulness depends on grounding in vetted instructional materials that are often revised mid-semester. Our prior work built a multimoda...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Discrete Tokenization for Multimodal LLMs: A Comprehensive Survey](http://arxiv.org/abs/2507.22920v2)
  来源：arXiv | 日期：2025-07-21 | 相关度：7.5 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：The rapid advancement of large language models (LLMs) has intensified the need for effective mechanisms to transform continuous multimodal data into discrete representations suitable for language-based processing. Discre...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Integration of Retrieval-Augmented Generation for Knowledge Access in the ELBE Accelerator Control System](http://arxiv.org/abs/2609.27579v1)
  来源：arXiv | 日期：2026-09-23 | 相关度：6.55 | 新颖度：6.48
  匹配主题：foundation_model_agent
  中文摘要：The efficient operation of accelerator facilities increas- ingly relies on rapid access to heterogeneous operational knowledge, including logbooks, interlock reports, machine parameters, and historical archive data. At E...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RAG-NAROK: Retrieval-Aware Knowledge Corpus Poisoning in RAG with Source-specific Refutation](http://arxiv.org/abs/2609.25469v1)
  来源：arXiv | 日期：2026-09-21 | 相关度：6.55 | 新颖度：1.2
  匹配主题：foundation_model_agent
  中文摘要：Retrieval augmented generation (RAG) systems have emerged as the dominant architecture for grounding large language model (LLM) outputs in verifiable external knowledge, yet their structural reliance on a dynamic retriev...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Retrieval Augmented (Knowledge Graph), and Large Language Model-Driven Design Structure Matrix (DSM) Generation of Cyber-Physical Systems](http://arxiv.org/abs/2602.16715v2)
  来源：arXiv | 日期：2026-01-30 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：We explore the potential of Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and Graph-based RAG (GraphRAG) for generating Design Structure Matrices (DSMs). We test these methods on two distinct use ca...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [GlyRAG: Context-Aware Retrieval-Augmented Framework for Blood Glucose Forecasting](http://arxiv.org/abs/2601.05353v3)
  来源：arXiv | 日期：2026-01-08 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Accurate blood glucose forecasting using continuous glucose monitoring (CGM) data can support the early prediction of dysglycemic risk. However, current neural-network-based forecasting models treat CGM data as a purely ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ProteinJEPA: Latent prediction improves protein language model pretraining](http://arxiv.org/abs/2605.07554v2)
  来源：arXiv | 日期：2026-05-08 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Protein language models are trained primarily with masked language modeling (MLM), which predicts masked amino-acid identities. Joint-embedding predictive architectures (JEPA) instead predict latent representations, but ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [UR$^2$: Unify RAG and Reasoning through Reinforcement Learning](http://arxiv.org/abs/2508.06165v6)
  来源：arXiv | 日期：2025-08-08 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have shown strong capabilities through two complementary paradigms: Retrieval-Augmented Generation (RAG) for knowledge grounding and Reinforcement Learning from Verifiable Rewards (RLVR) for ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Meet, Compare, or Abstain: LatWeave for Deterministic Multi-Hop Question Answering on Knowledge Lattices](http://arxiv.org/abs/2609.27225v1)
  来源：arXiv | 日期：2026-09-23 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Probabilistic question-answering systems -- whether large language models (LLMs) themselves, retrieval-augmented generation (RAG), or trained multi-hop retrievers -- conflate "what is known" and "how to reason" into a si...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Advances in Machine Learning for Drug Repurposing: From Methodologies to Precision Medicine with Case Studies in COVID-19, Parkinson's Disease, and Cancer.](https://pubmed.ncbi.nlm.nih.gov/42776876/)
  来源：PubMed | 日期：2026-09-23 | 相关度：5.75 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：This review investigates recent advances in machine learning (ML) for drug repurposing, with applications spanning COVID-19, Parkinson's disease, and cancer. We provide a methodological taxonomy of ML techniques includin...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [RexDrug: Reliable Multi-Drug Combination Extraction through Reasoning-Enhanced LLMs](http://arxiv.org/abs/2603.08166v2)
  来源：arXiv | 日期：2026-03-09 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Automated Drug Combination Extraction (DCE) from large-scale biomedical literature is crucial for advancing precision medicine and pharmacological research. However, existing relation extraction methods primarily focus o...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 其他

- [Only Pay What You Must Spend: On-Demand Privacy Budget Payment for Differentially Private RAG](http://arxiv.org/abs/2609.27406v1)
  来源：arXiv | 日期：2026-09-23 | 相关度：4.75 | 新颖度：5.29
  匹配主题：foundation_model_agent
  中文摘要：Deploying large language models (LLMs) on sensitive data via Retrieval-Augmented Generation (RAG) introduces severe privacy risks. Recent studies apply Differential Privacy (DP) to LLMs with RAG for formal privacy guaran...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Knowledge-as-Skill: A Structural Design for Autonomous Knowledge-Base Use by LLM Agents](http://arxiv.org/abs/2609.25991v1)
  来源：arXiv | 日期：2026-09-22 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) gives large language models (LLMs) access to external knowledge, but its conventional retrieve-concatenate-generate pipeline makes retrieval decisions on behalf of the model. As tool ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LADDER: Graph-Guided Diffusion Language Models for Efficient Multi-Hop Reasoning](http://arxiv.org/abs/2609.24346v1)
  来源：arXiv | 日期：2026-09-21 | 相关度：4.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Graph Retrieval-Augmented Generation (GraphRAG) has remarkably enhanced large language models on complex reasoning by leveraging structured entity topologies. However, existing frameworks heavily rely on standard autoreg...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [URA-NER: A Unified Retrieval-Augmented Framework with Retrieval Alignment and Uncertainty Reduction for Low-Resource NER](http://arxiv.org/abs/2609.24372v1)
  来源：arXiv | 日期：2026-09-21 | 相关度：4.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：In-context learning (ICL) based on large language models (LLMs) has shown promising potential in alleviating performance bottlenecks caused by the limited availability of annotated data in Named Entity Recognition (NER)....
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A dual-enzymatic activity/SERS dual-mode sensor array based on BSA-Cu nanoflowers for sensitive detection of various foodborne pathogens.](https://pubmed.ncbi.nlm.nih.gov/42401476/)
  来源：PubMed | 日期：2026-09-22 | 相关度：3.8 | 新颖度：0.25
  匹配主题：foundation_model_agent, application_monitoring
  中文摘要：Rapid and accurate detection of multiple foodborne pathogens is critical for public health and food safety. Although various sensing methods exist, many still face challenges in simultaneously discriminating and quantify...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Document Silos to Process Intelligence: A Multi-Layer Knowledge Graph for CMC Process Development](http://arxiv.org/abs/2609.11493v2)
  来源：arXiv | 日期：2026-09-10 | 相关度：2.1 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Chemistry, Manufacturing and Controls (CMC) process development generates an enormous body of technical information across a multi-stage, knowledge-intensive continuum from drug discovery to commercial manufacturing. Thi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Document Retrieval-Aware Chunking (D-RAC): Universal Retrieval-Aware Ingestion of Enterprise Documents via PDF Normalization and Multimodal Markdown Conversion](http://arxiv.org/abs/2609.24220v1)
  来源：arXiv | 日期：2026-09-21 | 相关度：2.1 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) systems over enterprise knowledge bases must ingest heterogeneous document formats -- PDFs, Word documents, presentations, and scans -- whose content is locked inside complex visual l...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Silent Failures in Agent-Tool Interaction: An Audit of ToolUniverse](http://arxiv.org/abs/2609.26836v1)
  来源：arXiv | 日期：2026-09-21 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Agentic AI systems are increasingly adopting automated pipelines that integrate multiple tools. While prior research and benchmarks have studied about task success and task completion of these agentic systems, the resear...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BoundaryMORPH: Budgeted Reranking via Active Set Selection for Diffuse Retrieval](http://arxiv.org/abs/2609.27213v1)
  来源：arXiv | 日期：2026-09-23 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Open-ended queries in modern Retrieval-Augmented Generation (RAG) are increasingly "diffuse," requiring a large set of documents to be assembled into a finite LLM context window. To ensure retrieval quality, systems use ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Autonomous Quantum Transport Measurements of 2D Semiconductors by an AI Agent](http://arxiv.org/abs/2609.26661v1)
  来源：arXiv | 日期：2026-09-22 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Artificial-intelligence (AI) agents are beginning to enter experimental laboratories, automating experiments and accelerating scientific discovery. Herein, we introduce an AI-driven workflow in which an AI agent performs...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agent-E2MD: Autonomous Translation of Interatomic Potential Equations into Physically Validated Pair Styles for Molecular Dynamics in LAMMPS](http://arxiv.org/abs/2609.26657v1)
  来源：arXiv | 日期：2026-09-22 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Interatomic potentials underpin MD and govern predictive atomistic-model fidelity for metals, semiconductors, oxides, liquids, and reactive systems. A potential has limited practical value until reliably implemented in p...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Efficient LLM Distillation for Bangladesh Legal Context: A Smartphone-Compatible Retrieval-Augmented Generation Model](http://arxiv.org/abs/2609.24177v1)
  来源：arXiv | 日期：2026-09-21 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Legal information in Bangladesh is inaccessible to most citizens. Statutory text is English-only, trained lawyers are concentrated in urban centres, and cloud-dependent AI fails where mobile connectivity is unreliable, a...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [QLoRA Fine-Tuning of Ministral LLM for Sequence-to-Function Protein Annotation](http://arxiv.org/abs/2609.24538v1)
  来源：arXiv | 日期：2026-09-21 | 相关度：2.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Functional annotation of newly sequenced proteins remains a bottleneck in molecular biology: the number of sequences in public repositories grows far faster than the capacity for manual curation. Most computational appro...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Divide and Doubt: Diverse Distributed Poisoning for Retrieval-Augmented Generation](http://arxiv.org/abs/2609.27090v1)
  来源：arXiv | 日期：2026-09-22 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Multi-passage corpus poisoning often repeats one target claim across similar documents, creating correlated lexical and semantic patterns that similarity- and conflict-aware defenses can suppress jointly. We introduce Dn...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Ground-Truth Subgraphs for Better Training and Evaluation of Knowledge Graph Augmented LLMs](http://arxiv.org/abs/2511.04473v3)
  来源：arXiv | 日期：2025-11-06 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval of information from graph-structured knowledge bases represents a promising direction for improving the factuality of LLMs. While various solutions have been proposed, a comparison of methods is difficult due t...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Seeing the imagined: latent functional alignment in visual imagery decoding from fMRI data](http://arxiv.org/abs/2604.15374v2)
  来源：arXiv | 日期：2026-04-15 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Recent progress in visual brain decoding from fMRI has been enabled by large-scale datasets such as the Natural Scenes Dataset (NSD) and powerful diffusion-based generative models. While current pipelines are primarily o...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Sampling at intermediate temperatures is optimal for training large language models in protein structure prediction](http://arxiv.org/abs/2603.29529v2)
  来源：arXiv | 日期：2026-03-31 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Using a statistical mechanics framework, we investigate the parameter space of transformer models trained on protein sequence data. We sample the loss landscape at varying temperatures using Langevin dynamics to characte...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Taramandal-GPT: Enhancing Astrodynamics Problem-Solving with Knowledge Retrieval and Structured Thinking](http://arxiv.org/abs/2609.24246v1)
  来源：arXiv | 日期：2026-09-21 | 相关度：5.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have shown remarkable progress in natural language understanding, yet their effectiveness in specialized fields like astronomy and astrodynamics remains limited due to challenges in multi-ste...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Nursing, omics, and artificial intelligence: Precision health's trifecta.](https://pubmed.ncbi.nlm.nih.gov/42777318/)
  来源：PubMed | 日期：2026-09-22 | 相关度：2.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Precision health individualizes care by integrating biological, environmental, and social drivers of health, a perspective that aligns with the holistic lens of nursing. Advances in omics, including genomics, epigenomics...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Metadata Supervised Imaging Representations for Modelling and Controlling Acquisition Variability](http://arxiv.org/abs/2607.11295v2)
  来源：arXiv | 日期：2026-07-13 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Biomedical imaging data exhibit substantial acquisition variability, where identical biological structures can appear markedly different due to differences in imaging devices, acquisition protocols, sites, and reconstruc...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Deep Generative and Graph-Based Representation Learning for Multiomics Survival Stratification in Ovarian Cancer: Secondary Analysis.](https://pubmed.ncbi.nlm.nih.gov/42766802/)
  来源：PubMed | 日期：2026-09-21 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Ovarian cancer remains one of the most lethal gynecologic malignancies, largely due to pronounced molecular heterogeneity, nonspecific clinical presentation, and frequent diagnosis at advanced stages. Multiomics profilin...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [BELXTR: Biomedical Entity Linking via Contextualized Token Retrieval](http://arxiv.org/abs/2609.25859v1)
  来源：arXiv | 日期：2026-09-22 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Biomedical Entity Linking disambiguates mentions to entities in a knowledge base (KB), making it the cornerstone of information extraction pipelines. While embedding-based models are a popular approach for the task, they...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Re:CAP - Auditing Retrieval Coverage in Production RAG Pipelines](http://arxiv.org/abs/2609.24122v2)
  来源：arXiv | 日期：2026-09-21 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) is hard to monitor in production: exhaustive relevance labels do not exist for non-stationary multi-million-passage corpora that re-index in real time. As a result, retrieval quality ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Dual-Hypergraph Indexing: Bridging Knowledge Islands for Multi-Hop Reasoning in Retrieval-Augmented Generation](http://arxiv.org/abs/2609.28108v1)
  来源：arXiv | 日期：2026-09-23 | 相关度：0.7 | 新颖度：7.01
  匹配主题：未命中具体主题
  中文摘要：While hypergraph-based Retrieval-Augmented Generation (RAG) effectively captures higher-order multi-entity correlations, existing paradigms treat extracted hyperedges as isolated factual assertions. This structural fragm...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [TEMPS: Temporal Sentence Embeddings for Temporal Information Retrieval](http://arxiv.org/abs/2609.28048v1)
  来源：arXiv | 日期：2026-09-23 | 相关度：1.7 | 新颖度：6.92
  匹配主题：未命中具体主题
  中文摘要：Modern information retrieval (IR) systems rarely represent time, yet many information needs depend on it: in clinical, journalistic, and legal search, when an event occurred can decide whether a document is relevant. Den...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [NIMO Controller: a self-driving laboratory orchestrator based on the Model Context Protocol](http://arxiv.org/abs/2605.15227v2)
  来源：arXiv | 日期：2026-05-13 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Self-driving laboratories (SDLs) are attracting increasing attention as a means of accelerating scientific discovery; however, developing SDL software remains technically demanding. To improve accessibility, orchestratio...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。
