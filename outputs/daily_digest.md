# 每日论文监控日报 (2026-04-05)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 24 篇新论文。

## 抓取状态

- arXiv：成功，命中 20 篇
- PubMed：成功，命中 19 篇
- bioRxiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='api.biorxiv.org', port=443): Read timed out. (read timeout=60)
- medRxiv：成功，命中 14 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [Citation Hallucination Determines Success: An Empirical Comparison of Six Medical AI Research Systems](https://www.medrxiv.org/content/10.64898/2026.04.02.26350091v1)
  来源：medRxiv | 日期：2026-04-04 | 相关度：7.55 | 新颖度：6.7
  匹配主题：foundation_model_agent
  中文摘要：Large language model (LLM) systems can now generate complete research manuscripts, yet their reliability in clinical medicine - where citation accuracy and reporting standards carry direct consequences - has not been sys...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 产品应用 / 监测落地

- [Extracting Social Determinants of Health from Electronic Health Records: Development and Comparison of Rule-Based and Large Language Model Methods](https://www.medrxiv.org/content/10.1101/2025.11.15.25339520v2)
  来源：medRxiv | 日期：2026-04-04 | 相关度：7.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Background Social determinants of health (SDoH) are critical drivers of health outcomes but are often under-documented in structured electronic health record (EHR) data. Instead, SDoH are more commonly recorded in unstru...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 可追踪

### Foundation Model / Agent

- [Med-ICE: Enhancing Factual Accuracy in Medical AI through Autonomous Multi-Agent Consensus](https://www.medrxiv.org/content/10.64898/2026.04.02.26350080v1)
  来源：medRxiv | 日期：2026-04-04 | 相关度：7.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：The integration of Large Language Models into high-stakes clinical workflows is critically hampered by their lack of verifiable reliability and tendency to generate hallucinations. This paper introduces Med-ICE, an auton...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Foundation Model for Intensive Care: Unlocking Generalization across Tasks and Domains at Scale](https://www.medrxiv.org/content/10.1101/2025.07.25.25331635v2)
  来源：medRxiv | 日期：2026-04-02 | 相关度：7.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：BACKGROUND Early recognition of physiological deterioration in critically ill patients enables timely intervention, yet much of the predictive information in routinely collected intensive care data remains underutilized....
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multi-Task Learning and Soft-Label Supervision for Psychosocial Burden Profiling in Cancer Peer-Support Text](https://www.medrxiv.org/content/10.64898/2026.04.03.26350034v1)
  来源：medRxiv | 日期：2026-04-04 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Objective: Online cancer peer-support text contains signals of psychosocial burden beyond emotional tone, including treatment burden, financial strain, uncertainty, and unmet support needs. We evaluated 2 modeling extens...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evaluating Large Language Models for Assessment of Psychosis Risk](https://www.medrxiv.org/content/10.64898/2026.04.02.26349960v1)
  来源：medRxiv | 日期：2026-04-04 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Psychosis prevention relies on early detection of individuals at clinical high risk for psychosis (CHR-P) remains limited, constraining preventive care. The effectiveness of the CHR-P state is constrained, in part due to...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 产品应用 / 监测落地

- [Enhancing Medical Knowledge in Large Language Models via Supervised Continued Pretraining on Clinical Notes](https://www.medrxiv.org/content/10.64898/2026.04.02.26350065v1)
  来源：medRxiv | 日期：2026-04-04 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Background: Large language models (LLMs) contain limited professional medical knowledge, as large-scale training on clinical text has not yet been possible due to restricted access. Objectives: To continue pre-training a...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Vision-language framework for multi-sequence brain magnetic resonance imaging](https://www.medrxiv.org/content/10.64898/2026.03.30.26349106v1)
  来源：medRxiv | 日期：2026-04-04 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Structural magnetic resonance imaging (MRI) is a cornerstone for diagnosing neurological disorders, yet automated interpretation of multi-sequence brain MRI remains limited by challenges in cross sequence reasoning and p...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Memory in the LLM Era: Modular Architectures and Strategies in a Unified Framework](http://arxiv.org/abs/2604.01707v1)
  来源：arXiv | 日期：2026-04-02 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Memory emerges as the core module in the large language model (LLM)-based agents for long-horizon complex tasks (e.g., multi-turn dialogue, game playing, scientific discovery), where memory can enable knowledge accumulat...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [GraphWalk: Enabling Reasoning in Large Language Models through Tool-Based Graph Navigation](http://arxiv.org/abs/2604.01610v1)
  来源：arXiv | 日期：2026-04-02 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：知识图谱（KG）在问答应用中日益重要，但处理超大规模 KG 的多跳推理常受限于大语言模型（LLM）的上下文窗口。本文提出 GraphWalk，一种无需训练、与问题无关的工具化框架，使现成 LLM 能通过顺序图导航进行推理。不同于将领域知识编码进特定工具的框架，GraphWalk 为 LLM 提供了一组最小的正交图操作，足以遍历任何图结构。每个工具调用代表一个可验证的推理步骤，形成透明的执行轨迹。研究首先在迷宫遍历任务中验证，随后在模拟企...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ByteRover: Agent-Native Memory Through LLM-Curated Hierarchical Context](http://arxiv.org/abs/2604.01599v1)
  来源：arXiv | 日期：2026-04-02 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：存储增强生成（MAG）通过外部存储扩展了大语言模型的长上下文推理能力，但现有方法普遍将存储视为外部服务，导致存储系统无法理解知识，进而引发语义漂移、协作上下文丢失及故障恢复脆弱等问题。本文提出 ByteRover，一种智能体原生（agent-native）存储架构，实现了存储流水线的反转：由负责推理的同一 LLM 直接进行知识的策划、结构化和检索。ByteRover 将知识表示为分层上下文树（Context Tree），以本地文件系统的...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Why Gaussian Diffusion Models Fail on Discrete Data?](http://arxiv.org/abs/2604.02028v1)
  来源：arXiv | 日期：2026-04-02 | 相关度：2.75 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：扩散模型已成为连续领域生成建模的标准方法，但在离散数据上的应用仍面临挑战。本研究探讨了采用 DDPM 求解器的高斯扩散模型在处理连续空间中以 delta 分布混合表示的离散分布时表现不佳的原因。通过随机层次模型（Random Hierarchy Model），研究识别出一个关键采样区间，在该区间内加噪数据的密度呈现多模态特征。在此机制下，DDPM 采样会偶尔进入众数之间的低密度区域，产生超出分布（OOD）的输入，导致样本质量下降。研究表...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Single-cell and spatial profiling in cancer biology and clinical oncology.](https://pubmed.ncbi.nlm.nih.gov/41933186/)
  来源：PubMed | 日期：2026-04-03 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：多种单细胞和空间基因组学工具已彻底改变了我们解析包括癌症在内的复杂疾病的能力。通过对复杂多模态数据的分析，研究者深入了解了肿瘤生态系统中的基因组学、细胞状态及相互作用，从而能够剖析显著的生物学特征，并扩展了对药物反应、耐药性和靶点发现的理解。然而，在这些方法实现其全部临床潜力之前，仍面临若干挑战。本文讨论了相关的机遇、障碍及潜在解决方案，包括样本获取与保存方法、针对异质群体的分析方法和分析工具，并为在临床环境中稳健、可重复地使用这些技术...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TEDDY: A Family Of Foundation Models For Understanding Single Cell Biology](http://arxiv.org/abs/2503.03485v2)
  来源：arXiv | 日期：2025-03-05 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：深入理解疾病的生物学机制对医学和药物研发至关重要。单细胞RNA测序数据的增长推动了疾病生物学大模型的发展，但现有模型在下游应用中仅比特定任务模型略有提升。本研究通过两条路径改进单细胞基础模型：首先，将预训练数据规模扩大至1.16亿个细胞的多样化集合，规模超过了以往模型；其次，在预训练中引入大规模生物学标注作为监督信号。我们训练了TEDDY系列模型，包含6个基于Transformer架构的单细胞基础模型，参数量分别为7000万、1.6亿和...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Optimizing RAG Rerankers with LLM Feedback via Reinforcement Learning](http://arxiv.org/abs/2604.02091v1)
  来源：arXiv | 日期：2026-04-02 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：重排序器（Rerankers）在检索增强生成（RAG）中对优化检索结果至关重要。然而，现有重排序模型通常基于静态的人工相关性标签进行独立优化，与下游生成过程脱节。这种孤立导致了根本性的失配：被信息检索指标认为“主题相关”的文档，往往无法为大语言模型（LLM）生成准确答案提供实际效用。为弥补这一差距，我们提出了重排序偏好优化（RRPO），这是一种通过强化学习将重排序与 LLM 生成质量直接对齐的框架。RRPO 将重排序建模为序列决策过程，...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Prior Knowledge Makes It Possible: From Sublinear Graph Algorithms to LLM Test-Time Methods](http://arxiv.org/abs/2510.16609v2)
  来源：arXiv | 日期：2025-10-18 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Test-time augmentation, such as Retrieval-Augmented Generation (RAG) or tool use, critically depends on an interplay between a model's parametric knowledge and externally retrieved information. However, the theoretical u...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [From BM25 to Corrective RAG: Benchmarking Retrieval Strategies for Text-and-Table Documents](http://arxiv.org/abs/2604.01733v1)
  来源：arXiv | 日期：2026-04-02 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）系统的性能高度依赖检索质量，但目前尚缺乏针对包含文本和表格数据的异构文档的现代检索方法系统性比较。本研究在一个具有挑战性的财务问答基准上，对涵盖稀疏检索、稠密检索、混合融合、交叉编码重排序、查询扩展、索引增强及自适应检索的 10 种检索策略进行了基准测试。该基准包含 7,318 份文本与表格混合文档及 23,088 个查询。研究通过 Recall@k、MRR 和 nDCG 评估检索质量，并利用数字匹配（Number...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [One Pic is All it Takes: Poisoning Visual Document Retrieval Augmented Generation with a Single Image](http://arxiv.org/abs/2504.02132v4)
  来源：arXiv | 日期：2025-04-02 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) is instrumental for inhibiting hallucinations in large language models (LLMs) through the use of a factual knowledge base (KB). Although PDF documents are prominent sources of knowled...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AI in Insurance: Adaptive Questionnaires for Improved Risk Profiling](http://arxiv.org/abs/2604.02034v1)
  来源：arXiv | 日期：2026-04-02 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Insurance application processes often rely on lengthy and standardized questionnaires that struggle to capture individual differences. Moreover, insurers must blindly trust users' responses, increasing the chances of fra...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Retrieval-Augmented Question Answering over Scientific Literature for the Electron-Ion Collider](http://arxiv.org/abs/2604.02259v1)
  来源：arXiv | 日期：2026-04-02 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：To harness the power of Language Models in answering domain specific specialized technical questions, Retrieval Augmented Generation (RAG) is been used widely. In this work, we have developed a Q\&A application inspired ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Unified modeling of 3D molecular generation via atomic interactions with PocketXMol.](https://pubmed.ncbi.nlm.nih.gov/41713417/)
  来源：PubMed | 日期：2026-04-02 | 相关度：3.1 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：本文介绍了 PocketXMol，这是一种原子级模型，旨在统一与蛋白质口袋相互作用相关的生成任务。PocketXMol 采用原子提示（atomic prompts）作为任务规范，支持包括小分子和多肽的结构预测及从头设计在内的多种分子任务，且无需针对特定任务进行微调。在 13 个计算基准测试中，PocketXMol 在 11 个项目中表现强劲，并在其余两个项目中保持了竞争力，性能超越了 55 个基准模型。研究团队应用 PocketXMol...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [BIOGEN: Evidence-Grounded Multi-Agent Reasoning Framework for Transcriptomic Interpretation in Antimicrobial Resistance](http://arxiv.org/abs/2510.16082v5)
  来源：arXiv | 日期：2025-10-17 | 相关度：3.1 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：解释RNA测序（RNA-seq）中的基因簇在抗微生物耐药性（AMR）研究中具有挑战性，因为生成科学假设需要深入的机制见解。现有的通路富集方法虽能总结共表达模块，但往往缺乏针对特定基因簇的详细解释，且与支持文献的联系较弱。本研究提出了BIOGEN，一个用于RNA-seq转录模块事后解释的证据驱动多智能体框架。BIOGEN结合了生物医学检索、结构化推理和多重批判验证（multi-critic verification），旨在生成具有明确证据...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Generative AI Spotlights the Human Core of Data Science: Implications for Education](http://arxiv.org/abs/2604.02238v1)
  来源：arXiv | 日期：2026-04-02 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：生成式人工智能（GAI）揭示了数据科学中不可还原的人类核心：GAI 的进步应强化而非削弱数据科学教育中对人类推理的关注。GAI 目前已能执行包括数据清洗、摘要、可视化、建模和报告起草在内的多种常规工作流。然而，最关键的能力仍属于人类：问题制定、测量与设计、因果识别、统计与计算推理、伦理与问责以及意义构建。本文基于 Donoho 的“大数据科学”（GDS）框架，追溯了数据科学源于 Tukey 的数据分析愿景、监控资本主义的商业逻辑及学术项...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [APITestGenie: Generating Web API Tests from Requirements and API Specifications with LLMs](http://arxiv.org/abs/2604.02039v1)
  来源：arXiv | 日期：2026-04-02 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：现代软件系统高度依赖 Web API，但编写有效且可执行的测试脚本仍是一项耗时且易出错的手动任务。本文介绍了 APITestGenie，这是一种利用大语言模型（LLM）、检索增强生成（RAG）和提示工程，直接根据业务需求和 OpenAPI 规范自动生成 API 集成测试的创新工具。我们在 10 个真实 API 上对 APITestGenie 进行了评估，其中包括来自汽车领域工业合作伙伴的 8 个 API（包含约 1,000 个实时端点）...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。
