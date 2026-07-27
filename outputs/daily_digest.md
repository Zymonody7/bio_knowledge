# 每日论文监控日报 (2026-07-27)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 14 篇新论文。

## 抓取状态

- arXiv：成功，命中 9 篇
- PubMed：成功，命中 27 篇
- bioRxiv：成功，命中 7 篇
- medRxiv：成功，命中 4 篇

## 最值得看

### Foundation Model / Agent

- [AINN-Express: A Leakage-Aware, Sequence-Only Predictor of VHH Antibody Expression Built on the AINN-P1 Protein Foundation Model](https://www.biorxiv.org/content/10.64898/2026.07.21.739256v1)
  来源：bioRxiv | 日期：2026-07-24 | 相关度：8.7 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Expression -- whether an antibody can be produced at usable yield -- is one of the earliest and most expensive filters in therapeutic discovery. We present AINN-Express, a sequence-only predictor of VHH single-domain ant...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Benchmarking Fine-tuning and Retrieval Strategies for a Multimodal Language Model on the NRC Reactor Operator Licensing Examination](http://arxiv.org/abs/2607.22067v1)
  来源：arXiv | 日期：2026-07-24 | 相关度：7.9 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：本研究评估了拥有310亿参数的开源多模态模型Gemma 4 31B-IT在核能领域知识应用的能力。通过对2015-2021年间14场美国核管理委员会（NRC）反应堆操作员通用基础考试（GFE，包含压水堆与沸水堆各7场）进行基准测试，对比了八种模型检索配置。研究采用了基于Gemini蒸馏的思维链（CoT）推理进行监督微调（SFT）、基于BM25算法的检索增强生成（RAG）以及检索增强微调（RAFT）。在检索流程中，对比了固定大小滑动窗口分...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [Small but Specialized: A Domain-Adapted Retrieval-Augmented LLM Outperforms Frontier Generalists in Pediatric and Adolescent Gynecology](https://www.medrxiv.org/content/10.64898/2026.07.22.26358688v1)
  来源：medRxiv | 日期：2026-07-24 | 相关度：7.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：小儿和青少年妇科学（PAG）对临床指导的准确性要求极高，但通用大模型（LLM）往往缺乏可靠的领域知识。本研究开发了领域专用模型 PAG-Health-LLM，旨在评估小型专用模型是否能超越大型通用模型。研究者利用医学教科书语料库，通过 QLoRA 技术对 Mistral 7B Instruct 进行微调，并结合检索增强生成（RAG）层（采用 BGE 嵌入和 FAISS 向量库）。在 182 个留出问题的测试中，PAG-Health-LL...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A unified 12-lead ECG-language model for interpretation and clinical-endpoint prediction](https://www.medrxiv.org/content/10.64898/2026.07.22.26358591v1)
  来源：medRxiv | 日期：2026-07-24 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：自动心电图（ECG）解释目前多局限于固定标签分类，难以生成临床所需的叙述性报告。本研究提出 DeepECG-Tok，将 12 导联 ECG 解释重构为统一的指令遵循问题。该模型采用残差向量量化分词器（QINCo）将连续波形映射为与大语言模型（LLM）兼容的离散标记。实验显示，其冻结嵌入在 77 种疾病分类任务中达到了 0.96 的宏平均 AUROC，优于现有基线。通过 727 万个问答对进行指令微调，模型可执行 ECG 解释、结构化报告...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MedKGent: A Large Language Model Agent Framework for Constructing Temporally Evolving Medical Knowledge Graph](http://arxiv.org/abs/2508.12393v3)
  来源：arXiv | 日期：2025-08-17 | 相关度：6.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：医学文献的快速增长对领域知识的规模化结构化提出了挑战。知识图谱（KG）虽是解决方案，但现有构建方法缺乏泛化性，且忽略了知识随时间演变的动态特性。为此，我们提出了 MedKGent，这是一个用于构建随时间演变的医学知识图谱的大语言模型（LLM）智能体框架。利用 1975 年至 2023 年间的 1000 多万份 PubMed 摘要，MedKGent 通过两个专业智能体实现每日增量构建：提取智能体（Extractor Agent）负责识别知...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Towards Trustworthy and Cost-Efficient Data Integration: From Naïve RAG to Agentic RAG](http://arxiv.org/abs/2607.22319v1)
  来源：arXiv | 日期：2026-07-24 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：大语言模型（LLMs）和 AI Agent 在零样本和少样本数据集成中展现了巨大潜力，但在企业环境中仍面临准确性和成本挑战。本文提出通过检索增强生成（RAG）工作流中的知识驱动型 LLMs 和 Agent 实现可靠、可扩展且经济高效的数据集成。这里的“可靠性”指基于证据的可验证推理，即集成决策由检索到的知识透明支撑，具备抗幻觉能力和任务一致性。文章追踪了从经典 RAG 到 GraphRAG 和 KG-RAG（基于知识图谱的 RAG）的演...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [IDEAgent: Agentic Quality-Diversity Search for Research Idea Generation](http://arxiv.org/abs/2607.22375v1)
  来源：arXiv | 日期：2026-07-24 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：大语言模型（LLMs）在自动化科学发现方面取得了显著进展，但现有系统通常独立优化想法的“质量”或“多样性”，导致生成的想法要么彼此雷同，要么包含大量平庸、不合理或模糊的概念。本文提出 IDEAgent，一个将科研构思视为“质量-多样性”（QD）搜索任务的多智能体框架。该框架通过谱系管理想法的演化：利用多目标反馈进行专门的修复和改进以提升质量；通过轻量级序列记忆以及与历史祖先、已完成想法和被拒绝提案的显式对比来确保多样性。为系统评估 QD...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [GoMA-DTA: A Gene Ontology-Guided Multimodal Attention Fusion Model for Drug-Target Affinity Prediction.](https://pubmed.ncbi.nlm.nih.gov/42497056/)
  来源：PubMed | 日期：2026-07-24 | 相关度：7.1 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：准确预测药物-靶点亲和力（DTA）对加速药物研发至关重要。尽管预训练蛋白质语言模型已取得显著进展，但现有方法多侧重于自下而上的序列模式，缺乏高层生物功能的显式约束。本研究提出 GoMA-DTA 框架，将基因本体（GO）功能注释与蛋白质语义特征相结合。该模型引入通道门控机制，以功能语义为锚点动态校准 ESM-2 嵌入，实现自适应语义过滤。在药物表征方面，整合了基于 Molformer 的语义特征和 TransConv 提取的结构特征。这些...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Clinical Impact, Diagnostic Performance, and Prognostic Implications of Plasma Metagenomic Next-Generation Sequencing in Solid Organ Transplant Recipients](https://www.medrxiv.org/content/10.64898/2026.07.02.26357172v2)
  来源：medRxiv | 日期：2026-07-24 | 相关度：8.1 | 新颖度：0.75
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Background: Plasma metagenomic next-generation sequencing (mNGS) may detect pathogens in solid organ transplant (SOT) recipients, but optimal patient selection and result interpretation remain uncertain. Methods: We stud...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Teachy Mini: Development and Preliminary Evaluation of a Knowledge-Based Generative Social Robot for Higher Education](http://arxiv.org/abs/2607.22345v1)
  来源：arXiv | 日期：2026-07-24 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：生成式社交机器人（GSR）为高等教育个性化辅导带来了新机遇，但也存在误导信息、透明度缺失及强化错误回答等风险。本研究基于知识驱动设计（KBD）需求，在 Reachy Mini 机器人平台上通过系统提示词、检索增强生成（RAG）和状态化提示词编排，开发了名为 Teachy Mini 的 GSR 辅导系统。为评估该系统，研究开展了一项初步实验，24 名参与者分别使用 Teachy Mini 或未遵循 KBD 原则的对照组机器人学习研究方法论...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Human cornea harbors tissue-resident memory T cells shaped by systemic immune activation, age and biological sex](https://www.biorxiv.org/content/10.64898/2026.07.20.739463v1)
  来源：bioRxiv | 日期：2026-07-24 | 相关度：4.05 | 新颖度：5.25
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：传统观点认为角膜是免疫赦免组织，但近期研究在健康人类角膜中发现了特定病原体缺失（SPF）小鼠所不具备的T细胞。本研究结合多模态人类数据与小鼠模型，表征了角膜免疫监视的细胞基础。通过对临床非炎症人类供体组织进行免疫荧光染色和共聚焦成像，在角膜上皮中发现了CD3+ T细胞。流式细胞术证实这些细胞主要是具有组织驻留记忆T（TRM）细胞表型的CD8+细胞。活体共聚焦显微镜显示，角膜T细胞丰度随年龄增长而增加，且在男性中更为显著，表明其积累受累积...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic AI for Bilevel Long-Term Optimization of Policy-Driven Physical Layer Systems](http://arxiv.org/abs/2606.24416v2)
  来源：arXiv | 日期：2026-06-23 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：针对网络运营商政策变化、业务需求及严苛实时约束导致固定目标优化方法失效的问题，本文提出了一种名为“智能体长期性能优化”（Agentic-LTPO）的嵌套双层优化框架，用于自适应物理层问题配置。该框架的核心在于利用智能体AI（Agentic AI）在双层结构中生成上层配置，将演进的运营商政策、环境摘要和历史经验转化为结构化的下层优化问题参数；下层则利用更新的配置进行实时物理层决策。研究以无小区MIMO波束赋形为应用场景，在上层设计了具有检...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [SURE-RAG: Sufficiency and Uncertainty-Aware Evidence Verification for Selective Retrieval-Augmented Generation](http://arxiv.org/abs/2605.03534v2)
  来源：arXiv | 日期：2026-05-05 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）虽能利用检索段落提供依据，但相关性并不等同于充分性：相关段落可能仍不足以证明答案。本研究针对选择性RAG回答中的证据充分性验证展开研究，即验证器需根据问题、候选答案及检索证据，判断证据是支持、反驳还是不足以支撑答案，且仅在支持关系确立时才给出回答。我们提出了SURE-RAG聚合协议，将证据充分性视为集合级属性，解决了独立评分无法检测多跳缺失或逻辑冲突的问题。该协议通过共享的声明-证据验证器生成局部关系分布，并聚合为...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 其他

- [LAMAR: An Open Language-Aware Multilingual Alignment Reranker](http://arxiv.org/abs/2607.22042v1)
  来源：arXiv | 日期：2026-07-24 | 相关度：2.05 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：在多语言检索增强生成（RAG）中，检索器会获取多种语言的相关文档，并在生成答案前对其进行重排序。然而，现有重排序器在处理语义相关的候选文档时，是否考虑了文档语言对生成质量的影响尚不明确。研究发现，即使存在语义等效的跨语言文档，现有模型也无法一致地优先选择与查询语言相同的文档。为此，本研究推出了 LAMAR，这是一种兼顾语义相关性和语言一致性的语言感知多语言交叉编码器。LAMAR 首先采用“以英语为锚点的相关性蒸馏”技术，在多语言输入中建...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。
