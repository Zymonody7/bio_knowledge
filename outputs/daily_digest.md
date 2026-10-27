# 每日论文监控日报 (2026-10-27)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 56 篇新论文。

## 抓取状态

- arXiv：成功，命中 46 篇
- PubMed：成功，命中 19 篇
- bioRxiv：成功，命中 12 篇
- medRxiv：成功，命中 11 篇

## 最值得看

### Foundation Model / Agent

- [OmicsLM: A Multimodal Large Language Model for Multi-Sample Omics Reasoning](http://arxiv.org/abs/2605.06728v2)
  来源：arXiv | 日期：2026-05-07 | 相关度：8.9 | 新颖度：6.7
  匹配主题：foundation_model_agent
  中文摘要：Large language models can reason over biological knowledge, but they are not naturally equipped to work with quantitative omics measurements. Existing approaches either convert expression profiles into long textual repre...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Benchmarking Ask Eolas-a medical AI tool for antimicrobial advice available in UK hospitals](https://www.medrxiv.org/content/10.64898/2026.10.22.26366212v1)
  来源：medRxiv | 日期：2026-10-26 | 相关度：7.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Selecting the most appropriate antimicrobial to treat an infection requires careful consideration of multiple streams of clinical information and is often supported by locally tailored guidelines. Recently, artificial in...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Scoring the NIH Stroke Scale from bedside exam transcripts: a synthetic benchmark of a decision model and a large language model](https://www.medrxiv.org/content/10.64898/2026.10.23.26366376v1)
  来源：medRxiv | 日期：2026-10-26 | 相关度：7.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Background. Clinicians score the NIH Stroke Scale (NIHSS) at the bedside, often under time pressure, and ambient AI tools that listen to clinical encounters are now entering practice. It is not known whether software can...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multimodal Requirements Traceability Link Recovery in Industrial Settings](http://arxiv.org/abs/2610.34503v1)
  来源：arXiv | 日期：2026-10-25 | 相关度：7.5 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Requirements traceability links support activities such as change-impact analysis, coverage checking, and validation. Industrial requirements can include traceable images, which text-only approaches cannot process direct...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Hypergraph-Enhanced Evidence Selection for Long-Context Multimodal Document QA](http://arxiv.org/abs/2610.35542v1)
  来源：arXiv | 日期：2026-10-26 | 相关度：6.8 | 新颖度：7.45
  匹配主题：foundation_model_agent
  中文摘要：Long-context multimodal document question answering (QA) has become an important yet challenging task for modern vision-language models (VLMs), as it requires reasoning over evidence dispersed across pages and modalities...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [BERAG: Bayesian Ensemble Retrieval-Augmented Generation for Knowledge-based Visual Question Answering](http://arxiv.org/abs/2604.22678v2)
  来源：arXiv | 日期：2026-04-24 | 相关度：7.9 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：A common approach to question answering with retrieval-augmented generation (RAG) is to concatenate documents into a single context and pass it to a language model to generate an answer. While simple, this strategy can o...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [Learning to Remember: Advances in Memory Mechanisms for Large Language Models](http://arxiv.org/abs/2610.35089v1)
  来源：arXiv | 日期：2026-10-26 | 相关度：6.8 | 新颖度：6.55
  匹配主题：foundation_model_agent
  中文摘要：Memory has become a central mechanism for extending large language models (LLMs) beyond fixed context windows, stateless interaction, and static parametric knowledge. This survey organizes the literature around three com...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Autonomous Structural Discovery Of Bioprocess Dynamics And Kinetics Via LLM-Driven Agents](http://arxiv.org/abs/2610.35391v1)
  来源：arXiv | 日期：2026-10-26 | 相关度：6.55 | 新颖度：7.16
  匹配主题：foundation_model_agent
  中文摘要：High-fidelity digital twins in continuous biomanufacturing are often bottlenecked by incomplete kinetic models, while standard data-driven algorithms (e.g., SINDy, PINNs) lack interpretability or impose rigid physical as...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LatentRAG: Latent Reasoning and Retrieval for Efficient Agentic RAG](http://arxiv.org/abs/2605.06285v2)
  来源：arXiv | 日期：2026-05-07 | 相关度：6.55 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：Single-step retrieval-augmented generation (RAG) provides an efficient way to incorporate external information for simple question answering tasks but struggles with complex questions. Agentic RAG extends this paradigm b...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Geometric Gain Graph: Zero-Token Graph Construction for Multi-Hop RAG](http://arxiv.org/abs/2609.19622v2)
  来源：arXiv | 日期：2026-09-17 | 相关度：6.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Existing Retrieval-Augmented Generation (RAG) systems struggle with multi-hop reasoning due to a fundamental inability to balance relevance and novelty. Traditional dense retrievers are constrained by surface-level match...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Large Language Models: A Plain-Language Overview for Engineers](http://arxiv.org/abs/2610.34585v1)
  来源：arXiv | 日期：2026-10-25 | 相关度：6.55 | 新颖度：6.2
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are neural networks trained on huge text collections to generate text by predicting what comes next. Engineers using ChatGPT and other generative artificial intelligence (AI) tools need a cle...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Data Governance for Generative and Agentic AI : Technology, Law, Economics, and Security](http://arxiv.org/abs/2610.33605v1)
  来源：arXiv | 日期：2026-10-24 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：This book develops a unified governance framework for systems that retrieve, generate, infer, remember and act on information from large language models and retrieval augmented pipelines to autonomous multi agent systems...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Towards Explainable Industrial Anomaly Detection via Knowledge-Guided Latent Reasoning](http://arxiv.org/abs/2602.09850v4)
  来源：arXiv | 日期：2026-02-10 | 相关度：6.1 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Industrial anomaly detection demands precise reasoning over fine-grained defect patterns. However, existing multimodal large language models (MLLMs), pretrained on general-domain data, often struggle to capture category-...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [UniGFM-RAG: Unify Graph Foundation Models and Large Language Models for End-to-End Retrieval and Reasoning](http://arxiv.org/abs/2610.34866v1)
  来源：arXiv | 日期：2026-10-26 | 相关度：5.45 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have shown remarkable capabilities across tasks, but they still struggle with complex reasoning that requires integrating scattered knowledge. Graph Retrieval-Augmented Generation (GraphRAG) ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Think Parallax: Solving Multi-Hop Problems via Multi-View Knowledge-Graph-Based Retrieval-Augmented Generation](http://arxiv.org/abs/2510.15552v5)
  来源：arXiv | 日期：2025-10-17 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) still struggle with multi-hop reasoning over knowledge-graphs (KGs), and we identify a previously overlooked structural reason for this difficulty: Transformer attention heads naturally speci...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [In-silico Tandem Mass Spectral Libraries for the Blood Exposome and Metabolomics Workbench Databases: Application of Gemini Large Language Model](https://www.biorxiv.org/content/10.64898/2026.10.20.760278v1)
  来源：bioRxiv | 日期：2026-10-25 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Human body contains endogenous metabolites, nutrients and xenobiotics chemicals. These chemicals can be detected in a biospecimen using high-resolution mass spectrometry instruments, yielding metabolomic and exposomic da...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Factual Yet One-Sided: Stance Poisoning and Evidence Balancing in Retrieval-Augmented Generation](http://arxiv.org/abs/2610.34294v1)
  来源：arXiv | 日期：2026-10-25 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：The stance expressed in responses from retrieval-augmented generation systems is significantly influenced by the stance distribution of the retrieved materials. Existing research on knowledge poisoning has primarily targ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Benchmarking LLM-based Information Extraction Tools for Medical Documents](https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v2)
  来源：medRxiv | 日期：2026-10-26 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Background: Medical documents are a crucial resource for medical research around the world. While troves of valuable health data exist, they are largely computationally inaccessible as hard copies of unstructured text. M...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Adaptive Retrieval, Selective Answers: Evaluating Conformal Factuality in Agentic RAG](http://arxiv.org/abs/2610.34872v1)
  来源：arXiv | 日期：2026-10-26 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) can improve factual grounding without guaranteeing that every generated claim is supported. Previous work has studied claim-level conformal factuality in single-stage RAG and, more re...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Building from the ground up: augmentation strategies to improve protein language model performance on protein sets](https://www.biorxiv.org/content/10.64898/2026.10.20.760553v1)
  来源：bioRxiv | 日期：2026-10-25 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：An important underlying requirement for deep learning models is the availability of large datasets, however, in sciences such as chemistry and biology, generating experimental data of sufficient size represents a signifi...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [GuardRAG: A Post-Retrieval Defense against Poisoning Attacks in Retrieval-Augmented Generation](http://arxiv.org/abs/2610.35071v1)
  来源：arXiv | 日期：2026-10-26 | 相关度：4.75 | 新颖度：6.27
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) enhances the factual grounding of Large Language Models (LLMs) by incorporating external evidence, but also exposes them to corpus poisoning attacks. In particular, coordinated attack...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [A Domain-Aware Pipeline for Structured Extraction and Retrieval-Augmented Question Answering over arXiv Superconductivity Literature](http://arxiv.org/abs/2610.34391v1)
  来源：arXiv | 日期：2026-10-25 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Scientific literature in materials physics is growing faster than researchers can manually inspect it, yet most retrieval tools rely on keyword matching or generic question answering that ignores domain-specific structur...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [ArchiveLens: A Generative Spatial Knowledge Framework for Semantic Reconstruction of Historical Maps](http://arxiv.org/abs/2610.35606v1)
  来源：arXiv | 日期：2026-10-26 | 相关度：6.15 | 新颖度：7.3
  匹配主题：foundation_model_agent
  中文摘要：Historical maps contain dense morphological and semantic information about past urban environments, but many digitization workflows focus primarily on extracting geometry, and do not capture cartographic semantics such a...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [TriageRAG: Failure-Aware Self-Training for Adapting Retrieval-Augmented Language Models to Specialized Domains](http://arxiv.org/abs/2610.33776v1)
  来源：arXiv | 日期：2026-10-24 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) lets large language models (LLMs) answer knowledge-intensive questions from retrieved evidence, but adapting a general-purpose RAG system to a specialized domain such as medicine is d...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Genotypic Triggers: Exposing Pharmacogenomic Blind Spots via Host-Specific Backdoors in Generative Antimicrobial Peptide Models](http://arxiv.org/abs/2608.06779v2)
  来源：arXiv | 日期：2026-08-07 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have accelerated drug discovery, particularly in the automated design of antimicrobial peptides (AMPs). However, current validation pipelines for peptide generation models overlook historical...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Agent K: An Agent-Orchestrated Pipeline for Mapping Genes to Biosynthetic Pathway towards Metabolite Discovery](https://www.biorxiv.org/content/10.64898/2026.10.19.760272v1)
  来源：bioRxiv | 日期：2026-10-24 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：The identification of biosynthetic gene clusters (BGCs) and their associated metabolic path- ways is central to genome-guided natural product discovery. However, existing computational tools depend on fragmented workflow...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Beyond Being Accurate: Implications for Using Natural Language Descriptions for Accessible 3D Modeling with~Blind and Low Vision Makers](http://arxiv.org/abs/2610.35562v1)
  来源：arXiv | 日期：2026-10-26 | 相关度：5.45 | 新颖度：7.48
  匹配主题：foundation_model_agent
  中文摘要：People who are blind or have low vision (BLV) are largely excluded from 3D modeling tools that rely on visual representations of geometry. Natural language descriptions offer a potential path to accessibility, but it is ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Hallucination-Aware Multi-Agent RAG via Internal Attention Rewards](http://arxiv.org/abs/2610.35056v1)
  来源：arXiv | 日期：2026-10-26 | 相关度：5.45 | 新颖度：6.48
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) grounds language models in retrieved evidence, but its outputs often contain claims unsupported by that evidence. Recent multi-agent RAG systems decompose the pipeline into cooperativ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Trust Mechanisms for Offline Generative AI at the Edge: A Connectivity-Regime Framework and an Empirical Study on a Raspberry Pi 5](http://arxiv.org/abs/2610.33732v1)
  来源：arXiv | 日期：2026-10-24 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Generative AI and large language models (LLMs) are moving into the Internet of Things, yet most deployments assume cloud connectivity, and many IoT settings have intermittent, restricted, or no connectivity. We propose a...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CalibraRL: Confidence-Calibrated Reinforcement Learning for Mitigating Hallucinations in RAG](http://arxiv.org/abs/2610.35142v1)
  来源：arXiv | 日期：2026-10-26 | 相关度：4.75 | 新颖度：6.42
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) often produce plausible but incorrect answers, motivating reinforcement learning methods that reward correct answers, penalize incorrect answers, and allow abstention. However, fixed outcome-...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SpecAgent: Empowering Program Verification with Agentic Synthesis of Formal Program Specifications](http://arxiv.org/abs/2610.05132v2)
  来源：arXiv | 日期：2026-10-04 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Formal specifications are essential for deductive program verification, providing semantic abstractions for compositional verification of complex software. However, manually constructing specifications is labor-intensive...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Identifying cohorts at elevated risk of cancers using generative modeling of patient health states](https://www.medrxiv.org/content/10.64898/2026.09.09.26362676v4)
  来源：medRxiv | 日期：2026-10-24 | 相关度：7.8 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：While large language models are powerful generators of new text, forecasting disease progression from longitudinal health histories remains a challenging problem. We introduce GenEHR, an autoregressive generative model t...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Bern Sleep-Wake Registry: temporal extraction of comorbidities from unstructured clinical text using a large language model](https://www.medrxiv.org/content/10.64898/2026.10.25.26364496v1)
  来源：medRxiv | 日期：2026-10-26 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Introduction Large language models (LLMs) may enable the extraction of clinically relevant information from unstructured electronic health records, but most previous work focused on identifying diagnoses without preservi...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Simulating Psychotherapeutic Sessions with Generative Artificial Intelligence: A Proof-of-Concept Study of In Silico Psychotherapy Research](https://www.medrxiv.org/content/10.64898/2026.10.22.26366245v1)
  来源：medRxiv | 日期：2026-10-26 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Background: Across biomedicine, in silico models increasingly complement in vivo and in vitro research. Psychotherapy science, however, remains constrained by methodological limitations, resource-intensive trials, challe...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Language models annotate mass cytometry clusters within the range where human experts disagree](https://www.biorxiv.org/content/10.64898/2026.10.20.760379v1)
  来源：bioRxiv | 日期：2026-10-24 | 相关度：5.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Cell-type identification of clusters from unsupervised cytometry pipelines (e.g. FlowSOM, GigaSOM) is a time-consuming, expert-dependent bottleneck, typically requiring an expert to read a heatmap of median marker intens...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Can System-1-Style Decision Models Replace Dedicated Rerankers in RAG? A Systems Evaluation](http://arxiv.org/abs/2610.34816v1)
  来源：arXiv | 日期：2026-10-26 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) systems often use a dedicated reranker to choose which retrieved candidates reach the language model. Reranking improves relevance but adds latency, so teams look for faster alternati...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [Offline Language-Based Support System for Tactical Decision-Making in Air Combat Operations](http://arxiv.org/abs/2610.35635v1)
  来源：arXiv | 日期：2026-10-26 | 相关度：4.75 | 新颖度：6.84
  匹配主题：foundation_model_agent
  中文摘要：An offline language-based support tool is presented to assist pilot training and tactical decision-making in air combat operations. The system, named MATE (Mission Assistant for Training and Evaluation), applies retrieva...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Automated Standardization of Legacy Biomedical Metadata Using an Ontology-Constrained LLM Agent](http://arxiv.org/abs/2604.08552v5)
  来源：arXiv | 日期：2026-03-10 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Descriptive scientific metadata in public repositories are often incomplete and inconsistent with community standards and ontologies, limiting data FAIRness. Large language models (LLM) offer a promising approach to auto...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RAGing Against Misogyny: Improving Implicit Misogyny Explanations](http://arxiv.org/abs/2610.35094v1)
  来源：arXiv | 日期：2026-10-26 | 相关度：2.75 | 新颖度：6.56
  匹配主题：foundation_model_agent
  中文摘要：Implicit misogyny often requires background knowledge to be understood. To address this challenge, we propose a Retrieval-Augmented Generation (RAG) framework for detecting and explaining implicit misogyny in English and...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Rethinking Scientific Discovery in the Agentic Era](http://arxiv.org/abs/2607.03863v3)
  来源：arXiv | 日期：2026-07-04 | 相关度：2.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Artificial intelligence has advanced scientific discovery, but most AI4Science systems remain fragmented tools that rely on humans to coordinate problem formulation, literature grounding, model use, simulation, validatio...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ECHOES: An Adaptive LLM-Powered AR Glasses Docent for Evidence-Grounded Urban Heritage Interpretation](http://arxiv.org/abs/2610.34865v1)
  来源：arXiv | 日期：2026-10-26 | 相关度：2.05 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Urban heritage tours are often delivered through fixed scripts, leaving limited room for visitors' situated questions, language preferences, or requests for evidence. We present ECHOES, an adaptive LLM-powered AR glasses...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Read the Route: Attention-Steered Hypergraph Retrieval for Multi-hop RAG](http://arxiv.org/abs/2610.35412v1)
  来源：arXiv | 日期：2026-10-26 | 相关度：1.4 | 新颖度：6.7
  匹配主题：未命中具体主题
  中文摘要：Graph-based retrieval-augmented generation (GraphRAG) answers multi-hop questions by organizing a corpus into a graph and retrieving along its structure. Existing retrieval methods face two limitations. Diffusion- and si...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Firefly: Illuminating Large-Scale Verified Tool-Call Data Generation from Real APIs](http://arxiv.org/abs/2605.17558v2)
  来源：arXiv | 日期：2026-05-17 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Training tool-calling agents requires large-scale trajectory data with verifiable labels, yet existing approaches either synthesize environments that diverge from real API behavior or generate tasks without ground-truth ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Novel or Not? PatEx-Gym: Agentic Prior-Art Search for Novelty Assessment in Patent Examination](http://arxiv.org/abs/2610.33503v1)
  来源：arXiv | 日期：2026-10-24 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Patent examination is a challenging real-world task that requires agents to discover sparse prior art, iteratively refine queries, inspect technical evidence, and produce novelty assessments documented in Office Actions ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [DISCERN: Can AI Agents Work Like Scientists and Guide Discovery?](http://arxiv.org/abs/2609.33357v2)
  来源：arXiv | 日期：2026-09-27 | 相关度：0.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Reliable automated research requires agents to vet data, verify analyses, and generate hypotheses grounded in trustworthy evidence, potentially reducing routine scientific workload while allowing scientists to focus on i...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Ranking Is Not Deciding: Benchmark Shortcuts and Operating-Point Collapse in Query-Time RAG Poisoning Defenses](http://arxiv.org/abs/2610.33849v1)
  来源：arXiv | 日期：2026-10-24 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Query-time filters that screen each retrieved document before it reaches the generator are the dominant published defense against retrieval-augmented generation poisoning, and they report near-perfect detection on domain...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Topic-Level Fairness in Retrieval-Augmented Generation](http://arxiv.org/abs/2610.34683v1)
  来源：arXiv | 日期：2026-10-26 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Group fairness in retrieval-augmented generation (RAG) systems is typically evaluated using metrics aggregated across queries. However, such metrics can conceal topic-level disparities: a system may favor women on questi...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [HerHealthGPT: An Evidence-Grounded Conversational AI System for Women's Reproductive Health Copy title](http://arxiv.org/abs/2610.33931v1)
  来源：arXiv | 日期：2026-10-24 | 相关度：3.1 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要："Why is my period late?" Sometimes, the most useful response begins with another question. Yet conversational AI systems may respond to incomplete health queries without seeking essential context or grounding their guida...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Closing the empirical loop: autonomous AI agents conduct end-to-end research with human participants](http://arxiv.org/abs/2508.13421v3)
  来源：arXiv | 日期：2025-08-19 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Artificial intelligence systems are transforming scientific discovery by accelerating specific research tasks, from protein structure prediction to materials design, yet remain confined to narrow domains requiring substa...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Proteogenomics captures a midlife biological state of Alzheimer's disease susceptibility](https://www.medrxiv.org/content/10.64898/2026.10.22.26366029v1)
  来源：medRxiv | 日期：2026-10-26 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Alzheimer's disease (AD) develops over decades, but biological processes underlying susceptibility during midlife remain poorly understood. Using multimodal neuroimaging and plasma proteomics in UK Biobank participants, ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A clinically annotated proteomic and histological resource of 1,000 colorectal cancers](https://www.biorxiv.org/content/10.64898/2026.10.20.757714v2)
  来源：bioRxiv | 日期：2026-10-24 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Colorectal cancer (CRC) is heterogeneous, yet current classifications capture this heterogeneity only in part. Here we present a multimodal resource of 1,000 treatment-naive CRC cases, the largest proteomically profiled ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Precision medicine approaches in diabetic cardiomyopathy: from molecular mechanisms to personalized therapeutic strategies.](https://pubmed.ncbi.nlm.nih.gov/42925888/)
  来源：PubMed | 日期：2026-10-24 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Diabetic cardiomyopathy (DCM) is a distinct myocardial disease defined by the existence of abnormal myocardial structure and performance in diabetes mellitus patients without hypertension and coronary artery disease. DCM...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Reading Beyond OCR Noise: Robust Cross-Lingual RAG for Legislative Archives](http://arxiv.org/abs/2610.35240v1)
  来源：arXiv | 日期：2026-10-26 | 相关度：0.7 | 新颖度：6.12
  匹配主题：未命中具体主题
  中文摘要：India's historical public archives present severe computer vision and document image analysis challenges: decades of parliamentary records survive only as degraded, multi-column scanned pages featuring mixed scripts, com...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Logic Hijacking of RAG: Single-Document Poisoning via Local Optimization](http://arxiv.org/abs/2610.34829v1)
  来源：arXiv | 日期：2026-10-26 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Single-document corpus poisoning under black-box access poses a severe threat to Retrieval-Augmented Generation (RAG). However, existing attacks predominantly rely on explicit factual refutations or imperative instructio...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Software Engineering for AI-Driven Science](http://arxiv.org/abs/2610.34573v1)
  来源：arXiv | 日期：2026-10-25 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：AI has made significant contributions to scientific discovery. Autonomous agents can now independently analyse complex problems, design experiments, write and execute code, analyse findings, and derive scientific conclus...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 其他

- [Agents for Experiments, Experiments for Agents: A Design Grammar for AI-Enabled Experimental Science](http://arxiv.org/abs/2605.17746v2)
  来源：arXiv | 日期：2026-05-18 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Human-AI experiments vary who receives information, who can act, and who holds decision authority. Precise descriptions of individual studies do not by themselves provide a common language for comparing these arrangement...
  为什么值得看：Agents for Experiments, Experiments for  与你的主题有弱匹配，暂时保留作低优先级跟踪。
