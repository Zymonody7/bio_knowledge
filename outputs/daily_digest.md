# 每日论文监控日报 (2026-07-12)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 29 篇新论文。

## 抓取状态

- arXiv：成功，命中 14 篇
- PubMed：成功，命中 54 篇
- bioRxiv：成功，命中 17 篇
- medRxiv：成功，命中 10 篇

## 最值得看

### Foundation Model / Agent

- [Automatic prompt engineering using multimodal large language models for the analysis of biological research images.](https://pubmed.ncbi.nlm.nih.gov/42431798/)
  来源：PubMed | 日期：2026-07-10 | 相关度：8.9 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are being applied across diverse fields due to their capability to derive various insights from complex data. In biotechnology, where complex multimodal data including images is rapidly expan...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [A five-dimensional functional state space for fingerprinting disease transcriptomes](https://www.biorxiv.org/content/10.64898/2026.07.04.736469v1)
  来源：bioRxiv | 日期：2026-07-09 | 相关度：7.55 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：High-throughput transcriptomics has transformed disease biology, but its outputs often remain fragmented into gene and pathway lists that are difficult to compare across conditions or use for human-AI interpretation. We ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [A multimodal foundation model for emergency head CT interpretation](https://www.medrxiv.org/content/10.64898/2026.07.07.26357429v1)
  来源：medRxiv | 日期：2026-07-09 | 相关度：8.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Non-contrast head CT is the first-line imaging modality for acute neurological emergencies, with demand rising worldwide. However, existing foundation models for head CT interpretation are ill-suited for emergency use be...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [NigBench: A multilingual point-of-care medical query benchmarking study of large language models in Nigeria](https://www.medrxiv.org/content/10.64898/2026.07.05.26356776v1)
  来源：medRxiv | 日期：2026-07-10 | 相关度：7.8 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：In this study, we introduce a novel benchmark comprising over 9,000 real-world, point-of-care, multilingual, and multimodal clinical question-answer pairs sourced from frontline health workers in Nigeria. Using the datas...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Autonomous biomedical research with an artificial intelligence agent.](https://pubmed.ncbi.nlm.nih.gov/42424436/)
  来源：PubMed | 日期：2026-07-09 | 相关度：6.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Biomedical research is increasingly constrained by repetitive, fragmented workflows that slow discovery. We introduce Biomni, a general-purpose biomedical artificial intelligence agent that autonomously executes diverse ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Automated Interpretation of EEG Reports Using a Large Language Model with Structured Confidence Outputs](https://www.medrxiv.org/content/10.64898/2026.07.07.26357190v1)
  来源：medRxiv | 日期：2026-07-10 | 相关度：7.55 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Background: Free-text EEG reports typically lack structure, hindering scalable analysis. We evaluate a large language model (LLM) pipeline to extract structured diagnostic labels and confidence levels from these reports....
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [DrugGen 2: A disease-aware language model for enhancing drug discovery](http://arxiv.org/abs/2607.08404v1)
  来源：arXiv | 日期：2026-07-09 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Current computational approaches for drug design typically focus on generating molecules conditioned on specific targets or general molecular properties, often neglecting the influence of disease context on target behavi...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Assessing AI and Neurologist Diagnostic Reasoning Against Neuropathological Ground Truth](https://www.medrxiv.org/content/10.64898/2026.07.07.26356930v1)
  来源：medRxiv | 日期：2026-07-10 | 相关度：7.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：BACKGROUND Accurate differential diagnosis of complex neurological disorders remains challenging due to overlapping clinical features and heterogeneous disease presentations. Although large language models (LLMs) show pr...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Expanding the Landscape of Disordered Flexible Linkers: A Structural and Computational Framework for DLD dataset assembly](https://www.biorxiv.org/content/10.1101/2025.10.26.684646v2)
  来源：bioRxiv | 日期：2026-07-09 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Disordered flexible linkers (DFLs) are functional elements found within intrinsically disordered regions that carry out key functions by connecting domains and/or short linear motifs. Understanding the features of DFLs i...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Thematic Shifts in Early-High-Impact Cancer Genomics and Diagnostics Research: A Bibliometric and Semantic Analysis](https://www.biorxiv.org/content/10.64898/2026.07.04.736459v1)
  来源：bioRxiv | 日期：2026-07-09 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Cancer genomics and diagnostics is a rapidly evolving field in which identifying which topics attract early citation prominence can inform laboratory investment, clinical translation, and research strategy. We developed ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Learning the shared structure of human health across diseases, modalities, and time](https://www.medrxiv.org/content/10.64898/2026.07.07.26357373v1)
  来源：medRxiv | 日期：2026-07-09 | 相关度：7.1 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：AO_SCPLOWBSTRACTC_SCPLOWHuman disease risk emerges from the shared influences of genetics, environment, lifestyle, and concurrent diseases over time, resulting in recurring patterns of susceptibility across conditions. H...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [The Dayhoff Atlas: scaling sequence diversity for improved protein generation](https://www.biorxiv.org/content/10.1101/2025.07.21.665991v2)
  来源：bioRxiv | 日期：2026-07-09 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Modern biology is powered by the organization of biological information, a framework pioneered in 1965 by Margaret Dayhoff's Atlas of Protein Sequence and Structure. Databases descended from this common ancestor power co...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Automated Phenotypic Characterization in Rare Hematologic Malignancies Using a Large Language Model-Based Framework](https://www.medrxiv.org/content/10.64898/2026.06.26.26356633v1)
  来源：medRxiv | 日期：2026-07-09 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Background. Diagnosis and risk stratification in rare hematologic malignancies such as myeloproliferative neoplasms (MPNs) - polycythemia vera (PV), essential thrombocythemia (ET), and myelofibrosis (MF) - require expert...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Resolving Complex Structural Variants in Undiagnosed Rare Movement Disorders via Multimodal Genomics and Multi-omics.](https://pubmed.ncbi.nlm.nih.gov/42421598/)
  来源：PubMed | 日期：2026-07-09 | 相关度：6.9 | 新颖度：1.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Long-read sequencing and multi-omic analytical frameworks are increasingly being adopted in rare disease diagnostics. However, clinical workflows comprehensively integrating these methodologies remain uncommon. This stud...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Cognitive-structured Multimodal Agent for Multimodal Understanding, Generation, and Editing](http://arxiv.org/abs/2607.08497v1)
  来源：arXiv | 日期：2026-07-09 | 相关度：6.1 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Recent unified multimodal models show a single architecture can jointly perform vision/language understanding and image generation/editing. However, they repeatedly feed all historical visual and textual inputs into a sh...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Decoding cancer circulating transcriptomic signatures with language models.](https://pubmed.ncbi.nlm.nih.gov/42425994/)
  来源：PubMed | 日期：2026-07-09 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Current liquid biopsy methods for multi-cancer detection using plasma cell-free RNA (cfRNA, short RNA fragments circulating in blood that can reflect disease states) typically rely on gene annotations, which can overlook...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Distill Where the Student Goes: Teacher-Regularized RL for English-Evidence Cross-Lingual RAG](http://arxiv.org/abs/2607.02966v2)
  来源：arXiv | 日期：2026-07-03 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：跨语言检索增强生成（RAG）常采用“英语证据”模式，即用户使用多种语言提问，但检索到的参考资料为英文。在这种设定下，即使是强大的基础模型也常面临语言漂移（输出英文或中英混杂）及证据利用不可靠的问题。本文将这些失败归因于训练后的两大挑战：前缀依赖性错误导致固定轨迹监督存在前缀不匹配，以及序列级奖励导致信用分配噪声大且更新方差高。为此，研究者提出了 TR-RAG，一种教师正则化的强化学习（RL）方案，将奖励优化与学生模型访问前缀的在线蒸馏相...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Game Theory Driven Multi-Agent Framework Mitigates Language Model Hallucination](http://arxiv.org/abs/2607.08403v1)
  来源：arXiv | 日期：2026-07-09 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：轻量级大语言模型在基于规则的科学领域应用受限，主要归因于其倾向于模仿语言模式而非重现公理化推理，从而导致频繁的幻觉。本研究提出了 G-Frame，这是一种集成贝叶斯和团队博弈原理的自适应多智能体框架，构建了高质量数据合成与模型训练的自动化闭环。通过结构化推理强制模型内化领域约束，研究者合成了一个包含 363,045 条思维链（CoT）和 199,589 个问答对的专业语料库。基于此开发的 7B 参数模型 OmniChem 在自定义基准测...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Truncated Step-Level Sampling with Process Rewards for Retrieval-Augmented Reasoning](http://arxiv.org/abs/2602.23440v4)
  来源：arXiv | 日期：2026-02-26 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：强化学习已成为训练大语言模型（LLM）交替进行推理与搜索引擎调用的有效范式。然而，现有方法面临严重的信用分配问题：如 Search-R1 等方法仅对多步轨迹分配单一结果奖励，无法明确具体推理或检索决策对成败的贡献；StepSearch 虽然引入步骤级监督，但仍独立采样完整轨迹，导致优势估计受随机性干扰。本文提出 SLATE（截断步骤级探索优势估计），通过两项核心创新解决上述问题。首先，截断步骤级采样从共享前缀生成 k 个后续步骤，将变异...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Artificial intelligence (AI) as a catalyst for mechanistic target discovery: Integrating systems pharmacology and multimodal data.](https://pubmed.ncbi.nlm.nih.gov/42423609/)
  来源：PubMed | 日期：2026-07-09 | 相关度：4.45 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：人工智能（AI）正从单纯的预测工具演变为机制驱动药理学的基础计算设施，从根本上重塑药物研发。本综述探讨了通过整合网络药理学与先进深度学习架构，如何解决靶点验证中长期存在的数据偏差和模型可解释性挑战。具体而言，图神经网络（GNN）用于解码生物系统的复杂拓扑结构，Transformer模型促进了从基因组学到真实世界临床记录的多模态数据融合。结合物理信息神经网络（PINN），该集成框架构建了预测性“计算显微镜”，支持跨越原子级分子相互作用到纵...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [NEP89: Universal neuroevolution potential for inorganic and organic materials across 89 elements](http://arxiv.org/abs/2504.21286v3)
  来源：arXiv | 日期：2025-04-30 | 相关度：2.4 | 新颖度：1.5
  匹配主题：未命中具体主题
  中文摘要：机器学习原子间势能模型虽能提供接近量子力学的精度，但往往受限于特定材料或高昂的计算成本。本文推出了 NEP89，这是一种基于神经进化势（NEP）架构的基础模型，涵盖了周期表中的 89 种元素。通过描述符空间子采样和跨多个数据集的迭代优化，研究者构建了一个涵盖无机和有机材料的紧凑且全面的训练集。实验表明，NEP89 在保持与现有代表性基础模型相当精度的同时，计算效率提升了 3 到 4 个数量级，从而实现了此前无法完成的百万原子级大规模模拟...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PolyUQuest: Verifiable Structure-Aware Web RAG over Heterogeneous Graphs](http://arxiv.org/abs/2607.08269v1)
  来源：arXiv | 日期：2026-07-09 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：现有的检索增强生成（RAG）系统通常将网页视为扁平文本，导致 HTML 中编码的结构和语义信号丢失。本文提出 PolyUQuest，一个基于异构图的可验证、结构感知型 Web RAG 框架。该框架统一了页面间的超链接拓扑、页面内的 DOM 层级以及跨页面的实体关系知识。通过两层路由机制，系统根据查询的结构需求将其分配至三种检索模式：直接块检索、跨页面图遍历和多跳实体推理。每个答案均具有完全的可验证性，引用的数据块均携带来源页面、标题路径...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Playing ZendoWorld: Challenging AI Agents on Active Visual Concept Induction](http://arxiv.org/abs/2607.08233v1)
  来源：arXiv | 日期：2026-07-09 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：构建智能系统的核心挑战是使 Agent 能够协同感知复杂输入、形成关于隐藏模式的假设，并设计信息丰富的实验进行验证。为此，我们提出了 ZendoWorld，这是一个受控的交互式环境，要求 Agent 推断视觉游戏观测背后的逻辑规则，通过提出新场景获取信息，并根据环境反馈完善假设。我们评估了包括纯 VLM 推理、贝叶斯粒子滤波、动态概念发现和神经符号方法在内的多种 Agent。主要发现如下：(1) 对观测样本标签的高预测准确率并不意味着掌...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [The Context Access Divide: Interaction-Level Architecture as a Complementary Dimension of Agentic Inequality](http://arxiv.org/abs/2607.08495v1)
  来源：arXiv | 日期：2026-07-09 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：本研究在 Sharp 等人（2025）提出的“智能体不平等”框架（包含可用性、质量和数量三个维度）基础上，引入了“上下文访问鸿沟”（CAD）这一补充维度。CAD 关注个体交互层面的结构性差异：即 AI 系统是能够从用户的知识库中自动检索上下文（动态上下文检索），还是需要用户在每次查询时手动识别并附加相关文档（手动附件）。对于拥有数万个文件等智力资本的知识密集型工作者，CAD 构成了 AI 效用的定性阈值。研究利用认知心理学中的“扇面效应...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Search Beyond What Can Be Taught: Evolving the Knowledge Boundary in Agentic Visual Generation](http://arxiv.org/abs/2607.05382v3)
  来源：arXiv | 日期：2026-07-06 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：视觉生成器在图像渲染方面表现出色，但常对未知知识进行虚假构建。由于用户需求具有无限性且处于动态演变中（如新角色、趋势实体、训练截止日期后的事件），生成器受限于固定训练语料，面临结构性的世界知识瓶颈。本研究构建了 SearchGen-20K 数据集和 SearchGen-Bench 基准，包含跨 12 个失败类别和 22 个领域的 20,839 条提示词，并配套了包含 100 万条记录的多模态 SearchGen-Corpus-1M 语料...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [ParamMute: Suppressing Knowledge-Critical FFNs for Faithful Retrieval-Augmented Generation](http://arxiv.org/abs/2502.15543v4)
  来源：arXiv | 日期：2025-02-21 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) integrated with retrieval-augmented generation (RAG) have improved factuality by grounding outputs in external evidence. However, they remain susceptible to unfaithful generation, where outpu...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Conversational Retrieval and On-the-Fly Knowledge Modeling of Historical Penitentiary Repression Records](http://arxiv.org/abs/2607.08459v1)
  来源：arXiv | 日期：2026-07-09 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：数字图书馆的最新进展日益倾向于通过检索增强生成（RAG）实现信息的对话式和自然语言访问。尽管这些方法在基于单条记录的抽取式任务中非常有效，但在整体解释文档集以及动态整合专家知识方面仍存在局限。本文提出了一种专为历史数字图书馆管理设计的文档分析系统，支持即时（on-the-fly）知识建模。该系统能够将专家档案管理员生成的事实或从文档检索过程中提取的事实存储在基于图（graph-based）的结构中。通过持续的专业交互，系统不仅能从原始文...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Combining pathology artificial intelligence and genomic biomarkers to refine long-term postprostatectomy outcome prediction.](https://pubmed.ncbi.nlm.nih.gov/42429593/)
  来源：PubMed | 日期：2026-07-10 | 相关度：3.75 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：本研究评估了一种多模态人工智能（MMAI）模型在预测前列腺癌根治术后长期预后中的价值。研究人员将原用于活检标本的 MMAI 模型应用于 424 例手术病例的组织微阵列（TMA），其中 414 例（98%）成功生成评分。通过 Cox 回归分析并校正前列腺癌风险评估（CAPRA）评分和基因组细胞周期进展（CCP）评分，评估其与生化复发（BCR）和转移的相关性。结果显示，10 年无复发和无转移生存率分别为 74% 和 96%。单变量模型中，M...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Bionic Magnetic Nanorobots Combined with AI-Assisted Microscopic Imaging for Argonaute-Powered Multiplexed Foodborne Pathogens Detection.](https://pubmed.ncbi.nlm.nih.gov/42429450/)
  来源：PubMed | 日期：2026-07-10 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：食源性致病菌的多重超灵敏鉴定对食品安全至关重要。然而，传统方法受限于复杂基质干扰、信号转换工具不足及灵敏度低等问题。本研究通过聚乙二醇（PEG）接头优化磁性纳米颗粒表面的苯硼酸密度，构建了仿生纳米机器人，在20分钟内实现了对革兰氏阳性菌92.21%的捕获率，且稳定性长达25天。此外，开发了一种基于聚苯乙烯微球尺寸编码和丁酸梭菌Argonaute（CbAgo）解码的人工智能（AI）辅助显微成像策略。经合理设计的CbAgo可激活循环切割电路...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
