# 每日论文监控日报 (2026-11-15)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 26 篇新论文。

## 抓取状态

- arXiv：成功，命中 7 篇
- PubMed：成功，命中 47 篇
- bioRxiv：成功，命中 19 篇
- medRxiv：成功，命中 11 篇

## 最值得看

### Foundation Model / Agent

- [MicroDUET: a dual-headed genomic foundation model for pathogen surveillance](https://www.biorxiv.org/content/10.64898/2026.11.11.765853v1)
  来源：bioRxiv | 日期：2026-11-13 | 相关度：8.75 | 新颖度：6.25
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：Pathogen genomic surveillance works from raw reads, assembled genomes and alignments, representations that are slow and costly to compare at scale. Compact embeddings from genomic language models offer an alternative, bu...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multimodal protein representations across human brain cell types](https://www.biorxiv.org/content/10.64898/2026.11.10.765762v1)
  来源：bioRxiv | 日期：2026-11-12 | 相关度：8.5 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：The central nervous system (CNS) comprises diverse cell types whose molecular context shapes the roles of the proteins they express. Computational models offer a scalable way to study the roles of proteins across human b...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [LLM Representations Rival Traditional Predictors and Enhance Multimodal Prediction of APOE4 and Aβ-Burden](https://www.medrxiv.org/content/10.64898/2026.11.09.26367620v2)
  来源：medRxiv | 日期：2026-11-12 | 相关度：7.8 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Spontaneous language offers a scalable, noninvasive approach for identifying biological indicators of preclinical Alzheimer's disease (AD). We examined prediction of APOE4 carrier status and cerebral amyloid-beta burden ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Automating postmarketing pharmacovigilance with large language model agents](https://www.medrxiv.org/content/10.64898/2026.11.10.26367711v1)
  来源：medRxiv | 日期：2026-11-12 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Postmarketing pharmacovigilance relies on spontaneous adverse event reporting and labor-intensive observational studies, which suffer from underreporting and delayed risk detection. Large language model (LLM) agents coul...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LUNA-FM: a subword foundation model for long non-coding RNAs for functional inference.](https://pubmed.ncbi.nlm.nih.gov/43023405/)
  来源：PubMed | 日期：2026-11-13 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：RNA foundation models (FMs) have shown promise for RNA identification and functional annotation. However, many use single-nucleotide tokenization, which produces long input sequences and can increase computational costs ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DrSai: an agentic AI system toward autonomous physics analysis workflows at BESIII](http://arxiv.org/abs/2604.22541v2)
  来源：arXiv | 日期：2026-04-24 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：High Energy Physics (HEP) experiments like BESIII produce petabyte-scale data. Extracting physics results requires complex workflows (simulation, reconstruction, statistical analysis, etc.) that traditionally take expert...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MENTOR: An Evidence-Informed Large Language Model-Based Multi-Agent System for Efficient Selection of Institution-Specific Negative Control Outcomes](https://www.medrxiv.org/content/10.64898/2026.11.10.26367768v1)
  来源：medRxiv | 日期：2026-11-12 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Objective Negative control outcomes (NCOs) help detect and correct systematic error in observational studies, yet their selection remains largely manual. The Common Evidence Model (CEM) can generate candidate lists, but ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [GeneEmbedLLM: Harnessing Large Language Models for Gene Functional Embedding and Association Prediction](https://www.biorxiv.org/content/10.64898/2026.11.05.764758v2)
  来源：bioRxiv | 日期：2026-11-12 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Effective and high-quality gene function representations are crucial for bioinformatics tasks. While biological knowledge about genes is inherently textual, encompassing functional descriptions and pathway annotations, c...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ProLigGPT: a language model for protein-targeted ligand design free from structural constraints](https://www.biorxiv.org/content/10.1101/2023.06.29.543848v2)
  来源：bioRxiv | 日期：2026-11-12 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：The deep-learning language model offers promising approaches to molecular design. However, existing models typically exhibit one or more of the following limitations: structural constraints, confinement to a single task,...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Systematic Benchmarking and Optimization of Retrieval-Augmented Generation (RAG) for Clinical Phenotyping: A Type II Diabetes Case Study in an ICD-Screened Cohort](https://www.medrxiv.org/content/10.1101/2025.04.29.25326696v5)
  来源：medRxiv | 日期：2026-11-14 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Traditional EHR phenotyping methods can require substantial disease-specific development and long-term maintenance. While integrating large language models (LLMs) with Retrieval-Augmented Generation (RAG) is promising, t...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Large language models complement established workflows for mechanistic model construction and refinement in systems biology](https://www.biorxiv.org/content/10.64898/2026.11.11.766014v1)
  来源：bioRxiv | 日期：2026-11-13 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Mechanistic models provide a framework for describing, understanding, and predicting biological processes, but their development requires an interdisciplinary team with expertise in biology, mathematics, and computation....
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [CauProphet: Teaching Agents to Develop Causal Cognition like Humans](http://arxiv.org/abs/2610.32477v3)
  来源：arXiv | 日期：2026-10-23 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large language model (LLM) agents increasingly support long-horizon tasks by leveraging external memory and past experience. However, existing agents mainly retrieve records or summaries, lacking the ability to form and ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DeePEn - A Depth sensitive benchmark for Protein Engineering](https://www.biorxiv.org/content/10.64898/2026.06.09.731073v2)
  来源：bioRxiv | 日期：2026-11-12 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Recent progress in modeling techniques and high-throughput screening has significantly enhanced the accessibility of protein engineering. Nevertheless, further progress gets hindered by the lack of robust benchmarks that...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Benchmark Self-Triage (BeST): Comparing Self-Triage Systems and Multiple Generations of OpenAI Models Against Preliminary Expert Consensus](https://www.medrxiv.org/content/10.64898/2026.10.12.26365287v2)
  来源：medRxiv | 日期：2026-11-12 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：As digital self-triage becomes more widely used, quality assurance requires evaluation of both emergency recognition and overall agreement with clinical judgement, including how these outcomes differ across generations o...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Enrollees and Early Lessons from an Agentic Healthcare Platform with Physicians in the Loop](https://www.medrxiv.org/content/10.64898/2026.11.12.26367291v1)
  来源：medRxiv | 日期：2026-11-13 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Agentic healthcare platforms that combine large language models with physician oversight are growing quickly, but little is known about who uses them. We characterized 3,223 enrollees of Lotus AI, a free, physician-super...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AstroMemBench: A Benchmark for Memory Systems in Embodied Spacecraft Agents](http://arxiv.org/abs/2611.16590v1)
  来源：arXiv | 日期：2026-11-12 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Long-term spacecraft autonomy requires embodied agents to use operational history under communication delays, time-critical operations, environmental uncertainty, complex physical interactions, power and computational co...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [BenchmarkHub: an open-source platform for reproducible evaluation of large language models in healthcare](https://www.medrxiv.org/content/10.64898/2026.11.11.26367866v1)
  来源：medRxiv | 日期：2026-11-13 | 相关度：6.1 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Background: Large language models (LLMs) are solely judged by their scores on biomedical benchmarks, yet these scores are rarely reproducible since the prompts, inference settings and model builds are seldom reported. We...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [AI-Driven Reconstruction of Online Health Narratives Using Agent-Action-Outcome Modeling: Algorithm Development and Validation.](https://pubmed.ncbi.nlm.nih.gov/43024829/)
  来源：PubMed | 日期：2026-11-13 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：People share health experiences online as stories, not isolated facts. Most computational systems reduce these narratives to keywords or claims, overlooking the agency, causality, and interpretation that determine whethe...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Pointing the Way, Hiding the Destination: Practical Private Dense Retrieval at Scale](http://arxiv.org/abs/2608.25735v3)
  来源：arXiv | 日期：2026-08-26 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Hosted retrieval-augmented generation (RAG) and semantic search allow users to query valuable provider-held corpora, raising two competing demands: to hide each query and chosen result, yet reveal only the documents that...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [AI for Biologists: The Knowledge Boundaries of Foundation Models in the Age of Agentic Systems](http://arxiv.org/abs/2611.17015v1)
  来源：arXiv | 日期：2026-11-12 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence (AI) is changing how biological research is done. Biological foundation models trained on millions of nucleotides, protein, and single-cell measurements predict protein structures, mutation effect...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Protein Language Models Fail To Capture Contact Predictions Under Invariant Relabeling](http://arxiv.org/abs/2611.16881v1)
  来源：arXiv | 日期：2026-11-12 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Protein language models (pLMs) produce highly accurate contact maps from single-sequence inputs. People often take this accuracy as proof that these models implicitly learn invariant coevolutionary statistics, extracting...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Coarse-tuning to improve a protein foundation model for a domain of proteins: the example of outer membrane beta barrels](https://www.biorxiv.org/content/10.64898/2026.11.09.765412v1)
  来源：bioRxiv | 日期：2026-11-12 | 相关度：3.95 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Foundation models for proteins have shown great potential in addressing a wide range of challenges in computational molecular biology. State-of-the-art models are trained on large and diverse corpora of protein sequences...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Toward precision nanomedicine via artificial intelligence guided design and prediction.](https://pubmed.ncbi.nlm.nih.gov/43025814/)
  来源：PubMed | 日期：2026-11-13 | 相关度：3.75 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence (AI) is advancing nanomedicine development by linking formulation variables and biological context with delivery, therapeutic efficacy, and safety. This review examines AI assisted formulation des...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Vermeer: Autoregressive generative modeling of microscopy predicts protein localization](https://www.biorxiv.org/content/10.64898/2026.06.01.729395v2)
  来源：bioRxiv | 日期：2026-11-12 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Fluorescent microscopy provides a rich view into how proteins localize within cells, but it remains experimentally infeasible to image human proteins across all of the different factors that can impact localization. We i...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [The Therapeutic Pipeline: Future Treatments and Precision Medicine.](https://pubmed.ncbi.nlm.nih.gov/43025460/)
  来源：PubMed | 日期：2026-11-13 | 相关度：3.7 | 新颖度：0.25
  匹配主题：pathogenomics
  中文摘要：rare interstitial lung diseases (ILDs) represent a heterogeneous group of disorders characterized by various pathogenic mechanisms, clinical presentations, prognoses, and therapeutic challenges. Among these, acid sphingo...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Precision Neurology in Alzheimer's Disease: Genomics to Drug Optimization for Effective Therapeutic Intervention.](https://pubmed.ncbi.nlm.nih.gov/43018845/)
  来源：PubMed | 日期：2026-11-12 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Alzheimer's disease (AD) exhibits high clinical and biological heterogeneity, which complicates the development of one-size-fits-all therapeutic strategies. Standard trial designs can mask subgroup-specific effects, high...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
