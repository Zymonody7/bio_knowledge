# 每日论文监控日报 (2026-03-15)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 38 篇新论文。

## 抓取状态

- arXiv：成功，命中 21 篇
- PubMed：成功，命中 38 篇
- bioRxiv：成功，命中 31 篇
- medRxiv：成功，命中 8 篇

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [EnsAgent: a tool-ensemble multiple Agent system for robust annotation in spatial transcriptomics](https://www.biorxiv.org/content/10.64898/2026.03.10.710824v1)
  来源：bioRxiv | 日期：2026-03-13 | 相关度：8.9 | 新颖度：2.2
  匹配主题：foundation_model_agent
  中文摘要：Motivation: Automated domain annotation in spatially resolved transcriptomics (SRT) remains challenging since it depends on gene expression, morphology, and clinical conventions, which vary across cohorts and platforms. ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ELISA: An Interpretable Hybrid Generative AI Agent for Expression-Grounded Discovery in Single-Cell Genomics](http://arxiv.org/abs/2603.11872v1)
  来源：arXiv | 日期：2026-03-12 | 相关度：7.55 | 新颖度：2.5
  匹配主题：foundation_model_agent
  中文摘要：Translating single-cell RNA sequencing (scRNA-seq) data into mechanistic biological hypotheses remains a critical bottleneck, as agentic AI systems lack direct access to transcriptomic representations while expression fo...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Can Theoretical Physics Research Benefit from Language Agents?](http://arxiv.org/abs/2506.06214v2)
  来源：arXiv | 日期：2025-06-06 | 相关度：7.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) are rapidly advancing across diverse domains, yet their application in theoretical physics remains inadequate. While current models show competence in mathematical reasoning and code generati...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback](http://arxiv.org/abs/2603.08561v3)
  来源：arXiv | 日期：2026-03-09 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Standard reinforcement learning (RL) for large language model (LLM)-based agents typically optimizes extrinsic task-success rewards, prioritizing one-off task solving over continual adaptation. As a result, agents may co...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multi-Agent Collaboration for Automated Design Exploration on High Performance Computing Systems](http://arxiv.org/abs/2603.11515v1)
  来源：arXiv | 日期：2026-03-12 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Today's scientific challenges, from climate modeling to Inertial Confinement Fusion design to novel material design, require exploring huge design spaces. In order to enable high-impact scientific discovery, we need to s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Toward AI foundation models for epidemics: Promise, challenges, and paths forward.](https://pubmed.ncbi.nlm.nih.gov/41824492/)
  来源：PubMed | 日期：2026-03-31 | 相关度：4.4 | 新颖度：5.5
  匹配主题：pathogenomics
  中文摘要：基础模型（如 GPT、GenCast、AlphaFold）通过在大规模异构数据上预训练，已显著改变科学发现模式，但在流行病建模领域尚未实现类似转型。传统模型通常针对特定病原体，在应对如 SARS-CoV-2 等突发疫情时，往往难以快速生成见解。本文探讨了将基础模型范式扩展至流行病学的可行性，旨在构建一个能捕捉跨病原体、人群和环境的传染病动力学共享原则的单一预训练模型。该模型仅需极少数据即可微调至新环境，实现更快速的预测、推理和响应，对资...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Ultra-Fast Language Generation via Discrete Diffusion Divergence Instruct](http://arxiv.org/abs/2509.25035v3)
  来源：arXiv | 日期：2025-09-29 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Fast and high-quality language generation is the holy grail that people pursue in the age of AI. In this work, we introduce Discrete Diffusion Divergence Instruct (DiDi-Instruct), a training-based method that initializes...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [stMCP: Spatial Transcriptomics with a Model Context Protocol Server](https://www.biorxiv.org/content/10.64898/2026.03.11.710153v1)
  来源：bioRxiv | 日期：2026-03-14 | 相关度：5.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Spatial transcriptomics enables high-resolution mapping of gene expression in intact tissues but remains challenging due to complex computational workflows that limit accessibility and reproducibility. Here, we present a...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [From Study Design to Executable Code: Automating Target Trial Emulation with Large Language Models](https://www.medrxiv.org/content/10.64898/2026.03.13.26348306v1)
  来源：medRxiv | 日期：2026-03-14 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Introduction: Implementing target trial emulation (TTE) study methods as end-to-end executable analytic code is technically demanding, and producing standardized, reproducible scripts consistently across research teams r...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [GUIDES: Guidance Using Instructor-Distilled Embeddings for Pre-trained Robot Policy Enhancement](http://arxiv.org/abs/2511.03400v3)
  来源：arXiv | 日期：2025-11-05 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Pre-trained robot policies serve as the foundation of many validated robotic systems, which encapsulate extensive embodied knowledge. However, they often lack the semantic awareness characteristic of foundation models, a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [QUARE: Multi-Agent Negotiation for Balancing Quality Attributes in Requirements Engineering](http://arxiv.org/abs/2603.11890v1)
  来源：arXiv | 日期：2026-03-12 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Requirements engineering (RE) is critical to software success, yet automating it remains challenging because multiple, often conflicting quality attributes must be balanced while preserving stakeholder intent. Existing L...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evaluating transformer-based models for structural characterization of orphan proteins](https://www.biorxiv.org/content/10.64898/2026.03.10.709490v1)
  来源：bioRxiv | 日期：2026-03-12 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：基于Transformer的模型（TBM）是预测蛋白质结构和功能特征的最先进深度学习架构。尽管方法各异，但它们均依赖于按同源性组织的大规模蛋白质序列数据集。然而，真核生物蛋白质组中有5-30%属于孤儿蛋白，即与已知家族无检测相似性的序列。由于缺乏同源性，孤儿蛋白成为评估TBM在熟悉序列空间外泛化能力的理想对象。本研究利用根结线虫属（Meloidogyne）中经专家策划的孤儿蛋白集，对比了多种常用TBM架构的预测性能。评估发现，基于多序列...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DocSage: An Information Structuring Agent for Multi-Doc Multi-Entity Question Answering](http://arxiv.org/abs/2603.11798v1)
  来源：arXiv | 日期：2026-03-12 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Multi-document Multi-entity Question Answering inherently demands models to track implicit logic between multiple entities across scattered documents. However, existing Large Language Models (LLMs) and Retrieval-Augmente...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TURA: Tool-Augmented Unified Retrieval Agent for AI Search](http://arxiv.org/abs/2508.04604v2)
  来源：arXiv | 日期：2025-08-06 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：The advent of Large Language Models (LLMs) is transforming search engines into conversational AI search products, primarily using Retrieval-Augmented Generation (RAG) on web corpora. However, this paradigm has significan...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Automating Skill Acquisition through Large-Scale Mining of Open-Source Agentic Repositories: A Framework for Multi-Agent Procedural Knowledge Extraction](http://arxiv.org/abs/2603.11808v1)
  来源：arXiv | 日期：2026-03-12 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：The transition from monolithic large language models (LLMs) to modular, skill-equipped agents represents a fundamental architectural shift in artificial intelligence deployment. While general-purpose models demonstrate r...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Truncated Step-Level Sampling with Process Rewards for Retrieval-Augmented Reasoning](http://arxiv.org/abs/2602.23440v2)
  来源：arXiv | 日期：2026-02-26 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Training large language models to reason with search engines via reinforcement learning is hindered by a fundamental credit assignment problem: existing methods such as Search-R1 provide only a sparse outcome reward afte...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [User-driven development and evaluation of an agentic framework for analysis of large pathway diagrams](https://www.biorxiv.org/content/10.64898/2026.03.10.710813v1)
  来源：bioRxiv | 日期：2026-03-12 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：随着生物医学知识的持续增长，存储分子相互作用图谱（描述正常或病理状态下的细胞与分子过程）的资源在规模和复杂性上不断增加，导致非专业用户难以导航和理解。本文介绍了一种基于大语言模型（LLM）的智能体（Agentic）框架——Llemy，旨在辅助用户探索这些复杂的分子相互作用图谱。研究采用用户驱动的开发流程，从最初的黑客松原型设计阶段起便邀请领域专家参与，并针对后续精细化版本收集了细粒度及通用的用户反馈。通过评估，研究验证了 Llemy 在...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CARROT: A Learned Cost-Constrained Retrieval Optimization System for RAG](http://arxiv.org/abs/2411.00744v2)
  来源：arXiv | 日期：2024-11-01 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：大语言模型（LLMs）在生成和推理中常面临知识更新滞后及幻觉问题。检索增强生成（RAG）通过引入外部知识块来缓解此问题，但现有系统存在三大挑战：知识块检索相互独立，忽略了冗余和顺序等相关性；知识块效用呈非单调性，增加数量可能降低生成质量；检索策略难以适应不同查询的特性。为此，本研究提出了 CARROT，一个受成本约束的 RAG 检索优化框架。该框架采用蒙特卡洛树搜索（MCTS）策略，通过考虑块间相关性来寻找最优的知识块组合顺序。针对效用...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Entity-Centric to Goal-Oriented Graphs: Enhancing LLM Knowledge Retrieval in Minecraft](http://arxiv.org/abs/2505.18607v2)
  来源：arXiv | 日期：2025-05-24 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：大语言模型（LLMs）在通用能力上表现出色，但在处理复杂交互环境中的分步程序化推理时常面临挑战。虽然像 GraphRAG 这样的检索增强方法试图弥补这一差距，但其碎片化的实体关系图阻碍了连贯多步计划的构建。本文提出了一种基于目标导向图（Goal-Oriented Graphs, GoGs）的新型框架，其中每个节点代表一个目标，边则编码目标间的逻辑依赖关系。该结构通过识别高层目标并递归检索其先决条件，显式检索出因果推理路径，从而形成引导 ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ARK: Answer-Centric Retriever Tuning via KG-augmented Curriculum Learning](http://arxiv.org/abs/2511.16326v2)
  来源：arXiv | 日期：2025-11-20 | 相关度：2.1 | 新颖度：1.75
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）在知识密集型任务中表现出色，但在长文本场景下，检索器往往因无法识别稀疏但关键的证据而面临瓶颈。传统的检索器多基于查询-文档相似度进行优化，难以对齐生成准确答案的下游目标。为此，我们提出了 ARK 框架，通过“答案对齐”优化检索器。该方法首先通过评估文本块对于生成正确答案的充分性来识别高质量正样本；随后采用基于课程学习的对比学习方案进行微调。该方案利用大语言模型（LLM）构建的知识图谱（KG）生成增强查询，从而挖掘难...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multi-modal benchmarking of the Ultima UG100 and Illumina NovaSeq sequencing platforms using clinically relevant FFPE tissues](https://www.biorxiv.org/content/10.64898/2026.03.11.710846v1)
  来源：bioRxiv | 日期：2026-03-13 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：本研究在临床相关的福尔马林固定石蜡包埋（FFPE）组织中，对 Ultima Genomics UG100 与 Illumina NovaSeq 测序平台进行了多模态基准测试。研究涵盖了单核 RNA 测序（snRNA-seq）、全转录组（WTS）、全外显子组（WES）和全基因组测序（WGS），涉及肿瘤和免疫介导疾病样本。通过系统评估数据质量、覆盖度、错误谱、变异一致性和转录组重现性，结果显示 UG100 与 Illumina 具有高度可比...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Benchmarking zero-shot single-cell foundation model embeddings for cellular dynamics reconstruction](https://www.biorxiv.org/content/10.64898/2026.03.10.710748v1)
  来源：bioRxiv | 日期：2026-03-12 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：从时间分辨单细胞转录组中重建细胞轨迹对于理解从胚胎发育到癌症进展的生物过程至关重要。虽然单细胞基础模型（scFMs）通过大规模预训练承诺提供通用的生物学表征，但其捕获控制细胞命运决定的非线性动力学能力尚未得到表征。本研究在涉及分支谱系和连续状态转换的挑战性生物医学场景中，系统地评估了多种 scFM。通过将零样本 scFM 嵌入与动态最优传输相结合，我们在回溯祖细胞状态、插值转换中间体和外推未来命运方面，将其性能与传统的高变基因（HVG）...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Statistical and structural identifiability in representation learning](http://arxiv.org/abs/2603.11970v1)
  来源：arXiv | 日期：2026-03-12 | 相关度：1.4 | 新颖度：1.5
  匹配主题：未命中具体主题
  中文摘要：表示学习模型在内部表示上表现出惊人的稳定性。先前研究多将其视为单一属性，本文将其形式化为两个独立概念：统计可识别性（不同运行间表示的一致性）和结构可识别性（表示与未观测真实值的对齐）。鉴于现代模型难以实现完美的逐点可识别性，本文提出了模型无关的 $\epsilon$-近可识别性定义。利用该定义，作者证明了具有非线性解码器模型的统计 $\epsilon$-近可识别性，将现有理论从 GPT 等模型的顶层表示扩展到包括掩码自编码器（MAE）和...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Exhaustive Circuit Mapping of a Single-Cell Foundation Model Reveals Massive Redundancy, Heavy-Tailed Hub Architecture, and Layer-Dependent Differentiation Control](http://arxiv.org/abs/2603.11940v1)
  来源：arXiv | 日期：2026-03-12 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：本研究针对生物基础模型解释性中存在的选择性特征采样偏差，对基于 Transformer 的单细胞基础模型 Geneformer 进行了详尽的电路映射。研究通过三个实验揭示了其内部机制：首先，对第 5 层的 4065 个稀疏自编码器（SAE）特征进行穷举追踪，发现了 1,393,850 条显著下游边，比选择性采样扩大了 27 倍，揭示了长尾中心架构，其中 1.8% 的特征贡献了极高连接性，且 40% 的核心特征缺乏生物学注释。其次，通过对...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [HitAnno: Atlas-level cell type annotation based on scATAC-seq data via a hierarchical language model](https://www.biorxiv.org/content/10.64898/2026.03.10.710729v1)
  来源：bioRxiv | 日期：2026-03-12 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：单细胞转座酶可及染色质测序（scATAC-seq）是剖析细胞表观基因组异质性和基因调控程序的关键技术。随着图谱级数据集的出现，细胞类型注释面临数据规模空前和细胞类型多样性增加的挑战，对模型的可靠性和鲁棒性提出了严苛要求。本文提出 HitAnno，一种能够对图谱级 scATAC-seq 数据进行准确且可扩展注释的分层语言模型。HitAnno 利用选定的细胞类型特异性峰（peaks）构建“细胞句子”，并采用两级注意力机制分层捕捉染色质可及性...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Legal-DC: Benchmarking Retrieval-Augmented Generation for Legal Documents](http://arxiv.org/abs/2603.11772v1)
  来源：arXiv | 日期：2026-03-12 | 相关度：4.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) has emerged as a promising technology for legal document consultation, yet its application in Chinese legal scenarios faces two key limitations: existing benchmarks lack specialized s...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [SINDI: an Efficient Index for Approximate Maximum Inner Product Search on Sparse Vectors](http://arxiv.org/abs/2509.08395v3)
  来源：arXiv | 日期：2025-09-10 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Sparse vector Maximum Inner Product Search (MIPS) is crucial in multi-path retrieval for Retrieval-Augmented Generation (RAG). Recent inverted index-based and graph-based algorithms have achieved high search accuracy wit...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [The landscape of structural variation in pediatric cancer.](https://pubmed.ncbi.nlm.nih.gov/41825442/)
  来源：PubMed | 日期：2026-03-12 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：结构变异（SVs）占儿童癌症驱动变异的60%以上。本研究通过对1,616例儿童和2,203例成人全基因组（WGS）的泛癌分析显示，儿童癌症的SV负荷在不同癌种间存在约100倍的差异；与成人脑肿瘤和实体瘤相比，儿童的SV负荷降低了6至16倍，但在血液系统恶性肿瘤中两者相当。研究发现，受SV干扰最严重的基因在儿童中多为驱动基因，而在成人中则多为脆性位点。在儿童急性淋巴细胞白血病中，RAG重组信号序列附近的复发性SV热点会破坏免疫位点和驱动基...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Cyclic peptides space: The methodology of sequence selection to cover the comprehensive physical properties](https://www.biorxiv.org/content/10.64898/2026.03.10.710724v1)
  来源：bioRxiv | 日期：2026-03-12 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Cyclic peptides have emerged as a pivotal modality for next-generation therapeutics, due to their superior biocompatibility, high selectivity, and structural stability. While AI-driven peptide design has advanced rapidly...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Highly accurate ab initio gene annotation with ANNEVO.](https://pubmed.ncbi.nlm.nih.gov/41820667/)
  来源：PubMed | 日期：2026-03-12 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Accurate gene annotation is essential for deciphering the mapping from genomic sequences to their functional roles. However, current methods struggle to model complex gene transmission patterns, such as vertical inherita...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Application of large language models to the annotation of cell lines and mouse strains in genomics data](https://www.biorxiv.org/content/10.64898/2026.03.05.709906v2)
  来源：bioRxiv | 日期：2026-03-12 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：这篇论文来自 bioRxiv，主题上与 foundation_model_agent 有交叉。原始英文摘要要点如下：Accurate, consistent and comprehensive metadata are essential for the reuse of functional genomics data deposited in repositories such as the Gene Expression Omni...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [QChunker: Learning Question-Aware Text Chunking for Domain RAG via Multi-Agent Debate](http://arxiv.org/abs/2603.11650v1)
  来源：arXiv | 日期：2026-03-12 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：The effectiveness upper bound of retrieval-augmented generation (RAG) is fundamentally constrained by the semantic integrity and information granularity of text chunks in its knowledge base. To address these challenges, ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Rapid and Interpretable AMR Diagnostics via Genomics and Cell Painting using Differential Geometry-based Directed-Simplicial Neural Networks on Multimodal Data](https://www.biorxiv.org/content/10.64898/2026.03.11.711128v1)
  来源：bioRxiv | 日期：2026-03-12 | 相关度：4.75 | 新颖度：1.0
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：针对全球及印度等高流行地区的抗生素耐药性（AMR）挑战，本研究提出了一种整合基因组与细胞表型数据的多模态计算框架。该框架利用基于微分几何的有向单纯神经网络（Dg Dir SNNs）分析了384个临床相关的AMR分离株（包括大肠杆菌和肺炎克雷伯菌）。研究整合了256个基因组k-mer特征和503个源自高内涵Cell Painting实验的细胞形态描述符。Dg Dir SNNs模型构建了顶级生物标志物驱动特征的推断因果网络，预测了基因组基序...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Learning the All-Atom Equilibrium Distribution of Biomolecular Interactions at Scale](https://www.biorxiv.org/content/10.64898/2026.03.10.710952v1)
  来源：bioRxiv | 日期：2026-03-13 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：生物分子的功能由动态构象系综而非静态结构决定。尽管 AlphaFold 等模型革新了静态结构预测，但由于分子动力学（MD）计算成本高昂，准确捕捉全原子生物分子相互作用的平衡分布仍是重大挑战。本研究提出了 AnewSampling，这是一个可迁移的生成式基础框架，旨在实现全原子平衡分布的高保真采样，是首个在全原子水平上忠实再现 MD 的模型。该模型采用新型商空间（quotient-space）生成框架以确保数学一致性，并利用了包含超过 1...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Multiscale conformational sampling of multidomain fusion proteins by a physics informed diffusion model](https://www.biorxiv.org/content/10.64898/2026.03.11.711061v1)
  来源：bioRxiv | 日期：2026-03-13 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：多结构域融合蛋白（如双特异性抗体）的疗效高度依赖其灵活的接头（linker）区域。表征这些庞大的构象系综对理性药物设计至关重要，但传统全原子分子动力学（MD）的高昂计算成本限制了对大规模结构域运动的模拟。虽然深度生成扩散模型已成为采样蛋白质动力学的快速替代方案，但现有模型多基于静态结构数据库训练，缺乏处理高度柔性多结构域架构所需的生物物理约束。为解决此问题，本研究利用包含多种接头的多结构域蛋白微秒级MD轨迹，训练了一个基于等变图神经网络...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Multi-Criteria Validation of LLM-Inferred Depression Severity from Outpatient Psychiatry Notes](https://www.medrxiv.org/content/10.64898/2026.03.11.26348066v1)
  来源：medRxiv | 日期：2026-03-12 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：门诊精神科护理中，抑郁严重程度的纵向测量受限于标准化评估的频率。本研究评估了大语言模型（LLM）从门诊精神科病程记录中推断临床抑郁严重程度的能力。研究收集了某大型医学中心2015-2021年间58家诊所、8,287名成年患者的91,651份病历。使用符合HIPAA标准的GPT-5.2模型，从脱敏后的病历中独立推断PHQ-9、HAM-D和CGI-S评分。结果显示，LLM推断的PHQ-9评分与患者自评结果具有中度一致性（Pearson r=...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Can Small Language Models Use What They Retrieve? An Empirical Study of Retrieval Utilization Across Model Scale](http://arxiv.org/abs/2603.11513v1)
  来源：arXiv | 日期：2026-03-12 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval augmented generation RAG is widely deployed to improve factual accuracy in language models yet it remains unclear whether smaller models of size 7B parameters or less can effectively utilize retrieved informati...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [Biodesign Buddy: Integrating Generative Artificial Intelligence in Academic Biodesign](https://www.biorxiv.org/content/10.64898/2026.03.11.710906v1)
  来源：bioRxiv | 日期：2026-03-13 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：生物设计（Biodesign）教育是一个结合设计实践与生命科学的新兴跨学科领域，旨在开发新型生物系统、材料和工艺。尽管相关竞赛和项目日益增多，但教育者在课程设计及培养非STEM背景学生的科学素养方面仍面临挑战。本研究探讨了领域特定生成式人工智能系统“Biodesign Buddy”的教学潜力。研究通过对参与国际生物设计竞赛的64名学生进行为期八周的部署，采用混合方法分析了问卷调查、教师反馈和学生设计笔记。评估重点在于AI辅助学习如何影响...
  为什么值得看：bioRxiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。
