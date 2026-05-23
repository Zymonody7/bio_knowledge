# 每日论文监控日报 (2026-05-23)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 56 篇新论文。

## 抓取状态

- arXiv：成功，命中 44 篇
- PubMed：成功，命中 52 篇
- bioRxiv：成功，命中 20 篇
- medRxiv：成功，命中 18 篇

## 最值得看

### 数据集 / Benchmark

- [GeoEPred: A Multimodal Structure-Aware Geometric Deep Learning Framework for Gram-Negative Bacterial Secreted Effector Prediction with Sequence Semantics](https://www.biorxiv.org/content/10.64898/2026.05.18.725929v1)
  来源：bioRxiv | 日期：2026-05-20 | 相关度：10.0 | 新颖度：6.5
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Accurate prediction of effector proteins secreted by Gram-negative bacteria is important for elucidating bacterial pathogenic mechanisms and developing precise anti-infective strategies. Although existing methods have be...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [ChatDIA: A zero-shot large language model workflow for targeted analysis of data-independent acquisition mass spectrometry data](https://www.biorxiv.org/content/10.64898/2026.02.11.705360v2)
  来源：bioRxiv | 日期：2026-05-20 | 相关度：7.55 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：Data-independent acquisition (DIA) proteomics enables reproducible, large-scale protein identification and quantification but remains challenging to analyze due to highly complex MS/MS spectra and chromatographic interfe...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [Language-dependent diagnostic safety of medical AI systems: a cross-lingual benchmarking and prospective clinical study](https://www.medrxiv.org/content/10.64898/2026.05.19.26353490v1)
  来源：medRxiv | 日期：2026-05-21 | 相关度：8.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Background Patients worldwide receive healthcare in many languages, yet medical AI systems are validated almost exclusively in high-resource languages such as English and Chinese, exposing patients in other linguistic se...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MyeGPT: an AI agent for Multiple Myeloma](https://www.medrxiv.org/content/10.64898/2026.05.14.26353252v1)
  来源：medRxiv | 日期：2026-05-20 | 相关度：7.55 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Today, advancements in our understanding of cancer biology are increasingly attributed to large-scale clinical-molecular datasets. The case in point for multiple myeloma - the second-most prevalent haematological maligna...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [What if Agents Could Imagine? Reinforcing Open-Vocabulary HOI Comprehension through Generation](http://arxiv.org/abs/2602.11499v2)
  来源：arXiv | 日期：2026-02-12 | 相关度：7.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Multimodal Large Language Models have shown promising capabilities in bridging visual and textual reasoning, yet their reasoning capabilities in Open-Vocabulary Human-Object Interaction (OV-HOI) are limited by cross-moda...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Comparative Study of Language Models for Khmer Retrieval-Augmented Question Answering](http://arxiv.org/abs/2605.22099v1)
  来源：arXiv | 日期：2026-05-21 | 相关度：6.55 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) has emerged as a promising paradigm for grounding large language model (LLM) outputs in retrieved evidence, thereby reducing hallucination and improving factual accuracy. Its efficacy...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DrugRAG: Enhancing Pharmacy LLM Performance Through A Novel Retrieval-Augmented Generation Pipeline](http://arxiv.org/abs/2512.14896v2)
  来源：arXiv | 日期：2025-12-16 | 相关度：6.55 | 新颖度：2.2
  匹配主题：foundation_model_agent
  中文摘要：In our study, we evaluated large language model (LLM) performance on pharmacy licensure-style question-answering tasks and developed an external knowledge integration method to improve accuracy. We benchmarked ten LLMs w...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Advancing generative large language models toward discriminative performance in protein function prediction.](https://pubmed.ncbi.nlm.nih.gov/42169056/)
  来源：PubMed | 日期：2026-05-21 | 相关度：6.45 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：While generative large language models (LLMs) have revolutionized diverse research domains through their advanced semantic understanding capabilities, their applications to protein function prediction remain limited. Alt...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RAGCap-Bench: Benchmarking Capabilities of LLMs in Agentic Retrieval Augmented Generation Systems](http://arxiv.org/abs/2510.13910v2)
  来源：arXiv | 日期：2025-10-15 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) mitigates key limitations of Large Language Models (LLMs)-such as factual errors, outdated knowledge, and hallucinations-by dynamically retrieving external information. Recent work ex...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [WCXB: A Multi-Type Web Content Extraction Benchmark](http://arxiv.org/abs/2605.21097v1)
  来源：arXiv | 日期：2026-05-20 | 相关度：6.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Web content extraction - isolating a page's main content from surrounding boilerplate - is a prerequisite for search indexing, retrieval-augmented generation, NLP dataset construction, and large language model training. ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Machine-Assisted Topic Analysis of Large-Scale Health Experience Data: Identifying Sociodemographic Differences and Evaluating Bias in Large Language Models](https://www.medrxiv.org/content/10.64898/2026.05.20.26353755v1)
  来源：medRxiv | 日期：2026-05-22 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Introduction: Large-scale free-text data with socio-demographic information can capture nuanced accounts of lived experience that are difficult to detect in structured measures. However, manual qualitative analysis is di...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Reinforced Preference Optimization for Reasoning-Augmented Recommendations](http://arxiv.org/abs/2605.21967v1)
  来源：arXiv | 日期：2026-05-21 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Recommender systems are critical for delivering personalized content across digital platforms, and recent advances in Large Language Models (LLMs) offer new opportunities to enhance them with richer world knowledge and e...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [GS-QA: A Benchmark for Geospatial Question Answering](http://arxiv.org/abs/2605.22811v1)
  来源：arXiv | 日期：2026-05-21 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in Large Language Models (LLMs) have led to dramatic improvements in question answering (QA). To address the challenge of evaluating QA systems, standardized benchmarks have been introduced. This work foc...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OSM+: Billion-Level OpenStreetMap Dataset for City-wide Experiments](http://arxiv.org/abs/2512.06743v2)
  来源：arXiv | 日期：2025-12-07 | 相关度：3.45 | 新颖度：7.25
  匹配主题：foundation_model_agent
  中文摘要：Road network data provides rich information about cities, but processing worldwide OpenStreetMap (OSM) data is computationally intensive, and the resulting graphs are often difficult to unify for benchmarking downstream ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Fine-grained Claim-level RAG Benchmark for Law](http://arxiv.org/abs/2605.21071v2)
  来源：arXiv | 日期：2026-05-20 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：The rapid progress of large language models (LLMs) is shifting semantic search toward a question-answering paradigm, where users ask questions and LLMs generate responses. In high-stake domains such as law, retrieval-aug...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [A comprehensive study on Salmonella enterica serovar Richmond in farmed fish Pangasianodon hypophthalmus: insights into zoonotic potential, virulence and antimicrobial resistance.](https://pubmed.ncbi.nlm.nih.gov/42165977/)
  来源：PubMed | 日期：2026-05-21 | 相关度：10.0 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Salmonella enterica serovar Richmond is an emerging pathogen from contaminated animal food, posing a risk of global foodborne outbreaks. Few reports have documented this species in live aquatic organisms. In this study, ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Spectra as Language: Large Language Models for Scalable Stellar Parameter and Abundance Inference](http://arxiv.org/abs/2605.22162v1)
  来源：arXiv | 日期：2026-05-21 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Stellar spectra encode key information on the physical properties and chemical compositions of stars. Accurate stellar parameter determination is essential for addressing major questions such as galaxy and stellar evolut...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches](http://arxiv.org/abs/2510.04905v3)
  来源：arXiv | 日期：2025-10-06 | 相关度：6.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in large language models (LLMs) have significantly improved automated code generation. While existing approaches have achieved strong performance at the function and file levels, real-world software engin...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [NasZip: Software and Hardware Co-Design to Accelerate Approximate Nearest Neighbor Search with DIMM-Based Near-Data Processing](http://arxiv.org/abs/2605.21952v1)
  来源：arXiv | 日期：2026-05-21 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：As large language models (LLMs) continue to advance, retrieval-augmented generation (RAG) has become the key mechanism for expanding model knowledge and reducing hallucinations. Central to RAG is approximate nearest neig...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Prediction of Transcription Factor DNA Binding Affinity with High-Throughput Kd Measurements and Deep Learning](https://www.biorxiv.org/content/10.64898/2026.05.18.725930v1)
  来源：bioRxiv | 日期：2026-05-20 | 相关度：4.6 | 新颖度：5.75
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Transcription factors (TFs) regulate gene expression through specific interactions with genomic DNA. While TF binding motifs from public databases describe sequence preferences, quantifying genome-wide affinity (Kd) is h...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Benchmarking General-Purpose and Medical AI Large Language Models for Clinical Assessment and Management in Parkinson's Disease](https://www.medrxiv.org/content/10.64898/2026.05.13.26353021v1)
  来源：medRxiv | 日期：2026-05-20 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：BackgroundThe clinical applicability of large language models (LLMs) in Parkinsons disease (PD) management remains insufficiently characterized, particularly in generative responses to clinical vignette scenarios. Object...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [An RNA Language Model trained on sequence alone reveals the structural logic of Internal Ribosome Entry Sites](https://www.biorxiv.org/content/10.64898/2026.05.19.726202v1)
  来源：bioRxiv | 日期：2026-05-20 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Viral RNA genomes are among the most information-dense codes in biology. In picornaviruses, translation depends entirely on Internal Ribosome Entry Sites (IRESes), yet their structures remain largely unresolved. Previous...
  为什么值得看：bioRxiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [SLiMNet: a deep learning model to detect short linear motifs using protein large language model representations and paired inputs](https://www.biorxiv.org/content/10.64898/2026.05.04.722713v2)
  来源：bioRxiv | 日期：2026-05-20 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Short linear motifs (SLiMs) are short (3-15 amino acids in length) segments within intrinsically disordered regions (IDRs) that mediate transient protein-protein interactions as well as other functions such as stability ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Mem-$π$: Adaptive Memory through Learning When and What to Generate](http://arxiv.org/abs/2605.21463v1)
  来源：arXiv | 日期：2026-05-20 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：We present Mem-$π$, a framework for adaptive memory in large language model (LLM) agents, where useful guidance is generated on demand rather than retrieved from external memory stores. Existing memory-augmented agents t...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AutoRPA: Efficient GUI Automation through LLM-Driven Code Synthesis from Interactions](http://arxiv.org/abs/2605.21082v1)
  来源：arXiv | 日期：2026-05-20 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large Language Model (LLM) based agents have demonstrated proficiency in multi-step interactions with graphical user interfaces (GUIs). While most research focuses on improving single-task performance, practical scenario...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Drug or Pokemon? An analysis of the ability of large language models to discern fabricated medications](https://www.medrxiv.org/content/10.64898/2026.01.12.26343930v3)
  来源：medRxiv | 日期：2026-05-20 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：尽管大语言模型（LLM）越来越多地用于药物相关任务，但其准确性和安全性证据有限。本研究旨在建立基准任务，评估 LLM 区分虚构药物与真实药物的能力。研究开发了品牌药和通用药两个数据集，各包含 250 个药物列表，每个列表含 4-6 种真实药物及一个虚构药物（宝可梦角色），并提供完整剂量信息。评估了 GPT-5-Chat、GPT-4o-mini、DrugGPT、Gemma-3-27B-IT、Llama-3.3-70B-Instruct 和...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AFD-INSTRUCTION: A Comprehensive Antibody Instruction Dataset with Functional Annotations for LLM-Based Understanding and Design](http://arxiv.org/abs/2602.04916v3)
  来源：arXiv | 日期：2026-02-04 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have significantly advanced protein representation learning. However, their capacity to interpret and design antibodies through natural language remains limited. To address this challenge, we...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CALMem : Application-Layer Dual Memory for Conversational AI](http://arxiv.org/abs/2605.20724v1)
  来源：arXiv | 日期：2026-05-20 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) operate within fixed context windows that fundamentally limit conversational continuity. When context fills, compaction discards history irreversibly; when sessions end, all memory resets to ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ChronoMedKG: A Temporally-Grounded Biomedical Knowledge Graph and Benchmark for Clinical Reasoning](http://arxiv.org/abs/2605.22734v1)
  来源：arXiv | 日期：2026-05-21 | 相关度：2.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Biomedical knowledge graphs (KGs) treat disease associations as static facts, but temporal information is crucial for clinical reasoning, e.g., a symptom diagnostic of one disease at age 3 may imply a different disease a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MTR-Suite: A Framework for Evaluating and Synthesizing Conversational Retrieval Benchmarks](http://arxiv.org/abs/2605.20729v1)
  来源：arXiv | 日期：2026-05-20 | 相关度：2.1 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Accurate evaluation of conversational retrieval is pivotal for advancing Retrieval-Augmented Generation (RAG) systems. However, existing conversational retrieval benchmarks suffer from costly, sparse human annotation or ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SMDD-Bench: Can LLMs Solve Real-World Small Molecule Drug Design Tasks?](http://arxiv.org/abs/2605.21740v1)
  来源：arXiv | 日期：2026-05-20 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：LLM agents have incredible potential for scientific discovery applications. However, the performance of LLM agents on real-world, small molecule drug design (SMDD) tasks across diverse chemistries and targets is unclear....
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OmniCellAgent: An AI Scientist for Omic-Driven Scientific Discovery](https://www.biorxiv.org/content/10.1101/2025.07.31.667797v2)
  来源：bioRxiv | 日期：2026-05-20 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：In biomedical scientific discovery, identifying relevant omics datasets and interpreting analysis results using prior knowledge from databases and literature are essential for generating novel hypotheses. Although recent...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CacheClip: Accelerating RAG with Effective KV Cache Reuse](http://arxiv.org/abs/2510.10129v2)
  来源：arXiv | 日期：2025-10-11 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) systems suffer from severe time-to-first-token (TTFT) bottlenecks due to long input sequences. Existing KV cache reuse methods face a fundamental trade-off: prefix caching requires id...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [APM: Evaluating Style Personalization in LLMs with Arbitrary Preference Mappings](http://arxiv.org/abs/2605.21063v1)
  来源：arXiv | 日期：2026-05-20 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Typical LLM responses tend to follow a default style, even though users often have distinct preferences regarding tone, verbosity, and formality that they do not explicitly state in their prompts. Evaluating whether pers...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Sound Agentic Science Requires Adversarial Experiments](http://arxiv.org/abs/2604.22080v2)
  来源：arXiv | 日期：2026-04-23 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：LLM-based agents are rapidly being adopted for scientific data analysis, automating tasks once limited by human time and expertise. This capability is often framed as an acceleration of discovery, but it also accelerates...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Can Current Agents Close the Discovery-to-Application Gap? A Case Study in Minecraft](http://arxiv.org/abs/2604.24697v2)
  来源：arXiv | 日期：2026-04-27 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Discovering causal regularities and applying them to build functional systems--the discovery-to-application loop--is a hallmark of general intelligence, yet evaluating this capacity has been hindered by the vast complexi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [EvoStruct: Bridging Evolutionary and Structural Priors for Antibody CDR Design via Protein Language Model Adaptation](http://arxiv.org/abs/2605.21485v1)
  来源：arXiv | 日期：2026-05-20 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Equivariant graph neural network (GNN) methods for antibody complementarity-determining region (CDR) design achieve the highest sequence recovery but suffer from severe vocabulary collapse. The current best GNN methods o...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [GraphRAG on Consumer Hardware: Benchmarking Local LLMs for Healthcare EHR Schema Retrieval](http://arxiv.org/abs/2605.20815v1)
  来源：arXiv | 日期：2026-05-20 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Graph-based Retrieval Augmented Generation (GraphRAG) extends retrieval-augmented generation to support structured reasoning over complex corpora, but its reliability under resource-constrained, privacy-sensitive deploym...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [A pan-cancer regulatory atlas of 6,983 GWAS variants prioritizes recurrent regulatory annotations and candidate programs at cancer risk loci](https://www.medrxiv.org/content/10.64898/2026.05.16.26353369v1)
  来源：medRxiv | 日期：2026-05-20 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：O_FIG O_LINKSMALLFIG WIDTH=200 HEIGHT=159 SRC="FIGDIR/small/26353369v1_ufig1.gif" ALT="Figure 1"> View larger version (64K): org.highwire.dtl.DTLVardef@1b34e41org.highwire.dtl.DTLVardef@d6a3d1org.highwire.dtl.DTLVardef@1...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Towards Generalization of Block Attention via Automatic Segmentation and Block Distillation](http://arxiv.org/abs/2605.15913v2)
  来源：arXiv | 日期：2026-05-15 | 相关度：1.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：Block attention, which processes the input as separate blocks that cannot attend to one another, offers significant potential to improve KV cache reuse in long-context scenarios such as Retrieval-Augmented Generation (RA...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [A Unified H i Rotation Curve Database for 129 Local Volume Dwarf and Irregular Galaxies](http://arxiv.org/abs/2605.22163v1)
  来源：arXiv | 日期：2026-05-21 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：We present a unified H i rotation curve database for 129 dwarf and irregular galaxies drawn from four Local Volume surveys: the Local Volume H i Survey (LVHIS; 33 galaxies), VLA-ANGST (29), LITTLE THINGS (26), and WALLAB...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Sequential Data Augmentation for Generative Recommendation](http://arxiv.org/abs/2509.13648v3)
  来源：arXiv | 日期：2025-09-17 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Generative recommendation plays a crucial role in personalized systems, predicting users' future interactions from their historical behavior sequences. A critical yet underexplored factor in training these models is data...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [MARRVEL-MCP: An agentic interface for Mendelian disease discovery via tool-augmented context engineering.](https://pubmed.ncbi.nlm.nih.gov/42167217/)
  来源：PubMed | 日期：2026-05-21 | 相关度：6.75 | 新颖度：0.25
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：Variant interpretation in rare diseases requires navigating multiple genomic databases, each with strict input formats, while synthesizing heterogeneous evidence. This process creates significant barriers for non-experts...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A Potent CRISPR-Cas12l Double-Strand Break Gene Editor.](https://pubmed.ncbi.nlm.nih.gov/42163774/)
  来源：PubMed | 日期：2026-05-21 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Recently, a new family of CRISPR-Cas12 endonucleases from an unexplored phylum of bacteria, Armatimonadota , was discovered. Named Cas12l, they are compact (800-900 aa), recognize a 5' C-rich protospacer adjacent motif, ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ATACompass enables cross-species cell identity mapping for scATAC-seq without gene annotations.](https://pubmed.ncbi.nlm.nih.gov/42167226/)
  来源：PubMed | 日期：2026-05-21 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Single-cell assay for transposase-accessible chromatin with sequencing (scATAC-seq) provides insights into transcriptional regulation, but there remain challenges in cell identity annotation due to data sparsity and limi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Towards Autonomous Mechanistic Reasoning in Virtual Cells](http://arxiv.org/abs/2604.11661v3)
  来源：arXiv | 日期：2026-04-13 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have recently gained significant attention as a promising approach to accelerate scientific discovery. However, their application in open-ended scientific domains such as biology remains limi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CancerOmicsStudio (CoS): A web server for integrative and interpretable analysis of multi-omics cancer data.](https://pubmed.ncbi.nlm.nih.gov/42162949/)
  来源：PubMed | 日期：2026-05-20 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large-scale omics resources, including The Cancer Genome Atlas, Genomics of Drug Sensitivity in Cancer, and the Cancer Dependency Map, have become essential for cancer research. However, these datasets are distributed ac...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [resLens: genomic language models to enhance antibiotic resistance gene detection.](https://pubmed.ncbi.nlm.nih.gov/42168341/)
  来源：PubMed | 日期：2026-05-21 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：The rise of antibiotic resistance necessitates advanced tools to detect and analyze antibiotic resistance genes (ARGs). We present resLens, a family of genomic language models that leverage latent genomic representations...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Sutra: Tensor-Op RNNs as a Compilation Target for Vector Symbolic Architectures](http://arxiv.org/abs/2605.20919v1)
  来源：arXiv | 日期：2026-05-20 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Sutra is a typed, purely functional programming language whose compiled forward pass is a PyTorch neural network. The compiler beta-reduces the whole program -- primitives, control flow, string I/O -- to one fused tensor...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [END: Early Noise Dropping for Efficient and Effective Context Denoising](http://arxiv.org/abs/2502.18915v3)
  来源：arXiv | 日期：2025-02-26 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have demonstrated remarkable performance across a wide range of natural language processing tasks. However, they are often distracted by irrelevant or noisy context in input sequences that de...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AI-genomics synergy for drug repurposing in breast cancer: an interpretability-driven framework.](https://pubmed.ncbi.nlm.nih.gov/42162002/)
  来源：PubMed | 日期：2026-05-20 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Breast cancer's genomic heterogeneity complicates drug discovery, making repurposing an attractive but challenging strategy. Advances in artificial intelligence now enable integration of multi-omics data to reveal drug-g...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Cell Phantom Video Generation in Elliptical Fourier Descriptor Domain](http://arxiv.org/abs/2605.22563v1)
  来源：arXiv | 日期：2026-05-21 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Training Deep Neural Networks for tracking individual cells in biomedical videos requires a large amount of annotated data. The annotation of videos for cell tracking is very time consuming and often requires domain expe...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AOP-Wiki EMOD 3.0: Data Model Expansions and Content Evaluation Framework for Using Agentic AI to Improve Integration between AOPs and New Approach Methodologies (NAMs)](http://arxiv.org/abs/2605.21645v1)
  来源：arXiv | 日期：2026-05-20 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Adverse Outcome Pathways (AOP) are logic models that causally link biological mechanisms that can be measured in a lab to adverse outcomes, relevant to chemical regulatory endpoints. AOPs contextualize new approach metho...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Evaluating Sycophancy in Frontier Models Using Persona-Driven Challenge](https://www.medrxiv.org/content/10.64898/2026.05.17.26353406v1)
  来源：medRxiv | 日期：2026-05-20 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly used for lay health queries, yet may abandon correct recommendations under pressure, a vulnerability termed sycophancy. We evaluated sycophancy across five frontier LLMs (Cla...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [ASO Special Article: Proceedings of the Inaugural Joint US-India Cancer Dialogue: Accelerating Collaboration to Advance Cancer Prevention, Early Detection, Treatment, and Care.](https://pubmed.ncbi.nlm.nih.gov/42166060/)
  来源：PubMed | 日期：2026-05-21 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Cancer is a leading cause of death in both the USA and India. During Prime Minister Narendra Modi's State Visit to Washington, DC in June 2023, the two governments announced several cooperation commitments. One such comm...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Claim-Selective Certification for High-Risk Medical Retrieval-Augmented Generation](http://arxiv.org/abs/2605.21949v1)
  来源：arXiv | 日期：2026-05-21 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Medical RAG systems in high-risk QA settings are often evaluated through a single answer-or-abstain decision, but mixed evidence may support one claim, require conditions for another, and contradict a third. We study cla...
  为什么值得看：Claim-Selective Certification for High-R 与你的主题有弱匹配，暂时保留作低优先级跟踪。
