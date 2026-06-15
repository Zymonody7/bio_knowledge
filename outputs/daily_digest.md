# 每日论文监控日报 (2026-06-15)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 16 篇新论文。

## 抓取状态

- arXiv：成功，命中 9 篇
- PubMed：成功，命中 25 篇
- bioRxiv：成功，命中 15 篇
- medRxiv：成功，命中 2 篇

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [MyeGPT: an AI agent for Multiple Myeloma](https://www.medrxiv.org/content/10.64898/2026.05.14.26353252v5)
  来源：medRxiv | 日期：2026-06-14 | 相关度：7.55 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Today, advancements in our understanding of cancer biology are increasingly attributed to large-scale clinical-molecular datasets. The case in point for multiple myeloma - the second-most prevalent haematological maligna...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Large Language Model Based Agent for Automated Discovery in Computational Physics](http://arxiv.org/abs/2606.14266v1)
  来源：arXiv | 日期：2026-06-12 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Scientific discovery in computational physics can often be framed as the optimization of quantitatively evaluable objectives subject to physical constraints. While researchers excel at formulating such problems, they fre...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Verifiable User Simulation for Search and Recommendation Systems](http://arxiv.org/abs/2606.14474v1)
  来源：arXiv | 日期：2026-06-12 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Large-language-model (LLM) based user simulation is increasingly adopted for evaluating search engines, recommender systems, and retrieval-augmented generation pipelines, yet most simulators remain opaque: it is difficul...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [MoE-Bind: Guiding De Novo Protein Binder Generation with Sparse Experts](https://www.biorxiv.org/content/10.64898/2026.06.13.732043v1)
  来源：bioRxiv | 日期：2026-06-13 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：De novo protein binder design has been dominated by structure-based pipelines that require known three-dimensional target conformations and consume substantial compute and generation time per design, limiting their throu...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [PHI-Reason: evidence-grounded species-level phage-host prediction from structured biological text profiles](https://www.biorxiv.org/content/10.64898/2026.06.10.727770v1)
  来源：bioRxiv | 日期：2026-06-12 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Phage--host interaction (PHI) prediction is a fundamental problem in microbiology with applications in microbial ecology and microbiome engineering. Existing computational approaches typically convert phage and host info...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Reproducibility of AI-Generated Antibiotic Recommendations in Standardized Clinical Scenarios: A Proof-of-Concept Experimental Study.](https://pubmed.ncbi.nlm.nih.gov/42285312/)
  来源：PubMed | 日期：2026-06-12 | 相关度：8.65 | 新颖度：0.75
  匹配主题：foundation_model_agent, application_monitoring
  中文摘要：Artificial intelligence (AI) tools are increasingly used to support antimicrobial prescribing, but most published literature focuses on accuracy rather than reproducibility across identical inputs. Reproducibility is a k...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Sentinel: Decoding Context Utilization via Attention Probing for Efficient LLM Context Compression](http://arxiv.org/abs/2505.23277v3)
  来源：arXiv | 日期：2025-05-29 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) often suffers from long and noisy retrieved contexts. Existing context compression methods typically rely on heuristic relevance estimation or supervised compression models rather tha...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DRIVE: Distributional and Retrieval-Augmented Bidding with Value Evaluation](http://arxiv.org/abs/2606.14192v1)
  来源：arXiv | 日期：2026-06-12 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Auto-bidding is a core component of real-time advertising systems, where decisions must optimize long-term performance under budget and cost constraints, while online exploration is prohibitively risky. Offline reinforce...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [DNA Compression with Genomic Language Models: Tokenization, Benchmarking, and an Information-Content Map](https://www.biorxiv.org/content/10.64898/2026.06.10.731316v1)
  来源：bioRxiv | 日期：2026-06-12 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Lossless compression and probabilistic sequence modeling are two faces of the same coin: a model that assigns high probability to a sequence can encode it in few bits via arithmetic coding. We exploit this duality to eva...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [CAREPath: Semantic Context-Aware Reasoning Paths with Mechanism-Augmented Embeddings for Drug Repurposing](https://www.biorxiv.org/content/10.64898/2026.06.09.731247v1)
  来源：bioRxiv | 日期：2026-06-12 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Biomedical knowledge graphs (BKGs) that include drugs, genes, and diseases support drug repurposing by connecting drugs to diseases through gene-mediated multi-hop paths, thereby enabling mechanism-of-action reasoning. H...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Unlocking Your Programmable and Creative RNA Sequence Designer with RDiffusion](https://www.biorxiv.org/content/10.64898/2026.06.13.732023v1)
  来源：bioRxiv | 日期：2026-06-13 | 相关度：2.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：As a cornerstone of the central dogma, RNA has both witnessed and actively shaped three billion years of evolution. Over this vast timescale, a remarkable diversity of RNA molecules has emerged, executing functions that ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ProtAff: Protein Binding Affinity Prediction via LoRA-Finetuned ESM-2](https://www.biorxiv.org/content/10.64898/2026.06.13.732058v1)
  来源：bioRxiv | 日期：2026-06-13 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Predicting the binding affinity of protein--protein interactions remains a central challenge in computational biology. Structure prediction models such as AlphaFold3 (AF3) and Boltz-2 can produce high-quality docking pos...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Doctor-RAG: A Failure-Aware Repair Framework for Agentic Retrieval-Augmented Generation](http://arxiv.org/abs/2604.00865v2)
  来源：arXiv | 日期：2026-04-01 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Agentic Retrieval-Augmented Generation interleaves retrieval and reasoning for multi-hop QA and complex knowledge tasks. As reasoning trajectories lengthen, failures become more frequent, while existing methods often eit...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Micro-Swarm Locomotion Optimization in Dynamic Flow using Multi-Objective Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2605.25025v2)
  来源：arXiv | 日期：2026-05-24 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Coordinating micro-robotic swarms in realistic, time-dependent fluid environments remains a major challenge for biomedical and environmental applications. We present a hybrid CFD-MO-MARL (Computational Fluid Dynamics-Mul...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Machine Learning for Biomedical Raman Spectroscopy: From Spectral Acquisition to Clinical Translation](http://arxiv.org/abs/2606.14169v1)
  来源：arXiv | 日期：2026-06-12 | 相关度：2.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Raman spectroscopy provides label-free, chemically specific characterization of biological systems and has become an important tool for cancer diagnosis, molecular subtyping, microbiological identification, and intraoper...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [When algorithms testify: artificial intelligence-driven DNA analysis, evidentiary standards, and criminal justice reform.](https://pubmed.ncbi.nlm.nih.gov/42286906/)
  来源：PubMed | 日期：2026-06-15 | 相关度：1.7 | 新颖度：8.15
  匹配主题：未命中具体主题
  中文摘要：Forensic DNA analysis has already influenced criminal justice, and serves as a powerful tool for both conviction and exoneration. Despite its scientific foundations and wide application, DNA evidence is vulnerable to int...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
