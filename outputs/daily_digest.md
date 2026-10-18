# 每日论文监控日报 (2026-10-18)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 24 篇新论文。

## 抓取状态

- arXiv：成功，命中 18 篇
- PubMed：成功，命中 34 篇
- bioRxiv：成功，命中 7 篇
- medRxiv：成功，命中 9 篇

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [Multimodal Artificial Intelligence for Cause-of-Death Assignment From Verbal Autopsy Records: A National Benchmark Study in South Africa](https://www.medrxiv.org/content/10.64898/2026.10.15.26364476v1)
  来源：medRxiv | 日期：2026-10-16 | 相关度：7.9 | 新颖度：1.7
  匹配主题：foundation_model_agent
  中文摘要：BACKGROUND Timely cause-of-death (COD) information guides health policy, yet many deaths in low- and middle-income countries are not medically certified. In Africa, fewer than 10% of deaths are. Verbal autopsy (VA) yield...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Loud and Clear: Making Visual Evidence Count in Multimodal Document RAG](http://arxiv.org/abs/2610.21318v1)
  来源：arXiv | 日期：2026-10-15 | 相关度：7.5 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Multimodal document retrieval-augmented generation (RAG) has focused largely on retrieval, yet its answers depend on how well a vision-language model reads the retrieved pages. We find that evidence in retrieved pages re...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Performance evaluation and benchmarking across 16 large language model configurations on a large real-world emergency department triage data set](https://www.medrxiv.org/content/10.64898/2026.05.28.26353935v2)
  来源：medRxiv | 日期：2026-10-16 | 相关度：7.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Background Emergency department (ED) triage is a decision process that determines patient prioritization and resource allocation. Large language models (LLMs) have been proposed as decision-support tools for triage, yet ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PatientPheX: A Full-Text Biomedical Corpus for Patient-Specific Phenotype Information Extraction](https://www.biorxiv.org/content/10.64898/2026.10.07.757319v1)
  来源：bioRxiv | 日期：2026-10-15 | 相关度：6.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Patient-specific phenotype information extraction identifiers and normalizes phenotype entities and links them with individual patients, supporting rare disease research and genotype-phenotype analysis. However, existing...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Tool-Augmented Large Language Models for Reliable Medical Calculation from Patient Notes](http://arxiv.org/abs/2610.21477v1)
  来源：arXiv | 日期：2026-10-15 | 相关度：7.55 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Medical calculators translate raw patient observations into clinically actionable values and scores. However, applying these calculators directly to free-form patient notes requires precise variable extraction combined w...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Drug-centric knowledge graph: representing therapeutic modality, pharmacology and multiscale biology](https://www.biorxiv.org/content/10.64898/2026.10.15.759051v1)
  来源：bioRxiv | 日期：2026-10-16 | 相关度：7.1 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Biomedical knowledge graphs link targets to mechanisms, diseases and phenotypes, but target-centered representations omit much of what distinguishes therapeutic interventions. We introduce a drug-centric knowledge graph,...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RAG4Tickets: AI-Powered Ticket Resolution via Retrieval-Augmented Generation on JIRA and GitHub Data](http://arxiv.org/abs/2510.08667v3)
  来源：arXiv | 日期：2025-10-09 | 相关度：6.55 | 新颖度：1.2
  匹配主题：foundation_model_agent
  中文摘要：Modern software teams frequently encounter delays in resolving recurring or related issues due to fragmented knowledge scattered across JIRA tickets, developer discussions, and GitHub pull requests (PRs). To address this...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Constructed Negatives Shape the Evaluation of Sequence-Based Protein--Protein Interaction Models](https://www.biorxiv.org/content/10.64898/2026.10.08.757593v1)
  来源：bioRxiv | 日期：2026-10-15 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Many machine-learning tasks, including representation learning, rely on negative examples that are constructed rather than directly observed. This issue is especially important for protein--protein interaction (PPI) pred...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Quantifying Cancer Clinical Trial Eligibility Using Artificial Intelligence-Based Matching](https://www.medrxiv.org/content/10.64898/2026.06.03.26354859v2)
  来源：medRxiv | 日期：2026-10-15 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：PURPOSE: To develop and validate an artificial intelligence-enabled platform that combines efficient screening with explicit eligibility logic by converting unstructured cancer trial criteria into reusable structured que...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Analyzing performance of Retrieval Augmented Generation models for Question Answering Tasks](http://arxiv.org/abs/2610.20419v2)
  来源：arXiv | 日期：2026-10-14 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) models have become almost a cornerstone of open-domain question answering tasks; in which the quality of answers generated in the process, greatly relies on the effectiveness of retri...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TEM: Temporal State Tracking Memory for Large Language Model Agents](http://arxiv.org/abs/2610.21900v1)
  来源：arXiv | 日期：2026-10-15 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：An agent's memory must remain useful as information changes across conversations. A new fact may replace an earlier value without making that value irrelevant to a later question. We present Temporal State Tracking Memor...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evaluating Inquiry Learning in LLM-Based Agents: Hypothesizing, Reasoning, and Exploration](http://arxiv.org/abs/2610.21604v1)
  来源：arXiv | 日期：2026-10-15 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Scientific inquiry involves iterative cycles of exploration, hypothesis generation, and reasoning over observations to uncover relationships in complex systems. Large language models (LLMs) have demonstrated strong capab...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PrefixFlow: Training-Time KV Caching for Schedule-Level Prefix Reuse in LLM RL Training](http://arxiv.org/abs/2606.01143v4)
  来源：arXiv | 日期：2026-05-31 | 相关度：3.45 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：In reinforcement learning (RL) post-training, one prompt fans out into $N$ trajectories, yet standard trainers replay the shared prefix's forward and backward pass $N$ times; in long-context retrieval-augmented generatio...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RAG-RST: Retrieved Exemplars as In-Context Discourse Schema for RST Parsing](http://arxiv.org/abs/2610.22150v1)
  来源：arXiv | 日期：2026-10-15 | 相关度：2.1 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：In Rhetorical Structure Theory (RST), each edge of a discourse tree carries a nuclearity label, marking which span holds the central content, and a relation drawn from a closed inventory of functional categories. Neither...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Onboard Lightweight LLM Reasoning for Human-Aware Safe UAV Navigation](http://arxiv.org/abs/2610.22092v1)
  来源：arXiv | 日期：2026-10-15 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Aerial robots operating near people must treat a pedestrian, a parked car, and a wall differently, yet conventional perception--planning stacks reduce all of them to occupied geometry---a \emph{human-aware safety gap} in...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Cost-Efficient RAG for Entity Matching with LLMs: A Blocking-based Batch Processing Framework](http://arxiv.org/abs/2602.05708v2)
  来源：arXiv | 日期：2026-02-05 | 相关度：5.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) offer a compelling approach to entity matching (EM) in label-scarce settings, yet their matching quality is sensitive to records with ambiguous or sparse attributes due to the absence of exte...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Private Retrieval Augmented Generation via Random Projection](http://arxiv.org/abs/2610.22297v1)
  来源：arXiv | 日期：2026-10-15 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) enhances the capabilities of large language models (LLMs) by querying external structured knowledge. However, it can also introduce privacy risks by leaking sensitive information from...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Multi-sourced AI Tutor for Non-Native English Speaker Students](http://arxiv.org/abs/2610.22163v1)
  来源：arXiv | 日期：2026-10-15 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly being adopted as teaching tools in computing education, particularly for developing AI tutors capable of answering student questions. With the rise in enrollment of internati...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Community-driven advances in computational mass spectrometry: The perspective of EuBIC-MS members.](https://pubmed.ncbi.nlm.nih.gov/42436009/)
  来源：PubMed | 日期：2026-10-15 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Advances in data acquisition, artificial intelligence, and integrative bioinformatics are driving the rapid evolution of computational mass spectrometry, and in turn, transforming modern proteomics, metabolomics, and lip...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Enhancing Knowledge Density via Hierarchical Context Pruning for Retrieval-Augmented Repository-Level Code Completion](http://arxiv.org/abs/2508.10068v3)
  来源：arXiv | 日期：2025-08-13 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) has advanced repository-level code completion by retrieving external code snippets, API documentation, or type definitions to expand the model's contextual awareness. However, under t...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [BanglaDiaHallu: Hallucinations of large language models and the effect of guideline-grounded retrieval-augmented generation in Bangla diabetes question answering](https://www.medrxiv.org/content/10.64898/2026.10.14.26365587v1)
  来源：medRxiv | 日期：2026-10-16 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly consulted for health advice, but they can produce fluent statements that are false or unsupported, known as hallucinations, and this risk is poorly characterised in low-resou...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Multimodal profiling for prediction of primary resistance to anti-PD-(L)1 therapy in advanced non-small-cell lung cancer: the prospective PIONeeR biomarkers study](https://www.medrxiv.org/content/10.64898/2026.01.09.26343779v3)
  来源：medRxiv | 日期：2026-10-16 | 相关度：3.05 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Background Pretreatment prediction of primary resistance to anti-PD-(L)1 therapy in advanced non-small-cell lung cancer (NSCLC) remains an unmet clinical need. Existing biomarkers - including PD-L1 expression and tumour ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Poisoning the Neighborhood: A Topology-Aware Topic-Level Attack on Large-Scale HNSW-based RAG Systems](http://arxiv.org/abs/2610.21464v1)
  来源：arXiv | 日期：2026-10-15 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) mitigates hallucinations and knowledge staleness in large language models using external knowledge. However, ingestion from public and third-party sources exposes RAG systems to poiso...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [ConStore: Search-Overlapped Prefetch and Co-Retrieval-Aware Content Storage for Disk-Based ANNS](http://arxiv.org/abs/2610.21676v1)
  来源：arXiv | 日期：2026-10-15 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Disk-based approximate nearest-neighbor search (ANNS) supports retrieval-augmented generation (RAG), search, recommendation, and advertising over corpora that exceed memory capacity. Existing ANNS research often focuses ...
  为什么值得看：ConStore: Search-Overlapped Prefetch and 与你的主题有弱匹配，暂时保留作低优先级跟踪。
