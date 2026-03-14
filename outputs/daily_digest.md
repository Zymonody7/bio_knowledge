# 每日论文监控日报 (2026-03-14)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 19 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：429 Client Error: Too Many Requests
- PubMed：成功，命中 44 篇
- bioRxiv：成功，命中 40 篇
- medRxiv：成功，命中 8 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [EnsAgent: a tool-ensemble multiple Agent system for robust annotation in spatial transcriptomics](https://www.biorxiv.org/content/10.64898/2026.03.10.710824v1)
  来源：bioRxiv | 日期：2026-03-13 | 相关度：8.9 | 新颖度：7.2
  匹配主题：foundation_model_agent
  中文摘要：Motivation: Automated domain annotation in spatially resolved transcriptomics (SRT) remains challenging since it depends on gene expression, morphology, and clinical conventions, which vary across cohorts and platforms. ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [WITHDRAWN: A Druggable Tumor Suppressor and Leukemic Stem Cell Marker](https://www.biorxiv.org/content/10.1101/2025.10.16.682831v5)
  来源：bioRxiv | 日期：2026-03-11 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Acute myeloid leukemia (AML) often enters remission after chemotherapy but frequently relapses due to chemotherapy-resistant leukemic stem cells (LSCs). Relapsed AML remains largely unresponsive to current therapies and ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Toward AI foundation models for epidemics: Promise, challenges, and paths forward.](https://pubmed.ncbi.nlm.nih.gov/41824492/)
  来源：PubMed | 日期：2026-03-31 | 相关度：4.4 | 新颖度：10.0
  匹配主题：pathogenomics
  中文摘要：基础模型（如 GPT、GenCast、AlphaFold）正通过在大规模异构数据上预训练来改变科学发现，但在流行病建模领域尚未实现类似变革。传统模型通常针对特定病原体，在应对如 SARS-CoV-2 等突发疫情时难以快速生成洞察。本文探讨了将基础模型范式扩展至流行病学的可能性：即构建一个能捕捉跨病原体、人群和环境的传染病动力学通用原理的单一预训练模型。该模型可通过极少数据微调至新环境，实现更快的预测、推理和响应，对资源匮乏地区尤为重要。...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Highly accurate ab initio gene annotation with ANNEVO.](https://pubmed.ncbi.nlm.nih.gov/41820667/)
  来源：PubMed | 日期：2026-03-12 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Accurate gene annotation is essential for deciphering the mapping from genomic sequences to their functional roles. However, current methods struggle to model complex gene transmission patterns, such as vertical inherita...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 其他

- [Biodesign Buddy: Integrating Generative Artificial Intelligence in Academic Biodesign](https://www.biorxiv.org/content/10.64898/2026.03.11.710906v1)
  来源：bioRxiv | 日期：2026-03-13 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：生物设计（Biodesign）教育是一个结合设计实践与生命科学的新兴跨学科领域，旨在开发新型生物系统、材料和工艺。尽管相关竞赛和项目日益增多，但教育者在课程设计及培养非STEM背景学生的科学素养方面仍面临挑战。本研究探讨了领域特定生成式人工智能系统“Biodesign Buddy”的教学潜力。研究通过对参与国际生物设计竞赛的64名学生进行为期八周的部署，采用混合方法分析了问卷调查、教师反馈和学生设计笔记。评估重点在于AI辅助学习如何影响...
  为什么值得看：bioRxiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Automated extraction and optimization of protein purification protocols using multi-agent large language models](https://www.biorxiv.org/content/10.64898/2026.03.03.709341v1)
  来源：bioRxiv | 日期：2026-03-11 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in Large Language Models (LLMs) present new opportunities for automating critical bottlenecks in scientific workflows such as literature reviews or protocol design. One such bottleneck is the purification...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Regression vs. Medical LLMs: A Comprehensive Study for CVD and Mortality Risk Prediction](https://www.medrxiv.org/content/10.64898/2026.03.11.26347789v1)
  来源：medRxiv | 日期：2026-03-11 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Cardiovascular diseases (CVDs) remain the foremost cause of global morbidity and mortality, driving an urgent need for robust predictive tools that enable early detection and preventive intervention. Traditional regressi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evaluating transformer-based models for structural characterization of orphan proteins](https://www.biorxiv.org/content/10.64898/2026.03.10.709490v1)
  来源：bioRxiv | 日期：2026-03-12 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：基于Transformer的模型（TBM）是预测蛋白质结构和功能特征的最先进深度学习架构。尽管方法各异，但它们均依赖于按同源性组织的大规模蛋白质序列数据集。然而，真核生物蛋白质组中有5-30%属于孤儿蛋白，即与已知家族无检测相似性的序列。由于缺乏同源性，孤儿蛋白成为评估TBM在熟悉序列空间外泛化能力的理想对象。本研究利用根结线虫属（Meloidogyne）中经专家策划的孤儿蛋白集，对比了多种常用TBM架构的预测性能。评估发现，基于多序列...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [User-driven development and evaluation of an agentic framework for analysis of large pathway diagrams](https://www.biorxiv.org/content/10.64898/2026.03.10.710813v1)
  来源：bioRxiv | 日期：2026-03-12 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：随着生物医学知识的持续增长，存储分子相互作用图谱（描述正常或病理状态下的细胞与分子过程）的资源在规模和复杂性上不断增加，导致非专业用户难以导航和理解。本文介绍了一种基于大语言模型（LLM）的智能体（Agentic）框架——Llemy，旨在辅助用户探索这些复杂的分子相互作用图谱。研究采用用户驱动的开发流程，从最初的黑客松原型设计阶段起便邀请领域专家参与，并针对后续精细化版本收集了细粒度及通用的用户反馈。通过评估，研究验证了 Llemy 在...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Benchmarking zero-shot single-cell foundation model embeddings for cellular dynamics reconstruction](https://www.biorxiv.org/content/10.64898/2026.03.10.710748v1)
  来源：bioRxiv | 日期：2026-03-12 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：从时间分辨单细胞转录组中重建细胞轨迹对于理解从胚胎发育到癌症进展的生物过程至关重要。虽然单细胞基础模型（scFMs）通过大规模预训练承诺提供通用的生物学表征，但其捕获控制细胞命运决定的非线性动力学能力尚未得到表征。本研究在涉及分支谱系和连续状态转换的挑战性生物医学场景中，系统地评估了多种 scFM。通过将零样本 scFM 嵌入与动态最优传输相结合，我们在回溯祖细胞状态、插值转换中间体和外推未来命运方面，将其性能与传统的高变基因（HVG）...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [HitAnno: Atlas-level cell type annotation based on scATAC-seq data via a hierarchical language model](https://www.biorxiv.org/content/10.64898/2026.03.10.710729v1)
  来源：bioRxiv | 日期：2026-03-12 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：单细胞转座酶可及染色质测序（scATAC-seq）是剖析细胞表观基因组异质性和基因调控程序的关键技术。随着图谱级数据集的出现，细胞类型注释面临数据规模空前和细胞类型多样性增加的挑战，对模型的可靠性和鲁棒性提出了严苛要求。本文提出 HitAnno，一种能够对图谱级 scATAC-seq 数据进行准确且可扩展注释的分层语言模型。HitAnno 利用选定的细胞类型特异性峰（peaks）构建“细胞句子”，并采用两级注意力机制分层捕捉染色质可及性...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Application of large language models to the annotation of cell lines and mouse strains in genomics data](https://www.biorxiv.org/content/10.64898/2026.03.05.709906v2)
  来源：bioRxiv | 日期：2026-03-12 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：这篇论文来自 bioRxiv，主题上与 foundation_model_agent 有交叉。原始英文摘要要点如下：Accurate, consistent and comprehensive metadata are essential for the reuse of functional genomics data deposited in repositories such as the Gene Expression Omni...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Cyclic peptides space: The methodology of sequence selection to cover the comprehensive physical properties](https://www.biorxiv.org/content/10.64898/2026.03.10.710724v1)
  来源：bioRxiv | 日期：2026-03-12 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Cyclic peptides have emerged as a pivotal modality for next-generation therapeutics, due to their superior biocompatibility, high selectivity, and structural stability. While AI-driven peptide design has advanced rapidly...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Rapid and Interpretable AMR Diagnostics via Genomics and Cell Painting using Differential Geometry-based Directed-Simplicial Neural Networks on Multimodal Data](https://www.biorxiv.org/content/10.64898/2026.03.11.711128v1)
  来源：bioRxiv | 日期：2026-03-12 | 相关度：4.75 | 新颖度：1.0
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：针对全球及印度等高流行地区的抗生素耐药性（AMR）挑战，本研究提出了一种整合基因组与细胞表型数据的多模态计算框架。该框架利用基于微分几何的有向单纯神经网络（Dg Dir SNNs）分析了384个临床相关的AMR分离株（包括大肠杆菌和肺炎克雷伯菌）。研究整合了256个基因组k-mer特征和503个源自高内涵Cell Painting实验的细胞形态描述符。Dg Dir SNNs模型构建了顶级生物标志物驱动特征的推断因果网络，预测了基因组基序...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MESSI: Multimodal Experiments with SyStematic Interrogation using nextflow](https://www.biorxiv.org/content/10.64898/2026.03.09.710452v1)
  来源：bioRxiv | 日期：2026-03-11 | 相关度：3.05 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：多模态生物医学研究通过整合同一样本的多种分子和临床模态，为疾病预测提供了新机遇，但现有整合方法的基准测试因预处理不一致、调参策略不等及评估方案不可比而面临挑战。本研究开发了 MESSI，一个基于 Nextflow 的可重复基准测试框架，专门用于多模态结果预测。MESSI 标准化了数据准备，支持 R 和 Python 互操作，并强制执行无泄漏的嵌套交叉验证以进行模型选择与评估。该框架目前实现了代表性的中端和后端整合方法，支持大块（bulk...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Learning the All-Atom Equilibrium Distribution of Biomolecular Interactions at Scale](https://www.biorxiv.org/content/10.64898/2026.03.10.710952v1)
  来源：bioRxiv | 日期：2026-03-13 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：生物分子的功能由动态构象系综而非静态结构决定。虽然 AlphaFold 等模型革新了静态结构预测，但由于分子动力学（MD）模拟的高昂计算成本，准确捕捉全原子生物分子相互作用的平衡分布仍是重大挑战。本研究提出了 AnewSampling，这是一个旨在实现全原子平衡分布高保真采样的可迁移生成式基础框架，也是首个在全原子水平上忠实重现 MD 的模型。该模型采用新型商空间（quotient-space）生成框架以确保数学一致性，并利用了包含超过...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Multiscale conformational sampling of multidomain fusion proteins by a physics informed diffusion model](https://www.biorxiv.org/content/10.64898/2026.03.11.711061v1)
  来源：bioRxiv | 日期：2026-03-13 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：多结构域融合蛋白（如双特异性抗体）的疗效高度依赖其灵活的接头（linker）区域。表征这些庞大的构象系综对药物理性设计至关重要，但传统全原子分子动力学（MD）的高昂计算成本限制了对大规模结构域运动的模拟。本研究开发了一种物理信息驱动的多尺度扩散模型，旨在快速采样蛋白质动力学。研究利用具有不同接头的多结构域蛋白微秒级 MD 轨迹，训练了一个基于等变图神经网络（EGNN）的框架。该模型采用粗粒化空间图，将刚性结构域简化为质心锚点，同时保留接...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Multi-Criteria Validation of LLM-Inferred Depression Severity from Outpatient Psychiatry Notes](https://www.medrxiv.org/content/10.64898/2026.03.11.26348066v1)
  来源：medRxiv | 日期：2026-03-12 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：门诊精神科护理中，抑郁严重程度的纵向测量受限于标准化评估的频率。本研究评估了大语言模型（LLM）从门诊精神科病程记录中推断临床抑郁严重程度的能力。研究收集了某大型医学中心2015-2021年间58家诊所、8,287名成年患者的91,651份病历。使用符合HIPAA标准的GPT-5.2模型，从脱敏后的病历中独立推断PHQ-9、HAM-D和CGI-S评分。结果显示，LLM推断的PHQ-9评分与患者自评结果具有中度一致性（Pearson r=...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Fingerprinting Fluorescent In Situ Hybridization Enables Multiplexed Identification of Pathogenic Bacteria.](https://pubmed.ncbi.nlm.nih.gov/41810482/)
  来源：PubMed | 日期：2026-03-11 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：荧光原位杂交（FISH）是一种无需培养即可检测病原菌的高特异性技术，能同时提供病原菌丰度、形态和空间定位信息。然而，传统 FISH 灵敏度低且多重检测能力有限，限制了其广泛应用。本研究提出了一种由 DNA 自组装驱动的指纹荧光原位杂交（FinFISH）策略，用于多重病原菌检测。以呼吸道病原体为模型，FinFISH 利用 FAM、Cy3 和 Cy5 三种荧光团进行组合标记，为每种病原体生成独特的荧光指纹。该策略突破了荧光通道数量对检测通量...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
