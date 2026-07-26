# 每日论文监控日报 (2026-07-26)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 20 篇新论文。

## 抓取状态

- arXiv：成功，命中 9 篇
- PubMed：成功，命中 43 篇
- bioRxiv：成功，命中 8 篇
- medRxiv：成功，命中 9 篇

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [Small but Specialized: A Domain-Adapted Retrieval-Augmented LLM Outperforms Frontier Generalists in Pediatric and Adolescent Gynecology](https://www.medrxiv.org/content/10.64898/2026.07.22.26358688v1)
  来源：medRxiv | 日期：2026-07-24 | 相关度：7.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Background. Pediatric and adolescent gynecology (PAG) is a highly specialized field where timely, accurate clinical guidance can prevent serious harm to a vulnerable population, yet most general-purpose large language mo...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SleepGPT: A Sleep Stage Language Model for Efficient Sleep Assessment](https://www.medrxiv.org/content/10.1101/2024.10.26.24316166v5)
  来源：medRxiv | 日期：2026-07-23 | 相关度：7.15 | 新颖度：2.25
  匹配主题：foundation_model_agent
  中文摘要：Background: Accurate and scalable sleep assessment is essential for the diagnosis of sleep disorders and the advancement of personalized sleep medicine. Current clinical practice relies predominantly on in-laboratory pol...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A unified 12-lead ECG-language model for interpretation and clinical-endpoint prediction](https://www.medrxiv.org/content/10.64898/2026.07.22.26358591v1)
  来源：medRxiv | 日期：2026-07-24 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Automated electrocardiogram (ECG) interpretation has advanced, yet most systems remain narrow classifiers that emit fixed labels rather than the narratives or endpoint-specific answers clinicians need. Generative approac...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PennySynth: RAG-Driven Data Synthesis for Automated Quantum Code Generation](http://arxiv.org/abs/2605.25572v2)
  来源：arXiv | 日期：2026-05-25 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：The growing complexity of quantum programming frameworks has exposed a critical limitation in existing large language model (LLM)-based code assistants: general-purpose models hallucinate PennyLane-specific gate names, m...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [GoMA-DTA: A Gene Ontology-Guided Multimodal Attention Fusion Model for Drug-Target Affinity Prediction.](https://pubmed.ncbi.nlm.nih.gov/42497056/)
  来源：PubMed | 日期：2026-07-24 | 相关度：7.1 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Accurate prediction of drug-target affinity (DTA) is essential for accelerating drug discovery. Although pretrained protein language models have achieved significant progress, existing methods predominantly focus on bott...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A germline shortcut in protein language model retrieval of adaptive immune receptors](https://www.biorxiv.org/content/10.64898/2026.07.21.739963v1)
  来源：bioRxiv | 日期：2026-07-23 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Protein language models (PLMs) are increasingly used to represent adaptive immune receptors; however, their advantages over classical alignment-based methods remain unclear. We benchmarked the ESM2 family, ESM-C, antibod...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Clinical Impact, Diagnostic Performance, and Prognostic Implications of Plasma Metagenomic Next-Generation Sequencing in Solid Organ Transplant Recipients](https://www.medrxiv.org/content/10.64898/2026.07.02.26357172v2)
  来源：medRxiv | 日期：2026-07-24 | 相关度：8.1 | 新颖度：0.75
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Background: Plasma metagenomic next-generation sequencing (mNGS) may detect pathogens in solid organ transplant (SOT) recipients, but optimal patient selection and result interpretation remain uncertain. Methods: We stud...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Efficacy of a Large Language Model Data Extraction System in Evidence Reviews for Emerging Infectious Diseases: A Randomized Crossover Trial.](https://pubmed.ncbi.nlm.nih.gov/42494833/)
  来源：PubMed | 日期：2026-07-01 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Rapid evidence synthesis during emerging infectious and re-emerging disease outbreaks is critical, yet traditional systematic reviews rarely meet urgent timelines. Large language models (LLMs) may accelerate evidence syn...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Initial-Visit Specialty Triage in Rare Diseases Using Large Language Models: Retrospective Benchmarking Study.](https://pubmed.ncbi.nlm.nih.gov/42490550/)
  来源：PubMed | 日期：2026-07-23 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：罕见病的首诊分诊是早期诊断中常被忽视的关键环节。由于患者常表现出重叠、多系统且不典型的症状，首诊专科选择极具挑战。本研究旨在评估大语言模型（LLMs）在罕见病首诊分诊中的准确性、响应时间和一致性，并与注册护士及非医学背景人员进行对比。研究采用回顾性基准测试，使用了包括RareBench和面部表型-基因-疾病数据集在内的5个罕见病数据集。评估涵盖14种LLM，每例病例独立运行5次。结果显示，模型准确率在0.4378至0.7141之间。Cl...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Risk Perception to Behavior Large Language Models-Based Simulation of Pandemic Prevention Behaviors](http://arxiv.org/abs/2601.03552v2)
  来源：arXiv | 日期：2026-01-07 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：针对新发传染病爆发初期个体防疫行为难以预测且实证数据稀缺的挑战，本研究开发了一个基于大语言模型（LLM）的防疫行为模拟框架。该框架耦合了两个核心模块：一是用于预测特定外部背景下行为强度的静态模块，二是随时间更新居民感知风险并驱动行为演变的动态模块。模型通过第一人称视角的结构化提示工程实现，并利用北京居民的两轮调查数据（2020年12月和2021年8月）在零样本、少样本及跨背景迁移设置下进行了评估。通过Kolmogorov-Smirnov...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EcoXAI: Autonomous Agentic Ecosystem for Explainable Artificial Intelligence and Biomedical Discovery](https://www.biorxiv.org/content/10.64898/2026.07.08.737358v2)
  来源：bioRxiv | 日期：2026-07-23 | 相关度：3.1 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：随着生物医学数据集和知识图谱在规模与复杂性上的增长，从海量数据中提取可操作见解成为研究瓶颈。EcoXAI 引入了一种模块化、可定制且容器化的多智能体（Multi-agent）系统，旨在利用智能体编排和循环工程的最新进展，同时解决 AI 幻觉和工作流碎片化问题。该系统将分析过程结构化为明确的流水线执行阶段，降低了临床和转化研究人员的计算门槛。EcoXAI 采用执行驱动的自主框架取代了单一的 AI 文本界面，利用专门的生物信息学智能体提供基...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [GRADRAG: Cross-Component Prompt Adaptation for Coordinated Multi-Agent RAG](http://arxiv.org/abs/2607.21324v1)
  来源：arXiv | 日期：2026-07-23 | 相关度：2.1 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）系统日益采用多LLM智能体协作，但现有工作多孤立优化各组件，缺乏全链路协同。本文提出 GRADRAG 框架，旨在实现跨组件的提示词适配。该框架将 RAG 流水线建模为计算图，通过传播结构化评估反馈来更新上游智能体。具体而言，评估器（Evaluator）对下游生成的回答及支持证据进行批判性分析，生成可操作的反馈，由提示词优化器（Prompt Optimizer）据此迭代更新检索器、图构建器和回答器等自适应智能体；同时...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AttriMem: Attribution-Guided Process Feedback for Agent Memory Learning](http://arxiv.org/abs/2607.21106v1)
  来源：arXiv | 日期：2026-07-23 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：有效的记忆对大语言模型（LLM）智能体至关重要，但其构建仍具挑战。记忆构建策略决定了在交互积累过程中提取、存储、更新、压缩或丢弃哪些信息。启发式方法依赖主观且特定于任务的规则，导致其与下游目标失配并限制了跨任务适应性。相比之下，基于强化学习（RL）的方法虽能从反馈中学习，但主要利用粗粒度的结果或模块级奖励，难以识别支撑最终答案的中间记忆内容，存在信用分配瓶颈。由于中间决策缺乏唯一真值，且信用随推理轨迹变化，构建过程反馈极难。为此，我们提...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [DB-ATRG: The Density and BI-RADS-Aware Triage and Automatic Report Generation System for Mammography](https://www.medrxiv.org/content/10.64898/2026.07.22.26358655v1)
  来源：medRxiv | 日期：2026-07-23 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：针对乳腺癌筛查量增加导致的放射科医生短缺及传统先来先服务（FIFO）队列无法优先处理紧急病例的问题，本研究提出了DB-ATRG框架。该框架利用DMID数据集，通过QLoRA技术微调了拥有40亿参数的MedGemma 1.5视觉语言模型，实现了诊断文本的自动生成与基于风险的病例分诊。DB-ATRG包含双阶段分诊算法：首先标记极高腺体密度（ACR D类）病例以进行补充筛查，随后利用累积紧急评分对剩余病例动态排序。实验结果显示，DB-ATRG...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [TeaRAG: A Token-Efficient Agentic Retrieval-Augmented Generation Framework](http://arxiv.org/abs/2511.05385v2)
  来源：arXiv | 日期：2025-11-07 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：检索增强生成（RAG）利用外部知识提升大语言模型（LLM）的可靠性，而智能体化 RAG（Agentic RAG）通过多轮检索与推理增强了处理复杂查询的灵活性，但常面临搜索和推理过程带来的巨大 Token 开销。为此，本文提出 TeaRAG 框架，旨在同时压缩检索内容与推理步骤。在内容压缩方面，TeaRAG 将块状语义检索与基于简洁三元组的图检索相结合，利用语义相似性和共现关系构建知识关联图，并应用个性化 PageRank（PPR）算法筛...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Enhancing Title and Abstract Priority Screening Through EdRoSi AI Pipeline.](https://www.medrxiv.org/content/10.64898/2026.06.26.26356718v2)
  来源：medRxiv | 日期：2026-07-23 | 相关度：2.1 | 新颖度：1.75
  匹配主题：未命中具体主题
  中文摘要：系统综述中证据的详尽识别至关重要，但题目和摘要筛选环节耗时耗力。优先筛选（Priority screening）作为一种主动学习方法，通过相关性排序减少工作量，其效率通常以100%召回率下的工作节省量（WSS@100%）来衡量。尽管现有模型在基准数据集上表现良好，但在处理某些挑战性数据集时，检索最后几个稀有的相关文献仍存在困难。本研究利用SYNERGY基准数据集证明，ASReview LAB v.2中的ELAS_h3模型在检索最后少数相...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GeneKnow: An auditable AI framework for source-grounded biological evidence synthesis](https://www.biorxiv.org/content/10.64898/2026.05.28.728511v2)
  来源：bioRxiv | 日期：2026-07-23 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：生物功能具有高度的背景依赖性，但在特定细胞类型、疾病或扰动下综合基因功能的证据仍是一项劳动密集型工作。本文提出了 GeneKnow，这是一个用于源头溯源生物证据合成的可审计人工智能（AI）框架。GeneKnow 将关键证据操作（包括文献检索、段落选择、出处追踪和参考文献构建）与仅限于语义分析和文献合成的生成步骤分离。该框架支持多论文发现和单论文检查，同时保留从合成结论到源段落的链接，从而生成可靠的合成内容，避免虚假引用并最大限度减少幻觉...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Coarse-to-Fine Long-term Interest Modeling for Generative Recommendation](http://arxiv.org/abs/2602.05663v2)
  来源：arXiv | 日期：2026-02-05 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：利用长期用户行为模式是提升现代推荐系统准确性的关键。尽管生成式推荐系统已成为一种变革性范式，但在有效建模超长历史序列方面仍面临挑战。为此，我们提出了 GLASS 框架，通过 SID-Tier 和语义搜索将长期用户兴趣整合到生成过程中。首先，SID-Tier 模块将长期交互映射为统一的兴趣向量，以增强初始语义 ID（SID）令牌的预测；与处理大规模物品空间的传统检索模型不同，该模块利用语义码本的紧凑性，结合用户长期历史与候选语义代码的交叉...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Artificial intelligence-based methods and applications in clinical and diagnostic microbiology: Current challenges and future perspectives.](https://pubmed.ncbi.nlm.nih.gov/42492779/)
  来源：PubMed | 日期：2026-07-23 | 相关度：4.7 | 新颖度：0.25
  匹配主题：pathogenomics
  中文摘要：微生物实验室在传染病诊断和管理中发挥着关键作用，而人工智能（AI）技术，特别是机器学习（ML）和深度学习（DL），正成为减少人力工作量和缩短诊断耗时的重要手段。本研究综述了AI在微生物实验室诊断中的显著贡献，指出该技术能显著提升分子生物学方法、基因测序及微生物元分析的分析速度与准确性。除临床诊断外，AI已广泛应用于基因组学、宏基因组学、抗生素耐药性（AMR）预测以及药物和疫苗研发，实现了更全面的数据驱动分析。本文全面评估了当前AI在微生...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [AI-Driven Multi-Omics Integrated Applications Using Diverse Neural Networks for Breast Cancer Diagnostic Screening and Biomarker Discovery.](https://pubmed.ncbi.nlm.nih.gov/42489168/)
  来源：PubMed | 日期：2026-07-23 | 相关度：3.75 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：乳腺癌（BC）是全球女性中最普遍且具有高度复杂性和异质性的恶性肿瘤，其诊断、预后和治疗的挑战限制了临床疗效。基于组学的技术通过分子谱分析和临床分析在乳腺癌诊断中受到广泛关注。整合代谢组学、蛋白质组学、转录组学和基因组学，通过高通量分子分型为个性化诊疗提供了多维方法。人工智能（AI）的兴起通过多模态数据整合支持了更准确的早期诊断。深度学习（DL）和机器学习（ML）已广泛用于肿瘤分级、组织病理学分类、分子分型、影像诊断和预后预测。本综述总结...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
