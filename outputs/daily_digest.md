# 每日论文监控日报 (2026-08-04)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 59 篇新论文。

## 抓取状态

- arXiv：成功，命中 39 篇
- PubMed：成功，命中 173 篇
- bioRxiv：成功，命中 12 篇
- medRxiv：成功，命中 5 篇

## 最值得看

### Foundation Model / Agent

- [GenED-SC: Generative Editing Semantic Communication with Integrated Multi-Modal LLMs](http://arxiv.org/abs/2606.04015v2)
  来源：arXiv | 日期：2026-05-31 | 相关度：7.9 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Deep learning-based joint source-channel coding has recently demonstrated strong potential for semantic communication (SemComm). However, most existing approaches focus on optimizing visual-fidelity metrics, which can le...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Structured Memory for Edge Language Models: Persistent Context and Corpus Retrieval via O(1) SSM State Injection](http://arxiv.org/abs/2608.02560v1)
  来源：arXiv | 日期：2026-08-03 | 相关度：6.55 | 新颖度：8.22
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) imposes a prefill cost proportional to retrieved context length, and -- with Transformer backbones -- a KV-cache that grows with each generated token. State-Space Models (SSMs) avoid ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 产品应用 / 监测落地

- [A Privacy-Preserving Zero-Code Conversational Statistical Analysis System for Clinical Research Using Agentic AI and Local R Execution](https://www.medrxiv.org/content/10.64898/2026.07.30.26359367v1)
  来源：medRxiv | 日期：2026-08-02 | 相关度：7.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Background Clinical data analysis typically requires statistical programming skills, whereas cloud-based artificial intelligence (AI) agents risk exposing sensitive patient records. We developed and functionally validate...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 可追踪

### Foundation Model / Agent

- [Automating clinical trial outcome identification and misreporting detection using RegCheck](https://www.medrxiv.org/content/10.64898/2026.07.30.26358885v1)
  来源：medRxiv | 日期：2026-08-02 | 相关度：7.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Objective To evaluate the accuracy and cost of RegCheck, an automated large language model (LLM)-based workflow, for identifying clinical trial outcomes and detecting outcome misreporting by comparing its outputs with ma...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LLM-Guided Retrieval for Prediction of Molecular Perturbation Responses](http://arxiv.org/abs/2608.01734v1)
  来源：arXiv | 日期：2026-08-03 | 相关度：7.15 | 新颖度：6.01
  匹配主题：foundation_model_agent
  中文摘要：Predicting transcriptomic responses to small-molecule perturbations across cell lines is central to drug discovery, but exhaustive profiling of drug-cell combinations is infeasible. We frame molecular perturbation predic...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Growth factor thermostability dataset derived from experimental and computational approaches to accelerate cultured meat development.](https://pubmed.ncbi.nlm.nih.gov/42422031/)
  来源：PubMed | 日期：2026-08-01 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：This project compiled experimentally measured and computationally predicted thermostability data for growth factors (GFs) commonly used in cultured meat and seafood (CM) production. Data were generated on recombinant GFs...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Sparse autoencoders reveal interpretable cell-type programs in single-cell foundation model representations.](https://pubmed.ncbi.nlm.nih.gov/42155660/)
  来源：PubMed | 日期：2026-08-01 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Single-cell foundation models such as scGPT learn rich representations of cellular identity, yet the biological programs encoded in their internal activations remain opaque. We investigate whether sparse autoencoders (SA...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PICopilot: An LLM-based Agentic Framework for Assisting Photonic Integrated Circuit Design via Script Generation](http://arxiv.org/abs/2608.01791v1)
  来源：arXiv | 日期：2026-08-03 | 相关度：6.55 | 新颖度：7.15
  匹配主题：foundation_model_agent
  中文摘要：The rapid development of photonic integrated circuits (PICs) is shifting the design flow from traditional graphical user interface (GUI)-based methods to script-based methods for higher flexibility, portability, and main...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PrefixPlace: Provable Prefix Key-Value Placement for Large Language Model Serving under Heterogeneous Compute and Transfer Costs](http://arxiv.org/abs/2608.01655v1)
  来源：arXiv | 日期：2026-08-03 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Prefix Key-Value (KV) reuse avoids repeated prefill in Large Language Model (LLM) inference, but local misses require recomputation or replica fetches. Their relative cost varies with hardware, prefix depth, KV goodput, ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EMMPREDMLsub: multi-label prediction of mRNA subcellular localization based on the ESM2 large language model and MMDO-MDPU resampling strategy.](https://pubmed.ncbi.nlm.nih.gov/41493162/)
  来源：PubMed | 日期：2026-08-01 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Subcellular localization of mRNA plays a crucial regulatory role in eukaryotic cells, directly affecting protein synthesis, functional localization and cellular activities. Its abnormal regulation is closely associated w...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PG-LLM: Benchmarking General-Purpose Language Models for Protein Variant Ranking](https://www.biorxiv.org/content/10.64898/2026.07.27.741045v2)
  来源：bioRxiv | 日期：2026-08-03 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：eneral-purpose language models are being increasingly utilized in protein-design workflows, yet their ability to evaluate variant effects remains unclear. To answer this question, we introduce PG-LLM, a benchmark built o...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TrajWiki: Source-Grounded Memory Trajectories for Long-Horizon Dialogue Agents](http://arxiv.org/abs/2608.00967v1)
  来源：arXiv | 日期：2026-08-02 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language model agents have shown strong capabilities in generating coherent and contextually appropriate responses, yet robust long-horizon dialogue remains limited by the lack of external memory that is traceable,...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RH-RAG: Trustworthy Long-Form Generation for Privacy-Constrained Settings](http://arxiv.org/abs/2608.01311v1)
  来源：arXiv | 日期：2026-08-02 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Generating long-form content from extensive internal reports remains challenging for organizations operating under strict privacy and security constraints, where proprietary cloud-based LLM APIs are often not viable. Whi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Mitigating Visual Hallucinations in Multimodal Systems through Retrieval-Augmented Reliability-Aware Inference](http://arxiv.org/abs/2606.15782v2)
  来源：arXiv | 日期：2026-06-14 | 相关度：6.1 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Multimodal large language models (MLLMs) have demonstrated strong capabilities in vision-language understanding and natural-language response generation. However, these systems can still produce overconfident predictions...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [X-KGRank: A Knowledge Graph RAG Framework for Explainable Recommendations via Pattern Mining and LLM Re-Ranking](http://arxiv.org/abs/2608.01732v1)
  来源：arXiv | 日期：2026-08-03 | 相关度：5.45 | 新颖度：6.26
  匹配主题：foundation_model_agent
  中文摘要：Modern recommender systems produce predictions that users cannot interrogate. The two dominant improvements, collaborative filtering and LLM-based reasoning, each fall short: collaborative filtering captures behavioural ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [On the Wings of Imagination: Conflicting Script-based Multi-role Framework for Humor Caption Generation](http://arxiv.org/abs/2602.06423v2)
  来源：arXiv | 日期：2026-02-06 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Humor is a commonly used and intricate human language in daily life. Humor generation, especially in multi-modal scenarios, is a challenging task for large language models (LLMs), which is typically as funny caption gene...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Operationalising LLM-assisted screening of literature to support systematic reviews](https://www.biorxiv.org/content/10.64898/2026.07.29.741127v1)
  来源：bioRxiv | 日期：2026-08-03 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) can ease the work of screening titles and abstracts for systematic reviews, but obtaining reliable results requires researchers to make practical choices about which LLMs to use, how to combi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [TM-Vec 2s: Accelerated Protein Remote Homology Detection](https://www.biorxiv.org/content/10.64898/2026.02.05.704073v2)
  来源：bioRxiv | 日期：2026-08-03 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Understanding protein function is an essential aspect of many biological applications. The exponential growth of protein sequence data has created a critical throughput bottleneck for structural homology detection: While...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Real-Time Hybrid Retrieval in Hyperbolic Space for Retrieval-Augmented Generation on Edge Devices](http://arxiv.org/abs/2608.01450v1)
  来源：arXiv | 日期：2026-08-02 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：This paper presents a hybrid document retrieval system designed for retrieval-augmented generation (RAG) that operates entirely within the Lorentz model of hyperbolic geometry. Unlike conventional dense retrievers confin...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Variantscape: Large Language Model-Driven Mining of Biomedical Literature for Clinical Interpretation of Cancer Variants](https://www.medrxiv.org/content/10.64898/2026.08.02.26359492v1)
  来源：medRxiv | 日期：2026-08-03 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Background: Precision oncology relies on accurate interpretation of tumour-detected gene variants, to guide personalized treatment decisions. However, accurate interpretation of variants in context requires extensive inf...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Zero-shot document-level biomedical relation extraction via scenario-based prompt design in two-stage with LLM.](https://pubmed.ncbi.nlm.nih.gov/41762612/)
  来源：PubMed | 日期：2026-08-01 | 相关度：6.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Document-level biomedical relation extraction is a crucial task due to the complex interactions among multiple entities distributed across lengthy scientific texts. Traditional supervised methods are constrained by their...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Detailed curation of biological samples and experimental designs for genomics using LLM-supported agentic workflows](https://www.biorxiv.org/content/10.64898/2026.07.30.741874v1)
  来源：bioRxiv | 日期：2026-08-02 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：We describe an automated software tool to accomplish data curation tasks previously performed by humans for the Gemma genomics data re-analysis resource. Gemma is a hand-curated database of reprocessed transcriptomic stu...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ECLAIR: A Causally-Grounded AI Framework for Scientific Discovery in Empirical Software Engineering](http://arxiv.org/abs/2608.02323v1)
  来源：arXiv | 日期：2026-08-03 | 相关度：4.75 | 新颖度：6.98
  匹配主题：foundation_model_agent
  中文摘要：The scientific method has long guided empirical research in Software Engineering (SE), but the complexity of modern software systems often hinders its systematic application. This paper introduces _ECLAIR_, a causally gr...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ARGen: Affect-Reinforced Generative Augmentation towards Vision-based Dynamic Emotion Perception](http://arxiv.org/abs/2604.12255v2)
  来源：arXiv | 日期：2026-04-14 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Dynamic facial expression recognition in the wild remains challenging due to data scarcity and long-tail distributions, which hinder models from effectively learning the temporal dynamics of scarce emotions. To address t...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Artificial intelligence in clinical metagenomic pathogen detection: A critical review of pipeline integrations, challenges, and future directions.](https://pubmed.ncbi.nlm.nih.gov/42289215/)
  来源：PubMed | 日期：2026-08-01 | 相关度：8.25 | 新颖度：1.75
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：Metagenomic next-generation sequencing (mNGS) has expanded the scope of clinical diagnostics by enabling culture-independent detection of microorganisms in patient samples. However, mNGS clinical utility remains constrai...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Applications of Machine Learning, Natural Language Processing, and Generative Artificial Intelligence in Dermatology Education and Research: A Scoping Review.](https://pubmed.ncbi.nlm.nih.gov/41981908/)
  来源：PubMed | 日期：2026-08-01 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence (AI) is being increasingly used in dermatology education and research as digital health data expands and large language models (LLMs) advance. This scoping review synthesized current applications,...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [C-MIG: Multi-view Information Gain-based Retrieval-Augmented Generation for Clinical Diagnosis Reasoning](http://arxiv.org/abs/2605.27860v2)
  来源：arXiv | 日期：2026-05-27 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation combined with reinforcement learning has shown promise for grounding large language models in trustworthy medical evidence. However, existing methods rely on exact-match binary rewards, whi...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Precision Endodontics-Advancing Towards Omics-Guided Personalisation: A Narrative Review.](https://pubmed.ncbi.nlm.nih.gov/42543866/)
  来源：PubMed | 日期：2026-08-02 | 相关度：5.45 | 新颖度：5.25
  匹配主题：pathogenomics, application_monitoring
  中文摘要：To critically evaluate the emerging contribution of genomics, transcriptomics, proteomics, metabolomics and microbiomics to the development of precision endodontics, and to examine the opportunities and translational cha...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Interpretable deep learning model of circulating genomics for quantitative survival prediction in advanced non-small cell lung cancer.](https://pubmed.ncbi.nlm.nih.gov/41649698/)
  来源：PubMed | 日期：2026-08-01 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Accurate quantitative survival prediction in advanced non-small cell lung cancer (NSCLC) remains an unmet clinical need. While liquid biopsy is widely used, single circulating tumor DNA (ctDNA) shows limited predictive p...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RING: Retrieval-Internalized Generation for Continual Large-Scale Knowledge Injection](http://arxiv.org/abs/2608.01630v1)
  来源：arXiv | 日期：2026-08-03 | 相关度：2.1 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) improves factuality but adds latency and engineering overhead at serving time. We propose RING (Retrieval-Internalized Generation), a holistic paradigm spanning both architecture and ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [UEmbed: Unified Sparse and Dense Multimodal Embeddings](http://arxiv.org/abs/2608.02583v1)
  来源：arXiv | 日期：2026-08-03 | 相关度：2.05 | 新颖度：7.5
  匹配主题：foundation_model_agent
  中文摘要：Sparse retrieval underpins modern search systems, from web search to retrieval-augmented generation. Existing work has introduced Learned Sparse Retrieval (LSR) to push beyond exact lexical matching toward richer semanti...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Before Reasoning Fails: Pre-Evidence Procedural Failures in Agentic RAG](http://arxiv.org/abs/2608.02011v1)
  来源：arXiv | 日期：2026-08-03 | 相关度：1.4 | 新颖度：6.46
  匹配主题：未命中具体主题
  中文摘要：Agentic RAG（检索增强生成）系统在测试证据推理能力之前，往往会先出现程序性失效：Agent可能检索到了候选片段，但在未对其进行检查的情况下就直接给出最终答案。本研究将此类失效视为Agent执行轨迹的程序属性，通过分析工具调用轨迹、检索证据、阅读段落和最终答案，将错误归因为“证据前规约失效”和“金标准阅读后失效”。在HotpotQA、2WikiMultiHopQA和MuSiQue数据集的12,000条配对轨迹分析中，发现这两类失...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Effective and Efficient Context Retrieval via Partial Dependency Graph for Repository-Level Code Generation](http://arxiv.org/abs/2608.01927v1)
  来源：arXiv | 日期：2026-08-03 | 相关度：1.4 | 新颖度：6.27
  匹配主题：未命中具体主题
  中文摘要：基于大语言模型（LLM）的仓库级代码生成旨在利用软件仓库中的上下文生成代码，这要求模型具备处理复杂代码依赖的能力。由于上下文窗口限制和对特定仓库理解不足，LLM 通常依赖检索增强生成（RAG）来引入相关代码。早期 RAG 方法主要采用基于相似性的检索，往往无法获取目标函数所依赖的关键代码片段。近期研究虽引入图检索来建模依赖关系，但通常依赖人工规则和静态全局图，导致灵活性受限且维护成本高。受人类开发者隐式构建局部依赖图并迭代检查行为的启发...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Comparative Validation of GPT-4o-mini and Teacher Mean Scores for Automated Scoring of Music Analysis Responses: Single-Pass Deployment, Repeatability, and Strategy-Specific Bias](http://arxiv.org/abs/2608.01783v1)
  来源：arXiv | 日期：2026-08-03 | 相关度：0.7 | 新颖度：6.68
  匹配主题：未命中具体主题
  中文摘要：本研究评估了 GPT-4o-mini 在基于量表的音乐分析论文自动评分中的有效性与重复性。研究以教师平均分为基准，利用包含 300 份大学水平学生回答的数据集，从和声、形式、推理和术语四个维度进行评分。实验对比了三种提示策略：少样本链式思考（Fs+CoT）、检索增强生成（RAG）以及基于五次内部生成的自我一致性（SC）。每种策略重复运行三次以测试稳健性，通过相关系数、组内相关系数（ICC）、Krippendorff's alpha 和二...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [A Unified Benchmark for Privacy-preserving Vector Search](http://arxiv.org/abs/2608.01192v1)
  来源：arXiv | 日期：2026-08-02 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：向量搜索是语义搜索、推荐系统和检索增强生成（RAG）的核心。然而，查询服务通常能直接访问查询嵌入和匹配语料库，这构成了用户和数据所有者的隐私泄露风险。虽然 SAP、EMVP、BNTM 和 Tip-toe 等加密方案试图解决此问题，但由于评估环境（语料库、威胁模型、硬件等）不统一，导致性能无法直接比较。本研究通过建立统一的实验基准填补了这一空白，在相同的工作负载、硬件和指标定义下，对比了明文基准与四种加密后端。实验发现，这些方案在隐私、性...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [ACE-GraphRAG: Agentic Context Engineering for Hierarchical GraphRAG](http://arxiv.org/abs/2608.01269v1)
  来源：arXiv | 日期：2026-08-02 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：层次化图检索增强生成（GraphRAG）虽然能多粒度组织知识，但固定的上下文构建方式往往难以将多分辨率表示转化为适配特定查询的内容，存在“表示-推理差距”。本文提出 ACE-GraphRAG，一种推理阶段的上下文策略层，旨在补充并调整初始生成上下文。该方法将上下文构建建模为涵盖差距感知优化、检索分支及任务条件适配的策略。其核心“并行差分检索”通过深度导向的事实分支和广度导向的语义分支获取补充证据，并在保留出处和抽象级别的基础上与初始上下...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [BioGraphX-RNA: A Universal Physicochemical Graph Encoding for Interpretable RNA Subcellular Localization Prediction](https://www.biorxiv.org/content/10.64898/2026.02.23.707573v3)
  来源：bioRxiv | 日期：2026-08-03 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：RNA subcellular localization is a critical determinant of cellular function. However, current computational approaches often operate as ""black boxes", overlooking the complex interplay among sequence, structure, and phy...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Artificial Intelligence in Food-Nutrition-Health Research: From Multimodal Data Integration to Precision Intervention.](https://pubmed.ncbi.nlm.nih.gov/42535509/)
  来源：PubMed | 日期：2026-08-01 | 相关度：4.5 | 新颖度：1.0
  匹配主题：foundation_model_agent, application_monitoring
  中文摘要：Artificial intelligence (AI) is transforming food-nutrition-health research by enabling pattern recognition in complex, high-dimensional datasets that traditional hypothesis-driven approaches cannot address. This review ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Deep learning-enabled ratiometric signal transduction for portable and intelligent colorimetric LAMP biosensing of Vibrio vulnificus.](https://pubmed.ncbi.nlm.nih.gov/42031193/)
  来源：PubMed | 日期：2026-08-01 | 相关度：2.65 | 新颖度：0.25
  匹配主题：sequencing_bioinformatics
  中文摘要：Vibrio vulnificus is a highly lethal zoonotic pathogen associated with seafood consumption and aquaculture environments, demanding rapid and reliable on-site molecular diagnostics. Here, we report an intelligent biosensi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [BioInsight: Multi-Agent Orchestration for Interactive Biomedical Knowledge Discovery](http://arxiv.org/abs/2606.20997v2)
  来源：arXiv | 日期：2026-06-19 | 相关度：2.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Biomedical deep-research systems increasingly retrieve and synthesize scientific evidence, but their outputs typically collapse heterogeneous evidence into static text, making provenance difficult to inspect and reuse. W...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [An Evidence-Grounded Retrieval-Augmented Transformer Framework for Health Misinformation Verification](http://arxiv.org/abs/2608.02310v1)
  来源：arXiv | 日期：2026-08-03 | 相关度：1.7 | 新颖度：7.45
  匹配主题：未命中具体主题
  中文摘要：The rapid spread of false and misleading health information through digital platforms has become a major public health challenge, particularly during infectious disease outbreaks where delayed verification can influence ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CREB gene regulation as a blood biomarker of neural sensitivity to social threat.](https://pubmed.ncbi.nlm.nih.gov/41905489/)
  来源：PubMed | 日期：2026-08-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：社会威胁会增强炎症反应并增加相关疾病风险，识别对社会威胁具有高度神经敏感性的个体对制定预防协议至关重要。本研究探讨了外周血中cAMP反应元件结合蛋白（CREB）转录因子活性是否可作为中枢神经系统（CNS）对社会威胁敏感性的生物标志物。研究利用一项随机对照试验的基线数据（n=44，平均年龄19.4岁），结合功能磁共振成像（fMRI）与外周血采样。通过基于TELiS启动子的生物信息学方法评估CREB基因调节活性，并利用改良蒙特利尔成像压力测...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CTRAG: An In-Context Retrieval-based Framework for Automated Compliance Checking using LLMs](http://arxiv.org/abs/2608.02472v1)
  来源：arXiv | 日期：2026-08-03 | 相关度：0.7 | 新颖度：7.3
  匹配主题：未命中具体主题
  中文摘要：在受控行业中，合规性检查是确保企业符合财务报告、数据隐私和网络安全准则的关键，但手动测试耗时且易出错，尤其是在涉及第三方云服务的间接合规场景下。本文提出了 CTRAG，一种用于自动合规性检查的新型检索增强生成（RAG）流水线。该框架集成了自适应分块、动态检索配置和上下文学习（In-context learning）等先进策略，旨在提高评估的精确度。CTRAG 通过从监管文本中提取控制问题，并将其与非结构化的公司文档进行交叉引用，实现文档...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MEGRAG: Multi-Granular Evidence Graphs for Answer-Aware Multi-Hop RAG](http://arxiv.org/abs/2608.02195v1)
  来源：arXiv | 日期：2026-08-03 | 相关度：0.7 | 新颖度：6.74
  匹配主题：未命中具体主题
  中文摘要：多跳问答是检索增强生成（RAG）中的核心挑战，因为生成答案需要整合分散的证据。现有的迭代RAG（iRAG）方法存在两个局限：一是多数方法仍采用单一粒度的证据支持推理步骤，难以平衡信息密度与上下文噪声；二是通常在完成所有中间检索后才回答原始问题，导致冗余证据和检索错误累积。为此，我们提出了MEGRAG，这是一个答案感知的框架，将多跳推理表示为路径结构的多粒度证据图。在离线阶段，MEGRAG通过跨粒度索引将段落与其句子及提取的三元组关联。在...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GraphER: An Efficient Graph-Based Enrichment and Reranking Method for Retrieval-Augmented Generation](http://arxiv.org/abs/2603.24925v3)
  来源：arXiv | 日期：2026-03-26 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）系统中的语义搜索在处理复杂信息需求时往往表现不足，特别是当相关证据分散在多个来源时，难以检索到完整的证据集。现有方法要么依赖迭代式代理检索（计算效率低），要么维护知识图谱等额外结构（存储和维护开销大）。本文提出 GraphER，一种基于图的增强和重排序框架。该框架：（1）利用数据的组织结构捕捉语义相似性之外的邻近关系；（2）在查询时基于这些邻近关系动态构建图；（3）应用基于图的排序算法筛选顶层候选文档。在表格检索、...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MERIT: Efficient In-Place Deletion for Dynamic Graph-Based Approximate Nearest Neighbor Indexes](http://arxiv.org/abs/2607.29173v2)
  来源：arXiv | 日期：2026-07-31 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：基于图的索引已成为高维数据近似最近邻搜索（ANNS）的主流方法，在检索增强生成（RAG）和向量数据库中起着关键作用。然而，如何在不中断在线服务且不产生高昂维护成本的前提下实现高效的原位删除仍具挑战。为此，本文提出 MERIT（基于 MST 的高效原位更新修复框架）。该框架包含三大核心技术：一是结合被删除顶点出邻居与可搜索入邻居的有界搜索恢复；二是利用 $k_r$-最小生成树（MST）进行局部修复，在增强局部连通性的同时保留多条路由选择；...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Collaborative Memory Augmentation for Generative Recommendation](http://arxiv.org/abs/2608.01315v1)
  来源：arXiv | 日期：2026-08-02 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：生成式推荐（GR）通过将项目转换建模为序列到序列任务展现出巨大潜力。然而，现有框架主要侧重于在受限的内部参数空间内建模个体用户序列，未能显式利用跨用户的协作信号。为此，我们提出了OMEGA，一种用于生成式推荐的协作记忆增强框架，旨在弥合隐式参数知识与显式协作信号之间的差距。首先，该框架引入潜在上下文压缩方法，利用可学习的查询令牌将序列化用户行为蒸馏为紧凑表示，显著降低存储开销。这些压缩表示被聚合到协作记忆库中，作为全局行为模式的显式存储...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MUSS: Multilevel Subset Selection for Relevance and Diversity](http://arxiv.org/abs/2503.11126v4)
  来源：arXiv | 日期：2025-03-14 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：针对推荐系统和检索增强生成（RAG）中相关且多样化子集选择的 NP 难问题，本文提出了 MUSS（多级子集选择）方法。传统方法如最大边际相关性（MMR）依赖贪婪选择且缺乏分布式支持，而后续的 DGDS 方法虽支持分布式随机分区，但未充分利用数据结构。MUSS 通过多级架构优化了在大规模数据集上的可扩展性与性能。实验结果显示，在推荐系统应用中，MUSS 不仅将准确率提升了 4 个百分点，运行速度还提高了 20 至 80 倍；在基于 RAG...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [From Explanation to Diagnosis: Next Generation Interactive Video Coach with Misstep Awareness](http://arxiv.org/abs/2606.02970v2)
  来源：arXiv | 日期：2026-06-02 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：智能教学系统虽擅长生成解释，但往往缺乏对学习者错误原因的系统性诊断。本研究为神经符号AI教练Ivy引入了“误区感知”（misstep-aware）辅导功能。该系统采用双模型架构，在佐治亚理工学院在线研究生AI课程背景下，将原有的任务-方法-知识（TMK）模型与新型教学模型（PM）相结合。PM通过编码学习者的潜在信念（错误观点或知识缺失）、TMK轨迹（误解来源）、误解类型以及源自教师问答库的针对性支架，使教师的诊断知识变得显性且机器可读。...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Toward Bridging the Gap from Artificial Intelligence in Clinical Research to Clinical Practice in Rheumatology: The Mayo Experience.](https://pubmed.ncbi.nlm.nih.gov/42409435/)
  来源：PubMed | 日期：2026-08-01 | 相关度：4.85 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：This article highlights Mayo Clinic's pioneering efforts to integrate artificial intelligence (AI) and machine learning into rheumatology, focusing on genomics, imaging, pathology, and clinical data science to improve di...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial intelligence in molecular diagnostics for pandemic preparedness.](https://pubmed.ncbi.nlm.nih.gov/42396845/)
  来源：PubMed | 日期：2026-08-01 | 相关度：3.65 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Molecular diagnostics focusing on the detection and analysis of nucleic acids are indispensable tools for early pathogen identification, transmission monitoring, and genomic surveillance during pandemics. Recent technolo...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Necrotizing pneumonia in children: a comprehensive narrative review of current challenges and future perspectives.](https://pubmed.ncbi.nlm.nih.gov/42545025/)
  来源：PubMed | 日期：2026-08-03 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Necrotizing pneumonia (NP) represents an uncommon but severe complication of community-acquired pneumonia (CAP) in children, characterized by the destruction of lung parenchyma and formation of multiple thin-walled cavit...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial Intelligence in Clinical Genetics: Current Applications and Challenges.](https://pubmed.ncbi.nlm.nih.gov/42443618/)
  来源：PubMed | 日期：2026-08-01 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：多组学、二代测序（NGS）和长读长测序技术已深刻改变医学遗传学实践。由于每位患者涉及数万至数百万个变异及复杂的生化模式，复杂病例的解读往往需要耗费大量人力。海量数据集的出现使传统分析方法难以为继。人工智能（AI）为处理临床遗传学中日益增长的基因组与表型数据提供了高效手段，目前已应用于变异优先排序与解读、罕见病筛查及精准医学等领域。然而，受限于特定人群代表性不足、伦理争议及数据治理等问题，这些技术向常规临床转化的过程依然困难。目前大多数 ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Bridging Trials and Real Life in Fixed-Duration BTKi-Venetoclax for CLL: A Delphi-Enhanced Synthesis Incorporating Artificial Intelligence (AI) Benchmarks.](https://pubmed.ncbi.nlm.nih.gov/41974594/)
  来源：PubMed | 日期：2026-08-01 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：针对慢性淋巴细胞白血病（CLL）中固定疗程（FD）BTK抑制剂（BTKi）联合维奈克拉方案的患者选择，本研究旨在弥合临床试验与真实世界实践的差距。研究采用改进的德尔菲法，由意大利坎帕尼亚地区的9名血液学家参与，重点评估了合并症、基因组学（TP53/del(17p)、IGHV状态、复杂核型）及物流因素（照护支持、就医距离、给药能力）对一线治疗决策的影响。基于2014-2025年的系统综述制定了12项陈述，共识标准设定为≥75%一致性。结果...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Nursing roles, competencies, and education in precision oncology: a scoping review.](https://pubmed.ncbi.nlm.nih.gov/42500353/)
  来源：PubMed | 日期：2026-08-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：护士在精准癌症护理路径中发挥着关键作用，支持基因组检测的整合并提供以患者为中心的持续护理。本范围综述旨在梳理护士在精准癌症护理中的角色、能力要求及相关教育现状。研究遵循JBI方法，系统检索了MEDLINE、Embase等数据库，并利用生成式人工智能（GenAI）对灰色文献中的国际研究生及继续教育项目进行了检索。研究共纳入52篇文献（44篇涉及角色/能力，23篇涉及教育干预）和65个教育项目。结果识别出五大护理角色主题：基因组风险评估与分...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Multi-omic biomarkers of neoadjuvant treatment response in rectal cancer: A narrative review.](https://pubmed.ncbi.nlm.nih.gov/42250371/)
  来源：PubMed | 日期：2026-08-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：直肠癌对新辅助治疗的反应具有高度异质性，这增加了器官保留策略中患者筛选的复杂性。本综述回顾了2015年以来关于直肠癌新辅助治疗反应预测因子的研究，涵盖六大领域：基因组与分子生物标志物、影像学标志物、组织病理学与数字病理标志物、液体活检（cfDNA/ctDNA）、患者来源的肿瘤模型以及微生物组相关标志物。研究表明，治疗反应受肿瘤内在特征、免疫微环境和间质特征的共同影响。免疫富集型肿瘤（如高CD8+ T细胞浸润、CMS1/iCMS3亚型、高...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [ASO Special Article: Proceedings of the Inaugural Joint US-India Cancer Dialogue: Accelerating Collaboration to Advance Cancer Prevention, Early Detection, Treatment, and Care.](https://pubmed.ncbi.nlm.nih.gov/42166060/)
  来源：PubMed | 日期：2026-08-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：癌症是美印两国的主要死因。2023年6月印度总理访美期间，两国承诺建立美印癌症对话机制，旨在通过结构化双边努力应对共同的癌症挑战。本文概述了2024年8月在新德里举行的首届美印癌症对话联合会议的筹备步骤与议程。通过由政府、科学和临床领导者参与的结构化共识制定流程，确定了双边合作的优先领域。筹备工作包括由美国临床肿瘤学会（ASCO）主办的技术工作组会议，涵盖预防、早期检测、治疗、临床试验和实施科学。会议最终确定了多项核心合作方向：扩大HP...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial intelligence, omics, and biomarkers: Redefining lung cancer early detection.](https://pubmed.ncbi.nlm.nih.gov/42105533/)
  来源：PubMed | 日期：2026-08-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：肺癌是全球死亡率最高的癌症，主要归因于早期干预手段有限。目前的筛查方法受限于侵入性、辐射暴露及早期灵敏度低等问题，亟需创新技术。本综述探讨了结合生物标志物、组学技术与人工智能（AI）的早期检测新兴工具。肿瘤细胞释放的特定生物标志物（如细胞成分、核酸片段、蛋白质片段或代谢物）可通过非侵入性体液检测获取。将生物标志物与蛋白质组学、基因组学或多组学结合，可提供不同癌症亚型和阶段分子特征的全面见解。机器学习和深度学习等AI工具进一步提升了这些技...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [RGTFormer: Predicting mutation-associated multi-drug resistance in Mycobacterium tuberculosis using a categorical gated transformer and relational graph convolutional network.](https://pubmed.ncbi.nlm.nih.gov/41722285/)
  来源：PubMed | 日期：2026-08-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：结核分枝杆菌引起的多重耐药结核病是全球公共卫生面临的重大挑战。耐药性通常由药物靶基因的单核苷酸突变引起，因此早期预测对于有效治疗至关重要。本研究提出了一种名为 RGTFormer 的新型深度学习模型，该模型结合了分类门控 Transformer 和关系图卷积网络（RGCN），用于预测 6 个关键耐药基因的突变是否会导致对一线抗结核药物的耐药性。RGTFormer 整合了突变的序列特征和结构特征，利用 RGCN 捕捉突变之间的依赖关系，并...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
