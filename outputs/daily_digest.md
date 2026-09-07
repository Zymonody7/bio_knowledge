# 每日论文监控日报 (2026-09-07)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 23 篇新论文。

## 抓取状态

- arXiv：成功，命中 19 篇
- PubMed：成功，命中 17 篇
- bioRxiv：成功，命中 13 篇
- medRxiv：成功，命中 4 篇

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [MARLA: An Autonomous Agent for Medical AI Research and Development](https://www.medrxiv.org/content/10.64898/2026.08.21.26361049v2)
  来源：medRxiv | 日期：2026-09-05 | 相关度：8.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Medical AI models have made a great impact on biomedical research and real-world clinical applications, but conducting interdisciplinary medical AI research remains challenging, requiring close collaboration between clin...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Pneumonia Detection in Paediatric Chest X-Rays using Ensembled Large Language Models](https://www.medrxiv.org/content/10.64898/2026.04.10.26347909v2)
  来源：medRxiv | 日期：2026-09-05 | 相关度：7.8 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Background: Paediatric pneumonia is a major cause of childhood morbidity and mortality. Chest X-rays (CXR) are central to diagnosis, but shortages of specialist radiologists can delay reporting. Multimodal large language...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From code to natural language: MErlin - a multiomics toolkit for bacterial epigenomics delivered as Claude agent skill.](https://www.biorxiv.org/content/10.64898/2026.09.02.748773v1)
  来源：bioRxiv | 日期：2026-09-06 | 相关度：7.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Interpreting a bacterial methylome is a multi-omics problem. It requires integrating modified-base calls with genome annotation, motif inventories, methyltransferase genotypes, transcript abundance, replichore position a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SAM-D2Q: Aligning Multimodal Doc2Query with Search Demand and Conversion for E-commerce](http://arxiv.org/abs/2609.04961v1)
  来源：arXiv | 日期：2026-09-04 | 相关度：6.8 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：E-commerce search often suffers from vocabulary mismatch between user queries and merchant-authored product titles, since short titles cannot fully cover diverse user expressions or visual product attributes. Although Do...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [InsightToast: Proactive Information Retrieval & Glanceable Visualization in the Side Channel of Data-Rich Meetings](http://arxiv.org/abs/2608.31115v2)
  来源：arXiv | 日期：2026-08-31 | 相关度：6.55 | 新颖度：1.2
  匹配主题：foundation_model_agent
  中文摘要：Missing institutional context during meetings can impede effective participation. Retrieving relevant information, often scattered across heterogeneous internal and external sources, requires costly task-switching that d...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Distill Globally, Adapt Locally: Reasoning Distillation and Product-Type Test-Time Training for Scalable Trade-Up Recommendation](http://arxiv.org/abs/2609.05363v1)
  来源：arXiv | 日期：2026-09-04 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Trade-up recommendation identifies higher-quality alternatives that preserve a customer's purchase intent while offering upgraded benefits. Large language models (LLMs) can reason about such distinctions, but applying th...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Does Your Agent's Memory Survive a Model Upgrade? A Controlled Study of Memory Portability](http://arxiv.org/abs/2609.05339v1)
  来源：arXiv | 日期：2026-09-04 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Model upgrades are routine; memory migrations are not. An agent can keep the same memory store and still forget: a new model may interpret old notes differently, mixed embedding versions may break retrieval, and repair m...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [OmniSyn unifies target-aware molecular generation and optimization within a synthesis-native LLM framework across the human proteome](https://www.biorxiv.org/content/10.64898/2026.09.02.748775v1)
  来源：bioRxiv | 日期：2026-09-06 | 相关度：7.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Designing target-specific bioactive molecules with actionable synthesis routes for the human proteome holds enormous potential for expanding therapeutic discovery, but remains a challenge. Existing target-aware generativ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ProtLingo: Efficient Protein Language Modeling via Conditional Memory and Expert Routing](http://arxiv.org/abs/2609.04793v1)
  来源：arXiv | 日期：2026-09-04 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Proteins perform diverse cellular functions, and even single amino-acid substitutions can alter stability, activity, or molecular interactions. Protein language models (PLMs) provide a scalable approach for modeling such...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Unlocking Sensitive Data with SPHERE in the Age of AI](https://www.biorxiv.org/content/10.64898/2026.09.01.748580v1)
  来源：bioRxiv | 日期：2026-09-05 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Sensitive human data underpin discoveries across medicine, biology and the social sciences, yet privacy regulation often prevents sharing them with collaborators or artificial intelligence (AI) systems. We introduce SPHE...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Compression Beyond the Uncompressed: A Two-Stage Training Recipe for Soft Context Compression in RAG](http://arxiv.org/abs/2609.05152v1)
  来源：arXiv | 日期：2026-09-04 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) enhances language models with external knowledge, but the lengthy retrieved context inflates the input and degrades inference efficiency. Soft context compression encodes each documen...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Turning Domain Expertise into Multi-Dimensional Evaluation of Biomedical AI with Karenina](https://www.biorxiv.org/content/10.64898/2026.09.01.748513v1)
  来源：bioRxiv | 日期：2026-09-04 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Language models and agents are increasingly used in biomedicine, but current benchmarks reward correct answers even when the underlying reasoning is flawed. Here we introduce Karenina, an open-source framework that turns...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 其他

- [Shadow Queries for Private Retrieval in Vector Databases](http://arxiv.org/abs/2609.04767v1)
  来源：arXiv | 日期：2026-09-04 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) increasingly rely on information retrieval (IR) systems, such as Retrieval-Augmented Generation (RAG), to incorporate domain-specific knowledge without costly re-training. These systems often...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Citation reliability of frontier large language models in medical writing and its automated verification](https://www.medrxiv.org/content/10.64898/2026.08.31.26361806v1)
  来源：medRxiv | 日期：2026-09-04 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly used to draft medical manuscripts, yet their citations are unreliable and clinicians lack a validated way to verify them. We evaluated three frontier LLMs, Claude Opus 4.8, G...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Coarse composition suffices: tabular in-context learning for multi-activity antimicrobial peptide profiling](https://www.biorxiv.org/content/10.64898/2026.08.27.747591v2)
  来源：bioRxiv | 日期：2026-09-06 | 相关度：4.7 | 新颖度：1.5
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Antimicrobial peptides (AMPs) often act against multiple pathogen classes, making multi-label activity prediction a more realistic screening target than binary antimicrobial classification. The ESCAPE benchmark formalize...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PromptBio: An Agentic Platform for End-to-End Computational Biomedical Research](https://www.biorxiv.org/content/10.64898/2026.09.02.748774v1)
  来源：bioRxiv | 日期：2026-09-06 | 相关度：2.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Modern biomedical research increasingly depends on complex computational analyses, yet translating a scientific question into a reliable workflow still requires substantial technical expertise and manual coordination. Pr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TruthInsightBench: An Evidence-Grounded Benchmark for Automated Evaluation of Open-Ended Scientific Discovery Agents](http://arxiv.org/abs/2609.05079v1)
  来源：arXiv | 日期：2026-09-04 | 相关度：1.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：Autonomous coding agents are increasingly proposed as AI-scientist systems that conduct analyses and write research reports, but executing a prescribed analysis is not the same as making a discovery. Existing benchmarks ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Conserved Immune Topology Improves Pathology Foundation Model Generalization for Cross-Cancer MSI-H Prediction](http://arxiv.org/abs/2609.05182v1)
  来源：arXiv | 日期：2026-09-04 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Pathology foundation models integrated with multiple instance learning achieve competitive accuracy within single-cancer cohorts, yet cross-cancer generalization remains unresolved due to organ-specific histological and ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BIT.UA at BioASQ 14B: Modular Retrieval with pg_textsearch and Qdrant, and Agent-Based Answer Generation](http://arxiv.org/abs/2609.04999v1)
  来源：arXiv | 日期：2026-09-04 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：This paper describes the participation of the BIT.UA team from the University of Aveiro in the 14th edition of the BioASQ Task B challenge on biomedical question answering. Building on our previous submissions, we introd...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Global tree encoding of atlas-scale single-cell genomics](https://www.biorxiv.org/content/10.64898/2026.08.31.747971v1)
  来源：bioRxiv | 日期：2026-09-04 | 相关度：2.4 | 新颖度：7.0
  匹配主题：未命中具体主题
  中文摘要：The rapid expansion of single-cell genomic datasets has led to the compilation of biological resources comprising hundreds of millions of cells across tissues, developmental stages, and disease states. This has underscor...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [SimCRAFT: Distilling Remote Sensing Agents via Synthetic Trajectories and Contextual Retrieval-Augmented Fine-Tuning](http://arxiv.org/abs/2608.30277v2)
  来源：arXiv | 日期：2026-08-31 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：The unprecedented surge in Earth observation data volume and diversity has exposed a critical bottleneck for traditional manual workflows, catalyzing the emergence of Remote Sensing (RS) Agents. However, the practical de...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Beyond Maintenance Manual Multimodal RAG: Suggesting What Tool](http://arxiv.org/abs/2609.05116v1)
  来源：arXiv | 日期：2026-09-04 | 相关度：3.45 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Aircraft technicians are required to consult the maintenance manual (MM) for nearly every task, and locating the relevant procedure across hundreds of pages remains time-consuming. Multimodal retrieval augmented generati...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CacheWeaver: Cache-Aware Evidence Ordering for Efficient Grounded RAG Inference](http://arxiv.org/abs/2606.19667v2)
  来源：arXiv | 日期：2026-06-18 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) improves factual grounding, but it also lengthens prompts and raises prefill cost. Prefix caching in serving engines such as vLLM reduces this cost only when requests share the same t...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。
