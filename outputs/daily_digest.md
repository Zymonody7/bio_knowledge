# 每日论文监控日报 (2026-11-08)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 27 篇新论文。

## 抓取状态

- arXiv：成功，命中 12 篇
- PubMed：成功，命中 43 篇
- bioRxiv：成功，命中 21 篇
- medRxiv：成功，命中 11 篇

## 最值得看

### 数据集 / Benchmark

- [A protein language model for domain, functional site, and variant effect prediction](https://www.biorxiv.org/content/10.64898/2026.11.03.764008v1)
  来源：bioRxiv | 日期：2026-11-05 | 相关度：9.55 | 新颖度：6.25
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Protein sequence databases are growing far faster than experimentally curated annotations, limiting functional interpretation of newly identified proteins and coding variants. We developed PALM, a protein annotation lang...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Language-guided domain adaptation improves protein sequence rep-resentations for antimicrobial resistance analysis](https://www.biorxiv.org/content/10.64898/2026.11.04.764426v1)
  来源：bioRxiv | 日期：2026-11-05 | 相关度：10.0 | 新颖度：5.5
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent, application_monitoring
  中文摘要：Antimicrobial resistance (AMR), particularly antibiotic resistance in bacterial pathogens, complicates infectious disease management. Because bacterial resistance is often mediated by protein functions, including antibio...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [Thalamus-Reasoning: A Multimodal Large Language Model for Multi-Sample Omics Reasoning](http://arxiv.org/abs/2605.06728v3)
  来源：arXiv | 日期：2026-05-07 | 相关度：8.9 | 新颖度：1.7
  匹配主题：foundation_model_agent
  中文摘要：Large language models can reason over biological knowledge, but they are not naturally equipped to work with quantitative omics measurements. Existing approaches either convert expression profiles into long textual repre...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multi-agent LLM teams improve differential recall on curated cases but underperform on emergency working-label matching: a two-cohort, two-family evaluation](https://www.medrxiv.org/content/10.64898/2026.09.24.26363897v4)
  来源：medRxiv | 日期：2026-11-06 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Background. Whether multi-agent large language model (LLM) pipelines help, add nothing, or underperform a single call may depend on the input and scoring contract rather than the architecture; these boundary conditions a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multimodal Graph RAG for Long-range Visually Rich Document Understanding](http://arxiv.org/abs/2606.28780v2)
  来源：arXiv | 日期：2026-06-27 | 相关度：7.5 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Multimodal large language models (MLLMs) are widely applied to visual document understanding. However, comprehending long documents remains an issue by the limited context window. Though recent multimodal retrieval-augme...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [NutriVisRAG: Multimodal Exemplar Grounding for Nutrient Estimation with Vision-Language Models](http://arxiv.org/abs/2611.08054v1)
  来源：arXiv | 日期：2026-11-05 | 相关度：7.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Diet is a major determinant of health, yet accurate dietary assessment from free-living meal images remains challenging. Existing retrieval-based Vision-Language Model (VLM) approaches to nutrient estimation typically re...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic Pipeline for Large-Scale Clinical Data Queries in Enterprise Electronic Health Records](https://www.medrxiv.org/content/10.64898/2026.11.05.26367378v1)
  来源：medRxiv | 日期：2026-11-06 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Using electronic health record (EHR) data to answer clinical research questions is challenging. It requires understanding the research question, finding relevant information across different sources, and combining that i...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond Visual Boundaries: Rethinking Scene Segmentation for Movie RAG](http://arxiv.org/abs/2608.28699v2)
  来源：arXiv | 日期：2026-08-27 | 相关度：6.8 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Understanding long-form video remains a fundamental challenge for multimodal large language models (MLLMs). Sparse frame sampling fails to capture fine-grained visual details, while dense sampling quickly exceeds context...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ZeroRAG: Adaptive Semantic Peer Routing for Decentralized Retrieval-Augmented Generation](http://arxiv.org/abs/2611.07928v1)
  来源：arXiv | 日期：2026-11-05 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) is a standard approach to enhance the reliability of large language model (LLM) outputs by retrieving documents relevant to a query and supplying them in the LLM prompt. Today's RAG s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Predicting dynamic expression patterns in budding yeast with a fungal DNA language model](https://www.biorxiv.org/content/10.1101/2025.09.19.677475v2)
  来源：bioRxiv | 日期：2026-11-05 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Predicting gene expression from DNA sequence remains challenging due to complex regulatory codes. We introduce a masked DNA language model pretrained on 165 fungal genomes related to budding yeast that learns conserved r...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Towards an analytical framework for investigating the neurophysiological influence of social context in speech perception](https://www.biorxiv.org/content/10.64898/2026.11.05.764590v1)
  来源：bioRxiv | 日期：2026-11-06 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Social information plays an important role in everyday speech communication, yet existing neurophysiological approaches provide limited means of isolating its contribution during naturalistic speech perception. Here, we ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RNA-X: Modeling RNA interactions to design binder RNA and simultaneously target multiple molecules of different types](https://www.biorxiv.org/content/10.1101/2025.11.24.690191v2)
  来源：bioRxiv | 日期：2026-11-05 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：RNA interactions with proteins, other RNA molecules, and DNA play essential roles in numerous cellular processes and underpin a wide range of therapeutic mechanisms. Consequently, modeling these interactions is critical ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [FeatureMAP enables network-guided interpretation of untargeted metabolomics](https://www.biorxiv.org/content/10.64898/2026.11.04.764165v1)
  来源：bioRxiv | 日期：2026-11-05 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Untargeted liquid chromatography-mass spectrometry (LC-MS) metabolomics generates thousands of features, but incomplete metabolite annotation and reliance on predefined pathways limit their biological interpretation. Her...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Towards Robust Automated Mouse Scratching Behavior Detection for Itch Research](https://www.biorxiv.org/content/10.64898/2026.10.12.758682v2)
  来源：bioRxiv | 日期：2026-11-05 | 相关度：6.8 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Quantification of mouse scratching behavior is essential for preclinical itch research. However, manual video annotation is labor-intensive, and automated detection remains challenging in terms of accuracy and generaliza...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [CauloBrowser 2.0: an AI powered update](https://www.biorxiv.org/content/10.64898/2026.11.05.764773v1)
  来源：bioRxiv | 日期：2026-11-06 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：CauloBrowser is a systems-biology database for Caulobacter crescentus that organizes the largest repository of experimental data for this model bacterium. The original CauloBrowser provided a web interface for accessing ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Protify: A Benchmarking Platform Revealing Task Dependence and Homology Leakage in Protein Language Model Evaluation](https://www.biorxiv.org/content/10.64898/2026.11.04.764373v1)
  来源：bioRxiv | 日期：2026-11-05 | 相关度：6.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Protein Language Models (pLMs) have become essential tools for computational protein analysis, and the rapid proliferation of architectures, training objectives, and pretraining corpora has produced a diverse and expandi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Figure format and the accuracy of AI-assisted reconstruction of Kaplan-Meier survival data](https://www.medrxiv.org/content/10.64898/2026.11.03.26367147v1)
  来源：medRxiv | 日期：2026-11-05 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Reconstructing participant-level data from published Kaplan-Meier curves supports meta-analysis and other secondary survival analyses when original trial records are unavailable. Researchers may use original PDF figures ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Translating chemical reactions into enzyme sequences enables formate dehydrogenase engineering](https://www.biorxiv.org/content/10.64898/2026.11.04.764151v1)
  来源：bioRxiv | 日期：2026-11-05 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Enzyme engineering has broad applications across chemistry and biotechnology but remains costly and susceptible to low success rates. Generative artificial intelligence can substantially expand the sequence space accessi...
  为什么值得看：bioRxiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Building Barricades: Red-Teaming Agentic Biosynthesis Planning](http://arxiv.org/abs/2611.08218v1)
  来源：arXiv | 日期：2026-11-05 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：The rapid democratization of biotechnology, enhanced by large language models (LLMs) and agentic software, is eroding longstanding barriers that have limited biosynthesis planning to experts. We present BioBulbul, an age...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DiverScan: attention-guided exploratory analysis of animal behaviour across diverse comparative experiments](https://www.biorxiv.org/content/10.64898/2026.10.01.755818v2)
  来源：bioRxiv | 日期：2026-11-05 | 相关度：5.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：High-throughput tracking yields rich time-series data of animal behaviour, yet extracting biological insight remains a bottleneck, even for simple control--treatment comparisons. Existing analyses struggle to pinpoint th...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Knowledge Database of Physical Activity Interventions for Hypertension using Large Language Models](https://www.medrxiv.org/content/10.64898/2026.10.22.26366246v3)
  来源：medRxiv | 日期：2026-11-06 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Physical exercise lowers blood pressure, but guidelines provide broad recommendations that rarely account for age, comorbidities, medications and hypertension severity. A structured, queryable resource of exercise interv...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CytoBERT: A Foundation Model for Cytometry Data](http://arxiv.org/abs/2608.14414v2)
  来源：arXiv | 日期：2026-08-14 | 相关度：2.4 | 新颖度：1.5
  匹配主题：未命中具体主题
  中文摘要：Cytometry measures the complex characteristics of single cells (e.g., counts and protein expression of immune cells) and is widely used across immunological research and clinical settings. However, cytometry data is high...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EIN-RECAP: Evidence-Grounded Multi-Agent Summarization and Retrieval of Infectious-Disease Expert Discussions](https://www.medrxiv.org/content/10.64898/2026.11.05.26367381v1)
  来源：medRxiv | 日期：2026-11-06 | 相关度：2.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Infectious disease experts exchange practical knowledge through clinical discussions, but identifying relevant information across years of conversations is difficult. These discussions often contain differing opinions an...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HyperSU: Corpus-Driven Semantic-Unit Hypergraph for Retrieval-Augmented Generation](http://arxiv.org/abs/2606.28351v3)
  来源：arXiv | 日期：2026-06-03 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Recent Hypergraph-based retrieval-augmented generation (HyperRAG) methods use hyper edges to connect multiple entities simultaneously, enabling more efficient multi-entity evidence organization than pairwise graph struct...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization](http://arxiv.org/abs/2611.08483v1)
  来源：arXiv | 日期：2026-11-05 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：LLM-guided evolutionary search uses AI agents to improve programs for mathematical and computational problems by iteratively refining solutions and combining high-scoring methods. However, the process is often slow becau...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [RIVER: Evidence-guided multi-agent retrieval for enzyme--reaction discovery](http://arxiv.org/abs/2611.07757v1)
  来源：arXiv | 日期：2026-11-05 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Enzyme function annotation and the identification of candidate enzymes for a given reaction are essential steps in connecting genomic information to biochemical reaction networks. However, existing methods rely on sequen...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Future directions and challenges of drug development and non-human primate models.](https://pubmed.ncbi.nlm.nih.gov/42988150/)
  来源：PubMed | 日期：2026-11-05 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Gene and cell therapy are transforming therapeutic approaches for genetic diseases and malignancies. This review examines the current role and future directions of non-human primate (NHP) models in preclinical safety eva...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。
