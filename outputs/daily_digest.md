# 每日论文监控日报 (2026-09-30)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 58 篇新论文。

## 抓取状态

- arXiv：成功，命中 65 篇
- PubMed：成功，命中 43 篇
- bioRxiv：成功，命中 14 篇
- medRxiv：成功，命中 8 篇

## 最值得看

### Foundation Model / Agent

- [LazySloth: Bounded LLM-based Lazy Tree Search for Fast Long Video Comprehension](http://arxiv.org/abs/2609.37426v1)
  来源：arXiv | 日期：2026-09-29 | 相关度：7.5 | 新颖度：7.29
  匹配主题：foundation_model_agent
  中文摘要：Modern vision-language models (VLMs) have shown promising results in long-video understanding due to the rich semantic information they can capture. However, most methods focus on coarse captioning of extracted image fra...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [M2Note: Continual Evolution of Vision Language Models via Mistake Notebook Learning](http://arxiv.org/abs/2607.00685v2)
  来源：arXiv | 日期：2026-07-01 | 相关度：7.5 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Vision Language Models (VLMs) have demonstrated remarkable capabilities in multimodal reasoning tasks, yet they still suffer from recurring failures, such as skipping key visual checks, misapplying domain rules, and hall...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Retrieve, Reproduce, Reveal: Dissecting Retrieval-Augmented Software Vulnerability Detection](http://arxiv.org/abs/2609.37669v1)
  来源：arXiv | 日期：2026-09-29 | 相关度：6.55 | 新颖度：8.3
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) is increasingly used to enhance Large Language Model (LLM)-based software vulnerability detection by grounding predictions in retrieved vulnerability knowledge, such as vulnerability ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 产品应用 / 监测落地

- [AI-Empowered Viral Metagenomics for Clinical Diagnosis: Advances, Bottlenecks, and Translational Pathways.](https://pubmed.ncbi.nlm.nih.gov/42809384/)
  来源：PubMed | 日期：2026-09-29 | 相关度：10.0 | 新颖度：5.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Viral metagenomics, leveraging high-throughput sequencing technologies, provides comprehensive, hypothesis-free characterization of viral communities in clinical specimens, establishing itself as a pivotal tool for clini...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 可追踪

### Foundation Model / Agent

- [Unifying Vision and Language: Benchmarking End to End Transformer Model Against the ClipCap Framework](https://www.medrxiv.org/content/10.64898/2026.09.24.26363914v1)
  来源：medRxiv | 日期：2026-09-27 | 相关度：8.5 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Background and purpose: Accurate identification of cardiac MRI volume orientations is essential for reliable image interpretation and for enabling downstream automated analysis pipelines. However, orientation labels and ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [GenoMorph: Pathway-Grounded Genomic Disease Reasoning via Adaptive Latent Computation](http://arxiv.org/abs/2609.34079v1)
  来源：arXiv | 日期：2026-09-28 | 相关度：8.5 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have demonstrated strong capabilities in biological reasoning; however, genomic disease inference remains largely dependent on memorized gene-disease associations rather than understanding bi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A ReAct Agentic AI System for Natural Language Querying and Statistical Analysis of The Cancer Genome Atlas Clinical Data](https://www.medrxiv.org/content/10.64898/2026.07.15.26358188v2)
  来源：medRxiv | 日期：2026-09-28 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：The Cancer Genome Atlas (TCGA) holds clinical data for over 11,000 patients across 33 cancer types, but access is hard because of complex file structures, heterogeneous formats, and the need for programming. We present a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [KUPAS MASTER: Distilling the Tacit Expertise of Master Practitioners into Agent-Ready Experience Corpora](http://arxiv.org/abs/2609.37673v1)
  来源：arXiv | 日期：2026-09-29 | 相关度：6.55 | 新颖度：7.3
  匹配主题：foundation_model_agent
  中文摘要：Experienced professionals know more than just facts and conclusions. They know which cues matter, why a judgment is reasonable, and which action to take. Routine work records often leave out this tacit knowledge, making ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Large language model-based bibliometric evaluation of population descriptors in human genetics](https://www.biorxiv.org/content/10.64898/2026.09.24.754051v1)
  来源：bioRxiv | 日期：2026-09-28 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：As the use of population descriptors such as race, ethnicity, and ancestry have become increasingly common in modern genetics research, there have been growing calls to critically examine their use. Most notably, in 2023...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [UltRAG: a Universal Simple Scalable Recipe for Knowledge Graph RAG](http://arxiv.org/abs/2603.28773v2)
  来源：arXiv | 日期：2026-01-28 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) frequently generate confident yet factually incorrect content when used for language generation (a phenomenon often known as hallucination). Retrieval augmented generation (RAG) tries to redu...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Is manual software optimization a thing of the past?](http://arxiv.org/abs/2609.37849v1)
  来源：arXiv | 日期：2026-09-29 | 相关度：5.75 | 新颖度：7.26
  匹配主题：foundation_model_agent
  中文摘要：Scientific software is increasingly required to process larger datasets while maintaining acceptable execution times. Software optimization traditionally requires substantial expertise in programming, algorithms, and num...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MERGE: Multi-LLM Ensemble for Retrieval via Generative Enrichment](http://arxiv.org/abs/2609.37574v1)
  来源：arXiv | 日期：2026-09-29 | 相关度：5.45 | 新颖度：7.17
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) are increasingly used to enrich user queries in information retrieval (IR) so that a standard retriever such as BM25 can bridge vocabulary gaps with the target corpus. Any single LLM, however...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ASCEND: Personal AI Agents for Autonomous Scientific Computing Across HPC Clusters and GPU Workstations](http://arxiv.org/abs/2609.32868v2)
  来源：arXiv | 日期：2026-09-26 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Traditional scientific computing requires researchers to translate computational intent into environment configuration, resource requests, and executable jobs, then diagnose failures from scheduler state and application ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Automated Simulation to Autonomous Discovery: A Hierarchical Framework for Agentic Computational Materials Science](http://arxiv.org/abs/2609.36469v1)
  来源：arXiv | 日期：2026-09-29 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：The convergence of large language models, materials-specific foundation models, and agentic artificial intelligence is reshaping the paradigm of computational materials discovery. While high-throughput computation, autom...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Lost in Conversation or Lost in Translation? Diagnosing Multi-Turn Degradation in RAG](http://arxiv.org/abs/2609.36700v1)
  来源：arXiv | 日期：2026-09-29 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：When conversing with large language models (LLMs), users often begin with a simple question and build towards a multi-hop question through follow-up turns. Retrieval-augmented generation (RAG) and its graph-based variant...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SIREN (Luring LLMs onto the Rocks): PAIR-Driven Preference Manipulation in Web-RAG Recommenders](http://arxiv.org/abs/2607.21951v3)
  来源：arXiv | 日期：2026-07-24 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：This paper investigates the adversarial manipulation of the ranked recommendations produced by web-augmented large language models (LLMs). When an LLM answers a recommendation query by retrieving and reading live webpage...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BRIDGE: Bilevel Retrieval-Credit-Aware Agentic Reinforcement Learning](http://arxiv.org/abs/2609.36505v1)
  来源：arXiv | 日期：2026-09-29 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Agentic reinforcement learning (ARL) with verifiable rewards improves the ability of large language models (LLMs) to tackle knowledge-intensive tasks by learning to interleave search and reasoning. However, most existing...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [A locally deployable agentic framework for clinical data deidentification](https://www.medrxiv.org/content/10.64898/2026.05.28.26353952v3)
  来源：medRxiv | 日期：2026-09-29 | 相关度：7.1 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Multimodal clinical data contain identifiers across diverse formats. We developed the Multimodal Anonymizer, a locally deployable framework combining multimodal language models, specialist networks, deterministic transfo...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Quantization Enables Private Dense Retrieval against Malicious Service Providers](http://arxiv.org/abs/2609.36376v1)
  来源：arXiv | 日期：2026-09-28 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Dense retrieval, the key component of Retrieval Augmented Generation (RAG), retrieves the most relevant documents by comparing dense vector representations of queries and passages from a large corpus. In privacy-sensitiv...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Certified Adaptive Refresh: Anytime-Valid Monitoring for Federated Conformal RAG](http://arxiv.org/abs/2605.29139v2)
  来源：arXiv | 日期：2026-05-27 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Question-answering services built on retrieval-augmented generation (RAG), in which a language model answers from retrieved documents, are inspected continuously and upgraded repeatedly, so their reliability guarantee mu...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Homo-RAG: Homology-Guided Retrieval-Augmented Generation for Cross-Species Gene Function Prediction](http://arxiv.org/abs/2608.25466v2)
  来源：arXiv | 日期：2026-08-26 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：The functional annotation of genes in non-model organisms remains a significant challenge in computational biology, with 20-70% of sequenced genes lacking characterized functions. Traditional homology-based methods are o...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RNASeek: A Cross-Phyla Generative Foundation Model for Multipurpose RNA Modeling and Reinforcement Learning-Based Design](https://www.biorxiv.org/content/10.64898/2026.09.24.754173v1)
  来源：bioRxiv | 日期：2026-09-28 | 相关度：7.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：RNA plays central roles in regulating information flow and provides a versatile substrate for engineering biological functions. While large language models (LLMs) have transformed natural language processing and protein ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Language as the Interface: Foundation-Model Contrastive Learning Links Transcriptomes and Electrophysiology](http://arxiv.org/abs/2609.37024v1)
  来源：arXiv | 日期：2026-09-29 | 相关度：7.1 | 新颖度：6.09
  匹配主题：foundation_model_agent
  中文摘要：Integrating transcriptomic and electrophysiological data is essential for building multimodal foundation models for neuroscience. Patch-seq provides paired measurements of gene expression and intrinsic electrophysiology ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A Safety-First Gateway Architecture for Trusted Public Health Resource Navigation](http://arxiv.org/abs/2607.13038v2)
  来源：arXiv | 日期：2026-06-11 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Conversational AI can improve access to public health information, but public-facing healthcare applications require safeguards against inappropriate medical guidance and unsupported generation. We present a Safety-First...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Genome-wide-scale prediction of compound-protein interactions using foundation and language models based on three-dimensional structures of compounds and proteins.](https://pubmed.ncbi.nlm.nih.gov/42803464/)
  来源：PubMed | 日期：2026-09-28 | 相关度：6.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：The identification of compound-protein interactions (CPIs) is crucial in the early stages of drug discovery. However, machine-learning (ML)-based methods based on one- and two-dimensional representations cannot capture i...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Bridging Semantic Gaps in RAG through Generated Context Knowledge Fusion](http://arxiv.org/abs/2609.37171v1)
  来源：arXiv | 日期：2026-09-29 | 相关度：5.45 | 新颖度：6.56
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation has established itself as a fundamental framework in natural language processing, seamlessly integrating information retrieval with the generative capabilities of large language models. How...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [TAEC: Trajectory-Aware Evidence Coordination for Multi-Step Visual RAG](http://arxiv.org/abs/2609.37349v1)
  来源：arXiv | 日期：2026-09-29 | 相关度：4.75 | 新颖度：6.19
  匹配主题：foundation_model_agent
  中文摘要：Multi-step visual retrieval-augmented generation (RAG) answers complex questions by repeatedly retrieving visual evidence, updating an intermediate state, and deciding whether to continue searching or answer. Yet retriev...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Byzantine-Robust Federated RAG via Aligned Calibration and Fixed-Membership Conformal Prediction](http://arxiv.org/abs/2609.33037v2)
  来源：arXiv | 日期：2026-09-27 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) lets language models answer questions more accurately by consulting relevant documents. Many valuable collections, such as medical records, cannot be pooled because of privacy rules. ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Assessing spoken discourse in aphasia using multimodal artificial intelligence](https://www.medrxiv.org/content/10.64898/2026.09.27.26364108v1)
  来源：medRxiv | 日期：2026-09-28 | 相关度：7.8 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Discourse analysis can reliably predict real-world communicative success, yet is rarely implemented clinically, due to challenges in manually generating stimulus-specific main concept inventories (MCIs) and scoring patie...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Transforming one health antimicrobial resistance surveillance in resource-limited countries (RLCs): From point-of-care diagnostics to AI-driven decision support.](https://pubmed.ncbi.nlm.nih.gov/42810525/)
  来源：PubMed | 日期：2026-09-29 | 相关度：5.95 | 新颖度：5.25
  匹配主题：pathogenomics, application_monitoring
  中文摘要：Antimicrobial resistance (AMR) is an emerging global problem, particularly for, resource-limited countries (RLCs) with limited capacity to diagnose diseases, inadequate surveillance systems, insufficient antimicrobial st...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [BadRAG: Identifying Vulnerabilities in Retrieval Augmented Generation of Large Language Models](http://arxiv.org/abs/2406.00083v3)
  来源：arXiv | 日期：2024-06-03 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) enhances Large Language Models (LLMs) by retrieving relevant information from external knowledge bases to provide more accurate, contextually informed, and up-to-date responses. Howev...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Active Hypothesis Testing under Computational Budgets](http://arxiv.org/abs/2512.01423v3)
  来源：arXiv | 日期：2025-12-01 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：In large-scale hypothesis testing, computing exact $p$-values or $e$-values is often resource-intensive, creating a need for budget-aware inferential methods. We propose a general framework for active hypothesis testing ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EHRAdapt: Adapting Pretrained Language Models to Electronic Health Records with Semantic Priors for Rare Clinical Events](http://arxiv.org/abs/2609.34007v1)
  来源：arXiv | 日期：2026-09-27 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Electronic health records (EHRs) encode clinical histories as (time, modality, code) tuples, whereas pretrained language models expect text tokens. Serializing them as text inflates sequence length and redundantly encode...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Systematic Survey of Agentic Skills: Architecture, Lifecycle, and Security](http://arxiv.org/abs/2608.29596v2)
  来源：arXiv | 日期：2026-08-30 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Autonomous large language model (LLM) agents increasingly face reliability, context consumption, and execution stability bottlenecks when deployed on complex, long-horizon tasks. While monolithic prompt engineering and s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Collaborative Principle Evolution via Evidence Transfer for Scientific Discovery](http://arxiv.org/abs/2609.35315v1)
  来源：arXiv | 日期：2026-09-28 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large Language Model (LLM)-based agents promise to automate scientific discovery, yet exploring the vast hypothesis space remains costly. Existing principle-evolution methods accelerate this loop, but operate sequentiall...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Comparative Evaluation of a System One Model and a General-Purpose Large Language Model on the Korean Physical Therapist Licensing Examination](https://www.medrxiv.org/content/10.64898/2026.09.26.26364067v1)
  来源：medRxiv | 日期：2026-09-28 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Background: System One Model is designed for structured decision-making and can provide probabilistic outputs, but their performance in domain-specific physical therapy tasks has not been established. Objective: To evalu...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Vision-language encoding models reveal an image-computable food-quality dimension in human occipitotemporal cortex](https://www.biorxiv.org/content/10.64898/2026.08.25.747006v2)
  来源：bioRxiv | 日期：2026-09-28 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Perceived calorie content contributes to neural representational structure in human ventral visual cortex, yet it remains unclear whether this reflects an abstract nutritional signal or whether perceived calorie is large...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A General Harness for Protein Foundation Model Fitness Prediction](http://arxiv.org/abs/2609.34654v1)
  来源：arXiv | 日期：2026-09-28 | 相关度：3.95 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Accurate fitness prediction is central to protein engineering and understanding sequence-function relationships. With advances in deep learning, protein foundation models (PFMs) have become widely used for this task. Rec...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multimodal deep learning-driven Raman spectroscopy for rapid identification of closely related pathogenic Bacillus species.](https://pubmed.ncbi.nlm.nih.gov/42810038/)
  来源：PubMed | 日期：2026-09-27 | 相关度：3.5 | 新颖度：6.0
  匹配主题：foundation_model_agent, application_monitoring
  中文摘要：Rapid and fine-grained identification of closely related pathogenic Bacillus species is a critical challenge in optical biosensing and biomolecular spectroscopy, hindered by their highly similar biochemical compositions ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LabFactory: Building and Evaluating Executable AI Labs](http://arxiv.org/abs/2609.28697v2)
  来源：arXiv | 日期：2026-09-23 | 相关度：3.1 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Scientific tasks specify a desired capability, but realizing it often requires building a computational system tailored to the task---acquiring data, designing representations, training models, implementing tools, and de...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OmniVCBench: Benchmarking Evidence-Grounded Multimodal Reasoning Towards AI Virtual Cells](http://arxiv.org/abs/2609.37773v1)
  来源：arXiv | 日期：2026-09-29 | 相关度：2.75 | 新颖度：7.43
  匹配主题：foundation_model_agent
  中文摘要：Artificial Intelligence Virtual Cells (AIVCs) are envisioned as scientific agents that simulate cellular responses, explain underlying mechanisms, and support hypothesis-driven discovery. Existing AIVC benchmarks, howeve...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic Graph Retrieval-Augmented Generation for Auditable Commercial Registry Analysis](http://arxiv.org/abs/2605.18770v3)
  来源：arXiv | 日期：2026-04-15 | 相关度：2.05 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Public commercial registries are formally open, yet their practical analysis remains difficult because relevant facts are scattered across millions of records that combine structured metadata, multilingual legal notices,...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ARCagent: An Adaptive Retrieval Calibration Agent for Clinical Question Answering](http://arxiv.org/abs/2609.36392v1)
  来源：arXiv | 日期：2026-09-28 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：In diseases where clinical guidelines are incomplete, contested, or mutually contradictory, knowledge completeness and dynamic conflict-aware synthesis are two safety-critical properties that standard Retrieval-Augmented...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Jet-Long: Efficient Long-Context Extension with Dynamic Bifocal RoPE](http://arxiv.org/abs/2607.07740v4)
  来源：arXiv | 日期：2026-07-08 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Modern LLMs are increasingly deployed in long-context applications such as retrieval-augmented generation, repository-level coding, and agentic workflows whose accumulated reasoning and tool traces routinely push the inp...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Grounded Revision vs. Prior Injection: Probing Retrieval-Augmented Patent Claim Amendment](http://arxiv.org/abs/2609.36550v1)
  来源：arXiv | 日期：2026-09-29 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation is widely used in professional writing, yet whether retrieval grounds revision or merely injects templates is rarely tested where "correct" has a definable meaning. Patent claim amendment s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EvoSCM: Scientific Belief Revision Through Causal Model Evolution and Experimentation](http://arxiv.org/abs/2609.01526v2)
  来源：arXiv | 日期：2026-09-01 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Scientific discovery depends on the ability to form hypotheses, test them through experiments, and revise them when evidence disagrees. Existing LLM agents support this process by improving their reasoning or actions, bu...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [HERO: Histology Encoder for Robust Representation in Oncology](http://arxiv.org/abs/2609.35943v1)
  来源：arXiv | 日期：2026-09-28 | 相关度：1.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Foundation models trained on large pathology image corpora now provide strong, transferable representations for computational pathology. Over the past few years a series of such models has been released, each trained on ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [PILLAR: Private Inverted-Index Lexical Lookup for Augmented Retrieval](http://arxiv.org/abs/2609.36326v1)
  来源：arXiv | 日期：2026-09-28 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) hands the user's query to whoever hosts the corpus. We propose PILLAR, a Privacy-Preserving RAG (PPRAG) system based on Private Information Retrieval (PIR) in which a client utilizes ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [DISCERN: Can AI Agents Work Like Scientists and Guide Discovery?](http://arxiv.org/abs/2609.33357v1)
  来源：arXiv | 日期：2026-09-27 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Reliable automated research requires agents to vet data, verify analyses, and generate hypotheses grounded in trustworthy evidence, potentially reducing routine scientific workload while allowing scientists to focus on i...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [MechBench: Can AI Scientific Agents Discover Mechanisms Beyond Phenomenal Laws?](http://arxiv.org/abs/2609.35515v1)
  来源：arXiv | 日期：2026-09-28 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Scientific discovery requires not only recovering mathematical laws that describe observable behavior, but also identifying the mechanisms that generate them. Existing benchmarks for symbolic regression and scientific ag...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [One Sequence, Many Decodings: CAGenMol-2 Recasts Drug Design as Masked Molecular Inference](http://arxiv.org/abs/2609.34301v1)
  来源：arXiv | 日期：2026-09-28 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Drug design couples property evaluation, conditional generation, structure-based design, and local optimization, yet machine learning systems typically address these capabilities with separate task-specific models. We in...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [NeSyFS: A Neuro-symbolic Fast-Slow Thinking Framework for LLM Agent under Partial Observability](http://arxiv.org/abs/2607.28942v3)
  来源：arXiv | 日期：2026-07-31 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Recently Large Language Models (LLMs) have been increasingly deployed as autonomous agents in applications such as self-reflection, retrieval-augmented generation, and scientific discovery. In these settings, agents must...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Reinforcing Agentic Creativity in Scientific Ideation with Night Science](http://arxiv.org/abs/2609.35706v1)
  来源：arXiv | 日期：2026-09-28 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) excel at structured, verifiable tasks, but their low-entropy bias can produce homogeneous and predictable outputs, limiting their utility for open-ended scientific ideation. Effective discove...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Human-in-the-loop machine learning with community engagement reduces title, abstract and full-text screening workload in knowledge synthesis.](https://pubmed.ncbi.nlm.nih.gov/42805514/)
  来源：PubMed | 日期：2026-09-28 | 相关度：2.45 | 新颖度：0.25
  匹配主题：application_monitoring
  中文摘要：Manual screening of titles, abstracts, and full texts for large-volume knowledge synthesis requires significant time investment. Machine-assisted tools offer solutions for facilitating screening. Most applications to dat...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Targeted finetuning enables co-folding models to learn ligand-induced protein conformational states](https://www.biorxiv.org/content/10.64898/2026.09.21.752570v1)
  来源：bioRxiv | 日期：2026-09-27 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Advances in protein structure prediction have enabled all-atom protein-ligand co-folding models that predict bound conformations directly from sequence and small-molecule structure. However, these models often fail to ge...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Towards Semi-Automatically Comparing Keyword-Based and Semantic Search Accuracy](http://arxiv.org/abs/2609.37749v1)
  来源：arXiv | 日期：2026-09-29 | 相关度：1.4 | 新颖度：7.4
  匹配主题：未命中具体主题
  中文摘要：The increasing importance of Information Retrieval (IR) in managing large datasets has highlighted significant limitations in traditional keyword-based search systems. Context-aware chat-based search methods, such as Ret...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Microfluidic approaches to next- generation sequencing library preparation: innovations, clinical integration and point-of-care settings.](https://pubmed.ncbi.nlm.nih.gov/42802333/)
  来源：PubMed | 日期：2026-09-27 | 相关度：4.65 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Next-generation sequencing (NGS) has revolutionized genomics by enabling high-throughput, cost-effective analysis of nucleic acids for both research and clinical applications. Library preparation remains a bottleneck in ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [More Features Are Not More Evidence: Limits of Training-Free Human Activity Recognition with Jev](http://arxiv.org/abs/2609.36154v1)
  来源：arXiv | 日期：2026-09-28 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：General-purpose models promise sensor-based decisions without training a task-specific classifier, which could reduce the dependence of Human Activity Recognition (HAR) on labeled data. Yet it remains unclear whether suc...
  为什么值得看：More Features Are Not More Evidence: Lim 与你的主题有弱匹配，暂时保留作低优先级跟踪。
