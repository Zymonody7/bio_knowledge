# 每日论文监控日报 (2026-05-13)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 60 篇新论文。

## 抓取状态

- arXiv：成功，命中 60 篇
- PubMed：成功，命中 51 篇
- bioRxiv：成功，命中 16 篇
- medRxiv：成功，命中 7 篇

## 最值得看

### 方法创新

- [A fine-tuned genomic language model adds complementary nucleotide-context information to missense variant interpretation](https://www.biorxiv.org/content/10.64898/2026.05.06.723362v1)
  来源：bioRxiv | 日期：2026-05-11 | 相关度：10.0 | 新颖度：5.5
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Missense variant interpretation remains a central challenge in clinical genomics. Missense pathogenicity predictors achieve strong performance, but many emphasize protein-level consequences or overlapping annotation prio...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Shaping the future of postoperative recurrence in Crohn's disease: personalised approaches with AI-enabled imaging and multi-omics.](https://pubmed.ncbi.nlm.nih.gov/41592952/)
  来源：PubMed | 日期：2026-05-12 | 相关度：9.7 | 新颖度：5.5
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Postoperative recurrence (POR) is a major challenge in the long-term management of Crohn's disease (CD), affecting up to 70% of patients within the first year after surgical resection. The multifactorial pathogenesis of ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Artificial Intelligence for Colorectal Surgeons - Part II: Research Applications, Challenges in Adoption and Practical Resources.](https://pubmed.ncbi.nlm.nih.gov/42117468/)
  来源：PubMed | 日期：2026-05-12 | 相关度：7.8 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：This is Part II of a two-part series examining artificial intelligence (AI) in colorectal surgery. Part I established foundational concepts and clinical applications. Implementation, however, requires understanding resea...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 可追踪

### Foundation Model / Agent

- [SAR-RAG: ATR Visual Question Answering by Semantic Search, Retrieval, and MLLM Generation](http://arxiv.org/abs/2602.04712v2)
  来源：arXiv | 日期：2026-02-04 | 相关度：7.9 | 新颖度：1.2
  匹配主题：foundation_model_agent
  中文摘要：We present a visual-context image-retrieval-augmented generation (ImageRAG)- assisted AI agent for automatic target recognition (ATR) of synthetic aperture radar (SAR) imagery. SAR is a remote sensing method used in defe...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agents Should Replace Narrow Predictive AI as the Orchestrator in 6G AI-RAN](http://arxiv.org/abs/2605.11516v1)
  来源：arXiv | 日期：2026-05-12 | 相关度：7.5 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：This position paper argues that to achieve Level 5 autonomous 6G networks, the next generation of Artificial Intelligence in Radio Access Networks (AI-RAN) should transition away from fragmented, narrow predictive models...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Geospatial-Temporal Sensemaking of Remote Sensing Activity Detections with Multimodal Large Language Model](http://arxiv.org/abs/2605.10739v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：7.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：We introduce SMART-HC-VQA, a Sentinel-2-based visual question answering dataset derived from the IARPA SMART Heavy Construction dataset, designed for spatiotemporal analysis of human activity. The dataset transforms cons...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LegalCheck: Retrieval- and Context-Augmented Generation for Drafting Municipal Legal Advice Letters](http://arxiv.org/abs/2605.12012v1)
  来源：arXiv | 日期：2026-05-12 | 相关度：6.55 | 新颖度：7.38
  匹配主题：foundation_model_agent
  中文摘要：Public-sector legal departments in the Netherlands face acute staff shortages, increased case volumes, and increased pressure to meet regulatory compliance. This paper presents LegalCheck, a novel system that addresses t...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Leveraging RAG for Training-Free Alignment of LLMs](http://arxiv.org/abs/2605.11217v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：6.55 | 新颖度：6.2
  匹配主题：foundation_model_agent
  中文摘要：Large language model (LLM) alignment algorithms typically consist of post-training over preference pairs. While such algorithms are widely used to enable safety guardrails and align LLMs with general human preferences, w...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Discovery of Interpretable Surrogates via Agentic AI: Application to Gravitational Waves](http://arxiv.org/abs/2605.11280v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Fast surrogate models for expensive simulations are now essential across the sciences, yet they typically operate as black boxes. We present \texttt{GWAgent}, a large language model (LLM)-based workflow that constructs i...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Theory of Multilevel Interactive Equilibrium in NeuroAI](http://arxiv.org/abs/2605.10505v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：6.55 | 新颖度：1.2
  匹配主题：foundation_model_agent
  中文摘要：We propose a game-theoretic framework for adaptive multi-agent intelligent systems. Unlike classical game theory, which often treats strategies as primitive objects chosen by perfectly rational agents, the proposed frame...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LEAPS: An LLM-Empowered Adaptive Plugin in Taobao AI Search](http://arxiv.org/abs/2601.05513v2)
  来源：arXiv | 日期：2026-01-09 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：The rapid rise of large language models has shifted user search behavior from discrete keywords to natural-language, multi-constraint queries--a shift existing e-commerce search architectures struggle to accommodate. Use...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Adversarial SQL Injection Generation with LLM-Based Architectures](http://arxiv.org/abs/2605.11188v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：SQL injection (SQLi) attacks are still one of the serious attacks ranked in the Open Worldwide Application Security Project (OWASP) Top 10 threats. Today, with advances in Artificial Intelligence (AI), especially in Larg...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Bridging Dual Knowledge Graphs for Multi-Hop Question Answering in Construction Safety](http://arxiv.org/abs/2507.13625v2)
  来源：arXiv | 日期：2025-07-18 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Information retrieval and question answering from safety regulations are essential for automated construction compliance checking but are hindered by the linguistic and structural complexity of regulatory text. Many quer...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [VulTriage: Triple-Path Context Augmentation for LLM-Based Vulnerability Detection](http://arxiv.org/abs/2605.09461v2)
  来源：arXiv | 日期：2026-05-10 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Automated vulnerability detection is a fundamental task in software security, yet existing learning-based methods still struggle to capture the structural dependencies, domain-specific vulnerability knowledge, and comple...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Toward Autonomous Computational Catalysis Research via Agentic Systems](http://arxiv.org/abs/2601.13508v3)
  来源：arXiv | 日期：2026-01-20 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Fully autonomous science has long been a defining ambition for artificial intelligence in materials discovery, yet its realization requires more than automating isolated calculations. In computational catalysis, a system...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ANCHOR: Abductive Network Construction with Hierarchical Orchestration for Reliable Probability Inference in Large Language Models](http://arxiv.org/abs/2605.10328v2)
  来源：arXiv | 日期：2026-05-11 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：A central challenge in large-scale decision-making under incomplete information is estimating reliable probabilities. Recent approaches use Large Language Models (LLMs) to generate explanatory factors and coarse-grained ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [MedHopQA: A Disease-Centered Multi-Hop Reasoning Benchmark and Evaluation Framework for LLM-Based Biomedical Question Answering](http://arxiv.org/abs/2605.12361v1)
  来源：arXiv | 日期：2026-05-12 | 相关度：5.75 | 新颖度：8.18
  匹配主题：foundation_model_agent
  中文摘要：Evaluating large language models (LLMs) in the biomedical domain requires benchmarks that can distinguish reasoning from pattern matching and remain discriminative as model capabilities improve. Existing biomedical quest...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [SCOPE: Siamese Contrastive Operon Pair Embeddings for Functional Sequence Representation and Classification](http://arxiv.org/abs/2605.11022v1)
  来源：arXiv | 日期：2026-05-10 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Identifying operons is a fundamental step in understanding prokaryotic gene regulation, as classifying genes into operons supports the reconstruction of regulatory networks, functional annotation of unannotated genes, an...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Towards Order Fairness: Mitigating LLMs Order Sensitivity through Dual Group Advantage Optimization](http://arxiv.org/abs/2605.11974v1)
  来源：arXiv | 日期：2026-05-12 | 相关度：5.45 | 新颖度：7.1
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) suffer from order bias, where their performance is affected by the arrangement order of input elements. This unfairness limits the model's applications in scenarios such as in-context learnin...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Overview of the MedHopQA track at BioCreative IX: track description, participation and evaluation of systems for multi-hop medical question answering](http://arxiv.org/abs/2605.12313v1)
  来源：arXiv | 日期：2026-05-12 | 相关度：4.75 | 新颖度：8.09
  匹配主题：foundation_model_agent
  中文摘要：Multi-hop question answering (QA) remains a significant challenge in the biomedical domain, requiring systems to integrate information across multiple sources to answer complex questions. To address this problem, the Bio...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [VLADriver-RAG: Retrieval-Augmented Vision-Language-Action Models for Autonomous Driving](http://arxiv.org/abs/2605.08133v2)
  来源：arXiv | 日期：2026-05-01 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving, yet their reliance on implicit parametric knowledge limits generalization in long-tail scenarios. While Retrieva...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Protein language model-guided generative design of affinity peptides for chromatographic purification of lentiviral vectors.](https://pubmed.ncbi.nlm.nih.gov/41833101/)
  来源：PubMed | 日期：2026-05-10 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Lentiviral vectors (LVs) have emerged as the most promising tool for cell and gene therapy. However, LVs are very fragile and sensitive to shear stress, buffer pH and salt concentration, resulting in serious hurdles in d...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RIMGOGraph: integrating AlphaFold-derived residue interaction graphs and protein language embeddings for structure-informed protein function prediction.](https://pubmed.ncbi.nlm.nih.gov/42119874/)
  来源：PubMed | 日期：2026-05-11 | 相关度：7.1 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Accurate protein function annotation remains a major challenge in computational biology because the growth of protein sequence and structural databases continues to outpace experimental characterization. Recent advances ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Evaluating Genomic Surveillance Methods for Shigella sonnei in a High-Income Setting](https://www.medrxiv.org/content/10.64898/2026.05.08.26352707v1)
  来源：medRxiv | 日期：2026-05-12 | 相关度：6.0 | 新颖度：5.75
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Shigella sonnei is a human-adapted enteric pathogen with a very low infectious dose and increasing antimicrobial resistance. In high-income settings, transmission is multimodal including sporadic cases/outbreaks associat...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Courtroom-Style Multi-Agent Debate with Progressive RAG and Role-Switching for Controversial Claim Verification](http://arxiv.org/abs/2603.28488v2)
  来源：arXiv | 日期：2026-03-30 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) remain unreliable for high-stakes claim verification due to hallucinations and shallow reasoning. While retrieval-augmented generation (RAG) and multi-agent debate (MAD) address this, they ar...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GRC: Unifying Reasoning-Driven Generation, Retrieval and Compression](http://arxiv.org/abs/2605.09100v2)
  来源：arXiv | 日期：2026-05-09 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Text embedding and generative tasks are usually trained separately based on large language models (LLMs) nowadays. This causes a large amount of training cost and deployment effort. Context compression is also a challeng...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Letting the neural code speak: Automated characterization of monkey visual neurons through human language](http://arxiv.org/abs/2605.12485v1)
  来源：arXiv | 日期：2026-05-12 | 相关度：4.75 | 新颖度：7.42
  匹配主题：foundation_model_agent
  中文摘要：Understanding what individual neurons encode is a core question in neuroscience. In primary visual cortex (V1), mathematical models (e.g., Gabor functions) capture neural selectivity, but no comparable framework exists f...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Differentially Private Synthetic Text Generation for Retrieval-Augmented Generation (RAG)](http://arxiv.org/abs/2510.06719v2)
  来源：arXiv | 日期：2025-10-08 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) enhances large language models (LLMs) by grounding them in external knowledge. However, its application in sensitive domains is limited by privacy risks. Existing private RAG methods ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Route Before Retrieve: Activating Latent Routing Abilities of LLMs for RAG vs. Long-Context Selection](http://arxiv.org/abs/2605.10235v2)
  来源：arXiv | 日期：2026-05-11 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in large language models (LLMs) have expanded the context window to beyond 128K tokens, enabling long-document understanding and multi-source reasoning. A key challenge, however, lies in choosing between ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [Towards Verifiable and Self-Correcting AI Physicists for Quantum Many-Body Simulations](http://arxiv.org/abs/2604.00149v2)
  来源：arXiv | 日期：2026-03-31 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：While large language models (LLMs) promise to revolutionize automated scientific discovery, their application in rigorous real-world physical research is stalled by two critical barriers: a lack of realistic evaluation b...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Polymer-Agent: Large Language Model Agent for Polymer Design.](https://pubmed.ncbi.nlm.nih.gov/42048526/)
  来源：PubMed | 日期：2026-05-11 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：按需聚合物发现对于从生物医学应用到增强材料的各个行业都至关重要。传统的聚合物实验涉及漫长的试错过程，消耗大量资源。虽然机器学习在性能预测和潜空间搜索方面加速了科学发现，但受限于基础设施，实验室研究人员往往难以直接调用代码和模型来提取特定结构与性能。本文提出了 Polymer-Agent，这是一个集成在终端中的闭环聚合物结构-性能预测框架，用于早期聚合物发现。该框架利用大语言模型（LLM）的推理能力，为用户提供性能预测、性能导向的聚合物结...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MolRGen: A Training and Evaluation Setting for De Novo Molecular Generation with Reasonning Models](http://arxiv.org/abs/2603.18256v2)
  来源：arXiv | 日期：2026-03-18 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Recent reasoning-based large language models have shown strong performance on tasks with verifiable outcomes, but their use in de novo molecular generation remains limited by the lack of training environments where rewar...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PathISE: Learning Informative Path Supervision for Knowledge Graph Question Answering](http://arxiv.org/abs/2605.10791v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Knowledge Graph Question Answering (KGQA) aims to answer user questions by reasoning over Knowledge Graphs (KGs). Recent KGQA methods mainly follow the retrieval-augmented generation paradigm to ground Large Language Mod...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PrimeKG-CL: A Continual Graph Learning Benchmark on Evolving Biomedical Knowledge Graphs](http://arxiv.org/abs/2605.10529v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：3.1 | 新颖度：1.75
  匹配主题：未命中具体主题
  中文摘要：Biomedical knowledge graphs underwrite drug repurposing and clinical decision support, yet the upstream ontologies they depend on update on independent cycles that add millions of edges and deprecate hundreds of thousand...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multimodal predictions of end stage chronic kidney disease from asymptomatic individuals for discovery of genomic biomarkers.](https://pubmed.ncbi.nlm.nih.gov/42120994/)
  来源：PubMed | 日期：2026-05-12 | 相关度：3.05 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Chronic kidney disease (CKD) is a complex condition where the kidneys are damaged and progressively lose their ability to filter blood, 10% of the world population have the disease that often goes undetected until it is ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Knowledge Poisoning Attacks on Medical Multi-Modal Retrieval-Augmented Generation](http://arxiv.org/abs/2605.10253v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：2.75 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) is a widely adopted paradigm for enhancing LLMs in medical applications by incorporating expert multimodal knowledge during generation. However, the underlying retrieval databases may...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Very Efficient Listwise Multimodal Reranking for Long Documents](http://arxiv.org/abs/2605.11864v1)
  来源：arXiv | 日期：2026-05-12 | 相关度：2.5 | 新颖度：7.3
  匹配主题：未命中具体主题
  中文摘要：Listwise reranking is a key yet computationally expensive component in vision-centric retrieval and multimodal retrieval-augmented generation (M-RAG) over long documents. While recent VLM-based rerankers achieve strong a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ProfiliTable: Profiling-Driven Tabular Data Processing via Agentic Workflows](http://arxiv.org/abs/2605.12376v1)
  来源：arXiv | 日期：2026-05-12 | 相关度：1.4 | 新颖度：7.96
  匹配主题：未命中具体主题
  中文摘要：表格处理（包括清洗、转换、增强和匹配）是数据流水线中基础但易出错的阶段。尽管基于大语言模型（LLM）的方法在自动化此类任务方面具有潜力，但面对模糊指令、复杂任务结构及缺乏结构化反馈时，常生成语法正确但语义错误的代码。为此，本文提出 ProfiliTable，一个以动态剖析为核心的自主多智能体框架。该框架通过交互式探索、知识增强合成和反馈驱动优化，构建并迭代完善统一的执行上下文。ProfiliTable 集成了三个核心组件：(i) 剖析器...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond RAG for Agent Memory: Retrieval by Decoupling and Aggregation](http://arxiv.org/abs/2602.02007v4)
  来源：arXiv | 日期：2026-02-02 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：标准的检索增强生成（RAG）与智能体记忆的需求并不匹配。与大型异构语料库不同，智能体记忆由有界且连贯的交互流组成，其中许多片段高度相关或近乎重复。因此，传统的 top-k 相似度检索常返回冗余上下文，而以摘要为中心的层级结构则可能模糊区分候选信息的细微细节。本文提出智能体记忆应遵循“先解耦后聚合”的原则：系统应首先从相似历史中分离出可重用的事实、更新和区分性细节，然后再进行组织以实现高效检索。基于此，我们提出了 xMemory，它构建了...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CVEvolve: Autonomous Algorithm Discovery for Unstructured Scientific Data Processing](http://arxiv.org/abs/2605.11359v1)
  来源：arXiv | 日期：2026-05-12 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：科学数据处理通常需要特定任务的算法或AI模型，这为缺乏计算或图像处理专业知识的领域科学家分析噪声大、高动态范围、稀疏标记或定义模糊的数据带来了障碍。本研究推出了 CVEvolve，一个具备零代码界面的自主智能体框架，用于科学数据处理算法的自动发现。CVEvolve 结合了多轮搜索策略与代码执行、评估实现、历史管理、留出测试以及对科学数据和视觉输出的可选检查工具。其搜索机制在“发现”与“改进”操作间交替，并利用谱系感知的随机候选采样来平衡...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Clever Hans to Scientific Discovery: Interpreting EEG Foundational Transformers with LRP](http://arxiv.org/abs/2605.11885v1)
  来源：arXiv | 日期：2026-05-12 | 相关度：0.7 | 新颖度：6.59
  匹配主题：未命中具体主题
  中文摘要：脑电图（EEG）领域新兴的基础模型（FMs）有望在数据稀缺的情况下，为临床诊断和脑机接口提供深度学习扩展路径，但其黑盒特性阻碍了广泛应用。本研究探讨了注意力感知的逐层相关性传播（LRP）作为 EEG-FMs 的事后归因方法，将 LRP 从传统的卷积神经网络（CNN）扩展到当前基础模型所采用的 Transformer 架构。研究发现，LRP 既能验证 EEG-FM 的决策逻辑，也能从中提出具有生物学合理性的新科学假设。在运动想象任务中，L...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Geometric coherence of single-cell CRISPR perturbations reveals regulatory architecture and predicts cellular stress](http://arxiv.org/abs/2604.16642v2)
  来源：arXiv | 日期：2026-04-17 | 相关度：0.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：基因组工程虽已实现序列级精准，但预测扰动后的转录组状态仍是难题。单细胞CRISPR筛选通常测量细胞偏离未扰动状态的距离（效应强度），但忽略了细胞是否协同移动。本研究引入几何稳定性指标 Shesha，通过计算个体细胞位移向量与平均扰动方向间的平均余弦相似度，量化单细胞扰动响应的方向一致性。在涵盖 CRISPRa、CRISPRi 和混合筛选的 5 个数据集（2,200 多个扰动）中，稳定性与效应强度强相关（Spearman ρ=0.75-0...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The Override Gap: A Magnitude Account of Knowledge Conflict Failure in Hypernetwork-Based Instant LLM Adaptation](http://arxiv.org/abs/2604.23750v2)
  来源：arXiv | 日期：2026-04-26 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：基于超网络的方法（如 Doc-to-LoRA）能通过单次前向传播将文档信息内化至大语言模型（LLM）权重中，但在处理知识冲突时存在系统性失效：当文档内容与预训练知识矛盾时，深度事实的准确率会骤降至 46.4%。研究发现，这种失效本质上是“量级（Magnitude）”问题而非表征问题。超网络虽能定位正确的层，但其适配器边际在不同文档间基本恒定，而预训练知识的边际随训练频率增长，导致深度冲突在结构上难以被覆盖。实验通过对 194 个冲突点按...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [The landscape of structural variation in pediatric cancer.](https://pubmed.ncbi.nlm.nih.gov/41825442/)
  来源：PubMed | 日期：2026-05-11 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：结构变异（SVs）占儿童癌症驱动变异的60%以上。本研究通过对1,616例儿童和2,203例成人全基因组（WGS）的泛癌分析显示，儿童癌症的SV负荷在不同癌种间存在约100倍的差异。与成人脑肿瘤和实体瘤相比，儿童的SV负荷降低了6至16倍，但在血液恶性肿瘤中两者相当。研究发现，受SV破坏最严重的基因在儿童癌症中多为驱动基因，而在成人癌症中则多为脆性位点。在儿童急性淋巴细胞白血病中，RAG重组信号序列附近的复发性SV热点会同时破坏免疫位点...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [CuSearch: Curriculum Rollout Sampling via Search Depth for Agentic RAG](http://arxiv.org/abs/2605.11611v1)
  来源：arXiv | 日期：2026-05-12 | 相关度：0.7 | 新颖度：5.54
  匹配主题：未命中具体主题
  中文摘要：具有可验证奖励的强化学习（RLVR）已成为从仅结果监督中训练代理式检索增强生成（RAG）系统的有效范式。然而，现有方法通常对采样轨迹进行均匀优化，忽略了不同轨迹在搜索深度上的差异。深层搜索轨迹包含更多检索决策点，能为检索子策略提供更密集的直接监督。为此，本文提出 CuSearch 框架，核心是搜索深度贪婪分配（SDGA）算子，旨在将固定更新预算重新分配给深层轨迹。SDGA-Auto 自动针对当前批次中最深的轨迹，随训练进程形成隐式课程；...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [PTM-dCN: Latent Space Control for Post-translational Modification-aware Protein Design](https://www.biorxiv.org/content/10.64898/2026.05.06.714367v1)
  来源：bioRxiv | 日期：2026-05-11 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Post-translational modifications (PTMs) are critical for protein function, yet their precise design by harnessing site specific information derived from native proteins remains challenging. Here, we present a deep learni...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [The Truth Lies Somewhere in the Middle (of the Generated Tokens)](http://arxiv.org/abs/2605.09969v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：How should hidden states generated autoregressively be collapsed into a representation that reflects a language model's internal state? Despite tokens being generated under causal masking, we find that mean pooling acros...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Grounded Satirical Generation with RAG](http://arxiv.org/abs/2605.10853v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Humor generation remains challenging task for Large Language Models (LLMs), due to their subjective nature. We focus on satire, a form of humor strongly shaped by context. In this work, we present a novel pipeline for gr...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Understand and Accelerate Memory Processing Pipeline for Disaggregated LLM Inference](http://arxiv.org/abs/2603.29002v2)
  来源：arXiv | 日期：2026-03-30 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Modern large language models (LLMs) increasingly depends on efficient long-context processing and generation mechanisms, including sparse attention, retrieval-augmented generation (RAG), and compressed contextual memory,...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Persistent and Conversational Multi-Method Explainability for Trustworthy Financial AI](http://arxiv.org/abs/2605.11687v1)
  来源：arXiv | 日期：2026-05-12 | 相关度：2.75 | 新颖度：5.97
  匹配主题：foundation_model_agent
  中文摘要：Financial institutions increasingly require AI explanations that are persistent, cross-validated across methods, and conversationally accessible to human decision-makers. We present an architecture for human-centered exp...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MoLF: Mixture-of-Latent-Flow for Pan-Cancer Spatial Gene Expression Prediction from Histology](http://arxiv.org/abs/2602.02282v3)
  来源：arXiv | 日期：2026-02-02 | 相关度：2.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：Inferring spatial transcriptomics (ST) from histology enables scalable histogenomic profiling, yet current methods are largely restricted to single-tissue models. This fragmentation fails to leverage biological principle...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Cosine Similarity Conflates Clinically Distinct Cancer Variants: A Case for Typed-Graph Retrieval in Precision Oncology Decision Support](https://www.biorxiv.org/content/10.64898/2026.05.05.723102v1)
  来源：bioRxiv | 日期：2026-05-11 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Cancer variant interpretation increasingly relies on retrieval from biomedical knowledge bases, with cosine similarity over neural text embeddings now the dominant retrieval substrate. Whether these embeddings preserve t...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RNA-FM: Flow-Matching Generative Model for Genome-wide RNA-Seq Prediction](http://arxiv.org/abs/2605.11622v1)
  来源：arXiv | 日期：2026-05-12 | 相关度：1.7 | 新颖度：5.56
  匹配主题：未命中具体主题
  中文摘要：Histopathology whole-slide images (WSIs) are routinely acquired in clinical practice and contain rich tissue morphology but lack direct molecular architecture and functional programs defining pathological states, whereas...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [eSkip2 prioritizes exon-skipping antisense oligonucleotide target regions across exon--intron contexts](https://www.biorxiv.org/content/10.64898/2026.05.05.722571v1)
  来源：bioRxiv | 日期：2026-05-11 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：用于外显子跳跃的反义寡核苷酸（ASO）正越来越多地被用于纠正致病性剪接，但由于调控信息分布在外显子、内含子和剪接接头中，合理选择目标区域仍具挑战。本研究提出了 eSkip2，这是一个利用外显子-内含子联合序列背景优先排序 ASO 目标区域的框架。eSkip2 结合了基因组预训练基础模型的迁移学习，以及 ASO 活性和单核苷酸变异（SNV）衍生的剪接扰动数据的联合训练，且无需实验性 ASO 标签即可适应特定的目标位点。在涵盖规范外显子、伪...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GRAFT-ATHENA: Self-Improving Agentic Teams for Autonomous Discovery and Evolutionary Numerical Algorithms](http://arxiv.org/abs/2605.11117v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：科学发现可建模为从物理问题到数值解的概率决策序列。现有的智能体系统虽能自动化单个任务，但通常孤立处理问题，缺乏跨领域的经验积累。本文提出了 GRAFT-ATHENA，一种具有自改进能力的智能体框架，能从既往问题中学习并自主扩展其跨领域动作空间。GRAFT（图归约为自适应分解树）将组合决策空间投影为分解概率树，使参数规模从指数级降至线性。该框架利用贝叶斯网络原理，将方法路径嵌入度量空间，使新问题能借鉴相似的历史经验。在物理信息机器学习（P...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Response-G1: Explicit Scene Graph Modeling for Proactive Streaming Video Understanding](http://arxiv.org/abs/2605.07575v2)
  来源：arXiv | 日期：2026-05-08 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：主动式流式视频理解要求视频大语言模型（Video-LLMs）在视频展开过程中自主决定何时做出响应，但现有方法因采用隐式且与查询无关的视觉证据建模，导致响应时机不准。本文提出 Response-G1 框架，通过场景图（Scene Graphs）在累积的视频证据与查询预期的响应条件之间建立显式的结构化对齐。该框架包含三个无需微调的阶段：(1) 从流式片段中生成在线查询引导的场景图；(2) 基于内存检索语义最相关的历史场景图；(3) 利用检索...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Qwen Goes Brrr: Off-the-Shelf RAG for Ukrainian Multi-Domain Document Understanding](http://arxiv.org/abs/2605.10296v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：We participated in the Fifth UNLP shared task on multi-domain document understanding, where systems must answer Ukrainian multiple-choice questions from PDF collections and localize the supporting document and page. We p...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Three Decades of FDA Authorizations of AI/ML Enabled Medical Devices: Persistent Specialty Concentration and the Care Delivery Gap (1995 to 2025)](https://www.medrxiv.org/content/10.64898/2026.05.08.26352766v1)
  来源：medRxiv | 日期：2026-05-12 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：The US Food and Drug Administration (FDA) maintains a public list of artificial intelligence and machine learning (AI/ML)-enabled medical devices that have received marketing authorization. Prior published analyses exami...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Bridging innovation and implementation in laboratory medicine: insights from a global survey on unmet needs and emerging technologies.](https://pubmed.ncbi.nlm.nih.gov/42119761/)
  来源：PubMed | 日期：2026-05-11 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Technological innovation in laboratory medicine is advancing rapidly, driven by artificial intelligence, next-generation sequencing, high-resolution mass spectrometry, novel biomarkers, and decentralized point-of-care te...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [MPEX AI Digital Twins Milestone Report](http://arxiv.org/abs/2605.12116v1)
  来源：arXiv | 日期：2026-05-12 | 相关度：0.7 | 新颖度：6.68
  匹配主题：未命中具体主题
  中文摘要：本报告是提交给聚变能源科学（FES）和美国科学云（AmSC）的 MPEX AI 数字孪生项目启动六个月后的进度报告。该项目旨在展示人工智能（AI）在材料等离子体暴露实验（MPEX）运行和科学发现中的优势，计划于 2026 年 6 月完成两个关键里程碑。第一个里程碑是 Helicon AI 热点控制器，它是更全面的 MPEX AI 热点数字孪生系统的核心加热组件。第二个里程碑是电子束（E-beam）损伤评估数字孪生，作为 MPEX AI ...
  为什么值得看：MPEX AI Digital Twins Milestone Report 与你的主题有弱匹配，暂时保留作低优先级跟踪。
