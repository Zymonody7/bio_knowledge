# 每日论文监控日报 (2026-09-06)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 22 篇新论文。

## 抓取状态

- arXiv：成功，命中 16 篇
- PubMed：成功，命中 30 篇
- bioRxiv：成功，命中 13 篇
- medRxiv：成功，命中 6 篇

## 最值得看

### Foundation Model / Agent

- [Pneumonia Detection in Paediatric Chest X-Rays using Ensembled Large Language Models](https://www.medrxiv.org/content/10.64898/2026.04.10.26347909v2)
  来源：medRxiv | 日期：2026-09-05 | 相关度：7.8 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Background: Paediatric pneumonia is a major cause of childhood morbidity and mortality. Chest X-rays (CXR) are central to diagnosis, but shortages of specialist radiologists can delay reporting. Multimodal large language...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [MARLA: An Autonomous Agent for Medical AI Research and Development](https://www.medrxiv.org/content/10.64898/2026.08.21.26361049v2)
  来源：medRxiv | 日期：2026-09-05 | 相关度：8.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Medical AI models have made a great impact on biomedical research and real-world clinical applications, but conducting interdisciplinary medical AI research remains challenging, requiring close collaboration between clin...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AI semantics for biomedical data integration](https://www.biorxiv.org/content/10.64898/2026.08.03.742514v2)
  来源：bioRxiv | 日期：2026-09-03 | 相关度：7.9 | 新颖度：1.2
  匹配主题：foundation_model_agent
  中文摘要：Researchers increasingly need to explore hypotheses that span multimodal data across different scales, organisms, and domains. In practice, this requires connecting knowledge across fragmented databases with incompatible...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Cost and Accuracy of Long-Term Memory in Distributed Multi-Agent Systems Based on Large Language Models](http://arxiv.org/abs/2601.07978v5)
  来源：arXiv | 日期：2026-01-12 | 相关度：6.55 | 新颖度：1.7
  匹配主题：foundation_model_agent
  中文摘要：Long-term memory (LTM) is fundamental to large language model (LLM)-based agents in the emerging Internet of Agents (IoA), where distributed multi-agent systems (DMAS) span cloud and edge networks. Existing evaluations a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [STAIR (STructure Aware Information Retriever): A novel dataset and LLM based retriever for document structure augmentation](http://arxiv.org/abs/2609.03874v1)
  来源：arXiv | 日期：2026-09-03 | 相关度：6.55 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval Augmented Generation (RAG) is a key component for generating accurate and hallucination free answers using Large Language Models (LLMs). LLMs are improving at handling long context, but still suffer from "lost ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [De novo design of ligand binding proteins using large language models alone](https://www.biorxiv.org/content/10.64898/2026.09.02.748987v1)
  来源：bioRxiv | 日期：2026-09-03 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Protein design has rapidly advanced with the advent of sequence- and structure-based machine learning models. However, reasoned design, which applies physicochemical principles and rules derived from sequence-structure-f...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [DuaDeep-SeqAffinity: Dual-Branch Deep Learning for Tri-Stream Sequence-Based Antibody--Antigen Affinity Prediction](http://arxiv.org/abs/2512.22007v2)
  来源：arXiv | 日期：2025-12-26 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：DuaDeep-SeqAffinity is a sequence-only deep learning framework that predicts antibody--antigen binding affinity directly from primary amino acid sequences, avoiding the cost and scarcity of resolved three-dimensional str...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Human-like meaning maps from single-prompt VLM ratings of local scene meaning](https://www.biorxiv.org/content/10.64898/2026.08.30.748100v1)
  来源：bioRxiv | 日期：2026-09-03 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Visual attention is shaped both by low-level perceptual features and by the semantic properties of scene regions. However, compared to the salience of low-level image features, the characterization of image properties th...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [When Retrieval Helps: Selective Retrieval for Single-Turn Mental-Health QA](http://arxiv.org/abs/2609.03454v1)
  来源：arXiv | 日期：2026-09-03 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) can improve the specificity and grounding of large language model responses, but its effect is not uniformly beneficial in single-turn mental-health question answering, where user que...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TC-RAG:Turing-Complete RAG's Case study on Medical LLM Systems](http://arxiv.org/abs/2408.09199v3)
  来源：arXiv | 日期：2024-08-17 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：In the pursuit of enhancing domain-specific Large Language Models (LLMs), Retrieval-Augmented Generation (RAG) emerges as a promising solution to mitigate issues such as hallucinations, outdated knowledge, and limited ex...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evaluating Large Language Models as Tools to Navigate Researchers in Rapidly Evolving Research Landscapes: A Case Study in Cancer Drug Response Prediction](https://www.biorxiv.org/content/10.64898/2026.09.02.748827v1)
  来源：bioRxiv | 日期：2026-09-03 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have emerged as promising tools for assisting researchers in automating and accelerating the synthesis of literature reviews. However, their reliability is a significant concern due to issues...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Citation reliability of frontier large language models in medical writing and its automated verification](https://www.medrxiv.org/content/10.64898/2026.08.31.26361806v1)
  来源：medRxiv | 日期：2026-09-04 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly used to draft medical manuscripts, yet their citations are unreliable and clinicians lack a validated way to verify them. We evaluated three frontier LLMs, Claude Opus 4.8, G...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [How AI Can Advance Mathematical Biology: Opportunities, Challenges, and Future Directions.](https://pubmed.ncbi.nlm.nih.gov/42693360/)
  来源：PubMed | 日期：2026-09-03 | 相关度：1.7 | 新颖度：0.25
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

- [Rent-a-RAG: Embedding-Space Watermarks for Auditing Third-Party RAG](http://arxiv.org/abs/2609.03749v1)
  来源：arXiv | 日期：2026-09-03 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Third-party retrieval-augmented generation (RAG) marketplaces create a new auditing problem: data providers may license corpora to a RAG operator, yet later have no visibility into whether their documents are being reuse...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Compression Sequencing enables ultra-sensitive and scalable scRNA-seq](https://www.biorxiv.org/content/10.64898/2026.09.01.748706v1)
  来源：bioRxiv | 日期：2026-09-03 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Current sequencing methods are inefficient and bottlenecked by repeated sampling of highly abundant molecules, which dominate sequencing reads, limit assay throughput and sensitivity for rare targets. For example, single...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RATL: Learning from Retrieved Residuals for Robust Multivariate Time-Series Forecasting](http://arxiv.org/abs/2609.03937v1)
  来源：arXiv | 日期：2026-09-03 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) complements parametric models with retrieved external evidence. The same idea is attractive for continuous-output regression, but directly reusing retrieved target values is often not...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。
