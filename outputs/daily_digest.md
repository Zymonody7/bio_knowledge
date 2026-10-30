# 每日论文监控日报 (2026-10-30)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 50 篇新论文。

## 抓取状态

- arXiv：成功，命中 43 篇
- PubMed：成功，命中 44 篇
- bioRxiv：成功，命中 12 篇
- medRxiv：成功，命中 13 篇

## 最值得看

### Foundation Model / Agent

- [Using iterative agentic retrieval-augmented generation to refine the risk of infection from social contexts during the COVID-19 pandemic: Development and Evaluation Study](https://www.medrxiv.org/content/10.64898/2026.10.28.26366693v1)
  来源：medRxiv | 日期：2026-10-29 | 相关度：8.1 | 新颖度：5.75
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Background: Contact tracing is crucial to limit pathogen transmission and to gather epidemiological data. However, despite machine learning optimizations, it remains time-consuming. Large language models have been used f...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [An Agentic AI Pipeline for an Evidence-Grounded Environmental Health Public Information System: Development and Evaluation](https://www.medrxiv.org/content/10.64898/2026.10.26.26366549v1)
  来源：medRxiv | 日期：2026-10-29 | 相关度：7.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Background: Existing environmental and health information systems typically provide isolated data streams, requiring users to interpret heterogeneous information sources without personalized guidance. Residents and healt...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 产品应用 / 监测落地

- [Beyond Blood Cultures and Echocardiography: Emerging Diagnostics for Infective Endocarditis.](https://pubmed.ncbi.nlm.nih.gov/42951945/)
  来源：PubMed | 日期：2026-10-29 | 相关度：10.0 | 新颖度：5.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent, application_monitoring
  中文摘要：Management of infective endocarditis (IE) is often confounded by the presence of prosthetic valves, transcatheter prostheses, and cardiovascular implantable electronic devices, as well as by changing epidemiologic risks ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Emerging advances in multimodal AI in cancer immunotherapy: from multi-scale data integration to clinical decision support.](https://pubmed.ncbi.nlm.nih.gov/42791141/)
  来源：PubMed | 日期：2026-10-30 | 相关度：7.8 | 新颖度：8.33
  匹配主题：foundation_model_agent
  中文摘要：Immunotherapy is increasingly reshaping the therapeutic landscape of clinical oncology by inducing effective tumor regression and durable responses in various types of human cancers. However, a substantial fraction of pa...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 可追踪

### Foundation Model / Agent

- [Richer database context improves LLM-generated EHR phenotyping algorithms](https://www.medrxiv.org/content/10.64898/2026.10.27.26366654v1)
  来源：medRxiv | 日期：2026-10-28 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Objective: To evaluate large language model (LLM) generation of type 2 diabetes (T2DM) phenotyping SQL and the effect of database implementation context. Materials and Methods: Eight publicly accessible LLM-based systems...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Hypergraph-Enhanced Evidence Selection for Long-Context Multimodal Document QA](http://arxiv.org/abs/2610.35542v2)
  来源：arXiv | 日期：2026-10-26 | 相关度：6.8 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Long-context multimodal document question answering (QA) has become an important yet challenging task for modern vision-language models (VLMs), as it requires reasoning over evidence dispersed across pages and modalities...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Adaptive Query Routing: A Tier-Based Framework for Hybrid Retrieval Across Financial, Legal, and Medical Documents](http://arxiv.org/abs/2604.14222v2)
  来源：arXiv | 日期：2026-04-14 | 相关度：6.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) has become the standard paradigm for grounding Large Language Model outputs in external knowledge. Lumer et al. presented the first systematic evaluation comparing vector-based agenti...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Post-Training Large Language Models with LLMON](http://arxiv.org/abs/2610.38120v1)
  来源：arXiv | 日期：2026-10-28 | 相关度：6.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) treat all context tokens uniformly, lacking explicit separation between executable instructions and passive data. This leads to prompt injection vulnerabilities, ambiguous instruction binding...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DeFT-RAG: Incrementally Decomposing Multi-Hop Questions into Self-Contained Sub-Questions with Reusable Answers](http://arxiv.org/abs/2610.37826v1)
  来源：arXiv | 日期：2026-10-27 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) lets a large language model (LLM) answer questions by retrieving relevant passages from a large corpus. However, RAG struggles with multi-hop questions, which require chaining facts s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [p-DCIM: A 28nm Probabilistic SRAM DCIM based Ising Machine for Near-Memory Context Selection in LLM-RAG Pipeline](http://arxiv.org/abs/2610.37033v1)
  来源：arXiv | 日期：2026-10-27 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：We present a fabricated SRAM DCIM Ising machine that performs set-level context selection for large language model (LLM) with retrieval-augmented generation (RAG). In RAG, the evidence-selection stage is increasingly del...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CauProphet: Teaching Agents to Develop Causal Cognition like Humans](http://arxiv.org/abs/2610.32477v2)
  来源：arXiv | 日期：2026-10-23 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language model (LLM) agents increasingly support long-horizon tasks by leveraging external memory and past experience. However, existing agents mainly retrieve records or summaries, lacking the ability to form and ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond LLM Wrappers: Context Engineering and the Three-Engine Architecture for Reliable Financial AI](http://arxiv.org/abs/2610.39230v1)
  来源：arXiv | 日期：2026-10-29 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Financial AI systems must support decision-bearing questions involving payments, collections, cash flow, and compliance while ensuring numerical accuracy, traceability, and auditability. Large language models (LLMs) enab...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MRC-MMAgent: Reinforcement Learning for Multi-Role Collaboration in Multimodal Tool-Using Agents](http://arxiv.org/abs/2610.39324v1)
  来源：arXiv | 日期：2026-10-29 | 相关度：6.1 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Multimodal tool-using agents augment vision-language models with access to external information and capabilities, enabling them to solve knowledge-intensive and visually complex tasks that cannot be addressed using visua...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Advancing Clinical Genomic Analysis with a Skill-Centred Agent](http://arxiv.org/abs/2610.40556v1)
  来源：arXiv | 日期：2026-10-29 | 相关度：5.75 | 新颖度：7.52
  匹配主题：foundation_model_agent
  中文摘要：Clinical genomic analysis requires experts to integrate evolving guidelines, databases, and computational evidence. As sequencing has become increasingly accessible, this complex and labor-intensive process has become a ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Survey on Open Dataset Search in the LLM Era: Retrospectives and Perspectives](http://arxiv.org/abs/2509.00728v2)
  来源：arXiv | 日期：2025-08-31 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：High-quality datasets are typically required for accomplishing data-driven tasks, such as training medical diagnosis models, predicting real-time traffic conditions, or conducting experiments to validate research hypothe...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evaluating and improving AI agents for sequencing protocol understanding](http://arxiv.org/abs/2610.37851v1)
  来源：arXiv | 日期：2026-10-27 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Existing scientific-agent benchmarks rarely evaluate whether agents can reconstruct the exact molecular structures and generation workflows specified by sequencing protocols, a capability critical for analyzing customize...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SciGame: Let Agents Play the Scientific Discovery Games in the Real and Counterfactual World](http://arxiv.org/abs/2610.37919v1)
  来源：arXiv | 日期：2026-10-27 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large language model agents are increasingly used for scientific discovery. However, existing benchmarks mix law inference with programming, score data fitting instead of prediction on unseen inputs, and do not separate ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SpectRAG: Weighted Chunk Graphs for Token-Budgeted Context Selection in Multi-Hop Retrieval-Augmented Generation](http://arxiv.org/abs/2610.36991v2)
  来源：arXiv | 日期：2026-10-27 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) systems ground large language models (LLMs) by retrieving external evidence and conditioning generation on the retrieved context. Although dense retrieval is effective for local seman...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Statistical Detection of Positional Bias in LLM-Based Recommender Systems: Methodologies and Empirical Evidence](http://arxiv.org/abs/2610.37962v1)
  来源：arXiv | 日期：2026-10-27 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) are increasingly used as recommendation generators in conversational recommender systems (RS) via retrieval-augmented generation (RAG). This flexible design introduces new sources of structur...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Retrieving from Your Own Mistakes: On-Policy Training of Embedding Models for Multi-Hop Retrieval-Augmented Generation](http://arxiv.org/abs/2610.40409v1)
  来源：arXiv | 日期：2026-10-29 | 相关度：4.75 | 新颖度：6.86
  匹配主题：foundation_model_agent
  中文摘要：Complex questions in retrieval-augmented generation require evidence spread over several documents, and an answer is reliable only when the retriever finds all of it. Chain embedding retrievers collect such evidence step...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Learning Scientific Trajectories to Predict Future Biomedical Discoveries](http://arxiv.org/abs/2610.38719v1)
  来源：arXiv | 日期：2026-10-28 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：AI co-scientists have expanded the use of large language models for generating scientific hypotheses and guiding experimental investigation. Here we investigate whether temporal patterns in the semantic representations o...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Asking the Data: Conversational Interrogation of LC-MS/MS Proteomics Data Sets with an LLM Agent](https://www.biorxiv.org/content/10.64898/2026.10.22.760949v1)
  来源：bioRxiv | 日期：2026-10-27 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Proteomics workflows are designed to answer predefined questions, leaving analytical problems that emerge after first results difficult to investigate without additional bioinformatics work. We introduce data set interro...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AltereGO: Prediction of Protein Function by Multimodal Fusion of Protein Language Models.](https://www.biorxiv.org/content/10.64898/2026.10.23.761425v1)
  来源：bioRxiv | 日期：2026-10-27 | 相关度：7.1 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Protein function prediction is increasingly important as the rapid growth of sequence databases outpaces the capacity of experimental pipelines to characterize protein function. Here we introduce AltereGO, a framework th...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Decompose, Estimate, Select: Coverage-Aware Context Construction for Long-Form RAG](http://arxiv.org/abs/2610.40314v1)
  来源：arXiv | 日期：2026-10-29 | 相关度：5.45 | 新颖度：6.97
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) grounds a language model's output in retrieved evidence, but for complex questions spanning multiple aspects of an information need, relevance-based retrieval may return redundant evi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Self-Augmenting Retrieval for Diffusion Language Models](http://arxiv.org/abs/2606.06474v2)
  来源：arXiv | 日期：2026-06-04 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Diffusion language models generate text by iteratively denoising an entire response in parallel, holding a noisy draft of the answer at every step. We show that these intermediate states surface salient entities early in...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [OmniVIC: A Self-Improving Variable Impedance Controller with Vision-Language In-Context Learning for Safe Robotic Manipulation](http://arxiv.org/abs/2510.17150v3)
  来源：arXiv | 日期：2025-10-20 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：We present OmniVIC, a universal variable impedance controller (VIC) enhanced by a vision language model (VLM), which improves safety and adaptation in any contact-rich robotic manipulation task to enhance safe physical i...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Incentivizing Self-Learning in Large Language Models via Reinforcement Learning](http://arxiv.org/abs/2610.39671v1)
  来源：arXiv | 日期：2026-10-29 | 相关度：4.75 | 新颖度：6.14
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) draw on parametric knowledge and retrieval-augmented generation (RAG) to solve knowledge-intensive tasks. Yet problem solving in unfamiliar domains calls for tightly coupled knowledge acquisi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Two Birds with One Stone: Skill-Augmented Generation via Unified Retrieval and Utilization](http://arxiv.org/abs/2610.38204v1)
  来源：arXiv | 日期：2026-10-28 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Skills, as reusable external knowledge, have demonstrated substantial potential to enhance the ability of Large Language Models (LLMs) to solve complex tasks. However, existing skill-augmented generation methods typicall...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 其他

- [TCC-RAG: Temporal Causal Chain-Guided RAG for Temporal Knowledge Graph Question Answering](http://arxiv.org/abs/2610.38366v1)
  来源：arXiv | 日期：2026-10-28 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in large language models (LLMs) have spurred growing interest in temporal knowledge graph question answering (TKGQA). Most existing methods rely on semantic retrieval augmented generation (RAG), which suf...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [DAPE-PD: Diffusion adaptation of genomic foundation model enables tailored-generation of cis-regulatory DNA](https://www.biorxiv.org/content/10.64898/2026.10.24.761598v1)
  来源：bioRxiv | 日期：2026-10-27 | 相关度：5.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Genomic foundation models (GFMs) have transformed our ability to learn the evolutionary language encoded in genomes, yet their potential for programmable regulatory DNA engineering remains underexplored. Regulatory funct...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Can LLMs Uncover Hidden Physical Laws through Free Exploration?](http://arxiv.org/abs/2610.37649v1)
  来源：arXiv | 日期：2026-10-27 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Scientific discovery often begins with an unexpected observation that prompts a new research question. In a world with altered physical laws, can large language models (LLMs) notice unexpected behavior, such as heavier o...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multi-modal data Integration for Metastatic Risk Prediction of AJCC Stage I/II Melanomas: Results from the Population-based Dutch Early-stage Melanoma Study (D-ESMEL)](https://www.medrxiv.org/content/10.64898/2026.10.29.26366608v1)
  来源：medRxiv | 日期：2026-10-29 | 相关度：3.05 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Early-stage melanoma accounts for 40-60% of melanoma-related deaths. Most prognostic modelling studies focus on unimodal approaches or a single multimodal integration strategy, overlooking alternative methods and biologi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ProtCell: a foundation model for single-cell proteomics](https://www.biorxiv.org/content/10.64898/2026.10.22.760932v1)
  来源：bioRxiv | 日期：2026-10-27 | 相关度：2.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：Single-cell proteomics provides a direct functional readout of cellular states, but targeted assays measure limited and non-identical protein panels, fragmenting information across experiments. Here, we present ProtCell,...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Adaptive Modular Retrieval-Augmented Framework for Cross-Domain Image Classification](http://arxiv.org/abs/2510.05071v2)
  来源：arXiv | 日期：2025-10-06 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Effective image classification in real-world scenarios requires models capable of capturing both local features and global context, while adapting to the evolving complexity of the input. This paper presents a hybrid dee...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Scaling genetic discovery through automated post-GWAS interpretation](https://www.biorxiv.org/content/10.64898/2026.10.23.761278v1)
  来源：bioRxiv | 日期：2026-10-27 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Genome-wide association studies (GWAS) have made association discovery systematic and cumulative, yet evidence for interpreting associated loci remains selective, heterogeneous and difficult to accumulate across studies....
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Benchmarking Vietnamese Legal Knowledge of Large Language Models](http://arxiv.org/abs/2512.14554v7)
  来源：arXiv | 日期：2025-12-16 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：The rapid advancement of large language models (LLMs) has enabled new possibilities for applying artificial intelligence within the legal domain. Nonetheless, the complexity, hierarchical organization, and frequent revis...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Beyond Similarity Search: Knowledge Graph Metadata Enrichment for Enterprise Retrieval-Augmented Generation](http://arxiv.org/abs/2610.37728v1)
  来源：arXiv | 日期：2026-10-27 | 相关度：1.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：A key challenge of RAG systems is retrieving information from enterprise documents created by multiple teams over time, where it is not possible to enrich the information using the latest information and metadata availab...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Glance: The Generator Is Its Own Reranker](http://arxiv.org/abs/2610.40454v1)
  来源：arXiv | 日期：2026-10-29 | 相关度：0.7 | 新颖度：7.42
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation commonly serves separate models for reranking and answering, duplicating model residency and passage processing. We introduce Glance, which equips the generator with a lightweight decision ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [DiG-bench: Discovery in Games](http://arxiv.org/abs/2608.12593v2)
  来源：arXiv | 日期：2026-08-12 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Discovery---formulating novel generalizations---is a central part of the scientific process. Despite its importance, there is a gap in the current AI benchmark landscape, with few benchmarks directly probing the capacity...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Latent Abstraction for Retrieval-Augmented Generation](http://arxiv.org/abs/2604.17866v4)
  来源：arXiv | 日期：2026-04-20 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) has become a standard approach for enhancing large language models (LLMs) with external knowledge, mitigating hallucinations, and improving factuality. However, existing systems rely ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Role-Augmented Intent-Driven Generative Search Engine Optimization](http://arxiv.org/abs/2508.11158v3)
  来源：arXiv | 日期：2025-08-15 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Generative search engines (GSEs), which combine large language models (LLMs) with retrieval-augmented generation (RAG), are reshaping how users access Web information and making source visibility and influence in generat...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Species phylogenetics using intraprotein residue dependence inferred with protein foundation models](https://www.biorxiv.org/content/10.64898/2026.05.26.727927v2)
  来源：bioRxiv | 日期：2026-10-27 | 相关度：3.05 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Traditional molecular phylogenetic inference uses multiple sequence alignments and amino acid substitution models that generally assume that sites evolve independently. In contrast, protein foundation models (pFMs) are d...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Simultaneous detection of influenza and SARS-CoV-2 on an AI-nanopore multiplex platform.](https://pubmed.ncbi.nlm.nih.gov/42831434/)
  来源：PubMed | 日期：2026-10-27 | 相关度：2.65 | 新颖度：0.75
  匹配主题：sequencing_bioinformatics
  中文摘要：Seasonal influenza and SARS-CoV-2 co-circulate and present overlapping symptoms, creating demand for rapid multiplex diagnostics beyond the sensitivity limits of antigen tests and the infrastructure requirements of nucle...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [From the Rock Floor to the Cloud: A Systematic Survey of State-of-the-Art NLP in Battery Life Cycle](http://arxiv.org/abs/2510.27369v2)
  来源：arXiv | 日期：2025-10-31 | 相关度：2.05 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：This work presents a systematic review of the application of natural language processing (NLP) along the entire battery life cycle, instead of the review of one stage or method, and introduces a novel conceptual technica...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SheafStain: Sheaf-Theoretic Schrödinger Bridge for Spatially and Biologically Coherent Virtual Staining](http://arxiv.org/abs/2606.11846v3)
  来源：arXiv | 日期：2026-06-10 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Current virtual staining approaches offer the potential for time- and cost-efficient biomarker quantification in cancer diagnostics and prognostics. However, patch-wise inference for gigapixel whole-slide images fails to...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Building virtual cell dynamics that evolve with biological measurements](https://www.biorxiv.org/content/10.64898/2026.10.23.761350v1)
  来源：bioRxiv | 日期：2026-10-27 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Virtual cell models built from single-cell measurements need to predict how cells change over time, but new biological measurements often reveal dynamical relationships that existing models cannot express. Translating su...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Origin Lens: A Privacy-First Mobile Framework for Cryptographic Image Provenance and AI Detection](http://arxiv.org/abs/2602.03423v2)
  来源：arXiv | 日期：2026-02-03 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：The proliferation of generative AI poses challenges for information integrity assurance, requiring systems that connect model governance with end-user verification. We present Origin Lens, a privacy-first mobile framewor...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A Sequential Decision Framework for Evaluating LLM-Guided Search](http://arxiv.org/abs/2610.39231v1)
  来源：arXiv | 日期：2026-10-29 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Recent systems applying retrieval-augmented generation (RAG) and "deep research" iteratively generate queries, retrieve documents, and examine their contents, using the resulting information to guide subsequent search st...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Tessera: Structure-Completed Evidence Units for Web Retrieval-Augmented Generation](http://arxiv.org/abs/2610.37080v1)
  来源：arXiv | 日期：2026-10-27 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Web retrieval-augmented generation (RAG) splits a page into fixed-size text chunks or, in recent visual pipelines, screenshot tiles, and the retrieved item serves at once as the unit of indexing, ranking, and reading. We...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 其他

- [When Is Additional Retrieval Worthwhile? A Cost-Aware Study of Evidence Gain and Answer Reliability in RAG](http://arxiv.org/abs/2610.37358v1)
  来源：arXiv | 日期：2026-10-27 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) can benefit from more sophisticated retrieval, but extra retrieval may be unnecessary for many questions and gains in evidence retrieval may not translate into faithful or correct ans...
  为什么值得看：When Is Additional Retrieval Worthwhile? 与你的主题有弱匹配，暂时保留作低优先级跟踪。
