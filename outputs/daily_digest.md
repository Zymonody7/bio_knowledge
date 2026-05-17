# 每日论文监控日报 (2026-05-17)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 30 篇新论文。

## 抓取状态

- arXiv：成功，命中 17 篇
- PubMed：成功，命中 46 篇
- bioRxiv：成功，命中 9 篇
- medRxiv：成功，命中 4 篇

## 最值得看

### Foundation Model / Agent

- [Bio-BLIP: A Multimodal Architecture for Transferable Reasoning in Genomic Variant Interpretation](https://www.biorxiv.org/content/10.64898/2026.05.12.724740v1)
  来源：bioRxiv | 日期：2026-05-15 | 相关度：8.9 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Developing scientific hypotheses in biology requires integrating heterogeneous evidence across DNA sequence, gene context, protein function, and prior literature. Existing multimodal AI systems expose biological evidence...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OmniGene-4: A Unified Bio-Language MoE Model with Router-Level Interpretability](https://www.biorxiv.org/content/10.64898/2026.05.12.724542v1)
  来源：bioRxiv | 日期：2026-05-14 | 相关度：7.15 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Mixture-of-Experts (MoE) architectures offer a rare opportunity to probe the internal organization of large language models, but this affordance has not been systematically exploited in biological foundation modeling. We...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [MethylCurate: Tool For Dataset Curation and Epigenetic Aging Clock Evaluation](https://www.biorxiv.org/content/10.64898/2026.05.11.723515v1)
  来源：bioRxiv | 日期：2026-05-14 | 相关度：7.15 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：SummaryDNA methylation datasets from public repositories such as NCBI Gene Expression Omnibus are central to the development and evaluation of epigenetic aging clocks, yet existing resources and tools do not fully resolv...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

## 可追踪

### Foundation Model / Agent

- [Towards Label-Free Single-Cell Phenotyping Using Multi-Task Learning](http://arxiv.org/abs/2605.14717v1)
  来源：arXiv | 日期：2026-05-14 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Label-free single-cell imaging offers a scalable, non-invasive alternative to fluorescence-based cytometry, yet inferring molecular phenotypes directly from bright-field morphology remains challenging. We present a unifi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A fully open structure-guided RNA foundation model for robust structural and functional inference](https://www.biorxiv.org/content/10.1101/2025.08.06.668731v2)
  来源：bioRxiv | 日期：2026-05-14 | 相关度：6.8 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：RNA language models have achieved strong performances across diverse downstream tasks by leveraging large-scale sequence data. However, RNA function is fundamentally shaped by its hierarchical structure, making the integ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RAPO++: Cross-Stage Prompt Optimization for Text-to-Video Generation via Data Alignment and Test-Time Scaling](http://arxiv.org/abs/2510.20206v2)
  来源：arXiv | 日期：2025-10-23 | 相关度：6.55 | 新颖度：1.7
  匹配主题：foundation_model_agent
  中文摘要：Prompt design plays a crucial role in text-to-video (T2V) generation, yet user-provided prompts are often short, unstructured, and misaligned with training data, limiting the generative potential of diffusion-based T2V m...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Simulating population compliance with pandemic interventions using large language models](https://www.medrxiv.org/content/10.64898/2026.05.12.26352942v1)
  来源：medRxiv | 日期：2026-05-15 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Effective pandemic response requires accurate modeling of population compliance with non-pharmaceutical interventions (NPIs), yet most epidemic models treat behavioral change as fixed scenarios rather than an emergent pr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Is Grep All You Need? How Agent Harnesses Reshape Agentic Search](http://arxiv.org/abs/2605.15184v1)
  来源：arXiv | 日期：2026-05-14 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in Large Language Model (LLM) agents have enabled complex agentic workflows where models autonomously retrieve information, call tools, and reason over large corpora to complete tasks on behalf of users. ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [MetaGEM: Bottom-Up Reconstruction of Genome-Scale Metabolic Networks via Deep Enzyme-Metabolite Anchoring](http://arxiv.org/abs/2605.14812v1)
  来源：arXiv | 日期：2026-05-14 | 相关度：8.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Genome-scale metabolic models (GEMs) are essential tools for systems biology and rational chassis design, but conventional top-down reconstruction depends heavily on sequence homology and often leaves unknown enzymes and...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Prompt-Only Gene-Circuit Modeling with a Large Language Model Simulates the synNotch Spheroids.](https://pubmed.ncbi.nlm.nih.gov/41968604/)
  来源：PubMed | 日期：2026-05-15 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Morphogenesis emerges from gene regulatory circuits that translate biochemical cues into spatially organized cell fates; yet, constructing quantitative simulations of these processes remains technically demanding. Here, ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Toward scalable early cancer detection: evaluating EHR-based predictive models against traditional screening criteria.](https://pubmed.ncbi.nlm.nih.gov/42141079/)
  来源：PubMed | 日期：2026-05-15 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Current cancer screening guidelines cover only a few cancer types and rely on narrowly defined criteria such as age or a single risk factor like smoking history, to identify high-risk individuals. Predictive models using...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Privacy-preserving local language models accurately identify the presence and timing of self-harm in electronic mental health records](https://www.medrxiv.org/content/10.1101/2025.10.27.25338892v2)
  来源：medRxiv | 日期：2026-05-16 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Background: Self-harm, defined as intentional self-injury or self-poisoning irrespective of motivation, is the strongest risk factor for suicide and an important outcome for mental health care. Although highly prevalent ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [MechAInistic: An LLM-guided Multi-Agent System for Reasoning over Genome-Scale Constraint-Based Metabolic Models](https://www.biorxiv.org/content/10.64898/2026.05.11.723319v2)
  来源：bioRxiv | 日期：2026-05-14 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Constraint-based metabolic modeling is a powerful way to study the mechanistic basis of cellular states and disease, but effective use demands substantial computational expertise and careful coordination of multi-step an...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [GGBound: A Genome-Grounded Agent for Microbial Life-Boundary Prediction](http://arxiv.org/abs/2605.14442v1)
  来源：arXiv | 日期：2026-05-14 | 相关度：2.4 | 新颖度：1.5
  匹配主题：未命中具体主题
  中文摘要：预测微生物菌株的生理生命边界（如温度、pH、盐度、底物利用和形态）对生物技术和生态学至关重要，但传统方法依赖耗时的体外筛选。现有计算方法多将生理特征视为孤立的监督目标，或仅将生物基础模型作为静态编码器，未能有效弥合基因型与表型间的鸿沟。本研究将微生物生命边界预测定义为统一的“基因组到生理”任务，并开发了受基因组约束且具备工具增强能力的LLM智能体GGBound。研究团队从IJSEM、NCBI和BacDive整理了一个包含1,525个菌株...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond AI as Assistants: Toward Autonomous Discovery in Cosmology](http://arxiv.org/abs/2605.14791v1)
  来源：arXiv | 日期：2026-05-14 | 相关度：2.1 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：人工智能（AI）智能体的最新进展正推动 AI 从辅助工具向自主科学发现转型。本文讨论了宇宙学领域两种互补的智能体系统：	exttt{CMBEvolve} 和 	exttt{CosmoEvolve}。	exttt{CMBEvolve} 针对具有明确定量目标的任务，通过大语言模型（LLM）引导的代码演化和树搜索实现目标优化；而 	exttt{CosmoEvolve} 则通过虚拟多智能体研究实验室，处理开放式科学工作流。初步演示中，	extt...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Falkor-IRAC: Graph-Constrained Generation for Verified Legal Reasoning in Indian Judicial AI](http://arxiv.org/abs/2605.14665v1)
  来源：arXiv | 日期：2026-05-14 | 相关度：2.1 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：法律推理并非简单的语义相似性搜索，而是涉及先例传播、程序状态转换和受法规约束的推理。传统的向量检索增强生成（RAG）无法忠实呈现这些属性，常导致虚假先例、过时引用和推理链断裂。本文提出 Falkor-IRAC，一个针对印度法律 AI 的图约束生成框架。该框架将印度最高法院和高等法院的判决书转化为包含 IRAC（问题、规则、分析、结论）节点结构的知识图谱，并存储在 FalkorDB 中以实现低延迟代理遍历。在推理阶段，LLM 生成的答案必...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BiomniBench: Process-level Evaluation of LLM Agents for Real-world Biomedical Research](https://www.biorxiv.org/content/10.64898/2026.05.12.724604v1)
  来源：bioRxiv | 日期：2026-05-14 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：LLM智能体已开始执行真实的生物医学研究，但对其进行严谨评估仍具挑战。仅关注结果的基准测试存在两大缺陷：一是正确答案可能源于记忆、奖励黑客攻击或偶然的错误推理；二是有效的替代分析方案常因与参考答案不符而被误判。为此，我们推出了BiomniBench，这是一个过程级评估框架，根据专家设计的任务特定准则对智能体的完整执行轨迹进行评分。其首个实例BiomniBench-DA包含100个数据分析任务，涵盖17种分析类型、5个疾病领域及通用生物学...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Does RAG Know When Retrieval Is Wrong? Diagnosing Context Compliance under Knowledge Conflict](http://arxiv.org/abs/2605.14473v1)
  来源：arXiv | 日期：2026-05-14 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）中的“上下文合规机制”是指当检索到的上下文与模型参数知识发生冲突时，上下文仍主导最终答案的现象。仅靠准确率指标无法揭示冲突下上下文如何因果性地塑造答案。本研究引入了上下文驱动分解（CDD），这是一种在推理阶段运行的信念分解探针，可作为受控检索冲突的干预机制。通过 Epi-Scale 压力测试、TruthfulQA 误解注入（N=500）及跨模型实验，CDD 揭示了三种模式：首先，上下文合规性在对抗设置下是可衡量的，...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Identification of race-specific QTL and candidate genes for Aphanomyces root rot resistance in alfalfa (Medicago sativa L.).](https://pubmed.ncbi.nlm.nih.gov/42132231/)
  来源：PubMed | 日期：2026-05-14 | 相关度：6.75 | 新颖度：0.25
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：Aphanomyces root rot (ARR), caused by the oomycete Aphanomyces euteiches, is one of the most devastating diseases of alfalfa in the United States. Two pathogenic races of A. euteiches have been identified, with most comm...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ToolMol: Evolutionary Agentic Framework for Multi-objective Drug Discovery](http://arxiv.org/abs/2605.12784v2)
  来源：arXiv | 日期：2026-05-12 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Advances in large language models (LLMs) have recently opened new and promising avenues for small-molecule drug discovery. Yet existing LLM-based approaches for molecular generation often suffer from high rates of invali...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Deepchecks: Evaluating Retrieval-Augmented Generation (RAG)](http://arxiv.org/abs/2605.14488v1)
  来源：arXiv | 日期：2026-05-14 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：大语言模型（LLM）结合检索增强生成（RAG）技术正在医疗、金融和客户服务等多个领域引发变革。尽管潜力巨大，但由于生成输出的随机性以及检索与生成组件之间复杂的相互作用，评估 RAG 系统仍是一项复杂的挑战。本文介绍了 Deepchecks，这是一个专门为评估 RAG 应用而量身定制的综合框架。Deepchecks 的评估框架通过多维度方法、根本原因分析和生产监控来解决 RAG 应用的评估问题。通过确保评估过程与特定应用的需求保持一致，该...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Not All RAGs Are Created Equal: A Component-Wise Empirical Study for Software Engineering Tasks](http://arxiv.org/abs/2605.14503v1)
  来源：arXiv | 日期：2026-05-14 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：检索增强生成（RAG）正被广泛用于将大语言模型（LLM）与软件工件结合，但其组件的最优配置在软件工程（SE）任务中仍不明确，导致从业者常陷入高成本的试错。本研究对 RAG 流水线进行了全面的组件级实证研究，评估了超过 21 种模型和方法。研究系统地隔离并评估了 4 种查询处理技术、7 种涵盖稀疏、密集和混合范式的检索模型、4 种上下文精炼方法以及 6 种不同的生成器。我们在代码生成、摘要和修复这三类核心 SE 任务上测试了这些组件。实证...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [From Scenes to Elements: Multi-Granularity Evidence Retrieval for Verifiable Multimodal RAG](http://arxiv.org/abs/2605.15019v1)
  来源：arXiv | 日期：2026-05-14 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：多模态检索增强生成（RAG）系统通常在粗粒度（如整张图像或场景）上检索证据，这导致其与细粒度的用户查询之间存在不匹配，且使得系统失效的原因难以验证。本研究引入了 GranuVistaVQA，这是一个包含真实世界地标的多模态基准测试，具有跨多个视角的元素级标注，能够捕捉单个图像仅包含实体子集的局部观测挑战。此外，我们提出了 GranuRAG 框架，该框架将视觉元素视为一级检索单元，分为三个阶段：元素级检测与分类、用于证据检索的多粒度跨模态...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [OneSearch-V2: The Latent Reasoning Enhanced Self-distillation Generative Search Framework](http://arxiv.org/abs/2603.24422v2)
  来源：arXiv | 日期：2026-03-25 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：生成式检索（GR）已成为现代搜索系统的关键范式，相比传统多级级联架构，具有端到端联合优化和高计算效率的优势。针对工业级框架 OneSearch 在复杂查询理解不足、潜在意图挖掘低效以及对历史偏好过拟合等局限性，本文提出 OneSearch-V2。该框架引入了三大创新：首先是思维增强的复杂查询理解模块，通过深度语义解析克服了直接推理的浅层匹配限制；其次是推理内化的自蒸馏训练流水线，利用隐式上下文学习挖掘用户精准的电商意图；最后是行为偏好对...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Evidence Behind the Automation of Clinical Trial Statistical Programming: A Scoping Review of Technology Adoption, Validation Frameworks, and AI/ML Integration (2020-2025)](https://www.medrxiv.org/content/10.64898/2025.12.24.25342988v2)
  来源：medRxiv | 日期：2026-05-15 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Background: Clinical trial statistical programming is transitioning from manual, study-specific coding toward metadata-driven, automated pipelines. Although general data management transformation has been reviewed, compr...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Clinical Safety of AI-Generated Antibiotic Prescribing Advice: Guideline Adherence and Misinformation Risk Among Large Language Models](https://www.medrxiv.org/content/10.64898/2026.05.13.26352828v1)
  来源：medRxiv | 日期：2026-05-15 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Background: Large language models (LLMs) are increasingly used in telehealth, but their safety in antibiotic prescribing remains uncertain, particularly in the presence of patient misinformation. Methods: A cross-section...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Osteoarthritis phenotypes: advancing precision medicine through clinical, structural, and molecular stratification.](https://pubmed.ncbi.nlm.nih.gov/42141125/)
  来源：PubMed | 日期：2026-05-15 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：骨关节炎（OA）被视为一种由生物学、生物力学、代谢、遗传和分子机制驱动的异质性综合征，这解释了其疾病进展和治疗反应的差异。本综述通过检索2010-2026年间的主要数据库和国际骨关节炎研究协会（OARSI）资源，对临床、影像和分子领域的证据进行了主题综合。研究识别出多种OA表型：炎症型、代谢型、生物力学型、软骨-软骨下骨型、疼痛致敏型及衰老型。影像学表型（如半月板-软骨型、肥大型等）与分子内型（如低周转、结构损伤、系统性炎症）进一步细化...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Beyond data and technology: the need for new thinking to enable the era of precision prevention.](https://pubmed.ncbi.nlm.nih.gov/42135719/)
  来源：PubMed | 日期：2026-05-14 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：全球旗舰计划日益倡导从反应式、以疾病为中心的医疗模式转向主动健康维护。精准预防被定义为在从潜在风险、疾病前期到临床表现的疾病连续体中，对因果路径进行针对性调节，这超越了传统的群体水平风险因素管理。然而，传统的研发与实施模式已无法匹配当前的科技进步。本综述概述了扩展精准预防的主要障碍，并主张将概念、方法和政策视角整合为单一的实施导向框架。个体化风险分层是精准预防的核心：基因组学作为终身易感性评估的基础，而多因素慢性病的预测则需结合动态中间...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Emotion-Attended Stateful Memory (EASM):The Architecture for Hyper-Personalization at Scale](http://arxiv.org/abs/2605.14833v1)
  来源：arXiv | 日期：2026-05-14 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Current language model systems remain fundamentally stateless across sessions, limiting their ability to personalize interactions over time. While retrieval-augmented generation and fine-tuning improve knowledge access a...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [When Retrieval Hurts Code Completion: A Diagnostic Study of Stale Repository Context](http://arxiv.org/abs/2605.14478v1)
  来源：arXiv | 日期：2026-05-14 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：检索增强的代码生成（RAG）依赖于跨文件的仓库上下文，但检索到的片段可能来自过时的项目状态。本研究旨在探讨时间上过时的仓库片段是仅作为无害噪声，还是会主动诱导生成与当前状态不兼容的代码。研究者针对 5 个 Python 仓库中 17 个生产环境辅助函数签名的变更进行了受控诊断研究。实验对比了仅当前、仅过时、无检索以及当前/过时混合检索四种条件，并在提示词中隐藏了提交新鲜度和预期签名。结果显示，在仅过时检索条件下，Qwen2.5-Code...
  为什么值得看：When Retrieval Hurts Code Completion: A  与你的主题有弱匹配，暂时保留作低优先级跟踪。
