# 每日论文监控日报 (2026-05-15)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 18 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：429 Client Error: Too Many Requests
- PubMed：成功，命中 70 篇
- bioRxiv：成功，命中 17 篇
- medRxiv：成功，命中 12 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [Retrieval-Augmented Claude Opus 4.7 and GPT-5.5 Surpass Human Performance on the Nuclear Cardiology Board Preparation Exam (and Claude Drafts a Paper About it)](https://www.medrxiv.org/content/10.64898/2026.05.08.26352768v1)
  来源：medRxiv | 日期：2026-05-13 | 相关度：7.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Background - Previous studies evaluated large language model (LLM) performance on the American Society of Nuclear Cardiology (ASNC) Board Preparation Exam. Without domain-specific context, the best model (GPT-4o) achieve...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Shaping the future of postoperative recurrence in Crohn's disease: personalised approaches with AI-enabled imaging and multi-omics.](https://pubmed.ncbi.nlm.nih.gov/41592952/)
  来源：PubMed | 日期：2026-05-12 | 相关度：9.7 | 新颖度：0.5
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Postoperative recurrence (POR) is a major challenge in the long-term management of Crohn's disease (CD), affecting up to 70% of patients within the first year after surgical resection. The multifactorial pathogenesis of ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ConvergeCELL: An end-to-end platform from patient transcriptomics to therapeutic hypotheses](https://www.biorxiv.org/content/10.64898/2026.05.07.723555v1)
  来源：bioRxiv | 日期：2026-05-12 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Translating transcriptomic data into therapeutic hypotheses remains fragmented and labor-intensive. Here we present ConvergeCELL, a platform combining a patient representation model trained on over 20 million cells acros...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Identification of race-specific QTL and candidate genes for Aphanomyces root rot resistance in alfalfa (Medicago sativa L.).](https://pubmed.ncbi.nlm.nih.gov/42132231/)
  来源：PubMed | 日期：2026-05-14 | 相关度：6.75 | 新颖度：5.25
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：Aphanomyces root rot (ARR), caused by the oomycete Aphanomyces euteiches, is one of the most devastating diseases of alfalfa in the United States. Two pathogenic races of A. euteiches have been identified, with most comm...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Unified sampling framework and experimental benchmarking of sequence- and structure-based protein models](https://www.biorxiv.org/content/10.64898/2026.05.08.723784v1)
  来源：bioRxiv | 日期：2026-05-12 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：生成模型在蛋白质设计中应用日益广泛，但缺乏标准化评估框架限制了不同模型间的比较及实验转化。本研究提出了一个统一的采样与基准测试框架，支持对比对模型、蛋白质语言模型（PLM）和基于结构的模型进行受控序列生成，并将其应用于烟草蚀刻病毒（TEV）蛋白酶。在数十万个设计序列中，不同模型探索了不同的序列空间，且缺乏明确的计算选择指标来评估酶功能。实验评估显示，功能结果差异巨大，涵盖了从无功能变体到活性比野生型高9倍的序列。机器学习设计的文库命中率...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Artificial Intelligence for Colorectal Surgeons - Part II: Research Applications, Challenges in Adoption and Practical Resources.](https://pubmed.ncbi.nlm.nih.gov/42117468/)
  来源：PubMed | 日期：2026-05-12 | 相关度：7.8 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：This is Part II of a two-part series examining artificial intelligence (AI) in colorectal surgery. Part I established foundational concepts and clinical applications. Implementation, however, requires understanding resea...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Multi-omics precision diagnosis of brucellosis: Advances in biomarker discovery and clinical application.](https://pubmed.ncbi.nlm.nih.gov/42128325/)
  来源：PubMed | 日期：2026-05-12 | 相关度：7.4 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：Brucellosis, a neglected zoonosis caused by intracellular Brucella bacteria, remains a formidable global public health challenge, especially in developing regions. The notorious ability of Brucella to evade host immunity...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [A transformer model explaining mechanisms of drug therapeutic and adverse effects](https://www.medrxiv.org/content/10.64898/2026.05.11.26352917v1)
  来源：medRxiv | 日期：2026-05-13 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：了解药物改变哪些疾病基因有助于揭示其药理机制、理解药物不良反应并发现新的药物用途。本研究在前期 Draphnet 模型的基础上提出了新一代模型 DraPhormer。Draphnet 最初旨在通过学习连接药物与其所改变的疾病基因的网络，来解释药物的治疗效果和副作用。DraPhormer 延续了这一目标，但将原有的线性模型替换为 Transformer 架构。该模型整合了药物分子数据、疾病遗传学信息以及已知的药物-疾病效应，并利用语言模型...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [An fMRI dataset of verbalized spontaneous thought with annotated transcripts and self-report trait measures](https://www.biorxiv.org/content/10.64898/2026.05.12.724488v1)
  来源：bioRxiv | 日期：2026-05-12 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：自发思维在人类日常认知中普遍存在，但在极小干扰条件下捕捉其神经动力学的数据集仍较稀缺。本研究公开了一项大声朗读式功能磁共振成像（fMRI）数据集，记录了118名参与者在10分钟扫描任务中持续口述自发思维的过程。在前期研究基础上，本次发布新增了预处理后的MRI数据、与图像采集对齐的词级时间戳语音转录、由大语言模型（LLM）生成的思维情感与感官维度评分，以及关于人格、心理健康和认知能力的自我报告调查量表。验证分析显示，与言语产生和感官内容相...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multimodal predictions of end stage chronic kidney disease from asymptomatic individuals for discovery of genomic biomarkers.](https://pubmed.ncbi.nlm.nih.gov/42120994/)
  来源：PubMed | 日期：2026-05-12 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：慢性肾脏病（CKD）影响全球约10%的人口，且在早期往往难以察觉。本研究利用英国生物样本库（UKBB）构建了一个包含46,986名具有基因组、临床和人口统计学数据患者的CKD队列，其中2,151名子集成员拥有全身磁共振成像（MRI）扫描数据。研究利用该多模态队列，成功对最初健康的个体进行了5年内终末期肾病（ESRD）风险预测（n=210，5折交叉验证AUC为0.804±0.03），并在大队列中验证了发病时间预测及全基因组关联分析（GWA...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ClaroAI-Bench: Evaluating Agentic Scientific Reproducibility on Real Biomedical Papers](https://www.biorxiv.org/content/10.64898/2026.05.08.723611v1)
  来源：bioRxiv | 日期：2026-05-12 | 相关度：1.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：本文介绍了 ClaroAI-Bench，这是一个用于评估 AI Agent 重现生物医学研究计算结果能力的基准测试套件。该基准包含 35 篇受 NIH 资助的真实论文，涵盖基因组学、影像学、临床/EHR、流行病学和湿实验五大领域。评估体系包含五个维度：数据可发现性（D1）、可访问性（D2）、代码可用性（D3）、环境可重构性（D4）和结果可重现性（D5）。任务要求 Agent 完成从定位数据、获取代码、重建环境到执行分析并验证结论的全流程...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Task-Specialized Protein Language Models Decode the Sequence Grammar of Post-Translational Modification Sites](https://www.biorxiv.org/content/10.64898/2026.05.08.723918v1)
  来源：bioRxiv | 日期：2026-05-12 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：翻译后修饰（PTMs）调节蛋白质信号传导、定位、降解及细胞决策，但在蛋白质组范围内区分可修饰残基与化学性质合格但未修饰残基的序列决定因素仍难以解码。本研究探讨了将通用蛋白质语言模型适配于 PTM 位点预测是否能揭示残基水平修饰的生化逻辑。研究人员针对磷酸化、乙酰化和泛素化位点预测，对在数千万个进化多样化蛋白质序列上训练的 ESM2 模型进行了微调。为解决蛋白质组范围内 PTM 注释中固有的严重类别不平衡问题，研究结合了参数高效微调（PE...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Hybrid Neural--Bayesian Belief Network Framework for Uncertainty-Aware Multimodal GBM Prediction](https://www.medrxiv.org/content/10.64898/2026.05.10.26352710v1)
  来源：medRxiv | 日期：2026-05-13 | 相关度：2.05 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：胶质母细胞瘤（GBM）的预后预测因临床信号分布在异质的影像和基因组模态中、样本量小且传统神经预测模型缺乏不确定性量化而具有挑战性。本研究评估了一种混合神经-贝叶斯信念网络（BBN）框架，用于不确定性感知的多模态GBM预测。研究利用TCGA-GBM放射基因组队列，涵盖四种输入模态（T1Gd、FLAIR、mRNA和CNA），对比了五种模型家族、五种结构权重设置和15个视图子集。结果显示，CNA特征在多数多模态设置中降低了性能，排除CNA的选...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Evaluating Genomic Surveillance Methods for Shigella sonnei in a High-Income Setting](https://www.medrxiv.org/content/10.64898/2026.05.08.26352707v1)
  来源：medRxiv | 日期：2026-05-12 | 相关度：6.0 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：索氏志贺氏菌（Shigella sonnei）是具有极低感染剂量且耐药性不断增强的人类适应性肠道病原体。在高收入地区，其传播模式包括与食物/旅行相关的散发病例，以及在男男性行为者（MSM）网络中的持续传播。本研究利用2016年至2022年间的英国监测数据集（n=3,639个分离株），评估了多种全基因组测序（WGS）分型方法在区分暴发株中的表现。对比方法包括：现行的10 SNP距离聚类（t10）、基于等位基因的cgMLST/HierCC ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Spatially Resolved Banff Tubulitis and Glomerulitis Scoring in Kidney Allograft Biopsies via Artificial Intelligent-Based Structure Segmentation and Spatial Transcriptomics](https://www.biorxiv.org/content/10.64898/2026.05.08.723594v1)
  来源：bioRxiv | 日期：2026-05-12 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：肾小管炎和肾小球炎分别是T细胞介导排斥反应（TCMR）和抗体介导排斥反应（AMR）的关键组织学特征，但传统的Banff评分存在观察者间差异，且大体转录组缺乏空间分辨率。本研究应用基于机器学习的FUSION平台，对8例肾移植活检样本（包括急性TCMR、活动性AMR、慢性活动性AMR及对照组各2例）进行分析。该平台整合了10x Genomics Visium v2空间转录组数据与高分辨率全切片图像。研究利用AI分割肾小管和肾小球区域，并结合...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Large-scale molecular epidemiological survey of Giardia and Cryptosporidium in Victoria, Australia (2020-2024), reveals novel subtypes and outbreak-associated lineages.](https://pubmed.ncbi.nlm.nih.gov/41891669/)
  来源：PubMed | 日期：2026-05-13 | 相关度：3.65 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：贾第鞭毛虫和隐孢子虫是全球胃肠道疾病的主要病因。本研究对 2020 年至 2024 年间澳大利亚维多利亚州腹泻患者的 2,330 份粪便样本进行了分子流行病学调查。通过对隐孢子虫（SSU 和 gp60 基因）和贾第鞭毛虫（tpi 基因）进行测序并估算寄生虫载量，共检出 225 份隐孢子虫阳性样本和 9 份贾第鞭毛虫阳性样本。结果显示，人隐孢子虫（C. hominis）占主导地位（85%），其次是微小隐孢子虫和火鸡隐孢子虫。研究识别出 7...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Beyond data and technology: the need for new thinking to enable the era of precision prevention.](https://pubmed.ncbi.nlm.nih.gov/42135719/)
  来源：PubMed | 日期：2026-05-14 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：全球旗舰计划日益倡导主动健康维护，以减轻反应性、以疾病为中心的医疗系统负担。精准预防被构想为对从潜在风险、疾病前期到临床表现的整个疾病连续体中因果路径的有针对性调节，超越了优先管理群体风险因素的传统公共卫生策略。然而，传统的发现和实施模式与科技进步的速度和广度并不匹配。本综述概述了扩展精准预防的主要障碍，并主张将概念、方法和政策视角整合到一个以实施为导向的框架中。个体化风险分层是精准预防的核心：基因组学作为终身易感性评估的基础，而多因素...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Three Decades of FDA Authorizations of AI/ML Enabled Medical Devices: Persistent Specialty Concentration and the Care Delivery Gap (1995 to 2025)](https://www.medrxiv.org/content/10.64898/2026.05.08.26352766v1)
  来源：medRxiv | 日期：2026-05-12 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：本研究对1995年9月至2025年12月期间获得美国FDA上市授权的所有1,430项人工智能/机器学习（AI/ML）赋能医疗器械进行了横断面分析，旨在表征其增长趋势、专业分布及制造商集中度。结果显示，年度授权量从1995-2014年间的年均1.8项激增至2023-2025年间的年均264项，仅2025年就记录了331项。在专业分布上，放射科专家组评审的器械达1,094项，占比76.5%；放射、心血管和神经科前三大专业合计占比90.6%。...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
