# 每日论文监控日报 (2026-04-24)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 41 篇新论文。

## 抓取状态

- arXiv：成功，命中 48 篇
- PubMed：成功，命中 36 篇
- bioRxiv：成功，命中 0 篇
- medRxiv：成功，命中 0 篇

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [Structure-guided molecular design with contrastive 3D protein-ligand learning](http://arxiv.org/abs/2604.19562v1)
  来源：arXiv | 日期：2026-04-21 | 相关度：8.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Structure-based drug discovery faces the dual challenge of accurately capturing 3D protein-ligand interactions while navigating ultra-large chemical spaces to identify synthetically accessible candidates. In this work, w...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multimodal Protein Language Models for Enzyme Kinetic Parameters: From Substrate Recognition to Conformational Adaptation](http://arxiv.org/abs/2603.12845v2)
  来源：arXiv | 日期：2026-03-13 | 相关度：7.8 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Predicting enzyme kinetic parameters quantifies how efficiently an enzyme catalyzes a specific substrate under defined biochemical conditions. Canonical parameters such as the turnover number ($k_\text{cat}$), Michaelis ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EgoMotion: Hierarchical Reasoning and Diffusion for Egocentric Vision-Language Motion Generation](http://arxiv.org/abs/2604.19105v1)
  来源：arXiv | 日期：2026-04-21 | 相关度：7.5 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Faithfully modeling human behavior in dynamic environments is a foundational challenge for embodied intelligence. While conditional motion synthesis has achieved significant advances, egocentric motion generation remains...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RAG-KT: Cross-platform Explainable Knowledge Tracing with Multi-view Fusion Retrieval Generation](http://arxiv.org/abs/2604.10960v2)
  来源：arXiv | 日期：2026-04-13 | 相关度：6.55 | 新颖度：1.7
  匹配主题：foundation_model_agent
  中文摘要：Knowledge Tracing (KT) infers a student's knowledge state from past interactions to predict future performance. Conventional Deep Learning (DL)-based KT models are typically tied to platform-specific identifiers and late...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Structure-Grounded Knowledge Retrieval via Code Dependencies for Multi-Step Data Reasoning](http://arxiv.org/abs/2604.10516v2)
  来源：arXiv | 日期：2026-04-12 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Selecting the right knowledge is critical when using large language models (LLMs) to solve domain-specific data analysis tasks. However, most retrieval-augmented approaches rely primarily on lexical or embedding similari...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SCM: Sleep-Consolidated Memory with Algorithmic Forgetting for Large Language Models](http://arxiv.org/abs/2604.20943v1)
  来源：arXiv | 日期：2026-04-22 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：We present SCM (Sleep-Consolidated Memory), a research preview of a memory architecture for large language models that draws on neuroscientific principles to address a fundamental limitation in current systems: the absen...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Research Question to Scientific Workflow: Leveraging Agentic AI for Science Automation](http://arxiv.org/abs/2604.21910v1)
  来源：arXiv | 日期：2026-04-23 | 相关度：2.75 | 新颖度：7.75
  匹配主题：foundation_model_agent
  中文摘要：Scientific workflow systems automate execution -- scheduling, fault tolerance, resource management -- but not the semantic translation that precedes it. Scientists still manually convert research questions into workflow ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [WildFireVQA: A Large-Scale Radiometric Thermal VQA Benchmark for Aerial Wildfire Monitoring](http://arxiv.org/abs/2604.20190v1)
  来源：arXiv | 日期：2026-04-22 | 相关度：7.5 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Wildfire monitoring requires timely, actionable situational awareness from airborne platforms, yet existing aerial visual question answering (VQA) benchmarks do not evaluate wildfire-specific multimodal reasoning grounde...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [It's High Time: A Survey of Temporal Question Answering](http://arxiv.org/abs/2505.20243v4)
  来源：arXiv | 日期：2025-05-26 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Time plays a critical role in how information is generated, retrieved, and interpreted. In this survey, we provide a comprehensive overview of Temporal Question Answering (TQA), a research area that focuses on answering ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Human-like Content Analysis for Generative AI with Language-Grounded Sparse Encoders](http://arxiv.org/abs/2508.18236v4)
  来源：arXiv | 日期：2025-08-20 | 相关度：8.5 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：The rapid development of generative AI has transformed content creation, communication, and human development. However, this technology raises profound concerns in high-stakes domains, demanding rigorous methods to analy...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Multimodal survival analysis of glioblastoma using whole-slide histopathology, gene expression, clinical variables and language-model-derived mutation features.](https://pubmed.ncbi.nlm.nih.gov/42014603/)
  来源：PubMed | 日期：2026-04-21 | 相关度：7.8 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Glioblastoma (GBM) is a highly aggressive brain tumor with poor prognosis, motivating the development of more accurate survival prediction models that can integrate complementary clinical and molecular information. Howev...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [KompeteAI: Accelerated Autonomous Multi-Agent System for End-to-End Pipeline Generation for Machine Learning Problems](http://arxiv.org/abs/2508.10177v3)
  来源：arXiv | 日期：2025-08-13 | 相关度：6.55 | 新颖度：6.7
  匹配主题：foundation_model_agent
  中文摘要：Recent Large Language Model (LLM)-based AutoML systems demonstrate impressive capabilities but face significant limitations such as constrained exploration strategies and a severe execution bottleneck. Exploration is hin...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SlideAgent: Hierarchical Agentic Framework for Multi-Page Visual Document Understanding](http://arxiv.org/abs/2510.26615v3)
  来源：arXiv | 日期：2025-10-30 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) extends large language models (LLMs) with external knowledge, but it must balance limited effective context, redundant retrieved evidence, and the loss of fine-grained facts under agg...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Knowledge Capsules: Structured Nonparametric Memory Units for LLMs](http://arxiv.org/abs/2604.20487v2)
  来源：arXiv | 日期：2026-04-22 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) encode knowledge in parametric weights, making it costly to update or extend without retraining. Retrieval-augmented generation (RAG) mitigates this limitation by appending retrieved text to ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [Automatic Ontology Construction Using LLMs as an External Layer of Memory, Verification, and Planning for Hybrid Intelligent Systems](http://arxiv.org/abs/2604.20795v1)
  来源：arXiv | 日期：2026-04-22 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：This paper presents a hybrid architecture for intelligent systems in which large language models (LLMs) are extended with an external ontological memory layer. Instead of relying solely on parametric knowledge and vector...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Reproducibility Study of Metacognitive Retrieval-Augmented Generation](http://arxiv.org/abs/2604.19899v1)
  来源：arXiv | 日期：2026-04-21 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Recently, Retrieval Augmented Generation (RAG) has shifted focus to multi-retrieval approaches to tackle complex tasks such as multi-hop question answering. However, these systems struggle to decide when to stop searchin...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Survey on MLLM-based Visually Rich Document Understanding: Methods, Challenges, and Emerging Trends](http://arxiv.org/abs/2507.09861v2)
  来源：arXiv | 日期：2025-07-14 | 相关度：6.1 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Visually Rich Document Understanding (VRDU) has become a pivotal area of research, driven by the need to automatically interpret documents that contain intricate visual, textual, and structural elements. Recently, Multim...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ItemRAG: Item-Based Retrieval-Augmented Generation for LLM-Based Recommendation](http://arxiv.org/abs/2511.15141v2)
  来源：arXiv | 日期：2025-11-19 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Recently, large language models (LLMs) have been widely used as recommender systems, owing to their reasoning capability and effectiveness in handling cold-start items. A common approach prompts an LLM with a target user...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ChipCraftBrain: Validation-First RTL Generation via Multi-Agent Orchestration](http://arxiv.org/abs/2604.19856v1)
  来源：arXiv | 日期：2026-04-21 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) show promise for generating Register-Transfer Level (RTL) code from natural language specifications, but single-shot generation achieves only 60-65% functional correctness on standard benchma...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Stateless Decision Memory for Enterprise AI Agents](http://arxiv.org/abs/2604.20158v1)
  来源：arXiv | 日期：2026-04-22 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：在核保、理赔及税务审计等受监管领域的长程决策智能体部署中，尽管状态化记忆架构日益复杂，但企业仍倾向于使用检索增强流水线。本文指出，这是由于受监管场景对确定性回放、可审计性、多租户隔离及水平扩展的无状态性有核心需求，而状态化架构在设计上违背了这些属性。为此，研究者提出了确定性投影记忆（DPM）：由只增（append-only）事件日志和决策时的单次任务条件投影组成。在10个监管决策案例的测试中，当压缩比为20倍时，DPM的事实精确度提升了...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RELOOP: Recursive Retrieval with Multi-Hop Reasoner and Planners for Heterogeneous QA](http://arxiv.org/abs/2510.20505v4)
  来源：arXiv | 日期：2025-10-23 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）在处理多步复杂问题和异构证据源时表现不佳，且常在准确率与延迟/成本之间权衡。本文提出 RELOOP 框架，核心是分层序列（HSEQ）技术，将文档、表格和知识图谱线性化为带有轻量级结构标签的可逆序列。该框架包含 Head Agent 和 Iteration Agent：前者负责引导检索，后者通过结构感知动作（如父子节点跳跃、表格行列邻居、知识图谱关系）扩展 HSeq 以收集充足证据。最后，Head Agent 整合规...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Progressive Multimodal Search and Reasoning for Knowledge-Intensive Visual Question Answering](http://arxiv.org/abs/2509.00798v7)
  来源：arXiv | 日期：2025-08-31 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：知识密集型视觉问答（VQA）需要图像内容之外的外部知识，要求精确的视觉定位以及视觉与文本信息的连贯整合。尽管多模态检索增强生成（RAG）通过引入外部知识库取得了显著进展，但现有方法多采用单次处理框架，往往无法获取充足知识，且缺乏修正错误推理的机制。本文提出 PMSR（渐进式多模态搜索与推理）框架，通过逐步构建结构化推理轨迹来增强知识获取与综合。PMSR 利用基于最新记录和整体轨迹的双范围查询，从异构知识库中检索多样化知识。随后，通过组合...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AstaBench: Rigorous Benchmarking of AI Agents with a Scientific Research Suite](http://arxiv.org/abs/2510.21652v2)
  来源：arXiv | 日期：2025-10-24 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：AI 智能体有望通过自动化文献综述、实验复制、数据分析及提出新研究方向来变革科学生产力。目前已出现 AI Scientist 和 AIGS 等专用智能体，但现有基准测试在工具可重复性、变量控制（如成本和工具访问）、标准化接口、真实科研场景衡量以及基准线完整性方面存在不足。为此，研究者推出了 AstaBench，这是一个严谨的科学研究智能体基准测试套件。它包含跨越多个科学领域和发现全过程的 2400 多个问题，部分源自真实用户需求。该套件...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Album: executable building blocks for scientific imaging routines, from sharing to LLM-assisted orchestration](http://arxiv.org/abs/2110.00601v2)
  来源：arXiv | 日期：2021-10-01 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：开源科学软件的开发与复现面临发现难、适配难、共享难及环境不稳定等挑战。本文提出 Album，一个将科学例程打包为可执行构件的开源框架。该框架包含两个核心原语：一是“解决方案（solution）”，即包含机器可读元数据、参数、环境规范和生命周期钩子的 Python 原生执行入口；二是“目录（catalog）”，即基于 Git 的去中心化分发机制，支持索引搜索和来源治理。Album 采用双上下文执行模型，由宿主控制器评估清单并准备隔离环境，...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [ORPHEAS: A Cross-Lingual Greek-English Embedding Model for Retrieval-Augmented Generation](http://arxiv.org/abs/2604.20666v1)
  来源：arXiv | 日期：2026-04-22 | 相关度：4.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Effective retrieval-augmented generation across bilingual Greek--English applications requires embedding models capable of capturing both domain-specific semantic relationships and cross-lingual semantic alignment. Exist...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Foundation Models in Biomedical Imaging: Turning Hype into Reality](http://arxiv.org/abs/2512.15808v2)
  来源：arXiv | 日期：2025-12-17 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：基础模型（FMs）正推动生物医学成像从特定任务模型向统一骨干模型转变，旨在整合影像、病理、临床记录和基因组数据。然而，这一愿景与现代医学细分专业化的趋势存在冲突。受限于数据稀缺、领域异质性和可解释性不足，基准测试的成功与实际临床价值之间存在差距。本文提出 REAL-FM（基础模型真实世界评估与考核）多维框架，从数据、技术就绪度、临床价值、工作流集成和负责任 AI 五个维度进行评估。研究发现，尽管 FMs 在模式识别方面表现出色，但在因果...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Adaptive Defense Orchestration for RAG: A Sentinel-Strategist Architecture against Multi-Vector Attacks](http://arxiv.org/abs/2604.20932v1)
  来源：arXiv | 日期：2026-04-22 | 相关度：0.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）系统在医疗和法律等处理私有领域知识的敏感领域应用日益广泛，但这引入了成员推理、数据投毒和内容泄露等显著安全风险。直接开启所有防御措施会导致严重的效用损失，实验显示全量防御栈会使上下文召回率下降超过40%，检索退化是主要失效模式。为此，本文提出“哨兵-策略家”（Sentinel-Strategist）架构，这是一种上下文感知的风险分析与防御选择框架。该架构通过“哨兵”检测异常检索行为，并由“策略家”根据查询上下文选择...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Coverage, Not Averages: Semantic Stratification for Trustworthy Retrieval Evaluation](http://arxiv.org/abs/2604.20763v1)
  来源：arXiv | 日期：2026-04-22 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：检索质量是检索增强生成（RAG）准确性和鲁棒性的核心瓶颈。当前的评估方法多依赖于启发式构建的查询集，这引入了隐性的内在偏差。本研究将检索评估形式化为一个统计估计问题，指出指标的可靠性受限于评估集的构建方式。为此，研究者提出了“语义分层”（Semantic Stratification）框架，通过将文档组织成基于实体的可解释全局聚类空间，并针对缺失的语义层级系统地生成查询，使评估回归语料库结构本身。该方法实现了：(1) 跨检索方案的形式化...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Generalizable deep-learning-based mRNA-protein interaction prediction strongly depends on protein diversity.](https://pubmed.ncbi.nlm.nih.gov/42015301/)
  来源：PubMed | 日期：2026-04-21 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Proteins regulate diverse biological processes through interactions with other molecules, including RNAs. RNA-binding proteins (RBPs) are essential regulators of gene expression, forming specific mRNA-protein interaction...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Context Attribution with Multi-Armed Bandit Optimization](http://arxiv.org/abs/2506.19977v2)
  来源：arXiv | 日期：2025-06-24 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Understanding which parts of the retrieved context contribute to a large language model's generated answer is essential for building interpretable and trustworthy retrieval-augmented generation. We propose a novel framew...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Optimizing User Profiles via Contextual Bandits for Retrieval-Augmented LLM Personalization](http://arxiv.org/abs/2601.12078v2)
  来源：arXiv | 日期：2026-01-17 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) excel at general-purpose tasks, yet adapting their responses to individual users remains challenging. Retrieval augmentation provides a lightweight alternative to fine-tuning by conditioning ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GenerativeMPC: VLM-RAG-guided Whole-Body MPC with Virtual Impedance for Bimanual Mobile Manipulation](http://arxiv.org/abs/2604.19522v1)
  来源：arXiv | 日期：2026-04-21 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Bimanual mobile manipulation requires a seamless integration between high-level semantic reasoning and safe, compliant physical interaction - a challenge that end-to-end models approach opaquely and classical controllers...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [HaS: Accelerating RAG through Homology-Aware Speculative Retrieval](http://arxiv.org/abs/2604.20452v1)
  来源：arXiv | 日期：2026-04-22 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) expands the knowledge boundary of large language models (LLMs) at inference by retrieving external documents as context. However, retrieval becomes increasingly time-consuming as the ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Trustworthy Clinical Decision Support Using Meta-Predicates and Domain-Specific Languages](http://arxiv.org/abs/2604.21263v1)
  来源：arXiv | 日期：2026-04-23 | 相关度：3.05 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：\textbf{Background:} Regulatory frameworks for AI in healthcare, including the EU AI Act and FDA guidance on AI/ML-based medical devices, require clinical decision support to demonstrate not only accuracy but auditabilit...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [scpFormer: A Foundation Model for Unified Representation and Integration of the Single-Cell Proteomics](http://arxiv.org/abs/2604.20003v1)
  来源：arXiv | 日期：2026-04-21 | 相关度：2.4 | 新颖度：1.5
  匹配主题：未命中具体主题
  中文摘要：The integration of single-cell proteomic data is often hindered by the fragmented nature of targeted antibody panels. To address this limitation, we introduce scpFormer, a transformer-based foundation model designed for ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Training-free retrieval-augmented generation with reinforced reasoning for flood damage nowcasting](http://arxiv.org/abs/2602.10312v2)
  来源：arXiv | 日期：2026-02-10 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：本文提出了 R2RAG-Flood，这是一个无需训练的检索增强生成（RAG）框架，专门用于具有强化推理能力的洪水灾害即时预报。该框架通过标记的表格记录构建了一个以推理为中心的知识库，其中每个样本包含结构化预测因子、简短的文本摘要以及模型生成的推理轨迹。在推理阶段，系统通过地理邻域样本和选定的示例（free-shots）增强目标提示词，从而在无需特定任务微调的情况下实现基于案例的推理。该流程采用两阶段程序：首先确定损害是否发生，随后在三级...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [From Past To Path: Masked History Learning for Next-Item Prediction in Generative Recommendation](http://arxiv.org/abs/2509.23649v2)
  来源：arXiv | 日期：2025-09-28 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：生成式推荐通过直接生成物品标识符，已成为推荐系统的一种极具前景的范式。然而，其潜力受限于纯自回归训练模式，该模式仅关注预测下一项，忽略了用户交互历史中丰富的内部结构，难以捕捉潜在意图。为此，我们提出掩码历史学习（MHL）框架，将训练目标从简单的下一步预测转向对历史的深度理解。MHL 在标准自回归目标基础上增加了重建掩码历史项的辅助任务，迫使模型理解用户过去行为形成特定路径的原因。该框架包含两大核心贡献：一是基于熵引导的掩码策略，智能选择...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Improving End-to-End Training of Retrieval-Augmented Generation Models via Joint Stochastic Approximation](http://arxiv.org/abs/2508.18168v3)
  来源：arXiv | 日期：2025-08-25 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）已成为结合参数化记忆与非参数化记忆的公认范式。RAG模型由检索器和生成器两个串联组件构成。端到端优化的主要挑战在于需要对知识库中作为离散隐变量的相关段落进行边际化处理。传统的Top-K边际化方法和变分RAG（VRAG）往往面临梯度估计偏差或高方差的问题。本文提出并开发了基于联合随机逼近（JSA）的RAG端到端训练方法，即JSA-RAG。JSA算法是期望最大化（EM）算法的随机扩展，在估计离散隐变量模型方面具有强大性...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Self-Aware Vector Embeddings for Retrieval-Augmented Generation: A Neuroscience-Inspired Framework for Temporal, Confidence-Weighted, and Relational Knowledge](http://arxiv.org/abs/2604.20598v1)
  来源：arXiv | 日期：2026-04-22 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：现代检索增强生成（RAG）系统将向量嵌入视为静态且缺乏上下文的产物，无法识别其创建时间、来源可信度或与其他向量的依赖关系，导致在处理版本化技术查询时准确率仅为58%。本文提出SmartVector框架，通过赋予嵌入向量时间感知、置信度衰减和关系感知三种显式属性，并模拟海马体-新皮层记忆整合过程建立五阶段生命周期。该框架在检索时采用结合语义相关性、时间有效性、实时置信度和图关系重要性的四信号评分，取代单一的余弦相似度。后台整合代理负责检测...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Advancing AI for multi-omics and clinical data integration in basic and translational cancer research.](https://pubmed.ncbi.nlm.nih.gov/42014628/)
  来源：PubMed | 日期：2026-04-21 | 相关度：3.75 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：The extensive heterogeneity of cancer across biological scales necessitates a holistic approach beyond single-analyte methods. Integrating multi-omics data - from genomics to proteomics - with multimodal information, suc...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [All Languages Matter: Understanding and Mitigating Language Bias in Multilingual RAG](http://arxiv.org/abs/2604.20199v1)
  来源：arXiv | 日期：2026-04-22 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Multilingual Retrieval-Augmented Generation (mRAG) leverages cross-lingual evidence to ground Large Language Models (LLMs) in global knowledge. However, we show that current mRAG systems suffer from a language bias durin...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。
