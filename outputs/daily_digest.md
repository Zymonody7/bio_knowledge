# 每日论文监控日报 (2026-07-08)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 55 篇新论文。

## 抓取状态

- arXiv：成功，命中 44 篇
- PubMed：成功，命中 54 篇
- bioRxiv：成功，命中 15 篇
- medRxiv：成功，命中 8 篇

## 最值得看

### Foundation Model / Agent

- [From Voting to Agent Collaboration: Answer-Type-Aware LLM Pipelines for BioASQ 14b](http://arxiv.org/abs/2607.06452v1)
  来源：arXiv | 日期：2026-07-07 | 相关度：6.55 | 新颖度：7.96
  匹配主题：foundation_model_agent
  中文摘要：Biomedical question answering requires not only accurate extraction of information from scientific literature but also reliable integration of evidence across multiple documents. This study presents a question-type-speci...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [ThermoFusion: A Multimodal Deep Learning Framework for Generalizable Prediction of Enzyme Thermostability](https://www.biorxiv.org/content/10.64898/2026.07.04.736494v1)
  来源：bioRxiv | 日期：2026-07-07 | 相关度：7.8 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Protein thermostability is a critical property for both industrial and biomedical enzyme applications, yet experimental evaluation of mutation-induced stability changes remains laborious and costly. Here, we present Ther...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Fine-Tuned Large Language Models for Detecting Social Isolation from Unstructured Clinical Notes](https://www.medrxiv.org/content/10.64898/2026.07.05.26357334v1)
  来源：medRxiv | 日期：2026-07-07 | 相关度：7.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Objectives: This study aimed to leverage FLAN-T5-Large, BERT, RoBERTa, and Gemma-2-2B, with fine-tuning, to identify instances of social isolation and social support within unstructured clinical notes. Materials and Meth...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 可追踪

### Foundation Model / Agent

- [Same Inputs, Different EDSS: Measuring Specification Drift in Clinical Scoring Pipelines](https://www.medrxiv.org/content/10.64898/2026.06.25.26356350v1)
  来源：medRxiv | 日期：2026-07-07 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Clinical informatics pipelines increasingly compute validated clinical endpoints from upstream NLP outputs. Even when the endpoint is defined by an established rubric, translating that rubric across representations - nat...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RS-Agent: Automating Remote Sensing Tasks through Intelligent Agent](http://arxiv.org/abs/2406.07089v4)
  来源：arXiv | 日期：2024-06-11 | 相关度：6.8 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in Multimodal Large Language Models (MLLMs) have shown promise for remote sensing tasks such as visual question answering and scene understanding. However, existing models remain limited to basic instruct...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Toward Trustworthy Large Language Model Agents in Healthcare](http://arxiv.org/abs/2607.05055v1)
  来源：arXiv | 日期：2026-07-06 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Healthcare appointment scheduling remains a persistent operational bottleneck, driven by manual coordination, fragmented legacy systems, and high administrative overhead. These inefficiencies constrain provider availabil...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [External Data Extraction Attacks against Retrieval-Augmented Large Language Models](http://arxiv.org/abs/2510.02964v2)
  来源：arXiv | 日期：2025-10-03 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：In recent years, RAG has emerged as a key paradigm for enhancing large language models (LLMs). By integrating externally retrieved information, RAG alleviates issues like outdated knowledge and, crucially, insufficient d...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [VASP Agent: An Agentic Framework for Autonomous First-principles Calculations](http://arxiv.org/abs/2512.19458v2)
  来源：arXiv | 日期：2025-12-22 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) are increasingly embedded in agentic frameworks for scientific discovery. First-principles materials computation imposes a demanding standard for autonomy: successful execution depends on int...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Generalized cell phenotyping for spatial proteomics with language-informed vision models](https://www.biorxiv.org/content/10.1101/2024.11.02.621624v4)
  来源：bioRxiv | 日期：2026-07-06 | 相关度：6.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：We present DeepCell Types, a novel approach to cell phenotyping for spatial proteomics that addresses the challenge of generalization across diverse datasets with varying marker panels collected across different platform...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Code-Level Cost Function Generation for Spatial Image Steganography Using RAG-Enhanced Large Language Models](http://arxiv.org/abs/2607.05868v1)
  来源：arXiv | 日期：2026-07-07 | 相关度：5.45 | 新颖度：6.26
  匹配主题：foundation_model_agent
  中文摘要：Designing cost functions of adaptive steganography traditionally requires extensive manual tuning, while deep learning methods lack interpretability. Although large language models (LLMs) offer an automated alternative v...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Prompt-to-Paper: Agentic AI System for Bioinformatics](http://arxiv.org/abs/2607.05456v1)
  来源：arXiv | 日期：2026-07-05 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：While recent advances in large language models have enabled end-to-end automated manuscript generation, existing systems suffer from three critical deficiencies: (i) generated claims are not deterministically grounded in...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Quantifying Retriever-Generator Alignment in RAG with Local Explanations](http://arxiv.org/abs/2601.21803v2)
  来源：arXiv | 日期：2026-01-29 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) systems combine dense retrievers and language models to ground their outputs in external documents. However, the interaction between these components remains opaque, creating challeng...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [KernelEvolve: Scaling Agentic Kernel Coding for Heterogeneous AI Accelerators at Meta](http://arxiv.org/abs/2512.23236v4)
  来源：arXiv | 日期：2025-12-29 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Making deep learning recommendation model (DLRM) training and inference fast and efficient is important. However, this presents three key system challenges - model architecture diversity, kernel primitive diversity, and ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Learning from Execution: Self-Evolving Memory for Private-Library Code Generation](http://arxiv.org/abs/2604.24222v2)
  来源：arXiv | 日期：2026-04-27 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have achieved strong performance on general code generation, but their effectiveness drops sharply in enterprise settings where software development relies on internal private libraries absen...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Bioactive environments to combat antimicrobial resistance: artificial intelligence and model-driven microbial biocontrol for living materials.](https://pubmed.ncbi.nlm.nih.gov/42411838/)
  来源：PubMed | 日期：2026-07-07 | 相关度：4.6 | 新颖度：6.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Antimicrobial resistance (AMR) continues to outpace development of new therapeutics. Many interventions focus on treating infection after it occurs, but resistant pathogens often emerge, persist, and spread within reserv...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AllTheBacteria: a community resource empowers biology and discovers novel peptide antibiotics](https://www.biorxiv.org/content/10.1101/2024.03.08.584059v8)
  来源：bioRxiv | 日期：2026-07-07 | 相关度：4.6 | 新颖度：5.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Public microbial genomes encode an immense record of biological diversity, evolution and molecular function, but much of this information remains difficult to reuse because raw sequencing data are not uniformly assembled...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Clinical Impact, Diagnostic Performance, and Prognostic Implications of Plasma Metagenomic Next-Generation Sequencing in Solid Organ Transplant Recipients](https://www.medrxiv.org/content/10.64898/2026.07.02.26357172v1)
  来源：medRxiv | 日期：2026-07-06 | 相关度：7.4 | 新颖度：0.5
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Introduction: Plasma metagenomic next-generation sequencing (mNGS) may detect pathogens in solid organ transplant (SOT) recipients, but optimal patient selection and result interpretation remain uncertain. Methods: Physi...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [LLMs for Agentic Home Energy Management](http://arxiv.org/abs/2607.04569v1)
  来源：arXiv | 日期：2026-07-06 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Home Energy Management Systems (HEMS) can reduce residential electricity costs and support demand response, but adoption is limited by the difficulty of translating household preferences into technical scheduling constra...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Biological Motifs for Agentic Control](http://arxiv.org/abs/2607.04240v1)
  来源：arXiv | 日期：2026-07-05 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：The transition of Large Language Models (LLMs) from passive generators to autonomous agents has introduced significant challenges in reliability, security, and state management. Current agentic architectures are often co...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CausalGame: Benchmarking Causal Thinking of LLM Agents in Games](http://arxiv.org/abs/2607.04293v1)
  来源：arXiv | 日期：2026-07-05 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Building AI Scientist agents with Large Language Models (LLMs) has recently attracted growing attention. Since scientific discovery fundamentally relies on uncovering causal relationships from observations, the capabilit...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TogoMCP: Natural Language Querying of Life-Science Knowledge Graphs via Schema-Guided LLMs and the Model Context Protocol](https://www.biorxiv.org/content/10.64898/2026.03.19.713030v3)
  来源：bioRxiv | 日期：2026-07-06 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Querying the RDF Portal knowledge graph maintained by DBCLS, which aggregates approximately 60 life-science databases, requires proficiency in both SPARQL and database-specific RDF schemas, placing this resource beyond t...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [GestaltMML: Enhancing Rare Genetic Disease Diagnosis through Multimodal Machine Learning Combining Facial Images and Clinical Text](http://arxiv.org/abs/2312.15320v3)
  来源：arXiv | 日期：2023-12-23 | 相关度：3.75 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Individuals with suspected rare genetic disorders often undergo multiple clinical evaluations, imaging studies, laboratory tests, and genetic tests over a prolonged period of time, a process commonly described as the dia...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multimodal temporal mapping of macrophage transcriptome remodeling during Salmonella infection](https://www.biorxiv.org/content/10.64898/2026.07.04.736507v1)
  来源：bioRxiv | 日期：2026-07-06 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Macrophages are equipped to eliminate invading pathogens, yet several intracellular bacteria exploit them as replicative niches. Salmonella enterica serovar Typhimurium subverts host immunity by injecting effector protei...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Canopy: A Heterograph Foundation Model for Metabolic Engineering](http://arxiv.org/abs/2607.06224v1)
  来源：arXiv | 日期：2026-07-07 | 相关度：2.4 | 新颖度：7.4
  匹配主题：未命中具体主题
  中文摘要：Designing microbial strains that produce high-value chemicals at commercially viable titers remains a central challenge in metabolic engineering. Existing computational approaches either rely on stoichiometric constraint...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Rethinking Scientific Discovery in the Agentic Era](http://arxiv.org/abs/2607.03863v2)
  来源：arXiv | 日期：2026-07-04 | 相关度：2.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Artificial intelligence has advanced scientific discovery, but most AI4Science systems remain fragmented tools that rely on humans to coordinate problem formulation, literature grounding, model use, simulation, validatio...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [FLOWR.ROOT - A flow matching-based foundation model for joint multi-purpose structure-aware 3D ligand generation and affinity prediction.](https://pubmed.ncbi.nlm.nih.gov/42409794/)
  来源：PubMed | 日期：2026-07-06 | 相关度：2.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：We present FLOWR.ROOT, an SE(3)-equivariant flow-matching foundation model that unifies pocket-aware 3D ligand generation with multi-endpoint binding affinity prediction (pIC 50 , pK i , pK d , pEC 50 ) and pLDDT-based c...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ContextNest: Verifiable Context Governance for Autonomous AI Agent](http://arxiv.org/abs/2607.02116v2)
  来源：arXiv | 日期：2026-07-02 | 相关度：2.1 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Autonomous AI agents increasingly depend on external knowledge stores, yet most retrieval pipelines provide relevance without durable guarantees of provenance, version identity, integrity, traceability, or point-in-time ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Memory-Orchestrated Semantic System (MOSS): An Auditable Agentic Memory Architecture](http://arxiv.org/abs/2607.04391v1)
  来源：arXiv | 日期：2026-07-05 | 相关度：2.1 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Long-term memory remains a structural weakness of AI agents. The dominant approach, retrieval-augmented generation (RAG), relies on embedding-based similarity search, which is opaque by construction, difficult to audit, ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Mitigating Errors in LLM-Generated Web API Invocations via Retrieval-Augmented Generation and Constrained Decoding](http://arxiv.org/abs/2607.05936v1)
  来源：arXiv | 日期：2026-07-07 | 相关度：1.4 | 新颖度：6.54
  匹配主题：未命中具体主题
  中文摘要：Integration of web APIs is a cornerstone of modern software systems, yet writing correct web API invocation code remains challenging due to complex and evolving API specifications. Although LLMs are increasingly used for...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PatchOptic for Shared-State LLM Workflows with Projected Views and Verified Structured Updates](http://arxiv.org/abs/2607.05483v1)
  来源：arXiv | 日期：2026-07-06 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Agentic workflows often operate over shared, structured state. Because LLM context windows are limited, each model invocation is typically shown only the state fragment needed for the current workflow step, a pattern com...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Know Your Source: A Public Knowledge Store for Media Background Checks](http://arxiv.org/abs/2607.02383v2)
  来源：arXiv | 日期：2026-07-02 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：LLM-based retrieval-augmented generation (RAG) is increasingly used for automated fact-checking (AFC) and related tasks. By grounding LLM outputs in retrieved evidence, RAG-based systems provide transparent justification...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [FirstResearch: Auditable Question Formation for LLM Scientific Discovery Agents](http://arxiv.org/abs/2607.05682v1)
  来源：arXiv | 日期：2026-07-06 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：LLM systems for scientific discovery increasingly assist with ideation, literature synthesis, experiment planning, and report generation, but the first research question they propose can remain difficult to audit: it may...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic Retrieval-Augmented Generation for Financial Document Question Answering](http://arxiv.org/abs/2605.05409v2)
  来源：arXiv | 日期：2026-05-06 | 相关度：1.4 | 新颖度：1.5
  匹配主题：未命中具体主题
  中文摘要：针对金融文档问答（QA）中跨表格、文本和脚注的复杂多步数值推理难题，现有检索增强生成（RAG）方法因采用单次“检索-生成”范式，难以应对金融分析中普遍存在的复合推理链。本文提出 FinAgent-RAG，这是一种专为金融数值推理精度设计的智能体 RAG 框架，通过迭代检索-推理循环及自我验证机制实现。该框架包含三大核心创新：(1) 采用难负样本挖掘训练的对比金融检索器，用于区分语义相似但数值不同的片段；(2) 思维程序（PoT）推理模块...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MAM-AI: An On-Device Medical Retrieval-Augmented Generation System for Nurses and Midwives in Zanzibar](http://arxiv.org/abs/2606.29580v3)
  来源：arXiv | 日期：2026-06-28 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：针对撒哈拉以南非洲地区孕产妇和新生儿死亡率高、助产培训不足及网络连接不稳定的现状，本研究开发了MAM-AI。这是一个专为桑给巴尔护士助产士设计的离线医疗问答助手，完全运行在普通Android设备上。该系统采用300M参数的EmbeddingGemma进行向量化，匹配包含87份指南文件（63,650个段落）的语料库，并由4B参数的int4量化Gemma模型生成带引用的回答，确保数据不离开设备。评估采用分层方法，涵盖检索器、理想上下文下的生...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Risk-Constrained Freshness-Aware Semantic Caching for Open-Web Retrieval-Augmented LLMs](http://arxiv.org/abs/2607.04281v1)
  来源：arXiv | 日期：2026-07-05 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：语义缓存通过为语义相似的查询提供缓存答案，降低了检索增强生成（RAG）的延迟和成本，但现有方法大多未对开放网络证据随时间变化的“新鲜度”建模。本文提出 FreshCache，一种三层语义缓存系统，将缓存重用视为受风险约束的时间推理问题。在批准缓存命中前，FreshCache 利用拟合的指数衰减模型（由 MLP 增强）估计缓存结果过时的概率，仅当该概率低于设定的误差预算（答案层 ε=0.10，URL 列表层 ε=0.20，页面内容层 ε=...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Knowledge Base Poisoning Attacks and Defense for Policy-Aware LLM-RAG Framework](http://arxiv.org/abs/2607.04379v1)
  来源：arXiv | 日期：2026-07-05 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：本研究针对战场物联网（IoBT）任务控制中的策略感知大语言模型检索增强生成（PA-LLM-RAG）框架进行了对抗性安全研究。提出了一种名为“查询无关语义检索投毒”的新型攻击方法，通过向 IoBT 知识库注入精心设计的语义规则，在无需预知运行时提示词的情况下，使恶意规则在各类操作员查询中均能获得极高的检索排名。实验结果显示，仅注入单条规则（投毒率 1.6%）即可导致 85% 的 LLM 上下文受损，投毒率在 7.7% 时达到饱和，证明极小...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Compressing the Validation Bottleneck: An Agentic Self-Driving Lab for Scientific Discovery](http://arxiv.org/abs/2607.04508v1)
  来源：arXiv | 日期：2026-07-05 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：科学智能体（Agentic AI-for-Science）虽能自动化构思、规划和分析，但最终验证仍依赖物理实验。自动驾驶实验室（SDL）在执行实验时面临两大瓶颈：智能体可能在低价值实验上耗费过多轮次，或每轮实验成本过高。本研究通过单一智能体针对性解决这两个物理瓶颈。首先，开发了具备先验意识的智能体实验设计（DOE）循环，利用领域知识和历史结果提出可行且具信息量的后续实验，从而减少达成目标所需的试验次数。其次，引入成本意识代理模型，利用低...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Privilege and confidentiality in generative AI workflows](http://arxiv.org/abs/2607.05479v1)
  来源：arXiv | 日期：2026-07-06 | 相关度：2.1 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Generative AI (GenAI) systems store and process client data in three distinct ways: in the model's parameters through training and memorisation, in the context window during a live session, and in knowledge databases for...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [mamabench and mamaretrieval: Benchmarks for Evaluating Medical Retrieval-Augmented Generation in Maternal, Neonatal, and Reproductive Health](http://arxiv.org/abs/2606.29467v3)
  来源：arXiv | 日期：2026-06-28 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Medical question-answering benchmarks rarely cover the maternal, neonatal, child, and reproductive-health questions a nurse-midwife asks, and, to our knowledge, no public chunk-level relevance benchmark exists for matern...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Search Beyond What Can Be Taught: Evolving the Knowledge Boundary in Agentic Visual Generation](http://arxiv.org/abs/2607.05382v1)
  来源：arXiv | 日期：2026-07-06 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：视觉生成器在图像渲染方面表现出色，但常会自信地虚构其未掌握的知识。由于用户需求具有无限性、演进性和长尾特征（如新角色、趋势实体、训练截止日期后的事件），受限于固定训练语料的生成器面临结构性的世界知识瓶颈。本研究构建了 SearchGen-20K 数据集和 SearchGen-Bench 基准，包含跨 12 个失败类别和 22 个领域的 20,839 个提示词，并配套了包含 100 万条记录的多模态 SearchGen-Corpus-1M...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Hybrid privacy-aware semantic search: SVD-truncated document geometry and CKKS-encrypted query reranking under a restricted threat model](http://arxiv.org/abs/2606.26373v3)
  来源：arXiv | 日期：2026-06-24 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：稠密嵌入技术驱动了语义搜索与检索增强生成（RAG），但向量数据库的泄露会导致原始文本被高保真还原。传统的防御手段存在局限：同态搜索在百万级文档规模下速度过慢，而隐私噪声则会在起到保护作用前损害排序质量。本研究提出一种基于非对称性的中间路径：对静态文档向量进行SVD截断并施加数据所有者持有的私有正交变换旋转，而对动态查询则采用CKKS加密保护，确保诚实但好奇的服务器无法获知查询值或评分。在包含100万文档、使用5种编码器的语料库上，该方案...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Identification of race-specific QTL and candidate genes for Aphanomyces root rot resistance in alfalfa (Medicago sativa L.).](https://pubmed.ncbi.nlm.nih.gov/42132231/)
  来源：PubMed | 日期：2026-07-06 | 相关度：6.75 | 新颖度：0.25
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：Aphanomyces root rot (ARR), caused by the oomycete Aphanomyces euteiches, is one of the most devastating diseases of alfalfa in the United States. Two pathogenic races of A. euteiches have been identified, with most comm...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A Unified Molecular Graph and Protein Language Model Framework for Predicting Human Drug-Hormone Receptor Interactions with Structure-Aware Validation.](https://pubmed.ncbi.nlm.nih.gov/42402023/)
  来源：PubMed | 日期：2026-07-05 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Hormones regulate many essential biological processes by interacting with specific receptors that control gene expression, metabolism, growth, and immune function. Because numerous therapeutic compounds can influence or ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [BindRNAgen: Protein-binding RNA sequence generation using latent diffusion models.](https://pubmed.ncbi.nlm.nih.gov/42409279/)
  来源：PubMed | 日期：2026-07-06 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：RNA-binding proteins (RBPs) are pivotal regulators of gene expression, and their dysregulation is implicated in a wide range of human diseases. Designing synthetic RNA molecules to modulate RBP activity represents a prom...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AI-guided CRISPR screening reveals therapeutic targets in psoriasis.](https://pubmed.ncbi.nlm.nih.gov/42409798/)
  来源：PubMed | 日期：2026-07-06 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Psoriasis affects over 125 million people globally. Biologics targeting the IL-17/IL-17RA axis are effective but require systemic administration, are costly, and are unsuitable for some patients. Developing topical small...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MLS-Bench: A Holistic and Rigorous Assessment of AI Systems on Building Better AI](http://arxiv.org/abs/2605.08678v3)
  来源：arXiv | 日期：2026-05-09 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Modern AI progress has been driven by ML methods that are generalizable across settings and scalable to larger regimes. As large language models demonstrate advanced capabilities in reasoning, coding, and engineering tas...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Hierarchical Evidence-Driven Reasoning for Long Document Understanding](http://arxiv.org/abs/2607.04625v1)
  来源：arXiv | 日期：2026-07-06 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）通过检索机制筛选输入图像子集，从而简化长文档理解。然而，现有的多模态RAG流程面临两大核心挑战：首先，标准的语义相似度检索器常获取主题重叠但无答案的干扰页面，误导下游生成；其次，僵化的单次处理流程过度依赖初始检索的成功，任何核心证据的遗漏都会导致连锁错误。为此，我们提出 HIEVI-RAG，一种用于闭域文档理解的分层、证据驱动型多模态 RAG 框架。该框架将复杂查询系统地分解为四个阶段：(1) 分层问题分解，将多跳...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [DynaKRAG: A Unified Framework for Learnable Evidence Control in Multi-Hop Retrieval-Augmented Generation](http://arxiv.org/abs/2607.06507v1)
  来源：arXiv | 日期：2026-07-07 | 相关度：0.7 | 新颖度：8.37
  匹配主题：未命中具体主题
  中文摘要：多跳检索增强生成（RAG）通过顺序获取证据来揭示缺失事实、桥接实体或判断证据充分性。现有方法通常将迭代检索、查询重构、证据批判和充分性判断等操作固定在特定流水线或预定义拓扑中，缺乏对共享状态条件策略的学习。本文提出 DynaKRAG 框架，将多跳证据获取建模为对原子证据操作的状态条件控制。该框架包含一个有效性层用于构建每一步的可执行动作集，以及一个学习型控制器用于选择最优操作，从而动态更新证据状态。实验基于 Qwen2.5-7B-Ins...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers?](http://arxiv.org/abs/2606.24530v2)
  来源：arXiv | 日期：2026-06-23 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：本文推出了 NatureBench，这是一个包含 90 个跨学科任务的基准测试，这些任务提炼自经过同行评审的《自然》（Nature）系列期刊论文，旨在评估 AI 编程智能体在解决真实科学问题时，能否从单纯的“复现”跨越到“发现”。NatureBench 基于 NatureGym 构建，这是一个自动化流水线，能够根据原始论文构建标准化的、针对具体任务的容器化环境，从而解决了此前限制研究类智能体基准测试可信度的环境碎片化问题。在禁用网络搜索...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Exploiting Structural Properties for Efficient Constraint-Aware HNSW Hyperparameter Tuning](http://arxiv.org/abs/2607.04630v1)
  来源：arXiv | 日期：2026-07-06 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：向量数据库（VectorDBs）是检索增强生成（RAG）等现代检索系统的核心，其中高效的近似最近邻搜索（ANNS）至关重要。分层导航小世界（HNSW）图算法因其在召回率与延迟之间的优异权衡而被广泛应用。然而，HNSW的超参数配置极具挑战：其参数以非线性方式共同影响搜索质量、延迟、构建时间和索引大小，且生产部署通常面临严格的资源和调优时间限制。本研究从系统角度分析了HNSW的调优，揭示了其配置空间具有显著的结构规律，包括搜索与构建参数间的...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Medi-Gemma: A Hybrid Clinical Decision Support System Integrating Deterministic EMR Analytics and Retrieval-Augmented Generation](http://arxiv.org/abs/2607.04907v1)
  来源：arXiv | 日期：2026-07-06 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Deploying Large Language Models (LLMs) in high-stakes clinical settings remains limited by structural hallucinations, weak deterministic reasoning over tabular patient data, and omissions in vector retrieval. This paper ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial intelligence in molecular diagnostics for pandemic preparedness.](https://pubmed.ncbi.nlm.nih.gov/42396845/)
  来源：PubMed | 日期：2026-07-06 | 相关度：3.65 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Molecular diagnostics focusing on the detection and analysis of nucleic acids are indispensable tools for early pathogen identification, transmission monitoring, and genomic surveillance during pandemics. Recent technolo...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Multimodal profiling for prediction of primary resistance to anti-PD-(L)1 therapy in advanced non-small-cell lung cancer: the prospective PIONeeR biomarkers study](https://www.medrxiv.org/content/10.64898/2026.01.09.26343779v2)
  来源：medRxiv | 日期：2026-07-07 | 相关度：3.05 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Background Pretreatment prediction of primary resistance to anti-PD-(L)1 therapy in advanced non-small-cell lung cancer (NSCLC) remains an unmet clinical need. Existing biomarkers - including PD-L1 expression and tumour ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Detecting Hallucinations in Retrieval-Augmented Generation through Grounding-Aware Sensitivity by Perturbation (GASP)](http://arxiv.org/abs/2607.04223v1)
  来源：arXiv | 日期：2026-07-05 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) reduces but does not eliminate hallucination, and existing detectors return a single answer-level score that does not indicate which sentence is unsupported, or why. To close this gap...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [MIRAGE: Defending Long-Form RAG Against Misinformation Pollution](http://arxiv.org/abs/2607.05069v1)
  来源：arXiv | 日期：2026-07-06 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）通过引入外部证据提升了大语言模型（LLM）的真实性，但现实中的检索结果常受污染，相关段落可能包含微妙的误导性框架或虚假信息。本文提出 MIRAGE，一种无需训练且模型无关的长文本 RAG 防御框架。MIRAGE 构建了一个基于自然语言推理（NLI）的跨文档断言图，并利用“防御断言门控”（Defended-Claims Gate）筛选出具备一致性且由多源支持的证据子集进行生成；若证据质量不足，则屏蔽检索结果并转由模型...
  为什么值得看：MIRAGE: Defending Long-Form RAG Against  与你的主题有弱匹配，暂时保留作低优先级跟踪。
