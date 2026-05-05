# 每日论文监控日报 (2026-05-05)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 12 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='export.arxiv.org', port=443): Read timed out. (read timeout=60)
- PubMed：成功，命中 16 篇
- bioRxiv：成功，命中 11 篇
- medRxiv：成功，命中 4 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [Historical Perspectives in Medicine using a Large Language Model: Emulating an 18th Century Physician](https://www.medrxiv.org/content/10.64898/2026.02.10.26345990v2)
  来源：medRxiv | 日期：2026-05-04 | 相关度：7.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：18世纪医学文献记录了临床推理演变的关键时期，但其在现代医学教育中的整合程度有限。本研究开发了一个受历史约束的大语言模型（LLM）教育平台，旨在模拟18世纪医生的诊断推理、语言风格和概念框架。研究采用现代GPT架构，通过严格的指令约束，将其知识范围限制在精心挑选的6本17至18世纪基础医学著作中，并设置护栏以防止出现时代错误术语和现代医学概念。评估通过将模型的诊断和治疗方案与原始历史文献进行定性对比，并将其应用于现代临床案例以展示古今差...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [GENERator-v2: Reconciling Coarse Tokenization with Single-Nucleotide Resolution in Genomic Language Modeling](https://www.biorxiv.org/content/10.64898/2026.01.27.702015v2)
  来源：bioRxiv | 日期：2026-05-04 | 相关度：6.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：基因组基础模型旨在从DNA序列中学习通用表示，但在处理长程上下文、单核苷酸分辨率与计算效率的矛盾时面临挑战。本文提出了GENERator-v2，从训练目标和数据构建角度重新设计了长上下文基因组模型。研究引入了“分解核苷酸监督”（FNS）技术，通过概率边缘化将高效的k-mer分词与单核苷酸似然对齐；同时采用“基因组压缩预训练”（GCP），通过聚焦于基因中心和调控区域来重塑训练分布。这些技术使标准Transformer模型在不牺牲单核苷酸精...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Automation of Systematic Reviews with Large Language Models](https://www.medrxiv.org/content/10.1101/2025.06.13.25329541v4)
  来源：medRxiv | 日期：2026-05-04 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：系统综述（SR）是循证决策的核心，但其过程耗时且易出错。本研究验证了一种基于大语言模型（LLM）的工作流 otto-SR，旨在自动化文献筛选、数据提取和偏倚风险评估三项繁重任务。研究分四阶段进行：第一阶段在 32,357 条引文中测试，otto-SR 的筛选灵敏度（96.7%）显著优于人类研究员（81.7%）；第二阶段在 4,495 个数据点中测试，其提取准确率（93.1%）高于人类（79.7%）；第三阶段在偏倚风险评估（ROB2、Ne...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Can large language models approximate human perceptions of disease severity? An evaluation using Global Burden of Disease 2010 disability weights](https://www.medrxiv.org/content/10.64898/2026.05.02.26352261v1)
  来源：medRxiv | 日期：2026-05-04 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：伤残权重（DW）是衡量健康损失严重程度、估算全球疾病负担（GBD）中伤残调整寿命年的核心指标。传统 DW 估算依赖高成本的人口调查，难以快速更新。本研究评估了大型语言模型（LLM）通过结构化判断任务模拟人类对疾病严重程度感知的潜力。研究采用 GBD 2010 中的 222 种健康状态，利用 GPT-5 和 Claude 4.5 等四种模型进行了 24,531 对两两比较。结果显示，LLM 与 GBD 2010 DW 排名高度一致（Spe...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Do Larger Models Really Win in Drug Discovery?A Benchmark Assessment of Model Scaling in AI-Driven Molecular Property and Activity Prediction](https://www.biorxiv.org/content/10.64898/2026.04.29.721568v1)
  来源：bioRxiv | 日期：2026-05-04 | 相关度：4.75 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：本研究评估了分子基础模型与通用大语言模型在药物研发中的“规模中心论”假设，即大型预训练模型是否优于小型化学信息学模型和特定任务的图神经网络（GNN）。研究涵盖22个分子属性和活性终点，包括公开的ADMET、Tox21基准及两个内部抗感染数据集（包含49,266个抗结核和2,088个抗疟疾数据）。在167,056次基于结构相似性划分的五折交叉验证评估中，传统机器学习模型（如RF(ECFP4)和ExtraTrees）在10个主要指标任务中获...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [SARS-CoV-2 Nsp1 suppresses the canonical NF-κB pathway by promoting ubiquitin-dependent degradation of TAK1 kinase.](https://pubmed.ncbi.nlm.nih.gov/42081588/)
  来源：PubMed | 日期：2026-05-04 | 相关度：7.65 | 新颖度：5.25
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：SARS-CoV-2表达的免疫调节蛋白通过干扰宿主抗病毒防御，在COVID-19的发病机制中发挥关键作用。本研究通过整合预训练蛋白质语言模型（pLM）和免疫相关通路中的基因权重，建立了一种新型预测算法，用于量化SARS-CoV-2蛋白对宿主免疫系统的扰动。研究结果显示，经典NF-κB通路在病毒感染过程中受到动态调节，其中非结构蛋白1（Nsp1）能显著抑制由其他病毒蛋白或促炎细胞因子（如IL-1β）诱导的NF-κB通路激活。分子机制研究表...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Species-specific transformer models of bacterial gene order and content for genomic surveillance tasks](https://www.biorxiv.org/content/10.64898/2026.04.28.721069v2)
  来源：bioRxiv | 日期：2026-05-04 | 相关度：6.55 | 新颖度：1.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Transformer模型在生物数据表征方面表现出色，但通用大模型在特定领域任务中常被分类受限的模型超越。本研究针对细菌病原体流行病学分析，开发了物种特异性Transformer模型PanBART。该模型基于大肠杆菌（Escherichia coli）和肺炎链球菌（Streptococcus pneumoniae）的基因含量和基因顺序进行训练，并与最先进的非Transformer基因组流行病学方法进行了基准测试。结果显示，PanBART...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Performance of Large Language Models as a Tool for Primary Care Consultations: Evaluation Study](https://www.medrxiv.org/content/10.64898/2026.04.29.26352082v1)
  来源：medRxiv | 日期：2026-05-04 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：自2022年ChatGPT发布以来，大语言模型（LLMs）在处理健康咨询等敏感且重要的信息需求方面演进迅速。本研究旨在识别生成式AI系统在应对关键医疗健康信息时的核心优劣势。研究采用问答（Q&A）形式，将用户查询作为输入，模型生成的回答作为输出。评估框架由两组不同专业的临床专家组成，从三个维度进行评价：医疗共识遵循程度、是否存在不当或错误信息、以及对用户的潜在危害性。实验选取了GPT-4o mini、Llama 3和MedLlama 3...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [A 37-million-particle dataset from over 250 experiments to accelerate data-driven cryo-EM analysis](https://www.biorxiv.org/content/10.64898/2026.04.29.720997v1)
  来源：bioRxiv | 日期：2026-05-03 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：冷冻电镜（cryo-EM）通过实现生物大分子的近原子分辨率结构解析，彻底改变了结构生物学。颗粒（即从显微照片中提取的生物分子2D投影）是3D重构的核心输入。尽管数据驱动方法已改变多个科学领域，但在冷冻电镜中的应用受限于现有颗粒数据集规模小、蛋白质多样性不足且缺乏丰富的单颗粒标注。本研究推出了cryoPANDA（冷冻电镜颗粒标注数据集），包含来自252个实验的超过3700万个标注颗粒，涵盖广泛的蛋白质类型，规模比以往集合大10倍以上。每个...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [EvoRMD: integrating biological context and evolutionary RNA language models for interpretable prediction of RNA modifications.](https://pubmed.ncbi.nlm.nih.gov/42070027/)
  来源：PubMed | 日期：2026-05-02 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：RNA修饰在转录后基因表达调控中起关键作用，但现有计算方法多针对单一修饰独立建模，忽略了单位点上不同修饰类型间的竞争关系。本研究提出EvoRMD，这是一个结合生物学背景且具有可解释性的RNA修饰预测框架。EvoRMD整合了RNA语言模型嵌入与结构化元数据（包括物种、器官、细胞类型和亚细胞定位），并利用注意力机制识别具有信息量的序列位置。通过共享的多分类器，该模型能够针对11种修饰类型生成受背景约束的预测结果。实验表明，EvoRMD表现出...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Agent-Driven Validation of Oncology Therapeutic Targets](https://www.biorxiv.org/content/10.64898/2026.04.29.721634v1)
  来源：bioRxiv | 日期：2026-05-03 | 相关度：2.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：靶点选择是药物研发的关键，但对已发表靶点声明进行系统性重复验证的情况极少。本研究引入了一种专注于重复验证的AI智能体（Agent）框架，用于评估31个基因靶点-疾病假设，涵盖了来自已撤稿和未撤稿论文的背景特异性肿瘤靶点。研究将每个靶点声明转化为零样本（zero-shot）验证提示词，由生物医学研究智能体执行单轮分析，所有智能体驱动的分析结果均由领域专家进行验证和评分。结果显示，与已撤稿靶点（2/17验证成功，11.8%）相比，未撤稿靶点...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Visualization analysis of research hotspots and trends in Type B Aortic Dissection based on bibliometrics.](https://pubmed.ncbi.nlm.nih.gov/42071232/)
  来源：PubMed | 日期：2026-05-03 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：本研究采用 CiteSpace 和 VOSviewer 软件，通过文献计量学方法系统分析了 B 型主动脉夹层（TBAD）领域的知识结构、研究热点及演化趋势。研究对发文趋势、国家/机构/作者合作网络、关键词共现及引文突发检测进行了多维度定量分析。结果显示，自 2013 年起 TBAD 发文量显著增长，形成了以中美为核心的全球合作格局。研究范式已从技术应用转向精准干预和个体化管理，当前热点聚焦于胸腔内主动脉修复术（TEVAR）、并发症预测、...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
