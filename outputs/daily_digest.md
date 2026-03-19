# 每日论文监控日报 (2026-03-19)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 66 篇新论文。

## 抓取状态

- arXiv：成功，命中 55 篇
- PubMed：成功，命中 35 篇
- bioRxiv：成功，命中 25 篇
- medRxiv：成功，命中 8 篇

## 最值得看

### Foundation Model / Agent

- [Tabular LLMs for Interpretable Few-Shot Alzheimer's Disease Prediction with Multimodal Biomedical Data](http://arxiv.org/abs/2603.17191v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：8.5 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Accurate diagnosis of Alzheimer's disease (AD) requires handling tabular biomarker data, yet such data are often small and incomplete, where deep learning models frequently fail to outperform classical methods. Pretraine...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Caption Injection for Optimization in Generative Search Engine](http://arxiv.org/abs/2511.04080v2)
  来源：arXiv | 日期：2025-11-06 | 相关度：7.9 | 新颖度：6.7
  匹配主题：foundation_model_agent
  中文摘要：Generative Search Engine (GSE) leverages the Retrieval-Augmented Generation (RAG) technique and the Large Language Model (LLM) to integrate multi-source information and provide users with accurate and comprehensive respo...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HARVEST: Unlocking the Dark Bioactivity Data of Pharmaceutical Patents via Agentic AI](https://www.biorxiv.org/content/10.64898/2026.03.15.711910v1)
  来源：bioRxiv | 日期：2026-03-18 | 相关度：7.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Pharmaceutical patents contain vast Structure-Activity Relationship tables documenting protein-ligand binding data that are technically public yet computationally inaccessible, rendering this wealth of data effectively d...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Grounded Multimodal Retrieval-Augmented Drafting of Radiology Impressions Using Case-Based Similarity Search](http://arxiv.org/abs/2603.17765v1)
  来源：arXiv | 日期：2026-03-18 | 相关度：8.5 | 新颖度：8.02
  匹配主题：foundation_model_agent
  中文摘要：Automated radiology report generation has gained increasing attention with the rise of deep learning and large language models. However, fully generative approaches often suffer from hallucinations and lack clinical grou...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [ELISA: An Interpretable Hybrid Generative AI Agent for Expression-Grounded Discovery in Single-Cell Genomics](http://arxiv.org/abs/2603.11872v2)
  来源：arXiv | 日期：2026-03-12 | 相关度：7.55 | 新颖度：2.5
  匹配主题：foundation_model_agent
  中文摘要：Translating single-cell RNA sequencing (scRNA-seq) data into mechanistic biological hypotheses remains a critical bottleneck, as agentic AI systems lack direct access to transcriptomic representations while expression fo...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AutothinkRAG: Complexity-Aware Control of Retrieval-Augmented Reasoning for Image-Text Interaction](http://arxiv.org/abs/2603.05551v2)
  来源：arXiv | 日期：2026-03-05 | 相关度：7.5 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Multimodal document question answering requires retrieving dispersed evidence from visually rich long documents and performing reliable reasoning over heterogeneous information. Existing multimodal RAG systems remain lim...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Ablation Study of a Fairness Auditing Agentic System for Bias Mitigation in Early-Onset Colorectal Cancer Detection](http://arxiv.org/abs/2603.17179v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence (AI) is increasingly used in clinical settings, yet limited oversight and domain expertise can allow algorithmic bias and safety risks to persist. This study evaluates whether an agentic AI system...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Sentiment in Clinical Notes: A Predictor for Length of Stay?](https://www.medrxiv.org/content/10.64898/2026.03.16.26348553v1)
  来源：medRxiv | 日期：2026-03-18 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Background: Length of stay (LOS) is a critical metric for hospital operational efficiency. While structured clinical data is widely used to predict LOS, unstructured admission notes contain latent prognostic information ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OmicClaw: executable and reproducible natural-language multi-omics analysis over the unified OmicVerse ecosystem.](https://www.biorxiv.org/content/10.64898/2026.03.13.711464v1)
  来源：bioRxiv | 日期：2026-03-17 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Advances in bulk, single-cell and spatial omics have transformed biological discovery, yet analysis remains fragmented across packages with incompatible interfaces, heterogeneous dependencies and limited workflow reprodu...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PaAgent: Portrait-Aware Image Restoration Agent via Subjective-Objective Reinforcement Learning](http://arxiv.org/abs/2603.17055v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：6.8 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Image Restoration (IR) agents, leveraging multimodal large language models to perceive degradation and invoke restoration tools, have shown promise in automating IR tasks. However, existing IR agents typically lack an in...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Large Language Models in Teaching and Learning: Reflections on Implementing an AI Chatbot in Higher Education](http://arxiv.org/abs/2603.17773v1)
  来源：arXiv | 日期：2026-03-18 | 相关度：6.55 | 新颖度：7.79
  匹配主题：foundation_model_agent
  中文摘要：The landscape of education is changing rapidly, shaped by emerging pedagogical approaches, technological innovations such as artificial intelligence (AI), and evolving societal expectations, all of which demand thorough ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions](http://arxiv.org/abs/2507.05257v3)
  来源：arXiv | 日期：2025-07-07 | 相关度：6.55 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：Recent benchmarks for Large Language Model (LLM) agents primarily focus on evaluating reasoning, planning, and execution capabilities, while another critical component-memory, encompassing how agents memorize, update, an...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Role-Augmented Intent-Driven Generative Search Engine Optimization](http://arxiv.org/abs/2508.11158v2)
  来源：arXiv | 日期：2025-08-15 | 相关度：6.55 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：Generative Search Engines (GSEs), powered by Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG), are reshaping information retrieval. While commercial systems (e.g., BingChat, Perplexity.ai) demonstrat...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SENSE: Efficient EEG-to-Text via Privacy-Preserving Semantic Retrieval](http://arxiv.org/abs/2603.17109v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：6.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Decoding brain activity into natural language is a major challenge in AI with important applications in assistive communication, neurotechnology, and human-computer interaction. Most existing Brain-Computer Interface (BC...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MetaBeeAI: an AI pipeline for structured evidence extraction from biological literature](https://www.biorxiv.org/content/10.1101/2025.11.24.690154v2)
  来源：bioRxiv | 日期：2026-03-18 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：The volume and complexity of scientific literature are expanding rapidly, making it increasingly difficult to extract and synthesise information across studies. This challenge is particularly acute in the biological scie...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Toward Experimentation-as-a-Service in 5G/6G: The Plaza6G Prototype for AI-Assisted Trials](http://arxiv.org/abs/2603.16356v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：6.55 | 新颖度：1.2
  匹配主题：foundation_model_agent
  中文摘要：This paper presents Plaza6G, the first operational Experiment-as-a-Service (ExaS) platform unifying cloud resources with next-generation wireless infrastructure. Developed at CTTC in Barcelona, Plaza6G integrates GPU-acc...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Unified Language Model for Large Scale Search, Recommendation, and Reasoning](http://arxiv.org/abs/2603.17533v1)
  来源：arXiv | 日期：2026-03-18 | 相关度：6.15 | 新颖度：6.73
  匹配主题：foundation_model_agent
  中文摘要：LLMs are increasingly applied to recommendation, retrieval, and reasoning, yet deploying a single end-to-end model that can jointly support these behaviors over large, heterogeneous catalogs remains challenging. Such sys...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Are a Thousand Words Better Than a Single Picture? Beyond Images -- A Framework for Multi-Modal Knowledge Graph Dataset Enrichment](http://arxiv.org/abs/2603.16974v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Multi-Modal Knowledge Graphs (MMKGs) benefit from visual information, yet large-scale image collection is hard to curate and often excludes ambiguous but relevant visuals (e.g., logos, symbols, abstract scenes). We prese...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Slides to Chatbots: Enhancing Large Language Models with University Course Materials](http://arxiv.org/abs/2510.22272v2)
  来源：arXiv | 日期：2025-10-25 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have advanced rapidly in recent years. One application of LLMs is to support student learning in educational settings. However, prior work has shown that LLMs still struggle to answer questio...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SYMDIREC: A Neuro-Symbolic Divide-Retrieve-Conquer Framework for Enhanced RTL Synthesis and Summarization](http://arxiv.org/abs/2603.17208v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Register-Transfer Level (RTL) synthesis and summarization are central to hardware design automation but remain challenging for Large Language Models (LLMs) due to rigid HDL syntax, limited supervision, and weak alignment...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [InferDPT: Privacy-Preserving Inference for Closed-box Large Language Model](http://arxiv.org/abs/2310.12214v8)
  来源：arXiv | 日期：2023-10-18 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs), like ChatGPT, have greatly simplified text generation tasks. However, they have also raised concerns about privacy risks such as data leakage and unauthorized data collection. Existing solut...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Machines acquire scientific taste from institutional traces](http://arxiv.org/abs/2603.16659v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence matches or exceeds human performance on tasks with verifiable answers, from protein folding to Olympiad mathematics. Yet the capacity that most governs scientific advance is not reasoning but tast...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [VarDCL: A Multimodal PLM-Enhanced Framework for Missense Variant Effect Prediction via Self-distilled Contrastive Learning](https://www.biorxiv.org/content/10.64898/2026.03.13.711612v1)
  来源：bioRxiv | 日期：2026-03-17 | 相关度：10.0 | 新颖度：1.0
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Abstract. Missense variants are a common type of genetic mutation that can alter the structure and function of proteins, thereby affecting the normal physiological processes of organisms. Accurately distinguishing damagi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Artificial Intelligence for Automated, Highly Accurate, and Scalable Multimodal EHR Data Abstraction](https://www.medrxiv.org/content/10.64898/2026.03.16.26348522v1)
  来源：medRxiv | 日期：2026-03-17 | 相关度：7.8 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Electronic health records (EHRs) contain rich multimodal data but remain underutilized for populating clinical registries due to the time and cost of manual abstraction. We developed an AI driven pipeline to automate dat...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SeekRBP: Leveraging Sequence-Structure Integration with Reinforcement Learning for Receptor-Binding Protein Identification](http://arxiv.org/abs/2603.04748v2)
  来源：arXiv | 日期：2026-03-05 | 相关度：7.1 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Motivation: Receptor-binding proteins (RBPs) initiate viral infection and determine host specificity, serving as key targets for phage engineering and therapy. However, the identification of RBPs is complicated by their ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Beyond Muon: MUD (MomentUm Decorrelation) for Faster Transformer Training](http://arxiv.org/abs/2603.17970v1)
  来源：arXiv | 日期：2026-03-18 | 相关度：6.45 | 新颖度：7.8
  匹配主题：foundation_model_agent
  中文摘要：Orthogonalized-momentum optimizers such as Muon improve transformer training by approximately whitening/orthogonalizing matrix-valued momentum updates via a short polar-decomposition iteration. However, polar-factor appr...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RNAElectra: An ELECTRA-Style RNA Foundation Model for RNA Regulatory Inference](https://www.biorxiv.org/content/10.64898/2026.03.15.711950v1)
  来源：bioRxiv | 日期：2026-03-17 | 相关度：6.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：RNA regulation governs gene expression through sequence-encoded mechanisms such as RNA structure formation, protein binding, chemical modification, and RNA-RNA targeting, with regulatory rules spanning both nucleotide-sc...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [HERCULES: an integrative deep-learning framework for predicting RNA-binding propensity and mutation effects at single-residue resolution](https://www.biorxiv.org/content/10.64898/2026.03.17.712455v1)
  来源：bioRxiv | 日期：2026-03-18 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：RNA-binding proteins (RBPs) regulate essential aspects of RNA metabolism, yet accurately identifying RNA-binding domains (RBDs) and quantifying the impact of sequence variation on RNA-binding ability remain challenging. ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Adaptive Guidance for Retrieval-Augmented Masked Diffusion Models](http://arxiv.org/abs/2603.17677v1)
  来源：arXiv | 日期：2026-03-18 | 相关度：5.45 | 新颖度：7.52
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) improves factual grounding by incorporating external knowledge into language model generation. However, when retrieved context is noisy, unreliable, or inconsistent with the model's p...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [LR-Robot: A Unified Supervised Intelligent Framework for Real-Time Systematic Literature Reviews with Large Language Models](http://arxiv.org/abs/2603.17723v1)
  来源：arXiv | 日期：2026-03-18 | 相关度：5.45 | 新颖度：7.15
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in artificial intelligence (AI) and natural language processing (NLP) have enabled tools to support systematic literature reviews (SLRs), yet existing frameworks often produce outputs that are efficient b...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RAGXplain: From Explainable Evaluation to Actionable Guidance of RAG Pipelines](http://arxiv.org/abs/2505.13538v2)
  来源：arXiv | 日期：2025-05-18 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) systems couple large language models with external knowledge, yet most evaluation methods report aggregate scores that reveal whether a pipeline underperforms but not where or why. We...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Towards Unsupervised Adversarial Document Detection in Retrieval Augmented Generation Systems](http://arxiv.org/abs/2603.17176v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval augmented generation systems have become an integral part of everyday life. Whether in internet search engines, email systems, or service chatbots, these systems are based on context retrieval and answer genera...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [HGP-Mamba: Integrating Histology and Generated Protein Features for Mamba-based Multimodal Survival Risk Prediction](http://arxiv.org/abs/2603.16421v2)
  来源：arXiv | 日期：2026-03-17 | 相关度：3.75 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in multimodal learning have significantly improved cancer survival risk prediction. However, the joint prognostic potential of protein markers and histopathology images remains underexplored, largely due ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [An Interpretable Machine Learning Framework for Non-Small Cell Lung Cancer Drug Response Analysis](http://arxiv.org/abs/2603.16330v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Lung cancer is a condition where there is abnormal growth of malignant cells that spread in an uncontrollable fashion in the lungs. Some common treatment strategies are surgery, chemotherapy, and radiation which aren't t...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [CoNVict: An Agentic AI System for Copy Number Variation Prioritization in Rare Disease Diagnosis](https://www.medrxiv.org/content/10.64898/2026.03.16.26348493v1)
  来源：medRxiv | 日期：2026-03-17 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Copy number variants (CNVs) are established contributors to rare genetic disorders, yet their clinical interpretation remains challenging in diagnostic genomics. Large CNVs frequently encompass multiple functional region...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Agentic Exploration of Physics Models](http://arxiv.org/abs/2509.24978v5)
  来源：arXiv | 日期：2025-09-29 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：The process of scientific discovery relies on an interplay of observations, analysis, and hypothesis generation. Machine learning is increasingly being adopted to address individual aspects of this process. However, it r...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Protein Design with Agent Rosetta: A Case Study for Specialized Scientific Agents](http://arxiv.org/abs/2603.15952v1)
  来源：arXiv | 日期：2026-03-16 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are capable of emulating reasoning and using tools, creating opportunities for autonomous agents that execute complex scientific tasks. Protein design provides a natural testbed: although mac...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights](http://arxiv.org/abs/2603.16817v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) frequently hallucinate, limiting their reliability in knowledge-intensive applications. Retrieval-augmented generation (RAG) and conformal factuality have emerged as potential ways to address...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Automating Skill Acquisition through Large-Scale Mining of Open-Source Agentic Repositories: A Framework for Multi-Agent Procedural Knowledge Extraction](http://arxiv.org/abs/2603.11808v2)
  来源：arXiv | 日期：2026-03-12 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：The transition from monolithic large language models (LLMs) to modular, skill-equipped agents represents a fundamental architectural shift in artificial intelligence deployment. While general-purpose models demonstrate r...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Retrieval-Augmented Sketch-Guided 3D Building Generation](http://arxiv.org/abs/2603.16612v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：3.45 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：In the early design stage of Japanese detached houses, the lack of a unified design representation among clients, sales representatives, and designers leads to design drift and inefficient feedback. Usually, sketches han...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Open Biomedical Knowledge Graphs at Scale: Construction, Federation, and AI Agent Access with Samyama Graph Database](http://arxiv.org/abs/2603.15080v3)
  来源：arXiv | 日期：2026-03-16 | 相关度：3.1 | 新颖度：6.75
  匹配主题：未命中具体主题
  中文摘要：Biomedical knowledge is fragmented across siloed databases -- Reactome for pathways, STRING for protein interactions, ClinicalTrials.gov for study registries, DrugBank for drug vocabularies, DGIdb for drug-gene interacti...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [IoDResearch: Deep Research on Private Heterogeneous Data via the Internet of Data](http://arxiv.org/abs/2510.01553v2)
  来源：arXiv | 日期：2025-10-02 | 相关度：2.1 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：The rapid growth of multi-source, heterogeneous, and multimodal scientific data has increasingly exposed the limitations of traditional data management. Most existing DeepResearch (DR) efforts focus primarily on web sear...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [IndexRAG: Bridging Facts for Cross-Document Reasoning at Index Time](http://arxiv.org/abs/2603.16415v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：2.1 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：多跳问答（QA）要求跨多个文档进行推理，但现有的检索增强生成（RAG）方法通常依赖于需要额外在线处理的图方法或迭代式多步推理。本文提出 IndexRAG，一种将跨文档推理从在线推理阶段转移到离线索引阶段的新方法。IndexRAG 通过识别文档间共享的桥接实体，生成作为独立可检索单元的“桥接事实”，该过程无需额外的模型训练或微调。在 HotpotQA、2WikiMultiHopQA 和 MuSiQue 三个主流多跳问答基准测试上的实验结果...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RADAR: Retrieval-Augmented Detector with Adversarial Refinement for Robust Fake News Detection](http://arxiv.org/abs/2601.03981v2)
  来源：arXiv | 日期：2026-01-07 | 相关度：2.05 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：为了有效打击大语言模型（LLM）生成的虚假信息，本文提出了 RADAR（具有对抗性细化的检索增强检测器）。该方法包含一个通过事实扰动重写真实文章的生成器，以及一个利用稠密段落检索（Dense Passage Retrieval）验证声明的轻量级检测器。为了实现有效的协同演化，研究引入了口头对抗反馈（VAF）。VAF 不再依赖传统的标量奖励，而是提供结构化的自然语言评论，引导生成器进行更复杂的规避尝试，从而迫使检测器不断适应和改进。在虚假...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CARE: A Molecular-Guided Foundation Model with Adaptive Region Modeling for Whole Slide Image Analysis](http://arxiv.org/abs/2602.21637v3)
  来源：arXiv | 日期：2026-02-25 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：基础模型在计算病理学中取得了显著成功，但现有模型多依赖于非组织形态定制的自然图像骨干网络，忽略了病理感兴趣区域（ROI）的异质性和非均匀组织，难以捕捉孤立补丁（patches）之外的连贯组织架构。为此，研究者提出了跨模态自适应区域编码器（CARE），这是一种能自动将全扫描切片图像（WSI）划分为多个形态相关区域的病理基础模型。CARE 采用两阶段预训练策略：首先在 34,277 张无分割标注的 WSI 上进行自监督单模态预训练以学习形态...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HindSight: Evaluating LLM-Generated Research Ideas via Future Impact](http://arxiv.org/abs/2603.15164v2)
  来源：arXiv | 日期：2026-03-16 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：评估人工智能生成的科研想法通常依赖于 LLM 评委或专家小组，这具有主观性且脱离了实际的科研影响力。本研究引入了 HindSight，这是一个基于时间切分的评估框架，通过将生成的想法与真实的未来出版物进行匹配，并根据引用影响力和发表平台进行评分，从而衡量想法的质量。该框架设定时间截止点 T，限制生成系统仅能访问 T 之前的文献，随后将其输出与之后 30 个月内发表的论文进行对比。在 10 个 AI/ML 研究主题上的实验揭示了显著差异：...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RPMS: Enhancing LLM-Based Embodied Planning through Rule-Augmented Memory Synergy](http://arxiv.org/abs/2603.17831v1)
  来源：arXiv | 日期：2026-03-18 | 相关度：0.7 | 新颖度：7.19
  匹配主题：未命中具体主题
  中文摘要：LLM 智能体在闭世界具身环境中常因动作必须满足严格前提条件（如位置、库存和容器状态）且反馈稀疏而失败。本文识别了两种耦合的失败模式：无效动作生成（P1）和状态漂移（P2），两者会形成退化循环。为此，我们提出了 RPMS，一种冲突管理架构。该架构通过结构化规则检索强制执行动作可行性，利用轻量级信念状态过滤记忆适用性，并通过规则优先仲裁解决两者间的冲突。在 ALFWorld 的 134 个未知任务中，RPMS 使 Llama 3.1 8B...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Intracellular Measurement-Informed Multiscale Modeling for Scalable iPSC Manufacturing](http://arxiv.org/abs/2603.17090v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：0.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：人诱导多能干细胞（iPSC）的大规模制造对于细胞疗法和再生医学的工业化生产至关重要。然而，与实验室研究中相对均质的单层培养系统相比，生产中使用的3D聚集体培养表现出显著的空间和代谢异质性，这增加了跨培养尺度的机制理解和预测性代谢建模的难度。为解决这一挑战，研究者开发了一个模块化多尺度机制基础模型，将分子、细胞和宏观过程联系起来，并兼顾了空间与代谢异质性。该框架通过扩展现有的单层动力学网络，并将其与用于聚集体培养的生物系统之系统（Bio-...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Exploring different approaches to customize language models for domain-specific text-to-code generation](http://arxiv.org/abs/2603.16526v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：5.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have demonstrated strong capabilities in generating executable code from natural language descriptions. However, general-purpose models often struggle in specialized programming contexts wher...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Detecting Manuscripts Related to Computable Phenotypes Using a Transformer-based Language Model](https://www.biorxiv.org/content/10.64898/2026.03.12.711165v1)
  来源：bioRxiv | 日期：2026-03-16 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Objective: The demand for a comprehensive phenomics library, which requires identifying computable phenotype definitions and associated metadata from an ever-expanding biomedical literature, presents a significant, labor...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [AI Scientist via Synthetic Task Scaling](http://arxiv.org/abs/2603.17216v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：0.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：随着AI智能体的兴起，自动化科学发现已成为可行目标。尽管现有系统可执行机器学习研究，但缺乏系统的训练方法，且大语言模型常生成看似合理但无效的思路。为提升智能体“在做中学”的能力，本文提出一种针对机器学习智能体的自动化合成环境生成管线。该管线可自动合成与SWE-agent框架兼容的机器学习挑战，涵盖主题采样、数据集建议及代码生成。合成任务具有两大特点：一是基于Huggingface API验证的真实机器学习数据集；二是通过自调试循环确保任...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Exposing Blindspots: Cultural Bias Evaluation in Generative Image Models](http://arxiv.org/abs/2510.20042v2)
  来源：arXiv | 日期：2025-10-22 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：生成式图像模型在产出高质量视觉内容的同时，常存在文化误导风险。本研究针对文本生成图像（T2I）和图像编辑（I2I）系统，构建了一个涵盖6个国家、8个大类及36个子类别的统一评估框架，并引入了具有时代意识的提示词。通过标准化协议，研究对开源模型进行了跨国、跨时代和跨类别的审计。评估方法结合了自动指标、文化感知检索增强型VQA以及母语专家的主观评价。研究发现：(1) 在国家中性提示下，模型默认呈现全球北方及现代风格，抹平了国家差异；(2) ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Unlocking Enzyme Discovery: A High-Resolution Gene Cluster Database Powered by Phylogenetic Insights and Machine Learning.](https://pubmed.ncbi.nlm.nih.gov/41837859/)
  来源：PubMed | 日期：2026-03-16 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：High-throughput sequencing has generated vast genomic repositories that remain under-annotated, hampering enzyme discovery. We present an integrated pipeline that (i) builds a high-resolution, cross-kingdom phylogenetic ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [When Stability Fails: Hidden Failure Modes Of LLMS in Data-Constrained Scientific Decision-Making](http://arxiv.org/abs/2603.15840v1)
  来源：arXiv | 日期：2026-03-16 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly used as decision-support tools in data-constrained scientific workflows, where correctness and validity are critical. However, evaluation practices often emphasize stability ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AGRAG: Advanced Graph-based Retrieval-Augmented Generation for LLMs](http://arxiv.org/abs/2511.05549v2)
  来源：arXiv | 日期：2025-11-02 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Graph-based retrieval-augmented generation (Graph-based RAG) has demonstrated significant potential in enhancing Large Language Models (LLMs) with structured knowledge. However, existing methods face three critical chall...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering](http://arxiv.org/abs/2601.03014v2)
  来源：arXiv | 日期：2026-01-06 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Traditional Retrieval-Augmented Generation (RAG) effectively supports single-hop question answering with large language models but faces significant limitations in multi-hop question answering tasks, which require combin...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Novel Deep-Learning Unsupervised Domain Adaptation Method for Mitigating Batch, Strain, and Instrument Variations to Enhance Raman Spectroscopy-Based Bacterial Pathogen Identification.](https://pubmed.ncbi.nlm.nih.gov/41842761/)
  来源：PubMed | 日期：2026-03-17 | 相关度：4.4 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：The escalating threat of antibiotic resistance demands a rapid and accurate pathogen identification. While Raman spectroscopy combined with deep learning supports fast detection, model robustness remains compromised by d...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Using image classifiers to predict CMT2A disease-relevant mitochondrial motility phenotypes in iPSC motor neurons](https://www.biorxiv.org/content/10.64898/2026.03.16.712192v1)
  来源：bioRxiv | 日期：2026-03-17 | 相关度：2.65 | 新颖度：0.75
  匹配主题：sequencing_bioinformatics
  中文摘要：Charcot-Marie-Tooth disease type 2A (CMT2A) is a genetic disease characterized by autosomal dominant MFN2 mutations and dysregulated mitochondrial trafficking. While there is currently no FDA-approved CMT2A therapy, the ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Species-specific small models for cell type classification approach the performance of large single cell foundation models](https://www.biorxiv.org/content/10.64898/2026.03.16.711196v1)
  来源：bioRxiv | 日期：2026-03-18 | 相关度：2.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Accurate cross-species cell type classification remains a key evaluation task in single-cell transcriptomics. Recent foundation models trained on millions of single-cell profiles demonstrate strong in-distribution and ou...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Atomic Trajectory Modeling with State Space Models for Biomolecular Dynamics](http://arxiv.org/abs/2603.17633v1)
  来源：arXiv | 日期：2026-03-18 | 相关度：1.7 | 新颖度：7.1
  匹配主题：未命中具体主题
  中文摘要：理解生物分子的动态行为对于阐明生物功能和促进药物发现至关重要。虽然分子动力学（MD）模拟为研究这些动态提供了严谨的物理基础，但在长时标模拟中计算成本极高。现有的深度生成模型虽能加速构象生成，但往往无法建模时间关系，或仅限于单体蛋白质。为此，我们提出了 ATMOS，这是一种基于状态空间模型（SSM）的新型生成框架，旨在生成生物分子系统的原子级 MD 轨迹。ATMOS 集成了基于 Pairformer 的状态转移机制以捕捉远程时间依赖性，并...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SCALE:Scalable Conditional Atlas-Level Endpoint transport for virtual cell perturbation prediction](http://arxiv.org/abs/2603.17380v1)
  来源：arXiv | 日期：2026-03-18 | 相关度：1.4 | 新颖度：6.84
  匹配主题：未命中具体主题
  中文摘要：虚拟细胞模型旨在通过单细胞测量数据，预测细胞对遗传、化学或细胞因子扰动的响应。然而，大规模扰动预测目前面临训练推理效率低下、高维稀疏表达空间建模不稳定以及评估协议过度强调重建精度而忽视生物学保真度三大瓶颈。本研究提出了专门用于虚拟细胞扰动预测的大规模基础模型 SCALE。首先，构建了基于 BioNeMo 的训练与推理框架，在相同系统设置下，预训练速度较现有 SOTA 提升 12.51 倍，推理速度提升 1.29 倍。其次，将扰动预测表述...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SEAL-Tag: Self-Tag Evidence Aggregation with Probabilistic Circuits for PII-Safe Retrieval-Augmented Generation](http://arxiv.org/abs/2603.17292v1)
  来源：arXiv | 日期：2026-03-18 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）系统面临上下文泄露的严峻挑战，攻击者可通过指令遵循利用自适应提取手段窃取个人身份信息（PII）。现有的防御方案通常在语义效用与处理延迟之间进行权衡。本文提出 SEAL-Tag，一种基于“先验证后路由”范式的隐私保护运行时环境。该方案引入 SEAL-Probe 协议，将审计过程转化为结构化的工具调用操作，使模型在生成草稿的同时产生可验证的 PII 证据表（PET）。为了裁定这些证据，研究采用概率电路（PC）实施可验证...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [A Comprehensive Benchmark of Histopathology Foundation Models for Kidney Digital Pathology Images](http://arxiv.org/abs/2603.15967v2)
  来源：arXiv | 日期：2026-03-16 | 相关度：3.05 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Histopathology foundation models (HFMs), pretrained on large-scale cancer datasets, have advanced computational pathology. However, their applicability to non-cancerous chronic kidney disease remains underexplored, despi...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Advances in spherical nanoparticle-labeled lateral flow immunoassays in the field of clinical detection.](https://pubmed.ncbi.nlm.nih.gov/41736637/)
  来源：PubMed | 日期：2026-03-18 | 相关度：3.05 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Lateral flow immunoassay (LFIA), as one of the core technologies of point-of-care testing (POCT), holds significant value in pathogen diagnosis and biomarker analysis. Notably, spherical nanomaterials exhibit high clinic...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [OpenScientist: evaluating an open agentic AI co-scientist to accelerate biomedical discovery](https://www.medrxiv.org/content/10.64898/2026.03.15.26348338v1)
  来源：medRxiv | 日期：2026-03-18 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：背景：医学进步受限于研究者有限的时间和专业领域知识。OpenScientist 是一款开源的智能体 AI（agentic AI）科研助手，旨在通过半自主地调查科学问题并生成临床相关且可验证的见解，从而加速生物医学发现。方法：领域专家在四个临床案例中评估了 OpenScientist：(1) 社区阿尔茨海默病生物标志物队列的预设分析；(2) 血浆蛋白质组生存预测的无监督建模；(3) 神经原纤维缠结神经元的单细胞转录组数据假设调查；(4) ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Toward precision chemotherapy in pancreatic ductal adenocarcinoma: molecular, transcriptomic and clinical determinants.](https://pubmed.ncbi.nlm.nih.gov/41846177/)
  来源：PubMed | 日期：2026-03-16 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：胰腺导管腺癌（PDAC）是致死率极高的恶性肿瘤，化疗仍是各阶段系统治疗的核心。尽管改良型FOLFIRINOX及吉西他滨联合白蛋白结合型紫杉醇（AG或PAXG）等方案改善了部分患者预后，但疗效具有高度异质性且受毒性限制。本综述总结了从经验性化疗转向整合肿瘤生物学、分子生物学标志物及患者相关因素（如药物基因组学、合并症和毒性特征）的个体化方案的证据。目前，同源重组修复缺陷（HRD）、错配修复缺陷（MMRD）及罕见致癌融合等分子特征仅能为少数...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
