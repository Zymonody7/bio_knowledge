# 每日论文监控日报 (2026-07-13)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 22 篇新论文。

## 抓取状态

- arXiv：成功，命中 9 篇
- PubMed：成功，命中 40 篇
- bioRxiv：成功，命中 11 篇
- medRxiv：成功，命中 5 篇

## 最值得看

### Foundation Model / Agent

- [Performance evaluation of five major large language models in tuberculosis Q&A systems: A multidimensional assessment of readability, quality, and reliability.](https://pubmed.ncbi.nlm.nih.gov/42436893/)
  来源：PubMed | 日期：2026-01-01 | 相关度：7.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Pulmonary tuberculosis (TB) is a chronic infectious disease that burdens patients and public health systems. Limited reach of traditional education and uneven online information may undermine patients' understanding, adh...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [Automatic prompt engineering using multimodal large language models for the analysis of biological research images.](https://pubmed.ncbi.nlm.nih.gov/42431798/)
  来源：PubMed | 日期：2026-07-10 | 相关度：8.9 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are being applied across diverse fields due to their capability to derive various insights from complex data. In biotechnology, where complex multimodal data including images is rapidly expan...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A multimodal foundation model for emergency head CT interpretation](https://www.medrxiv.org/content/10.64898/2026.07.07.26357429v2)
  来源：medRxiv | 日期：2026-07-10 | 相关度：8.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Non-contrast head CT is the first-line imaging modality for acute neurological emergencies, with demand rising worldwide. However, existing foundation models for head CT interpretation are ill-suited for emergency use be...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [NigBench: A multilingual point-of-care medical query benchmarking study of large language models in Nigeria](https://www.medrxiv.org/content/10.64898/2026.07.05.26356776v1)
  来源：medRxiv | 日期：2026-07-10 | 相关度：7.8 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：In this study, we introduce a novel benchmark comprising over 9,000 real-world, point-of-care, multilingual, and multimodal clinical question-answer pairs sourced from frontline health workers in Nigeria. Using the datas...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Toward Auditable AI Scientists: A Hypothesis Evolution Protocol for LLM Agents](http://arxiv.org/abs/2607.09195v1)
  来源：arXiv | 日期：2026-07-10 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large language model (LLM) agents are increasingly expected to play a central role in AI-driven scientific discovery. Equipped with broad knowledge, flexible reasoning, and tool use, they have the potential to autonomous...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Semantic fragment representations for coordinate-free analysis of genomics data](https://www.biorxiv.org/content/10.64898/2026.07.09.737627v1)
  来源：bioRxiv | 日期：2026-07-10 | 相关度：6.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Many genomic assays begin with individual DNA fragments, but standard analysis quickly collapses those molecules into counts over genomic intervals. Rich information carried by each fragment, including its sequence, frag...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Augmenting Fundamental Analysis with Large Language Models: A RAG-Based System for Generating Investor Briefs](http://arxiv.org/abs/2607.09121v1)
  来源：arXiv | 日期：2026-07-10 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：本研究探讨了大语言模型（LLMs）在公司基本面分析中的应用潜力。研究整合了公司年度报告、宏观经济指标（如GDP和通货膨胀变化）以及从美国证券交易委员会（SEC）EDGAR系统获取的监管文件。通过对这些多源数据进行预处理，研究采用检索增强生成（RAG）模式，将数据通过API发送至gpt-4o模型进行处理。此外，研究还引入了基于基钦周期（Kitchin cycles）的专业投资者知识文档以增强模型表现。在为期四周的实验中，系统持续扫描并分析...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Automated Interpretation of EEG Reports Using a Large Language Model with Structured Confidence Outputs](https://www.medrxiv.org/content/10.64898/2026.07.07.26357190v1)
  来源：medRxiv | 日期：2026-07-10 | 相关度：7.55 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Background: Free-text EEG reports typically lack structure, hindering scalable analysis. We evaluate a large language model (LLM) pipeline to extract structured diagnostic labels and confidence levels from these reports....
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Assessing AI and Neurologist Diagnostic Reasoning Against Neuropathological Ground Truth](https://www.medrxiv.org/content/10.64898/2026.07.07.26356930v1)
  来源：medRxiv | 日期：2026-07-10 | 相关度：7.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：BACKGROUND Accurate differential diagnosis of complex neurological disorders remains challenging due to overlapping clinical features and heterogeneous disease presentations. Although large language models (LLMs) show pr...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Interpretable variant effect prediction from genomic foundation model embeddings](https://www.biorxiv.org/content/10.64898/2026.04.10.717844v4)
  来源：bioRxiv | 日期：2026-07-11 | 相关度：8.35 | 新颖度：1.0
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Scientific foundation models learn high-dimensional representations from diverse data modalities, yet what they encode and how to extract that knowledge remain open questions. Here we show that probing the internal repre...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CellPilot: an agentic framework that pilots small language models through autonomous single-cell annotation](https://www.biorxiv.org/content/10.64898/2026.07.06.736807v1)
  来源：bioRxiv | 日期：2026-07-10 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models can annotate cell types from marker gene lists, but they typically operate after preprocessing and clustering are complete, treating annotation as a terminal labeling step rather than controlling th...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Autonomous computational prioritisation of colorectal cancer vulnerabilities via multi-scale AI swarms](https://www.biorxiv.org/content/10.64898/2026.07.05.736565v1)
  来源：bioRxiv | 日期：2026-07-10 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：自动化科学发现受限于大语言模型（LLM）的语义推理与复杂生物学现实之间的认识差距。本文提出多尺度自主发现引擎（Octopus），这是一个神经符号框架，结合了本地化、隐私保护的多智能体群（multi-agent swarm）与正则化预测算法环境。该系统不仅限于孤立的细胞实验，还能自主筛选针对CRISPR依赖性数据（CCLE）的治疗假设，利用XGBoost SHAP向量追踪特征归因级联，并将发现的脆弱点在计算机内转化为对体内肿瘤轨迹（PDX...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A Note on k-NN Gating in RAG](http://arxiv.org/abs/2601.13744v2)
  来源：arXiv | 日期：2026-01-20 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：本研究针对检索增强生成（RAG）提出了一种统计代理框架，旨在从数学层面形式化语言模型在内部先验预测与外部检索证据之间的权衡机制。研究推导出了一个最优的查询级门控（query-level gate）方案，用于动态调节检索信息的权重。通过引入“检索不一致性”（retrieval discordance）概念，该框架能够定量分析模型幻觉的产生原因，并对查询需求与存储记忆之间的不匹配（query-memory mismatch）进行建模。研究团...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Large Behavior Model: A Promptable Digital Twin of the Retail Customer](http://arxiv.org/abs/2607.06993v2)
  来源：arXiv | 日期：2026-07-08 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：客户行为建模是推荐、营销和决策支持的基础，但现有方法往往在优化预测准确性的同时缺乏决策解释性，或在模拟用户时脱离真实行为数据。本文提出大行为模型（LBM），通过统一的“人-环境”公式，直接从大规模零售交易中学习客户决策逻辑。该模型利用历史购买记录构建行为档案来表示客户状态，并通过检索增强生成（RAG）整合产品上下文。LBM 的训练流程包括：对语言化行为数据进行持续预训练、针对决策生成的监督微调（SFT），以及利用可验证奖励进行证据校准的...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Tokenizing single-cell transcriptomes as a native language for large language models](https://www.biorxiv.org/content/10.1101/2025.10.22.684047v2)
  来源：bioRxiv | 日期：2026-07-11 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：大语言模型（LLMs）能够处理多种形式的信息，前提是将其表示为共享序列空间中的 Token。然而，单细胞转录组由于是连续、高维的分子图谱而非离散语言单位，对 LLM 而言仍是异质模态。本研究提出了 CellTok，一种单细胞语言建模方法，将转录组图谱转换为紧凑的细胞 Token 序列，并将其整合进预训练 LLM 的词表。通过将细胞表示为原生 Token，CellTok 使得细胞测量值、文本指令、生物学上下文和多细胞群体能够在同一个自回归...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [SAGEAgent: A Self-Evolving Agent for Cost-Aware Modality Acquisition in Multimodal Survival Prediction](http://arxiv.org/abs/2607.09521v1)
  来源：arXiv | 日期：2026-07-10 | 相关度：2.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：在多模态临床肿瘤学中，诊断手段通常遵循临床规定的负担递增顺序，从基础的人口统计学信息到需要专门组织分析的基因组谱分析。当前的生存预测方法多假设模态完整或被动处理缺失数据，缺乏对是否需获取后续高负担模态的主动推理。本研究提出 SAGEAgent（基于经验引导的序列获取），这是一种基于大语言模型（LLM）的自进化临床智能体，旨在平衡预测准确性与临床侵入性。SAGEAgent 将模态获取建模为序列决策问题，通过临床工具将数值预测转化为文本，利...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Looking Locally: Object-Centric Vision Transformers as Foundation Models for Efficient Segmentation](http://arxiv.org/abs/2502.02763v3)
  来源：arXiv | 日期：2025-02-04 | 相关度：0.7 | 新颖度：6.75
  匹配主题：未命中具体主题
  中文摘要：当前主流分割模型在关注特定对象前需编码整幅图像，导致计算资源浪费。本研究提出 FLIP（类视网膜输入补丁），一种受生物启发、通过自上而下注意力实现目标分割的参数高效视觉模型。FLIP 从输入中选择性采样以目标为中心的多分辨率补丁，在保持粗糙外围上下文的同时，对目标中心进行高分辨率处理。这种离栅格、尺度不变的设计使 FLIP 性能显著超越 Meta 的 SAM 系列：仅含 0.51M 参数的 FLIP-Tiny 达到 79.90% mIo...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Deceptive Grounding: Entity Attribution Failure in Clinical Retrieval-Augmented Generation](http://arxiv.org/abs/2607.09349v1)
  来源：arXiv | 日期：2026-07-10 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）评估通常检查模型声明是否在检索文档中有事实依据，但往往忽略了证据是否归属于正确的实体。本研究定义了“欺骗性接地”（Deceptive Grounding, DG）：即临床 RAG 响应虽然通过了所有自动化检查（如零幻觉、高忠实度、真实引用），却将药物 Y 的临床证据误报为查询药物 X 的证据。通过对 13 个模型进行受控因子基准测试，发现在极端对抗条件下 DG 发生率介于 8-87% 之间。医学和生物医学微调模型表...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Community-driven advances in computational mass spectrometry: The perspective of EuBIC-MS members.](https://pubmed.ncbi.nlm.nih.gov/42436009/)
  来源：PubMed | 日期：2026-07-11 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：数据采集、人工智能和综合生物信息学的进步正推动计算质谱的快速演变，进而改变现代蛋白质组学、代谢组学和脂质组学。随着质谱数据规模和复杂性的增加，开发准确、透明、高效且可重复的数据处理流程至关重要。欧洲质谱生物信息学社区（EuBIC-MS）通过开发者会议和冬季学校促进开放的社区驱动开发。本文总结了2025年在意大利诺瓦切拉举行的EuBIC-MS开发者会议的成果。会议通过三大主题演讲探讨了深度蛋白质组与磷酸化组分析、用于蛋白质相互作用提取的文...
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

### 其他

- [The Powerless Noise: How Experimental Settings Shape the Reported Power of Noise](http://arxiv.org/abs/2607.03615v2)
  来源：arXiv | 日期：2026-07-03 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：近期研究提出在检索增强生成（RAG）系统的输入中加入无关文档可提升问答性能，这一现象被称为“噪声的力量”。本文复现了 Cuconasu 等人的主要研究结果，并在扩展实验设置下评估了该效应的稳健性。研究首先确认了在原始设置（采用早期 LLM、限制性提示词和受限解码设置）下该现象确实存在。随后，作者引入了一系列扩展实验以探究噪声效应的深层原因，包括测试不同模型、指令提示词以及放宽输出长度限制。消融实验表明，“噪声的力量”模式对推理配置高度敏...
  为什么值得看：The Powerless Noise: How Experimental Se 与你的主题有弱匹配，暂时保留作低优先级跟踪。
