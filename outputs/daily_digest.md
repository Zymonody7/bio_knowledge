# 每日论文监控日报 (2026-07-25)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 35 篇新论文。

## 抓取状态

- arXiv：成功，命中 21 篇
- PubMed：成功，命中 56 篇
- bioRxiv：成功，命中 11 篇
- medRxiv：成功，命中 11 篇

## 最值得看

### Foundation Model / Agent

- [Small but Specialized: A Domain-Adapted Retrieval-Augmented LLM Outperforms Frontier Generalists in Pediatric and Adolescent Gynecology](https://www.medrxiv.org/content/10.64898/2026.07.22.26358688v1)
  来源：medRxiv | 日期：2026-07-24 | 相关度：7.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Background. Pediatric and adolescent gynecology (PAG) is a highly specialized field where timely, accurate clinical guidance can prevent serious harm to a vulnerable population, yet most general-purpose large language mo...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [Antigen-specific Antibody Multi-modal Foundation Model for Functional Antibody Design](http://arxiv.org/abs/2607.20057v1)
  来源：arXiv | 日期：2026-07-22 | 相关度：7.8 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Antibodies are essential proteins that play a central role in immune recognition by binding specific antigen molecules. Although recent protein language models have enabled progress in single-chain protein modeling and g...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A unified 12-lead ECG-language model for interpretation and clinical-endpoint prediction](https://www.medrxiv.org/content/10.64898/2026.07.22.26358591v1)
  来源：medRxiv | 日期：2026-07-24 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Automated electrocardiogram (ECG) interpretation has advanced, yet most systems remain narrow classifiers that emit fixed labels rather than the narratives or endpoint-specific answers clinicians need. Generative approac...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SleepGPT: A Sleep Stage Language Model for Efficient Sleep Assessment](https://www.medrxiv.org/content/10.1101/2024.10.26.24316166v5)
  来源：medRxiv | 日期：2026-07-23 | 相关度：7.15 | 新颖度：2.25
  匹配主题：foundation_model_agent
  中文摘要：Background: Accurate and scalable sleep assessment is essential for the diagnosis of sleep disorders and the advancement of personalized sleep medicine. Current clinical practice relies predominantly on in-laboratory pol...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Using Deep Learning to predict replication timing reveals baseline control of genomic DNA sequence](https://www.biorxiv.org/content/10.64898/2026.07.18.739304v1)
  来源：bioRxiv | 日期：2026-07-22 | 相关度：6.8 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Human DNA replicates according to a precise schedule: certain regions are replicated early, while others replicate later in the cell cycle. The DNA sequence and the epigenome are both indicative for replication timing (R...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PennySynth: RAG-Driven Data Synthesis for Automated Quantum Code Generation](http://arxiv.org/abs/2605.25572v2)
  来源：arXiv | 日期：2026-05-25 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：The growing complexity of quantum programming frameworks has exposed a critical limitation in existing large language model (LLM)-based code assistants: general-purpose models hallucinate PennyLane-specific gate names, m...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Efficacy of a Large Language Model Data Extraction System in Evidence Reviews for Emerging Infectious Diseases: A Randomized Crossover Trial.](https://pubmed.ncbi.nlm.nih.gov/42494833/)
  来源：PubMed | 日期：2026-07-01 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Rapid evidence synthesis during emerging infectious and re-emerging disease outbreaks is critical, yet traditional systematic reviews rarely meet urgent timelines. Large language models (LLMs) may accelerate evidence syn...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Reducing Hallucinations in Complex Question Answering using Simple Graph-based Retrieval-Augmented Generation (long version)](http://arxiv.org/abs/2606.05901v2)
  来源：arXiv | 日期：2026-06-04 | 相关度：6.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have fundamentally transformed the landscape of Natural Language Processing (NLP), although they remain susceptible to errors. Retrieval-augmented generation (RAG) systems have emerged as a c...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Omics Data Discovery Agents: Agent-Supported Retrieval, Reanalysis, and Synthesis of Published Omics Data](http://arxiv.org/abs/2603.10161v3)
  来源：arXiv | 日期：2026-03-10 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：The biomedical literature contains a vast collection of omics studies, yet most published data remain functionally inaccessible for computational reuse. When raw data are deposited in public repositories, essential infor...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GoMA-DTA: A Gene Ontology-Guided Multimodal Attention Fusion Model for Drug-Target Affinity Prediction.](https://pubmed.ncbi.nlm.nih.gov/42497056/)
  来源：PubMed | 日期：2026-07-24 | 相关度：7.1 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Accurate prediction of drug-target affinity (DTA) is essential for accelerating drug discovery. Although pretrained protein language models have achieved significant progress, existing methods predominantly focus on bott...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [VizRAG: Enhancing Retrieval-Augmented Generation with Hypergraph Visualization](http://arxiv.org/abs/2607.19830v1)
  来源：arXiv | 日期：2026-07-22 | 相关度：6.8 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Hypergraph-based RAG systems surpass traditional graph-based approaches by organizing complex n-ary atomic facts among entities, rather than relying solely on binary relationships. Despite the advancements in multimodal ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Clinical Impact, Diagnostic Performance, and Prognostic Implications of Plasma Metagenomic Next-Generation Sequencing in Solid Organ Transplant Recipients](https://www.medrxiv.org/content/10.64898/2026.07.02.26357172v2)
  来源：medRxiv | 日期：2026-07-24 | 相关度：8.1 | 新颖度：0.75
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Background: Plasma metagenomic next-generation sequencing (mNGS) may detect pathogens in solid organ transplant (SOT) recipients, but optimal patient selection and result interpretation remain uncertain. Methods: We stud...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Graph Lens Lite: A browser-based tool for interactive visualization and exploration of biological networks](https://www.biorxiv.org/content/10.64898/2026.02.25.708026v3)
  来源：bioRxiv | 日期：2026-07-22 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Biological network visualization together with graph-based analyses are key techniques in systems biology and network medicine to detect patterns and generate hypotheses regarding disease pathobiology, drug target identi...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial intelligence-based methods and applications in clinical and diagnostic microbiology: Current challenges and future perspectives.](https://pubmed.ncbi.nlm.nih.gov/42492779/)
  来源：PubMed | 日期：2026-07-23 | 相关度：4.7 | 新颖度：5.25
  匹配主题：pathogenomics
  中文摘要：微生物实验室在传染病诊断和管理中发挥着关键作用。为减少人力工作量并缩短诊断耗时，人工智能（AI）技术，特别是机器学习（ML）和深度学习（DL），已在微生物实验室诊断中展现出显著贡献。通过这些方法，分子诊断、基因测序、微生物元分析及相关领域获得了更快速、更准确的分析能力。除诊断应用外，AI 正越来越多地应用于基因组学、宏基因组学、抗菌药物耐药性（AMR）预测以及药物和疫苗发现，实现了更全面且数据驱动的微生物分析。本综述全面评估了当前微生物...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Initial-Visit Specialty Triage in Rare Diseases Using Large Language Models: Retrospective Benchmarking Study.](https://pubmed.ncbi.nlm.nih.gov/42490550/)
  来源：PubMed | 日期：2026-07-23 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Specialty triage at first contact is an overlooked step in early diagnostic pathways for rare diseases. Patients often present with overlapping, multisystem, and atypical manifestations, making first-visit specialty sele...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Risk Perception to Behavior Large Language Models-Based Simulation of Pandemic Prevention Behaviors](http://arxiv.org/abs/2601.03552v2)
  来源：arXiv | 日期：2026-01-07 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Individual prevention behaviors are a primary line of defense during the early stages of novel infectious disease outbreaks, yet their adoption is heterogeneous and difficult to forecast-especially when empirical data ar...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Reinforcement Learning for Large Language Model Selective Evidence Adoption from Contaminated Retrieval Results](http://arxiv.org/abs/2607.20090v1)
  来源：arXiv | 日期：2026-07-22 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented large language models frequently face contexts that interleave useful evidence with misleading statements or instruction-like content. Blanket refusal discards valid evidence, whereas uncritical adopt...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [IteraSim RAG: A Multi-Stage Retrieval-Augmented Agentic Back-End for OpenFOAM-Based Computational Fluid Dynamics](http://arxiv.org/abs/2607.20346v1)
  来源：arXiv | 日期：2026-07-22 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Configuring a computational fluid dynamics (CFD) case in OpenFOAM requires assembling a multi-directory input deck of mutually consistent solver, discretisation and boundary-condition dictionaries -- a task that remains ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MechAInistic: An LLM-guided Multi-Agent System for Reasoning over Genome-Scale Constraint-Based Metabolic Models](https://www.biorxiv.org/content/10.64898/2026.05.11.723319v4)
  来源：bioRxiv | 日期：2026-07-22 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：LLM agents are increasingly used for scientific reasoning, but their fluent-sounding outputs can diverge from verifiable computational evidence, limiting their reliability for biomedical hypothesis generation. We develop...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evaluating Large Language Models for Colonoscopy Preparation Assistance: Correctness and Diversity in Synthetic Dialogues](https://www.medrxiv.org/content/10.1101/2025.11.19.25340596v3)
  来源：medRxiv | 日期：2026-07-22 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Background: Colorectal cancer is a leading cause of cancer-related deaths in the United States, and colonoscopy remains the gold standard for early detection and prevention. However, many procedures are postponed due to ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Uni-XAS: Alignment-Driven Bidirectional Multimodal Learning for X-ray Absorption Spectroscopy](http://arxiv.org/abs/2607.20906v1)
  来源：arXiv | 日期：2026-07-23 | 相关度：2.75 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：X射线吸收光谱（XAS）是探测局部原子环境的关键技术，但建模需桥接1D连续光谱与3D原子结构这两种异构模态。现有方法通常将前向光谱预测与逆向结构推断解耦为独立的回归任务，阻碍了共享表示学习，且原子置换歧义限制了逆向建模生成显式3D结构。本研究提出Uni-XAS，一个将双向XAS建模重构为跨模态对齐与条件生成问题的统一框架。首先，XASLip通过物理感知光谱编码器与吸收体感知流形优化策略，解决细粒度元素内配位变化。在此共享潜空间上，通过检...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [GRADRAG: Cross-Component Prompt Adaptation for Coordinated Multi-Agent RAG](http://arxiv.org/abs/2607.21324v1)
  来源：arXiv | 日期：2026-07-23 | 相关度：2.1 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）系统日益采用多LLM智能体协作，但现有工作多孤立优化各组件，缺乏全链路协同。本文提出 GRADRAG 框架，旨在实现跨组件的提示词适配。该框架将 RAG 流水线建模为计算图，通过传播结构化评估反馈来更新上游智能体。具体而言，评估器（Evaluator）对下游生成的回答及支持证据进行批判性分析，生成可操作的反馈，由提示词优化器（Prompt Optimizer）据此迭代更新检索器、图构建器和回答器等自适应智能体；同时...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OpenCosmo: Community Portal and Analysis Framework for Flagship Cosmological Simulations](http://arxiv.org/abs/2607.16059v3)
  来源：arXiv | 日期：2026-07-17 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：宇宙学是一门精密观测科学，大型模拟是其分析的核心。然而，这些模拟计算成本极高且产生海量复杂数据，共享这些数据对于实现其科学价值至关重要。本文介绍了 OpenCosmo 项目，该项目为基于 HACC 框架的旗舰级宇宙学模拟提供灵活的访问与分析。通过 Web 门户（https://opencosmo.science），用户可以获取包括两万亿粒子的 Frontier-E 纯重力模拟、Last Journey、Discovery 以及 64 成...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AttriMem: Attribution-Guided Process Feedback for Agent Memory Learning](http://arxiv.org/abs/2607.21106v1)
  来源：arXiv | 日期：2026-07-23 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：有效的记忆对大语言模型（LLM）智能体至关重要，但其构建仍具挑战。记忆构建策略决定了在交互积累过程中提取、存储、更新、压缩或丢弃哪些信息。启发式方法依赖主观且特定于任务的规则，导致其与下游目标失配并限制了跨任务适应性。相比之下，基于强化学习（RL）的方法虽能从反馈中学习，但主要利用粗粒度的结果或模块级奖励，难以识别支撑最终答案的中间记忆内容，存在信用分配瓶颈。由于中间决策缺乏唯一真值，且信用随推理轨迹变化，构建过程反馈极难。为此，我们提...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [DB-ATRG: The Density and BI-RADS-Aware Triage and Automatic Report Generation System for Mammography](https://www.medrxiv.org/content/10.64898/2026.07.22.26358655v1)
  来源：medRxiv | 日期：2026-07-23 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Background: The growing volume of mammography screenings has created severe radiologist shortages, while standard First-In, First-Out (FIFO) reading queues fail to prioritize urgent or complex cases, delaying critical di...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Foundation-model-guided radiogenomic discovery linking cancer genomes to cancer scans](http://arxiv.org/abs/2607.20583v1)
  来源：arXiv | 日期：2026-07-22 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：The function of many genes is still unknown, and conventional driver-discovery methods, which rely on how frequently a gene is mutated, cannot assess genes that are only rarely affected. Here we pair Evo~2-based genome a...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [The use of artificial intelligence in advancing molecular biology in Africa: a narrative review.](https://pubmed.ncbi.nlm.nih.gov/42481850/)
  来源：PubMed | 日期：2026-07-22 | 相关度：5.55 | 新颖度：1.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Artificial intelligence (AI) is rapidly becoming a core methodological pillar of molecular biology and precision medicine, and Africa is a uniquely consequential setting for this transition because the continent combines...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [TeaRAG: A Token-Efficient Agentic Retrieval-Augmented Generation Framework](http://arxiv.org/abs/2511.05385v2)
  来源：arXiv | 日期：2025-11-07 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) utilizes external knowledge to augment Large Language Models' (LLMs) reliability. For flexibility, agentic RAG employs autonomous, multi-round retrieval and reasoning to resolve queri...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GeneKnow: An auditable AI framework for source-grounded biological evidence synthesis](https://www.biorxiv.org/content/10.64898/2026.05.28.728511v2)
  来源：bioRxiv | 日期：2026-07-23 | 相关度：2.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：生物功能具有高度的背景依赖性，但在特定细胞类型、疾病或扰动下合成基因功能的证据仍是一项劳动密集型工作。本文提出了 GeneKnow，这是一个用于源头导向型生物证据合成的可审计人工智能（AI）框架。GeneKnow 将关键的证据操作（包括文献检索、段落选择、出处追踪和参考文献构建）与仅限于语义分析和文献合成的生成步骤分离。该框架支持多论文发现和单论文检查，同时保留合成断言与源段落之间的链接，从而生成不含虚假引用且最大限度减少幻觉的可信合成...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Enhancing Title and Abstract Priority Screening Through EdRoSi AI Pipeline.](https://www.medrxiv.org/content/10.64898/2026.06.26.26356718v2)
  来源：medRxiv | 日期：2026-07-23 | 相关度：2.1 | 新颖度：1.75
  匹配主题：未命中具体主题
  中文摘要：系统综述中证据的详尽识别至关重要，但题目和摘要筛选环节耗时耗力。优先筛选（Priority screening）作为一种主动学习方法，通过相关性排序减少工作量，其效率通常以100%召回率下的工作节省量（WSS@100%）来衡量。尽管现有模型在基准数据集上表现良好，但在处理某些挑战性数据集时，检索最后几个稀有的相关文献仍存在困难。本研究利用SYNERGY基准数据集证明，ASReview LAB v.2中的ELAS_h3模型在检索最后少数相...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Systematic evaluation of single-cell foundation model interpretability: attention-derived edge scores add no incremental value over gene-level features for perturbation-target prediction.](https://pubmed.ncbi.nlm.nih.gov/42482180/)
  来源：PubMed | 日期：2026-07-22 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：本研究对单细胞基础模型（如 scGPT 和 Geneformer）的可解释性进行了系统评估，重点探讨注意力权重在基因调控网络（GRN）推断和扰动目标预测中的作用。研究构建了一个包含 37 项分析和 153 个统计测试的评估框架，涵盖 scGPT 和 Geneformer V2-316M 两种架构，涉及 K562、RPE1 等 4 种细胞类型及 CRISPRi/a 两种扰动模式。结果表明，注意力模式确实编码了层特异性生物结构（早期层为蛋白...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Brain network-based stratification of mental health disorders: design and cohort description of the STRATIFY and ESTRA studies.](https://pubmed.ncbi.nlm.nih.gov/42486943/)
  来源：PubMed | 日期：2026-07-22 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：STRATIFY（基于脑网络的强化相关障碍分层）和 ESTRA（进食障碍分层）研究旨在建立一个基于机制的精神疾病分层框架。本研究描述了其设计、方法及队列特征。两项研究共同调查了大脑结构与功能的网络属性，以及源自血液的基因组学、表观基因组学和蛋白质组学生物标志物，如何与跨越重度抑郁症、酒精使用障碍、精神病和进食障碍的强化相关行为产生关联。核心目标是识别能够预测疾病发作、症状演变和功能结果的判别性多模态特征，以支持精准干预。研究共招募了 6...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Coarse-to-Fine Long-term Interest Modeling for Generative Recommendation](http://arxiv.org/abs/2602.05663v2)
  来源：arXiv | 日期：2026-02-05 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：利用长期用户行为模式是提升现代推荐系统准确性的关键。尽管生成式推荐系统已成为一种变革性范式，但在有效建模超长历史序列方面仍面临挑战。为此，我们提出了 GLASS 框架，通过 SID-Tier 和语义搜索将长期用户兴趣整合到生成过程中。首先，SID-Tier 模块将长期交互映射为统一的兴趣向量，以增强初始语义 ID（SID）令牌的预测；与处理大规模物品空间的传统检索模型不同，该模块利用语义码本的紧凑性，结合用户长期历史与候选语义代码的交叉...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [AI-Driven Multi-Omics Integrated Applications Using Diverse Neural Networks for Breast Cancer Diagnostic Screening and Biomarker Discovery.](https://pubmed.ncbi.nlm.nih.gov/42489168/)
  来源：PubMed | 日期：2026-07-23 | 相关度：3.75 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：乳腺癌（BC）是全球女性中最普遍且具有高度复杂性和异质性的恶性肿瘤，其诊断、预后和治疗的挑战限制了临床疗效。基于组学的技术通过分子谱分析和临床分析在乳腺癌诊断中受到广泛关注。整合代谢组学、蛋白质组学、转录组学和基因组学，通过高通量分子分型为个性化诊疗提供了多维方法。人工智能（AI）的兴起通过多模态数据整合支持了更准确的早期诊断。深度学习（DL）和机器学习（ML）已广泛用于肿瘤分级、组织病理学分类、分子分型、影像诊断和预后预测。本综述总结...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Bionic Magnetic Nanorobots Combined with AI-Assisted Microscopic Imaging for Argonaute-Powered Multiplexed Foodborne Pathogens Detection.](https://pubmed.ncbi.nlm.nih.gov/42429450/)
  来源：PubMed | 日期：2026-07-22 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：食源性致病菌的多重超灵敏鉴定对食品安全至关重要。本研究通过聚乙二醇（PEG）接头优化磁性纳米颗粒上的苯硼酸（PBA）密度，构建了仿生纳米机器人，在20分钟内实现了92.21%的革兰氏阳性菌捕获，且稳定性达25天。此外，开发了一种基于聚苯乙烯微球尺寸编码和丁酸梭菌Argonaute（CbAgo）解码的AI辅助显微成像策略。经合理设计的CbAgo可激活循环切割电路进行多重解码，并以AI介导的计数作为读数。在无需DNA扩增的情况下，整个检测可...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
