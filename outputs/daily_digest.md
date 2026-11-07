# 每日论文监控日报 (2026-11-07)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 40 篇新论文。

## 抓取状态

- arXiv：成功，命中 30 篇
- PubMed：成功，命中 61 篇
- bioRxiv：成功，命中 19 篇
- medRxiv：成功，命中 15 篇

## 最值得看

### Foundation Model / Agent

- [Roost: Avian Influenza Host Genomics Resource](https://www.biorxiv.org/content/10.64898/2026.11.01.763514v1)
  来源：bioRxiv | 日期：2026-11-04 | 相关度：9.4 | 新颖度：5.5
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Highly pathogenic avian influenza (HPAI) causes mass mortality in poultry and wildlife, and puts already threatened species at further risk. Understanding differences in host susceptibility requires evidence currently sc...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [MicrobeRT: A Framework and Suite of Fine-tuned Language Models for Genomic Sequences](https://www.biorxiv.org/content/10.64898/2026.11.03.763945v1)
  来源：bioRxiv | 日期：2026-11-04 | 相关度：10.0 | 新颖度：6.75
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent, application_monitoring
  中文摘要：Accurate and reproducible metagenomic analysis is essential for effective infectious disease surveillance. Targeted diagnostics such as culturing, antigen assays, and multiplex PCR panels identify only predefined organis...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [XAMPGen: An Interpretable SI Pipeline For Novel Antimicrobial Peptide Discovery](https://www.biorxiv.org/content/10.64898/2026.11.03.764041v1)
  来源：bioRxiv | 日期：2026-11-04 | 相关度：9.35 | 新颖度：5.5
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Antimicrobial peptides (AMPs) are short peptides with a broad spectrum of activity against bacterial pathogens, representing a promising avenue for combating the growing threat of antibiotic resistance. This study focuse...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Protein language models learn the underlying accessibility of mutations alongside protein fitness landscapes](https://www.biorxiv.org/content/10.64898/2026.07.06.736753v2)
  来源：bioRxiv | 日期：2026-11-04 | 相关度：8.65 | 新颖度：5.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Protein language models (PLMs) score the effects of amino acid replacements as pseudo-probabilities, which are widely utilised to map protein fitness landscapes. However, because their training data relies on natural ami...
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
  来源：medRxiv | 日期：2026-11-06 | 相关度：7.15 | 新颖度：5.75
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

- [Agentic Literature Extraction Augments Targeted Protein Degradation Databases](http://arxiv.org/abs/2605.11221v2)
  来源：arXiv | 日期：2026-05-11 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Predictive models in medicinal chemistry depend on structured assay data locked in primary publications. This bottleneck is acute in targeted protein degradation (TPD), where each assay record must combine compound ident...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [AssameseLM-E2B: An Open-Weight Assamese Language Model for Efficient Consumer-Grade Deployment](http://arxiv.org/abs/2611.06170v1)
  来源：arXiv | 日期：2026-11-04 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：While Large Language Models (LLMs) excel in high-resource languages, their performance often degrades in low-resource languages due to tokenization inefficiencies, generative instability, and linguistic interference. Thi...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Massively parallel quantification and prediction of monomeric protein yield in Escherichia coli](https://www.biorxiv.org/content/10.64898/2026.11.02.763507v1)
  来源：bioRxiv | 日期：2026-11-04 | 相关度：5.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Obtaining sufficient quantities of purified proteins in their intended molecular states is essential for biological research and protein engineering. Advances in computational protein design have expanded the functional ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [GPBench: A benchmark framework for genomic prediction](https://www.biorxiv.org/content/10.64898/2026.10.31.762999v1)
  来源：bioRxiv | 日期：2026-11-04 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Genomic prediction (GP) has emerged as a powerful data mining strategy for disease risk assessment and molecular breeding. GP leverages genome-wide genetic variations and phenotypic information through a computational mo...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Decoding Cell-type Specific Gene Regulation with CellReg3D by Integrating DNA Large Language Models and 3D Genome Structure](https://www.biorxiv.org/content/10.64898/2026.11.01.763421v1)
  来源：bioRxiv | 日期：2026-11-04 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Gene regulation is a core biological mechanism crucial for organismal growth and development. Recent advances in deep learning, coupled with increasing computational resources, have enabled large-scale modelling of gene ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Figure format and the accuracy of AI-assisted reconstruction of Kaplan-Meier survival data](https://www.medrxiv.org/content/10.64898/2026.11.03.26367147v1)
  来源：medRxiv | 日期：2026-11-05 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Reconstructing participant-level data from published Kaplan-Meier curves supports meta-analysis and other secondary survival analyses when original trial records are unavailable. Researchers may use original PDF figures ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Auditing Biomedical Literature with Blinded AI Peer Review: Where Peer Review Works, Where It Fails, and How to Strengthen It](https://www.biorxiv.org/content/10.64898/2026.11.02.763753v1)
  来源：bioRxiv | 日期：2026-11-04 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Biomedical publishing has grown more than elevenfold since 1991, outstripping human peer review. Unblinded language models cannot audit this literature objectively because they recognize famous authors and journals from ...
  为什么值得看：bioRxiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Building Barricades: Red-Teaming Agentic Biosynthesis Planning](http://arxiv.org/abs/2611.08218v1)
  来源：arXiv | 日期：2026-11-05 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：The rapid democratization of biotechnology, enhanced by large language models (LLMs) and agentic software, is eroding longstanding barriers that have limited biosynthesis planning to experts. We present BioBulbul, an age...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CLEAR: Structured Specifications for Controllable Long-Horizon ML Research Engineering](http://arxiv.org/abs/2611.06263v1)
  来源：arXiv | 日期：2026-11-04 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Large language model (LLM) agents are increasingly being used to automate machine learning (ML) research workflows, ranging from code development and experiment execution to research reproduction and scientific discovery...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CacheGraft: Enhancing Retrieval-Augmented Generation via Latent-Space Document Enrichment](http://arxiv.org/abs/2611.07393v1)
  来源：arXiv | 日期：2026-11-05 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Recent work in machine learning has demonstrated that transformer-based language model agents can communicate state not only through text, but also directly in latent space via key-value (KV) caches. In this paper, we ar...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MIND: AI Co-Scientist for Material Research](http://arxiv.org/abs/2604.13699v2)
  来源：arXiv | 日期：2026-04-15 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have enabled agentic AI systems for scientific discovery, but most approaches remain limited to textbased reasoning without automated experimental verification. We propose MIND, an LLM-driven...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics](http://arxiv.org/abs/2606.11833v2)
  来源：arXiv | 日期：2026-06-10 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Flow matching and diffusion models enable conditional generation across domains ranging from images to proteins, with recent extensions to out-of-distribution contexts. Yet generative models of neural time series have la...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Reasoning over Non-Parametric Memory in Multilingual LLMs: A Cognitive-Based Analysis of Relational Knowledge](http://arxiv.org/abs/2611.06715v1)
  来源：arXiv | 日期：2026-11-04 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) assumes that language models can reason over relations stated in their context rather than fall back on associations memorized during pretraining. We study this evidence-conditioned r...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Knowledge Database of Physical Activity Interventions for Hypertension using Large Language Models](https://www.medrxiv.org/content/10.64898/2026.10.22.26366246v3)
  来源：medRxiv | 日期：2026-11-06 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Physical exercise lowers blood pressure, but guidelines provide broad recommendations that rarely account for age, comorbidities, medications and hypertension severity. A structured, queryable resource of exercise interv...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EIN-RECAP: Evidence-Grounded Multi-Agent Summarization and Retrieval of Infectious-Disease Expert Discussions](https://www.medrxiv.org/content/10.64898/2026.11.05.26367381v1)
  来源：medRxiv | 日期：2026-11-06 | 相关度：2.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Infectious disease experts exchange practical knowledge through clinical discussions, but identifying relevant information across years of conversations is difficult. These discussions often contain differing opinions an...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CytoBERT: A Foundation Model for Cytometry Data](http://arxiv.org/abs/2608.14414v2)
  来源：arXiv | 日期：2026-08-14 | 相关度：2.4 | 新颖度：1.5
  匹配主题：未命中具体主题
  中文摘要：Cytometry measures the complex characteristics of single cells (e.g., counts and protein expression of immune cells) and is widely used across immunological research and clinical settings. However, cytometry data is high...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EMA: Approximate Nearest Neighbor Search with General Attribute Filtering and Dynamic Updates](http://arxiv.org/abs/2606.00734v2)
  来源：arXiv | 日期：2026-05-30 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Filtering approximate nearest neighbor search (Filtering ANNS) retrieves approximate nearest neighbors subject to attribute constraints in applications such as recommendation, retrieval-augmented generation (RAG), and LL...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HyperSU: Corpus-Driven Semantic-Unit Hypergraph for Retrieval-Augmented Generation](http://arxiv.org/abs/2606.28351v3)
  来源：arXiv | 日期：2026-06-03 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Recent Hypergraph-based retrieval-augmented generation (HyperRAG) methods use hyper edges to connect multiple entities simultaneously, enabling more efficient multi-entity evidence organization than pairwise graph struct...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HYPIC: Position-Independent Caching for Hybrid-Attention LLM Serving](http://arxiv.org/abs/2607.01299v3)
  来源：arXiv | 日期：2026-07-01 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：In retrieval-augmented generation (RAG) and agentic LLM serving, prompts are assembled from multiple independent segments into long contexts, making prefill dominate the computation cost. To reduce this cost, position-in...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization](http://arxiv.org/abs/2611.08483v1)
  来源：arXiv | 日期：2026-11-05 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：LLM-guided evolutionary search uses AI agents to improve programs for mathematical and computational problems by iteratively refining solutions and combining high-scoring methods. However, the process is often slow becau...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Signed but Steerable: Measuring and Closing the Text-Vector Integrity Gap in Offline Retrieval-Augmented Generation](http://arxiv.org/abs/2611.06498v1)
  来源：arXiv | 日期：2026-11-04 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Offline retrieval-augmented generation (RAG) on edge devices is updated through signed knowledge packs that carry text and precomputed embedding vectors. A signature proves who published a pack, not that its vectors enco...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Embodied RAG++: Retrieval-Augmented Generation From What Exists to What Works in Embodied Scenes](http://arxiv.org/abs/2611.07517v1)
  来源：arXiv | 日期：2026-11-05 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：To serve a request in a human environment, a robot system must find an object that satisfies a functional requirement and a robot that can feasibly reach it. Scene graphs record which objects exist and where, but they of...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Few-shot regulatory sequence design with a genomic language model](https://www.biorxiv.org/content/10.64898/2026.10.28.762639v2)
  来源：bioRxiv | 日期：2026-11-04 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：A central challenge in generative biology is translating knowledge learned from natural sequences and experiments into designs with desired functions. In-context learning (ICL) is an emergent capability of large language...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RIVER: Evidence-guided multi-agent retrieval for enzyme--reaction discovery](http://arxiv.org/abs/2611.07757v1)
  来源：arXiv | 日期：2026-11-05 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Enzyme function annotation and the identification of candidate enzymes for a given reaction are essential steps in connecting genomic information to biochemical reaction networks. However, existing methods rely on sequen...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [DB-ATRG: The Density and BI-RADS-Aware Triage and Automatic Report Generation System for Mammography](https://www.medrxiv.org/content/10.64898/2026.07.22.26358655v2)
  来源：medRxiv | 日期：2026-11-04 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：针对乳腺癌筛查量增加导致的放射科医生短缺及传统先来先服务（FIFO）队列无法优先处理紧急病例的问题，本研究提出了DB-ATRG框架。该框架利用DMID数据集，通过QLoRA技术微调了拥有40亿参数的MedGemma 1.5视觉语言模型，实现了诊断文本的自动生成与基于风险的病例分诊。DB-ATRG包含双阶段分诊算法：首先标记极高腺体密度（ACR D类）病例以进行补充筛查，随后利用累积紧急评分对剩余病例动态排序。实验结果显示，DB-ATRG...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Future directions and challenges of drug development and non-human primate models.](https://pubmed.ncbi.nlm.nih.gov/42988150/)
  来源：PubMed | 日期：2026-11-05 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Gene and cell therapy are transforming therapeutic approaches for genetic diseases and malignancies. This review examines the current role and future directions of non-human primate (NHP) models in preclinical safety eva...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Spectral Adaptive Repositioning for Flow-Based Single-Cell Perturbation Modeling](https://www.biorxiv.org/content/10.64898/2026.11.02.763678v1)
  来源：bioRxiv | 日期：2026-11-04 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Predicting transcriptome-wide cellular responses to genetic and biomolecular perturbations is central to functional genomics and therapeutic target discovery. Existing methods assign gene positional encodings derived fro...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Genome-Factory: A Library for Tuning, Deploying, and Interpreting Genomic Foundation Models](http://arxiv.org/abs/2509.12266v3)
  来源：arXiv | 日期：2025-09-13 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：We introduce Genome-Factory, the first integrated Python library for tuning, deploying, and interpreting genomic foundation models. Our core contribution is to simplify and unify the workflow for genomic model developmen...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Spatial omics in cancer: a review of computational approaches and vision of AI-driven analysis.](https://pubmed.ncbi.nlm.nih.gov/42982206/)
  来源：PubMed | 日期：2026-11-04 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Predicting patient response to cancer treatments remains a challenge due to tumor heterogeneity and complex tumor microenvironments (TMEs). Modern spatial genomics technologies enable gene expression profiling alongside ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
