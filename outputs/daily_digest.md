# 每日论文监控日报 (2026-09-05)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 35 篇新论文。

## 抓取状态

- arXiv：成功，命中 34 篇
- PubMed：成功，命中 50 篇
- bioRxiv：成功，命中 11 篇
- medRxiv：成功，命中 11 篇

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [Generative large language models in medicine: a scoping review of recent methodological advances.](https://pubmed.ncbi.nlm.nih.gov/42686940/)
  来源：PubMed | 日期：2026-09-02 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Generative large language models (LLMs) are rapidly transforming medicine, demonstrating unprecedented capability across a broad spectrum of clinical and biomedical tasks. While prior literature has extensively investiga...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Benchmarking ten frontier large language models on 1,477 board style multiple choice questions in hematology](https://www.medrxiv.org/content/10.64898/2026.09.01.26361881v1)
  来源：medRxiv | 日期：2026-09-02 | 相关度：7.1 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) are increasingly used by clinicians and patients for medical queries, yet their accuracy and safety at the specialist level in hematology remain insufficiently characterised. We benchmarked t...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Cost and Accuracy of Long-Term Memory in Distributed Multi-Agent Systems Based on Large Language Models](http://arxiv.org/abs/2601.07978v5)
  来源：arXiv | 日期：2026-01-12 | 相关度：6.55 | 新颖度：1.7
  匹配主题：foundation_model_agent
  中文摘要：Long-term memory (LTM) is fundamental to large language model (LLM)-based agents in the emerging Internet of Agents (IoA), where distributed multi-agent systems (DMAS) span cloud and edge networks. Existing evaluations a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LLM4Log: A Systematic Review of Large Language Model-based Log Analysis](http://arxiv.org/abs/2604.16359v3)
  来源：arXiv | 日期：2026-03-18 | 相关度：6.55 | 新颖度：1.7
  匹配主题：foundation_model_agent
  中文摘要：Software systems generate massive, evolving, semi-structured logs that are central to reliability engineering and AIOps, yet difficult to analyze at scale under drift and limited labels. Recent advances in pretrained Tra...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evaluating Large Language Models as Tools to Navigate Researchers in Rapidly Evolving Research Landscapes: A Case Study in Cancer Drug Response Prediction](https://www.biorxiv.org/content/10.64898/2026.09.02.748827v1)
  来源：bioRxiv | 日期：2026-09-03 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have emerged as promising tools for assisting researchers in automating and accelerating the synthesis of literature reviews. However, their reliability is a significant concern due to issues...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Citation reliability of frontier large language models in medical writing and its automated verification](https://www.medrxiv.org/content/10.64898/2026.08.31.26361806v1)
  来源：medRxiv | 日期：2026-09-04 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly used to draft medical manuscripts, yet their citations are unreliable and clinicians lack a validated way to verify them. We evaluated three frontier LLMs, Claude Opus 4.8, G...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [STAIR (STructure Aware Information Retriever): A novel dataset and LLM based retriever for document structure augmentation](http://arxiv.org/abs/2609.03874v1)
  来源：arXiv | 日期：2026-09-03 | 相关度：6.55 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval Augmented Generation (RAG) is a key component for generating accurate and hallucination free answers using Large Language Models (LLMs). LLMs are improving at handling long context, but still suffer from "lost ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [DuaDeep-SeqAffinity: Dual-Branch Deep Learning for Tri-Stream Sequence-Based Antibody--Antigen Affinity Prediction](http://arxiv.org/abs/2512.22007v2)
  来源：arXiv | 日期：2025-12-26 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：DuaDeep-SeqAffinity is a sequence-only deep learning framework that predicts antibody--antigen binding affinity directly from primary amino acid sequences, avoiding the cost and scarcity of resolved three-dimensional str...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [Using Large Language Models for Legal Decision-Making in Austrian Value-Added Tax Law: A Comparative Study](http://arxiv.org/abs/2507.08468v2)
  来源：arXiv | 日期：2025-07-11 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：This paper provides an experimental evaluation of the capability of large language models (LLMs) to assist in legal decision-making within the framework of Austrian and European Union value-added tax (VAT) law. In tax co...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [When Retrieval Helps: Selective Retrieval for Single-Turn Mental-Health QA](http://arxiv.org/abs/2609.03454v1)
  来源：arXiv | 日期：2026-09-03 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) can improve the specificity and grounding of large language model responses, but its effect is not uniformly beneficial in single-turn mental-health question answering, where user que...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents](http://arxiv.org/abs/2609.00065v2)
  来源：arXiv | 日期：2026-08-30 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：A language-model agent asked to analyse an experiment will usually return working code. Whether the analysis is defensible is a different question. A defensible analysis depends on procedural choices: which test the fiel...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Language-encoded network topology enables large language models to reason about complex networks](http://arxiv.org/abs/2609.03229v1)
  来源：arXiv | 日期：2026-09-03 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Networks describe systems in biology and beyond, from protein interactions and social relationships to power grids and citation records. Reasoning about such systems requires understanding their structure: which elements...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TC-RAG:Turing-Complete RAG's Case study on Medical LLM Systems](http://arxiv.org/abs/2408.09199v3)
  来源：arXiv | 日期：2024-08-17 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：In the pursuit of enhancing domain-specific Large Language Models (LLMs), Retrieval-Augmented Generation (RAG) emerges as a promising solution to mitigate issues such as hallucinations, outdated knowledge, and limited ex...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [In Search of Ethical Procedures for LLM-Assisted Systematic Review Production: A Proof-of-Concept Evaluation of Selected Review Components](https://www.medrxiv.org/content/10.64898/2026.02.18.26346559v2)
  来源：medRxiv | 日期：2026-09-02 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly used in scientific writing, but the conditions under which they can be applied responsibly to evidence synthesis remain poorly defined. We conducted a proof-of-concept study ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Improving Health Literacy through Lay Summarization of Radiological Reports: An Evaluation of BioNER and Retrieval-Augmented Generation](http://arxiv.org/abs/2609.02396v1)
  来源：arXiv | 日期：2026-09-02 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Radiology reports are written primarily for clinicians, and their specialized terminology often makes them difficult for patients to interpret. As a result, many patients turn to publicly available Large Language Models ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Visionary Look at Vibe Researching](http://arxiv.org/abs/2604.00945v2)
  来源：arXiv | 日期：2026-04-01 | 相关度：2.1 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Vibe researching is an emerging paradigm in which human researchers provide high-level direction and critical judgment while LLM-based agents handle the labor-intensive execution of literature review, experimentation, da...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [How AI Can Advance Mathematical Biology: Opportunities, Challenges, and Future Directions.](https://pubmed.ncbi.nlm.nih.gov/42693360/)
  来源：PubMed | 日期：2026-09-03 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Mathematical biology has long relied on mechanistic models, including ordinary and partial differential equations, stochastic systems, and agent-based models, to study biological processes across scales. These approaches...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PACMS: Submodular Context Selection as a Pluggable Engine for LLM Agents](http://arxiv.org/abs/2606.20047v2)
  来源：arXiv | 日期：2026-06-18 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Conversational and tool-using LLM agents operate over a context window that fills from several directions simultaneously. As a session proceeds, the agent accumulates user and assistant turns, entries drawn from a persis...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OpenCosmo: Community Portal and Analysis Framework for Flagship Cosmological Simulations](http://arxiv.org/abs/2607.16059v5)
  来源：arXiv | 日期：2026-07-17 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Cosmology is a precision observational science, and large simulations are necessary components of many analyses. These simulations are computationally expensive and produce massive, complex datasets; sharing them widely ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CodePoisonRAG: Knowledge Poisoning Attacks on Retrieval-Augmented Code Generation](http://arxiv.org/abs/2609.02774v1)
  来源：arXiv | 日期：2026-09-02 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Code Generation (RACG) improves LLM-based software development by retrieving external code artifacts, documentation, and patches, and incorporating them into the generation context. This reliance on e...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Spruce: Scalable Private Outsourced Retrieval Using Compact Embeddings](http://arxiv.org/abs/2609.03376v1)
  来源：arXiv | 日期：2026-09-03 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) has made dense retrieval over large document collections a standard building block. Organizations increasingly outsource vector indexes to untrusted clouds, exposing proprietary corpo...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [GRASP: Graph-Retrieval Automated Scoring Pipeline for Label-Free Multi-Topic Essay Grading](http://arxiv.org/abs/2609.03857v1)
  来源：arXiv | 日期：2026-09-03 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Automated short-answer grading research has historically focused on exams consisting solely of questions pertaining to a single topic. Automatic grading of exams containing questions about more than one topic remains les...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Causal-Counterfactual RAG: The Integration of Causal-Counterfactual Reasoning into RAG](http://arxiv.org/abs/2509.14435v3)
  来源：arXiv | 日期：2025-09-17 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have transformed natural language processing (NLP), enabling diverse applications by integrating large-scale pre-trained knowledge. However, their static knowledge limits dynamic reasoning ov...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Language-Guided Hypotheses Generation for Sparse SMEFT Analyses](http://arxiv.org/abs/2608.04100v2)
  来源：arXiv | 日期：2026-08-04 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Global fits of the Standard Model Effective Field Theory are challenged by the large number of operators, while any given database constrains only a small subset. Selecting relevant operator hypotheses therefore requires...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ViSAR: Training-Free Adaptive-$k$ Retrieval for Visual Document Question Answering](http://arxiv.org/abs/2609.02486v2)
  来源：arXiv | 日期：2026-09-02 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Document Visual Question Answering (DocVQA) often leverages Retrieval-Augmented Generation (RAG), where late-interaction encoders are commonly used to identify document pages relevant to a user query, before answer gener...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Invoice Haystack: Benchmarking Document Retrieval and Visual Question Answering Under Strong Visual Homogeneity](http://arxiv.org/abs/2606.25343v3)
  来源：arXiv | 日期：2026-06-24 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Vision Language Models have achieved near-human performance on single-document Visual Question Answering, yet their effectiveness degrades significantly when retrieving information from large collections of visually homo...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [NE-R1: Enhancing Named Entity Recognition Model via Reinforcement Learning](http://arxiv.org/abs/2609.02366v1)
  来源：arXiv | 日期：2026-09-02 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Named Entity Recognition (NER) has achieved substantial progress since the advent of large language models (LLMs). Nevertheless, the recognition of long-tail and domain-specific entities remains challenging due to the de...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Large Language Models (LLMs) for Telecom Root Cause Analysis (RCA): A Structured Reasoning Framework for Evidence-Grounded Diagnosis](http://arxiv.org/abs/2609.02805v1)
  来源：arXiv | 日期：2026-09-02 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Root cause analysis (RCA) is a critical task in telecom network operations, but diagnosing performance degradations in modern 5G and emerging 6G networks remains challenging due to complex cross-layer dependencies. While...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Compression Sequencing enables ultra-sensitive and scalable scRNA-seq](https://www.biorxiv.org/content/10.64898/2026.09.01.748706v1)
  来源：bioRxiv | 日期：2026-09-03 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Current sequencing methods are inefficient and bottlenecked by repeated sampling of highly abundant molecules, which dominate sequencing reads, limit assay throughput and sensitivity for rare targets. For example, single...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Rent-a-RAG: Embedding-Space Watermarks for Auditing Third-Party RAG](http://arxiv.org/abs/2609.03749v1)
  来源：arXiv | 日期：2026-09-03 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Third-party retrieval-augmented generation (RAG) marketplaces create a new auditing problem: data providers may license corpora to a RAG operator, yet later have no visibility into whether their documents are being reuse...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ICEGR: An Intent-Coherent End-to-End Generative Retrieval Framework for E-commerce Search](http://arxiv.org/abs/2608.29652v2)
  来源：arXiv | 日期：2026-08-30 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Generative Retrieval (GR) is promising for e-commerce search, yet existing methods struggle to maintain query-intent consistency throughout the training pipeline. First, semantic ID (SID) construction based on static pro...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SpecXMaster Technical Report](http://arxiv.org/abs/2603.23101v4)
  来源：arXiv | 日期：2026-03-24 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Intelligent spectroscopy serves as a pivotal element in AI-driven closed-loop scientific discovery, functioning as the critical bridge between matter structure and artificial intelligence. However, conventional expert-de...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RATL: Learning from Retrieved Residuals for Robust Multivariate Time-Series Forecasting](http://arxiv.org/abs/2609.03937v1)
  来源：arXiv | 日期：2026-09-03 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) complements parametric models with retrieved external evidence. The same idea is attractive for continuous-output regression, but directly reusing retrieved target values is often not...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Decoding cancer with artificial intelligence: Transforming research, diagnosis, and therapy with future insights.](https://pubmed.ncbi.nlm.nih.gov/42685611/)
  来源：PubMed | 日期：2026-09-02 | 相关度：3.75 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Cancer remains one of the leading global health burdens, with increasing complexity in genomic, imaging, and clinical datasets presenting significant challenges for effective management. Artificial intelligence (AI) has ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [A Knowledge-Enhanced Multimodal Framework with Genomic Reconstruction for DLBCL Drug Response Prediction.](https://pubmed.ncbi.nlm.nih.gov/42688326/)
  来源：PubMed | 日期：2026-01-01 | 相关度：3.05 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Diffuse large B-cell lymphoma (DLBCL) exhibits substantial biological heterogeneity, leading to pronounced variability in patient response to therapy. Accurate drug response prediction is therefore critical for precision...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
