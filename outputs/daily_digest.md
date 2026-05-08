# 每日论文监控日报 (2026-05-08)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 12 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：429 Client Error: Unknown Error
- PubMed：成功，命中 42 篇
- bioRxiv：成功，命中 16 篇
- medRxiv：成功，命中 8 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### 方法创新

- [STAT: A multi-agent framework for integrated and interactive spatial transcriptomics analysis](https://www.biorxiv.org/content/10.64898/2026.05.01.722244v1)
  来源：bioRxiv | 日期：2026-05-05 | 相关度：7.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：空间转录组学（ST）分析通常涉及跨平台的多种计算方法，导致研究人员在数据整合上耗费过多时间。目前的 AI 方案要么将空间数据过度简化为通用的单细胞表格，要么在缺乏中间审查的情况下自主运行，阻碍了空间生物学中至关重要的视觉和迭代分析。为此，我们开发了 STAT，一个多智能体（multi-agent）框架，旨在通过对话式交互提高空间分析的易用性，同时保持透明度和控制力。STAT 集成了持久会话、共享交互式组织查看器和分阶段技能感知流水线。在...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [Extracting adverse event nature, severity, timelines and resulting interventions from clinical notes of patients receiving CAR-T therapy using large language models.](https://www.medrxiv.org/content/10.64898/2026.04.28.26351782v1)
  来源：medRxiv | 日期：2026-05-05 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：嵌合抗原受体T细胞（CAR-T）疗法在血液肿瘤治疗中具有重要地位，但其不良事件（AE）通常仅记录在非结构化的电子健康记录（EHR）中。本研究在加州大学旧金山分校（UCSF）的安全环境下，评估了基于大语言模型（LLM）的方法，用于提取2012-2023年间293名患者（共4,762份病程记录）在CAR-T输注后30天内的AE、日期、分级及干预措施。研究使用GPT-4-0314在零样本（zero-shot）设置下，通过四种特定提示词提取信息...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multilingual Evaluation of a Large Language Model-Based Primary Care Chatbot](https://www.medrxiv.org/content/10.64898/2026.05.03.26352241v1)
  来源：medRxiv | 日期：2026-05-05 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：诊前计划具有减轻电子健康记录（EHR）记录负担并提高临床效率的潜力。本研究采用混合方法，系统评估了基于 GPT-4o 开发的临床聊天机器人 PCP-Bot 的多语言能力。该机器人旨在收集患者诉求并生成约 200 字的结构化医生摘要。研究招募了 31 名双语受试者（11 名中文、10 名西班牙语、10 名印地语），针对 5 个合成临床病例，分别使用英语和第二语言与机器人进行角色扮演互动。无论互动语言为何，生成的摘要均统一为英文。结果显示：...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [ChatIBD: design, safeguards, and early international use of a guideline-grounded generative AI tool for inflammatory bowel disease (IBD) professionals](https://www.medrxiv.org/content/10.64898/2026.05.06.26352526v1)
  来源：medRxiv | 日期：2026-05-07 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：本研究描述了ChatIBD的设计、运行保障及早期使用情况。ChatIBD是一个专为炎症性肠病（IBD）专业人士设计的生成式AI平台。该平台采用检索增强生成（RAG）技术，基于精选的IBD指南语料库进行问答。技术实现上，系统结合了混合语义与关键词检索、查询扩展及重排序，并强制模型仅依据检索到的材料回答并返回引用链接。安全保障措施包括集成欧洲药品管理局（EMA）的固定药物剂量信息、用户反馈捕获以及临床医生对标记输出的审查。在2025年10月...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Patient2Sentence: Large Language Model-based Semantic Compression for Oncology Trial Eligibility Screening](https://www.medrxiv.org/content/10.1101/2025.11.14.25340276v2)
  来源：medRxiv | 日期：2026-05-05 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：肿瘤临床试验招募效率受限于冗长且非结构化的电子健康档案（EHR）解读。本研究提出 Patient2Sentence (P2S) 框架，利用大语言模型将完整的肿瘤 EHR 语义压缩为简洁、标准化的自然语言“患者句子”，同时保留定义入组资格的关键临床逻辑。研究采用模拟 KATHERINE、MONARCH-E 和 OLYMPIA 乳腺癌试验的 75 份合成 EHR 进行验证，对比了基于全量临床叙述与仅基于压缩句子的入组判定。结果显示，基于压缩...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Structure-derived synthetic sequences guide a protein language model toward metalloproteins](https://www.biorxiv.org/content/10.64898/2026.04.30.722007v1)
  来源：bioRxiv | 日期：2026-05-05 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：蛋白质语言模型（pLMs）虽能捕捉进化序列约束，但受限于训练数据不平衡，难以建模金属蛋白等代表性不足的功能类别。本研究评估了结构约束的合成序列是否能引导 pLM 专门化于金属结合功能。研究者利用逆折叠模型 ProteinMPNN 生成合成序列，并对通用模型 ProtGPT2 进行微调，构建了具有受控规模和多样性的训练集。结果显示，微调将模型对经典金属结合基序的恢复率从基准模型的 43% 提升至 91%。生成的序列在保持低序列一致性的同时...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Interpreting Omics Data Analysis with Large Language Models for Disease Target and Drug Discovery](https://www.biorxiv.org/content/10.64898/2026.04.30.721768v1)
  来源：bioRxiv | 日期：2026-05-05 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：在生物医学发现中，整合文献先验知识对于解释数值组学数据以识别疾病靶点和药物至关重要。单纯的大语言模型（LLMs）虽能快速检索疾病机制，但由于缺乏队列特异性的定量证据，其输出在靶点和药物优先级排序上往往泛泛且不可靠。本研究提出了一种溯源感知的“Text-to-Target”框架，将模式约束的多模型LLM检索与数值组学数据分析相结合。核心设计是模态感知融合步骤：将候选对象划分为重叠支持的锚点、仅检索的隐藏枢纽和网络涌现的新颖节点，并在拓扑约...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [Effect of Large Language Models on P300 Speller Performance with Cross-Subject Training](https://www.biorxiv.org/content/10.1101/2025.10.28.685216v2)
  来源：bioRxiv | 日期：2026-05-05 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：肌萎缩侧索硬化症（ALS）会导致患者沟通能力迅速丧失，P300 拼写器脑机接口（BCI）通过追踪受试者对屏幕高亮字符的脑电图（EEG）反应将其转化为文本。本研究旨在解决多受试者分类器训练的局限性，并集成先进的大语言模型（LLM）以优化刺激呈现和单词预测，从而提高沟通效率。研究引入了三项创新：先进的多受试者分类器训练、评估多种 LLM 对拼写器性能的影响，以及利用“理想 LLM”确定性能边界。通过对随机采样的 EEG 数据进行大规模模拟，...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Systematic contextual biases in SegmentNT potentially relevant to other nucleotide transformer models](https://www.biorxiv.org/content/10.1101/2025.04.09.647946v2)
  来源：bioRxiv | 日期：2026-05-05 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：近期大语言模型（LLM）已扩展至基因组学领域，但模型相对于上下文的鲁棒性仍不明确。本研究揭示了影响 SegmentNT 结果的两种内在偏见：输入序列长度和核苷酸位置。SegmentNT 是 Nucleotide Transformer 框架下的一个模型，旨在提供生物特征的核苷酸级预测。研究证明，核苷酸在输入序列中的位置（开头、中间或结尾）会改变原始预测概率，而通过标准化处理可显著提高预测的一致性。虽然增加输入序列长度能提升模型性能，但边...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Multiscale brain-wide mapping of α-synuclein-driven dopaminergic degeneration and white matter impairment in α-synucleinopathy mice](https://www.biorxiv.org/content/10.64898/2025.12.05.692595v2)
  来源：bioRxiv | 日期：2026-05-05 | 相关度：2.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：本研究旨在阐明α-突触核蛋白（α-syn）包涵体形成、多巴胺能变性与白质微结构变化之间的时空关系。研究者向野生型小鼠的黑质致密部（SNc）单侧注射预制纤维体（PFFs）或单体α-syn，并在注射后12周和20周进行9.4T离体磁共振成像（MRI）以评估微结构、体积及顺磁性变化。同时，利用光片显微镜（LSM）在全脑范围内以单细胞分辨率映射α-syn聚集体和多巴胺能神经元。研究开发了一个基于Python的自动化配准流程，实现了离体MRI与L...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Autoencoder/RandomForest-TabPFN for Cross-Cancer Metabolomics: Prostate and Breast Cancer Diagnosis Using Paper Spray and Ion Mobility-Mass Spectrometry Techniques.](https://pubmed.ncbi.nlm.nih.gov/42096511/)
  来源：PubMed | 日期：2026-05-07 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：准确快速的疾病诊断对前列腺癌（PC）和乳腺癌（BC）的早期干预至关重要。本研究提出了一种整合自动编码器（Autoencoder）、基于随机森林（Random Forest）的特征选择和表格先验数据拟合网络（TabPFN）的新型预测方法，用于分析癌症代谢组学数据。研究利用纸喷雾电离质谱（PSI-MS）和流动注射-行波离子迁移质谱（FI-TWIM-MS）获取了PC患者的尿液和血清样本数据，以及BC患者穿刺活检的代谢和脂质组特征。结果显示，该...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Evaluating the Potential Impact of AI on Urinary Tract Infection Diagnosis in the Emergency Department Across Demographic Groups: Retrospective Cohort Study.](https://pubmed.ncbi.nlm.nih.gov/42090580/)
  来源：PubMed | 日期：2026-05-06 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：尿路感染（UTI）是急诊科（ED）的常见病，但存在严重的误诊和漏诊风险，尤其是老年群体。本研究开发了一种结合尿培养阳性预测与自然语言处理（NLP）的 AI 模型，仅利用患者就诊时的即时信息预测 UTI 诊断。研究对 2013 年至 2021 年间美国某医疗系统 9 个急诊科的 149,449 例非妊娠成年患者进行了回顾性分析。研究人员使用 Extreme Gradient Boosting（XGBoost）分类器预测尿培养阳性（≥10,...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
