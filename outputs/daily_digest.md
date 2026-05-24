# 每日论文监控日报 (2026-05-24)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 26 篇新论文。

## 抓取状态

- arXiv：成功，命中 15 篇
- PubMed：成功，命中 39 篇
- bioRxiv：成功，命中 13 篇
- medRxiv：成功，命中 14 篇

## 最值得看

### Foundation Model / Agent

- [BioRAG-DRAG: A Multimodal Biological Retrieval Layer for Local-First Biomedical Agents](https://www.biorxiv.org/content/10.64898/2026.05.19.726174v1)
  来源：bioRxiv | 日期：2026-05-21 | 相关度：8.9 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Biomedical agents need reliable access to heterogeneous evidence: literature text, gene and pathway records, protein sequences, DNA/cDNA sequences, and structured biological relations. Classical sequence tools such as BL...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [Digital Registrar: A Schema-First Framework for Multi-Cancer Privacy-Preserving Pathology Abstraction via Local LLMs](https://www.medrxiv.org/content/10.1101/2025.10.21.25338475v9)
  来源：medRxiv | 日期：2026-05-23 | 相关度：8.9 | 新颖度：1.7
  匹配主题：foundation_model_agent
  中文摘要：手术病理报告包含精细的癌症诊断数据，但其自由文本格式阻碍了自动化登记和二次分析。本研究开发了“Digital Registrar”框架，其核心是基于美国病理学家协会（CAP）标准的临床本体，通过严格类型的分层架构和 DSPy 签名实现。该系统涵盖 10 种主要癌症类型，涉及 193 个登记字段，包括淋巴结组和手术切缘等复杂变量。研究利用 DSPy 框架构建了与模型无关的提取流水线，并在单块 48GB GPU 上测试了本地部署的可行性。实...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [NEURA: A proof-carrying framework for hallucination-resistant neuroimaging automation](https://www.biorxiv.org/content/10.64898/2026.04.27.721217v2)
  来源：bioRxiv | 日期：2026-05-21 | 相关度：7.9 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Neuroimaging research depends on heterogeneous software, multimodal data and multistage statistical workflows. Large language model (LLM)-based agents offer a route to automate these workflows, but their susceptibility t...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MyeGPT: an AI agent for Multiple Myeloma](https://www.medrxiv.org/content/10.64898/2026.05.14.26353252v2)
  来源：medRxiv | 日期：2026-05-23 | 相关度：7.55 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Today, advancements in our understanding of cancer biology are increasingly attributed to large-scale clinical-molecular datasets. The case in point for multiple myeloma - the second-most prevalent haematological maligna...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Comparative Study of Language Models for Khmer Retrieval-Augmented Question Answering](http://arxiv.org/abs/2605.22099v1)
  来源：arXiv | 日期：2026-05-21 | 相关度：6.55 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) has emerged as a promising paradigm for grounding large language model (LLM) outputs in retrieved evidence, thereby reducing hallucination and improving factual accuracy. Its efficacy...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Advancing generative large language models toward discriminative performance in protein function prediction.](https://pubmed.ncbi.nlm.nih.gov/42169056/)
  来源：PubMed | 日期：2026-05-21 | 相关度：6.45 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：While generative large language models (LLMs) have revolutionized diverse research domains through their advanced semantic understanding capabilities, their applications to protein function prediction remain limited. Alt...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [PlasmidLM: A Promptable DNA Language Model via Verifiable-Reward Post-Training](https://www.biorxiv.org/content/10.64898/2026.05.19.725242v1)
  来源：bioRxiv | 日期：2026-05-21 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Generative DNA models are typically next-token completers: they extend a sequence but offer no native interface for telling the model what to make. PlasmidLM is a promptable DNA language model for plasmids. A designer su...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [A comprehensive study on Salmonella enterica serovar Richmond in farmed fish Pangasianodon hypophthalmus: insights into zoonotic potential, virulence and antimicrobial resistance.](https://pubmed.ncbi.nlm.nih.gov/42165977/)
  来源：PubMed | 日期：2026-05-21 | 相关度：10.0 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Salmonella enterica serovar Richmond is an emerging pathogen from contaminated animal food, posing a risk of global foodborne outbreaks. Few reports have documented this species in live aquatic organisms. In this study, ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Spectra as Language: Large Language Models for Scalable Stellar Parameter and Abundance Inference](http://arxiv.org/abs/2605.22162v1)
  来源：arXiv | 日期：2026-05-21 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Stellar spectra encode key information on the physical properties and chemical compositions of stars. Accurate stellar parameter determination is essential for addressing major questions such as galaxy and stellar evolut...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [NanoCortex: A Unified Agentic System for Nanopore Sequencing Analysis](https://www.biorxiv.org/content/10.64898/2026.05.19.726254v1)
  来源：bioRxiv | 日期：2026-05-21 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Nanopore sequencing has enabled various layers of information about DNA and RNA sequence isoforms and chemical modifications. Yet, the archipelago of disjoint nanopore analysis tools makes navigating among these a signif...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Language-dependent diagnostic safety of medical AI systems: a cross-lingual benchmarking and prospective clinical study](https://www.medrxiv.org/content/10.64898/2026.05.19.26353490v1)
  来源：medRxiv | 日期：2026-05-21 | 相关度：7.8 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：BackgroundPatients worldwide receive healthcare in many languages, yet medical AI systems are validated almost exclusively in high-resource languages such as English and Chinese, exposing patients in other linguistic set...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [RAGCap-Bench: Benchmarking Capabilities of LLMs in Agentic Retrieval Augmented Generation Systems](http://arxiv.org/abs/2510.13910v2)
  来源：arXiv | 日期：2025-10-15 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) mitigates key limitations of Large Language Models (LLMs)-such as factual errors, outdated knowledge, and hallucinations-by dynamically retrieving external information. Recent work ex...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Machine-Assisted Topic Analysis of Large-Scale Health Experience Data: Identifying Sociodemographic Differences and Evaluating Bias in Large Language Models](https://www.medrxiv.org/content/10.64898/2026.05.20.26353755v1)
  来源：medRxiv | 日期：2026-05-22 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Introduction: Large-scale free-text data with socio-demographic information can capture nuanced accounts of lived experience that are difficult to detect in structured measures. However, manual qualitative analysis is di...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [GS-QA: A Benchmark for Geospatial Question Answering](http://arxiv.org/abs/2605.22811v1)
  来源：arXiv | 日期：2026-05-21 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in Large Language Models (LLMs) have led to dramatic improvements in question answering (QA). To address the challenge of evaluating QA systems, standardized benchmarks have been introduced. This work foc...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OSM+: Billion-Level OpenStreetMap Dataset for City-wide Experiments](http://arxiv.org/abs/2512.06743v2)
  来源：arXiv | 日期：2025-12-07 | 相关度：3.45 | 新颖度：2.25
  匹配主题：foundation_model_agent
  中文摘要：Road network data provides rich information about cities, but processing worldwide OpenStreetMap (OSM) data is computationally intensive, and the resulting graphs are often difficult to unify for benchmarking downstream ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ChronoMedKG: A Temporally-Grounded Biomedical Knowledge Graph and Benchmark for Clinical Reasoning](http://arxiv.org/abs/2605.22734v1)
  来源：arXiv | 日期：2026-05-21 | 相关度：2.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Biomedical knowledge graphs (KGs) treat disease associations as static facts, but temporal information is crucial for clinical reasoning, e.g., a symptom diagnostic of one disease at age 3 may imply a different disease a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CacheClip: Accelerating RAG with Effective KV Cache Reuse](http://arxiv.org/abs/2510.10129v2)
  来源：arXiv | 日期：2025-10-11 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) systems suffer from severe time-to-first-token (TTFT) bottlenecks due to long input sequences. Existing KV cache reuse methods face a fundamental trade-off: prefix caching requires id...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Fine-grained Claim-level RAG Benchmark for Law](http://arxiv.org/abs/2605.21071v2)
  来源：arXiv | 日期：2026-05-20 | 相关度：4.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：The rapid progress of large language models (LLMs) is shifting semantic search toward a question-answering paradigm, where users ask questions and LLMs generate responses. In high-stake domains such as law, retrieval-aug...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Towards Generalization of Block Attention via Automatic Segmentation and Block Distillation](http://arxiv.org/abs/2605.15913v2)
  来源：arXiv | 日期：2026-05-15 | 相关度：1.4 | 新颖度：1.5
  匹配主题：未命中具体主题
  中文摘要：Block attention, which processes the input as separate blocks that cannot attend to one another, offers significant potential to improve KV cache reuse in long-context scenarios such as Retrieval-Augmented Generation (RA...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [A Unified H i Rotation Curve Database for 129 Local Volume Dwarf and Irregular Galaxies](http://arxiv.org/abs/2605.22163v1)
  来源：arXiv | 日期：2026-05-21 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：We present a unified H i rotation curve database for 129 dwarf and irregular galaxies drawn from four Local Volume surveys: the Local Volume H i Survey (LVHIS; 33 galaxies), VLA-ANGST (29), LITTLE THINGS (26), and WALLAB...
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

- [resLens: genomic language models to enhance antibiotic resistance gene detection.](https://pubmed.ncbi.nlm.nih.gov/42168341/)
  来源：PubMed | 日期：2026-05-21 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：The rise of antibiotic resistance necessitates advanced tools to detect and analyze antibiotic resistance genes (ARGs). We present resLens, a family of genomic language models that leverage latent genomic representations...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Cell Phantom Video Generation in Elliptical Fourier Descriptor Domain](http://arxiv.org/abs/2605.22563v1)
  来源：arXiv | 日期：2026-05-21 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Training Deep Neural Networks for tracking individual cells in biomedical videos requires a large amount of annotated data. The annotation of videos for cell tracking is very time consuming and often requires domain expe...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [ASO Special Article: Proceedings of the Inaugural Joint US-India Cancer Dialogue: Accelerating Collaboration to Advance Cancer Prevention, Early Detection, Treatment, and Care.](https://pubmed.ncbi.nlm.nih.gov/42166060/)
  来源：PubMed | 日期：2026-05-21 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Cancer is a leading cause of death in both the USA and India. During Prime Minister Narendra Modi's State Visit to Washington, DC in June 2023, the two governments announced several cooperation commitments. One such comm...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
