# 每日论文监控日报 (2026-07-31)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 51 篇新论文。

## 抓取状态

- arXiv：成功，命中 54 篇
- PubMed：成功，命中 54 篇
- bioRxiv：成功，命中 12 篇
- medRxiv：成功，命中 6 篇

## 最值得看

### Foundation Model / Agent

- [ProtSyntax: a protein large language model for decoding post-translational modification syntax and function](https://www.biorxiv.org/content/10.64898/2026.07.18.739331v2)
  来源：bioRxiv | 日期：2026-07-28 | 相关度：8.4 | 新颖度：6.0
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Post-translational modifications (PTMs) expand protein function by encoding context-dependent regulatory states, and their dysregulation contributes to cancer, neurodegeneration and metabolic disease. However, existing m...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BioPathfinder: Evidence-guided multi-agent platform enables hypothesis discovery for CAR-T engineering](https://www.biorxiv.org/content/10.64898/2026.07.15.738646v2)
  来源：bioRxiv | 日期：2026-07-28 | 相关度：7.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Clinical studies of chimeric antigen receptor (CAR)-T therapy generate diverse molecular and clinical evidence that remains fragmented across publications, public repositories and patient-derived datasets, limiting syste...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Sequence determinants of pathogenicity in glucose-6-phosphatase linked to glycogen storage disease type 1a](https://www.biorxiv.org/content/10.64898/2026.07.27.741017v1)
  来源：bioRxiv | 日期：2026-07-28 | 相关度：10.0 | 新颖度：5.25
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Glycogen storage disease type 1a (GSD1a) is an autosomal recessive Mendelian disorder that can be caused by missense variants in glucose-6-phosphatase catalytic subunit 1 (G6PC1). Although hundreds of missense variants h...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [OSCAgent: Accelerating the Discovery of Organic Solar Cells with LLM Agents](http://arxiv.org/abs/2602.04510v2)
  来源：arXiv | 日期：2026-02-04 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Organic solar cells (OSCs) hold great promise for sustainable energy, but discovering high-performance materials is time-consuming and costly. Existing molecular generation methods can aid the design of OSC molecules, bu...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SENSE: Efficient EEG-to-Text via Privacy-Preserving Semantic Retrieval](http://arxiv.org/abs/2603.17109v2)
  来源：arXiv | 日期：2026-03-17 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Decoding brain activity into natural language is a major challenge in AI with important applications in assistive communication, neurotechnology, and human-computer interaction. Most existing Brain-Computer Interface (BC...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PG-LLM: Benchmarking General-Purpose Language Models for Protein Variant Ranking](https://www.biorxiv.org/content/10.64898/2026.07.27.741045v1)
  来源：bioRxiv | 日期：2026-07-28 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：General-purpose language models are being increasingly utilized in protein-design workflows, yet their ability to evaluate variant effects remains unclear. To answer this question, we introduce PG-LLM, a benchmark built ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evaluating Agentic Bioinformatics through Function, Evidence, and Validation](http://arxiv.org/abs/2607.27556v1)
  来源：arXiv | 日期：2026-07-30 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large language model agents increasingly plan, execute, and interpret biological analyses, yet fluent responses, successful tool calls, and benchmark performance alone do not establish scientific credibility. Existing re...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MemHarness: Memory Is Reconstructed, Not Replayed](http://arxiv.org/abs/2607.28272v1)
  来源：arXiv | 日期：2026-07-30 | 相关度：6.15 | 新颖度：7.39
  匹配主题：foundation_model_agent
  中文摘要：Retrieving past experiences has become a common strategy to enhance large language model agents. However, most existing memory-augmented agents treat retrieved experiences as static records to be replayed verbatim, injec...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OptGraph: Large Language Models Enhanced Evolutionary Optimization Via Graph Retrieval-Augmented Generation](http://arxiv.org/abs/2607.27918v1)
  来源：arXiv | 日期：2026-07-30 | 相关度：4.75 | 新颖度：7.07
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have emerged as a powerful tool for automated evolutionary optimization, but existing methods remain limited in pattern reuse, error-aware refinement, and retrieval robustness across diverse ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DualG-MRAG: Decoupling Macro-Reasoning and Micro-Matching for Multimodal Retrieval-Augmented Generation](http://arxiv.org/abs/2607.28580v1)
  来源：arXiv | 日期：2026-07-30 | 相关度：3.45 | 新颖度：7.93
  匹配主题：foundation_model_agent
  中文摘要：While Multimodal Retrieval-Augmented Generation (MM-RAG) has shown promising results, it still struggles with complex multi-hop reasoning tasks. Existing methods primarily focus on independent instance-level matching, wh...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Keyphrase Identification Using Minimal Labeled Data with Hierarchical Contexts and Transfer Learning](https://www.medrxiv.org/content/10.1101/2023.01.26.23285060v4)
  来源：medRxiv | 日期：2026-07-30 | 相关度：6.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Background: Interoperable clinical decision support system (CDSS) rules provide a pathway to interoperability, a well-recognized challenge in health information technology. Building an ontology facilitates creating inter...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [From Single- to Cross-Document: Benchmarking Multi-Granularity Event Analysis of Large Language Models](http://arxiv.org/abs/2607.27654v1)
  来源：arXiv | 日期：2026-07-30 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Event analysis is an essential and fundamental direction of information extraction, involving various event-centric tasks at different granularity of documents. While large language models (LLMs) have preliminarily achie...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [VESTIGE: A Knowledge-Guided Masking Strategy for Corruption-Aware Fine-Tuning of Genomic Transformers, Validated on Ancient DNA Reconstruction](http://arxiv.org/abs/2607.27712v1)
  来源：arXiv | 日期：2026-07-30 | 相关度：4.75 | 新颖度：5.96
  匹配主题：foundation_model_agent
  中文摘要：Standard masked-language-model fine-tuning applies a uniform masking probability across every token position, assuming reconstruction difficulty is position-agnostic. When the degradation process is characterised and con...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Prioritizing Non-coding Variants in Rice GWAS Loci with a Chromatin-Informed DNA Language Model](https://www.biorxiv.org/content/10.64898/2026.07.24.740656v1)
  来源：bioRxiv | 日期：2026-07-28 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Numerous genome-wide association studies in rice have identified loci associated with diverse agronomic traits. However, interpreting the regulatory and functional significance of these loci remains challenging because e...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 其他

- [Hallucinations and Truth: A Comprehensive Accuracy Evaluation of RAG, LoRA and DoRA](http://arxiv.org/abs/2502.10497v2)
  来源：arXiv | 日期：2025-02-14 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Recent advancements in Generative AI have significantly improved the efficiency and adaptability of natural language processing (NLP) systems, particularly through Retrieval-Augmented Generation (RAG), Low-Rank Adaptatio...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [GLM-RAG: Graph Language Models for Graph-Based Retrieval-Augmented Generation](http://arxiv.org/abs/2607.28397v1)
  来源：arXiv | 日期：2026-07-30 | 相关度：4.75 | 新颖度：8.13
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) over knowledge graphs requires retrievers that can effectively capture both graph structure and semantic information. Recent approaches have explored graph neural network (GNN)-based ...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [ARC-Encoder: learning compressed text representations for large language models](http://arxiv.org/abs/2510.20535v2)
  来源：arXiv | 日期：2025-10-23 | 相关度：5.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Recent techniques such as retrieval-augmented generation or chain-of-thought reasoning have led to longer contexts and increased inference costs. Context compression techniques can reduce these costs, but the most effect...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EvoPINN: Agentic Discovery of Executable Algorithms for Physics-Informed Neural Networks](http://arxiv.org/abs/2607.26490v1)
  来源：arXiv | 日期：2026-07-29 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Physics-informed neural networks (PINNs) have emerged as a powerful paradigm for solving partial differential equations (PDEs), yet their performance heavily relies on the manual, trial-and-error engineering of neural re...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Challenges and proposed solutions in modeling multimodal medical data: A systematic review](http://arxiv.org/abs/2505.06945v5)
  来源：arXiv | 日期：2025-05-11 | 相关度：3.75 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Multimodal data modeling has emerged as a powerful approach in clinical research, enabling the integration of diverse data types such as imaging, genomics, wearable sensors, and electronic health records. Despite its pot...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ClinLens: Towards Long-Horizon Coding Agents for Longitudinal Multimodal Clinical Data Science](http://arxiv.org/abs/2607.26155v1)
  来源：arXiv | 日期：2026-07-28 | 相关度：3.05 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Clinical data-science agents must transform heterogeneous longitudinal records into auditable analyses, yet existing benchmarks largely isolate medical question answering, structured-table reasoning, or generic scientifi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BM25 Wins at Scale: A Scaling Study of Retrieval-Augmented Generation Paradigms](http://arxiv.org/abs/2607.26497v2)
  来源：arXiv | 日期：2026-07-29 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) spans lexical and dense retrieval, graph-based indexing, and agentic search, but these paradigms are usually evaluated on different benchmarks at one corpus size, leaving their accura...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MEDIAREF: A Public Knowledge Store for Media Background Checks](http://arxiv.org/abs/2607.02383v3)
  来源：arXiv | 日期：2026-07-02 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：LLM-based retrieval-augmented generation (RAG) is increasingly used for automated fact-checking (AFC) and related tasks. By grounding LLM outputs in retrieved evidence, RAG-based systems provide transparent justification...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RAG-HAR+: Towards Cost-Efficient LLM-Based Human Activity Recognition for Edge Deployment](http://arxiv.org/abs/2607.26631v1)
  来源：arXiv | 日期：2026-07-29 | 相关度：1.4 | 新颖度：1.5
  匹配主题：未命中具体主题
  中文摘要：穿戴式传感器的人体活动识别（HAR）在医疗保健、康复和健身追踪等领域具有重要应用。然而，现有的深度学习方法通常需要针对特定数据集进行训练、依赖大规模标注语料库，且难以适应新的传感器设置或活动分类。RAG-HAR 框架通过将 HAR 建模为无需训练的检索增强任务，利用传感器窗口的统计描述检索相似的标注示例来引导基于 LLM 的分类。本文提出 RAG-HAR+，这是一种检索优先且经过成本优化的扩展版本，旨在增强检索能力并减少对 LLM 推理...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RSIBench-Data: Benchmarking Data-Centric Research for Recursive Self-Improvement](http://arxiv.org/abs/2607.25886v1)
  来源：arXiv | 日期：2026-07-28 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：递归自我改进（RSI）要求将模型失败的证据转化为更优的模型。以数据为中心的后期训练研究涉及诊断能力差距、设计与验证训练数据策略以及从检查点反馈中学习。本文引入了 RSIBench-Data，这是一个评估 LLM 智能体作为数据中心研究员能力的受控基准。该基准固定了后期训练技术栈，智能体需迭代修改固定目标模型的训练数据策略；训练与推理使用 Tinker 后端服务，评估通过 Harbor 和 E2B 沙箱执行，且各智能体预算固定。研究在软件...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [When Knowledge Changes: Metamorphic Testing of RAG Systems with Mutations](http://arxiv.org/abs/2607.26843v1)
  来源：arXiv | 日期：2026-07-29 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG)-based LLM systems rely on external document corpora that can evolve and change over time. However, current evaluation methodologies (e.g., RAGAS) assess correctness against static sna...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [StateRAG: Typed State Contracts for Complex Retrieval-Augmented Generation](http://arxiv.org/abs/2605.25379v2)
  来源：arXiv | 日期：2026-05-25 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Complex retrieval-augmented generation requires evidence retrieval and control over what to retrieve next, which paths to explore, whether evidence is sufficient, and which intermediate results to retain. Existing RAG pa...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [FirstResearch: Auditable Question Formation for LLM Scientific Discovery Agents](http://arxiv.org/abs/2607.05682v2)
  来源：arXiv | 日期：2026-07-06 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：LLM systems for scientific discovery increasingly assist with ideation, literature synthesis, experiment planning, and report generation, but the first research question they propose can remain difficult to audit: it may...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond "What to Retrieve": Uncertainty in Retrieval-Augmented Code Generation](http://arxiv.org/abs/2607.24884v2)
  来源：arXiv | 日期：2026-07-27 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Repository-level code generation relies on heterogeneous evidence whose relevance, compatibility, and completeness are inherently uncertain. Similar-code examples, repository context, and project-specific APIs may provid...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Negative controls reveal volume-driven confounding in radiomics and imaging foundation model features](http://arxiv.org/abs/2607.28423v1)
  来源：arXiv | 日期：2026-07-30 | 相关度：0.7 | 新颖度：7.66
  匹配主题：未命中具体主题
  中文摘要：影像组学和影像基础模型有望成为肿瘤生物学的无创生物标志物，但预测特征可能仅反映肿瘤体积或采集伪影，而非有意义的图像空间结构。本研究推出了 READII-2-ROQC 开源框架，利用保持体积的阴性对照评估影像组学和深度影像特征是否捕捉到了独立的空间信号。该框架通过可配置的随机化策略，在肿瘤、背景和全图区域生成体素扰动图像，并对比原始图像与对照图像的特征行为及模型性能。研究人员将其应用于三个公共癌症影像队列，处理了 3,552 个肿瘤体积，...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RRM: Experience-Driven Reflective Retrieval Memory for Long-Horizon Multimodal Reasoning](http://arxiv.org/abs/2607.28156v1)
  来源：arXiv | 日期：2026-07-30 | 相关度：0.7 | 新颖度：6.65
  匹配主题：未命中具体主题
  中文摘要：Existing multimodal long-term memory agents use external memory to overcome the limited context available for long videos. However, most methods emphasize what to store rather than how stored memory should be retrieved. ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Detecting Knowledge Inconsistencies Across Text, Tables, and Knowledge Graphs](http://arxiv.org/abs/2607.25959v2)
  来源：arXiv | 日期：2026-07-28 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Wikipedia and Wikidata are widely used for information access, LLM pre-training, and retrieval-augmented generation. Their knowledge is deeply connected but scattered across text, tables, and knowledge graphs. This raise...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [KAMR: Grounding Generation via Knowledge-Aligned Multi-hop Retrieval](http://arxiv.org/abs/2607.27136v1)
  来源：arXiv | 日期：2026-07-29 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Graph-based retrieval-augmented generation increasingly relies on multi-hop retrieval, where answering a query requires composing multiple connected knowledge-graph triplets. However, existing retrievers often rank tripl...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [ChatIBD: design, safeguards, and early international use of a guideline-grounded generative AI tool for inflammatory bowel disease (IBD) professionals](https://www.medrxiv.org/content/10.64898/2026.05.06.26352526v2)
  来源：medRxiv | 日期：2026-07-30 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：本研究描述了ChatIBD的设计、运行保障及早期使用情况。ChatIBD是一个专为炎症性肠病（IBD）专业人士设计的生成式AI平台。该平台采用检索增强生成（RAG）技术，基于精选的IBD指南语料库进行问答。技术实现上，系统结合了混合语义与关键词检索、查询扩展及重排序，并强制模型仅依据检索到的材料回答并返回引用链接。安全保障措施包括集成欧洲药品管理局（EMA）的固定药物剂量信息、用户反馈捕获以及临床医生对标记输出的审查。在2025年10月...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [GEqTrain: A Configuration-Driven Framework for Retargeting Equivariant Graph Neural Networks Across 3D Scientific Tasks](http://arxiv.org/abs/2607.19083v2)
  来源：arXiv | 日期：2026-07-21 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Equivariant graph neural networks provide a powerful modeling language for three-dimensional scientific data, but their reuse is often limited by implementations tied to specific tasks, outputs, and training regimes. We ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [LC-SEPLM: long-range contact-supervised adaptation for sequence-only protein representation learning](http://arxiv.org/abs/2607.22777v2)
  来源：arXiv | 日期：2026-07-24 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Protein language models learn transferable sequence representations. However, because they primarily model contextual dependencies along amino-acid sequences, their training objectives do not explicitly constrain the mod...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [LabRobFail: A Benchmark for Robotic Failure Analysis in Chemical Self-driving Laboratory](http://arxiv.org/abs/2607.23704v2)
  来源：arXiv | 日期：2026-07-26 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：The deployment of embodied agents in self-driving laboratories could accelerate scientific discovery, yet their reliability is constrained by the irreversible and safety-critical nature of chemical experiments. Progress ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [ASARL: Autonomous Social-Aware Relevance Learning for QQ Search](http://arxiv.org/abs/2607.26593v1)
  来源：arXiv | 日期：2026-07-29 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：The rapid growth of online social platforms has transformed communication and information retrieval, giving rise to social search, where queries-titles are typically expressed in informal, community-specific language. Wh...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [ConMem: Contribution-Aware Memory for Long-Horizon Manufacturing Inspection Logs](http://arxiv.org/abs/2607.28126v1)
  来源：arXiv | 日期：2026-07-30 | 相关度：0.7 | 新颖度：7.09
  匹配主题：未命中具体主题
  中文摘要：Long-horizon steel-equipment inspection requires reasoning over heterogeneous records accumulated across repeated inspection cycles. Existing retrieval-augmented generation systems treat historical logs as a static corpu...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [AfriEconQA: A Benchmark for Quantitative and Temporal Reasoning over World Bank Economic Reports](http://arxiv.org/abs/2601.15297v3)
  来源：arXiv | 日期：2026-01-06 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Reliable question answering over long institutional documents requires more than topical retrieval: a system must localize the exact passage that supports a claim and preserve precise numerical and temporal detail when t...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Improving Item Discoverability in e-Commerce Search via Related Intent Generation](http://arxiv.org/abs/2607.27172v1)
  来源：arXiv | 日期：2026-07-29 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Traditional search systems are optimized to retrieve items that strictly match a query, often prioritizing precision over recall. In e-commerce marketplaces and particularly grocery, this paradigm is limiting, as user sa...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Automatic programming via large language models with population self-evolution for dynamic fuzzy job shop scheduling problem](http://arxiv.org/abs/2410.22657v2)
  来源：arXiv | 日期：2024-10-30 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Heuristic dispatching rules (HDRs) are widely used for solving the dynamic fuzzy job shop scheduling problem (DFJSSP). However, their performance is highly sensitive to specific scenarios and often necessitates expert cu...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MRCoder: An Efficient Context Selecting Approach for Repository-Level Code Generation](http://arxiv.org/abs/2607.26805v1)
  来源：arXiv | 日期：2026-07-29 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have demonstrated strong capabilities in code generation. However, repository-level code generation remains challenging, as it requires effectively identifying and utilizing repository-specif...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Better Call Grep: Evaluating and Improving Grep-Like Lexical Retrieval for Repository-Level Code Completion](http://arxiv.org/abs/2601.23254v3)
  来源：arXiv | 日期：2026-01-30 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Repository-level code completion remains challenging for large language models (LLMs) due to cross-file dependencies and limited context windows. Prior work addresses this challenge using Retrieval-Augmented Generation (...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Understanding LoRA as Knowledge Memory: An Empirical Analysis](http://arxiv.org/abs/2603.01097v5)
  来源：arXiv | 日期：2026-03-01 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Continuous knowledge updating for pre-trained large language models (LLMs) is increasingly necessary yet remains challenging. Although inference-time methods like In-Context Learning (ICL) and Retrieval-Augmented Generat...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Knowledge before Reasoning: EC-Reason-Bench, a Training-Free Diagnostic Benchmark for LLM Enzyme Classification](http://arxiv.org/abs/2607.26397v1)
  来源：arXiv | 日期：2026-07-29 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Enzyme function prediction is a hierarchical, knowledge-intensive form of protein function classification. Existing benchmarks expose an anomaly: general LLMs often get the coarse first level right, yet once asked for a ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Hierarchical Reranking for Scalable Financial RAG System](http://arxiv.org/abs/2607.27523v1)
  来源：arXiv | 日期：2026-07-29 | 相关度：1.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：Analyzing financial documents such as 10-K filings, tabular disclosures, and macroeconomic reports demands expert reasoning and extensive time. However, existing Retrieval-Augmented Generation systems often struggle to p...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [From Backlog Items to Security Guidance: Towards Continuous Security Compliance](http://arxiv.org/abs/2607.27374v1)
  来源：arXiv | 日期：2026-07-29 | 相关度：0.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：在受监管领域的持续软件工程中，确保开发全生命周期的安全性至关重要，但积压工作项（backlog items）中的安全需求往往不明确，导致工程师难以从简短描述中推断安全相关性。本文提出一种基于自然语言处理（NLP）的积压工作项增强系统，旨在自动检测安全相关项并将其链接至相应的安全需求。该系统结合了一个安全相关性分类器和一套基于安全需求文档的检索增强生成（RAG）流水线。研究贡献包括：1. 发布了由9位专家标注的288个积压项数据集（Fle...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Networked Intelligence: Active Shared Context Graphs for Human-AI Team Science](http://arxiv.org/abs/2607.13220v3)
  来源：arXiv | 日期：2026-07-14 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Most AI-for-science systems focus on scaling a single reasoning process by using better models, larger context windows, long-horizon agentic execution, or digital co-scientists working with one principal user. However, c...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Learning Ophthalmologist Clinical Reasoning for Glaucoma Diagnosis from Fundus Images](https://www.medrxiv.org/content/10.64898/2026.07.28.26359057v1)
  来源：medRxiv | 日期：2026-07-29 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Glaucoma is a leading cause of irreversible blindness worldwide. Ophthalmologists diagnose glaucoma through a structured reasoning process by sequentially evaluating optic nerve head characteristics before reaching a fin...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial intelligence in pediatric medical genetics and genomics.](https://pubmed.ncbi.nlm.nih.gov/42516066/)
  来源：PubMed | 日期：2026-07-28 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：人工智能（AI）正迅速且不均衡地融入医学及社会各领域。本综述重点探讨了 AI 在儿科基因组学领域的最新进展。文章阐述了 AI 及其子类型的通用定义，并介绍了最新的 AI 应用。随后，文章概述了 AI 在儿科基因组学多个环节的应用与测试，包括：识别潜在遗传病患者并辅助诊断过程；在实验室遗传检测流程中的实施；以及 AI 如何支持患者管理、新药发现及遗传病治疗研究。总体而言，AI 正以多种方式应用于儿科基因组学，该领域将因 AI 发生剧变。本...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [VITAL-RAG: Invariance Race for Context Allocation in Coding Agents](http://arxiv.org/abs/2607.26937v1)
  来源：arXiv | 日期：2026-07-29 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Coding agents often retrieve code from an entire repository, but only limited evidence can fit into the final model input. Conventional retrieval-augmented generation (RAG) for coding agents treats fragments from the sam...
  为什么值得看：VITAL-RAG: Invariance Race for Context A 与你的主题有弱匹配，暂时保留作低优先级跟踪。
