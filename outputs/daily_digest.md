# 每日论文监控日报 (2026-08-10)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 26 篇新论文。

## 抓取状态

- arXiv：成功，命中 18 篇
- PubMed：成功，命中 22 篇
- bioRxiv：成功，命中 16 篇
- medRxiv：成功，命中 3 篇

## 最值得看

### Foundation Model / Agent

- [AI semantics for biomedical data integration](https://www.biorxiv.org/content/10.64898/2026.08.03.742514v1)
  来源：bioRxiv | 日期：2026-08-07 | 相关度：7.9 | 新颖度：6.2
  匹配主题：foundation_model_agent
  中文摘要：Researchers increasingly need to explore hypotheses that span multimodal data across different scales, organisms, and domains. In practice, this requires connecting knowledge across fragmented databases with incompatible...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Assessing Computational Models for Pharmacogenomic Variant Interpretation](https://www.biorxiv.org/content/10.64898/2026.08.03.742561v1)
  来源：bioRxiv | 日期：2026-08-09 | 相关度：10.0 | 新颖度：5.75
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Accurately predicting the effects of pharmacogenomic variants is essential for the development of personalized therapeutic strategies, as genetic variability can influence drug response differently across patients. Here,...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [Does More Retrieved Evidence Help Visual Retrieval-Augmented Generation with Diffusion Language Models?](http://arxiv.org/abs/2608.07006v1)
  来源：arXiv | 日期：2026-08-07 | 相关度：6.8 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Visual retrieval-augmented generation (RAG) commonly expands the retrieved evidence set to improve answer-page coverage, implicitly assuming that all available evidence should be passed to the generator. We show that thi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Mind the Gap: A Dual Knowledge Graph Framework for Unified Multi-task User Intent Inference](http://arxiv.org/abs/2608.06752v1)
  来源：arXiv | 日期：2026-08-07 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：This paper proposes DKG-MTI, a dual knowledge graph framework for unified multi-task user intent inference from online travel reviews. Existing approaches often rely on hierarchical pipelines that suffer from error propa...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Science Edge Evaluation: SEE the Missing Step Toward Real Scientific Discovery](http://arxiv.org/abs/2608.06931v1)
  来源：arXiv | 日期：2026-08-07 | 相关度：6.1 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly involved in scientific discovery, yet it remains unclear whether they can support complex real laboratory science. Here we introduce Science Edge Evaluation (SEE), a multimod...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Evaluating Lightweight and Full Fine-Tuning Strategies Against Classical Machine Learning for Protein Function Prediction](https://www.biorxiv.org/content/10.64898/2026.08.02.737389v1)
  来源：bioRxiv | 日期：2026-08-07 | 相关度：5.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Motivation Protein language models (PLMs) have emerged as powerful tools for sequence-based prediction of protein function, yet systematic benchmarks comparing frozen embeddings, fine-tuning strategies like Low-Rank Adap...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Coevolution-informed Bayesian optimization for sample-efficient protein design](https://www.biorxiv.org/content/10.64898/2026.08.06.743295v1)
  来源：bioRxiv | 日期：2026-08-07 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Protein engineering is limited less by generating variants than by the cost of evaluating them, so designing under a tight budget demands sequence features that let a model learn fitness from very few examples. We introd...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Index SLM Technical Report](http://arxiv.org/abs/2607.09885v2)
  来源：arXiv | 日期：2026-07-10 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：We present Index-1.9B, a series of open small language models developed at Bilibili. The series comprises four models: Index-1.9B-Base, a foundation model with 1.9 billion non-embedding parameters pre-trained on 2.8 tril...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Artificial Intelligence-Driven Natural Product Drug Discovery: From Computational Genome Mining to Clinical Translation.](https://pubmed.ncbi.nlm.nih.gov/42565648/)
  来源：PubMed | 日期：2026-08-07 | 相关度：6.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Natural products (NPs) have historically yielded numerous therapeutic agents, yet their integration into modern drug discovery has been constrained by chemical complexity, low abundance, laborious dereplication, and limi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Safety First: Input Screening for Protein Design Tools](https://www.biorxiv.org/content/10.64898/2026.08.04.740855v1)
  来源：bioRxiv | 日期：2026-08-07 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：As biological AI models become more powerful, practical biosecurity approaches are needed to support beneficial applications while reducing misuse risks. Sequence-similarity-based screening approaches are no longer adequ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Taxonomy-Driven Analysis of Open-Source AI Risk Mitigation Tools](http://arxiv.org/abs/2608.07446v1)
  来源：arXiv | 日期：2026-08-07 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Rapid adoption of large language models (LLMs) in enterprise settings has introduced operational, security, and governance risks. As generative AI applications move from pilot to production, manual harm identification an...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Genotypic Triggers: Exposing Pharmacogenomic Blind Spots via Host-Specific Backdoors in Generative Antimicrobial Peptide Models](http://arxiv.org/abs/2608.06779v1)
  来源：arXiv | 日期：2026-08-07 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have accelerated drug discovery, particularly in the automated design of antimicrobial peptides (AMPs). However, current validation pipelines for peptide generation models overlook historical...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Skill-RAG: Failure-State-Aware Retrieval Augmentation via Hidden-State Probing and Skill Routing](http://arxiv.org/abs/2604.15771v4)
  来源：arXiv | 日期：2026-04-17 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：检索增强生成（RAG）已成为大型语言模型利用外部知识的基础范式。尽管自适应检索机制提高了效率，但现有方法仅将检索后的失败视为重试信号而非诊断信号，未能解决查询与证据空间失配的结构性原因。本研究观察到，很大一部分持续性的检索失败并非源于缺乏相关证据，而是源于查询与证据空间之间的对齐间隙。为此，我们提出了 Skill-RAG，这是一个失败感知的 RAG 框架，它结合了轻量级隐藏状态探测器（hidden-state prober）和基于提示的...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [When Context Bites: Detecting RAG Poisoning via Document-Level Attention Collapse](http://arxiv.org/abs/2608.06947v1)
  来源：arXiv | 日期：2026-08-07 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：检索增强生成（RAG）是增强大语言模型能力的关键技术，但其日益受到投毒攻击的威胁，即攻击者通过注入对抗性文档来操纵生成器的输出。现有的检测方法主要依赖困惑度（perplexity）和一致性检查等输出端信号。然而，本研究分析表明，蓄意攻击往往会诱导“虚假置信度”，导致中毒输出的困惑度甚至低于良性输出，使得基于不确定性的检测方法失效。为解决这一挑战，研究者探索了生成器的内部动力学，并发现了一种名为“注意力坍缩”（Attention Coll...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [Interventional Embolization Under Multifactorial Coupling: Mechanisms of Embolic-Agent Distribution and Feasibility of Closed-Loop Automatic Injection.](https://pubmed.ncbi.nlm.nih.gov/42566076/)
  来源：PubMed | 日期：2026-08-07 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：本综述旨在综合当前关于栓塞剂分布机制的知识，并探讨闭环或半自动栓塞剂注射的工程原理与转化可行性。通过对实验、计算和临床研究的结构化检索，本文从生物医学工程角度分析了颗粒特性、注射参数、血流动力学、影像反馈及压力监测在栓塞过程中的证据，重点关注转运机制、传感模式和控制变量。研究发现，栓塞剂分布是由颗粒尺寸、形状、材料属性，以及注射速率、模式、导管配置和病变/器械引起的血流动力学改变共同耦合的结果。定量数字减影血管造影（qDSA 和 4D-...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Retrieval-Constrained Policy Optimization for Attack Technique Extraction from Cyber Threat Intelligence](http://arxiv.org/abs/2608.06778v1)
  来源：arXiv | 日期：2026-08-07 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：将网络威胁情报（CTI）文本映射到 MITRE ATT&CK 技术对于结构化威胁分析至关重要，但人工标注成本高且难以扩展。ATT&CK 分类法包含数百种攻击技术，且单段 CTI 文本可能涉及多种技术，使得准确且完整的提取具有挑战性。现有自动化方法存在局限：多标签分类器难以处理严重的类别不平衡和大标签空间，而基于大语言模型（LLM）的检索或微调方法通常优化 Token 级目标，将标注视为序列生成而非集合预测，缺乏对预测集合正确性和完整性的...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [SAGEO Arena: A Realistic Environment for Evaluating Search-Augmented Generative Engine Optimization](http://arxiv.org/abs/2602.12187v2)
  来源：arXiv | 日期：2026-02-12 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：搜索增强生成引擎（SAGE）已成为信息获取的新范式，通过结合大规模网络检索与生成能力提供综合答案，这促使了搜索增强生成引擎优化（SAGEO）的出现，旨在提升网页在 AI 生成回复中的可见性。然而，现有基准测试缺乏对优化策略的端到端评估，通常仅在预定义的候选文档上操作，忽略了生成前的检索和重排序阶段，且丢弃了真实网页中的结构化信息（如架构标记）。为此，本研究推出了 SAGEO Arena，这是一个用于阶段级 SAGEO 分析的真实且可重复...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Exact Adaptive Hybrid Retrieval Without Fixed Top-L Cutoffs](http://arxiv.org/abs/2608.07152v1)
  来源：arXiv | 日期：2026-08-07 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：现代检索增强生成（RAG）系统通常融合来自稠密和稀疏检索器的固定 Top-L 结果，将后续贡献视为零。然而，截断融合并不等同于全列表融合，未读取的跨列表排名可能改变 Top-K 的成员或顺序，且固定深度在查询变化或语料库更新时无法可靠迁移。本文提出精确自适应混合检索（EAHR），将全列表加权倒数排名融合（RRF）定义的有序 Top-K 作为检索目标，将通道深度视为特定请求的执行状态。EAHR 利用每向量标量量化（PVS）和倒排块最大值（...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Rhetorical-Role-Aware Retrieval-Augmented Generation for Legal Question Answering over Indian Supreme Court Judgments](http://arxiv.org/abs/2608.06828v1)
  来源：arXiv | 日期：2026-08-07 | 相关度：2.1 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：本研究提出了一种专门针对法律领域的检索增强生成（RAG）框架，旨在实现对印度最高法院判决书的交互式检索与推理。该方案通过增强型RAG架构，整合了基于修辞的角色分块（rhetorically based chunking）、融合检索及交叉编码器重排序方法，显著提升了检索信息的相关性。为优化对话交互，框架利用聊天历史、查询分类与重写技术来精准捕捉连续查询中的用户意图。此外，研究还针对法律文档的结构特征（如孤立的法官姓名）进行了优化，以消除其...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Benchmarking single-cell foundation models in a zero-shot setting](https://www.biorxiv.org/content/10.64898/2026.08.03.739553v1)
  来源：bioRxiv | 日期：2026-08-07 | 相关度：1.7 | 新颖度：6.75
  匹配主题：未命中具体主题
  中文摘要：单细胞基础模型（Foundation Models）通过大规模转录组数据学习通用表征，旨在迁移至多种下游任务。本研究在零样本（zero-shot）设置下评估了 scGPT、SCimilarity、UCE 和 Transcriptformer 四种模型，涵盖细胞类型注释、人类数据整合、跨物种数据整合及蛋白质表达预测四项任务。研究利用多个公共单细胞数据集，将模型生成的嵌入向量与传统机器学习基准进行对比，并采用分类、整合及回归等指标进行评估。...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Precision periodontology in clinical practice: bridging omics and clinical decision-making.](https://pubmed.ncbi.nlm.nih.gov/42567900/)
  来源：PubMed | 日期：2026-08-08 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：精准牙周病学旨在将分子诊断、基因组学和先进成像技术整合至临床决策。尽管在微生物组特征、宿主遗传学和炎症生物标志物领域进展显著，但其临床转化仍受限。本研究通过检索2010-2025年间的PubMed、Scopus等数据库，评价了微生物组分析、遗传/表观遗传标记、宿主反应标志物（如aMMP-8）及三维成像（CBCT）的证据，并提出了一个连接诊断输出与治疗行动的决策支持框架。研究发现：微生物检测适应症较窄；单SNP基因分型临床效用低；aMMP...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [INTRYGUE: Induction-Aware Entropy Gating for Reliable RAG Uncertainty Estimation](http://arxiv.org/abs/2603.21607v2)
  来源：arXiv | 日期：2026-03-23 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）虽提升了大型语言模型（LLM）的事实可靠性，但仍无法完全消除幻觉，因此鲁棒的不确定性量化（UQ）至关重要。本文揭示了标准基于熵的 UQ 方法在 RAG 场景中失效的机制悖论：上下文利用中存在一种内在的“拉锯战”，即诱导头（induction heads）在通过复制正确答案促进可靠响应的同时，会附带触发预先存在的“熵神经元”。这种相互作用导致预测熵虚高，使模型对准确输出发出错误的不确定性信号。为此，我们提出了 INT...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Surface-enhanced Raman scattering for the diagnosis of respiratory viruses.](https://pubmed.ncbi.nlm.nih.gov/42565721/)
  来源：PubMed | 日期：2026-08-07 | 相关度：5.75 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent, application_monitoring
  中文摘要：Surface-enhanced Raman scattering (SERS) has become a promising tool for rapid and sensitive respiratory pathogen detection. However, relevant reviews remain scarce. This review systematically summarizes the evolution of...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [The Illusion of Understanding: A Randomized Controlled Trial of LLM-Generated Lay Summaries of Brain MRI Reports](https://www.medrxiv.org/content/10.64898/2026.08.05.26359773v1)
  来源：medRxiv | 日期：2026-08-07 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Background: Large language models have been proposed to improve patient comprehension of radiology reports. However, whether they improve objective understanding remains unproven. Purpose: To evaluate the effect of appen...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial Intelligence-Driven Multiomics Integration in Lung Cancer: From Data Convergence to Precision Phenomics.](https://pubmed.ncbi.nlm.nih.gov/42566262/)
  来源：PubMed | 日期：2026-08-07 | 相关度：3.75 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：肺癌因其广泛的分子异质性、晚期诊断和治疗耐药性，仍是全球癌症死亡的主要原因。高通量组学技术的进步实现了对肿瘤在基因组、表观基因组、转录组、蛋白质组和代谢组等多生物层面的全面表征。然而，单组学分析仅能提供碎片化的肿瘤生物学见解，凸显了整合多组学方法的需求。人工智能（AI），特别是机器学习和深度学习，已成为整合异构数据集并揭示生物学和临床相关模式的强大工具。本综述总结了AI驱动的肺癌多组学整合的最新进展，重点介绍了其在分子分型、生物标志物发...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [CoinRAG: Contextualized Information Nugget KV Cache Reuse for Long-Context RAG](http://arxiv.org/abs/2608.07458v1)
  来源：arXiv | 日期：2026-08-07 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：最近的检索增强生成（RAG）优化研究利用块级 KV 缓存复用来避免处理长检索上下文，以提高效率，但粗粒度块中仍存在显著的信息冗余和噪声。本文提出了 CoinRAG（长上下文 RAG 的上下文信息金块 KV 缓存复用），旨在低预填充延迟约束下优化帕累托前沿并最大化准确率。CoinRAG 组合式地复用离线计算的细粒度“金块（nugget）”缓存，以更具语义相关性且紧凑的方式高效形成上下文表示。具体而言，CoinRAG 放弃了全块编码，而是通...
  为什么值得看：CoinRAG: Contextualized Information Nugg 与你的主题有弱匹配，暂时保留作低优先级跟踪。
