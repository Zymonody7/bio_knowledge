# 每日论文监控日报 (2026-08-03)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 31 篇新论文。

## 抓取状态

- arXiv：成功，命中 17 篇
- PubMed：成功，命中 173 篇
- bioRxiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='api.biorxiv.org', port=443): Read timed out. (read timeout=60)
- medRxiv：失败，命中 0 篇，错误：503 Server Error: Service Unavailable

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [Growth factor thermostability dataset derived from experimental and computational approaches to accelerate cultured meat development.](https://pubmed.ncbi.nlm.nih.gov/42422031/)
  来源：PubMed | 日期：2026-08-01 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：This project compiled experimentally measured and computationally predicted thermostability data for growth factors (GFs) commonly used in cultured meat and seafood (CM) production. Data were generated on recombinant GFs...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Sparse autoencoders reveal interpretable cell-type programs in single-cell foundation model representations.](https://pubmed.ncbi.nlm.nih.gov/42155660/)
  来源：PubMed | 日期：2026-08-01 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Single-cell foundation models such as scGPT learn rich representations of cellular identity, yet the biological programs encoded in their internal activations remain opaque. We investigate whether sparse autoencoders (SA...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Accelerating inference in genomic and proteomic foundation models via speculative decoding.](https://pubmed.ncbi.nlm.nih.gov/42536416/)
  来源：PubMed | 日期：2026-07-31 | 相关度：7.1 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Genomic and protein foundation models (GFMs and PFMs) have demonstrated strong performance in learning the language of DNA and proteins, but their use in large-scale sequence generation is limited by the latency of autor...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Can Large Language Models Derive New Knowledge? A Dynamic Benchmark for Biological Knowledge Discovery](http://arxiv.org/abs/2603.03322v2)
  来源：arXiv | 日期：2026-02-10 | 相关度：6.55 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：Recent advancements in Large Language Model (LLM) agents have demonstrated remarkable potential in automatic knowledge discovery. However, rigorously evaluating an AI's capacity for knowledge discovery remains a critical...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Multi-Agent System for Motor Design Optimization via an FEA-AI Hybrid Approach](http://arxiv.org/abs/2606.09037v2)
  来源：arXiv | 日期：2026-06-08 | 相关度：6.55 | 新颖度：6.2
  匹配主题：foundation_model_agent
  中文摘要：This study presents a large language model (LLM)-based multi-agent framework for interior permanent magnet synchronous motor (IPMSM) design optimization that mitigates limitations of conventional workflows: expertise-dep...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [UltraSAM3: A Concept-Driven Foundation Model for Universal Ultrasound Image Segmentation](http://arxiv.org/abs/2607.29200v1)
  来源：arXiv | 日期：2026-07-31 | 相关度：5.75 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Ultrasound imaging has become increasingly widespread in clinical practice due to its portability, low cost and real-time capability, making ultrasound image segmentation important. However, ultrasound images differ subs...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [When Safety Becomes a Vulnerability: Exploiting LLM Alignment Homogeneity for Transferable Blocking in RAG](http://arxiv.org/abs/2603.03919v2)
  来源：arXiv | 日期：2026-03-04 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) systems are vulnerable to blocking attacks, in which poisoned documents cause large language models (LLMs) to refuse benign queries. Existing attacks rely on adversarial suffixes or e...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [When Iterative RAG Beats Ideal Evidence: A Diagnostic Study in Scientific Multi-hop Question Answering](http://arxiv.org/abs/2601.19827v5)
  来源：arXiv | 日期：2026-01-27 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) extends large language models (LLMs) beyond parametric knowledge, yet it is unclear when iterative retrieval-reasoning loops meaningfully outperform static RAG, particularly in scient...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Zero-shot document-level biomedical relation extraction via scenario-based prompt design in two-stage with LLM.](https://pubmed.ncbi.nlm.nih.gov/41762612/)
  来源：PubMed | 日期：2026-08-01 | 相关度：6.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Document-level biomedical relation extraction is a crucial task due to the complex interactions among multiple entities distributed across lengthy scientific texts. Traditional supervised methods are constrained by their...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Bridging the Question-Answer Gap in Retrieval-Augmented Generation: Hypothetical Prompt Embeddings](http://arxiv.org/abs/2607.29402v1)
  来源：arXiv | 日期：2026-07-31 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) systems synergize retrieval mechanisms with generative language models to enhance the accuracy and relevance of responses. However, bridging the style gap between user queries and rel...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GoldenRetriever: Non-Interactive Homomorphic Encrypted Retrieval for Privacy-Preserving RAG](http://arxiv.org/abs/2607.29019v1)
  来源：arXiv | 日期：2026-07-31 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) enhances large language models by incorporating external knowledge, but existing pipelines typically operate on plaintext data, raising significant privacy concerns. Prior work on pri...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Artificial intelligence in clinical metagenomic pathogen detection: A critical review of pipeline integrations, challenges, and future directions.](https://pubmed.ncbi.nlm.nih.gov/42289215/)
  来源：PubMed | 日期：2026-08-01 | 相关度：8.25 | 新颖度：1.75
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：Metagenomic next-generation sequencing (mNGS) has expanded the scope of clinical diagnostics by enabling culture-independent detection of microorganisms in patient samples. However, mNGS clinical utility remains constrai...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Applications of Machine Learning, Natural Language Processing, and Generative Artificial Intelligence in Dermatology Education and Research: A Scoping Review.](https://pubmed.ncbi.nlm.nih.gov/41981908/)
  来源：PubMed | 日期：2026-08-01 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence (AI) is being increasingly used in dermatology education and research as digital health data expands and large language models (LLMs) advance. This scoping review synthesized current applications,...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Interpretable deep learning model of circulating genomics for quantitative survival prediction in advanced non-small cell lung cancer.](https://pubmed.ncbi.nlm.nih.gov/41649698/)
  来源：PubMed | 日期：2026-08-01 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Accurate quantitative survival prediction in advanced non-small cell lung cancer (NSCLC) remains an unmet clinical need. While liquid biopsy is widely used, single circulating tumor DNA (ctDNA) shows limited predictive p...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BM25 Wins at Scale: A Scaling Study of Retrieval-Augmented Generation Paradigms](http://arxiv.org/abs/2607.26497v3)
  来源：arXiv | 日期：2026-07-29 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：本研究针对检索增强生成（RAG）中的词法检索、稠密检索、图索引及智能体搜索等范式，在不同语料规模下的准确率与成本缩放关系进行了系统评估。研究通过 28 个嵌套层级将语料规模扩大约 450 倍，同时保持问题及核心相关与对抗文档不变。在统一的阅读器模型和评测协议下，测量了准确率、构建与查询 Token 数及延迟。结果显示，各范式表现随规模呈现交叉趋势而非绝对领先：文件系统智能体在极小规模表现最佳，但随着搜索空间扩大，其查询 Token 成本...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AttriMem: Attribution-Guided Process Feedback for Agent Memory Construction](http://arxiv.org/abs/2607.21106v2)
  来源：arXiv | 日期：2026-07-23 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：有效的记忆对大语言模型（LLM）智能体至关重要，但其构建仍具挑战。记忆构建策略决定了在交互积累过程中提取、存储、更新、压缩或丢弃哪些信息。启发式方法依赖主观且特定于任务的规则，可能与下游目标不匹配并限制跨任务适应性。基于强化学习（RL）的方法虽能从反馈中学习，但主要使用结果或模块级奖励，这种粗粒度信号无法识别哪些中间记忆内容支持了最终答案，导致细粒度信用分配瓶颈。由于中间决策缺乏唯一标准答案且信用随推理轨迹变化，构建过程反馈极难。为此，...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Artificial Intelligence in Food-Nutrition-Health Research: From Multimodal Data Integration to Precision Intervention.](https://pubmed.ncbi.nlm.nih.gov/42535509/)
  来源：PubMed | 日期：2026-08-01 | 相关度：4.5 | 新颖度：1.0
  匹配主题：foundation_model_agent, application_monitoring
  中文摘要：Artificial intelligence (AI) is transforming food-nutrition-health research by enabling pattern recognition in complex, high-dimensional datasets that traditional hypothesis-driven approaches cannot address. This review ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Deep learning-enabled ratiometric signal transduction for portable and intelligent colorimetric LAMP biosensing of Vibrio vulnificus.](https://pubmed.ncbi.nlm.nih.gov/42031193/)
  来源：PubMed | 日期：2026-08-01 | 相关度：2.65 | 新颖度：0.25
  匹配主题：sequencing_bioinformatics
  中文摘要：Vibrio vulnificus is a highly lethal zoonotic pathogen associated with seafood consumption and aquaculture environments, demanding rapid and reliable on-site molecular diagnostics. Here, we report an intelligent biosensi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Quaternionic Response Geometry for Proteins: Toward a Noncommutative Theory of Ordered Deformations](http://arxiv.org/abs/2607.29101v1)
  来源：arXiv | 日期：2026-07-31 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Protein function may depend on both endpoint conformations and the ordered deformation histories by which they are reached. This distinction is relevant to allostery, conformational switching, mutation-induced rearrangem...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CREB gene regulation as a blood biomarker of neural sensitivity to social threat.](https://pubmed.ncbi.nlm.nih.gov/41905489/)
  来源：PubMed | 日期：2026-08-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：社会威胁会增强炎症反应并增加相关疾病风险，识别对社会威胁具有高度神经敏感性的个体对制定预防协议至关重要。本研究探讨了外周血中cAMP反应元件结合蛋白（CREB）转录因子活性是否可作为中枢神经系统（CNS）对社会威胁敏感性的生物标志物。研究利用一项随机对照试验的基线数据（n=44，平均年龄19.4岁），结合功能磁共振成像（fMRI）与外周血采样。通过基于TELiS启动子的生物信息学方法评估CREB基因调节活性，并利用改良蒙特利尔成像压力测...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [TFGformer: Multivariate Time Series Forecasting via Time-Frequency Graph Learning and Covariate Fusion](http://arxiv.org/abs/2607.29459v1)
  来源：arXiv | 日期：2026-07-31 | 相关度：0.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：针对异构物联网传感器产生的大规模多元时间序列，准确的长期预测对资源调度和预测性维护至关重要。虽然现有时间序列基础模型泛化性强，但依赖静态参数，缺乏推理时动态访问外部历史模式的能力。检索增强生成（RAG）虽有潜力，但在处理异构源量级差异及历史相似性与未来一致性不匹配方面存在挑战。本文提出 CrossRAG 框架，集成形状感知记忆（SAM）与 RevIN 归一化以实现量级鲁棒的形状级检索；引入未来一致对比（FCC）学习，以区分具有相似历史但...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MERIT: Efficient In-Place Deletion for Dynamic Graph-Based Approximate Nearest Neighbor Indexes](http://arxiv.org/abs/2607.29173v1)
  来源：arXiv | 日期：2026-07-31 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：基于图的索引已成为高维数据近似最近邻搜索（ANNS）的主流方法，在检索增强生成（RAG）和向量数据库等实际应用中发挥着关键作用。尽管静态图构建和搜索已取得显著进展，但高效的原位删除仍具挑战，因为必须在不让陈旧入边消耗搜索能力或因昂贵的全局维护中断在线服务的情况下移除过时向量。为此，本文提出 MERIT 框架，包含三大核心技术：(1) 基于有界搜索的恢复，结合被删顶点的出邻居与其可搜索的入邻居；(2) $k_r$-最小生成树（MST）局部...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Shaping Scientific Explanations to Expert Perspectives with Persona-Conditioned Reinforcement Learning](http://arxiv.org/abs/2603.21846v2)
  来源：arXiv | 日期：2026-03-23 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：可解释人工智能（XAI）对科学发现日益重要，但现有方法往往忽略了专家在评估证据、优先处理机制和构建叙述逻辑上的认识论差异。本研究提出了“视角调节解释”（perspective-conditioned explanations）框架，旨在使解释生成适应专家判断的个性化需求。在药物研发的知识图谱推理路径任务中，研究发现专家的偏好可以组织成连贯的认识论视角，并由“代理人格”（agentic personas）这一表征形式进行捕捉。通过人格对齐...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Toward Bridging the Gap from Artificial Intelligence in Clinical Research to Clinical Practice in Rheumatology: The Mayo Experience.](https://pubmed.ncbi.nlm.nih.gov/42409435/)
  来源：PubMed | 日期：2026-08-01 | 相关度：4.85 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：This article highlights Mayo Clinic's pioneering efforts to integrate artificial intelligence (AI) and machine learning into rheumatology, focusing on genomics, imaging, pathology, and clinical data science to improve di...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial Intelligence in Clinical Genetics: Current Applications and Challenges.](https://pubmed.ncbi.nlm.nih.gov/42443618/)
  来源：PubMed | 日期：2026-08-01 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：多组学、二代测序（NGS）和长读长测序技术已深刻改变医学遗传学实践。由于每位患者涉及数万至数百万个变异及复杂的生化模式，复杂病例的解读往往需要耗费大量人力。海量数据集的出现使传统分析方法难以为继。人工智能（AI）为处理临床遗传学中日益增长的基因组与表型数据提供了高效手段，目前已应用于变异优先排序与解读、罕见病筛查及精准医学等领域。然而，受限于特定人群代表性不足、伦理争议及数据治理等问题，这些技术向常规临床转化的过程依然困难。目前大多数 ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Bridging Trials and Real Life in Fixed-Duration BTKi-Venetoclax for CLL: A Delphi-Enhanced Synthesis Incorporating Artificial Intelligence (AI) Benchmarks.](https://pubmed.ncbi.nlm.nih.gov/41974594/)
  来源：PubMed | 日期：2026-08-01 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：针对慢性淋巴细胞白血病（CLL）中固定疗程（FD）BTK抑制剂（BTKi）联合维奈克拉方案的患者选择，本研究旨在弥合临床试验与真实世界实践的差距。研究采用改进的德尔菲法，由意大利坎帕尼亚地区的9名血液学家参与，重点评估了合并症、基因组学（TP53/del(17p)、IGHV状态、复杂核型）及物流因素（照护支持、就医距离、给药能力）对一线治疗决策的影响。基于2014-2025年的系统综述制定了12项陈述，共识标准设定为≥75%一致性。结果...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Nursing roles, competencies, and education in precision oncology: a scoping review.](https://pubmed.ncbi.nlm.nih.gov/42500353/)
  来源：PubMed | 日期：2026-08-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：护士在精准癌症护理路径中发挥着关键作用，支持基因组检测的整合并提供以患者为中心的持续护理。本范围综述旨在梳理护士在精准癌症护理中的角色、能力要求及相关教育现状。研究遵循JBI方法，系统检索了MEDLINE、Embase等数据库，并利用生成式人工智能（GenAI）对灰色文献中的国际研究生及继续教育项目进行了检索。研究共纳入52篇文献（44篇涉及角色/能力，23篇涉及教育干预）和65个教育项目。结果识别出五大护理角色主题：基因组风险评估与分...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Multi-omic biomarkers of neoadjuvant treatment response in rectal cancer: A narrative review.](https://pubmed.ncbi.nlm.nih.gov/42250371/)
  来源：PubMed | 日期：2026-08-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：直肠癌对新辅助治疗的反应具有高度异质性，这增加了器官保留策略中患者筛选的复杂性。本综述回顾了2015年以来关于直肠癌新辅助治疗反应预测因子的研究，涵盖六大领域：基因组与分子生物标志物、影像学标志物、组织病理学与数字病理标志物、液体活检（cfDNA/ctDNA）、患者来源的肿瘤模型以及微生物组相关标志物。研究表明，治疗反应受肿瘤内在特征、免疫微环境和间质特征的共同影响。免疫富集型肿瘤（如高CD8+ T细胞浸润、CMS1/iCMS3亚型、高...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [ASO Special Article: Proceedings of the Inaugural Joint US-India Cancer Dialogue: Accelerating Collaboration to Advance Cancer Prevention, Early Detection, Treatment, and Care.](https://pubmed.ncbi.nlm.nih.gov/42166060/)
  来源：PubMed | 日期：2026-08-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：癌症是美印两国的主要死因。2023年6月印度总理访美期间，两国承诺建立美印癌症对话机制，旨在通过结构化双边努力应对共同的癌症挑战。本文概述了2024年8月在新德里举行的首届美印癌症对话联合会议的筹备步骤与议程。通过由政府、科学和临床领导者参与的结构化共识制定流程，确定了双边合作的优先领域。筹备工作包括由美国临床肿瘤学会（ASCO）主办的技术工作组会议，涵盖预防、早期检测、治疗、临床试验和实施科学。会议最终确定了多项核心合作方向：扩大HP...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial intelligence, omics, and biomarkers: Redefining lung cancer early detection.](https://pubmed.ncbi.nlm.nih.gov/42105533/)
  来源：PubMed | 日期：2026-08-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：肺癌是全球死亡率最高的癌症，主要归因于早期干预手段有限。目前的筛查方法受限于侵入性、辐射暴露及早期灵敏度低等问题，亟需创新技术。本综述探讨了结合生物标志物、组学技术与人工智能（AI）的早期检测新兴工具。肿瘤细胞释放的特定生物标志物（如细胞成分、核酸片段、蛋白质片段或代谢物）可通过非侵入性体液检测获取。将生物标志物与蛋白质组学、基因组学或多组学结合，可提供不同癌症亚型和阶段分子特征的全面见解。机器学习和深度学习等AI工具进一步提升了这些技...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [RGTFormer: Predicting mutation-associated multi-drug resistance in Mycobacterium tuberculosis using a categorical gated transformer and relational graph convolutional network.](https://pubmed.ncbi.nlm.nih.gov/41722285/)
  来源：PubMed | 日期：2026-08-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：结核分枝杆菌引起的多重耐药结核病是全球公共卫生面临的重大挑战。耐药性通常由药物靶基因的单核苷酸突变引起，因此早期预测对于有效治疗至关重要。本研究提出了一种名为 RGTFormer 的新型深度学习模型，该模型结合了分类门控 Transformer 和关系图卷积网络（RGCN），用于预测 6 个关键耐药基因的突变是否会导致对一线抗结核药物的耐药性。RGTFormer 整合了突变的序列特征和结构特征，利用 RGCN 捕捉突变之间的依赖关系，并...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
