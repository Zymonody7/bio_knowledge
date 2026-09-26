# 每日论文监控日报 (2026-09-26)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 28 篇新论文。

## 抓取状态

- arXiv：成功，命中 30 篇
- PubMed：成功，命中 58 篇
- bioRxiv：失败，命中 0 篇，错误：Expecting value: line 1 column 1 (char 0)
- medRxiv：失败，命中 0 篇，错误：Expecting value: line 1 column 1 (char 0)

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [A Comprehensive Review of Large Language Models for Nanophotonics: From Surrogate Modeling to Autonomous Design](http://arxiv.org/abs/2608.18279v3)
  来源：arXiv | 日期：2026-08-18 | 相关度：7.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Metasurfaces have revolutionized the development of photonic devices by enabling unprecedented precision in light manipulation. However, their design processes are often constrained by computationally expensive simulatio...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CRISS: A Retrieval-Augmented AI Chatbot for Assisting Cancer Registrars](http://arxiv.org/abs/2609.29075v1)
  来源：arXiv | 日期：2026-09-24 | 相关度：6.55 | 新颖度：1.2
  匹配主题：foundation_model_agent
  中文摘要：Cancer registrars, including Oncology Data Specialists (ODSs), must interpret complex and frequently updated coding and staging standards. We developed CRISS (Cancer Registry Intelligent Support System), a retrieval-augm...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Integration of Retrieval-Augmented Generation for Knowledge Access in the ELBE Accelerator Control System](http://arxiv.org/abs/2609.27579v1)
  来源：arXiv | 日期：2026-09-23 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：The efficient operation of accelerator facilities increas- ingly relies on rapid access to heterogeneous operational knowledge, including logbooks, interlock reports, machine parameters, and historical archive data. At E...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EvoTreeNAD: Genealogy-Guided Evolution for LLM-Driven Neural Architecture Discovery](http://arxiv.org/abs/2609.29016v1)
  来源：arXiv | 日期：2026-09-24 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：AI-driven scientific discovery accelerates research by autonomously developing solutions and designs. Large language model (LLM) agents support this process through iterative generation and evaluation. Yet these iteratio...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Unraveling the cognitive patterns of Large Language Models through module communities](http://arxiv.org/abs/2508.18192v2)
  来源：arXiv | 日期：2025-08-25 | 相关度：6.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have reshaped our world with significant advancements in science, engineering, and society through applications ranging from scientific discoveries and medical diagnostics to Chatbots. Despit...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 低优先级

### Foundation Model / Agent

- [REAT: A Reflective Experience-Augmented Tutoring Framework for Multi-turn Mathematical Instruction](http://arxiv.org/abs/2609.29804v1)
  来源：arXiv | 日期：2026-09-24 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Current Large Language Models (LLMs) excel at solving complex mathematical problems, yet this proficiency does not inherently translate into effective tutoring. While advanced LLM tutors may leverage multi-agent framewor...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BaseCamp --- An Agentic AI Framework for Automating DNA Sequencing Data Pipelines](http://arxiv.org/abs/2609.28557v1)
  来源：arXiv | 日期：2026-09-23 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：DNA sequencing pipelines, spanning quality control, alignment, variant calling, and annotation, are now reliably executed by workflow management systems that orchestrate established bioinformatics tools at scale. What re...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PFArena: Benchmarking Language Models for Protein Modification](http://arxiv.org/abs/2609.28921v1)
  来源：arXiv | 日期：2026-09-24 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Protein modification requires navigating an immense sequence space, yet wet-lab validation remains low-throughput and costly. Although computational paradigms including protein language models (PLMs), large language mode...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ProteinJEPA: Latent prediction improves protein language model pretraining](http://arxiv.org/abs/2605.07554v2)
  来源：arXiv | 日期：2026-05-08 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Protein language models are trained primarily with masked language modeling (MLM), which predicts masked amino-acid identities. Joint-embedding predictive architectures (JEPA) instead predict latent representations, but ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Driving Epidemic Models with AI Agents: the Epydemix Agent Framework](http://arxiv.org/abs/2609.28692v1)
  来源：arXiv | 日期：2026-09-23 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Artificial Intelligence agents based on large language models provide convenient natural language interfaces to scientific software, but reliability is not automatic. Here we introduce the Epydemix Agent Framework, an ad...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LSF-SR: Latent Semantic Fusion for Sequential Recommendation via Flow-based Conditional Variational Autoencoders](http://arxiv.org/abs/2609.29815v1)
  来源：arXiv | 日期：2026-09-24 | 相关度：4.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Sequential recommendation aims to predict users' future interests from their historical interactions. Although Large Language Models (LLMs) capture rich item semantics, existing methods often struggle to align collaborat...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The Fellowship of the Query: Learning Retrieval Actions](http://arxiv.org/abs/2609.28653v1)
  来源：arXiv | 日期：2026-09-23 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented question answering requires control decisions about when to decompose a question, search, reformulate, extract evidence, synthesize facts, verify progress, and stop. We study whether trajectory fine-t...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Multimodal 3D Foundation Model for Light Sheet Fluorescence Microscopy Enables Few-Shot Segmentation, Classification, and Deblurring](http://arxiv.org/abs/2605.26026v2)
  来源：arXiv | 日期：2026-05-25 | 相关度：3.45 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Light sheet fluorescence microscopy (LSM) enables high-resolution, three-dimensional (3D) imaging of biological specimens, providing rich volumetric data for studying cellular organization, pathology, and vascular networ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LabFactory: Building and Evaluating Executable AI Labs](http://arxiv.org/abs/2609.28697v1)
  来源：arXiv | 日期：2026-09-23 | 相关度：3.1 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Scientific tasks specify a desired capability, but realizing it often requires building a computational system tailored to the task---acquiring data, designing representations, training models, implementing tools, and de...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Document Silos to Process Intelligence: A Multi-Layer Knowledge Graph for CMC Process Development](http://arxiv.org/abs/2609.11493v2)
  来源：arXiv | 日期：2026-09-10 | 相关度：2.1 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Chemistry, Manufacturing and Controls (CMC) process development generates an enormous body of technical information across a multi-stage, knowledge-intensive continuum from drug discovery to commercial manufacturing. Thi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [VidTutorAssistant: Automating Responses to Programming Tutorial Questions](http://arxiv.org/abs/2609.29129v1)
  来源：arXiv | 日期：2026-09-24 | 相关度：2.05 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Programming tutorial videos on YouTube are an important information resource for software developers and students, and their comment sections have evolved into active spaces where viewers ask follow-up questions. The vol...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Advances in Machine Learning for Drug Repurposing: From Methodologies to Precision Medicine with Case Studies in COVID-19, Parkinson's Disease, and Cancer.](https://pubmed.ncbi.nlm.nih.gov/42776876/)
  来源：PubMed | 日期：2026-09-23 | 相关度：5.75 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：This review investigates recent advances in machine learning (ML) for drug repurposing, with applications spanning COVID-19, Parkinson's disease, and cancer. We provide a methodological taxonomy of ML techniques includin...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [RexDrug: Reliable Multi-Drug Combination Extraction through Reasoning-Enhanced LLMs](http://arxiv.org/abs/2603.08166v2)
  来源：arXiv | 日期：2026-03-09 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Automated Drug Combination Extraction (DCE) from large-scale biomedical literature is crucial for advancing precision medicine and pharmacological research. However, existing relation extraction methods primarily focus o...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [RexDrug: Reliable Multi-Drug Combination Extraction Through Reasoning-Enhanced LLMs.](https://pubmed.ncbi.nlm.nih.gov/42784491/)
  来源：PubMed | 日期：2026-09-24 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Automated Drug Combination Extraction (DCE) from large-scale biomedical literature is crucial for advancing precision medicine and pharmacological research. However, existing relation extraction methods primarily focus o...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Automated Regulatory Compliance Question Answering in Financial Services with Domain-Adapted Retrieval-Augmented Generation](http://arxiv.org/abs/2609.30009v1)
  来源：arXiv | 日期：2026-09-24 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Financial institutions operate under dense, frequently amended rulebooks, and answering a compliance question correctly requires not only fluency but verifiable grounding in the authoritative text. Large language models ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [TWIST: A Proposed Benchmark for Intervention Quality in Conversational Memory, with a Human-Validated Draft-Alignment](http://arxiv.org/abs/2609.28575v1)
  来源：arXiv | 日期：2026-09-23 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Long-conversation memory benchmarks increasingly test recall and prompted knowledge updates, and recent work studies evolving user beliefs and memory state. TWIST is a proposed benchmark suite for a complementary, unmeas...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Qwen-Planner-Agent: A Closed-Loop AI-for-AI Framework for Real-World Mobile Planner Agents](http://arxiv.org/abs/2609.29892v1)
  来源：arXiv | 日期：2026-09-24 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：The rapid progression of large language models is extending AI from passive content generation into the active workflows of engineering and scientific discovery. This shift raises a compelling question: can AI be both th...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Asymmetric Dynamic Routing: Balancing Reasoning Depth and Computational Efficiency in Hypergraph RAG](http://arxiv.org/abs/2609.29282v1)
  来源：arXiv | 日期：2026-09-24 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：While graph-based and hypergraph-based Retrieval-Augmented Generation (RAG) significantly mitigate hallucinations in Large Language Models (LLMs), existing structure-based RAG systems typically adopt static traversal str...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Dual-Hypergraph Indexing: Bridging Knowledge Islands for Multi-Hop Reasoning in Retrieval-Augmented Generation](http://arxiv.org/abs/2609.28108v1)
  来源：arXiv | 日期：2026-09-23 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：While hypergraph-based Retrieval-Augmented Generation (RAG) effectively captures higher-order multi-entity correlations, existing paradigms treat extracted hyperedges as isolated factual assertions. This structural fragm...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Advancing the Physical Internet with GraphRAG: A New Way to Review and Integrate Existing Research](http://arxiv.org/abs/2609.29083v1)
  来源：arXiv | 日期：2026-09-24 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Physical Internet (PI) is an emerging concept that applies the digital internet as a design metaphor for the development of sustainable, interoperable, and collaborative freight transportation. It is considered a way to ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [TEMPS: Temporal Sentence Embeddings for Temporal Information Retrieval](http://arxiv.org/abs/2609.28048v1)
  来源：arXiv | 日期：2026-09-23 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Modern information retrieval (IR) systems rarely represent time, yet many information needs depend on it: in clinical, journalistic, and legal search, when an event occurred can decide whether a document is relevant. Den...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Integrative AI-based multiomic and neurophysiological profiling of chronic pain in rheumatoid arthritis: study protocol for the prospective, observational, case-control RA-PAIN-AI study.](https://pubmed.ncbi.nlm.nih.gov/42785931/)
  来源：PubMed | 日期：2026-09-24 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Rheumatoid arthritis (RA) is a chronic systemic autoimmune disease in which pain remains the most prominent and burdensome symptom from the patient's perspective. Despite effective control of peripheral inflammation with...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Only Pay What You Must Spend: On-Demand Privacy Budget Payment for Differentially Private RAG](http://arxiv.org/abs/2609.27406v1)
  来源：arXiv | 日期：2026-09-23 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Deploying large language models (LLMs) on sensitive data via Retrieval-Augmented Generation (RAG) introduces severe privacy risks. Recent studies apply Differential Privacy (DP) to LLMs with RAG for formal privacy guaran...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。
