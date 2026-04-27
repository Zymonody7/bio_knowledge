# 每日论文监控日报 (2026-04-27)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 31 篇新论文。

## 抓取状态

- arXiv：成功，命中 18 篇
- PubMed：成功，命中 16 篇
- bioRxiv：成功，命中 20 篇
- medRxiv：成功，命中 7 篇

## 最值得看

### Foundation Model / Agent

- [GenNA: Conditional generation of nucleotide sequences guided by natural-language annotations](https://www.biorxiv.org/content/10.64898/2026.04.22.720063v1)
  来源：bioRxiv | 日期：2026-04-24 | 相关度：8.5 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Deciphering the mapping between linear biomolecular sequences and complex biological functions remains a central challenge in genomics. Although existing generative nucleotide language models have made substantial progre...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [BERAG: Bayesian Ensemble Retrieval-Augmented Generation for Knowledge-based Visual Question Answering](http://arxiv.org/abs/2604.22678v1)
  来源：arXiv | 日期：2026-04-24 | 相关度：7.9 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：A common approach to question answering with retrieval-augmented generation (RAG) is to concatenate documents into a single context and pass it to a language model to generate an answer. While simple, this strategy can o...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [H2O: A Foundation Model Bridging Histopathology to Spatial Multi-Omics Profiling](https://www.biorxiv.org/content/10.64898/2026.04.21.717342v1)
  来源：bioRxiv | 日期：2026-04-24 | 相关度：7.15 | 新颖度：7.25
  匹配主题：foundation_model_agent
  中文摘要：Spatial omics technologies have revolutionized the molecular profiling of tissues but remain constrained by high costs and limited scalability. While hematoxylin and eosin (H&E) staining is ubiquitous, it lacks molecular...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [Dr.Sai: An agentic AI for real-world physics analysis at BESIII](http://arxiv.org/abs/2604.22541v1)
  来源：arXiv | 日期：2026-04-24 | 相关度：7.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：High Energy Physics (HEP) experiments like BESIII produce petabyte-scale data. Extracting physics results requires complex workflows (simulation, reconstruction, statistical analysis, etc.) that traditionally take expert...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Large language models and retrieval augmented generation for complex clinical codelists: evaluating performance and assessing failure modes](https://www.medrxiv.org/content/10.64898/2026.04.23.26351098v1)
  来源：medRxiv | 日期：2026-04-24 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Objectives: Large language models (LLMs) have shown promise in creating clinical codelists for research purposes, a time-consuming task requiring expert domain knowledge. Here, we evaluate the performance and assess fail...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Words to Amino Acids: Does the Curse of Depth Persist?](http://arxiv.org/abs/2602.21750v2)
  来源：arXiv | 日期：2026-02-25 | 相关度：7.1 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Protein language models (PLMs) have become widely adopted as general-purpose models, demonstrating strong performance in protein engineering and de novo design. Like large language models (LLMs), they are typically train...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SAGE: Selective Attention-Guided Extraction for Token-Efficient Document Indexing](http://arxiv.org/abs/2604.15583v2)
  来源：arXiv | 日期：2026-04-16 | 相关度：6.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Large language models with long context windows can answer complex questions directly from full-length academic, technical, and policy documents, but passing entire documents is often costly, slow, and can degrade answer...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Comparing prognostic performance and reasoning between large language models and physicians](https://www.medrxiv.org/content/10.64898/2026.04.17.26350898v1)
  来源：medRxiv | 日期：2026-04-25 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Importance: Physicians routinely prognosticate to guide care delivery and shared decision making, particularly when caring for patients with critical illnesses. Yet, these physician estimates are prone to inaccuracy and ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Chain-of-Memory: Lightweight Memory Construction with Dynamic Evolution for LLM Agents](http://arxiv.org/abs/2601.14287v2)
  来源：arXiv | 日期：2026-01-14 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：External memory systems are pivotal for enabling Large Language Model (LLM) agents to maintain persistent knowledge and perform long-horizon decision-making. Existing paradigms typically follow a two-stage process: compu...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [UR$^2$: Unify RAG and Reasoning through Reinforcement Learning](http://arxiv.org/abs/2508.06165v4)
  来源：arXiv | 日期：2025-08-08 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have shown strong capabilities through two complementary paradigms: Retrieval-Augmented Generation (RAG) for knowledge grounding and Reinforcement Learning from Verifiable Rewards (RLVR) for ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Decoding the phenomenology of spontaneous thought using large language-model ratings on verbal retrospective free reports](https://www.biorxiv.org/content/10.64898/2026.04.22.720079v1)
  来源：bioRxiv | 日期：2026-04-26 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：自发性思维构成了日常内在体验的主要部分，但其内容与神经生理基础的探索受限于方法学挑战。传统思维探测法限制了现象学报告的深度，而实时口头报告则会干扰自然思维流并产生运动伪迹。本研究提出并测试了一种新方法，将延迟口头回顾性自由报告（RFR）与大语言模型（LLM）生成的自动现象学评分相结合。22名参与者完成了闭眼自由思考任务，其报告由4个先进LLM和一组人类评分者在10个现象学维度上进行评估。随后，研究利用机器学习（ML）模型从EEG频谱、复...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [MIMIC-IV-Phenotype-Atlas (MIPA) : A Publicly Available Dataset for EHR Phenotyping](https://www.medrxiv.org/content/10.64898/2026.04.16.26350888v1)
  来源：medRxiv | 日期：2026-04-24 | 相关度：7.1 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Introduction Secondary use of electronic health records (EHRs) often requires transforming raw clinical information into research-grade data. A central step in this process is EHR phenotyping - the identification of pati...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Graph Neural Networks (GNNs) for Protein-Ligand Interaction Prediction](https://www.biorxiv.org/content/10.64898/2026.04.23.720519v1)
  来源：bioRxiv | 日期：2026-04-24 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Predicting protein-ligand interactions in the modern drug discovery has revolved from the involvement of artificial intelligence and structural bioinformatics using Graph Neural Networks (GNNs). The limited explainabilit...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Learning from Natural Language Feedback for Personalized Question Answering](http://arxiv.org/abs/2508.10695v2)
  来源：arXiv | 日期：2025-08-14 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Personalization is crucial for enhancing both the effectiveness and user satisfaction of language technologies, particularly in information-seeking tasks like question answering. Current approaches for personalizing larg...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [RAG-Reflect: Agentic Retrieval-Augmented Generation with Reflections for Comment-Driven Code Maintenance on Stack Overflow](http://arxiv.org/abs/2604.22217v1)
  来源：arXiv | 日期：2026-04-24 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：User comments on online programming platforms such as Stack Overflow play a vital role in maintaining the correctness and relevance of shared code examples. However, the majority of comments express gratitude or clarific...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Bridging the Long-Tail Gap: Robust Retrieval-Augmented Relation Completion via Multi-Stage Paraphrase Infusion](http://arxiv.org/abs/2604.22261v1)
  来源：arXiv | 日期：2026-04-24 | 相关度：6.15 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) struggle with relation completion (RC), both with and without retrieval-augmented generation (RAG), particularly when the required information is rare or sparsely represented. To address this...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SNPic: SNP Topic Modeling for Interpretable Clustering of Complex phenotypes](https://www.biorxiv.org/content/10.64898/2026.04.22.720106v1)
  来源：bioRxiv | 日期：2026-04-24 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Genome-wide association studies (GWAS) have cataloged thousands of disease-associated variants, yet a central challenge remains: decoding the shared, pleiotropic architecture that links complex phenotypes. Existing appro...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Mechanistic Interpretability of Antibody Language Models Using SAEs](http://arxiv.org/abs/2512.05794v2)
  来源：arXiv | 日期：2025-12-05 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Sparse autoencoders (SAEs) are a mechanistic interpretability technique that have been used to provide insight into learned concepts within large protein language models. Here, we employ TopK and Ordered SAEs to investig...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Decoding Smell from Receptor Structure](https://www.biorxiv.org/content/10.64898/2026.04.22.720159v1)
  来源：bioRxiv | 日期：2026-04-24 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Olfaction enables animals to detect and discriminate a vast array of chemicals, yet how odorant receptors (ORs) encode ligand selectivity remains unclear. Although recent advances in protein structure prediction have exp...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Rethinking Retrieval-Augmented Generation as a Cooperative Decision-Making Problem](http://arxiv.org/abs/2602.18734v2)
  来源：arXiv | 日期：2026-02-21 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：检索增强生成（RAG）通过将语言生成锚定在外部证据上，在知识密集型任务中表现出强大效能。然而，现有RAG系统多基于以排序为中心的不对称依赖范式，即生成器的质量高度依赖于重排序器（reranker）的输出结果。为克服这一局限性，本文提出了协作式检索增强生成（CoRAG）框架。该框架将重排序器和生成器视为对等的决策者，而非简单的线性流水线关系。通过针对共同的任务目标联合优化两者的行为，CoRAG促使重排序器与生成器进行协作，确保文档重排序与...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [LARA: Validation-Driven Agentic Supercomputer Workflows for Atomistic Modeling](http://arxiv.org/abs/2604.22571v1)
  来源：arXiv | 日期：2026-04-24 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：大语言模型（LLM）和智能体系统在自动化科学工作流（如原子模拟）中展现出潜力，但在高性能计算（HPC）环境中的应用受限于正确性、可重复性及资源交互安全性。生成的流程常因API误用或物理配置无效导致模拟失败。本文提出 LARA-HPC，一个验证驱动的智能体框架，旨在实现可靠的原子建模工作流生成。该框架包含三个核心组件：中介HPC交互的受控执行层；支持无成本验证的模拟原生“干跑”（dry-run）功能；以及结合检索增强生成（RAG）与迭代优...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Can QPP Choose the Right Query Variant? Evaluating Query Variant Selection for RAG Pipelines](http://arxiv.org/abs/2604.22661v1)
  来源：arXiv | 日期：2026-04-24 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：随着大语言模型（LLM）的普及，查询重构在检索增强生成（RAG）流程中变得无处不在，能够生成多个语义等价的查询变体。然而，为每个变体执行完整流程计算成本高昂，因此需要选择性执行：能否在产生下游检索和生成成本之前识别出最佳查询变体？本研究探讨了查询性能预测（QPP）作为跨即时检索和端到端 RAG 的变体选择机制。与估算跨主题查询难度的传统 QPP 不同，我们研究了“主题内区分”，即在同一信息需求的竞争变体中选择最优重构。通过在 TREC-...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Geometric Theoretical Framework for Dynamic Protein Mutation Detection Models: Defect Awareness and Pathogenicity Prediction](https://www.biorxiv.org/content/10.64898/2026.04.22.720255v1)
  来源：bioRxiv | 日期：2026-04-26 | 相关度：4.6 | 新颖度：5.75
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：传统蛋白质突变检测和致病性预测依赖静态单构象建模，忽略了构象柔性、动态系综演化及蛋白质动态背后的流形几何，导致在柔性区域和变构位点出现系统性失效。本研究建立了一个定理驱动的几何代数框架，用于动态蛋白质突变建模。该框架从动态构象黎曼流形出发，通过算子值观测的表示诱导补全构建潜空间，并将代数约束松弛为可学习的近似李代数正则化。通过整合列维-奇维塔联络、测地线偏离和热核渐近性，引入了利普希茨稳定的拓扑谱缺陷（TSD, δ_spec）指标，用于...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond](http://arxiv.org/abs/2604.22748v1)
  来源：arXiv | 日期：2026-04-24 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：随着人工智能系统从单纯的文本生成转向通过持续交互实现复杂目标，环境动力学建模能力已成为核心瓶颈。本文针对操纵物体、软件导航、社交协作及实验设计等任务，提出了“等级x定律（levels x laws）”分类框架。该框架包含三个能力等级：L1预测器（学习单步局部转移算子）、L2模拟器（构建符合领域定律的多步动作条件推演）和L3进化器（根据新证据自主修正模型）。同时识别了物理、数字、社会和科学四种治理定律范式，界定了模型必须满足的约束及潜在失...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [AI-readiness criteria for biomedical data](https://www.biorxiv.org/content/10.1101/2024.10.23.619844v6)
  来源：bioRxiv | 日期：2026-04-24 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：生物医学研究正迅速转向人工智能（AI）驱动模式，但生物医学数据的复杂性要求在“模型前”阶段（涵盖数据获取、转换和伦理治理）实施稳健的可操作标准，以确保AI的伦理性和可解释性（XAI）。研究指出，单纯遵循FAIR原则（可发现、可访问、可互操作、可重用）已不足以满足AI建模需求。为此，NIH Bridge2AI标准工作组定义了生物医学数据“AI就绪”（AI-readiness）的标准与实践，涵盖七个核心维度：FAIR性、溯源性、特征化、伦理...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [A Co-Evolutionary Theory of Human-AI Coexistence: Mutualism, Governance, and Dynamics in Complex Societies](http://arxiv.org/abs/2604.22227v1)
  来源：arXiv | 日期：2026-04-24 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：经典的机器人伦理通常围绕“服从”展开（如阿西莫夫定律），但这已不适用于当今具有适应性、生成性和具身性的 AI 系统。本文提出，未来的类人-AI 关系不应被视为“主人-工具”的服从关系，而应是在治理下的“条件互利主义”：一种共同演化的关系，使人类与 AI 系统能够共同发展、专业化并进行协作，同时通过制度保障关系的互惠性、可逆性、心理安全和社会合法性。研究综合了计算理论、自动机、统计机器学习、深度学习、生成式基础模型、具身 AI、生态互利共...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [The complexome contextualizes proteomics data to fingerprint biological states and highlight perturbed functional modules in disease.](https://pubmed.ncbi.nlm.nih.gov/42034643/)
  来源：PubMed | 日期：2026-04-25 | 相关度：3.05 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：分析单组学并整合多模态组学数据以捕捉疾病中的功能失调仍具挑战。本研究提出了一个生物信息学框架，利用人工策划的蛋白质复合物数据集（“复合物组”，complexome）作为蛋白质组学数据整合的基础。该框架适用于人类及其他模式生物，通过蛋白质复合物提供细胞功能的全局视角，并支持蛋白质组数据集的查询。研究首先基准测试了不同人体组织的蛋白质丰度如何塑造独特的复合物组特征，从而指征生物学状态。随后，通过对比疾病与对照组的蛋白质组定量数据，分析了复合...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Aligning Dense Retrievers with LLM Utility via DistillationAligning Dense Retrievers with LLM Utility via Distillation](http://arxiv.org/abs/2604.22722v1)
  来源：arXiv | 日期：2026-04-24 | 相关度：2.1 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：稠密向量检索是检索增强生成（RAG）的核心架构，但传统的相似度搜索在精度上存在局限。相比之下，利用大语言模型（LLM）重排序的效用驱动方法虽性能优异，但计算开销巨大且易受困惑度（perplexity）估计噪声的影响。本文提出效用对齐嵌入（UAE）框架，旨在将两者的优势整合为一种高效的检索方法。我们将检索建模为分布匹配问题，通过“效用调制 InfoNCE”目标函数训练双编码器，使其模仿由困惑度降幅推导出的效用分布。该方法直接将分级效用信号...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [A Scalable Method for Validated Data Extraction from Electronic Health Records with Large Language Models](https://www.medrxiv.org/content/10.1101/2025.02.25.25322898v2)
  来源：medRxiv | 日期：2026-04-25 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Purpose/Background: Healthcare organizations increasingly require structured, patient-level clinical variables for treatment decisions, operational workflows, quality measurement, and clinical trial screening. Relevant i...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Generalizing intensive care AI across time scales in resource-limited settings](https://www.medrxiv.org/content/10.64898/2026.04.23.26351588v1)
  来源：medRxiv | 日期：2026-04-24 | 相关度：2.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：重症监护中的生理监测时间分辨率在不同医疗系统中差异巨大，而现有AI模型通常假设采样频率固定，限制了其在资源受限地区的推广。本研究提出了一种针对生理时间序列的新型分辨率迁移任务，探讨在高分辨率数据上训练的模型能否在不重新训练的情况下推广到低数据密度环境。研究利用印度一家三级医院长达十年的新型儿科重症监护数据集SafeICU，包含984次住院的144,271个患者小时的高分辨率生理信号。研究采用自监督Transformer模型学习心率、呼吸...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Tuberculosis in households with infectious cases in Kampala city: Harnessing health data science for new insights on an ancient disease with persistent, unresolved problems (DS-IAFRICA TB) study protocol](https://www.medrxiv.org/content/10.64898/2026.04.23.26351571v1)
  来源：medRxiv | 日期：2026-04-25 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：乌干达坎帕拉市的结核病（TB）流行严重，且伴随高HIV共感染率。在主动筛查发现的未诊断病例中，30%以上为无症状感染者，且宿主与环境风险因素交织，传统方法难以区分。本研究（DS-IAFRICA TB）旨在利用健康数据科学（AI/ML）技术解决这一复杂性。研究将利用马凯雷雷大学的计算资源，整合结核病患者及其家庭接触者的人口统计学、临床和实验室数据，开发AI/ML算法。核心目标包括：(1) 在基线期（0月）预测哪些患者在治疗第2和第5个月时...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
