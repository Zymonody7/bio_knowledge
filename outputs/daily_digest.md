# 每日论文监控日报 (2026-08-24)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 26 篇新论文。

## 抓取状态

- arXiv：成功，命中 19 篇
- PubMed：成功，命中 18 篇
- bioRxiv：成功，命中 13 篇
- medRxiv：成功，命中 17 篇

## 最值得看

### Foundation Model / Agent

- [Vis-Poison: Poisoning Visual Knowledge in Multimodal Retrieval-Augmented Generation](http://arxiv.org/abs/2608.20756v1)
  来源：arXiv | 日期：2026-08-21 | 相关度：7.9 | 新颖度：6.2
  匹配主题：foundation_model_agent
  中文摘要：While multimodal retrieval-augmented generation (RAG) systems increasingly rely on images as external knowledge sources, the introduction of poisoned visual evidence can severely compromise multimodal large language mode...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [ConceptFormer: Learning Adaptive Latent Concepts for Query-Document Alignment in Visual Document Retrieval](http://arxiv.org/abs/2608.15698v2)
  来源：arXiv | 日期：2026-08-16 | 相关度：6.8 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Visual document retrieval is a critical component of multimodal retrieval-augmented generation, aiming to identify query-relevant pages from document collections where evidence is distributed across text, layout, charts,...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Trustworthy RAG: An Evaluation Agent for Detecting Misinformation and Knowledge Poisoning in Generative AI Systems](http://arxiv.org/abs/2608.21095v1)
  来源：arXiv | 日期：2026-08-21 | 相关度：6.55 | 新颖度：6.7
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) grounds Large Language Model (LLM) outputs in external knowledge, but RAG systems usually trust whatever they retrieve, creating a Security-Reliability Gap: high semantic relevance do...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Designing a Robust LLM-Based Evaluation System for Agentic AI in Drug Discovery Through Human Alignment](http://arxiv.org/abs/2608.21057v1)
  来源：arXiv | 日期：2026-08-21 | 相关度：6.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Agentic large language model (LLM) systems are reshaping scientific workflows in chemistry and drug discovery, but evaluating their open-ended, tool-augmented outputs remains a fundamental bottleneck. Reference-based met...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PG-LLM: Benchmarking General-Purpose Language Models for Protein Variant Ranking](https://www.biorxiv.org/content/10.64898/2026.07.27.741045v3)
  来源：bioRxiv | 日期：2026-08-21 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：General-purpose frontier language models are being increasingly utilized for protein-design work, yet their ability to understand and evaluate variant effects remains unclear. Here, we introduce PG-LLM, a benchmark compr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Searching the Druggable Genome using Large Language Models.](https://pubmed.ncbi.nlm.nih.gov/42631692/)
  来源：PubMed | 日期：2026-08-22 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：The druggable genome encompasses the genes that are known or predicted to interact with drugs. The Drug-Gene Interaction Database (DGIdb) provides an integrated resource for discovering and contextualizing these interact...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SIREN (Luring LLMs onto the Rocks): PAIR-Driven Preference Manipulation in Web-RAG Recommenders](http://arxiv.org/abs/2607.21951v2)
  来源：arXiv | 日期：2026-07-24 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：This paper investigates the adversarial manipulation of the ranked recommendations produced by web-augmented large language models (LLMs). When an LLM answers a recommendation query by retrieving and reading live webpage...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Graph Engineering in the Era of LLM Agents: From Individual Intelligence to System Intelligence](http://arxiv.org/abs/2608.21156v1)
  来源：arXiv | 日期：2026-08-21 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：LLMs have evolved from language generators to autonomous agents capable of complex, long-horizon tasks. This evolution has produced paradigms including Prompt Engineering to elicit model capabilities, Context Engineering...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [MTS-Bench: A Manchester Triage System Benchmark for Language Model Triage Safety](https://www.medrxiv.org/content/10.64898/2026.08.04.26359651v2)
  来源：medRxiv | 日期：2026-08-21 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：BackgroundGeneral purpose language models such as ChatGPT are increasingly used by physicians and triage nurses during emergency triage. A recent study reported 51.6% undertriage of emergencies when patients queried Chat...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Index SLM Technical Report](http://arxiv.org/abs/2607.09885v3)
  来源：arXiv | 日期：2026-07-10 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：We present Index-1.9B, a series of open small language models developed at Bilibili. The series comprises four models: Index-1.9B-Base, a foundation model with 1.9 billion non-embedding parameters pre-trained on 2.8 tril...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [jXBW: A Compressed Index Enabling Structure-Aware JSONL Retrieval for Structured RAG](http://arxiv.org/abs/2508.12536v4)
  来源：arXiv | 日期：2025-08-18 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Providing \textit{structured} information to large language models (LLMs) improves multi-step reasoning and factual grounding, and recent retrieval-augmented generation (RAG) systems therefore reconstruct structure from ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Towards Query-Agnostic RAG Evaluation via Query Coverage and Claim Verifiability](http://arxiv.org/abs/2608.11238v2)
  来源：arXiv | 日期：2026-07-31 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation improves the factuality of large language models by grounding responses in retrieved evidence, yet existing evaluation frameworks struggle to provide consistent, fine-grained diagnostics ac...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Sparse autoencoder features from InterPLM predict neuropeptide precursors among secreted proteins](https://www.biorxiv.org/content/10.64898/2026.08.20.746077v1)
  来源：bioRxiv | 日期：2026-08-21 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Neuropeptides are a diverse class of short, secreted signaling molecules that regulate key physiological processes in animals. Despite their important biological roles and increasingly recognized therapeutic value, the d...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Self-Revising Discovery Systems for Science: A Categorical Framework for Agentic Artificial Intelligence](http://arxiv.org/abs/2606.01444v2)
  来源：arXiv | 日期：2026-05-31 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Scientific discovery is not only answer generation but revision of the representational regime in which evidence, artifacts, operations, and verifiers are typed. We develop a category-theoretic account of agentic discove...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MedRAGChecker: Claim-Level Verification for Biomedical Retrieval-Augmented Generation](http://arxiv.org/abs/2601.06519v2)
  来源：arXiv | 日期：2026-01-10 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Biomedical retrieval-augmented generation (RAG) can ground LLM answers in medical literature, yet long-form outputs often contain isolated unsupported or contradictory claims with safety implications. We introduce MedRAG...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [TabMedQA: From Structured Data to Question-Answer Datasets in Early Clinical Decision-Making](https://www.medrxiv.org/content/10.64898/2026.08.19.26360779v1)
  来源：medRxiv | 日期：2026-08-21 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：The rising adoption of Large Language Models (LLMs) and Retrieval Augmented Generation (RAG) in clinical general practice demands datasets that capture realistic early-stage clinical decision-making, where experts must d...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [A Human-in-the-Loop Large Language Model System Based on the Model Context Protocol for Differential Diagnosis from Electronic Medical Records and Literature](https://www.medrxiv.org/content/10.64898/2026.08.18.26359085v1)
  来源：medRxiv | 日期：2026-08-21 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Diagnostic errors, including misdiagnoses and delayed clinical diagnoses, could affect outcomes of a significant patient population, particularly individuals presenting with rare diseases or non-specific symptoms. From r...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [MetaFemina: development and evaluation of a large language model-assisted platform for automated meta-analysis of nutritional exposures and breast, ovarian, and uterine cancer risk](https://www.medrxiv.org/content/10.64898/2026.08.18.26360713v1)
  来源：medRxiv | 日期：2026-08-21 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Objective To develop and evaluate an automated large language model (LLM)-based framework for conducting meta-analyses of nutrition-related exposures and the risk of breast, ovarian, and uterine cancers. Design We develo...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Self-Reported Side Effects Among Reddit Users Taking Nonapproved Retatrutide](https://www.medrxiv.org/content/10.64898/2026.05.28.26352819v2)
  来源：medRxiv | 日期：2026-08-21 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Gray-market retatrutide use is increasing, but patient safety experiences remain poorly characterized. This cross-sectional analysis examined Reddit posts and comments from retatrutide-specific and broader peptide or wei...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Specification Portability Across LLM Development Agents: Cross-Agent Compatibility in Specification-Driven Software Migration](http://arxiv.org/abs/2608.21208v1)
  来源：arXiv | 日期：2026-08-21 | 相关度：2.1 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：This paper investigates cross-agent specification portability using Oracle-to-PostgreSQL migration as a controlled software transformation task. The study combines two experimental stages. First, a specification-first mi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Temporal Validity on Real Software Histories: Eliminating Stale-Fact Errors in Code-Assistant Memory over GitHub Fixes](http://arxiv.org/abs/2608.20685v1)
  来源：arXiv | 日期：2026-08-21 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) has no model of time: when a fact changes across a coding session - a function is renamed, an endpoint moves, a dependency is bumped - RAG retrieves both the old and new value with ne...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EnSI-RAG: Entity-Structure-Indexed Retrieval-Augmented Generation for Long-Document Question Answering](http://arxiv.org/abs/2608.21252v1)
  来源：arXiv | 日期：2026-08-21 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Question answering (QA) over long, connected documents remains challenging because relevant evidence may span multiple entities and their relationships. Existing retrieval-augmented generation (RAG) methods typically ind...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Assessing the Reliability of LLM-Generated Phenotype-Genotype Associations Through External Validation](https://www.biorxiv.org/content/10.64898/2026.08.13.744701v1)
  来源：bioRxiv | 日期：2026-08-21 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：BackgroundPhenotype-genotype associations underpin precision medicine by enabling disease prevention, early diagnosis, risk stratification, therapeutic target discovery, and personalized treatment. However, the rapid gro...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Quality, consistency, and clinical safety of AI-generated versus clinician-written clinical notes: a multi-country paired simulation study](https://www.medrxiv.org/content/10.64898/2026.08.18.26360701v1)
  来源：medRxiv | 日期：2026-08-21 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Background Ambient AI documentation tools, known as scribes, are entering routine clinical practice at scale, but the evidence comparing the notes they produce against clinician-written notes is dominated by single-site,...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SENTRY: Deterministic, Intelligent Risk Assessment for IT Change Management](http://arxiv.org/abs/2608.21203v1)
  来源：arXiv | 日期：2026-08-21 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Technology change management in large financial institutions depends on risk assessments that are accurate, consistent, and auditable. In practice, many institutions still rely on self-reported questionnaires. Those ques...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Artificial Intelligence-Empowered Single-Cell Phenotyping for Rapid, Automated Pathogen Diagnostics.](https://pubmed.ncbi.nlm.nih.gov/42627671/)
  来源：PubMed | 日期：2026-08-21 | 相关度：2.45 | 新颖度：0.25
  匹配主题：application_monitoring
  中文摘要：Accurate bacterial identification and antimicrobial susceptibility testing (AST) are essential for timely clinical decision-making. Conventional diagnostic methods typically require 24-48 h, leading to inappropriate empi...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
