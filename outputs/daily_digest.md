# 每日论文监控日报 (2026-04-03)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 17 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：429 Client Error: Too Many Requests
- PubMed：成功，命中 143 篇
- bioRxiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='api.biorxiv.org', port=443): Read timed out. (read timeout=60)
- medRxiv：成功，命中 14 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [A Foundation Model for Intensive Care: Unlocking Generalization across Tasks and Domains at Scale](https://www.medrxiv.org/content/10.1101/2025.07.25.25331635v2)
  来源：medRxiv | 日期：2026-04-02 | 相关度：7.15 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：BACKGROUND Early recognition of physiological deterioration in critically ill patients enables timely intervention, yet much of the predictive information in routinely collected intensive care data remains underutilized....
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### 数据集 / Benchmark

- [MedScope: A Lightweight Benchmark of Open-Source Large Language Models for Medical Question Answering](https://www.medrxiv.org/content/10.64898/2026.03.31.26349827v1)
  来源：medRxiv | 日期：2026-04-01 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：The rapid development of large language models (LLMs) has stimulated growing interest in their use for medical question answering and clinical decision support. However, compared with frontier proprietary systems, the em...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 产品应用 / 监测落地

- [HealthFormer: Dual-level time-aware Transformers for irregular electronic health record events](https://www.medrxiv.org/content/10.64898/2026.03.25.26349262v2)
  来源：medRxiv | 日期：2026-03-31 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：纵向电子健康记录（EHR）构成了混合多种临床编码系统和护理场景的不规则事件序列。为了学习可迁移的患者表示，本研究开发了 HealthFormer，一种用于以事件为中心的 EHR 建模的双层 Transformer 框架。该模型包含：1）事件内编码器（Intra-Event Encoder），通过特定代码嵌入模块和注意力池化聚合临床事件内的异构领域 token；2）事件间编码器（Inter-Event Encoder），结合日期编码器和基...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Measuring the Unmeasurable: A Diagnostic Sensor for AI Reasoning Pathology in Sequential Clinical Decision-Making](https://www.medrxiv.org/content/10.64898/2026.03.27.26349583v2)
  来源：medRxiv | 日期：2026-04-01 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models achieve impressive accuracy on medical benchmarks that present clinical information as complete vignettes, but their behavior under sequential information delivery, the standard mode of real clinica...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Toward AI foundation models for epidemics: Promise, challenges, and paths forward.](https://pubmed.ncbi.nlm.nih.gov/41824492/)
  来源：PubMed | 日期：2026-03-31 | 相关度：4.4 | 新颖度：1.5
  匹配主题：pathogenomics
  中文摘要：基础模型（如 GPT、GenCast、AlphaFold）在科学发现中展现出卓越的通用表示学习和任务迁移能力。然而，流行病建模尚未经历类似变革，传统模型仍局限于特定病原体，在 SARS-CoV-2 等突发疫情中难以快速生成洞察。本文探讨了将基础模型范式扩展至流行病学的可能性：即构建一个能捕捉跨病原体、人群和环境的传染病动力学共享原理的预训练模型。该模型可通过极少数据微调至新环境，实现快速预测、推理和响应，对资源匮乏地区尤为重要。文章指出...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [From sequence to structure: A comprehensive review of deep learning models for RNA structure prediction.](https://pubmed.ncbi.nlm.nih.gov/41650708/)
  来源：PubMed | 日期：2026-04-01 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：RNA structure prediction remains one of the most challenging problems in computational biology, with significant implications for understanding gene regulation, drug design, and synthetic biology. While deep learning has...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Natural language processing of biomedical text to map and prioritize protein-disease associations in HFpEF.](https://pubmed.ncbi.nlm.nih.gov/41780317/)
  来源：PubMed | 日期：2026-04-01 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：针对心血管疾病（CVD）生物标志物和药物靶点验证受限于海量碎片化文献（超过3800万篇）的问题，本研究开发并应用了基于机器学习和自然语言处理（NLP）的VITAL（基于先进语言模型的验证文本挖掘）框架。通过分析全量PubMed摘要，识别出550万篇与六大类CVD相关的文献。以射血分数保留的心衰（HFpEF）为案例，该框架系统地量化并优先排序了蛋白质与疾病的关联。研究确认了BNP、肌钙蛋白-I、半乳糖凝集素-3和肾素等已知标志物，并发现了...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Novel Deep-Learning Unsupervised Domain Adaptation Method for Mitigating Batch, Strain, and Instrument Variations to Enhance Raman Spectroscopy-Based Bacterial Pathogen Identification.](https://pubmed.ncbi.nlm.nih.gov/41842761/)
  来源：PubMed | 日期：2026-03-31 | 相关度：4.4 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：针对抗生素耐药性对快速准确病原体鉴定的需求，本研究提出了一种名为拉曼光谱分类差异模型（RSCDM）的新型深度学习无监督领域自适应框架。虽然拉曼光谱结合深度学习可实现快速检测，但仪器异质性、批次变异和菌株多样性导致的领域偏移（Domain Shifts）严重影响了模型的鲁棒性。RSCDM 通过任务特定分类器之间的输出差异动态识别远离源域分布的目标样本，并利用对抗性训练对齐不同领域的特征，以消除光谱变异。实验结果显示，在商用光谱仪上，RSC...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Big data in multiple sclerosis.](https://pubmed.ncbi.nlm.nih.gov/41925198/)
  来源：PubMed | 日期：2026-04-01 | 相关度：3.05 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：本综述总结了利用多源大数据和先进分析技术在多发性硬化症（MS）领域取得的关键进展。源自MS大数据的真实世界证据（RWE）显著优化了治疗策略，重新定义了疾病进展概念，并完善了预后模型。RWE强调了早期强化治疗相较于阶梯治疗的长期获益，揭示了减量治疗的风险及妊娠期管理的重要性。此外，研究明确了特定高效疗法的有效性与安全性差异，以及换药的关键预测因子。RWE还强调了“独立于复发活动的进展”（PIRA）是导致成人和儿童MS残疾及长期不良预后的核...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Machine learning-based DNA microarray analysis for disease detection using the MICRO-AI framework.](https://pubmed.ncbi.nlm.nih.gov/41925147/)
  来源：PubMed | 日期：2026-01-01 | 相关度：1.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：DNA微阵列技术在基因组学中具有重要地位，但其高维度（1.2万-2.2万个基因）、小样本量（155-1097个样本）、噪声及类别不平衡问题挑战了诊断模式的提取。本文提出MICRO-AI框架，用于微阵列数据的自动化疾病诊断。该框架集成了分位数归一化、ComBat批次校正和KNN填补等预处理技术，并采用基于注意力加权的自适应特征选择（结合RFE-CV）以及由GBM、随机森林和SVM组成的异构集成分类器。通过新型注意力特征融合机制，该框架在不...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Hypergraph Foundation Model.](https://pubmed.ncbi.nlm.nih.gov/41433164/)
  来源：PubMed | 日期：2026-04-01 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：超图神经网络（HGNNs）通过超边连接多个顶点，能有效建模蛋白质相互作用和社交网络等领域的高阶复杂关系，增强建模能力并减少信息损失。然而，由于超图数据兼具顶点特征与复杂的结构信息，开发超图基础模型（Foundation Model）面临挑战。本研究提出了 Hyper-FM，一种用于多领域知识提取的超图基础模型。该模型核心包含：用于顶点特征表示的“分层高阶邻居引导的顶点知识嵌入”，以及用于结构信息捕捉的“分层多超图引导的结构知识提取”。此...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Functional impact assessment of tissue-specific missense variants in the PTPRH gene using a multi-tool computational framework.](https://pubmed.ncbi.nlm.nih.gov/41570449/)
  来源：PubMed | 日期：2026-04-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：癌症由破坏细胞过程的遗传改变驱动，其中蛋白酪氨酸磷酸酶受体H型（PTPRH）基因在癌症进展中具有双重作用。本研究采用计算机模拟框架评估了PTPRH的组织特异性错义变异。研究从COSMIC数据库中鉴定出478个独特错义变异，通过fathmm、PROVEAN、PolyPhen-2、SIFT等8种计算工具筛选出14个一致预测为有害的变异。随后利用MUpro、I-Mutant等工具进行稳定性分析，发现其中10个变异可能破坏蛋白质稳定性。进化保守...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Longitudinal information extraction from clinical notes in rare diseases: an efficient approach with small language models](https://www.medrxiv.org/content/10.64898/2026.03.30.26349388v1)
  来源：medRxiv | 日期：2026-03-31 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：罕见病通常需要纵向监测以表征疾病进展，但大量关键临床信息仍锁定在非结构化电子健康记录（EHR）中。本研究旨在开发并评估一种基于小语言模型（SLM）的流水线，用于从罕见肾脏病患者的法语临床记录中提取纵向信息。研究以肾功能关键生物标志物血清肌酐为切入点，分析了包含 200 个测量值（日期、数值和单位三元组）的 81 份临床记录。系统测试了 Mistral-7B、Llama-3.2-3B、Qwen3-4B 和 Qwen3-8B 四种开源 SL...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial intelligence and multi-omics convergence in breast cancer: Revolutionizing diagnosis, prognostication, and precision oncology.](https://pubmed.ncbi.nlm.nih.gov/41616992/)
  来源：PubMed | 日期：2026-04-01 | 相关度：3.75 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：乳腺癌（BC）具有高度异质性，是全球女性癌症死亡的主要原因。基因组学、转录组学、表观基因组学、蛋白质组学和代谢组学等多组学分析的进展，实现了更精细的亚型分层和肿瘤生物学表征，加速了诊断、预后生物标志物及治疗靶点的发现。然而，受限于组学数据的高维性、异质性、跨平台变异以及单模态分析的局限性，将多层分子信号转化为临床决策支持仍具挑战。本综述总结了多组学如何完善乳腺癌亚型定义，并综合了人工智能（特别是深度学习）在整合多组学与影像、病理及临床变...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Multi-omics biomarkers in psychiatric disorders diagnosis and stratification.](https://pubmed.ncbi.nlm.nih.gov/41655615/)
  来源：PubMed | 日期：2026-04-01 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：精神疾病的精准诊断与分层因缺乏客观生物标志物且依赖主观临床标准而面临挑战。基因组学、转录组学、蛋白质组学、代谢组学和表观基因组学等多组学技术的进展，深化了对精神分裂症、双相情感障碍、重度抑郁症和自闭症谱系障碍等复杂神经精神疾病的理解。本综述评估了精神医学领域多组学研究的现状，重点关注方法学创新、整合策略以及在标志物发现和临床实施中的转化潜力。通过合成不同分子层面的数据，多组学方法能够从系统水平将精神疾病视为受分子、细胞、环境和神经回路相...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Comparative evaluation of multimodal point-of-care tests to differentiate gram-negative from gram-positive infections in critically ill adults: a diagnostic accuracy study.](https://pubmed.ncbi.nlm.nih.gov/41535672/)
  来源：PubMed | 日期：2026-04-01 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：针对脓毒症患者在培养结果前过度使用广谱抗生素的问题，本研究系统评估了区分革兰氏阴性（GN）与革兰氏阳性（GP）感染的即时检测（POCT）方法。研究检索了 2005 年至 2025 年间 86 项相关研究，对 72 项研究进行了定量合成，涵盖宿主反应生物标志物、病原体定向检测、组学测试及临床参数。结果显示，病原体定向快速检测（如 PCR、MALDI-TOF MS）表现出最高的准确性，合并灵敏度和特异性均 >0.90，AUC 达 0.97-...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [MedResearchBench: A Multi-Domain Benchmark for Evaluating AI Research Agents on Clinical Medical Research](https://www.medrxiv.org/content/10.64898/2026.03.30.26349749v1)
  来源：medRxiv | 日期：2026-03-31 | 相关度：2.7 | 新颖度：1.25
  匹配主题：pathogenomics
  中文摘要：随着AI Scientist等自动化研究系统的发展，自主科学发现展现出巨大潜力，但现有基准多集中于基础科学，忽视了临床医学研究中复杂的调查设计、混杂控制及报告规范（如STROBE）。为此，本研究推出了MedResearchBench，这是首个专门评估AI系统在临床医学研究任务中表现的基准。该基准包含涵盖心血管、肿瘤、传染病等7个领域的16项任务，基于NHANES和SEER公开数据集构建，并以16篇高质量已发表论文（影响因子2.3-51....
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
