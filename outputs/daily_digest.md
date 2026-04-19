# 每日论文监控日报 (2026-04-19)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 19 篇新论文。

## 抓取状态

- arXiv：成功，命中 21 篇
- PubMed：成功，命中 27 篇
- bioRxiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='api.biorxiv.org', port=443): Read timed out. (read timeout=60)
- medRxiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='api.biorxiv.org', port=443): Read timed out. (read timeout=60)

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [Retrieve, Then Classify: Corpus-Grounded Automation of Clinical Value Set Authoring](http://arxiv.org/abs/2604.14616v1)
  来源：arXiv | 日期：2026-04-16 | 相关度：7.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Clinical value set authoring -- the task of identifying all codes in a standardized vocabulary that define a clinical concept -- is a recurring bottleneck in clinical quality measurement and phenotyping. A natural approa...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [VideoStir: Understanding Long Videos via Spatio-Temporally Structured and Intent-Aware RAG](http://arxiv.org/abs/2604.05418v3)
  来源：arXiv | 日期：2026-04-07 | 相关度：6.8 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Scaling multimodal large language models (MLLMs) to long videos is constrained by limited context windows. While retrieval-augmented generation (RAG) is a promising remedy by organizing query-relevant visual evidence int...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AI4S-SDS: A Neuro-Symbolic Solvent Design System via Sparse MCTS and Differentiable Physics Alignment](http://arxiv.org/abs/2603.03686v3)
  来源：arXiv | 日期：2026-03-04 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Automated design of chemical formulations is a cornerstone of materials science, yet it requires navigating a high-dimensional combinatorial space involving discrete compositional choices and continuous geometric constra...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 低优先级

### Foundation Model / Agent

- [UrbanClipAtlas: A Visual Analytics Framework for Event and Scene Retrieval in Urban Videos](http://arxiv.org/abs/2604.15225v1)
  来源：arXiv | 日期：2026-04-16 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Extracting actionable insights from long-duration urban videos is often labor-intensive: analysts must manually sift through raw footage to pinpoint target events or uncover broader behavioral trends. In this work, we pr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [El Agente Forjador: Task-Driven Agent Generation for Quantum Simulation](http://arxiv.org/abs/2604.14609v1)
  来源：arXiv | 日期：2026-04-16 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：AI for science promises to accelerate the discovery process. The advent of large language models (LLMs) and agentic workflows enables the expediting of a growing range of scientific tasks. However, most of the current ge...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [UniDoc-RL: Coarse-to-Fine Visual RAG with Hierarchical Actions and Dense Rewards](http://arxiv.org/abs/2604.14967v1)
  来源：arXiv | 日期：2026-04-16 | 相关度：4.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：检索增强生成（RAG）通过外部视觉知识扩展了大视觉语言模型（LVLM）的能力。然而，现有视觉RAG系统多依赖通用检索信号，忽略了复杂推理所需的细粒度视觉语义。为此，我们提出UniDoc-RL，这是一个统一的强化学习框架，使LVLM智能体能够协同执行检索、重排序、主动视觉感知和推理任务。UniDoc-RL将视觉信息获取建模为具有分层动作空间的序列决策问题，将视觉证据从粗粒度的文档检索逐步细化为细粒度的图像选择和主动区域裁剪，从而抑制无关内...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RACER: Retrieval-Augmented Contextual Rapid Speculative Decoding](http://arxiv.org/abs/2604.14885v1)
  来源：arXiv | 日期：2026-04-16 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：大语言模型（LLM）的自回归解码由于每步仅生成一个 token，导致推理延迟较高。投机解码（SD）通过“猜测-验证”策略缓解了这一问题，但现有的免训练变体面临权衡：基于检索的草稿在缺乏精确匹配时会失效，而基于 Logit 的草稿则缺乏结构化引导。本文提出 RACER（检索增强上下文快速投机解码），这是一种轻量级且免训练的方法，它将检索到的精确模式与 Logit 驱动的未来线索相结合。这种统一的方法既提供了可靠的锚点，又具备灵活的外推能力...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CheMLT-F: multitask learning in biochemistry through transformer fusion.](https://pubmed.ncbi.nlm.nih.gov/41992362/)
  来源：PubMed | 日期：2026-04-16 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：药物研发因需在庞大化学空间内筛选有效性、毒性和理化性质而耗时耗力，传统的单任务预测器导致工作流碎片化且表征难以复用。本研究提出 CheMLT-F，一种紧凑的多任务 Transformer 模型，通过融合分子和蛋白质序列编码器，学习涵盖 680 多个终点的统一表征，包括多种毒性、理化性质和药物-靶点相互作用（DTI）。在 13 个公开基准测试中，CheMLT-F 在毒性分类上达到 SOTA 水平，在理化性质预测上创下新纪录，并在 KIBA...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SGA-MCTS: Decoupling Planning from Execution via Training-Free Atomic Experience Retrieval](http://arxiv.org/abs/2604.14712v1)
  来源：arXiv | 日期：2026-04-16 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：大型语言模型（LLM）在解决现实任务时需要复杂的多步决策能力，但现有规划方法在推理搜索的高延迟与监督微调的泛化性限制之间存在权衡。为此，研究者提出了SGA-MCTS框架，将LLM规划建模为非参数化检索过程。在离线阶段，该框架利用蒙特卡洛树搜索（MCTS）探索解空间，并将高保真轨迹蒸馏为“状态-目标-动作”（SGA）原子。这些原子是去词汇化的原语，通过将具体实体抽象为符号槽位，保留了可重用的因果逻辑并去除了领域特定噪声。在在线阶段，检索增...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Intermediate Layers Encode Optimal Biological Representations in Single-Cell Foundation Models](http://arxiv.org/abs/2604.14838v1)
  来源：arXiv | 日期：2026-04-16 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：当前的单细胞基础模型基准测试普遍提取最后一层嵌入，假设其代表了最优特征空间。本研究系统评估了 scFoundation（1亿参数）和 Tahoe-X1（13.3亿参数）在轨迹推断和扰动响应预测任务中的逐层表示。分析表明，最优特征层具有任务依赖性（轨迹推断在 60% 深度处达到峰值，性能比最后一层高出 31%）和背景依赖性（扰动预测的最优层在 T 细胞激活状态下偏移范围达 0-96%）。值得注意的是，在静息细胞中，第一层嵌入的性能优于所有...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [LR-Robot: An Human-in-the-Loop LLM Framework for Systematic Literature Reviews with Applications in Financial Research](http://arxiv.org/abs/2604.14793v1)
  来源：arXiv | 日期：2026-04-16 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：The exponential growth of financial research has rendered traditional systematic literature reviews (SLRs) increasingly impractical, as manual screening and narrative synthesis struggle to keep pace with the scale and co...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [BarrierBench: Evaluating Large Language Models for Safety Verification in Dynamical Systems](http://arxiv.org/abs/2511.09363v2)
  来源：arXiv | 日期：2025-11-12 | 相关度：4.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：动力系统通过屏障证书（barrier certificates）进行的安全性验证对于确保自主应用的正确定性至关重要。合成这些证书涉及发现复杂的数学函数，但现有方法面临可扩展性差、过度依赖预设模板以及函数空间搜索效率低下等挑战。此外，该过程高度依赖专家的理论与实践经验。本文探讨了语言模型是否能捕捉并操作此类专家推理，并提出了一个基于大语言模型（LLM）的智能体框架，用于屏障证书的自动化合成。该框架利用自然语言推理来提议、改进和验证候选证书...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Enhancing Large Language Models with Retrieval Augmented Generation for Software Testing and Inspection Automation](http://arxiv.org/abs/2604.15270v1)
  来源：arXiv | 日期：2026-04-16 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：In this paper, we focus on automating two of the widely used Verification and Validation (V&V) activities in the Software Development Lifecycle (SDLC): Software testing and software inspection (also known as review). Con...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Zero-Effort Image-to-Music Generation: An Interpretable RAG-based VLM Approach](http://arxiv.org/abs/2509.22378v2)
  来源：arXiv | 日期：2025-09-26 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：图像到音乐（I2M）生成在游戏、广告和多模态艺术创作中具有重要应用，但现有端到端方法由于任务的主观性常缺乏可解释性，且计算资源需求巨大。为此，本文提出首个基于视觉语言模型（VLM）的I2M框架，旨在实现高可解释性与低计算成本。该框架利用 ABC 记谱法作为桥梁连接文本与音乐模态，使 VLM 能够通过自然语言生成音乐。研究引入了多模态检索增强生成（RAG）和自我修正（Self-refinement）技术，使 VLM 无需外部训练即可产出高...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Query pipeline optimization for cancer patient question answering systems](http://arxiv.org/abs/2412.14751v2)
  来源：arXiv | 日期：2024-12-19 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：检索增强生成（RAG）通过利用查询管道检索相关的外部信息，并将响应建立在检索到的知识之上，从而减轻大语言模型（LLM）的幻觉。然而，针对癌症患者问答系统（CPQA）的查询管道优化需要结合领域特定因素对多个组件进行单独优化。本研究提出了一种针对 CPQA 系统 RAG 查询管道的三方面优化方法，利用 PubMed 和 PubMed Central 等公共生物医学数据库。优化内容包括：（1）文档检索：通过对比分析 NCBI 资源并引入混合语...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MAB-DQA: Addressing Query Aspect Importance in Document Question Answering with Multi-Armed Bandits](http://arxiv.org/abs/2604.08952v2)
  来源：arXiv | 日期：2026-04-10 | 相关度：2.75 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：文档问答（DQA）是文档理解的关键任务，涉及根据用户查询从文档中生成答案。由于需要解释视觉布局，近期研究多采用多模态检索增强生成（RAG）处理页面图像。然而，多模态 RAG 在处理大量图像时存在局限，检索阶段通常仅保留少数候选页（如 Top-4），导致信息丰富但视觉显著性较低的内容被忽略。为解决此问题，本文提出基于多臂老虎机（MAB）的 DQA 框架（MAB-DQA），显式建模查询中多个隐含维度的重要性。MAB-DQA 将查询分解为维度...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [CoDaS: AI Co-Data-Scientist for Biomarker Discovery via Wearable Sensors](http://arxiv.org/abs/2604.14615v1)
  来源：arXiv | 日期：2026-04-16 | 相关度：2.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：数字健康领域的科学发现需要将可穿戴设备的连续生理信号转化为临床可操作的生物标志物。本文介绍了 CoDaS（AI 协同数据科学家），这是一个多智能体系统，通过大规模可穿戴数据集，将生物标志物发现构建为包含假设生成、统计分析、对抗验证、基于文献的推理及人工监督的迭代过程。在总计 9,279 名受试者的三个队列中，CoDaS 识别出 41 个心理健康候选数字标志物和 25 个代谢结果标志物，并进行了包含复制性、稳定性、鲁棒性和判别力的内部验证...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Toward Agentic RAG for Ukrainian](http://arxiv.org/abs/2604.14896v1)
  来源：arXiv | 日期：2026-04-16 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：本研究针对乌克兰语的代理式检索增强生成（Agentic RAG）进行了初步探索，该工作是在 UNLP 2026 多领域文档理解共享任务框架下开展的。系统架构结合了两阶段检索流程（利用 BGE-M3 模型进行初步检索并配合 BGE 重排序）以及基于 Qwen2.5-3B-Instruct 构建的轻量化代理层，该代理层具备查询改写（query rephrasing）和答案重试循环（answer-retry loops）功能。实验分析表明，检...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents](http://arxiv.org/abs/2601.03236v2)
  来源：arXiv | 日期：2026-01-06 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：存储增强生成（MAG）通过外部存储扩展大语言模型以支持长上下文推理，但现有方法主要依赖单一存储库的语义相似性检索，导致时间、因果和实体信息相互纠缠。这种设计限制了查询意图与检索证据之间的可解释性与对齐，进而降低了推理准确性。本文提出 MAGMA，一种基于多图的智能体记忆架构，将每个记忆项分别表示在正交的语义、时间、因果和实体图中。MAGMA 将检索过程定义为在这些关系视图上的策略引导遍历，实现了查询自适应选择和结构化上下文构建。通过将记...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。
