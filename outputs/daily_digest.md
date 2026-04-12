# 每日论文监控日报 (2026-04-12)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 26 篇新论文。

## 抓取状态

- arXiv：成功，命中 19 篇
- PubMed：成功，命中 26 篇
- bioRxiv：成功，命中 25 篇
- medRxiv：成功，命中 0 篇

## 最值得看

### 方法创新

- [EVEE: Interpretable variant effect prediction from genomic foundation model embeddings](https://www.biorxiv.org/content/10.64898/2026.04.10.717844v1)
  来源：bioRxiv | 日期：2026-04-11 | 相关度：9.6 | 新颖度：6.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Predicting the clinical significance of genetic variants remains a central challenge in genomic medicine, with most observed variants classified as variants of uncertain significance. Here we show that representations fr...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [Figures as Interfaces: Toward LLM-Native Artifacts for Scientific Discovery](http://arxiv.org/abs/2604.08491v1)
  来源：arXiv | 日期：2026-04-09 | 相关度：7.9 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are transforming scientific workflows, not only through their generative capabilities but also through their emerging ability to use tools, reason about data, and coordinate complex analytica...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Towards Effective Long Video Understanding of Multimodal Large Language Models via One-shot Clip Retrieval](http://arxiv.org/abs/2512.08410v2)
  来源：arXiv | 日期：2025-12-09 | 相关度：6.8 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Due to excessive memory overhead, most Multimodal Large Language Models (MLLMs) can only process videos of limited frames. In this paper, we propose an effective and efficient paradigm to remedy this shortcoming, termed ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SUPERGLASSES: Benchmarking Vision Language Models as Intelligent Agents for AI Smart Glasses](http://arxiv.org/abs/2602.22683v2)
  来源：arXiv | 日期：2026-02-26 | 相关度：6.8 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：The rapid advancement of AI-powered smart glasses-one of the hottest wearable devices-has unlocked new frontiers for multimodal interaction, with Visual Question Answering (VQA) over external knowledge sources emerging a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Causal Prediction of TP53 Variant Pathogenicity Using a Perturbation-Informed Protein Language Model.](https://pubmed.ncbi.nlm.nih.gov/41955512/)
  来源：PubMed | 日期：2026-04-09 | 相关度：10.0 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：准确预测变异的功能影响对于理解人类疾病（特别是 TP53 等癌症相关基因）至关重要。尽管高通量突变分析提升了变异效应预测（VEP）能力，但通用型模型在错义突变分类上仍存在局限。本研究开发了 CaVepP53，这是一种针对 TP53 特化的预测模型，通过扰动实验变异数据对蛋白质语言模型（PLM）进行微调。该模型通过计算野生型与突变体嵌入向量之间的欧几里得距离，并结合逻辑变换推导置信度评分，实现对突变致病性的量化分类。基准测试表明，CaVe...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [STAnalyzer: Transparent Spatial Transcriptomics Analysis via an Agentic Architecture](https://www.biorxiv.org/content/10.64898/2026.04.06.716827v1)
  来源：bioRxiv | 日期：2026-04-09 | 相关度：8.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Spatial transcriptomics enables high resolution profiling of gene expression within spatial contexts, yet its potential is often hindered by fragmented toolchains, intricate parameters, and cognitive bottlenecks of inter...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ViralMap: Predicting Features in Viral Proteins from Primary Sequence](https://www.biorxiv.org/content/10.64898/2026.04.07.716565v1)
  来源：bioRxiv | 日期：2026-04-09 | 相关度：7.65 | 新颖度：0.75
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Modern viral vaccines are designed to elicit an immune response against viral proteins that mediate infection, making those proteins important targets for characterization and engineering. To improve vaccine efficacy, th...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Generative design of intrinsically disordered protein regions with IDiom](https://www.biorxiv.org/content/10.64898/2026.04.10.717777v1)
  来源：bioRxiv | 日期：2026-04-11 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Intrinsically disordered protein regions are ubiquitous across all kingdoms of life. These structurally heterogeneous regions play central roles in cellular processes such as transcriptional regulation, cellular signalin...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Towards a Universal Foundation Model for Protein Dynamics: A Multi-Chain Tree-Structured Framework with Transformer Propagators](http://arxiv.org/abs/2502.05909v2)
  来源：arXiv | 日期：2025-02-09 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Simulating large-scale protein dynamics using traditional all-atom molecular dynamics (MD) remains computationally prohibitive. We present a unified, universal framework for coarse-grained molecular dynamics (CG-MD) that...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [WildAlert: A Real-Time, AI-Driven Early Warning System for Wildlife Health and Ecological Threat Detection](https://www.biorxiv.org/content/10.64898/2026.04.07.716505v1)
  来源：bioRxiv | 日期：2026-04-10 | 相关度：9.2 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent, application_monitoring
  中文摘要：Emerging infections and environmental disruptions increasingly threaten wildlife and ecosystem health. Free-ranging wildlife often serve as early indicators of ecological instability, making timely detection of morbidity...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Detecting RAG Advertisements Across Advertising Styles](http://arxiv.org/abs/2603.04925v2)
  来源：arXiv | 日期：2026-03-05 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) enable a new form of advertising for retrieval-augmented generation (RAG) systems in which organic responses are blended with contextually relevant ads. The prospect of such "generated native...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions](http://arxiv.org/abs/2604.08304v1)
  来源：arXiv | 日期：2026-04-09 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) significantly enhances large language models (LLMs) but introduces novel security risks through external knowledge access. While existing studies cover various RAG vulnerabilities, th...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Automated Extraction and Meta-Analysis of a Century of Motor-Unit Research with NeuromechaniX](https://www.biorxiv.org/content/10.64898/2026.04.08.717204v1)
  来源：bioRxiv | 日期：2026-04-10 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：针对人类运动单位和肌电图（EMG）长达一个世纪（1925-2025年）的科学文献，手动进行研究合成已无法实现。本研究推出了 NeuromechaniX，一个用于此类文献自动化提取和元分析的领域专用平台。其核心组件 MUscraper 是一个大语言模型（LLM）流水线，从约 2,000 篇关于人类肢体肌肉的出版物中提取了约 200 个结构化元数据字段，涵盖参与者人口统计、EMG 采集参数、肌肉识别、任务协议、分解方法和运动单位结果等 17...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Title: Multimodal profiling reveals Mycobacterium tuberculosis restricts lung mitochondrial immunometabolism to promote pathogenesis](https://www.biorxiv.org/content/10.64898/2026.04.07.717012v1)
  来源：bioRxiv | 日期：2026-04-10 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：结核分枝杆菌（Mtb）感染早期肺部免疫反应的塑造机制尚不明确。本研究利用高维流式细胞术、单细胞转录组学和非靶向代谢组学，定义了小鼠气溶胶感染 Mtb 后产生保护性与致病性结果前的早期肺部免疫环境。研究发现，Mtb 诱导肺部持续糖酵解，同时限制氧化磷酸化（OXPHOS）并损害线粒体，该过程部分通过 Mtb 丝氨酸蛋白酶 Hip1 实现，导致能量输出降低及巨噬细胞与 T 细胞相互作用受损，从而促进致病性免疫。相反，早期肺部线粒体 OXPHO...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HyperMem: Hypergraph Memory for Long-Term Conversations](http://arxiv.org/abs/2604.08256v1)
  来源：arXiv | 日期：2026-04-09 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：长期记忆对于对话智能体在长对话中保持连贯性、跟踪持久任务和提供个性化交互至关重要。然而，现有的检索增强生成（RAG）和基于图的记忆方法主要依赖二元成对关系，难以捕捉多个元素之间的联合依赖等高阶关联，导致检索内容碎片化。为此，本研究提出了 HyperMem，一种基于超图的分层记忆架构，利用超边显式建模此类高阶关联。HyperMem 将记忆结构化为主题、情节和事实三个层级，并通过超边将相关情节及其事实进行分组，将分散的内容统一为连贯的单元。...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ReRec: Reasoning-Augmented LLM-based Recommendation Assistant via Reinforcement Fine-tuning](http://arxiv.org/abs/2604.07851v1)
  来源：arXiv | 日期：2026-04-09 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：随着大语言模型（LLM）的兴起，开发能够处理复杂查询并提供个性化、推理驱动建议的智能推荐助手需求日益增长。尽管基于 LLM 的推荐系统展现出潜力，但在多步推理方面仍面临挑战。为此，我们提出了 ReRec，一种旨在提升 LLM 在复杂推荐任务中推理能力的强化微调（RFT）框架。该框架包含三个核心组件：(1) 双图增强奖励塑造，整合了 NDCG@K 等推荐指标以及查询对齐和偏好对齐分数，为 LLM 优化提供细粒度奖励信号；(2) 推理感知优...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [From Binary Groundedness to Support Relations: Towards a Reader-Centred Taxonomy for Comprehension of AI Output](http://arxiv.org/abs/2604.08082v1)
  来源：arXiv | 日期：2026-04-09 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Generative AI tools often answer questions using source documents, e.g., through retrieval augmented generation. Current groundedness and hallucination evaluations largely frame the relationship between an answer and its...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Structure-Based and Stability-Validated Prioritization of BACE1 Inhibitors Integrating Meta-Ensemble QSAR and Molecular Dynamics](https://www.biorxiv.org/content/10.64898/2026.04.07.716920v1)
  来源：bioRxiv | 日期：2026-04-10 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Alzheimers disease remains an unmet therapeutic challenge, and no {beta}-secretase (BACE1) inhibitor has achieved clinical approval. A major limitation of prior discovery efforts is reliance on single-parameter optimizat...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Learning to Search: A Decision-Based Agent for Knowledge-Based Visual Question Answering](http://arxiv.org/abs/2604.07146v2)
  来源：arXiv | 日期：2026-04-08 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：知识库视觉问答（KB-VQA）要求视觉语言模型在理解图像的同时利用外部知识，特别是针对稀有实体和长尾事实。现有的检索增强生成（RAG）方法多采用固定的顺序流水线（检索、过滤、回答），难以适应多样化的提问，且检索与推理分离，导致模型无法自主决定搜索时机、优化查询或停止搜索，造成检索证据与问题匹配度差。为解决此问题，本研究将 KB-VQA 重新定义为搜索智能体问题，并将求解过程建模为多步决策程序。在每一步中，智能体根据当前信息状态从“回答”...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Quantifying Scientific Consensus in Biomedical Hypotheses via LLM-Assisted Literature Screening](https://www.biorxiv.org/content/10.64898/2026.04.06.716861v1)
  来源：bioRxiv | 日期：2026-04-09 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：系统综述在生物医学研究中是一项劳动密集型任务。虽然利用检索增强生成（RAG）技术的大语言模型（LLM）提高了信息获取效率，但生物系统固有的复杂性（如高上下文依赖和数据冲突）仍是导致 LLM 产生幻觉的主要原因，限制了证据合成的精度。为解决这些局限性，我们提出了一种自动化框架，旨在详尽识别目标文献集中的支持性与矛盾性证据。该系统不依赖模型的预训练知识，而是要求 LLM 逐篇审阅论文，以确定其与特定研究假设的一致性。通过评估语义上下文，该框...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Guaranteeing Knowledge Integration with Joint Decoding for Retrieval-Augmented Generation](http://arxiv.org/abs/2604.08046v1)
  来源：arXiv | 日期：2026-04-09 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：检索增强生成（RAG）通过引入外部知识显著提升了大语言模型（LLM）的性能。然而，现有研究多关注检索质量，忽略了关键的“集成瓶颈”：即当检索到的文档与模型内部参数化知识发生冲突时，LLM 往往无法有效利用外部证据。本文提出 GuarantRAG 框架，旨在显式解耦推理过程与证据集成。该框架首先仅依据参数化知识生成“内部答案”（Inner-Answer）以捕捉模型的推理逻辑；随后，利用新型对比直接偏好优化（DPO）目标生成“参考答案”（R...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Modification-aware AI enables terminal chemical modifications for peptide design and discovers potent antimicrobials](https://www.biorxiv.org/content/10.64898/2026.04.09.717597v1)
  来源：bioRxiv | 日期：2026-04-10 | 相关度：3.35 | 新颖度：0.5
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：针对日益严重的抗生素耐药性（AMR）威胁，本研究开发了名为 Termini 的生成式机器学习框架，用于系统化识别高效抗菌肽（AMPs）。该框架集成了肽序列生成、分类和回归模块，其核心创新在于显式设计了肽链的 N 端和 C 端化学修饰，并结合了针对 15 种细菌物种的预测建模。实验验证阶段涵盖了 11 种病原菌，是目前同类研究中测试光谱最广的工作。研究团队合成并测试了 120 种肽（包含 60 个独特氨基酸序列），对比了有无末端修饰的效果...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Co-design for Trustworthy AI: An Interpretable and Explainable Tool for Type 2 Diabetes Prediction Using Genomic Polygenic Risk Scores](http://arxiv.org/abs/2604.08217v1)
  来源：arXiv | 日期：2026-04-09 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：多基因风险评分（PRS）是量化复杂性状和临床疾病遗传易感性的重要方法，已广泛应用于肥胖、癌症和2型糖尿病（T2DM）的风险识别。然而，PRS目前面临缺乏可解释性的局限。为解决此问题，首尔大学研究团队开发了可视化工具eXplainable PRS (XPRS)。该工具利用Shapley Additive Explanations (SHAP) 算法将PRS分解为基因级和单核苷酸多态性（SNP）贡献得分，为驱动个体风险的遗传因素提供细粒度见...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Rag Performance Prediction for Question Answering](http://arxiv.org/abs/2604.07985v1)
  来源：arXiv | 日期：2026-04-09 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：本研究针对问答（QA）任务中，预测使用检索增强生成（RAG）相对于不使用 RAG 所能获得的性能增益这一课题进行了深入探讨。研究团队评估了多种最初为即时检索（ad hoc retrieval）设计的检索前（pre-retrieval）和检索后（post-retrieval）预测指标。此外，研究还考察了若干生成后（post-generation）预测指标，并提出了一种在该领域尚属首创的新型预测方法。实验结果表明，最有效的预测方案是一种新型...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AnomalyAgent: Agentic Industrial Anomaly Synthesis via Tool-Augmented Reinforcement Learning](http://arxiv.org/abs/2604.07900v1)
  来源：arXiv | 日期：2026-04-09 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：工业异常生成是缓解异常检测任务中数据稀缺问题的关键。现有方法多依赖单步生成机制，缺乏复杂推理与迭代优化能力，难以生成具备高语义真实性的异常样本。本文提出 AnomalyAgent，一种具备自我反思、知识检索和迭代改进能力的异常合成智能体。该智能体配备了提示词生成（PG）、图像生成（IG）、质量评估（QE）、知识检索（KR）和掩码生成（MG）五种工具，实现了闭环优化。为提升决策与反思能力，研究者利用真实异常图像构建了结构化轨迹，并设计了监...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 其他

- [Efficient Federated Search for Retrieval-Augmented Generation using Lightweight Routing](http://arxiv.org/abs/2502.19280v2)
  来源：arXiv | 日期：2025-02-26 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：大语言模型（LLMs）在各领域表现出色，但仍存在幻觉和不一致性问题。检索增强生成（RAG）通过引入外部检索的相关文档来缓解这些问题。在许多现实场景中，相关知识往往分散在不同组织或机构中，因此需要联邦搜索机制在不集中数据的情况下聚合异构数据源的结果。本文提出了 RAGRoute，一种用于 RAG 系统联邦搜索的轻量级路由机制。该机制利用神经分类器在查询时动态选择相关数据源，避免了无差别的全量查询。实验表明，RAGRoute 在三个基准测试...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。
