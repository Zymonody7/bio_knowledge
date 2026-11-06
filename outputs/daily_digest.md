# 每日论文监控日报 (2026-11-06)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 55 篇新论文。

## 抓取状态

- arXiv：成功，命中 54 篇
- PubMed：成功，命中 61 篇
- bioRxiv：成功，命中 14 篇
- medRxiv：成功，命中 12 篇

## 最值得看

### Foundation Model / Agent

- [Thalamus-Reasoning: A Multimodal Large Language Model for Multi-Sample Omics Reasoning](http://arxiv.org/abs/2605.06728v3)
  来源：arXiv | 日期：2026-05-07 | 相关度：8.9 | 新颖度：6.7
  匹配主题：foundation_model_agent
  中文摘要：Large language models can reason over biological knowledge, but they are not naturally equipped to work with quantitative omics measurements. Existing approaches either convert expression profiles into long textual repre...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [NutriVisRAG: Multimodal Exemplar Grounding for Nutrient Estimation with Vision-Language Models](http://arxiv.org/abs/2611.08054v1)
  来源：arXiv | 日期：2026-11-05 | 相关度：7.5 | 新颖度：7.3
  匹配主题：foundation_model_agent
  中文摘要：Diet is a major determinant of health, yet accurate dietary assessment from free-living meal images remains challenging. Existing retrieval-based Vision-Language Model (VLM) approaches to nutrient estimation typically re...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multimodal Graph RAG for Long-range Visually Rich Document Understanding](http://arxiv.org/abs/2606.28780v2)
  来源：arXiv | 日期：2026-06-27 | 相关度：7.5 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Multimodal large language models (MLLMs) are widely applied to visual document understanding. However, comprehending long documents remains an issue by the limited context window. Though recent multimodal retrieval-augme...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [ImagineAgent: What if Agents Could Imagine? Reinforcing Open-Vocabulary HOI Comprehension through Generation](http://arxiv.org/abs/2602.11499v3)
  来源：arXiv | 日期：2026-02-12 | 相关度：7.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Multimodal Large Language Models have shown promising capabilities in bridging visual and textual reasoning, yet their reasoning capabilities in Open-Vocabulary Human-Object Interaction (OV-HOI) are limited by cross-moda...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic Discovery Transfer Enables Cross-Cancer Discovery at Scale](https://www.biorxiv.org/content/10.64898/2026.10.28.762506v2)
  来源：bioRxiv | 日期：2026-11-03 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Cancer research generates tens of thousands of studies each year, yet whether a published finding holds in another cancer type or patient population is rarely tested as doing so is labor-intensive and difficult to scale....
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond Visual Boundaries: Rethinking Scene Segmentation for Movie RAG](http://arxiv.org/abs/2608.28699v2)
  来源：arXiv | 日期：2026-08-27 | 相关度：6.8 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Understanding long-form video remains a fundamental challenge for multimodal large language models (MLLMs). Sparse frame sampling fails to capture fine-grained visual details, while dense sampling quickly exceeds context...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AromaGen: Interactive Generation of Rich Olfactory Experiences with Multimodal Language Models](http://arxiv.org/abs/2604.01650v5)
  来源：arXiv | 日期：2026-04-02 | 相关度：6.8 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Smell's connections with food, memory, and social experience have motivated researchers to bring olfaction into interactive systems. Multimodal AI opens new possibilities for generating smells from natural language, yet ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ZeroRAG: Adaptive Semantic Peer Routing for Decentralized Retrieval-Augmented Generation](http://arxiv.org/abs/2611.07928v1)
  来源：arXiv | 日期：2026-11-05 | 相关度：6.55 | 新颖度：6.78
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) is a standard approach to enhance the reliability of large language model (LLM) outputs by retrieving documents relevant to a query and supplying them in the LLM prompt. Today's RAG s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Trustworthy RAG: An Evaluation Agent for Detecting Misinformation and Knowledge Poisoning in Generative AI Systems](http://arxiv.org/abs/2608.21095v2)
  来源：arXiv | 日期：2026-08-21 | 相关度：6.55 | 新颖度：1.7
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) grounds Large Language Model (LLM) outputs in external knowledge, but RAG systems usually trust whatever they retrieve, creating a Security-Reliability Gap: high semantic relevance do...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Building Barricades: Red-Teaming Agentic Biosynthesis Planning](http://arxiv.org/abs/2611.08218v1)
  来源：arXiv | 日期：2026-11-05 | 相关度：6.45 | 新颖度：6.87
  匹配主题：foundation_model_agent
  中文摘要：The rapid democratization of biotechnology, enhanced by large language models (LLMs) and agentic software, is eroding longstanding barriers that have limited biosynthesis planning to experts. We present BioBulbul, an age...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PREBA: Surgical Duration Prediction via PCA-Weighted Retrieval-Augmented LLMs and Bayesian Averaging Aggregation](http://arxiv.org/abs/2603.13275v4)
  来源：arXiv | 日期：2026-02-27 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Accurate prediction of surgical duration is pivotal for hospital resource management. Although recent supervised learning approaches, from machine learning (ML) to fine-tuned large language models (LLMs), have shown stro...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic Literature Extraction Augments Targeted Protein Degradation Databases](http://arxiv.org/abs/2605.11221v2)
  来源：arXiv | 日期：2026-05-11 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Predictive models in medicinal chemistry depend on structured assay data locked in primary publications. This bottleneck is acute in targeted protein degradation (TPD), where each assay record must combine compound ident...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CacheGraft: Enhancing Retrieval-Augmented Generation via Latent-Space Document Enrichment](http://arxiv.org/abs/2611.07393v1)
  来源：arXiv | 日期：2026-11-05 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Recent work in machine learning has demonstrated that transformer-based language model agents can communicate state not only through text, but also directly in latent space via key-value (KV) caches. In this paper, we ar...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MIND: AI Co-Scientist for Material Research](http://arxiv.org/abs/2604.13699v2)
  来源：arXiv | 日期：2026-04-15 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have enabled agentic AI systems for scientific discovery, but most approaches remain limited to textbased reasoning without automated experimental verification. We propose MIND, an LLM-driven...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [AssameseLM-E2B: An Open-Weight Assamese Language Model for Efficient Consumer-Grade Deployment](http://arxiv.org/abs/2611.06170v1)
  来源：arXiv | 日期：2026-11-04 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：While Large Language Models (LLMs) excel in high-resource languages, their performance often degrades in low-resource languages due to tokenization inefficiencies, generative instability, and linguistic interference. Thi...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Learning inhibitor interactions from protein deep mutational scanning data and deep learning models](https://www.biorxiv.org/content/10.64898/2026.11.01.763444v1)
  来源：bioRxiv | 日期：2026-11-03 | 相关度：5.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in protein language models, geometric deep learning, and structure prediction frameworks have the potential to accelerate computational drug discovery. However, it remains unclear how well these methods g...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Protein large language model-assisted one-to-one gene homology mapping in cross-species single-cell transcriptome integration.](https://pubmed.ncbi.nlm.nih.gov/42855280/)
  来源：PubMed | 日期：2026-11-03 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Cross-species integration of single-cell transcriptomes requires establishing gene correspondences to enable comparative analysis of expression profiles across organisms. Current approaches predominantly rely on Ensembl ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RIVER: Evidence-guided multi-agent retrieval for enzyme--reaction discovery](http://arxiv.org/abs/2611.07757v1)
  来源：arXiv | 日期：2026-11-05 | 相关度：5.75 | 新颖度：6.61
  匹配主题：foundation_model_agent
  中文摘要：Enzyme function annotation and the identification of candidate enzymes for a given reaction are essential steps in connecting genomic information to biochemical reaction networks. However, existing methods rely on sequen...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [VIGAT: VLM-guided gene activity quantification from single-cell ATAC-seq](https://www.biorxiv.org/content/10.64898/2026.10.16.759698v1)
  来源：bioRxiv | 日期：2026-11-03 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Summary: Gene activity quantification from single-cell ATAC-seq is challenging because genomic regions informative of cell identity can vary across genes and tissues, while broadly accessible regions may provide limited ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Future directions and challenges of drug development and non-human primate models.](https://pubmed.ncbi.nlm.nih.gov/42988150/)
  来源：PubMed | 日期：2026-11-05 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Gene and cell therapy are transforming therapeutic approaches for genetic diseases and malignancies. This review examines the current role and future directions of non-human primate (NHP) models in preclinical safety eva...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Figure format and the accuracy of AI-assisted reconstruction of Kaplan-Meier survival data](https://www.medrxiv.org/content/10.64898/2026.11.03.26367147v1)
  来源：medRxiv | 日期：2026-11-05 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Reconstructing participant-level data from published Kaplan-Meier curves supports meta-analysis and other secondary survival analyses when original trial records are unavailable. Researchers may use original PDF figures ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [CLEAR: Structured Specifications for Controllable Long-Horizon ML Research Engineering](http://arxiv.org/abs/2611.06263v1)
  来源：arXiv | 日期：2026-11-04 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Large language model (LLM) agents are increasingly being used to automate machine learning (ML) research workflows, ranging from code development and experiment execution to research reproduction and scientific discovery...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CONFIRM: Governing Scientific Reporting for Trustworthy Agentic Neuroimaging](http://arxiv.org/abs/2611.01449v2)
  来源：arXiv | 日期：2026-11-01 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large language model (LLM) agents can autonomously run neuroimaging analyses from research questions to reported findings. Existing agentic systems use tools to check that code runs and reported values match its output, ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics](http://arxiv.org/abs/2606.11833v2)
  来源：arXiv | 日期：2026-06-10 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Flow matching and diffusion models enable conditional generation across domains ranging from images to proteins, with recent extensions to out-of-distribution contexts. Yet generative models of neural time series have la...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond Isolated Dots: Benchmarking Structured Table Construction as Deep Knowledge Extraction](http://arxiv.org/abs/2507.16271v3)
  来源：arXiv | 日期：2025-07-22 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly expected to extract and synthesize structured information from complex real-world documents, yet they typically produce unstructured, hard-to-verify paragraph-style outputs. ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [When Reviews Are Scarce: Structure-Aware Review Imputation for Recommendation in Realistic Sparse Review Settings](http://arxiv.org/abs/2508.01128v2)
  来源：arXiv | 日期：2025-08-02 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Textual reviews enrich recommender systems with fine-grained preference signals and enhanced explainability. However, in real-world scenarios, users rarely leave reviews, resulting in severe sparsity that undermines the ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RecoAtlas: A Benchmark and RL Environment for LLM Recommendation Agents Optimizing Set-Level Utility](http://arxiv.org/abs/2605.18805v2)
  来源：arXiv | 日期：2026-05-11 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：LLM recommender agents increasingly produce structured reports: sets of items accompanied by natural-language justifications. Yet existing benchmarks often focus on reranking small candidate sets or judging reports prima...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Knowledge Database of Physical Activity Interventions for Hypertension using Large Language Models](https://www.medrxiv.org/content/10.64898/2026.10.22.26366246v2)
  来源：medRxiv | 日期：2026-11-03 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Physical exercise lowers blood pressure, but guidelines provide broad recommendations that rarely account for age, comorbidities, medications and hypertension severity. A structured, queryable resource of exercise interv...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Reasoning over Non-Parametric Memory in Multilingual LLMs: A Cognitive-Based Analysis of Relational Knowledge](http://arxiv.org/abs/2611.06715v1)
  来源：arXiv | 日期：2026-11-04 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) assumes that language models can reason over relations stated in their context rather than fall back on associations memorized during pretraining. We study this evidence-conditioned r...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [vLLM Hook v1: A Plug-in for Programming Model Internals on vLLM](http://arxiv.org/abs/2603.06588v2)
  来源：arXiv | 日期：2026-02-02 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Modern artificial intelligence models are deployed on inference engines to optimize runtime efficiency and resource allocation, particularly for transformer-based large language models. The vLLM project is a major open-s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CytoBERT: A Foundation Model for Cytometry Data](http://arxiv.org/abs/2608.14414v2)
  来源：arXiv | 日期：2026-08-14 | 相关度：2.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：Cytometry measures the complex characteristics of single cells (e.g., counts and protein expression of immune cells) and is widely used across immunological research and clinical settings. However, cytometry data is high...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization](http://arxiv.org/abs/2611.08483v1)
  来源：arXiv | 日期：2026-11-05 | 相关度：1.4 | 新颖度：7.35
  匹配主题：未命中具体主题
  中文摘要：LLM-guided evolutionary search uses AI agents to improve programs for mathematical and computational problems by iteratively refining solutions and combining high-scoring methods. However, the process is often slow becau...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EMA: Approximate Nearest Neighbor Search with General Attribute Filtering and Dynamic Updates](http://arxiv.org/abs/2606.00734v2)
  来源：arXiv | 日期：2026-05-30 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Filtering approximate nearest neighbor search (Filtering ANNS) retrieves approximate nearest neighbors subject to attribute constraints in applications such as recommendation, retrieval-augmented generation (RAG), and LL...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HyperSU: Corpus-Driven Semantic-Unit Hypergraph for Retrieval-Augmented Generation](http://arxiv.org/abs/2606.28351v3)
  来源：arXiv | 日期：2026-06-03 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Recent Hypergraph-based retrieval-augmented generation (HyperRAG) methods use hyper edges to connect multiple entities simultaneously, enabling more efficient multi-entity evidence organization than pairwise graph struct...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [QueryFlow: Multi-Hop Graph Retrieval with Adaptive Query Evolution](http://arxiv.org/abs/2611.04625v1)
  来源：arXiv | 日期：2026-11-03 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Multi-hop retrieval-augmented generation (RAG) supports Web information seeking and fact verification by recovering complementary evidence across related pages within a limited retrieval budget. Scoring evidence independ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HYPIC: Position-Independent Caching for Hybrid-Attention LLM Serving](http://arxiv.org/abs/2607.01299v3)
  来源：arXiv | 日期：2026-07-01 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：In retrieval-augmented generation (RAG) and agentic LLM serving, prompts are assembled from multiple independent segments into long contexts, making prefill dominate the computation cost. To reduce this cost, position-in...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [EpiLens: Lightweight RAG for Epidemiological Knowledge Acquisition](http://arxiv.org/abs/2610.26730v2)
  来源：arXiv | 日期：2026-10-19 | 相关度：6.7 | 新颖度：0.25
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：To prepare for future outbreaks, researchers need to know what studies have been done and what data they use. Mapping a large literature by hand is slow, while large language models alone can misstate or conflate sources...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Signed but Steerable: Measuring and Closing the Text-Vector Integrity Gap in Offline Retrieval-Augmented Generation](http://arxiv.org/abs/2611.06498v1)
  来源：arXiv | 日期：2026-11-04 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Offline retrieval-augmented generation (RAG) on edge devices is updated through signed knowledge packs that carry text and precomputed embedding vectors. A signature proves who published a pack, not that its vectors enco...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [RAGCompass: Generalizable Retriever Routing via Reranking](http://arxiv.org/abs/2611.05596v1)
  来源：arXiv | 日期：2026-11-03 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Different retrievers exist for retrieval-augmented generation, yet none performs best for all queries. Therefore, the key question is: given a query and retrieved passages from different retrievers, which one is most sui...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Molecular Prior Networks](http://arxiv.org/abs/2611.05103v1)
  来源：arXiv | 日期：2026-11-03 | 相关度：1.7 | 新颖度：1.75
  匹配主题：未命中具体主题
  中文摘要：Predicting affinity between small molecules and their protein targets remains one of the central problems in drug discovery. Due to the substantial cost of wet-lab experiments, machine learning models of drug-target affi...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Embodied RAG++: Retrieval-Augmented Generation From What Exists to What Works in Embodied Scenes](http://arxiv.org/abs/2611.07517v1)
  来源：arXiv | 日期：2026-11-05 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：To serve a request in a human environment, a robot system must find an object that satisfies a functional requirement and a robot that can feasibly reach it. Scene graphs record which objects exist and where, but they of...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Ablating Design Choices for Protein Ensemble Generators Across Structural Regimes](http://arxiv.org/abs/2611.05055v1)
  来源：arXiv | 日期：2026-11-03 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Generative models of protein conformational ensembles inherit much of their design from structure prediction for folded proteins. Ordered and disordered proteins, however, occupy distinct structural regimes, and we inves...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Parameter-Efficient Adaptation of Protein Language Models for Dual-Target Antimicrobial Peptide Discovery Under Strict Homology Constraints](https://www.biorxiv.org/content/10.64898/2026.10.31.763384v1)
  来源：bioRxiv | 日期：2026-11-03 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：The worldwide escalation of antimicrobial resistance (AMR) poses a severe challenge to modern public health, necessitating novel classes of therapeutic agents. Antimicrobial peptides (AMPs) represent highly promising alt...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [FedEpitope: Parameter-Efficient Federated Protein Language Models for Linear B-Cell Epitope Prediction](https://www.biorxiv.org/content/10.64898/2026.10.31.763304v1)
  来源：bioRxiv | 日期：2026-11-03 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Linear B-cell epitopes are antigenic regions recognised by antibodies that play crucial roles in vaccine development, antibody production, and other therapeutic applications.Their prediction can support peptide-based vac...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [DB-ATRG: The Density and BI-RADS-Aware Triage and Automatic Report Generation System for Mammography](https://www.medrxiv.org/content/10.64898/2026.07.22.26358655v2)
  来源：medRxiv | 日期：2026-11-04 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：针对乳腺癌筛查量增加导致的放射科医生短缺及传统先来先服务（FIFO）队列无法优先处理紧急病例的问题，本研究提出了DB-ATRG框架。该框架利用DMID数据集，通过QLoRA技术微调了拥有40亿参数的MedGemma 1.5视觉语言模型，实现了诊断文本的自动生成与基于风险的病例分诊。DB-ATRG包含双阶段分诊算法：首先标记极高腺体密度（ACR D类）病例以进行补充筛查，随后利用累积紧急评分对剩余病例动态排序。实验结果显示，DB-ATRG...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [HERIT: Enabling Global Access to Hanja-to-English Historical Translation by Mitigating Temporal Bias](http://arxiv.org/abs/2611.04949v1)
  来源：arXiv | 日期：2026-11-03 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Historical archives are invaluable for multidisciplinary research but remain inaccessible globally due to severe language barriers. While manual translation is prohibitively expensive and time-consuming, simply applying ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Physical Diffusion Policy via MPM-Guided 3D Gaussian Simulation](http://arxiv.org/abs/2611.04493v1)
  来源：arXiv | 日期：2026-11-03 | 相关度：2.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Learning robust manipulation policies for diverse everyday objects remains challenging because objects with different materials exhibit distinct deformation and contact dynamics. While diffusion policies provide a powerf...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AI-Guided Structure-Aware Modeling and Thermal Proteomics Reveal Direct Demethylzeylasteral-ACLY Interaction](https://www.biorxiv.org/content/10.64898/2026.04.07.717093v3)
  来源：bioRxiv | 日期：2026-11-03 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Identifying the direct molecular targets of bioactive natural products remains a central challenge in chemical biology. Here we present an integrated experimental-computational framework, that combines matrix-augmented t...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Bridging the Modality Bottleneck in Pathology MIL through Molecularly Guided Feature Adaptation](http://arxiv.org/abs/2605.16392v2)
  来源：arXiv | 日期：2026-05-12 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Multiple instance learning (MIL) is the dominant framework for whole-slide image analysis in computational pathology, typically combining a frozen patch encoder, a projection layer, and a slide-level aggregator. While en...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Genome-Factory: A Library for Tuning, Deploying, and Interpreting Genomic Foundation Models](http://arxiv.org/abs/2509.12266v3)
  来源：arXiv | 日期：2025-09-13 | 相关度：0.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：We introduce Genome-Factory, the first integrated Python library for tuning, deploying, and interpreting genomic foundation models. Our core contribution is to simplify and unify the workflow for genomic model developmen...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [The Little Scientist: What Does the Scientific Method Buy an LLM Agent?](http://arxiv.org/abs/2608.16951v2)
  来源：arXiv | 日期：2026-08-16 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Scientific discovery emerges from cycles of hypothesis, implementation, empirical testing, and feedback. Can this process be automated? We approach automated algorithm design through the lens of the scientific method, wh...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Weaver: Weaving Preference Evidence through Incremental Reasoning for Personalized Retrieval-Augmented Generation](http://arxiv.org/abs/2611.05900v1)
  来源：arXiv | 日期：2026-11-04 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Personalized retrieval-augmented generation requires extracting and applying user preferences from extended interaction histories. This task is challenging because preference evidence is scattered across past conversatio...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Conversational Multi-Agentic Network-Driven Disease Module Identification and Drug Repurposing Prediction With ChatDRex: Platform Development Study.](https://pubmed.ncbi.nlm.nih.gov/42976355/)
  来源：PubMed | 日期：2026-11-03 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Repurposing approved drugs offers a time- and cost-effective alternative to traditional drug development. However, in silico prediction of repurposing candidates is challenging and requires the effective collaboration of...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [BioResearchBench: 50 Long Horizon Biological Research Tasks](https://www.biorxiv.org/content/10.64898/2026.10.28.762290v1)
  来源：bioRxiv | 日期：2026-11-03 | 相关度：1.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：AI models are used in biology research to study disease mechanisms, discover potential treatments, analyze experimental data, troubleshoot problems, and plan next steps. Useful assistance depends on working with data in ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Spatial omics in cancer: a review of computational approaches and vision of AI-driven analysis.](https://pubmed.ncbi.nlm.nih.gov/42982206/)
  来源：PubMed | 日期：2026-11-04 | 相关度：1.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Predicting patient response to cancer treatments remains a challenge due to tumor heterogeneity and complex tumor microenvironments (TMEs). Modern spatial genomics technologies enable gene expression profiling alongside ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
