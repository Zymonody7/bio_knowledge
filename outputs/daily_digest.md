# 每日论文监控日报 (2026-06-16)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 58 篇新论文。

## 抓取状态

- arXiv：成功，命中 44 篇
- PubMed：成功，命中 53 篇
- bioRxiv：成功，命中 14 篇
- medRxiv：成功，命中 12 篇

## 最值得看

### Foundation Model / Agent

- [Branching Flows: Discrete, Continuous, and Manifold Flow Matching with Splits and Deletions](http://arxiv.org/abs/2511.09465v4)
  来源：arXiv | 日期：2025-11-12 | 相关度：8.9 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Diffusion and flow matching approaches to generative modeling have shown promise in domains where the state space is continuous, such as image generation or protein folding & design, and discrete, exemplified by diffusio...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [How Post-Training Shapes Biological Reasoning Models](http://arxiv.org/abs/2606.16517v1)
  来源：arXiv | 日期：2026-06-15 | 相关度：7.8 | 新颖度：6.61
  匹配主题：foundation_model_agent
  中文摘要：Scientific reasoning models for biology combine language models with foundation models trained on multimodal biological data, including DNA, RNA, and proteins. These models are built through post-training, yet how each s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Intelligent tool orchestration for rapid mechanistic model prototyping: MCP servers as AI-biology interfaces.](https://pubmed.ncbi.nlm.nih.gov/42297831/)
  来源：PubMed | 日期：2026-06-15 | 相关度：7.55 | 新颖度：6.2
  匹配主题：foundation_model_agent
  中文摘要：Constructing multicellular mechanistic models traditionally requires extensive time and computational expertise. We introduce intelligent tool orchestration via Model Context Protocol (MCP) servers, enabling Large Langua...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Entity-Aware Generation of Synthetic Clinical Progress Notes for Prostate Cancer using Large Language Model](https://www.medrxiv.org/content/10.64898/2026.06.12.26355166v1)
  来源：medRxiv | 日期：2026-06-15 | 相关度：7.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Objectives: This study investigates large language models (LLMs) for clinical entity projection across substantial textual transformation. Specifically, we evaluate whether entities annotated in Spanish prostate cancer c...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 产品应用 / 监测落地

- [Artificial intelligence in clinical metagenomic pathogen detection: A critical review of pipeline integrations, challenges, and future directions.](https://pubmed.ncbi.nlm.nih.gov/42289215/)
  来源：PubMed | 日期：2026-06-14 | 相关度：8.25 | 新颖度：6.75
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：Metagenomic next-generation sequencing (mNGS) has expanded the scope of clinical diagnostics by enabling culture-independent detection of microorganisms in patient samples. However, mNGS clinical utility remains constrai...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [LiteOdyssey: A Lightweight Reasoning AI Agent for Interpretable Rare-Disease Diagnosis](http://arxiv.org/abs/2606.16149v1)
  来源：arXiv | 日期：2026-06-15 | 相关度：7.55 | 新颖度：6.7
  匹配主题：foundation_model_agent
  中文摘要：Most medical AI systems improve by scaling additional machinery: more fine-tuning data, more agents, and/or larger retrieval databases. In rare-disease diagnosis, however, such scaling can produce systems that are diffic...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Evaluation of AI-Generated Synthetic Data for Clinical Research in Secondary Cardiovascular Prevention among Dyslipidemia Patients](https://www.medrxiv.org/content/10.64898/2026.06.12.26355456v1)
  来源：medRxiv | 日期：2026-06-15 | 相关度：7.15 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Background: Access to high-quality clinical data is essential for advancing medical research and developing effective medical statistical and Artificial Intelligence models. However, privacy regulations and logistical ba...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 可追踪

### Foundation Model / Agent

- [MyeGPT: an AI agent for Multiple Myeloma](https://www.medrxiv.org/content/10.64898/2026.05.14.26353252v5)
  来源：medRxiv | 日期：2026-06-14 | 相关度：7.55 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Today, advancements in our understanding of cancer biology are increasingly attributed to large-scale clinical-molecular datasets. The case in point for multiple myeloma - the second-most prevalent haematological maligna...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Ablation Study of a Fairness Auditing Agentic System for Bias Mitigation in Early-Onset Colorectal Cancer Detection](http://arxiv.org/abs/2603.17179v2)
  来源：arXiv | 日期：2026-03-17 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence (AI) is increasingly used in clinical settings, yet limited oversight and domain expertise can allow algorithmic bias and safety risks to persist. This study evaluates whether an agentic AI system...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SPIRIT-CONSORT-ELM: Element-Level Assessment of Randomized Controlled Trial Reporting Using Large Language Models](https://www.medrxiv.org/content/10.64898/2026.06.06.26354746v1)
  来源：medRxiv | 日期：2026-06-15 | 相关度：6.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Randomized controlled trials (RCTs) play a central role in assessing the benefits and harms of interventions. Incomplete reporting in RCT publications can compromise the verifiability and usefulness of RCTs. SPIRIT and C...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AI-Driven Framework for Adaptive Water Network Management with Proof-of-Concept Implementation: Addressing Non-Revenue Water in Jordan](http://arxiv.org/abs/2606.15709v1)
  来源：arXiv | 日期：2026-06-14 | 相关度：6.55 | 新颖度：6.2
  匹配主题：foundation_model_agent
  中文摘要：Jordan faces severe water scarcity with 50\% of water produced is lost to leakage, theft and metering issues also known as non-revenue water (NRW). Traditional reactive approaches have proven insufficient for sustained N...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic Retrieval and Reinforcement Learned Equation Chains: A Controlled Generation Framework for Complex and Novel Physics Word Problems](http://arxiv.org/abs/2606.15591v1)
  来源：arXiv | 日期：2026-06-14 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Generating high-quality Physics Word Problems (PWPs) that are novel, complex, and solvable remains a challenging and underexplored problem in educational content generation. Existing approaches, many adapted from Math Wo...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Deterministic Integrity Gates for LLM-Assisted Clinical Manuscript Preparation: An Auditable Biomedical Informatics Architecture](http://arxiv.org/abs/2606.09500v4)
  来源：arXiv | 日期：2026-06-08 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：As autonomous research agents and AI co-scientist systems push large language models (LLMs) from drafting toward end-to-end manuscript production, the bottleneck shifts from generation to verification. Fluent LLM output ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CistromeMeta: A Large Language Model Powered Tool for Automated ChIP-seq Metadata Extraction.](https://pubmed.ncbi.nlm.nih.gov/42287723/)
  来源：PubMed | 日期：2026-06-13 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Public repositories such as NCBI's Gene Expression Omnibus (GEO) contain large numbers of ChIP-seq experiments, but their reuse is limited by heterogeneous free-text metadata describing target proteins, histone marks, ce...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Let LLMs Judge Each Other: Multi-Agent Peer-Reviewed Reasoning for Medical Question Answering](http://arxiv.org/abs/2606.15419v1)
  来源：arXiv | 日期：2026-06-13 | 相关度：6.15 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Objective: To enhance the accuracy, interpretability, and robustness of large language models (LLMs) in medical question answering (MedQA). Method: We designed a multi-agent peer-reviewed reasoning method in which multip...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Let large language models judge each other: multi-agent peer-reviewed reasoning for medical question answering.](https://pubmed.ncbi.nlm.nih.gov/42289818/)
  来源：PubMed | 日期：2026-06-15 | 相关度：6.15 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：To enhance the accuracy, interpretability, and robustness of large language models (LLMs) in medical question answering (MedQA). We designed a multi-agent peer-reviewed reasoning method in which multiple LLM agents indep...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SAG: SQL-Retrieval Augmented Generation with Query-Time Dynamic Hyperedges](http://arxiv.org/abs/2606.15971v1)
  来源：arXiv | 日期：2026-06-14 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) offers an effective approach for large language models to access external knowledge. However, existing methods rely on dense similarity retrieval and face inherent limitations in hand...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [VarEx: A Large Language Model Pipeline for Automated Extraction of Exposures, Outcomes, and Covariates from Epidemiologic Studies](https://www.medrxiv.org/content/10.64898/2026.06.13.26355589v1)
  来源：medRxiv | 日期：2026-06-15 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Objective: Observational studies are essential for investigating risk factors for Alzheimer's disease and related dementias (ADRD), but inconsistent reporting and selection of covariates can contribute to residual confou...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MolE-RAG: Molecular Structure-Enhanced Retrieval-Augmented Generation for Chemistry](http://arxiv.org/abs/2606.05693v2)
  来源：arXiv | 日期：2026-06-04 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have shown promise for molecular property prediction, but their ability to reason over chemical structures remains limited, as molecular representations such as SMILES differ substantially fr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SPARK: Security Knowledge Priming and Representation-Guided Knowledge Activation for LLM-based Secure Code Generation](http://arxiv.org/abs/2606.16244v1)
  来源：arXiv | 日期：2026-06-15 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models routinely generate code with exploitable security flaws. Prior literature attributes this limitation to a lack of security expertise, steering current defense mechanisms toward heavy fine-tuning or ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Mitigating Visual Hallucinations in Multimodal Systems through Retrieval-Augmented Reliability-Aware Inference](http://arxiv.org/abs/2606.15782v1)
  来源：arXiv | 日期：2026-06-14 | 相关度：6.1 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Multimodal large language models (MLLMs) have demonstrated strong capabilities in vision-language understanding and natural-language response generation. However, these systems can still produce overconfident predictions...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Protein Design with Agent Rosetta: A Case Study for Specialized Scientific Agents](http://arxiv.org/abs/2603.15952v2)
  来源：arXiv | 日期：2026-03-16 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are capable of emulating reasoning and using tools, creating opportunities for autonomous agents that execute complex scientific tasks. Protein design provides a natural testbed: although mac...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond Chunks and Graphs: Retrieval-Augmented Generation through Triplet-Driven Thinking](http://arxiv.org/abs/2508.02435v2)
  来源：arXiv | 日期：2025-08-04 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) is critical for reducing hallucinations and incorporating external knowledge into Large Language Models (LLMs). However, advanced RAG systems face a trade-off between performance and ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OmicsNavigator: An auditable scientific partner for scalable hypothesis validation in spatial omics](https://www.biorxiv.org/content/10.1101/2025.07.21.665821v2)
  来源：bioRxiv | 日期：2026-06-14 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Translating high-dimensional, spatially resolved molecular datasets into testable biological findings remains a major research bottleneck. Here, we present OmicsNavigator, an autonomous large language model-powered syste...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MemBoost: A Memory-Boosted Framework for Cost-Aware LLM Inference](http://arxiv.org/abs/2603.26557v2)
  来源：arXiv | 日期：2026-03-27 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) deliver strong performance but incur high inference cost in real-world services, especially under workloads with repeated or near-duplicate queries across users and sessions. In this work, we...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Theorem-Grounded Execution Ontologies for Interpretable Machine Reasoning](http://arxiv.org/abs/2606.16010v1)
  来源：arXiv | 日期：2026-06-14 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models have achieved impressive performance on reasoning tasks spanning mathematics, science, programming, and commonsense inference. Despite these advances, their reasoning processes remain largely latent...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Trustworthy agentic genomics through versioned skill libraries](https://www.biorxiv.org/content/10.64898/2026.06.11.731523v1)
  来源：bioRxiv | 日期：2026-06-15 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Genomics is adopting autonomous AI agents that interpret genomes from natural-language instructions faster than it is building the means to trust them. We report the first large-scale controlled evaluation of where, in a...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Circuit Tracing in Autoregressive Protein Language Models](http://arxiv.org/abs/2606.16044v1)
  来源：arXiv | 日期：2026-06-14 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Protein language models (pLMs) can generate novel protein sequences with properties beyond those observed in nature, yet the mechanisms underlying protein generation remain poorly understood. Existing mechanistic interpr...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [FasterPy: An LLM-based Code Execution Efficiency Optimization Framework](http://arxiv.org/abs/2512.22827v2)
  来源：arXiv | 日期：2025-12-28 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Code often suffers from performance bugs. These bugs necessitate the research and practice of code optimization. Traditional rule-based methods rely on manually designing and maintaining rules for specific performance bu...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AlignCoder: Aligning Retrieval with Target Intent for Repository-Level Code Completion](http://arxiv.org/abs/2601.19697v2)
  来源：arXiv | 日期：2026-01-27 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Repository-level code completion remains a challenging task for existing code large language models (code LLMs) due to their limited understanding of repository-specific context and domain knowledge. While retrieval-augm...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Retrieve, Don't Retrain: Extending Vision Language Action Models to New Tasks at Test Time](http://arxiv.org/abs/2606.15631v1)
  来源：arXiv | 日期：2026-06-14 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Extending a vision-language-action (VLA) policy to a new task typically requires task-specific teleoperated demonstrations and per-task fine-tuning, making adaptation costly in both data collection and compute. In this p...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 其他

- [Islamic Large Language Models: From Knowledge Acquisition to Trustworthy and Hallucination-Resistant AI](http://arxiv.org/abs/2606.16629v1)
  来源：arXiv | 日期：2026-06-15 | 相关度：4.75 | 新颖度：6.7
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly used for knowledge-intensive question answering, including religious and legal questions. Islamic knowledge is a particularly demanding setting: answers are expected to be gr...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [When RAG Hurts: Diagnosing and Mitigating Attention Distraction in Retrieval-Augmented LVLMs](http://arxiv.org/abs/2602.00344v2)
  来源：arXiv | 日期：2026-01-30 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：While Retrieval-Augmented Generation (RAG) is one of the dominant paradigms for enhancing Large Vision-Language Models (LVLMs) on knowledge-based VQA tasks, recent work attributes RAG failures to insufficient attention t...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [Retrievable Gradients: Continual Post-Training Without Cumulative Weight Drift](http://arxiv.org/abs/2606.15734v1)
  来源：arXiv | 日期：2026-06-14 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Continual post-training enables models to absorb emerging knowledge after deployment, but repeatedly updating shared parameters can accumulate weight drift, potentially causing catastrophic forgetting and degrading gener...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Evaluating Large Language Models for Assessment of Psychosis Risk](https://www.medrxiv.org/content/10.64898/2026.04.02.26349960v2)
  来源：medRxiv | 日期：2026-06-15 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：精神病预防依赖于对临床高风险（CHR-P）个体的早期检测，但目前受限于临床评估需要专家对叙述性访谈进行解读，导致其难以大规模推广。本研究评估了大语言模型（LLMs）能否从访谈文本中提取临床信息以支持风险评估。研究人员利用来自373名参与者（其中77.7%为CHR-P）的678份PSYCHS访谈转录本，对11个开源LLM进行了评估。模型任务包括推断CHR-P状态，并估算15个症状领域的严重程度和频率。结果显示，大型模型表现最强，其中Lla...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Intelligent Multimodal Retrieval and Reasoning for Geospatial Knowledge Discovery on the I-GUIDE Platform](http://arxiv.org/abs/2606.15838v1)
  来源：arXiv | 日期：2026-06-14 | 相关度：2.1 | 新颖度：6.75
  匹配主题：未命中具体主题
  中文摘要：Geospatial knowledge discovery increasingly requires search across heterogeneous artifacts: datasets, maps, notebooks, software, publications, and the provenance links among them. Conventional geoportals support metadata...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Scaling Short-Term Memory of Visuomotor Policies for Long-Horizon Tasks](http://arxiv.org/abs/2606.16178v1)
  来源：arXiv | 日期：2026-06-15 | 相关度：2.05 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Many robotic tasks require short-term memory, whether it's retrieving an object that's no longer visible or turning off an appliance after a set period. Yet, most visuomotor policies trained via imitation learning rely o...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Understanding the Behaviors of Environment-aware Information Retrieval](http://arxiv.org/abs/2606.16817v1)
  来源：arXiv | 日期：2026-06-15 | 相关度：1.4 | 新颖度：6.89
  匹配主题：未命中具体主题
  中文摘要：Recent retrieval-augmented generation (RAG) approaches have demonstrated strong capability in handling complex queries, yet current research overlooks a critical challenge: different retrievers require fundamentally diff...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DeepRoot: A KG-Coordinated Multi-Agent System for Therapeutic Reasoning over Historical Medical Texts](http://arxiv.org/abs/2606.15931v1)
  来源：arXiv | 日期：2026-06-14 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Historical medical archives and traditional medicines hold immense potential for drug discovery and remain a primary source for current drug development. However, pre-ontological prose and idiosyncratic taxonomies preven...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [MoE-Bind: Guiding De Novo Protein Binder Generation with Sparse Experts](https://www.biorxiv.org/content/10.64898/2026.06.13.732043v1)
  来源：bioRxiv | 日期：2026-06-13 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：De novo protein binder design has been dominated by structure-based pipelines that require known three-dimensional target conformations and consume substantial compute and generation time per design, limiting their throu...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [MIRAGE: Misleading Retrieval-Augmented Generation via Black-box and Query-agnostic Poisoning Attacks](http://arxiv.org/abs/2512.08289v3)
  来源：arXiv | 日期：2025-12-09 | 相关度：1.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) systems enhance LLMs with external knowledge but introduce a critical attack surface: corpus poisoning. While recent studies have demonstrated the potential of such attacks, they typi...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [VrySure: A Multi-Task AI Scientific Fraud Detection Platform for Identifying Manipulated and AI-Generated Biomedical Research Images](https://www.biorxiv.org/content/10.64898/2026.06.10.731492v1)
  来源：bioRxiv | 日期：2026-06-15 | 相关度：1.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：Integrity of scientific data is critical in biomedical research, where images often serve as primary evidence for experimental observations and conclusions. Advances in image-editing technologies and generative artificia...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [SCAR: Semantic Continuity-Aware Retrieval for Efficient Context Expansion in RAG](http://arxiv.org/abs/2606.16661v1)
  来源：arXiv | 日期：2026-06-15 | 相关度：0.7 | 新颖度：6.29
  匹配主题：未命中具体主题
  中文摘要：Fixed-length chunking in Retrieval-Augmented Generation (RAG) often leads to boundary fragmentation, where critical evidence is split across segments, degrading retrieval recall. While static windowing and parent retriev...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [RoTRAG: Rule of Thumb Reasoning for Conversation Harm Detection with Retrieval-Augmented Generation](http://arxiv.org/abs/2604.17301v2)
  来源：arXiv | 日期：2026-04-19 | 相关度：0.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Detecting harmful content in multi turn dialogue requires reasoning over the full conversational context rather than isolated utterances. However, most existing methods rely mainly on models internal parametric knowledge...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [RL-Index: Reinforcement Learning for Retrieval Index Reasoning](http://arxiv.org/abs/2606.16316v1)
  来源：arXiv | 日期：2026-06-15 | 相关度：0.7 | 新颖度：5.86
  匹配主题：未命中具体主题
  中文摘要：Retrieving external knowledge is essential for solving real-world tasks, yet it remains challenging when the relationship between a query and its relevant knowledge involves implicit and complex reasoning beyond surface-...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Toward Precision Cardiac Rehabilitation: Current Limitations and Future Opportunities of Omics and Artificial Intelligence.](https://pubmed.ncbi.nlm.nih.gov/42295671/)
  来源：PubMed | 日期：2026-06-15 | 相关度：2.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Cardiovascular disease involves complex molecular, cellular, and physiological derangements that present challenges for traditional diagnostic and therapeutic approaches. Precision medicine is an evolving field that seek...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Unlocking Your Programmable and Creative RNA Sequence Designer with RDiffusion](https://www.biorxiv.org/content/10.64898/2026.06.13.732023v1)
  来源：bioRxiv | 日期：2026-06-13 | 相关度：2.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：As a cornerstone of the central dogma, RNA has both witnessed and actively shaped three billion years of evolution. Over this vast timescale, a remarkable diversity of RNA molecules has emerged, executing functions that ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A novel computational framework for tumor-specific T cell antigen identification using a deep neural network.](https://pubmed.ncbi.nlm.nih.gov/42295488/)
  来源：PubMed | 日期：2026-06-15 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Identifying tumor-specific T-cell antigens is essential for advancing cancer immunotherapy and enabling precision-driven, AI-assisted discovery. While artificial intelligence (AI) and machine learning (ML) have significa...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ProtAff: Protein Binding Affinity Prediction via LoRA-Finetuned ESM-2](https://www.biorxiv.org/content/10.64898/2026.06.13.732058v1)
  来源：bioRxiv | 日期：2026-06-13 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Predicting the binding affinity of protein--protein interactions remains a central challenge in computational biology. Structure prediction models such as AlphaFold3 (AF3) and Boltz-2 can produce high-quality docking pos...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Ricci-Filtration: Boosting Retrieval-Augmented Generation Reranker to Query-Answer Tasks by Discrete Ricci Flow](http://arxiv.org/abs/2606.15482v1)
  来源：arXiv | 日期：2026-06-13 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Ricci flow is a curvature-guided diffusion process that deforms space by shrinking regions of high positive curvature and expanding those with negative curvature. Similarly, discrete Ricci flow on weighted graphs modifie...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RAGR: Review-Augmented Generative Recommendation](http://arxiv.org/abs/2605.17267v2)
  来源：arXiv | 日期：2026-05-17 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Sequential recommendation (SR) is traditionally formulated as next-item prediction over chronological item interactions. Although recent generative recommendation (GR) methods introduce new machinery, such as semantic ID...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SPI: Query-Depth-Adaptive Indexing for Streaming RAG in Vector Databases](http://arxiv.org/abs/2511.16681v3)
  来源：arXiv | 日期：2025-11-12 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Vector databases (VecDBs) are increasingly deployed in retrieval-augmented generation (RAG) pipelines where query processing and document ingestion occur concurrently. The index layer needs to provide low-latency search ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Not All Retrievals are Useful: Cross-Attention for Input-Aware RAG in Time Series Forecasting](http://arxiv.org/abs/2603.14709v2)
  来源：arXiv | 日期：2026-03-16 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) enhances zero-shot time series (TS) forecasting by leveraging external knowledge bases, yet existing approaches overlook input-level relevance when fusing retrieved samples with the q...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Conversational Speech for Respiratory Triage in Primary Care: A Pilot Study](https://www.medrxiv.org/content/10.64898/2026.06.09.26355284v2)
  来源：medRxiv | 日期：2026-06-15 | 相关度：2.65 | 新颖度：0.75
  匹配主题：sequencing_bioinformatics
  中文摘要：BackgroundRespiratory complaints account for a substantial share of adult ambulatory care visits, and triaging them accurately has direct consequences for antibiotic stewardship and pathogen-specific therapy. Prior work ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [MedAI: Evaluating TxAgent's Therapeutic Agentic Reasoning in the NeurIPS CURE-Bench Competition](http://arxiv.org/abs/2512.11682v2)
  来源：arXiv | 日期：2025-12-12 | 相关度：2.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Therapeutic decision-making in clinical medicine constitutes a high-stakes domain in which AI guidance interacts with complex interactions among patient characteristics, disease processes, and pharmacological agents. Tas...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Trust, mistrust, and the promise of AI in genomics for African populations.](https://pubmed.ncbi.nlm.nih.gov/42296962/)
  来源：PubMed | 日期：2026-06-15 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Artificial intelligence (AI) is rapidly reshaping genomic medicine, yet its benefits remain unevenly distributed due to the profound under-representation of African populations in genomic datasets and persistent legacies...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [When algorithms testify: artificial intelligence-driven DNA analysis, evidentiary standards, and criminal justice reform.](https://pubmed.ncbi.nlm.nih.gov/42286906/)
  来源：PubMed | 日期：2026-06-15 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Forensic DNA analysis has already influenced criminal justice, and serves as a powerful tool for both conviction and exoneration. Despite its scientific foundations and wide application, DNA evidence is vulnerable to int...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Clinical Implications of Coexisting EWSR1 Rearrangements in Ewing Sarcoma: A Database Analysis and Representative Cases.](https://pubmed.ncbi.nlm.nih.gov/41224264/)
  来源：PubMed | 日期：2026-06-15 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Objective Ewing sarcoma (ES) is a highly aggressive malignancy with a poor prognosis, particularly in metastatic disease. While localized disease treated with multimodal therapy achieves favorable survival rates, metasta...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
