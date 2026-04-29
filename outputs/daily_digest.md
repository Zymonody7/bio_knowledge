# 每日论文监控日报 (2026-04-29)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 53 篇新论文。

## 抓取状态

- arXiv：成功，命中 49 篇
- PubMed：成功，命中 28 篇
- bioRxiv：成功，命中 15 篇
- medRxiv：成功，命中 4 篇

## 最值得看

### Foundation Model / Agent

- [Branching Flows: Discrete, Continuous, and Manifold Flow Matching with Splits and Deletions](http://arxiv.org/abs/2511.09465v3)
  来源：arXiv | 日期：2025-11-12 | 相关度：8.9 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Diffusion and flow matching approaches to generative modeling have shown promise in domains where the state space is continuous, such as image generation or protein folding & design, and discrete, exemplified by diffusio...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RareCollab: an LLM-powered framework for multimodal reasoning in Mendelian disease diagnosis](http://arxiv.org/abs/2602.04058v2)
  来源：arXiv | 日期：2026-02-03 | 相关度：7.8 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Rare disease diagnosis increasingly relies on integrating genomic, phenotypic and transcriptomic evidence, yet these signals remain difficult to reconcile within a common interpretive framework. Here we present RareColla...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Multi-modal LLM-Knowledge Fusion Framework for Predicting Single-cell Genetic Perturbation Effects](https://www.biorxiv.org/content/10.64898/2026.04.24.720560v1)
  来源：bioRxiv | 日期：2026-04-28 | 相关度：7.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Understanding cellular responses to genetic perturbations is fundamental for drug discovery, yet experimental approaches face significant limitations in coverage and cost that prevent comprehensive mapping of cellular be...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [AI-Augmented Bibliometric Framework: A Paradigm Shift with Agentic AI for Dynamic, Snippet-Based Research Analysis](http://arxiv.org/abs/2511.21745v2)
  来源：arXiv | 日期：2025-11-22 | 相关度：7.9 | 新颖度：6.2
  匹配主题：foundation_model_agent
  中文摘要：Our paper introduces a generative, multiagent AI framework designed to overcome the rigidity, limited flexibility and technical barriers of current bibliometric tools. The objective is to enable researchers to perform fu...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [From simulation to pedagogy: structured AI standardized patients for clinical communication training validated through multi-model and randomized evaluation](https://www.medrxiv.org/content/10.64898/2026.04.26.26351793v1)
  来源：medRxiv | 日期：2026-04-28 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Standardized patients (SPs) are central to clinical communication training but are constrained by cost, scalability, and reliance on trained actors. We present AI standardized patients (AI-SPs), large language model-driv...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MEG-RAG: Quantifying Multi-modal Evidence Grounding for Evidence Selection in RAG](http://arxiv.org/abs/2604.24564v1)
  来源：arXiv | 日期：2026-04-27 | 相关度：6.8 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Multimodal Retrieval-Augmented Generation (MRAG) addresses key limitations of Multimodal Large Language Models (MLLMs), such as hallucination and outdated knowledge. However, current MRAG systems struggle to distinguish ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MERIT: Modular Framework for Multimodal Misinformation Detection with Web-Grounded Reasoning](http://arxiv.org/abs/2510.17590v2)
  来源：arXiv | 日期：2025-10-20 | 相关度：6.8 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：We present MERIT, an inference-time modular framework for multimodal misinformation detection that decomposes verification into four specialized modules: visual forensics, cross-modal alignment, retrieval-augmented claim...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Comparative Study in Surgical AI: Datasets, Foundation Models, and Barriers to Med-AGI](https://www.medrxiv.org/content/10.64898/2026.03.26.26349455v3)
  来源：medRxiv | 日期：2026-04-28 | 相关度：6.8 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：近年来，AI在多项生物医学任务中已达到或超越人类专家水平，但在外科图像分析基准上表现滞后。外科手术需要整合多模态数据、人类交互及物理效应，因此通用AI模型作为协作工具具有巨大潜力。然而，尽管每年产生数百万小时的手术视频，但数据准备需要极高的专业知识，且训练成本高昂。本研究以2026年最先进的AI方法为基础，针对神经外科手术器械检测进行了案例研究。结果显示，即使是拥有数十亿参数的模型并经过广泛训练，目前的视觉语言模型（VLM）在简单的器械...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Silent numerical failures in large language model-generated pharmacokinetic simulation code: a benchmark against target-controlled infusion validation criteria using the Marsh propofol model](https://www.medrxiv.org/content/10.64898/2026.04.27.26351582v1)
  来源：medRxiv | 日期：2026-04-28 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Background. Large language models (LLMs) are increasingly used by clinicians to generate executable code for pharmacokinetic (PK) simulation. Whether such code meets the accuracy standards of target-controlled infusion s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Prism-Reranker: Beyond Relevance Scoring -- Jointly Producing Contributions and Evidence for Agentic Retrieval](http://arxiv.org/abs/2604.23734v1)
  来源：arXiv | 日期：2026-04-26 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Modern retrieval pipelines increasingly serve downstream consumers like retrieval-augmented generation (RAG) and autonomous agents that need more than a scalar relevance score. A reranker that only tells the caller "how ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Polymer-Agent: Large Language Model Agent for Polymer Design.](https://pubmed.ncbi.nlm.nih.gov/42048526/)
  来源：PubMed | 日期：2026-04-28 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：On-demand polymer discovery is essential across various industries, from biomedical applications to reinforcement materials. Experiments with polymers involve a long trial-and-error process that consumes extensive resour...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Structure-Grounded Knowledge Retrieval via Code Dependencies for Multi-Step Data Reasoning](http://arxiv.org/abs/2604.10516v3)
  来源：arXiv | 日期：2026-04-12 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Selecting the right knowledge is critical when using large language models (LLMs) to solve domain-specific data analysis tasks. However, most retrieval-augmented approaches rely primarily on lexical or embedding similari...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MIMIC: A Generative Multimodal Foundation Model for Biomolecules](http://arxiv.org/abs/2604.24506v1)
  来源：arXiv | 日期：2026-04-27 | 相关度：4.45 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Biological function emerges from coupled constraints across sequence, structure, regulation, evolution, and cellular context, yet most foundation models in biology are trained within one modality or for a fixed forward t...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Domain Fine-Tuning vs. Retrieval-Augmented Generation for Medical Multiple-Choice Question Answering: A Controlled Comparison at the 4B-Parameter Scale](http://arxiv.org/abs/2604.23801v1)
  来源：arXiv | 日期：2026-04-26 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Practitioners deploying small open-weight large language models (LLMs) for medical question answering face a recurring design choice: invest in a domain-fine-tuned model, or keep a general-purpose model and inject domain...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Personalization Toolkit: Training Free Personalization of Large Vision Language Models](http://arxiv.org/abs/2502.02452v4)
  来源：arXiv | 日期：2025-02-04 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Personalization of Large Vision-Language Models (LVLMs) involves customizing models to recognize specific users or object instances and to generate contextually tailored responses. Existing approaches rely on time-consum...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [CUB: Benchmarking Context Utilisation Techniques for Language Models](http://arxiv.org/abs/2505.16518v3)
  来源：arXiv | 日期：2025-05-22 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Incorporating external knowledge is crucial for knowledge-intensive tasks, such as question answering and fact checking. However, language models (LMs) may ignore relevant information that contradicts outdated parametric...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Enhancing Financial Report Question-Answering: A Retrieval-Augmented Generation System with Reranking Analysis](http://arxiv.org/abs/2603.16877v2)
  来源：arXiv | 日期：2026-02-18 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Financial analysts face significant challenges extracting information from lengthy 10-K reports, which often exceed 100 pages. This paper presents a Retrieval-Augmented Generation (RAG) system designed to answer question...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Risk Based Prediction of Novel AMR Variants Using Protein Language Models](https://www.biorxiv.org/content/10.1101/2025.09.12.672331v2)
  来源：bioRxiv | 日期：2026-04-27 | 相关度：9.65 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：抗生素耐药性（AMR）是全球健康的重大威胁，监测系统亟需检测已知及新兴的耐药标志物。本研究开发了 AMRscope，这是一种基于 ESM2 蛋白质语言模型（PLM）嵌入向量的预测模型，专门用于评估单位点突变导致耐药的可能性。该工具应用于多种细菌的抗生素相互作用蛋白，涵盖了世卫组织（WHO）重点病原体，如耐利福平结核分枝杆菌和耐碳青霉烯铜绿假单胞菌。实验结果显示，在随机划分的数据集上，模型达到了 0.88 的准确率、0.87 的 F1 分...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [mKG-RAG: Leveraging Multimodal Knowledge Graphs in Retrieval-Augmented Generation for Knowledge-intensive VQA](http://arxiv.org/abs/2508.05318v2)
  来源：arXiv | 日期：2025-08-07 | 相关度：6.8 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) has emerged as an effective paradigm for expanding the knowledge capacity of Multimodal Large Language Models (MLLMs) by incorporating external knowledge sources into the generation p...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [From Ambiguity to Accuracy: The Transformative Effect of Coreference Resolution on Retrieval-Augmented Generation systems](http://arxiv.org/abs/2507.07847v3)
  来源：arXiv | 日期：2025-07-10 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) has emerged as a crucial framework in natural language processing (NLP), improving factual consistency and reducing hallucinations by integrating external document retrieval with larg...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [XGRAG: A Graph-Native Framework for Explaining KG-based Retrieval-Augmented Generation](http://arxiv.org/abs/2604.24623v1)
  来源：arXiv | 日期：2026-04-27 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Graph-based Retrieval-Augmented Generation (GraphRAG) extends traditional RAG by using knowledge graphs (KGs) to give large language models (LLMs) a structured, semantically coherent context, yielding more grounded answe...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Question-Adaptive Graph Learning for Multi-hop Retrieval Augmented Generation](http://arxiv.org/abs/2510.11541v2)
  来源：arXiv | 日期：2025-10-13 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) has demonstrated its ability to enhance Large Language Models (LLMs) by integrating external knowledge sources. However, multi-hop questions, which require the identification of multi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [In-depth Analysis of Graph-based RAG in a Unified Framework](http://arxiv.org/abs/2503.04338v2)
  来源：arXiv | 日期：2025-03-06 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Graph-based Retrieval-Augmented Generation (RAG) has proven effective in integrating external knowledge into large language models (LLMs), improving their factual accuracy, adaptability, interpretability, and trustworthi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MEMCoder: Multi-dimensional Evolving Memory for Private-Library-Oriented Code Generation](http://arxiv.org/abs/2604.24222v1)
  来源：arXiv | 日期：2026-04-27 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) excel at general code generation, but their performance drops sharply in enterprise settings that rely on internal private libraries absent from public pre-training corpora. While Retrieval-A...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [S2G-RAG: Structured Sufficiency and Gap Judging for Iterative Retrieval-Augmented QA](http://arxiv.org/abs/2604.23783v1)
  来源：arXiv | 日期：2026-04-26 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) grounds language models in external evidence, but multi-hop question answering remains difficult because iterative pipelines must control what to retrieve next and when the available ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GeoSearch: Augmenting Worldwide Geolocalization with Web-Scale Reverse Image Search and Image Matching](http://arxiv.org/abs/2604.25390v1)
  来源：arXiv | 日期：2026-04-28 | 相关度：3.45 | 新颖度：6.98
  匹配主题：foundation_model_agent
  中文摘要：Worldwide image geolocalization, which aims to predict the GPS coordinates of any image on Earth, remains challenging due to global visual diversity. Recent generative approaches based on Retrieval-Augmented Generation (...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Vibe Medicine: Redefining Biomedical Research Through Human-AI Co-Work](http://arxiv.org/abs/2604.23674v1)
  来源：arXiv | 日期：2026-04-26 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：With the emergence of large language models (LLMs) and AI agent frameworks, the human-AI co-work paradigm known as Vibe Coding is changing how people code, making it more accessible and productive. In scientific research...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [BRIEF-Pro: Universal Context Compression with Short-to-Long Synthesis for Fast and Accurate Multi-Hop Reasoning](http://arxiv.org/abs/2510.13799v2)
  来源：arXiv | 日期：2025-10-15 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：As retrieval-augmented generation (RAG) tackles complex tasks, increasingly expanded contexts offer richer information, but at the cost of higher latency and increased cognitive load on the model. To mitigate this bottle...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Decoding the phenomenology of spontaneous thought using large language-model ratings on verbal retrospective free reports](https://www.biorxiv.org/content/10.64898/2026.04.22.720079v1)
  来源：bioRxiv | 日期：2026-04-26 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：自发性思维占据了日常内心体验的大部分，但其内容和神经生理基础的探索长期受限于方法学挑战。传统思维探测法限制了现象学报告的完整性，而实时口头报告则会干扰思维流并产生运动伪迹。本研究设计并测试了一种新方法，将延迟口头回顾性自由报告（RFR）与大语言模型（LLM）生成的自动现象学评分相结合，以评估自发思维的神经基础。22名参与者完成了闭眼自由思考任务，其报告由四种最先进的LLM和人类评分小组针对10个现象学维度进行评估。随后，研究者训练机器学...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [All Models are Wrong, Some are Annotated: Automating Metadata in Biomedical Repositories](https://www.biorxiv.org/content/10.64898/2026.04.23.720371v1)
  来源：bioRxiv | 日期：2026-04-27 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：高质量元数据对科学发现至关重要，但生物医学数据库中普遍存在的标注稀疏问题限制了生物学细节的获取。本研究评估了大语言模型（LLMs）从神经科学数据库 ModelDB 的源代码中自动推断离子通道和受体亚型元数据的能力。研究者从 ModelDB 提取了 5,133 个模型文件，并对其中 1,100 个进行了人工标注（253 个用于测试）。实验对比了 GPT-5.2 和 GPT-mini 在零样本及启发式增强提示下的表现，并以特征工程驱动的 X...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RADD: Retrieval-Augmented Discrete Diffusion for Multi-Modal Knowledge Graph Completion](http://arxiv.org/abs/2604.25693v1)
  来源：arXiv | 日期：2026-04-28 | 相关度：2.75 | 新颖度：7.62
  匹配主题：foundation_model_agent
  中文摘要：Most multi-modal knowledge graph completion (MMKGC) models use one embedding scorer to do both retrieval over the full entity set and final decision making. We argue that this coupling is a core bottleneck: global high-r...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [IoDResearch: Deep Research on Private Heterogeneous Data via the Internet of Data](http://arxiv.org/abs/2510.01553v3)
  来源：arXiv | 日期：2025-10-02 | 相关度：2.1 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：The rapid growth of multi-source, heterogeneous, and multimodal scientific data has increasingly exposed the limitations of traditional data management. Most existing DeepResearch (DR) efforts focus primarily on web sear...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SIMPLER: H&E-Informed Representation Learning for Structured Illumination Microscopy](http://arxiv.org/abs/2604.10334v2)
  来源：arXiv | 日期：2026-04-11 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Structured Illumination Microscopy (SIM) enables rapid, high-contrast optical sectioning of fresh tissue without staining or physical sectioning, making it promising for intraoperative and point-of-care diagnostics. Rece...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BridgeRAG: Training-Free Bridge-Conditioned Retrieval for Multi-Hop Question Answering](http://arxiv.org/abs/2604.03384v2)
  来源：arXiv | 日期：2026-04-03 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Multi-hop retrieval is not a single-step relevance problem: later-hop evidence should be ranked by its utility conditioned on retrieved bridge evidence, not by similarity to the original query alone. We present BridgeRAG...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration](http://arxiv.org/abs/2604.25080v1)
  来源：arXiv | 日期：2026-04-28 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：KV cache restoration has emerged as a dominant bottleneck in serving long-context LLM workloads, including multi-turn conversations, retrieval-augmented generation, and agentic pipelines. Existing approaches treat restor...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The Override Gap: A Magnitude Account of Knowledge Conflict Failure in Hypernetwork-Based Instant LLM Adaptation](http://arxiv.org/abs/2604.23750v1)
  来源：arXiv | 日期：2026-04-26 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Hypernetwork-based methods such as Doc-to-LoRA internalize a document into an LLM's weights in a single forward pass, but they fail systematically on conflicts: when the document contradicts pretraining knowledge, accura...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Can Current Agents Close the Discovery-to-Application Gap? A Case Study in Minecraft](http://arxiv.org/abs/2604.24697v1)
  来源：arXiv | 日期：2026-04-27 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Discovering causal regularities and applying them to build functional systems--the discovery-to-application loop--is a hallmark of general intelligence, yet evaluating this capacity has been hindered by the vast complexi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CoRaCMG: Contextual Retrieval-Augmented Framework for Commit Message Generation](http://arxiv.org/abs/2509.18337v3)
  来源：arXiv | 日期：2025-09-22 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Commit messages play a key role in documenting the intent behind code changes. However, they are often low-quality, vague, or incomplete, limiting their usefulness. Commit Message Generation (CMG) aims to automatically g...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MultiHedge: Adaptive Coordination via Retrieval-Augmented Control](http://arxiv.org/abs/2604.24905v1)
  来源：arXiv | 日期：2026-04-27 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Decision-making under changing conditions remains a fundamental challenge in many real-world systems. Existing approaches often fail to generalize across shifting regimes and exhibit unstable behavior under uncertainty. ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Faithfulness-QA: A Counterfactual Entity Substitution Dataset for Training Context-Faithful RAG Models](http://arxiv.org/abs/2604.25313v1)
  来源：arXiv | 日期：2026-04-28 | 相关度：0.7 | 新颖度：6.71
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) models frequently produce answers grounded in parametric memory rather than the retrieved context, undermining the core promise of retrieval augmentation. A fundamental obstacle to fi...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [AutoResearchBench: Benchmarking AI Agents on Complex Scientific Literature Discovery](http://arxiv.org/abs/2604.25256v1)
  来源：arXiv | 日期：2026-04-28 | 相关度：0.7 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：Autonomous scientific research is significantly advanced thanks to the development of AI agents. One key step in this process is finding the right scientific literature, whether to explore existing knowledge for a resear...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Navigating Global AI Regulation: A Multi-Jurisdictional Retrieval-Augmented Generation System](http://arxiv.org/abs/2604.25448v1)
  来源：arXiv | 日期：2026-04-28 | 相关度：0.7 | 新颖度：6.14
  匹配主题：未命中具体主题
  中文摘要：Navigating AI regulation across jurisdictions is increasingly difficult for policymakers, legal professionals, and researchers. To address this, we present a multi-jurisdictional Retrieval-Augmented Generation system for...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Reducing Redundancy in Retrieval-Augmented Generation through Chunk Filtering](http://arxiv.org/abs/2604.24334v1)
  来源：arXiv | 日期：2026-04-27 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Standard Retrieval-Augmented Generation (RAG) chunking methods often create excessive redundancy, increasing storage costs and slowing retrieval. This study explores chunk filtering strategies, such as semantic, topic-ba...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Designing DNA With Tunable Regulatory Activity Using Discrete Diffusion](https://www.biorxiv.org/content/10.1101/2024.05.23.595630v3)
  来源：bioRxiv | 日期：2026-04-27 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：设计具有可调且背景特异性活性的调控DNA是生物技术和医学的核心目标。本文提出了DNA离散扩散模型（D3），这是一种通过迭代核苷酸替换过程生成调控DNA序列的生成模型。在计算基准测试中，D3在生成调控序列方面优于匹配的扩散基准模型，其生成的序列在目标活性、活性分布及序列组成上与天然序列高度匹配。在K562细胞系的lentiMPRA（大规模平行报告基因检测）实验中，D3设计的序列保留了可测量的调控活性，且比基准模型更准确地重现了基因组调控序...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Geometric Theoretical Framework for Dynamic Protein Mutation Detection Models: Defect Awareness and Pathogenicity Prediction](https://www.biorxiv.org/content/10.64898/2026.04.22.720255v1)
  来源：bioRxiv | 日期：2026-04-26 | 相关度：4.6 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：传统蛋白质突变检测依赖静态单构象模型，忽略了构象柔性和动态演化，导致在柔性区域和变构位点出现系统性失效。本研究建立了一个定理驱动的几何代数框架，用于动态蛋白质突变建模。该框架从动态构象黎曼流形出发，通过算子值观测构建潜表示空间，并将代数约束放宽为可学习的近似李代数正则化。研究引入了利普希茨稳定的拓扑谱缺陷（TSD, δ_spec）指标，利用列维-奇维塔联络和热核渐近性量化静态表示与动态几何不变量之间的不一致性。在包含108个PDB结构及...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Scalable Agentic Reasoning for Designing Biologics Targeting Intrinsically Disordered Proteins](http://arxiv.org/abs/2512.15930v2)
  来源：arXiv | 日期：2025-12-17 | 相关度：2.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Intrinsically disordered proteins (IDPs) represent crucial therapeutic targets due to their significant role in disease -- approximately 80\% of cancer-related proteins contain long disordered regions -- but their lack o...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [TSAssistant: A Human-in-the-Loop Agentic Framework for Automated Target Safety Assessment](http://arxiv.org/abs/2604.23938v1)
  来源：arXiv | 日期：2026-04-27 | 相关度：2.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Target Safety Assessment (TSA) requires systematic integration of heterogeneous evidence, including genetic, transcriptomic, target homology, pharmacological, and clinical data, to evaluate potential safety liabilities o...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CORAL: Adaptive Retrieval Loop for Culturally-Aligned Multilingual RAG](http://arxiv.org/abs/2604.25676v1)
  来源：arXiv | 日期：2026-04-28 | 相关度：2.05 | 新颖度：7.33
  匹配主题：foundation_model_agent
  中文摘要：Multilingual retrieval-augmented generation (mRAG) is often implemented within a fixed retrieval space, typically via query or document translation or multilingual embedding vector representations. However, this approach...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CroSearch-R1: Better Leveraging Cross-lingual Knowledge for Retrieval-Augmented Generation](http://arxiv.org/abs/2604.25182v1)
  来源：arXiv | 日期：2026-04-28 | 相关度：2.05 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：A multilingual collection may contain useful knowledge in other languages to supplement and correct the facts in the original language for Retrieval-Augmented Generation (RAG). However, the vanilla approach that simply c...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AlphaFold's Bayesian Roots in Probability Kinematics](http://arxiv.org/abs/2505.19763v3)
  来源：arXiv | 日期：2025-05-26 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：The seminal breakthrough of AlphaFold in protein structure prediction relied on a learned potential energy function parameterized by deep models, in contrast to its successors AlphaFold2 and AlphaFold3, which lack an exp...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ComplianceNLP: Knowledge-Graph-Augmented RAG for Multi-Framework Regulatory Gap Detection](http://arxiv.org/abs/2604.23585v1)
  来源：arXiv | 日期：2026-04-26 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Financial institutions must track over 60,000 regulatory events annually, overwhelming manual compliance teams; the industry has paid over USD 300 billion in fines and settlements since the 2008 financial crisis. We pres...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Subarachnoid hemorrhage: epidemiology, risk factors, pathogenesis, and clinical therapies.](https://pubmed.ncbi.nlm.nih.gov/42043672/)
  来源：PubMed | 日期：2026-04-27 | 相关度：5.0 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：蛛网膜下腔出血（SAH）是一种致死率极高的脑血管急症，常导致严重的长期神经功能障碍。研究表明，SAH的发病率在不同地区和人群间存在显著差异，这由不可调控因素（如年龄、性别、家族史和遗传易感性）与可调控因素（如高血压、吸烟、药物使用和代谢紊乱）共同决定。血管生物学与基因组学的进展揭示，细胞外基质不稳定、内皮功能障碍、慢性炎症及特定遗传变异在动脉瘤形成与破裂中起关键作用。破裂后，SAH触发双相损伤级联反应：早期脑损伤（EBI）在数小时内发生...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Agentic clinical reasoning over longitudinal myeloma records: a retrospective evaluation against expert consensus](http://arxiv.org/abs/2604.24473v1)
  来源：arXiv | 日期：2026-04-27 | 相关度：2.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Multiple myeloma is managed through sequential lines of therapy over years to decades, with each decision depending on cumulative disease history distributed across dozens to hundreds of heterogeneous clinical documents....
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
