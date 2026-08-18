# 每日论文监控日报 (2026-08-18)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 44 篇新论文。

## 抓取状态

- arXiv：成功，命中 37 篇
- PubMed：成功，命中 22 篇
- bioRxiv：成功，命中 9 篇
- medRxiv：成功，命中 12 篇

## 最值得看

### Foundation Model / Agent

- [From Output Errors to Workflow Harm: A Practitioner-Audit Method for LLM-Mediated Research](https://www.medrxiv.org/content/10.64898/2026.08.13.26360414v1)
  来源：medRxiv | 日期：2026-08-17 | 相关度：7.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Objective. Formal large language model (LLM) evaluations score isolated prompts, but clinicians and health-informatics researchers meet model failures inside multi-step workflows where erroneous output can alter procedur...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multimodal Language Models Benchmarked Against the NRC Reactor Operator Licensing Examination: Fine-Tuning and Retrieval Strategies](http://arxiv.org/abs/2607.22067v2)
  来源：arXiv | 日期：2026-07-24 | 相关度：7.5 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Competence claims for a language model in a safety-critical domain are credible when measured against a standard the domain already enforces. We evaluate an open-weight 31-billion-parameter multimodal model (Gemma 4 31B-...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LLMs for Zero-Shot Threat Detection via Structured Risk Indicators](http://arxiv.org/abs/2608.16508v1)
  来源：arXiv | 日期：2026-08-17 | 相关度：6.55 | 新颖度：8.74
  匹配主题：foundation_model_agent
  中文摘要：We propose a two-stage large language model (LLM) framework for zero-shot detection of insider threats and advanced persistent threats (APTs) from heterogeneous security logs. The framework models user activity as chrono...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Ribonucleic-Acid Protein Interaction Prediction Based on Deep Learning: A Comprehensive Survey](http://arxiv.org/abs/2410.00077v2)
  来源：arXiv | 日期：2024-09-30 | 相关度：9.65 | 新颖度：5.75
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：The interaction between Ribonucleic Acids (RNAs) and proteins, also called RNA Protein Interaction (RPI), governs biological processes, including gene regulation and disease pathogenesis. This comprehensive survey examin...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [CACSurv: Concordance-Aligned Comparative Learning with Large Language Models for Cancer Survival Prediction](http://arxiv.org/abs/2608.16594v1)
  来源：arXiv | 日期：2026-08-17 | 相关度：7.8 | 新颖度：8.42
  匹配主题：foundation_model_agent
  中文摘要：Cancer survival prediction supports treatment planning, risk stratification, and follow-up management. Existing methods use structured clinical variables, whole-slide images, genomic profiles, or multimodal inputs, while...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 可追踪

### Foundation Model / Agent

- [SMA: Who Said That? Auditing Membership Leakage in Semi-Black-box RAG Controlling](http://arxiv.org/abs/2508.09105v3)
  来源：arXiv | 日期：2025-08-12 | 相关度：7.5 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) and its Multimodal Retrieval-Augmented Generation (MRAG) significantly improve the knowledge coverage and contextual understanding of Large Language Models (LLMs) by introducing exter...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [GraphLoom: Reliability-Calibrated Graph Evidence Routing for Multimodal KG-RAG](http://arxiv.org/abs/2608.15056v1)
  来源：arXiv | 日期：2026-08-15 | 相关度：7.5 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Multimodal retrieval-augmented generation (RAG) systems often rely on long unstructured contexts or aggressively expanded evidence graphs, which can introduce noisy evidence, weaken multi-hop reasoning, and increase unsu...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A contextualised protein language model reveals the functional syntax of bacterial evolution](https://www.biorxiv.org/content/10.1101/2025.07.20.665723v3)
  来源：bioRxiv | 日期：2026-08-17 | 相关度：7.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Bacteria have evolved a vast diversity of functions and behaviours that are currently incompletely understood and poorly predicted from DNA sequence alone. To understand the syntax of bacterial evolution and discover gen...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [mR$^2$AG: Multimodal Retrieval-Reflection-Augmented Generation for Knowledge-Based VQA](http://arxiv.org/abs/2411.15041v2)
  来源：arXiv | 日期：2024-11-22 | 相关度：6.8 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Advanced Multimodal Large Language Models (MLLMs) struggle with recent Knowledge-based Visual Question Answering (VQA) tasks, such as INFOSEEK and Encyclopedic-VQA, due to their limited and frozen knowledge scope, often ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ConceptFormer: Learning Adaptive Latent Concepts for Query-Document Alignment in Visual Document Retrieval](http://arxiv.org/abs/2608.15698v1)
  来源：arXiv | 日期：2026-08-16 | 相关度：6.8 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Visual document retrieval is a critical component of multimodal retrieval-augmented generation, aiming to identify query-relevant pages from document collections where evidence is distributed across text, layout, charts,...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Five Queries Are Enough: Query-Efficient and Surrogate-Free Membership Inference Attacks on RAG via Entailment](http://arxiv.org/abs/2605.24312v4)
  来源：arXiv | 日期：2026-05-23 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) has become central to large language model (LLM) deployments, grounding responses in enterprise or proprietary data to reduce hallucinations. However, this design introduces a new pri...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Large Discovery Models: Empirically-grounded Model-Based Open-Ended Search](http://arxiv.org/abs/2608.15669v1)
  来源：arXiv | 日期：2026-08-16 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Scientific discovery often involves optimising expensive-to-evaluate objectives over vast, structured, and open-ended hypothesis spaces, such as molecules, protein sequences, and computer programs. Generative models such...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Lectures to Learning Outcomes: Meaningful Integration of AI-Generated Content in Pre-Clerkship Medical Training](https://www.medrxiv.org/content/10.1101/2025.05.13.25327518v2)
  来源：medRxiv | 日期：2026-08-17 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Background Large Language Models (LLMs) can efficiently synthesize educational content, yet few studies have evaluated standardized, LLM-powered curricular interventions and their effects on medical student learning. Met...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BengaliMCQ: Automatic Generation and Answer Prediction of Academic Multiple-Choice Questions in a Low-Resource Language](http://arxiv.org/abs/2608.15547v1)
  来源：arXiv | 日期：2026-08-16 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Traditional retrieval-augmented generation (RAG) frameworks process documents without attending to their hierarchical structure, leading to poor performance, especially in low-resource languages such as Bengali. To addre...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PertMind: Eliciting Emergent Biological Reasoning in LLM via Reinforcement Learning on Cellular Perturbation Data](http://arxiv.org/abs/2608.16419v1)
  来源：arXiv | 日期：2026-08-17 | 相关度：5.75 | 新颖度：6.74
  匹配主题：foundation_model_agent
  中文摘要：Large language models can describe mechanisms, yet scalable post-training still depends on costly, manually curated biological reasoning traces. Here we show that cellular perturbation atlases can instead become reinforc...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [REFINE: Closing the Loop Between Large Language Models and Symbolic Rules in Clinical NLP](https://www.medrxiv.org/content/10.64898/2026.08.11.26360118v1)
  来源：medRxiv | 日期：2026-08-17 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Symbolic clinical natural language processing (NLP) systems remain widely used for extracting clinical concepts from electronic health record (EHR) narratives, but maintaining rule resources requires extensive manual err...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Clause Encounters of the Third Kind: Can LLMs Replace Language Teachers?](http://arxiv.org/abs/2608.16286v1)
  来源：arXiv | 日期：2026-08-17 | 相关度：5.45 | 新颖度：6.61
  匹配主题：foundation_model_agent
  中文摘要：While various organizations now actively encourage LLM use in classrooms, we still lack rigorous, systematic evaluations of how well these models actually perform the fundamental tasks of language pedagogy. This paper ex...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Catching Hallucinated Citations in Video-LLM Question Answering: A Self-Verification Pipeline and Verifier Ablation Study](http://arxiv.org/abs/2608.15574v1)
  来源：arXiv | 日期：2026-08-16 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Video question answering systems built on vision-language models often produce timestamped claims with high confidence even when unsupported by the cited frame. This deceptive hallucination arises because timestamps impl...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RAGas: Retrieval-Augmented Gas Optimization for Smart Contracts with Continuous Knowledge Integration](http://arxiv.org/abs/2608.15857v1)
  来源：arXiv | 日期：2026-08-16 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Ethereum is now integral to mission-critical sectors, including finance, healthcare, and supply chain management. Execution fees, commonly referred to as Gas, scale with the computational complexity of their functions. S...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Bye-bye, Bluebook? Automating Legal Drudgery With AI-Augmented Rule Following](http://arxiv.org/abs/2505.02763v2)
  来源：arXiv | 日期：2025-05-05 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：One of the central promises of legal AI is to automate drudgery -- the formal, repetitive tasks of lawyers' work that consume time without calling for much discretion. Yet it remains an open question how well AI models a...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Think Inside the Chunk: RegulaRAG for Regulation-Compliant Scenario Generation using LLMs: A Case Study of UN Regulation No. 152](http://arxiv.org/abs/2608.16394v1)
  来源：arXiv | 日期：2026-08-17 | 相关度：4.75 | 新颖度：7.16
  匹配主题：foundation_model_agent
  中文摘要：Generating regulation-compliant test scenarios is essential for validating safety-critical automotive systems, yet Large Language Models (LLMs) struggle to ground outputs in long, hierarchical standards. We present Regul...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Efficient exploration of sequence space enables rapid generation of functional genome editors](https://www.biorxiv.org/content/10.64898/2026.08.16.745112v1)
  来源：bioRxiv | 日期：2026-08-17 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：The problem of how protein sequences translate into defined functions remains largely unsolved despite decades of progress. New methods to efficiently explore protein sequence space will help to shed light on these seque...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Fine-Grained Structural Classification of Biosynthetic Gene Cluster-Encoded Products.](https://pubmed.ncbi.nlm.nih.gov/42606533/)
  来源：PubMed | 日期：2026-08-17 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Biosynthetic gene clusters (BGCs) are responsible the biosynthesis of many natural products, including a multitude of effective therapeutics and their precursors. Advances in genomic data collection as well as computatio...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [When Context Misleads: Intent-Guided Decoding for Robust Retrieval-Augmented Generation](http://arxiv.org/abs/2608.16515v1)
  来源：arXiv | 日期：2026-08-17 | 相关度：4.75 | 新颖度：7.52
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) improves large language models by grounding generation in external evidence, but it also introduces a source trust problem: retrieved context may be useful, irrelevant, or even mislea...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [An Agentic AI Framework with Large Language Models and Chain-of-Thought for UAV-Assisted Logistics Scheduling with Mobile Edge Computing](http://arxiv.org/abs/2605.13221v2)
  来源：arXiv | 日期：2026-05-13 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：In cloud manufacturing, unmanned aerial vehicles (UAVs) can support both product collection and mobile edge computing (MEC). This joint operation forms a hybrid scheduling problem, where physical logistics decisions are ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [DSPrompt: Dynamic Soft Prompt Defense Against M-RAG Corruption](http://arxiv.org/abs/2608.16536v1)
  来源：arXiv | 日期：2026-08-17 | 相关度：3.45 | 新颖度：8.06
  匹配主题：foundation_model_agent
  中文摘要：Multimodal Retrieval Augmented Generation (M-RAG) is increasingly vulnerable to adversarial attacks where malicious data are crafted to produce embeddings that align with benign entries in the vector space, deceiving ret...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Hypergraph-based Multimodal Retrieval-Augmented Generation with Incremental Refinement](http://arxiv.org/abs/2608.16628v1)
  来源：arXiv | 日期：2026-08-17 | 相关度：2.75 | 新颖度：8.53
  匹配主题：foundation_model_agent
  中文摘要：Modern Multimodal Retrieval-Augmented Generation (M-RAG) systems are fundamentally limited by the binary connectivity paradigm of traditional simple graphs, which fails to capture the intricate, high-order correlations a...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Multi-omics precision diagnosis of brucellosis: Advances in biomarker discovery and clinical application.](https://pubmed.ncbi.nlm.nih.gov/42128325/)
  来源：PubMed | 日期：2026-08-15 | 相关度：7.4 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：Brucellosis, a neglected zoonosis caused by intracellular Brucella bacteria, remains a formidable global public health challenge, especially in developing regions. The notorious ability of Brucella to evade host immunity...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Performance of an Ambient Generative AI Documentation Tool in a Linguistically Diverse Clinical Setting](https://www.medrxiv.org/content/10.64898/2026.08.14.26360467v1)
  来源：medRxiv | 日期：2026-08-17 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Ambient artificial intelligence scribes are being increasingly used in healthcare to improve efficiency and reduce provider clinical documentation burden, yet their performance across linguistically diverse patient popul...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Noesis: Bidirectional Graph-RAG with Adaptive Parallelism and Cross-Knowledge-Base Semantic Discovery](http://arxiv.org/abs/2608.15919v1)
  来源：arXiv | 日期：2026-08-16 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation over knowledge graphs (Graph-RAG) has emerged as a powerful paradigm for grounding large language models in domain-specific corpora. However, existing systems face persistent limitations: (...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [POI Recommendation with LLM-Augmented Multi-Graph Learning and Contrastive Alignment](http://arxiv.org/abs/2608.16407v1)
  来源：arXiv | 日期：2026-08-17 | 相关度：2.75 | 新颖度：7.45
  匹配主题：foundation_model_agent
  中文摘要：Point-of-interest (POI) recommendation models based on graph neural networks achieve strong performance by propagating collaborative signals over user-item interactions, yet they struggle with the cold-start problem, whe...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [D2-ScaleAgent: Dual-Dimensional Scaling for Long Document Understanding](http://arxiv.org/abs/2608.16417v1)
  来源：arXiv | 日期：2026-08-17 | 相关度：1.4 | 新颖度：7.49
  匹配主题：未命中具体主题
  中文摘要：Multi-modal retrieval-augmented generation (RAG) is a key technique for visually rich long document understanding. Existing multi-modal RAG methods are progressively advancing toward multi-agent systems: they first retri...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond Thresholds: A Quality-Aware Decision Intelligence Framework for Cold Chain IoT Systems](http://arxiv.org/abs/2608.15082v1)
  来源：arXiv | 日期：2026-08-15 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Cold chain logistics has advanced technologically, yet most deployed systems remain reactive monitors, not decision-making agents: thresholds trigger alerts, but nothing relates violations to cumulative product degradati...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [P-PAS: Prefill-Pressure Adaptive Scheduling for Long-Context LLM Serving](http://arxiv.org/abs/2608.15171v1)
  来源：arXiv | 日期：2026-08-15 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Long-context LLM applications such as retrieval-augmented generation (RAG) and agentic systems often process tens of thousands of input tokens to produce short outputs, making end-to-end request latency an important serv...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Skill2Query: Exploiting Skill Structure to Generate Pseudo-Queries for Agent Skill Retrieval](http://arxiv.org/abs/2608.16071v1)
  来源：arXiv | 日期：2026-08-17 | 相关度：0.7 | 新颖度：6.04
  匹配主题：未命中具体主题
  中文摘要：Pseudo-query generation can alleviate the supervision bottleneck for agent skill retrieval, but existing document-level approaches typically leave the rich internal relations among capabilities, parameters, and usage exa...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ALKEMIE Agent: an autonomous platform for computational materials design](http://arxiv.org/abs/2608.15776v1)
  来源：arXiv | 日期：2026-08-16 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Despite the powerful multi-scale modeling methods and high-throughput infrastructures established in the materials community, real material computation workflows remain fragmented and heavily manual, requiring researcher...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [ML-AutoResearch: Training Machine Learning Research Agents with Automatically Generated Environments](http://arxiv.org/abs/2603.17216v2)
  来源：arXiv | 日期：2026-03-17 | 相关度：1.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：With the advent of AI agents, automated scientific discovery is becoming an increasingly plausible goal. However, training agents to autonomously execute the engineering-heavy labor of machine learning (ML) research requ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Discovery of Selective Small-Molecule Ligands of SV2C by AI-Enhanced Virtual Screening and Experimental Validation](https://www.biorxiv.org/content/10.64898/2026.08.11.744237v1)
  来源：bioRxiv | 日期：2026-08-16 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Synaptic vesicle glycoprotein 2C (SV2C) is a vesicular protein enriched in dopaminergic neurons of the basal ganglia that modulates dopamine storage and release, and its disruption is implicated in Parkinson's disease (P...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Integrating stemness and epithelial-mesenchymal transition signatures with machine learning identifies RUNX1 as a therapeutic vulnerability in colorectal cancer.](https://pubmed.ncbi.nlm.nih.gov/42372471/)
  来源：PubMed | 日期：2026-08-15 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Colorectal cancer (CC) arises from a complex interplay between genetic and epigenetic alterations within the colorectal mucosa, resulting in unchecked cellular proliferation and tumor development. This complexity results...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Coverage Is Not Containment: A Fundamental Limit of Admission-Time Defenses Against Coordinated Poisoning of Vector Retrieval](http://arxiv.org/abs/2608.16044v1)
  来源：arXiv | 日期：2026-08-17 | 相关度：0.7 | 新颖度：5.41
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) answers a question by retrieving passages from a vector store and trusting them as context, so anyone who can add documents can try to steer the answer. A recent, appealing defense fi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Artificial intelligence for predicting BCG response in non-muscle-invasive bladder cancer: a systematic review.](https://pubmed.ncbi.nlm.nih.gov/42605566/)
  来源：PubMed | 日期：2026-08-17 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：To systematically identify, appraise and synthesise artificial intelligence (AI) and machine-learning (ML) models that predict treatment response and clinical outcomes after intravesical bacillus Calmette-Guérin (BCG) in...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Bridging innovation and implementation in laboratory medicine: insights from a global survey on unmet needs and emerging technologies.](https://pubmed.ncbi.nlm.nih.gov/42119761/)
  来源：PubMed | 日期：2026-08-15 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Technological innovation in laboratory medicine is advancing rapidly, driven by artificial intelligence, next-generation sequencing, high-resolution mass spectrometry, novel biomarkers, and decentralized point-of-care te...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [GRIP: Grounded Reasoning via Information-Restricted Premises](http://arxiv.org/abs/2608.16776v1)
  来源：arXiv | 日期：2026-08-17 | 相关度：0.7 | 新颖度：8.09
  匹配主题：未命中具体主题
  中文摘要：High-capacity encoders in retrieval-augmented generation (RAG) can let the query dominate the latent state, leaving retrieved evidence functionally irrelevant. We call this failure mode query dominance. To address it, we...
  为什么值得看：GRIP: Grounded Reasoning via Information 与你的主题有弱匹配，暂时保留作低优先级跟踪。

- [Empowering Polymeric Materials Discovery by Artificial Intelligence](http://arxiv.org/abs/2606.20753v2)
  来源：arXiv | 日期：2026-06-18 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Polymeric materials underpin modern technologies spanning energy storage, microelectronics, healthcare and sustainable manufacturing. Yet their rational design remains exceptionally challenging because material performan...
  为什么值得看：Empowering Polymeric Materials Discovery 与你的主题有弱匹配，暂时保留作低优先级跟踪。
