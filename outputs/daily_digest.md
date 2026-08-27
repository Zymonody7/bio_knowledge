# 每日论文监控日报 (2026-08-27)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 43 篇新论文。

## 抓取状态

- arXiv：成功，命中 51 篇
- PubMed：成功，命中 42 篇
- bioRxiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='api.biorxiv.org', port=443): Max retries exceeded with url: /details/biorxiv/2026-08-24/2026-08-27/0 (Caused by Ne...
- medRxiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='api.biorxiv.org', port=443): Max retries exceeded with url: /details/medrxiv/2026-08-24/2026-08-27/0 (Caused by Ne...

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [MLLMCLIP: Feature-Level Distillation of MLLM for Robust Vision-Language Representations](http://arxiv.org/abs/2608.25575v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：7.9 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Pretrained vision-language models such as CLIP excel at zero-shot recognition but often fail at compositionality, particularly attribute-object and relational structures. Recent studies mitigate this issue by augmenting ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Recurrence Meets Transformers for Universal Multimodal Retrieval](http://arxiv.org/abs/2509.08897v2)
  来源：arXiv | 日期：2025-09-10 | 相关度：7.5 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：With the rapid advancement of multimodal retrieval and its application in LLMs and multimodal LLMs, increasingly complex retrieval tasks have emerged. Existing methods predominantly rely on task-specific fine-tuning of v...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [Federation Is Nearly Free, Reasoning Is Not: Tradeoffs for AI Co-Scientists in Protein Characterization Workflows](http://arxiv.org/abs/2608.25215v1)
  来源：arXiv | 日期：2026-08-25 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Natural language driven autonomous co-scientist workflows involve a fundamental trade-off between flexibility and reasoning at the expense of determinism, reproducibility, and observability. Such agents increasingly must...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ProgRouter: Online Progress-Guided Orchestration for Multi-Agent LLM Workflows under Quality-Cost Tradeoffs](http://arxiv.org/abs/2608.25992v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：6.55 | 新颖度：6.92
  匹配主题：foundation_model_agent
  中文摘要：Multi-agent large language model (LLM) workflows have emerged as a powerful paradigm for solving complex, open-ended tasks through collaborative reasoning among specialized LLM agents, but they incur substantial operatin...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Automating Parent Selection Configuration in Genetic Programming with Agentic AI](http://arxiv.org/abs/2608.17172v2)
  来源：arXiv | 日期：2026-08-17 | 相关度：6.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：We investigate whether agentic artificial intelligence can automate parts of the process of designing genetic programming systems by introducing an agentic framework that identifies and implements parent selection algori...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Comparative Evaluation of Digitization Pipelines for Historiographical Sources](http://arxiv.org/abs/2608.24976v1)
  来源：arXiv | 日期：2026-08-25 | 相关度：6.55 | 新颖度：6.2
  匹配主题：foundation_model_agent
  中文摘要：Purpose: The digitization of historical documents presents fundamental challenges for modern information retrieval and Artificial Intelligence (AI) systems. Optical character recognition (OCR) errors in source corpora pr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Layered Security Framework Against Prompt Injection in RAG-Based Chatbots](http://arxiv.org/abs/2606.19660v2)
  来源：arXiv | 日期：2026-06-17 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Prompt injection is ranked as the most critical vulnerability in large language model (LLM) deployments by the OWASP Top 10 for LLM Applications, yet existing defenses operate at isolated pipeline stages and remain incom...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Retrieval-Augmented Agentic Rubric Generation for Reliable Medical Response Evaluation](http://arxiv.org/abs/2601.15161v3)
  来源：arXiv | 日期：2026-01-21 | 相关度：6.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) are increasingly used for clinical decision support, where hallucinations and unsafe suggestions may pose direct risks to patient safety. These risks are hard to assess: subtle clinical error...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HypoForge: A Self-Improving Multi-Agent Framework for Automated Hypothesis Generation and Testing via Scientific Skill Learning](http://arxiv.org/abs/2608.25770v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：6.15 | 新颖度：7.1
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have enabled AI scientist systems to automate scientific discovery, yet existing approaches most rely on static prompting or fixed workflows and fail to accumulate experience for continual im...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The Performance of Large Language Models in Extracting Intestinal Symptoms From Electronic Health Records: Retrospective Observational Study.](https://pubmed.ncbi.nlm.nih.gov/42647073/)
  来源：PubMed | 日期：2026-08-26 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Unstructured electronic health records (EHRs) hinder the monitoring of intestinal infections. Large language models (LLMs) enable automated symptom extraction. However, their clinical validation is limited by a lack of s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TAU-Agent: An Agentic Retrieval-Augmented Framework for Traffic Anomaly Understanding](http://arxiv.org/abs/2608.25935v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：5.45 | 新颖度：6.78
  匹配主题：foundation_model_agent
  中文摘要：Traffic Anomaly Understanding (TAU) requires models and systems to detect, reason about, and explain anomalous events in transportation videos. To address this challenge, we propose TAU-Agent, an agentic retrieval-augmen...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Graph Engineering in the Era of LLM Agents: From Individual Intelligence to System Intelligence](http://arxiv.org/abs/2608.21156v2)
  来源：arXiv | 日期：2026-08-21 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：LLMs have evolved from language generators to autonomous agents capable of complex, long-horizon tasks. This evolution has produced paradigms including Prompt Engineering to elicit model capabilities, Context Engineering...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [When RAG Fails to Equalize: Geo-bias in Factual Question Answering over Public Companies](http://arxiv.org/abs/2608.25717v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：4.75 | 新颖度：5.99
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) is widely assumed to mitigate factual errors in large language models (LLMs), but it remains unclear whether retrieval uniformly compensates for missing knowledge. We study this quest...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Retrieved But Not Reliable: A Survey on Attacks, and Defenses in Retrieval-Augmented Generation](http://arxiv.org/abs/2608.24977v1)
  来源：arXiv | 日期：2026-08-25 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) enhances large language models by grounding outputs in external knowledge, improving factuality and reducing hallucinations. At the same time, the retrieval-augmented pipeline introdu...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [SelfGraphRAG: Bridging the Supervision Gap in Graph-Based RAG with Synthetic QA Generation](http://arxiv.org/abs/2608.25123v1)
  来源：arXiv | 日期：2026-08-25 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) improves large language models by incorporating external knowledge without retraining, but existing methods often underuse the relational structure encoded in knowledge graphs. Graph-...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Homo-RAG: Homology-Guided Retrieval-Augmented Generation for Cross-Species Gene Function Prediction](http://arxiv.org/abs/2608.25466v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：The functional annotation of genes in non-model organisms remains a significant challenge in computational biology, with 20-70% of sequenced genes lacking characterized functions. Traditional homology-based methods are o...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Unlocking Multimodal Protein Language Models at Inference Time](http://arxiv.org/abs/2608.25855v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：7.1 | 新颖度：5.81
  匹配主题：foundation_model_agent
  中文摘要：Multimodal protein language models (pLMs) learn joint protein sequence-structure distributions, and their generation performance should also depend critically on inference-time sampling strategies. Yet prior work has foc...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Multi-Granularity Context-Enhanced RAG over Multimodal Knowledge Graphs](http://arxiv.org/abs/2608.25986v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：6.8 | 新颖度：6.91
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) is widely used to mitigate hallucination issues in large language models (LLMs) and multimodal large language models (MLLMs). In particular, knowledge graph (KG)-based RAG leverages s...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [OmicSync: Reliability-Aware Spatial Multi-Omics Clustering with Evidence-Constrained LLM Reasoning](http://arxiv.org/abs/2608.22785v2)
  来源：arXiv | 日期：2026-08-24 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Spatial multi-omics technologies jointly profile gene expression, surface proteins, and histology at each tissue spot, yet most spatial domain discovery methods provide only cluster assignments, without indicating assign...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Interpreting Protein Language Model Embeddings via Orthogonal Projection for Protein Fitness Prediction](http://arxiv.org/abs/2608.25548v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Recently, there has been a growing adoption of protein language models (PLMs) in biomedical science. Their embeddings provide a rich numerical representation of protein sequences which achieve state-of-the-art performanc...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Interpretable physics-informed retrieval-augmented generation language model for end-to-end inorganic crystal synthesis planning](http://arxiv.org/abs/2608.25392v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Synthesis planning for inorganic materials requires predicting both synthesizability and viable routes by linking microscopic thermodynamic stability with macroscopic synthesis methods, precursors, and processing conditi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ReliableRAG: Combating Misinformation in Retrieval-Augmented Generation via Reliability-Guided Reasoning Chains](http://arxiv.org/abs/2608.25487v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) has emerged as a powerful architecture for Question Answering (QA) by integrating external information into Large Language Models (LLMs). However, false, inaccurate, and misleading in...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Multimodal artificial intelligence in prostate cancer: integrating multiparametric MRI with clinicopathological, molecular, and functional imaging data.](https://pubmed.ncbi.nlm.nih.gov/42635792/)
  来源：PubMed | 日期：2026-08-24 | 相关度：8.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Multimodal artificial intelligence (AI) is reshaping prostate cancer imaging by moving beyond MRI-only algorithms toward models that integrate multiparametric MRI (mpMRI) with clinical variables, pathology, genomics, ult...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Microbiome-metabolome multi-omics biomarkers for infectious disease prognosis: Current evidence, AI-driven integration, and translational challenges.](https://pubmed.ncbi.nlm.nih.gov/42642268/)
  来源：PubMed | 日期：2026-08-25 | 相关度：7.3 | 新颖度：5.75
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：Microbiome-metabolome interactions are emerging as promising predictors of infectious disease, beyond conventional pathogen detection. Growing evidence shows that microbial dysbiosis, altered microbial-derived metabolite...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Towards World Models in Biomedical Research](http://arxiv.org/abs/2606.05925v2)
  来源：arXiv | 日期：2026-06-04 | 相关度：5.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：A central goal of biomedicine is to understand, predict and ultimately control the dynamic mechanisms by which biological systems respond to perturbations, disease progression and therapeutic intervention. Although found...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Generating Biomedical Fact-Checking Reports with RL-Enhanced Agentic Search](http://arxiv.org/abs/2608.23811v1)
  来源：arXiv | 日期：2026-08-24 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Automated fact-checking is essential for ensuring the reliability of public health information, yet the biomedical domain poses unique challenges. Validating biomedical claims requires rigorous interpretation of scientif...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evidence Blindness in Direct Corpus Interaction: Persistent Navigation with AtlasNav](http://arxiv.org/abs/2608.24764v1)
  来源：arXiv | 日期：2026-08-25 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Large language model agents are moving beyond conventional retrieval-augmented generation toward direct interaction with external corpora. Direct Corpus Interaction (DCI) keeps the full corpus accessible, yet reachable e...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Molecular LLM Agents: From Architectural Design to Scientific Autonomy](http://arxiv.org/abs/2608.23104v2)
  来源：arXiv | 日期：2026-08-24 | 相关度：2.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Molecular science represents an important frontier for LLM-based agents. Unlike general agents that mainly operate over natural language, code, or web environments, molecular LLM agents must perceive, reason about, and a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LivingRAG: Augmenting Graph RAG with Experience](http://arxiv.org/abs/2608.25960v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：1.4 | 新颖度：6.87
  匹配主题：未命中具体主题
  中文摘要：Graph-based RAG improves multi-hop question answering by organizing evidence as a knowledge graph. However, most existing RAG systems process each query in isolation and discard useful reasoning from the LLM's response a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution](http://arxiv.org/abs/2606.25721v2)
  来源：arXiv | 日期：2026-06-24 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate model outputs through malicious retrieved documents. Existing detection methods typically rely on auxiliary classifi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Less can be More: Relieving RAG Bottlenecks via Evidence Frontloading and Pressure-Adaptive Budgeting](http://arxiv.org/abs/2608.25115v1)
  来源：arXiv | 日期：2026-08-25 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Existing methods for improving Retrieval-Augmented Generation (RAG) efficiency mainly optimize downstream LLM generation, such as context compression or serving optimization. However, RAG is an end-to-end system, and its...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Autonomous Mathematical Discovery in an Open-World Multi-Agent Environment](http://arxiv.org/abs/2608.23691v1)
  来源：arXiv | 日期：2026-08-24 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：We study autonomous mathematical discovery in the Station, an open-world multi-agent environment in which AI agents from different model families pursue a shared research goal without a central coordinator or scripted pi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [VGGT-DP: Generalizable Robot Control via Vision Foundation Models](http://arxiv.org/abs/2509.18778v2)
  来源：arXiv | 日期：2025-09-23 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Visual imitation learning frameworks allow robots to learn manipulation skills from expert demonstrations. While existing approaches mainly focus on policy design, they often neglect the structure and capacity of visual ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [PlanSightRAG: A Visual-First Multimodal RAG for Automating Question Answering and Compliance Checking for Civil Standard Plans](http://arxiv.org/abs/2608.26091v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：1.4 | 新颖度：7.13
  匹配主题：未命中具体主题
  中文摘要：Civil infrastructure compliance checking has long relied on engineers manually reading legacy 2D plans; however, OCR-based automation strips away the geometry and layout essential for interpreting these plans. We present...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Corpus2Skill: Distilling Enterprise Knowledge into Navigable Agent Skills for QA and RAG](http://arxiv.org/abs/2604.14572v4)
  来源：arXiv | 日期：2026-04-16 | 相关度：1.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) grounds LLM responses in external evidence but treats the model as a passive consumer of search results, with no view of how the corpus is organized or what it has not yet seen. We pr...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Pointing the Way, Hiding the Destination: Practical Private Dense Retrieval at Scale](http://arxiv.org/abs/2608.25735v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：0.7 | 新颖度：5.52
  匹配主题：未命中具体主题
  中文摘要：Hosted retrieval-augmented generation (RAG) and semantic search allow users to query valuable provider-held corpora, raising two competing demands: to hide each query and chosen result, yet reveal only the documents that...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Data-Driven Modeling of Spatiotemporal Dynamics Using Multimodal Imaging Data](http://arxiv.org/abs/2511.08847v2)
  来源：arXiv | 日期：2025-11-12 | 相关度：3.05 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Understanding how biological systems evolve across space and time remains a fundamental challenge, particularly when dynamic processes vary substantially across individuals. We present a personalized graph-based dynamica...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention](http://arxiv.org/abs/2602.04711v3)
  来源：arXiv | 日期：2026-02-04 | 相关度：2.1 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Retrieval Augmented Generation (RAG) is a highly effective paradigm for keeping LLM-based responses up-to-date and reducing the likelihood of hallucinations. Yet, RAG was recently shown to be quite vulnerable to corpus k...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [PonsRAG: A Pons-Inspired RAG Bridging Cognitive Islands for Coordinated Long Narrative Reasoning](http://arxiv.org/abs/2608.25486v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Long Narrative Reasoning is an essential capability for processing and reasoning over complex narratives. While retrieval-augmented generation provides a promising framework, existing methods still face two critical chal...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [The "Curse of Knowledge" in LLM Query Simulation: Concept Provenance for Tracing Answer-Side Intrusion](http://arxiv.org/abs/2608.25245v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：LLM-generated search queries are widely used to augment IR evaluation, yet they may contain concepts that presuppose answer-side document knowledge, violating the information-access boundary of pre-search users. Existing...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [How Do Agents Fail on AutoResearch: End-to-End Diagnostic Evaluation on 100 Real-World Frontier Research Tasks](http://arxiv.org/abs/2608.14905v3)
  来源：arXiv | 日期：2026-08-14 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：AI has long assisted scientific research, but the rapid advance of LLMs and agentic scaffolds is reshaping the landscape; a single system can now carry whole-stage research from an initial hypothesis all the way to final...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Surface-enhanced Raman scattering for the diagnosis of respiratory viruses.](https://pubmed.ncbi.nlm.nih.gov/42565721/)
  来源：PubMed | 日期：2026-08-25 | 相关度：5.75 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent, application_monitoring
  中文摘要：Surface-enhanced Raman scattering (SERS) has become a promising tool for rapid and sensitive respiratory pathogen detection. However, relevant reviews remain scarce. This review systematically summarizes the evolution of...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [A Multimodal Foundation Model for Longitudinal Patient Representation and Scalable Insight Generation in Oncology](http://arxiv.org/abs/2608.24688v1)
  来源：arXiv | 日期：2026-08-25 | 相关度：3.75 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Precision oncology necessitates a longitudinal model of patient state that captures cancer evolution and treatment over time, integrating multimodal observations. We introduce the oFM, a foundation model developed on a r...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
