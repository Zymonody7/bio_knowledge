# 每日论文监控日报 (2026-05-11)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 27 篇新论文。

## 抓取状态

- arXiv：成功，命中 22 篇
- PubMed：成功，命中 39 篇
- bioRxiv：成功，命中 10 篇
- medRxiv：成功，命中 6 篇

## 最值得看

### Foundation Model / Agent

- [Think Before You Drive: World Model-Inspired Multimodal Grounding for Autonomous Vehicles](http://arxiv.org/abs/2512.03454v4)
  来源：arXiv | 日期：2025-12-03 | 相关度：7.9 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：Interpreting natural-language commands to localize target objects is critical for autonomous driving (AD). Existing visual grounding (VG) methods for autonomous vehicles (AVs) typically struggle with ambiguous, context-d...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Standalone LLMs to Integrated Intelligence: A Survey of Compound Al Systems](http://arxiv.org/abs/2506.04565v2)
  来源：arXiv | 日期：2025-06-05 | 相关度：7.9 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Compound AI Systems (CAIS) are an emerging paradigm that integrates large language models (LLMs) with external components, including retrievers, agents, tools, and orchestrators, to overcome the limitations of standalone...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Unified genomic and chemical representations enable bidirectional biosynthetic gene cluster and natural product retrieval.](https://pubmed.ncbi.nlm.nih.gov/42106434/)
  来源：PubMed | 日期：2026-05-09 | 相关度：8.5 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Natural product discovery is increasingly driven by the ability to analyze microbial genomes for biosynthetic gene clusters (BGCs) that encode secondary metabolites. While existing approaches have successfully linked BGC...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [Benchmarking and behavioral characterization of LLM agents for protein design](https://www.biorxiv.org/content/10.64898/2026.05.06.723381v1)
  来源：bioRxiv | 日期：2026-05-08 | 相关度：7.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly deployed as agents for scientific discovery, but standardized frameworks for evaluating their performance and behaviour in scientific workflows are lacking. Protein design pr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Prototype Guided Post-pretraining for Single-Cell Representation Learning](http://arxiv.org/abs/2605.07938v1)
  来源：arXiv | 日期：2026-05-08 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Single-cell representation learning (SCRL) from gene expression data offers a way to uncover the complex regulatory logic underlying cellular function. Inspired by large language models in natural language modeling, seve...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AI CFD Scientist: Toward Open-Ended Computational Fluid Dynamics Discovery with Physics-Aware AI Agents](http://arxiv.org/abs/2605.06607v2)
  来源：arXiv | 日期：2026-05-07 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Recent LLM-based agents have closed substantial portions of the scientific discovery loop in software-only machine-learning research, in chemistry, and in biology. Extending the same loop to high-fidelity physical simula...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Open-Rosalind: Tool-First Biomedical LLM Agents with Process-Aware Benchmarking](https://www.biorxiv.org/content/10.64898/2026.05.06.722404v1)
  来源：bioRxiv | 日期：2026-05-08 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models are increasingly used as scientific agents, yet the flexibility that benefits general-purpose agents can conflict with the accountability required in biomedical research. We study whether biomedical...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [LARAG: Link-Aware Retrieval Strategy for RAG Systems in Hyperlinked Technical Documentation](http://arxiv.org/abs/2605.07517v1)
  来源：arXiv | 日期：2026-05-08 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) enhances the factual grounding of Large Language Models by conditioning their outputs on external documents. However, standard embedding-based retrievers treat naturally structured co...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Characterizing and Mitigating False-Positive Bug Reports in the Linux Kernel](http://arxiv.org/abs/2605.07678v1)
  来源：arXiv | 日期：2026-05-08 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：False-positive bug reports represent a significant yet underexplored challenge in the development and maintenance of the Linux kernel. They occur when correct system behavior is mistakenly flagged as a defect, consuming ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [DisastRAG: A Multi-Source Disaster Information Integration and Access System Based on Retrieval-Augmented Large Language Models](http://arxiv.org/abs/2605.05210v2)
  来源：arXiv | 日期：2026-04-06 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：有效的灾害管理需要快速获取分布在结构化运行记录、非结构化机构文档和动态外部来源中的信息。然而，现有系统多采用单一访问路径，难以支持异构、时效性强且依赖上下文的信息需求。本研究提出 DisastRAG，一个结合大语言模型（LLM）与检索增强生成（RAG）的灾害信息集成系统。该框架采用多路径架构，支持对精选灾害语料库的文档检索、对关系型灾害记录的结构化访问以及针对库外请求的外部网页回退，并集成了查询理解、策略路由、响应生成和上下文记忆。通过...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [UPhAIR: A Hybrid Pipeline for Generating Understandable Post-hoc AI Reports in Glioma IDH Mutation Status Prediction](https://www.medrxiv.org/content/10.64898/2026.05.01.26349658v1)
  来源：medRxiv | 日期：2026-05-08 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Clinical adoption of machine learning (ML) in medical imaging is limited by the lack of interpretability. To address this, we present understandable post-hoc artificial intelligence reports (UPhAIR), a pipeline designed ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Protein language model-guided generative design of affinity peptides for chromatographic purification of lentiviral vectors.](https://pubmed.ncbi.nlm.nih.gov/41833101/)
  来源：PubMed | 日期：2026-05-10 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Lentiviral vectors (LVs) have emerged as the most promising tool for cell and gene therapy. However, LVs are very fragile and sensitive to shear stress, buffer pH and salt concentration, resulting in serious hurdles in d...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [POETS: Uncertainty-Aware LLM Optimization via Compute-Efficient Policy Ensembles](http://arxiv.org/abs/2605.07775v1)
  来源：arXiv | 日期：2026-05-08 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Balancing exploration and exploitation is a core challenge in sequential decision-making and black-box optimization. We introduce POETS ($\textbf{Po}$licy $\textbf{E}$nsembles for $\textbf{T}$hompson $\textbf{S}$ampling)...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Functional alignment of protein language models via reinforcement learning](https://www.biorxiv.org/content/10.1101/2025.05.02.651993v2)
  来源：bioRxiv | 日期：2026-05-08 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Protein language models (pLMs) enable generative design of novel protein sequences but remain fundamentally misaligned with protein engineering goals, as they lack explicit understanding of function and often fail to imp...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MIPIAD: Multilingual Indirect Prompt Injection Attack Defense with Qwen -- TF-IDF Hybrid and Meta-Ensemble Learning](http://arxiv.org/abs/2605.07269v1)
  来源：arXiv | 日期：2026-05-08 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Indirect prompt injection remains a persistent weakness in retrieval-augmented and tool-using LLM systems, and the problem becomes harder to characterise in multilingual settings. We present MIPIAD, a defense framework e...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [Prompt-engineering improves clinical safety of large language models for opioid equipotency conversion](https://www.medrxiv.org/content/10.64898/2026.05.06.26352590v1)
  来源：medRxiv | 日期：2026-05-08 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Background: Large language models (LLMs) are increasingly used in medical education and clinical decision-making, but their reliability in high-risk medication dosing remains unclear. Opioid rotation is a common task req...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PAIR-Former: Budgeted Relational Multi-Instance Learning for Functional miRNA Target Prediction](http://arxiv.org/abs/2602.00465v3)
  来源：arXiv | 日期：2026-01-31 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：功能性 miRNA-mRNA 靶向预测是一个典型的大包（large-bag）预测问题，每个转录本包含大量候选靶位点（CTS），但仅能观测到对级别的标签。现有方法多采用针对单个位点得分的最大池化，忽略了位点间的关联模式，而建模这些模式对提高准确性至关重要。由于位点数量 $n$ 可达数千，朴素的关联聚合计算复杂度为 $O(n^2)$，计算成本极高。本研究提出了“预算受限的关联多实例学习”（BR-MIL）框架，将计算预算 $K$ 作为核心约束...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Transforming Semi-structured Variant Assessments into Computable Clinical Assertions: A Pilot Study for AI-Assisted Curation](https://www.medrxiv.org/content/10.64898/2026.05.07.26352456v1)
  来源：medRxiv | 日期：2026-05-08 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：基因组医学依赖专家对基因变异的评估，但由于缺乏易于获取的基因组知识，这一过程受到严重阻碍。尽管 ClinVar 和 CIViC 等资源支持结构化数据共享，但上游产生的大量变异解释数据与这些资源不兼容，导致了知识孤岛。本研究评估了一种将半结构化变异分类知识转化为可计算临床断言的策略，该策略遵循全球基因组学与健康联盟（GA4GH）的基因组知识标准规范。研究人员通过程序化方式将电子表格中的体细胞癌症临床意义分类映射到 GA4GH 变异注释规范...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Contextual Invertible World Models: A Neuro-Symbolic Agentic Framework for Colorectal Cancer Drug Response](http://arxiv.org/abs/2603.02274v2)
  来源：arXiv | 日期：2026-03-01 | 相关度：2.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：精准肿瘤学目前受限于“小样本、高维度”悖论，即基因组数据丰富但药敏响应样本稀缺，且深度学习模型往往缺乏临床所需的机制透明度。本研究提出“上下文可逆世界模型”（CIWM），这是一种将定量机器学习仿真器与基于大语言模型（LLM）的推理层相结合的神经符号智能体框架。通过在Sanger GDSC数据集（N=83）上利用零泄露取证流水线进行验证，该模型实现了稳健的预测相关性（r=0.447, p=2.30e-05）。研究识别出“符号支架”效应，即...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [TSAssistant: A Human-in-the-Loop Agentic Framework for Automated Target Safety Assessment](http://arxiv.org/abs/2604.23938v2)
  来源：arXiv | 日期：2026-04-27 | 相关度：2.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：靶点安全性评估（TSA）需要系统整合遗传学、转录组学、靶点同源性、药理学和临床数据等多源异构证据，以评估治疗靶点的潜在安全性风险。该过程具有高度迭代性和专家驱动特征，在可扩展性和可重复性方面面临挑战。本文提出 TSAssistant，这是一个基于多智能体框架的自动化 TSA 报告撰写系统，采用模块化、分章节及人机协同（human-in-the-loop）范式。该框架将报告生成任务分解为由专门子智能体组成的协调流水线，每个子智能体负责特定...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Pretraining a Foundation Model for Small-Molecule Natural Products](http://arxiv.org/abs/2503.17656v4)
  来源：arXiv | 日期：2025-03-22 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：天然产物作为微生物、动物或植物的代谢产物，具有多样的生物活性，是药物研发的关键来源。目前的深度学习方法主要依赖针对特定下游任务的监督学习，缺乏泛化性且性能提升空间有限，且现有分子表征方法难以适配天然产物的独特任务。本研究开发了针对天然产物属性预训练的基础模型 NaFM。该模型采用创新的预训练策略，结合对比学习和掩码图学习目标，在捕捉侧链信息的同时，强调分子骨架的进化信息。实验结果显示，NaFM 在天然产物挖掘和药物研发的多种下游任务中达...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Validation of an AI-Powered Automated Colony Analysis Platform Across Eight ISO Microbiological Methods: A Multi-Pathogen, Multi-Matrix Performance Study](https://www.biorxiv.org/content/10.64898/2026.05.08.723721v1)
  来源：bioRxiv | 日期：2026-05-09 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：手动菌落计数是食品微生物质量控制（QC）中受操作者影响的限速步骤。本研究对 Reshape Smart Incubator（一种基于机器学习的自动化成像与菌落分析系统）进行了前瞻性、多研究验证，涵盖 8 种 ISO 微生物参考方法。研究共分析了 887 张培养皿，包括对李斯特菌（ISO 11290-1）和沙门氏菌（ISO 6579）的定性检测，以及对菌落总数（ISO 4833）、蜡样芽孢杆菌（ISO 7932）、肠杆菌科（ISO 215...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Retrieval from Within: An Intrinsic Capability of Attention-Based Models](http://arxiv.org/abs/2605.05806v2)
  来源：arXiv | 日期：2026-05-07 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）通常将检索和生成视为两个独立的系统。本研究探讨了基于注意力的编码器-解码器模型是否可以直接从其内部表示中进行检索。我们提出了 INTRA（通过注意力的内在检索）框架，在该框架中，解码器注意力查询对预编码的证据块进行评分，随后这些证据块被直接复用为生成的上下文。INTRA 在结构上统一了检索和生成，消除了传统 RAG 流程中检索器与生成器之间的不匹配问题。此外，该设计通过在不同查询中复用预计算的编码器状态，分摊了上下...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Response-G1: Explicit Scene Graph Modeling for Proactive Streaming Video Understanding](http://arxiv.org/abs/2605.07575v1)
  来源：arXiv | 日期：2026-05-08 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：主动流式视频理解要求视频大语言模型（Video-LLMs）在视频展开过程中自主决定何时做出响应。现有方法由于对视觉证据采用隐式且与查询无关的建模，往往难以准确把握响应时机。本文提出 Response-G1 框架，通过场景图（scene graphs）在累积的视频证据与查询预期的响应条件之间建立显式、结构化的对齐。该框架包含三个无需微调的阶段：(1) 从流式视频剪辑中生成在线查询引导的场景图；(2) 基于内存检索语义最相关的历史场景图；(...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [FAVOR: Efficient Filter-Agnostic Vector ANNS Based on Selectivity-Aware Exclusion Distances](http://arxiv.org/abs/2605.07770v1)
  来源：arXiv | 日期：2026-05-08 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：现代检索系统日益需要将近似最近邻搜索（ANNS）与复杂属性过滤相结合，以处理推荐系统和检索增强生成（RAG）中的混合查询。针对现有基于 HNSW 的内联过滤方法在低选择性场景下吞吐量低，且难以平衡搜索效率、过滤通用性与索引连通性的挑战，本文提出 FAVOR。这是一种高效且与过滤条件无关的向量 ANNS 框架，支持任意过滤条件并在不同选择性水平下保持性能稳定。FAVOR 引入了三大核心特性：(1) 集成架构，统一了选择性估计与过滤 ANN...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [DentaCoPilot: An LLM-Augmented Next-Procedure Recommender for General Dentistry, Designed for Dentist Augmentation](https://www.medrxiv.org/content/10.64898/2026.05.07.26352635v1)
  来源：medRxiv | 日期：2026-05-08 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：2026年的商业牙科AI主要集中在影像学诊断（如龋齿、牙槽骨检测），但针对“下一步该做什么”的临床决策支持仍是难题。本研究推出DentaCoPilot，这是一款基于结构化病历推荐后续操作的系统。该系统可输出当前牙科术语（CDT）代码的Top-K概率分布、置信度标签、在信息不足时的弃权标志以及基于病历的解释理由。研究对比了4种传统基准（如XGBoost、CNN-RNN）与6种大语言模型（LLM）变体（如Claude Sonnet/Opus...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial intelligence, omics, and biomarkers: Redefining lung cancer early detection.](https://pubmed.ncbi.nlm.nih.gov/42105533/)
  来源：PubMed | 日期：2026-05-08 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：肺癌是全球范围内导致死亡的主要原因，由于早期干预手段有限，每年夺走数百万人的生命。目前的肺癌筛查方法受限于侵入性、辐射暴露以及早期灵敏度低等问题，迫切需要创新技术。本综述探讨了结合生物标志物、组学方法与人工智能（AI）技术的肺癌早期检测新兴工具。肿瘤细胞释放的特定生物标志物（如细胞成分、核酸片段、蛋白质片段或代谢物）可通过非侵入性方法从体液中检测。将生物标志物与蛋白质组学、基因组学或多组学技术整合，可提供不同癌症亚型和阶段的全面分子图谱...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
