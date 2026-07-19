# 每日论文监控日报 (2026-07-19)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 19 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='export.arxiv.org', port=443): Read timed out. (read timeout=60)
- PubMed：成功，命中 43 篇
- bioRxiv：成功，命中 19 篇
- medRxiv：成功，命中 13 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [Medea: An AI agent for therapeutic reasoning across biological contexts](https://www.biorxiv.org/content/10.64898/2026.01.16.696667v2)
  来源：bioRxiv | 日期：2026-07-16 | 相关度：8.5 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Therapeutic hypotheses can transfer across diseases but their relevance depends on biological context. The same target, perturbation, or treatment can produce different effects across cell types, disease states, genetic ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [A ReAct Agentic AI System for Natural Language Querying and Statistical Analysis of The Cancer Genome Atlas Clinical Data](https://www.medrxiv.org/content/10.64898/2026.07.15.26358188v1)
  来源：medRxiv | 日期：2026-07-17 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：The Cancer Genome Atlas (TCGA) holds clinical data for over 11,000 patients across 33 cancer types, but access is hard because of complex file structures, heterogeneous formats, and the need for programming. We present a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multi-Agent Dynamic Refinement Outperforms Static RAG in Clinical Reasoning for Complex Nephrology Cases](https://www.medrxiv.org/content/10.64898/2026.07.15.26358121v1)
  来源：medRxiv | 日期：2026-07-16 | 相关度：7.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Background: Large language models (LLMs) struggle with dynamic, longitudinal clinical reasoning. We developed a Multi-Stage Iterative Clinical Reasoning Agent framework to address this gap and systematically decouple the...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ReCo: a self-configuring and self-extending agentic framework for biomedical research](https://www.medrxiv.org/content/10.64898/2026.07.14.26358025v1)
  来源：medRxiv | 日期：2026-07-16 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：This study presents ReCo (Research Cosmos), a self-configuring and self-extending agentic research framework for the biomedical domain. ReCo is orchestrated by a large language model that interacts with native computing ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Large Language Model - Enhanced Decision Tree Framework for Identifying Multiple Sclerosis Diagnoses from Clinical Documentation](https://www.medrxiv.org/content/10.64898/2026.07.14.26357416v1)
  来源：medRxiv | 日期：2026-07-17 | 相关度：7.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Background. Early diagnosis and intervention are crucial in multiple sclerosis (MS), yet diagnostic delays are common. Large language models (LLMs) such as generative pre-trained transformers (GPTs) may help streamline d...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Evaluating Voice-Enabled Generative AI for Mental Health: Real-Time Performance and Safety Analyses](https://www.medrxiv.org/content/10.1101/2025.11.14.25340246v2)
  来源：medRxiv | 日期：2026-07-16 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：This study investigates the integration of Voice AI into a locally hosted generative AI chatbot designed to function as a mental health assistant, with the goal of enabling intuitive, voice-based therapeutic interaction....
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [{Sigma}0-EvoCell: An AI-Native Ontology that Unifies Evolutionary and Cell Biology in Latent Space](https://www.biorxiv.org/content/10.64898/2026.07.15.738795v1)
  来源：bioRxiv | 日期：2026-07-16 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：生物学基础模型在分子序列和单细胞转录组的模式识别上表现出色，但在预测遗传扰动效应方面仍逊于简单线性基准，暴露出统计相关性与机制理解之间的脱节。此外，生物知识（如FASTA、SBML）在进入神经网络推理前需进行有损重新编码。本研究提出进化细胞本体（ECO），这是一种基于{Sigma}0底层的AI原生形式语言，将生物知识直接表示为向量编码的关系图。ECO包含16个结构算子，兼具知识符号与张量运算功能，并具有跨越进化与细胞时间尺度的双重语义：...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [The evolutionary processes of bacterial aromatic polyketide ketosynthases](https://www.biorxiv.org/content/10.64898/2026.07.16.738910v1)
  来源：bioRxiv | 日期：2026-07-16 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：细菌芳香聚酮化合物（T2PKs）的生物合成依赖于一组特定的催化剂，即酮合酶（KS）和链长因子（CLF，又称 KSβ），通过迭代方式组装碳骨架并实现精确的链长控制。鉴于实验室发现的 T2PKs 数量日益增多，阐明 KS 和 CLF 的进化轨迹变得至关重要。本研究采用了近期开发的基于大型蛋白质语言模型（PLM）的 MAAPE 算法，对 KS 和 CLF 的进化过程进行了深入分析。研究结果揭示了细菌 T2PKSs 中 KS 和 CLF 结构域...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [A layer-resolved diagnostic identifies bias-driven decisions in deep neural networks](https://www.biorxiv.org/content/10.1101/2025.09.16.676625v7)
  来源：bioRxiv | 日期：2026-07-16 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Modern AI systems can be accurate and confident, but this alone does not reveal whether a decision is well supported by the input. This creates a trust problem because confidence reports how decisive a model is, but not ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Comparing Human and Large Language Model Responses to Patients Online Questions: Towards Multi-dimensional Patient-centered Support](https://www.medrxiv.org/content/10.64898/2026.07.15.26355314v1)
  来源：medRxiv | 日期：2026-07-17 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：患者和护理人员在医疗过程中，尤其是在解读陌生的实验室检测结果时，迫切需要信息和情感支持。虽然患者门户和在线健康社区（OHC）提供了部分帮助，但仍存在服务缺口。大语言模型（LLM）的兴起为协助患者理解和利用检测结果提供了新的补充途径。本研究旨在实证对比 LLM 与 OHC 同伴对包含实验室检测结果的在线问题的回答差异。研究者采用计算与定性相结合的混合方法，对比了来自 OHC 的 122 个实验室检测相关帖子的 519 条同伴回复，以及由四...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Community-Tailored One Health Educational Intervention to Enhance Knowledge and Practices for Zoonotic Disease Prevention in Rural Thailand: a Protocol for a Prospective Cluster Randomised Controlled Trial in Chanthaburi, Thailand (Saan Suk trial)](https://www.medrxiv.org/content/10.64898/2026.07.16.26358293v1)
  来源：medRxiv | 日期：2026-07-18 | 相关度：3.05 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：本研究针对泰国农村人兽共患病溢出风险，制定了名为 Saan Suk 的干预方案。该方案采用以人为中心的设计（HCD），结合健康信念模型与 One Health 原则，旨在通过泰国村卫生志愿者（VHV）系统实施。研究设计为平行臂集群随机对照优效性试验，计划于 2026 年在尖竹汶府 24 个村庄开展，共纳入 1008 名成年受试者。干预组将接受为期四周、每周一次的多模态教育，内容涵盖病原体溢出知识、保护性行为及与野生动物的共处方式。主要评...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Biological Continued Pretraining Reshapes the Capability Profile of a Foundation Model Without Catastrophic Forgetting](https://www.biorxiv.org/content/10.64898/2026.07.06.736700v1)
  来源：bioRxiv | 日期：2026-07-16 | 相关度：2.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：普遍认为，在生物序列等窄领域分布外语料库上进行持续预训练（CPT）会损害通用模型的广泛能力，即产生“灾难性遗忘”。本研究通过分析 26B 参数混合专家模型（Gemma-4-26B-A4B）的三个阶段（指令微调基座、8.7B token 的生物 CPT 后模型、以及随后的 SFT 模型）挑战了这一观点。CPT 语料包含 DNA、蛋白质和生物医学文本。实验涵盖通用知识（MMLU）、代码生成（MBPP）和生物医学知识（BixBench）等维度...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [What Do Generative Models Learn About Adaptive Immune Receptor Repertoires? A Benchmark Study](https://www.biorxiv.org/content/10.64898/2026.07.10.737788v1)
  来源：bioRxiv | 日期：2026-07-16 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：生成模型正越来越多地用于模拟适应性免疫受体库（AIRR）序列分布，有望解码塑造免疫反应的序列多样性并加速治疗性抗体和T细胞受体的设计。然而，目前尚不清楚这些模型是产生了具有生物学意义的输出，还是仅捕获了表层序列统计数据而忽略了受体生成和选择驱动的特征。由于AIRR数据结构复杂且缺乏生物学真值，现有机器学习指标难以直接转化，导致模型评估和选择面临挑战。本研究应用了一套针对AIRR定制的评估指标，系统比较了变分自编码器（VAE）、长短期记忆...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Genomic foundation model embeddings encode higher-order viral genome architecture beyond sequence composition: a benchmark of Evo 2](https://www.biorxiv.org/content/10.64898/2026.07.14.738542v1)
  来源：bioRxiv | 日期：2026-07-16 | 相关度：3.4 | 新颖度：6.5
  匹配主题：pathogenomics
  中文摘要：本研究针对基因组基础模型 Evo 2 在病毒基因组组织表征及序列生成方面的可靠性进行了系统性基准测试。研究利用包含 19,429 个基因组的 RefSeq 病毒语料库（涵盖不同 Baltimore 分类和宿主域），从三个维度评估了 Evo 2：首先，利用线性探针从平均池化嵌入中解码 Baltimore 分类、宿主域和病毒科；其次，通过岭回归探针恢复基因密度、编码比例和基因重叠等高阶架构特征；最后，在排除于训练集之外的真核病毒集上测试片段...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [MINA: linear probes reveal coding-sequence family signal in frozen DNA encoders up to protein composition](https://www.biorxiv.org/content/10.64898/2026.05.25.727711v3)
  来源：bioRxiv | 日期：2026-07-16 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：冻结的 DNA 编码器常被用作特征提取器，但微调过程往往掩盖了其固定嵌入向量中已包含的线性可访问信息。本研究引入了 MINA（核苷酸架构模型询问），这是一个轻量级基准测试，旨在评估冻结的 DNA 嵌入是否能恢复：(i) 五类蛋白质家族标签，以及 (ii) 每个基因的 1,536 维 GenePT 自然语言嵌入。实验对比了编码序列（CDS）和转录起始位点（TSS）背景，采用同源性感知划分，并与翻译后的组成成分及蛋白质语言模型基准进行比较。...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Predicting the protein interaction landscape of a mycobacterial pathogen](https://www.biorxiv.org/content/10.64898/2026.07.15.738315v1)
  来源：bioRxiv | 日期：2026-07-16 | 相关度：4.6 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：细菌功能缺失突变库的高维表型筛选已确定了数千个基因间的联系，但阐明其底层机制仍处于低通量阶段。本研究展示了基于 AI 的全蛋白质组蛋白质相互作用（PPI）预测在弥补这一差距方面的效用。研究利用 pooled-AlphaFold3 评估了麻风分枝杆菌（Mycobacterium leprae）蛋白质组中约 130 万种可能的两两相互作用。研究识别出约 2,000 个强及中等强度的 PPI，这些相互作用解释了在结核分枝杆菌、耻垢分枝杆菌和谷...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Parameter-efficient deep learning for pneumonia detection on chest X-rays: A comparative evaluation of explainable AI methods](https://www.medrxiv.org/content/10.64898/2026.07.14.26358065v1)
  来源：medRxiv | 日期：2026-07-16 | 相关度：2.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：肺炎是全球感染性疾病死亡的主要原因，每年导致约250万人死亡，其中5岁以下儿童占15%。胸部X射线是主要的诊断工具，但其准确解读高度依赖放射学专家，导致医疗资源匮乏地区的诊断缺口。本研究针对大型深度学习模型在资源受限环境下计算可行性低及“黑盒”模型缺乏解释性的问题，提出了一种基于迁移学习的参数高效深度学习框架。研究对比了EfficientNet-B0（微调）、ResNet50和DenseNet121三种架构，并在包含5,863张图像的K...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Machine Learning for Microbial Cell Factories: Pathway Design, Enzyme Engineering, and Metabolic Regulation.](https://pubmed.ncbi.nlm.nih.gov/42359840/)
  来源：PubMed | 日期：2026-07-17 | 相关度：2.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：微生物细胞工厂是生产燃料、化学品和药物的可持续平台，但其发展受限于代谢途径发现、酶优化和代谢调节等挑战。人工智能与机器学习的最新进展正在重塑该领域，实现了预测性途径设计、增强的蛋白质工程和动态网络调节。图神经网络（GNN）、生成模型和强化学习（RL）等新兴策略，能够以更高的准确性和可扩展性系统地探索庞大的设计空间。本综述重点介绍了微生物工程的最新进展，讨论了 AI 驱动的框架如何推动该领域从经验引导和基于规则的工程转向数据驱动、模型辅助...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Conditional superiorities and unaddressed bottlenecks: a critical review of artificial intelligence for waterborne microbial detection.](https://pubmed.ncbi.nlm.nih.gov/42467233/)
  来源：PubMed | 日期：2026-07-17 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：尽管传统的水样微生物检测方法应用广泛，但仍存在检测周期长（24-72小时）、灵敏度低且缺乏实时监测能力等缺陷。人工智能（AI）在特定实验环境下展现出有条件的优势，例如在低浊度水中检测隐孢子虫和贾第鞭毛虫时，基于约12,000张标注图像并采用五折交叉验证，其实验室灵敏度可达99%；然而，在高浊度水基质或训练数据集不足时，这些优势往往会显著减弱。本综述批判性地评估了四类AI驱动的方法：基于图像的分析、光谱技术、基因组和宏基因组测序以及污染预...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
