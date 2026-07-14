# 每日论文监控日报 (2026-07-14)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 49 篇新论文。

## 抓取状态

- arXiv：成功，命中 34 篇
- PubMed：成功，命中 30 篇
- bioRxiv：成功，命中 21 篇
- medRxiv：成功，命中 7 篇

## 最值得看

### Foundation Model / Agent

- [A geometric atlas of how ESM3 organizes modalities across depth](https://www.biorxiv.org/content/10.64898/2026.07.08.737319v1)
  来源：bioRxiv | 日期：2026-07-12 | 相关度：8.5 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Protein language models learn general-purpose representations from large collections of protein sequences and structures, and have advanced the prediction of protein structure and function. ESM3 is a multimodal protein l...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A retrospective study of a Chinese vision-language large model for emergency 3D brain CT interpretation](https://www.medrxiv.org/content/10.64898/2026.07.11.26357421v1)
  来源：medRxiv | 日期：2026-07-13 | 相关度：8.5 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Emergency brain computed tomography (CT) is the first line imaging modality for patients with acute neurological symptoms and trauma, where delayed or incomplete recognition of critical findings can directly compromise c...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AeroRAG: Structured Multimodal Retrieval-Augmented LLM for Fine-Grained Aerial Visual Reasoning](http://arxiv.org/abs/2604.17889v2)
  来源：arXiv | 日期：2026-04-20 | 相关度：7.9 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：Despite recent progress in multimodal large language models (MLLMs), reliable visual question answering in aerial scenes remains challenging. In such scenes, task-critical evidence is often carried by small objects, expl...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [FHIRTrustBench: A Benchmark for Interoperability-Driven Clinical AI Readiness and Trustworthiness](https://www.medrxiv.org/content/10.64898/2026.07.08.26357574v1)
  来源：medRxiv | 日期：2026-07-13 | 相关度：7.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Existing evaluations of healthcare AI often treat interoperability as a technical infrastructure issue rather than a factor that directly influences the safety and reliability of clinical AI systems. Yet the quality of F...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Metagenomic contextualization of proteins with state space models](https://www.biorxiv.org/content/10.64898/2026.07.07.736993v1)
  来源：bioRxiv | 日期：2026-07-11 | 相关度：7.45 | 新颖度：6.5
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：Since the early adoption of metagenomics (the culture-free sequencing of microbial community genomes) in 2011, sequence data has increased over 500-fold across ecosystems. This surge in data has outpaced reliable taxonom...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [ProtBLIP2-SST: Protein Function Prediction via BLIP2 with Sequence, Structure, and Text](https://www.biorxiv.org/content/10.64898/2026.07.10.737551v1)
  来源：bioRxiv | 日期：2026-07-12 | 相关度：7.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Protein function prediction traditionally relies on structured gene ontology (GO) labels or multi-label classifiers. However, these labels or classifiers cannot flexibly describe molecular function, biological process, c...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [GeoPep: A Geometry-Aware Masked Language Model for Protein-Peptide Binding Site Prediction.](https://pubmed.ncbi.nlm.nih.gov/42367058/)
  来源：PubMed | 日期：2026-07-13 | 相关度：10.0 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Multimodal approaches that integrate protein structure and sequence have achieved remarkable success in protein-protein interface prediction. However, extending these methods to protein-peptide interactions remains chall...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Hindsight to Foresight: Self-Encouraged Hindsight Distillation for Knowledge-based Visual Question Answering](http://arxiv.org/abs/2511.11132v3)
  来源：arXiv | 日期：2025-11-14 | 相关度：7.5 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Knowledge-based Visual Question Answering (KBVQA) necessitates external knowledge incorporation beyond cross-modal understanding. Existing KBVQA methods either utilize implicit knowledge in multimodal large language mode...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MG$^2$-RAG: Multi-Granularity Graph for Multimodal Retrieval-Augmented Generation](http://arxiv.org/abs/2604.04969v2)
  来源：arXiv | 日期：2026-04-04 | 相关度：6.8 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) mitigates hallucinations in Multimodal Large Language Models (MLLMs), yet existing systems struggle with complex cross-modal reasoning. Flat vector retrieval often ignores structural ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Cost and Accuracy of Long-Term Memory in Distributed Multi-Agent Systems Based on Large Language Models](http://arxiv.org/abs/2601.07978v4)
  来源：arXiv | 日期：2026-01-12 | 相关度：6.55 | 新颖度：6.7
  匹配主题：foundation_model_agent
  中文摘要：Long-term memory (LTM) is fundamental to large language model (LLM)-based agents in the emerging Internet of Agents (IoA), where distributed multi-agent systems (DMAS) span cloud and edge networks. Existing evaluations a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Multi-Agent Framework for Zero-Dimensional Reduced-Order Model Planning](http://arxiv.org/abs/2607.10994v1)
  来源：arXiv | 日期：2026-07-13 | 相关度：6.55 | 新颖度：6.7
  匹配主题：foundation_model_agent
  中文摘要：Zero-dimensional reduced-order models (0D ROMs) are central to multi-dimensional design workflows for high-end complex equipment. However, the planning process currently relies on manual expertise, limiting topological e...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Demographic Prompting at Scale: When More Attributes Hurt LLM--Human Agreement](http://arxiv.org/abs/2607.10590v1)
  来源：arXiv | 日期：2026-07-12 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：We investigate how annotator demographic attributes, supplied as prompt cues, shape the alignment between large language model (LLM) predictions and human annotations across five tasks. Using five open-source LLMs, we sy...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [How Temperature Shapes Ideological Discourse in Retrieval-Augmented Generation?](http://arxiv.org/abs/2607.11783v1)
  来源：arXiv | 日期：2026-07-13 | 相关度：5.45 | 新颖度：7.57
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) has been increasingly adopted to reduce hallucinations and strengthen the factual grounding of large language models (LLMs). While robustness to errors in the retrieval process has be...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ARSENAL: Learning Transferable Regulatory DNA Representations with Targeted Short-Context Language Models](https://www.biorxiv.org/content/10.64898/2026.02.05.703637v3)
  来源：bioRxiv | 日期：2026-07-12 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：DNA language models (DNALMs) aim to learn representations of genomic sequence for variant interpretation, regulatory prediction, and sequence design. Most DNALMs are trained on whole genomes and long contexts, but regula...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TENET: One Step Toward Test-Driven Development for Repository-Level Code Generation](http://arxiv.org/abs/2509.24148v3)
  来源：arXiv | 日期：2025-09-29 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Test-Driven Development (TDD) is a widely adopted practice that requires developers to create and execute tests alongside implementation. With recent advances in Large Language Models (LLMs), developers can shift from ma...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RAGU: A Multi-Step GraphRAG Engine with a Compact Domain-Adapted LLM](http://arxiv.org/abs/2607.11683v1)
  来源：arXiv | 日期：2026-07-13 | 相关度：4.75 | 新颖度：7.11
  匹配主题：foundation_model_agent
  中文摘要：Graph retrieval-augmented generation (GraphRAG) enhances large language models with structured knowledge, yet existing systems construct knowledge graphs in a single extraction pass, producing noisy entities and brittle ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [GRASP: GRanularity-Aware Search Policy for Agentic RAG](http://arxiv.org/abs/2607.10463v1)
  来源：arXiv | 日期：2026-07-11 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Agentic retrieval-augmented generation (RAG) extends static RAG by allowing language models to iteratively reason, generate search queries, retrieve evidence, and predict answers. However, it remains challenging for mode...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AI Research Agents Narrow Scientific Exploration](http://arxiv.org/abs/2605.27905v2)
  来源：arXiv | 日期：2026-05-27 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：AI research agents now support large-scale AI-assisted scientific discovery. We examine whether AI-generated ideas broaden scientific exploration or primarily reinforce existing work. Using five agent frameworks and five...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The Next Paradigm in Medical AI: A Survey of Agentic AI in Biomedicine.](https://pubmed.ncbi.nlm.nih.gov/42441446/)
  来源：PubMed | 日期：2026-07-13 | 相关度：3.75 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Biomedical AI is increasingly shaped by policy-bound, multi-step clinical workflows and non-stationary, multimodal data and tools. In this setting, the field is moving beyond static predictors toward agentic systems, ena...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [FAIR GraphRAG: A Retrieval-Augmented Generation Approach for Semantic Data Analysis](http://arxiv.org/abs/2607.11464v1)
  来源：arXiv | 日期：2026-07-13 | 相关度：5.75 | 新颖度：7.09
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) addresses the limitations of Large Language Models (LLMs) when providing responses to domain-specific questions. Graph-based RAG approaches, such as GraphRAG, enhance retrieval by cap...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Board-Level Performance of Leading Open-Weight Vision-Language Models on the Japanese Diagnostic Radiology Board Examination: Reasoning, Image-Input, and Language Effects](https://www.medrxiv.org/content/10.64898/2026.07.09.26357709v1)
  来源：medRxiv | 日期：2026-07-13 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Purpose: To evaluate the latest open-weight vision-language models (VLMs) on the Japanese Diagnostic Radiology Board Examination (JDRBE), assessing overall accuracy and the effects of image input, reasoning, and language...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Interpretable variant effect prediction from genomic foundation model embeddings](https://www.biorxiv.org/content/10.64898/2026.04.10.717844v4)
  来源：bioRxiv | 日期：2026-07-11 | 相关度：8.35 | 新颖度：1.0
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Scientific foundation models learn high-dimensional representations from diverse data modalities, yet what they encode and how to extract that knowledge remain open questions. Here we show that probing the internal repre...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AGPI: An AI-Powered Genomic Pathogen Intelligence Platform for Integrated Classification, Visualization, and Therapeutic Targeting](https://www.biorxiv.org/content/10.64898/2026.07.07.737037v1)
  来源：bioRxiv | 日期：2026-07-11 | 相关度：7.5 | 新颖度：5.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Rapid and accurate pathogen detection remains a major challenge in modern bioinformatics, as existing tools are often fragmented and require multiple specialized workflows. We present AGPI (AI-powered Genomic Pathogen In...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [OCellus: A Language-Model Framework for Single-Cell, Spatial, and Perturbation Biology with Natural-Language Reasoning](https://www.biorxiv.org/content/10.64898/2026.07.08.737248v1)
  来源：bioRxiv | 日期：2026-07-12 | 相关度：5.75 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Computational modeling of cellular behavior - the virtual cell - has emerged as a stated grand challenge at the intersection of artificial intelligence and biology, yet existing foundation models remain specialized: sing...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ProtAug: An Empirical Investigation of pLM-Guided Data Augmentation for Protein Sequence Prediction Tasks](https://www.biorxiv.org/content/10.64898/2026.07.10.737545v1)
  来源：bioRxiv | 日期：2026-07-11 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Protein language models (pLMs) offer great potential for protein sequence analysis, yet the scarcity of labeled data often limits their effectiveness in fine-tuning. Data augmentation is a promising remedy, but systemati...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [General-Purpose vs. Domain-Specific Large Language Models in Antibiotic Clinical Decision-Making: A Double-Blind Evaluation with a 2X2 Factorial Design](https://www.medrxiv.org/content/10.64898/2026.07.11.26357814v1)
  来源：medRxiv | 日期：2026-07-13 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Background: Antimicrobial resistance poses a major threat to global public health. Large language models (LLMs) offer new possibilities for optimizing antibiotic prescribing decisions, but the capabilities of general-pur...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [HiQA: A Hierarchical Contextual Augmentation RAG for Multi-Documents QA](http://arxiv.org/abs/2402.01767v3)
  来源：arXiv | 日期：2024-02-01 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) has rapidly advanced the language model field, particularly in question-answering (QA) systems. By integrating external documents during the response generation phase, RAG significant...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SVD-RAG: Efficient Tree-Organized Retrieval-Augmented Generation via Singular Value Decomposition](http://arxiv.org/abs/2607.10316v1)
  来源：arXiv | 日期：2026-07-11 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) systems enhance large language models by retrieving relevant documents from external knowledge bases. Recent work by Sarthi et al. (2024) introduced RAPTOR, which organizes documents ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [FedMosaic: Federated Retrieval-Augmented Generation via Parametric Adapters](http://arxiv.org/abs/2602.05235v2)
  来源：arXiv | 日期：2026-02-05 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) enhances Large Language Models (LLMs) by grounding generation in external knowledge to improve factuality and reduce hallucinations. Yet most deployments assume a centralized corpus, ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [NGM-RAG: Neural Graph Matching based Retrieval-Augmented Generation](http://arxiv.org/abs/2607.11159v1)
  来源：arXiv | 日期：2026-07-13 | 相关度：4.75 | 新颖度：5.69
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) significantly enhances the ability of Large Language Models (LLMs) to provide accurate and contextually relevant answers by dynamically integrating external databases. However, tradit...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [EvidentialRAG: Quantifying and Mitigating Information Conflict in Multi-Source Retrieval-Augmented Generation via Evidential Deep Learning](http://arxiv.org/abs/2607.10491v1)
  来源：arXiv | 日期：2026-07-11 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation grounds large language models in external evidence, but most pipelines still treat retrieved passages as deterministic and mutually consistent context. In open information environments, ret...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Fine-Tuned Large Language Models for Detecting Social Isolation from Unstructured Clinical Notes](https://www.medrxiv.org/content/10.64898/2026.07.05.26357334v2)
  来源：medRxiv | 日期：2026-07-13 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Objective: To identify instances of social isolation and social support within unstructured clinical notes by leveraging fine-tuned FLAN-T5-Large, BERT, RoBERTa, and Gemma-2-2B models. Materials and Methods: The study us...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [A scoping review on emerging biomarkers in inflammatory bowel disease: Towards precision medicine in diagnosis and therapeutic management.](https://pubmed.ncbi.nlm.nih.gov/42441552/)
  来源：PubMed | 日期：2026-01-01 | 相关度：6.15 | 新颖度：5.25
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：Inflammatory Bowel Diseases (IBD) are chronic conditions presenting significant diagnostic and management challenges. Current invasive methods and traditional biomarkers often lack sufficient accuracy and fail to address...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Language Model Embedding Classifiers Enable Identification of Multiple Sclerosis-Associated BCRs and Repertoires](https://www.biorxiv.org/content/10.64898/2026.07.07.735316v1)
  来源：bioRxiv | 日期：2026-07-13 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Multiple sclerosis (MS) is a chronic inflammatory demyelinating disease. It affects over 2 million people worldwide but has historically been challenging to diagnose, categorize, and treat. MS has an autoimmune component...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [NiCLIP: Neuroimaging contrastive language-image pretraining model for predicting text from brain activation images](https://www.biorxiv.org/content/10.1101/2025.06.14.659706v4)
  来源：bioRxiv | 日期：2026-07-11 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Predicting cognitive processes from brain activation maps has remained an open question within the neuroscience community for many years. Meta-analytic functional decoding methods aim to tackle this issue by providing a ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [UNIBROWSE: A Data-to-Agent Framework for Multimodal BrowseComp](http://arxiv.org/abs/2607.10557v1)
  来源：arXiv | 日期：2026-07-12 | 相关度：2.75 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Multimodal BrowseComp 任务要求智能体在动态网页内容上结合感知、工具调用和长程推理，这对处理组合结构、开放世界不确定性及跨长程交互的多模态整合提出了挑战。现有的数据构建方法仅涵盖纯文本和“图生文”模式，忽略了“文生图”模式，限制了智能体的通用性。本研究提出 UNIBROWSE，这是一个统一的数据流水线，首次同时生成涵盖上述三种模式的训练数据。该流水线通过实时网页检索增强知识图谱以提升保真度，并引入“探索度”指标过滤低...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [NVAITC AI Scientist: A Governed End-to-End Research System -- A Hypertension GWAS Case Study](http://arxiv.org/abs/2607.11084v1)
  来源：arXiv | 日期：2026-07-13 | 相关度：2.75 | 新颖度：5.62
  匹配主题：foundation_model_agent
  中文摘要：Agentic research systems are emerging as a new paradigm for coordinating scientific workflows beyond isolated model inference, code generation, or statistical analysis. However, deployment in institutional biomedical env...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CRINN: Contrastive Reinforcement Learning for Approximate Nearest Neighbor Search](http://arxiv.org/abs/2508.02091v3)
  来源：arXiv | 日期：2025-08-04 | 相关度：2.1 | 新颖度：6.75
  匹配主题：未命中具体主题
  中文摘要：近似最近邻搜索（ANNS）算法在检索增强生成（RAG）和基于 Agent 的大语言模型（LLM）应用中变得愈发关键。本文提出了 CRINN，一种 ANNS 算法优化新范式。CRINN 将 ANNS 优化建模为强化学习问题，并将执行速度作为奖励信号，从而在满足准确性约束的前提下，自动生成执行速度更快的 ANNS 实现。实验评估涵盖了六个广泛使用的 NNS 基准数据集。结果显示，与最先进的开源 ANNS 算法相比，CRINN 在 GIST-...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Toward AI-Agent-Driven Particle Transport Simulations: Implementation of AI-Assisted Workflows for PHITS](http://arxiv.org/abs/2607.11309v1)
  来源：arXiv | 日期：2026-07-13 | 相关度：1.4 | 新颖度：6.36
  匹配主题：未命中具体主题
  中文摘要：蒙特卡罗粒子输运代码（如 PHITS）功能强大，但其使用涉及复杂的输入准备、执行和结果分析，对用户专业知识要求极高。本研究提出了一种将现有 AI 助手和 AI 智能体（AI Agents）应用于 PHITS 的代码侧策略。研究准备了两套互补的 AI 资源：一套是基于手册、讲义、示例输入和开发者注意事项构建的 RAG（检索增强生成）知识库，用于 NotebookLM 提供对话支持；另一套是紧凑的智能体参考指南，结合 PHITS 特定策略和...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Eval-Pair Matrix: Answer-Paired Meta-Evaluation of LLM Judges for Grounded RAG](http://arxiv.org/abs/2607.10626v1)
  来源：arXiv | 日期：2026-07-12 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：本研究针对检索增强生成（RAG）中“LLM作为评委”评估存在的自我宽容（self-leniency）偏见难以识别的问题，提出了Eval-Pair Matrix元评估协议。研究基于GaRAGe数据集的问题和背景段落，在每条记录中引入一个隐藏的答案因果矛盾，并利用GPT、Grok和Gemini模型从扰动段落中生成答案。随后，这些模型作为盲审评委，根据原始段落评估所有生成的答案。实验包含300条核心记录、897个标记的生成输出和2683个评委...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Imaging-101: Benchmarking LLM Coding Agents on Scientific Computational Imaging](http://arxiv.org/abs/2607.10789v1)
  来源：arXiv | 日期：2026-07-12 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：计算成像通过间接、有噪声的测量恢复隐藏信号，是各科学领域定量发现的基础，但构建正确的重建流程需要深厚的领域知识。本文推出了 Imaging-101，这是一个包含 57 个专家验证的计算成像任务基准，涵盖六个科学领域。每个任务均源自同行评审论文，并标准化为预处理、前向物理建模、逆求解器和可视化四个阶段。该基准通过规划、函数级单元测试和端到端重建三个评估轨道，探测智能体在完整流程中的能力。对七种前沿大语言模型（LLM）的评估揭示了编码智能体...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HYPIC: Accelerating Hybrid-Attention LLM Serving with Position-Independent Caching](http://arxiv.org/abs/2607.01299v2)
  来源：arXiv | 日期：2026-07-01 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：在检索增强生成（RAG）和智能体（Agent）LLM 服务中，提示词通常由独立片段组合成超长上下文，导致预填充阶段成为主要的计算瓶颈。目前存在两种优化方向：位置无关缓存（PIC）允许跨请求重用非连续片段的 KV 缓存；混合注意力模型则通过线性注意力层替换全注意力层以减少计算量。然而，由于线性注意力的循环状态无法直接应用逐 Token 的 KV 缓存重用原语，两者难以兼容。本文提出 Hypic，这是首个利用 PIC 加速混合注意力 LLM...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Tokenizing single-cell transcriptomes as a native language for large language models](https://www.biorxiv.org/content/10.1101/2025.10.22.684047v2)
  来源：bioRxiv | 日期：2026-07-11 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：大语言模型（LLMs）能够处理多种形式的信息，前提是将其表示为共享序列空间中的 Token。然而，单细胞转录组由于是连续、高维的分子图谱而非离散语言单位，对 LLM 而言仍是异质模态。本研究提出了 CellTok，一种单细胞语言建模方法，将转录组图谱转换为紧凑的细胞 Token 序列，并将其整合进预训练 LLM 的词表。通过将细胞表示为原生 Token，CellTok 使得细胞测量值、文本指令、生物学上下文和多细胞群体能够在同一个自回归...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Evo-EquiGPS: Synergizing Dynamic Geometry, Global Topology, and Explicit Evolution for High-Precision Enzyme Active Site Prediction.](https://pubmed.ncbi.nlm.nih.gov/42439568/)
  来源：PubMed | 日期：2026-07-13 | 相关度：3.05 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Accurate identification of enzyme active sites is a prerequisite for elucidating protein functions and guiding enzyme engineering. Driven by the exponential growth of protein sequence data from next-generation sequencing...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Trust Before Fusion: QIMG-7 and Source-Aware Resolution for Polluted Multimodal RAG](http://arxiv.org/abs/2607.10798v1)
  来源：arXiv | 日期：2026-07-12 | 相关度：2.75 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：多模态检索增强生成（RAG）通常在理想证据下评估，但实际检索常返回相关却不可靠的内容，如虚假文本或因元数据损坏、实体交换、对抗补丁及风格迁移导致的误导性图像。本研究引入了 QIMG-7，这是一个针对多句子事实问答中多模态检索污染的受控基准，涵盖 4 个数据集、7 类图像攻击家族和 16 种清洁/污染配对方案，每种方法包含 1,760 行评估数据。实验显示，在四种生成器堆栈中，原生多模态融合表现脆弱：在 gpt-4o-mini 堆栈中，F...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Enhancing LLMs through human feedback: a journey towards self-improvement](http://arxiv.org/abs/2607.11267v1)
  来源：arXiv | 日期：2026-07-13 | 相关度：2.1 | 新颖度：7.52
  匹配主题：未命中具体主题
  中文摘要：在信息检索系统快速演进的背景下，通过用户反馈进行适应和改进至关重要。本研究提出了一种创新方法，通过战略性地整合辅助反馈检索增强生成（RAG）系统，来优化主 RAG 系统的性能。该方法系统地利用人类生成的反馈，旨在提高响应的准确性、相关性和整体质量，推动系统实现自我改进。其核心在于“人类在环”（human-in-the-loop）的实现，即持续收集、分类用户反馈并将其整合到推理工作流中，使系统能够迭代学习和演化。为验证该方法的有效性，研究...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Community-driven advances in computational mass spectrometry: The perspective of EuBIC-MS members.](https://pubmed.ncbi.nlm.nih.gov/42436009/)
  来源：PubMed | 日期：2026-07-11 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：数据采集、人工智能和综合生物信息学的进步正推动计算质谱学的快速演变，进而改变现代蛋白质组学、代谢组学和脂质组学。随着质谱数据规模和复杂性的增加，开发准确、透明、高效且可重复的数据处理工作流变得至关重要。欧洲质谱生物信息学社区（EuBIC-MS）通过开发者会议和冬季学校促进开放式社区驱动开发。本文总结了 2025 年 EuBIC-MS 开发者会议的成果。会议涵盖三大前沿领域：深度蛋白质组与磷酸化蛋白质组分析、用于蛋白质相互作用（PPI）提...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [From Embedding Geometry to Spectral Search: Energy Dispersion Networks For Vector Retrieval](http://arxiv.org/abs/2606.21535v2)
  来源：arXiv | 日期：2026-06-19 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：高维向量空间（尤其是具有密集语义结构的嵌入空间）通常仅利用几何关系进行解释。本研究表明，这些空间也可以被视为由底层特征空间流形拓扑诱导的光谱能量网络（spectral energy networks），并能显著提升下游任务性能。基于此视角，我们提出了 Graph Wiring 通用框架以利用特征空间的光谱结构，并开发了针对向量搜索的任务特定实例——Spectral Indexing。通过将几何相似性与光谱信息耦合，该方法相较于纯几何检索...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MC-RAG System: A Structure-Driven RAG System for Multi-Constraint Queries](http://arxiv.org/abs/2607.10151v1)
  来源：arXiv | 日期：2026-07-11 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）系统在问答领域被广泛采用，但在处理复杂的多约束查询时，往往难以满足所有条件，导致约束违背、事实不一致或产生幻觉。本文提出了 MC-RAG，这是一种面向多约束查询的结构驱动型 RAG 系统。该系统将检索过程重新定义为知识图谱上的子图匹配问题。通过整合语义与结构嵌入以及路径级索引，MC-RAG 实现了具有可解释性、结构感知且符合约束条件的检索与生成。在演示环节中，参与者可以输入医疗或百科类的多约束查询，并直观地观察系统...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。
