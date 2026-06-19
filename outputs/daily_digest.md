# 每日论文监控日报 (2026-06-19)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 56 篇新论文。

## 抓取状态

- arXiv：成功，命中 51 篇
- PubMed：成功，命中 61 篇
- bioRxiv：成功，命中 15 篇
- medRxiv：成功，命中 14 篇

## 最值得看

### Foundation Model / Agent

- [Stellar: Scalable Multimodal Document Retrieval for Natural Language Queries](http://arxiv.org/abs/2606.19960v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：7.9 | 新颖度：7.41
  匹配主题：foundation_model_agent
  中文摘要：Multimodal document retrieval--selecting the most relevant multimodal document from a large corpus to answer a natural language query--plays an essential role in Retrieval-Augmented Generation (RAG) systems. State-of-the...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BioHarness: Substrate-Aware Evidence Assembly for Biomedical Question Answering across Literature, Knowledge Bases, and Biological Atlases](http://arxiv.org/abs/2606.19396v1)
  来源：arXiv | 日期：2026-06-17 | 相关度：7.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Motivation: Biomedical question answering often requires evidence beyond topically retrieved literature, including gene alias resolution, database identifier normalization, and atlas-derived biological measurements. Howe...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 产品应用 / 监测落地

- [MedRLM: Recursive Multimodal Health Intelligence for Long-Context Clinical Reasoning, Sensor-Guided Screening, Evidence-Grounded Decision Support, and Community-to-Tertiary Referral Optimization](http://arxiv.org/abs/2606.20164v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：7.8 | 新颖度：7.01
  匹配主题：foundation_model_agent
  中文摘要：Real-world clinical decision support requires reasoning over heterogeneous and longitudinal patient information rather than answering isolated medical questions. However, current medical large language models and retriev...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 可追踪

### Foundation Model / Agent

- [Silent Manipulation of Mental Health Treatment Recommendations from a Large Language Model](https://www.medrxiv.org/content/10.64898/2026.06.16.26355686v1)
  来源：medRxiv | 日期：2026-06-17 | 相关度：7.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Importance. Large language models (LLMs) increasingly inform mental health decisions by patients and clinicians. Inference-time activation steering can shift model behavior on a target dimension without altering weights ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [scIsoAgent enables autonomous isoform-resolved characterization and sequence-informed interpretation of long-read single-cell transcriptomes](https://www.biorxiv.org/content/10.64898/2026.06.11.731519v1)
  来源：bioRxiv | 日期：2026-06-16 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Alternative isoform usage can alter gene function independently of total gene expression, creating a need to resolve transcript isoforms at single-cell resolution. Long-read single-cell RNA sequencing meets this need by ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DPRM: A Plug-in Doob h transform-induced Token-Ordering Module for Diffusion Language Models](http://arxiv.org/abs/2604.24357v2)
  来源：arXiv | 日期：2026-04-27 | 相关度：7.1 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Diffusion language models generate without a fixed left-to-right order, leaving token ordering as a central algorithmic choice. Existing systems mainly use random masking or confidence-driven ordering, which respectively...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Layered Security Framework Against Prompt Injection in RAG-Based Chatbots](http://arxiv.org/abs/2606.19660v1)
  来源：arXiv | 日期：2026-06-17 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Prompt injection is ranked as the most critical vulnerability in large language model (LLM) deployments by the OWASP Top 10 for LLM Applications, yet existing defenses operate at isolated pipeline stages and remain incom...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Library-Aware Doubles and Iterative Repair for Large Language Model-Generated Unit Tests in OpenSIL Firmware](http://arxiv.org/abs/2606.19725v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Validating changes in low-level C firmware is expensive because unit tests (UTs) are fragile under strict build constraints, where missing headers, unresolved symbols, and dependency mismatches frequently prevent compila...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Improve Large Language Model Systems with User Logs](http://arxiv.org/abs/2602.06470v3)
  来源：arXiv | 日期：2026-02-06 | 相关度：6.55 | 新颖度：1.2
  匹配主题：foundation_model_agent
  中文摘要：Scaling training data and model parameters has long driven progress in large language models (LLMs), but this paradigm is increasingly constrained by the scarcity of high-quality data and diminishing returns from rising ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DeepInflation: an AI agent for research and model discovery of inflation](http://arxiv.org/abs/2601.14288v2)
  来源：arXiv | 日期：2026-01-14 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：We present DeepInflation, an AI agent designed for research and model discovery in inflationary cosmology. Built upon a multi-agent architecture, DeepInflation integrates Large Language Models (LLMs) with a symbolic regr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Repository-Level Solidity Code Generation with Large Language Models: From Prompting to Fine-Tuning](http://arxiv.org/abs/2606.19988v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have shown strong capabilities in general-purpose code generation, but their effectiveness in specialized software domains remains underexplored. Solidity smart contracts represent a high-sta...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [NIM4-ASR: Towards Efficient, Robust, and Customizable Real-Time LLM-Based ASR](http://arxiv.org/abs/2604.18105v2)
  来源：arXiv | 日期：2026-04-20 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Integrating large language models (LLMs) into automatic speech recognition (ASR) has become a mainstream paradigm in recent years. Although existing LLM-based ASR models demonstrate impressive performance on public bench...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts](http://arxiv.org/abs/2606.19847v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：4.75 | 新颖度：5.83
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) demonstrate strong reasoning and generation abilities, but their fixed context windows limit long-term information accumulation and reuse across multi-session interactions. Existing memory-au...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Shift-Left High-Level Synthesis Verification via Knowledge-Augmented LLM Agent](http://arxiv.org/abs/2606.17128v3)
  来源：arXiv | 日期：2026-06-15 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：High-Level Synthesis (HLS) relies on transforming original C specifications into synthesizable HLS-oriented C (HLS-C) implementations. Functional consistency verification between original C specifications and HLS-C imple...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CoRaCommit: A VS Code Extension for Commit Message Generation with Exemplar Retrieval](http://arxiv.org/abs/2606.19814v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Commit messages are essential textual artifacts that describe the intent behind code changes, and play a critical role in version control, code review, and historical tracking. However, in practice, commit messages are p...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Prompt, Plan, Extract: Zero-Shot Agentic LLMs Workflows for Lung Pathology Extraction from Clinical Narratives](http://arxiv.org/abs/2606.19852v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：5.75 | 新颖度：5.34
  匹配主题：foundation_model_agent
  中文摘要：Information extraction from pathology reports is essential for cancer staging, tumor registry population. Yet key data remains embedded in narrative reports, making manual extraction labor-intensive and error-prone. Trad...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Self-Driving Datasets: From 20 Million Papers to Nuanced Biomedical Knowledge at Scale](http://arxiv.org/abs/2605.07022v3)
  来源：arXiv | 日期：2026-05-07 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Manually curated biomedical repositories -- spanning bioactivity, genomics, and chemistry -- are expensive to maintain, lag behind primary literature, and discard experimental context, obscuring nuances needed to assess ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Fail-RAG : A Retrieval Augmented Generation Informed Framework for Robot Failure Identification](http://arxiv.org/abs/2606.19598v1)
  来源：arXiv | 日期：2026-06-17 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Industry automation is witnessing an evolution in robotics driven by both technological breakthroughs and societal changes: progress towards generalist robots, embodied and physical artificial intelligence (AI), and incr...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Dual-Agent Framework for Cross-Model Verified Translation of Natural-Language Protocols into Robotic Laboratory Platform](http://arxiv.org/abs/2606.20120v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：5.75 | 新颖度：6.12
  匹配主题：foundation_model_agent
  中文摘要：Biological experiment protocols are written in natural language, whereas automation systems rely on predefined control commands, creating a semantic gap that limits autonomous execution. Microplate-based automatic experi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Automating Information Extraction and Retrieval for Industrial Spare Parts Pooling](http://arxiv.org/abs/2606.03367v2)
  来源：arXiv | 日期：2026-06-02 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Maintenance organizations in manufacturing try to avoid downtime and unnecessary purchasing by reusing existing assets, but the main obstacle is not a lack of parts but a lack of actionable visibility across sites and pa...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Secure Coding Drift in LLM-Assisted Post-Quantum Cryptography Development: A Gamified Fix](http://arxiv.org/abs/2606.19474v1)
  来源：arXiv | 日期：2026-06-17 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：The transition to Post Quantum Cryptography (PQC) introduces considerable implementation complexity, requiring strict adherence to constant-time execution, side channel resistance, and precise parametrisation. Simultaneo...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Qiskit Code Migration with LLMs](http://arxiv.org/abs/2606.20173v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：4.75 | 新颖度：6.28
  匹配主题：foundation_model_agent
  中文摘要：The rapid evolution of Quantum Development Kits (QDKs) introduces a specific form of technical debt that compromises code maintainability and hinders software reuse. In the specialized domain of Quantum Software Engineer...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Learning What to Remember: Observability-Safe Memory Retention via Constrained Optimization for Long-Horizon Language Agents](http://arxiv.org/abs/2606.10616v4)
  来源：arXiv | 日期：2026-06-09 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Long-horizon language agents accumulate observations, reasoning traces, and retrieved facts exceeding context windows, making memory retention a fundamental resource-allocation problem. Existing systems treat retention a...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [AI-assisted continuous-time modelling of metastatic breast cancer reveals subtype-specific spatiotemporal organ interactions](https://www.medrxiv.org/content/10.64898/2026.06.15.26355684v1)
  来源：medRxiv | 日期：2026-06-16 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Metastatic breast cancer is one of the leading causes of premature mortality among women worldwide. A major barrier to optimal care is the marked heterogeneity in both the temporal dynamics of metastatic spread and the o...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [MedAgent: A Retrieval-Augmented Clinical Decision Support Agent with Verifiable Evidence Grounding for Evidence-Based Medicine](https://www.medrxiv.org/content/10.64898/2026.06.15.26355735v1)
  来源：medRxiv | 日期：2026-06-17 | 相关度：6.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Evidence-based medicine demands clinical answers that are not only fluent and medically plausible, but also anchored in traceable evidence, tailored to patient-specific clinical questions, sensitive to the hierarchy of e...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [FlowBench: separating planning, fault recovery and interpretation in agentic bioinformatics](https://www.biorxiv.org/content/10.64898/2026.06.12.731844v1)
  来源：bioRxiv | 日期：2026-06-16 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：AO_SCPLOWBSTRACTC_SCPLOWAgentic large language model (LLM) systems are being deployed in bioinformatics faster than they are understood, and single-metric evaluations conflate capabilities that fail independently. We int...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Field-Deployable Risk Stratification of Pathogens via an AI-Integrated Nanozyme Sensor.](https://pubmed.ncbi.nlm.nih.gov/42301193/)
  来源：PubMed | 日期：2026-06-16 | 相关度：5.5 | 新颖度：0.5
  匹配主题：pathogenomics, foundation_model_agent, application_monitoring
  中文摘要：Pathogen surveillance in complex environmental matrices requires analytical methods that are sensitive, robust, and suitable for field deployment. Here, we report a geometry-engineered trimetallic PdPtRu nanozyme-enabled...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Orion: Towards Lab Automation with Computer-Using Agents](https://www.biorxiv.org/content/10.64898/2026.06.13.732095v1)
  来源：bioRxiv | 日期：2026-06-16 | 相关度：5.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Laboratory discovery increasingly depends on computational workflows that connect experimental data to analysis, interpretation and follow-up hypotheses. Yet these workflows remain constrained by labor-intensive use of s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MemBoost: A Memory-Boosted Framework for Cost-Aware LLM Inference](http://arxiv.org/abs/2603.26557v3)
  来源：arXiv | 日期：2026-03-27 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) deliver strong performance but incur high inference cost in real-world services, especially under workloads with repeated or near-duplicate queries across users and sessions. In this work, we...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Towards an ecosystem of clinical decision support tools for precision cancer medicine.](https://pubmed.ncbi.nlm.nih.gov/42310422/)
  来源：PubMed | 日期：2026-06-17 | 相关度：3.75 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Molecular tumor boards are supported by clinical decision support system (CDSS) tools for the interpretation of complex molecular data towards personalized treatments. Current CDSS tools are genomics-focused and characte...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ResearchClawBench: A Benchmark for End-to-End Autonomous Scientific Research](http://arxiv.org/abs/2606.07591v3)
  来源：arXiv | 日期：2026-05-28 | 相关度：2.5 | 新颖度：1.5
  匹配主题：未命中具体主题
  中文摘要：AI coding agents are increasingly used for scientific work, but their end-to-end autonomous research capability remains difficult to verify. We present ResearchClawBench, a benchmark for evaluating autonomous scientific ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Science Earth: Towards A Planet-Scale Operating System for AI-Native Scientific Discovery](http://arxiv.org/abs/2606.01316v2)
  来源：arXiv | 日期：2026-05-31 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Scientific discovery demands intelligence, perseverance, and serendipity across vast search spaces. Today, top scientific capabilities remain siloed--one AI system for biological analysis, another for clinical reasoning,...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TSAssistant: A Human-in-the-Loop Agentic Framework for Automated Target Safety Assessment](http://arxiv.org/abs/2604.23938v3)
  来源：arXiv | 日期：2026-04-27 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Target Safety Assessment (TSA) requires systematic integration of genetic, transcriptomic, target homology, pharmacological, and clinical data to evaluate potential safety liabilities of therapeutic targets. This process...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PACMS: Submodular Context Selection as a Pluggable Engine for LLM Agents](http://arxiv.org/abs/2606.20047v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：1.4 | 新颖度：6.15
  匹配主题：未命中具体主题
  中文摘要：Conversational and tool-using LLM agents operate over a context window that fills from several directions simultaneously. As a session proceeds, the agent accumulates user and assistant turns, entries drawn from a persis...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multi-Agent Transactive Memory](http://arxiv.org/abs/2606.19911v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：1.4 | 新颖度：5.77
  匹配主题：未命中具体主题
  中文摘要：The decentralized deployment of LLM agents with diverse capabilities across diverse tasks motivates infrastructure for knowledge sharing across heterogeneous agent populations. Just as search engines index human-generate...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Graphs Don't Stay Secret: Practical Subgraph Reconstruction Attacks on Defended Graph RAG](http://arxiv.org/abs/2602.06495v2)
  来源：arXiv | 日期：2026-02-06 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Graph-based retrieval-augmented generation (Graph RAG) is increasingly deployed to support LLM applications by augmenting user queries with structured knowledge retrieved from a knowledge graph. While Graph RAG improves ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond](http://arxiv.org/abs/2604.22748v3)
  来源：arXiv | 日期：2026-04-24 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：As AI systems move from generating text to accomplishing goals through sustained interaction, the ability to model environment dynamics becomes a central bottleneck. Agents that manipulate objects, navigate software, coo...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Automated Standardization of Legacy Biomedical Metadata Using an Ontology-Constrained LLM Agent](http://arxiv.org/abs/2604.08552v2)
  来源：arXiv | 日期：2026-03-10 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Scientific metadata are often incomplete and noncompliant with community standards, limiting dataset findability, interoperability, and reuse. Even when standard metadata reporting guidelines exist, they typically lack m...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [SciHorizon-GENE: Benchmarking LLM for Life Sciences Inference from Gene Knowledge to Functional Understanding](http://arxiv.org/abs/2601.12805v4)
  来源：arXiv | 日期：2026-01-19 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have shown growing promise in biomedical research, particularly for knowledge-driven interpretation tasks. However, their ability to reliably reason from gene-level knowledge to functional un...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Poisoning the Genome: Targeted Backdoor Attacks on DNA Foundation Models](http://arxiv.org/abs/2603.27465v2)
  来源：arXiv | 日期：2026-03-29 | 相关度：5.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Foundation models trained on DNA sequences have achieved strong performance across biological tasks including variant effect prediction and genome design. These models rely on massive public genomic datasets comprising t...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Telenor Nordics Customer Service self-help corpus](http://arxiv.org/abs/2605.26891v2)
  来源：arXiv | 日期：2026-05-26 | 相关度：2.05 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：This paper presents a multilingual customer service self-help corpus comprising 1,122 manually validated documents in Finnish, Danish, Norwegian, and Swedish, totaling 274,599 words and 1,884,833 characters. The document...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [MetaHarmonizer: robust biomedical metadata harmonization and a contamination control for inflated LLM performance on public benchmarks](https://www.biorxiv.org/content/10.64898/2026.06.13.732088v1)
  来源：bioRxiv | 日期：2026-06-17 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Public biomedical repositories hold substantial reuse potential, but inconsistent metadata routinely blocks integration across studies. Recent LLM-based harmonization approaches address scale but suffer from non-determin...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [When Does Streaming Tool Use Help? Characterizing Tool-Intent Stabilization in Streaming Retrieval-Augmented Generation](http://arxiv.org/abs/2606.20113v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：0.7 | 新颖度：6.61
  匹配主题：未命中具体主题
  中文摘要：Streaming Retrieval-Augmented Generation (Streaming RAG) reduces user-perceived latency by issuing tool queries in parallel with ongoing user input, before the utterance is complete. Reported gains are aggregate, yet the...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [TransLaw: A Large-Scale Dataset and Multi-Agent Benchmark Simulating Professional Translation of Hong Kong Case Law](http://arxiv.org/abs/2507.00875v3)
  来源：arXiv | 日期：2025-07-01 | 相关度：0.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Translating Hong Kong Court Judgments from English to Traditional Chinese is mandated by Articles 8-9 of the Basic Law, yet remains constrained by a shortage of parallel resources and rigorous demands on legal terminolog...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [When Global Gating Is Enough: Admission-Time Hubness Control in Anisotropic Vector Retrieval Systems](http://arxiv.org/abs/2606.19692v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Vector hubness, where a few points become nearest neighbors of many queries, creates a poisoning risk in retrieval-augmented generation (RAG): one injected document can influence unrelated requests. Existing defenses use...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [The Unreliable Judges: Assessing Reproducibility and Self-Preference Bias of LLMs as Free-Text Evaluators](https://www.medrxiv.org/content/10.64898/2026.06.15.26355670v1)
  来源：medRxiv | 日期：2026-06-17 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) are transforming clinical practice and research, but their adoption requires rigorous evaluation. While human assessment is ideal, its cost has driven the widespread use of LLMs as evaluators...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Predicting Immune Biomarkers with MultiModal Mixture-of-Expert Pathology Foundation Models Empowers Precision Oncology](http://arxiv.org/abs/2606.18123v1)
  来源：arXiv | 日期：2026-06-16 | 相关度：4.45 | 新颖度：2.25
  匹配主题：foundation_model_agent
  中文摘要：Predicting immune biomarkers associated with the tumor immune microenvironment (TIME) is critical for advancing precision oncology, yet existing approaches are largely limited to single image modalities and suffer from i...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [EpiGIS pro: an AI-powered geospatial intelligence platform for integrated disease surveillance and predictive analytics.](https://pubmed.ncbi.nlm.nih.gov/42304469/)
  来源：PubMed | 日期：2026-06-16 | 相关度：2.7 | 新颖度：0.25
  匹配主题：pathogenomics
  中文摘要：Global infectious disease surveillance requires timely integration of heterogeneous data sources. Existing platforms typically address only one dimension, leaving cross-domain correlations unexplored. This study presents...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SIGMA: Search-Augmented On-Demand Knowledge Integration for Agentic Mathematical Reasoning](http://arxiv.org/abs/2510.27568v2)
  来源：arXiv | 日期：2025-10-31 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Solving mathematical reasoning problems requires not only accurate access to relevant knowledge but also careful, multi-step thinking. However, current retrieval-augmented models often rely on a single perspective, follo...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CacheWeaver: Cache-Aware Evidence Ordering for Efficient Grounded RAG Inference](http://arxiv.org/abs/2606.19667v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) improves factual grounding, but it also lengthens prompts and raises prefill cost. Prefix caching in serving engines such as vLLM reduces this cost only when requests share the same t...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [OmicOS: A Comprehensive Omics Ecosystem Infrastructure and Agent System for the AI Era](https://www.biorxiv.org/content/10.64898/2026.06.11.731775v1)
  来源：bioRxiv | 日期：2026-06-16 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Biology has accumulated a vast ecosystem of omics methods, but much of this ecosystem remains built for expert humans rather than scientific agents. Methods are scattered across Python packages, R/Bioconductor and CRAN w...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Towards autonomous medical artificial intelligence agents.](https://pubmed.ncbi.nlm.nih.gov/42310457/)
  来源：PubMed | 日期：2026-06-17 | 相关度：6.5 | 新颖度：0.25
  匹配主题：foundation_model_agent, application_monitoring
  中文摘要：Large language models (LLMs) show great potential for clinical decision-making, yet most applications remain narrow, task-specific chat tools rather than systems integrated into clinical workflows 1,2 . However, building...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Configurable Clinical Information Extraction with Agentic RAG: What Works, What Breaks, and Why](http://arxiv.org/abs/2606.19602v1)
  来源：arXiv | 日期：2026-06-17 | 相关度：2.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Patient contexts span hundreds of heterogeneous documents and thousands of structured data points, yet the document-level metadata that AI systems need for retrieval and triage is absent or incomplete. Standard retrieval...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Improving Scientific Document Retrieval with Academic Concept Index](http://arxiv.org/abs/2601.00567v2)
  来源：arXiv | 日期：2026-01-02 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Adapting general-domain retrievers to scientific domains is challenging due to the scarcity of large-scale domain-specific relevance annotations and the substantial mismatch in vocabulary and information needs. Recent ap...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [BoltzGen: Toward Universal Binder Design](https://www.biorxiv.org/content/10.1101/2025.11.20.689494v2)
  来源：bioRxiv | 日期：2026-06-16 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：We introduce BoltzGen, an all-atom generative model for designing proteins and peptides across all modalities to bind a wide range of biomolecular targets. BoltzGen builds strong structural reasoning capabilities about t...
  为什么值得看：bioRxiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [Policy-aware Vector Search: A Vision for Fine Grained Access Control in Vector Databases](http://arxiv.org/abs/2606.19803v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Vector databases are increasingly used in security sensitive contexts with Retrieval Augmented Generation and organizational AI pipelines; however, their security capabilities remain limited. Specifically, Fine-grained A...
  为什么值得看：Policy-aware Vector Search: A Vision for 与你的主题有弱匹配，暂时保留作低优先级跟踪。
