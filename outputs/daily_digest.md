# 每日论文监控日报 (2026-06-14)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 30 篇新论文。

## 抓取状态

- arXiv：成功，命中 20 篇
- PubMed：成功，命中 39 篇
- bioRxiv：成功，命中 15 篇
- medRxiv：成功，命中 6 篇

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [CFALR: Collaborative Filtering-Augmented Large Language Model for Personalized Fashion Outfit Recommendation](http://arxiv.org/abs/2606.13001v1)
  来源：arXiv | 日期：2026-06-11 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Personalized outfit recommendation poses a significant challenge in e-commerce and social media platforms, requiring systems that balance user preferences with aesthetic compatibility. Collaborative filtering (CF) provid...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Mod-Guide: An LLM-based Content Moderation Feedback System to Address Insensitive Speech toward Indigenous Ethnic and Religious Minority Communities](http://arxiv.org/abs/2606.13397v1)
  来源：arXiv | 日期：2026-06-11 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Language operates as a mechanism of both marginalization and resistance, especially for minority communities navigating insensitive and harmful speech online. As content moderation increasingly depends on large language ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BLUEmed: Retrieval-Augmented Multi-Agent Debate for Clinical Error Detection](http://arxiv.org/abs/2604.10389v2)
  来源：arXiv | 日期：2026-04-12 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Terminology substitution errors in clinical notes, where one medical term is replaced by a linguistically valid but clinically different term, pose a persistent challenge for automated error detection in healthcare. We i...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Deterministic Integrity Gates for LLM-Assisted Clinical Manuscript Preparation: An Auditable Biomedical Informatics Architecture](http://arxiv.org/abs/2606.09500v3)
  来源：arXiv | 日期：2026-06-08 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：As autonomous research agents and AI co-scientist systems push large language models (LLMs) from drafting toward end-to-end manuscript production, the bottleneck shifts from generation to verification. Fluent LLM output ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DeePEn - A Depth sensitive benchmark for Protein Engineering](https://www.biorxiv.org/content/10.64898/2026.06.09.731073v1)
  来源：bioRxiv | 日期：2026-06-11 | 相关度：5.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Recent progress in modeling techniques and high-throughput screening has significantly enhanced the accessibility of protein engineering. Nevertheless, further progress gets hindered by the lack of robust benchmarks that...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [DNA Compression with Genomic Language Models: Tokenization, Benchmarking, and an Information-Content Map](https://www.biorxiv.org/content/10.64898/2026.06.10.731316v1)
  来源：bioRxiv | 日期：2026-06-12 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Lossless compression and probabilistic sequence modeling are two faces of the same coin: a model that assigns high probability to a sequence can encode it in few bits via arithmetic coding. We exploit this duality to eva...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [HD-Prot: A Protein Language Model for Joint Sequence-Structure Modeling with Continuous Structure Tokens](http://arxiv.org/abs/2512.15133v3)
  来源：arXiv | 日期：2025-12-17 | 相关度：8.5 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Proteins inherently possess a consistent sequence-structure duality. The abundance of protein sequence data, which can be readily represented as discrete tokens, has driven fruitful developments in protein language model...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Explainable protein-protein binding affinity prediction via fine-tuning protein language models](https://www.biorxiv.org/content/10.64898/2026.03.30.715237v2)
  来源：bioRxiv | 日期：2026-06-11 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Protein-protein interactions underpin virtually every aspect of cellular life, and the precise quantification of their binding affinity is fundamental to understanding immune recognition, disease mechanisms, and the rati...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [PHI-Reason: evidence-grounded species-level phage-host prediction from structured biological text profiles](https://www.biorxiv.org/content/10.64898/2026.06.10.727770v1)
  来源：bioRxiv | 日期：2026-06-12 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Phage--host interaction (PHI) prediction is a fundamental problem in microbiology with applications in microbial ecology and microbiome engineering. Existing computational approaches typically convert phage and host info...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CAREPath: Semantic Context-Aware Reasoning Paths with Mechanism-Augmented Embeddings for Drug Repurposing](https://www.biorxiv.org/content/10.64898/2026.06.09.731247v1)
  来源：bioRxiv | 日期：2026-06-12 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Biomedical knowledge graphs (BKGs) that include drugs, genes, and diseases support drug repurposing by connecting drugs to diseases through gene-mediated multi-hop paths, thereby enabling mechanism-of-action reasoning. H...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [scLLM-DSC: LLM-Knowledge Enhanced Cross-Modal Deep Structural Clustering for Single-Cell RNA Sequencing](http://arxiv.org/abs/2606.13007v1)
  来源：arXiv | 日期：2026-06-11 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Clustering is fundamental to scRNA-seq analysis, serving as a cornerstone for identifying cell populations and resolving tissue heterogeneity. However, existing methods focus on mining numerical statistical patterns, suf...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GermRL: Alleviating The Germline Bias In Autoregressive Antibody Language Models Through Reinforcement Learning](https://www.biorxiv.org/content/10.64898/2026.06.08.730660v1)
  来源：bioRxiv | 日期：2026-06-11 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Antibodies are powerful therapeutics whose antigen specificity arises from sequence diversity shaped during development. Recently, language models trained on large antibody repertoire datasets have enabled the generation...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Viability of engineered AAVs via protein language models](https://www.biorxiv.org/content/10.64898/2026.06.11.731521v1)
  来源：bioRxiv | 日期：2026-06-11 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Capsid engineering has greatly improved the performance of recombinant AAV vectors used for gene therapy. One commonly used strategy is the insertion of a short, 7-mer, peptide into surface-exposed loops to modify recept...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [An AI-Powered Trisomy 21 Research Assistant](https://www.biorxiv.org/content/10.64898/2026.06.08.730893v1)
  来源：bioRxiv | 日期：2026-06-11 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Down syndrome, caused by trisomy 21, increases the risk of diverse co-occurring conditions. With more than 34,000 related publications indexed in PubMed as of early 2026, keeping pace with this expanding literature is ch...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Reproducibility of AI-Generated Antibiotic Recommendations in Standardized Clinical Scenarios: A Proof-of-Concept Experimental Study.](https://pubmed.ncbi.nlm.nih.gov/42285312/)
  来源：PubMed | 日期：2026-06-12 | 相关度：8.65 | 新颖度：0.75
  匹配主题：foundation_model_agent, application_monitoring
  中文摘要：Artificial intelligence (AI) tools are increasingly used to support antimicrobial prescribing, but most published literature focuses on accuracy rather than reproducibility across identical inputs. Reproducibility is a k...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Beyond Injection Detection: A Positive-Security Prompt Firewall that Closes the Scope and PHI Gap SOTA Classifiers Miss in Healthcare](https://www.medrxiv.org/content/10.64898/2026.06.04.26354950v2)
  来源：medRxiv | 日期：2026-06-11 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models embedded in autonomous agents process trusted instructions and untrusted data in one context window, leaving them open to direct and indirect prompt injection. In healthcare this is not hypothetical...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [One Polluted Page Is Enough: Evaluating Web Content Pollution in Generative Recommenders](http://arxiv.org/abs/2606.13610v1)
  来源：arXiv | 日期：2026-06-11 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Search-augmented LLMs increasingly mediate everyday consumer recommendations by retrieving live web content. This creates a new risk: generative recommenders may consume polluted web content, such as fake reviews and pro...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific Discovery](http://arxiv.org/abs/2606.13662v1)
  来源：arXiv | 日期：2026-06-11 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：LLM-based agents have shown increasing potential in automating scientific discovery. Given an optimizable metric and an execution environment, they can propose, validate, and iterate scientific solutions, and have produc...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [TimeLens: On-Device Artifact Recognition with Retrieval-Augmented Question Answering for the Grand Egyptian Museum](http://arxiv.org/abs/2606.13267v1)
  来源：arXiv | 日期：2026-06-11 | 相关度：5.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：TimeLens is an AI-powered bilingual mobile guide for the Grand Egyptian Museum (GEM). Pointing a phone at an exhibit, a visitor sees the artifact recognized in real time and can ask follow-up questions answered in Englis...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [SkMTEB: Slovak Massive Text Embedding Benchmark and Model Adaptation](http://arxiv.org/abs/2606.13647v1)
  来源：arXiv | 日期：2026-06-11 | 相关度：5.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：We introduce SkMTEB, the first comprehensive MTEB-style text embedding benchmark for Slovak, a low-resource West Slavic language, comprising 31 datasets across 7 task types -- nearly 4$\times$ the depth of existing multi...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [DCD: Domain-Oriented Design for Controlled Retrieval-Augmented Generation](http://arxiv.org/abs/2604.07590v2)
  来源：arXiv | 日期：2026-04-08 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) is widely used to ground large language models in external knowledge sources. However, when applied to heterogeneous corpora and multi-step queries, Naive RAG pipelines often degrade ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Rethinking RAG in Long Videos: What to Retrieve and How to Use It?](http://arxiv.org/abs/2606.13141v1)
  来源：arXiv | 日期：2026-06-11 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation is moving beyond text into long, egocentric video, where systems must select query-relevant chunks across multiple modalities and temporal granularities. Yet progress in VideoRAG is limited...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Learning to Reason by Analogy via Retrieval-Augmented Reinforcement Fine-Tuning](http://arxiv.org/abs/2606.13680v1)
  来源：arXiv | 日期：2026-06-11 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) has become a standard mechanism for grounding language models in external knowledge, yet conventional retrieval based on lexical or semantic similarity is poorly suited for complex re...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CQC-RAG: Robust Retrieval-Augmented Generation via Cross-Query Consistency](http://arxiv.org/abs/2606.13438v1)
  来源：arXiv | 日期：2026-06-11 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) has become a common approach for improving the factuality of Large Language Models (LLMs), yet its reliability remains highly sensitive to how external evidence is retrieved and used....
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [HoloCell: A Generative Foundation Model for Holistic Cellular Modeling](https://www.biorxiv.org/content/10.64898/2026.06.07.730684v1)
  来源：bioRxiv | 日期：2026-06-11 | 相关度：2.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Single-cell multi-omics technologies have recently advanced to enable the profiling of epigenomic, transcriptomic, and proteomic layers within individual cells, offering new opportunities to characterize cellular states ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Under What Conditions Can a Machine Become Genuinely Creative?](http://arxiv.org/abs/2606.13196v1)
  来源：arXiv | 日期：2026-06-11 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Recent AI systems can generate texts, software architectures, hypotheses, designs, and scientific workflows that appear creative. This paper asks under what conditions a machine can become genuinely creative, and how hum...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Multi-Field Hybrid Retrieval-Augmented Generation for Maritime Accident Root Cause Analysis](http://arxiv.org/abs/2606.13249v1)
  来源：arXiv | 日期：2026-06-11 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Maritime accident adjudication reports contain critical tribunal findings for root cause analysis (RCA), yet retrieving relevant precedents and drafting consistent reports from decades of records remains labor-intensive....
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Uncertainty-Aware Hybrid Retrieval for Long-Document RAG](http://arxiv.org/abs/2606.13550v1)
  来源：arXiv | 日期：2026-06-11 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Retrieval augmented generation (RAG) depends critically on the quality and granularity of retrieved evidence. Large retrieval units preserve context but often introduce irrelevant content, which can dilute answer bearing...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Blood Culture-Negative Infective Endocarditis: A Review.](https://pubmed.ncbi.nlm.nih.gov/42271556/)
  来源：PubMed | 日期：2026-06-11 | 相关度：4.0 | 新颖度：0.25
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Blood culture-negative infective endocarditis (BCNIE) represents a diagnostically challenging subset of infective endocarditis in which routine blood cultures remain negative despite fulfillment of Duke-ISCVID diagnostic...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Conversational Speech for Respiratory Triage in Primary Care: A Pilot Study](https://www.medrxiv.org/content/10.64898/2026.06.09.26355284v1)
  来源：medRxiv | 日期：2026-06-11 | 相关度：2.65 | 新颖度：0.75
  匹配主题：sequencing_bioinformatics
  中文摘要：Background. Respiratory complaints account for a substantial share of adult ambulatory care visits, and triaging them accurately has direct consequences for antibiotic stewardship and pathogen-specific therapy. Prior wor...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
