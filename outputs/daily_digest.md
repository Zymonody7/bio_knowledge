# 每日论文监控日报 (2026-06-21)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 24 篇新论文。

## 抓取状态

- arXiv：成功，命中 18 篇
- PubMed：成功，命中 32 篇
- bioRxiv：成功，命中 21 篇
- medRxiv：成功，命中 5 篇

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [Stellar: Scalable Multimodal Document Retrieval for Natural Language Queries](http://arxiv.org/abs/2606.19960v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：7.9 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Multimodal document retrieval--selecting the most relevant multimodal document from a large corpus to answer a natural language query--plays an essential role in Retrieval-Augmented Generation (RAG) systems. State-of-the...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [From Scarce Functional Labels to Label-Aware Generation in Homologous Protein Families](https://www.biorxiv.org/content/10.1101/2025.07.22.665933v2)
  来源：bioRxiv | 日期：2026-06-19 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Accurately annotating and controlling protein function from sequence data remains a major challenge in protein engineering, especially when functional labels are scarce within large homologous families. Here, we study a ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Quantifying evolutionary novelty and design efficiency in generative genome design](https://www.biorxiv.org/content/10.64898/2026.06.12.731871v1)
  来源：bioRxiv | 日期：2026-06-19 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Generative genome design models can now produce previously unobserved genome-length sequences, but assessing their capabilities is complicated by limitations in functional prediction. The ability to engineer genomes fast...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [MedRLM: Recursive Multimodal Health Intelligence for Long-Context Clinical Reasoning, Sensor-Guided Screening, Evidence-Grounded Decision Support, and Community-to-Tertiary Referral Optimization](http://arxiv.org/abs/2606.20164v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：7.8 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Real-world clinical decision support requires reasoning over heterogeneous and longitudinal patient information rather than answering isolated medical questions. However, current medical large language models and retriev...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [NIM4-ASR: Towards Efficient, Robust, and Customizable Real-Time LLM-Based ASR](http://arxiv.org/abs/2604.18105v2)
  来源：arXiv | 日期：2026-04-20 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Integrating large language models (LLMs) into automatic speech recognition (ASR) has become a mainstream paradigm in recent years. Although existing LLM-based ASR models demonstrate impressive performance on public bench...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Repository-Level Solidity Code Generation with Large Language Models: From Prompting to Fine-Tuning](http://arxiv.org/abs/2606.19988v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have shown strong capabilities in general-purpose code generation, but their effectiveness in specialized software domains remains underexplored. Solidity smart contracts represent a high-sta...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts](http://arxiv.org/abs/2606.19847v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) demonstrate strong reasoning and generation abilities, but their fixed context windows limit long-term information accumulation and reuse across multi-session interactions. Existing memory-au...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TSAssistant: A Human-in-the-Loop Agentic Framework for Automated Target Safety Assessment](http://arxiv.org/abs/2604.23938v3)
  来源：arXiv | 日期：2026-04-27 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Target Safety Assessment (TSA) requires systematic integration of genetic, transcriptomic, target homology, pharmacological, and clinical data to evaluate potential safety liabilities of therapeutic targets. This process...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multi-Agent Transactive Memory](http://arxiv.org/abs/2606.19911v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：The decentralized deployment of LLM agents with diverse capabilities across diverse tasks motivates infrastructure for knowledge sharing across heterogeneous agent populations. Just as search engines index human-generate...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PACMS: Submodular Context Selection as a Pluggable Engine for LLM Agents](http://arxiv.org/abs/2606.20047v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Conversational and tool-using LLM agents operate over a context window that fills from several directions simultaneously. As a session proceeds, the agent accumulates user and assistant turns, entries drawn from a persis...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Automated Standardization of Legacy Biomedical Metadata Using an Ontology-Constrained LLM Agent](http://arxiv.org/abs/2604.08552v2)
  来源：arXiv | 日期：2026-03-10 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Scientific metadata are often incomplete and noncompliant with community standards, limiting dataset findability, interoperability, and reuse. Even when standard metadata reporting guidelines exist, they typically lack m...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Elucidating the Design Space of Generative Models for Single-Cell Perturbation Prediction](https://www.biorxiv.org/content/10.64898/2026.06.15.732063v1)
  来源：bioRxiv | 日期：2026-06-18 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Next-token prediction has produced predictable scaling in language, but the recipe presumes a sequence of tokens with a meaningful order. Single-cell RNA-seq counts have no natural gene ordering, so applying the recipe d...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Prompt, Plan, Extract: Zero-Shot Agentic LLMs Workflows for Lung Pathology Extraction from Clinical Narratives](http://arxiv.org/abs/2606.19852v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Information extraction from pathology reports is essential for cancer staging, tumor registry population. Yet key data remains embedded in narrative reports, making manual extraction labor-intensive and error-prone. Trad...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Telenor Nordics Customer Service self-help corpus](http://arxiv.org/abs/2605.26891v2)
  来源：arXiv | 日期：2026-05-26 | 相关度：2.05 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：This paper presents a multilingual customer service self-help corpus comprising 1,122 manually validated documents in Finnish, Danish, Norwegian, and Swedish, totaling 274,599 words and 1,884,833 characters. The document...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [When Does Streaming Tool Use Help? Characterizing Tool-Intent Stabilization in Streaming Retrieval-Augmented Generation](http://arxiv.org/abs/2606.20113v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Streaming Retrieval-Augmented Generation (Streaming RAG) reduces user-perceived latency by issuing tool queries in parallel with ongoing user input, before the utterance is complete. Reported gains are aggregate, yet the...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Predicting optimal growth temperatures of bacteria using learned structural information from a single protein](https://www.biorxiv.org/content/10.64898/2026.06.15.732269v1)
  来源：bioRxiv | 日期：2026-06-18 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Temperature is a fundamental determinant of bacterial physiology and ecology. Optimal growth temperature (OGT) is highly variable across species, contributing to differences in where and when species are most likely to t...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Protein Language Model Decoys for Target Decoy Competition in Proteomics: Quality Assessment and Benchmarks](https://www.biorxiv.org/content/10.64898/2026.03.27.714819v3)
  来源：bioRxiv | 日期：2026-06-18 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large-scale proteomics relies heavily on target--decoy competition for false discovery rate estimation in peptide identification, and the performance of this strategy depends strongly on the design of the decoy database....
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [The Unreliable Judges: Assessing Reproducibility and Self-Preference Bias of LLMs as Free-Text Evaluators](https://www.medrxiv.org/content/10.64898/2026.06.15.26355670v2)
  来源：medRxiv | 日期：2026-06-18 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) are transforming clinical practice and research, but their adoption requires rigorous evaluation. While human assessment is ideal, its cost has driven the widespread use of LLMs as evaluators...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Dual-Agent Framework for Cross-Model Verified Translation of Natural-Language Protocols into Robotic Laboratory Platform](http://arxiv.org/abs/2606.20120v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Biological experiment protocols are written in natural language, whereas automation systems rely on predefined control commands, creating a semantic gap that limits autonomous execution. Microplate-based automatic experi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [IDPForge: Deep Learning of Proteins with Global and Local Regions of Disorder](https://www.biorxiv.org/content/10.64898/2026.03.25.714313v2)
  来源：bioRxiv | 日期：2026-06-19 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：尽管机器学习在预测折叠蛋白质基态结构方面取得了显著进展，但内在无序蛋白质和区域（IDPs/IDRs）因其多样且动态的结构系综，在 AlphaFold 和 RoseTTAFold 等算法中预测置信度较低。本文提出了一种名为 IDPForge 的新机器学习方法，利用 Transformer 蛋白质语言扩散模型生成全原子 IDP 系综以及保留折叠结构域的 IDR 无序系综。IDPForge 的优势在于无需针对特定序列进行训练，也不需要从粗粒度...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Automating Information Extraction and Retrieval for Industrial Spare Parts Pooling](http://arxiv.org/abs/2606.03367v2)
  来源：arXiv | 日期：2026-06-02 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Maintenance organizations in manufacturing try to avoid downtime and unnecessary purchasing by reusing existing assets, but the main obstacle is not a lack of parts but a lack of actionable visibility across sites and pa...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Qiskit Code Migration with LLMs](http://arxiv.org/abs/2606.20173v1)
  来源：arXiv | 日期：2026-06-18 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：The rapid evolution of Quantum Development Kits (QDKs) introduces a specific form of technical debt that compromises code maintainability and hinders software reuse. In the specialized domain of Quantum Software Engineer...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Spatial omics illuminates tumor heterogeneity.](https://pubmed.ncbi.nlm.nih.gov/42320479/)
  来源：PubMed | 日期：2026-06-19 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Intratumoral heterogeneity (ITH) is the coexistence of diverse cancer cell states, genotypes, and microenvironmental niches within a single tumor and is a major driver of therapeutic resistance and disease progression. W...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ContinuumCellAgent: A Framework-Guided Agent for Long-Horizon Scientific Research](https://www.biorxiv.org/content/10.64898/2026.06.15.732409v1)
  来源：bioRxiv | 日期：2026-06-19 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：AI-scientist systems are beginning to automate parts of scientific research. We present ContinuumCellAgent, an autonomous agent that executes literature review, hypothesis formation, computational experimentation, manusc...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。
