# 每日论文监控日报 (2026-04-28)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 10 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：429 Client Error: Too Many Requests
- PubMed：成功，命中 18 篇
- bioRxiv：成功，命中 10 篇
- medRxiv：成功，命中 3 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### 方法创新

- [Risk Based Prediction of Novel AMR Variants Using Protein Language Models](https://www.biorxiv.org/content/10.1101/2025.09.12.672331v2)
  来源：bioRxiv | 日期：2026-04-27 | 相关度：9.65 | 新颖度：5.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：抗生素耐药性（AMR）是全球健康的重大威胁，监测系统亟需检测已知及新兴的耐药标志物。本研究开发了 AMRscope，这是一种基于 ESM2 蛋白质语言模型（PLM）嵌入向量的预测模型，专门用于评估单位点突变导致耐药的可能性。该工具应用于多种细菌的抗生素相互作用蛋白，涵盖了世卫组织（WHO）重点病原体，如耐利福平结核分枝杆菌和耐碳青霉烯铜绿假单胞菌。实验结果显示，在随机划分的数据集上，模型达到了 0.88 的准确率、0.87 的 F1 分...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [Comparing prognostic performance and reasoning between large language models and physicians](https://www.medrxiv.org/content/10.64898/2026.04.17.26350898v1)
  来源：medRxiv | 日期：2026-04-25 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：本研究旨在评估并比较大语言模型（LLMs）与医生在预测危重症幸存成人患者出院后6个月死亡率方面的表现。研究采用嵌入式混合方法，从MIMIC-IV v2.2数据库中随机抽取100例病例，由4种当代LLM（OpenAI GPT-4o、o3-mini、o4-mini及DeepSeek-R1）和7位执业医生根据住院出院小结和人口统计学信息，独立提供预后预测（是/否）及推理过程。结果显示，医生预测的平均准确率为70.1%（敏感性59.7%，特异性...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [All Models are Wrong, Some are Annotated: Automating Metadata in Biomedical Repositories](https://www.biorxiv.org/content/10.64898/2026.04.23.720371v1)
  来源：bioRxiv | 日期：2026-04-27 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：高质量元数据对科学发现至关重要，但生物医学数据库中普遍存在的标注稀疏问题限制了生物学细节的获取。本研究评估了大语言模型（LLMs）从神经科学数据库 ModelDB 的源代码中自动推断离子通道和受体亚型元数据的能力。研究者从 ModelDB 提取了 5,133 个模型文件，并对其中 1,100 个进行了人工标注（253 个用于测试）。实验对比了 GPT-5.2 和 GPT-mini 在零样本及启发式增强提示下的表现，并以特征工程驱动的 X...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Designing DNA With Tunable Regulatory Activity Using Discrete Diffusion](https://www.biorxiv.org/content/10.1101/2024.05.23.595630v3)
  来源：bioRxiv | 日期：2026-04-27 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：设计具有可调且背景特异性活性的调控DNA是生物技术和医学的核心目标。本文提出了DNA离散扩散模型（D3），这是一种通过迭代核苷酸替换过程生成调控DNA序列的生成模型。在计算基准测试中，D3在生成调控序列方面优于匹配的扩散基准模型，其生成的序列在目标活性、活性分布及序列组成上与天然序列高度匹配。在K562细胞系的lentiMPRA（大规模平行报告基因检测）实验中，D3设计的序列保留了可测量的调控活性，且比基准模型更准确地重现了基因组调控序...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Subarachnoid hemorrhage: epidemiology, risk factors, pathogenesis, and clinical therapies.](https://pubmed.ncbi.nlm.nih.gov/42043672/)
  来源：PubMed | 日期：2026-04-27 | 相关度：5.0 | 新颖度：5.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：蛛网膜下腔出血（SAH）是一种致死率极高的脑血管急症，常导致严重的长期神经功能障碍。研究表明，SAH的发病率在不同地区和人群间存在显著差异，这由不可调控因素（如年龄、性别、家族史和遗传易感性）与可调控因素（如高血压、吸烟、药物使用和代谢紊乱）共同决定。血管生物学与基因组学的进展揭示，细胞外基质不稳定、内皮功能障碍、慢性炎症及特定遗传变异在动脉瘤形成与破裂中起关键作用。破裂后，SAH触发双相损伤级联反应：早期脑损伤（EBI）在数小时内发生...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Decoding the phenomenology of spontaneous thought using large language-model ratings on verbal retrospective free reports](https://www.biorxiv.org/content/10.64898/2026.04.22.720079v1)
  来源：bioRxiv | 日期：2026-04-26 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：自发性思维占据了日常内心体验的大部分，但其内容和神经生理基础的探索长期受限于方法学挑战。传统思维探测法限制了现象学报告的完整性，而实时口头报告则会干扰思维流并产生运动伪迹。本研究设计并测试了一种新方法，将延迟口头回顾性自由报告（RFR）与大语言模型（LLM）生成的自动现象学评分相结合，以评估自发思维的神经基础。22名参与者完成了闭眼自由思考任务，其报告由四种最先进的LLM和人类评分小组针对10个现象学维度进行评估。随后，研究者训练机器学...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Geometric Theoretical Framework for Dynamic Protein Mutation Detection Models: Defect Awareness and Pathogenicity Prediction](https://www.biorxiv.org/content/10.64898/2026.04.22.720255v1)
  来源：bioRxiv | 日期：2026-04-26 | 相关度：4.6 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：传统蛋白质突变检测依赖静态单构象模型，忽略了构象柔性和动态演化，导致在柔性区域和变构位点出现系统性失效。本研究建立了一个定理驱动的几何代数框架，用于动态蛋白质突变建模。该框架从动态构象黎曼流形出发，通过算子值观测构建潜表示空间，并将代数约束放宽为可学习的近似李代数正则化。研究引入了利普希茨稳定的拓扑谱缺陷（TSD, δ_spec）指标，利用列维-奇维塔联络和热核渐近性量化静态表示与动态几何不变量之间的不一致性。在包含108个PDB结构及...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [The complexome contextualizes proteomics data to fingerprint biological states and highlight perturbed functional modules in disease.](https://pubmed.ncbi.nlm.nih.gov/42034643/)
  来源：PubMed | 日期：2026-04-25 | 相关度：3.05 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：分析单组学及整合多模态组学数据以捕捉疾病中的功能失调仍具挑战。本研究提出了一个生物信息学框架，利用人工策划的蛋白质复合物数据集（“复合物组”，complexome）作为蛋白质组学数据整合的基础。该框架适用于人类及其他模式生物，通过提供细胞功能的全局视图，支持蛋白质组学数据的查询。研究首先基准测试了人类组织中蛋白质丰度如何塑造独特的复合物组特征，从而实现生物活性的“指纹化”识别。随后，通过对比疾病与对照组的蛋白质组定量数据，分析了复合物组...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [A Scalable Method for Validated Data Extraction from Electronic Health Records with Large Language Models](https://www.medrxiv.org/content/10.1101/2025.02.25.25322898v2)
  来源：medRxiv | 日期：2026-04-25 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：医疗机构日益需要结构化的患者级临床变量，但相关信息常碎片化存在于异构EHR系统、非结构化文档和扫描件中。本研究开发了两种互补的LLM方法：一是基于模式的命名实体识别与关系抽取，将变量标准化为FHIR和OHDSI词汇；二是检索增强的清单框架，通过规范提示词整合文档文本与结构化数据，并提供证据支持。在3,493名患者的验证中，基于模式的抽取器在药物、放射和手术领域的准确率、召回率及F1值均达到约95%。相比结构化C-CDA数据，LLM抽取的...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Tuberculosis in households with infectious cases in Kampala city: Harnessing health data science for new insights on an ancient disease with persistent, unresolved problems (DS-IAFRICA TB) study protocol](https://www.medrxiv.org/content/10.64898/2026.04.23.26351571v1)
  来源：medRxiv | 日期：2026-04-25 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：乌干达坎帕拉市的结核病（TB）流行严重，且伴随高HIV共感染率。在主动筛查发现的未诊断病例中，30%以上为无症状感染者，且宿主与环境风险因素交织，传统方法难以区分。本研究（DS-IAFRICA TB）旨在利用健康数据科学（AI/ML）技术解决这一复杂性。研究将利用马凯雷雷大学的计算资源，整合结核病患者及其家庭接触者的人口统计学、临床和实验室数据，开发AI/ML算法。核心目标包括：(1) 在基线期（0月）预测哪些患者在治疗第2和第5个月时...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
