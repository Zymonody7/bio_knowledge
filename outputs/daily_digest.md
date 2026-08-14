# 每日论文监控日报 (2026-08-14)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 44 篇新论文。

## 抓取状态

- arXiv：成功，命中 49 篇
- PubMed：成功，命中 47 篇
- bioRxiv：失败，命中 0 篇，错误：500 Server Error: Internal Server Error
- medRxiv：失败，命中 0 篇，错误：500 Server Error: Internal Server Error

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [Natural Language Processing: A Comprehensive Practical Guide from Tokenisation to RLHF](http://arxiv.org/abs/2605.03799v3)
  来源：arXiv | 日期：2026-05-05 | 相关度：7.9 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：This preprint presents a systematic, research-oriented practicum that guides the reader through the entire modern NLP pipeline --- from tokenisation and vectorisation to fine tuning of large language models, retrieval au...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Multi-Resolution Cells to Gigapixel Whole Slide Images Foundation Model for Computational Pathology](http://arxiv.org/abs/2608.03508v2)
  来源：arXiv | 日期：2026-08-04 | 相关度：7.5 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Vision Transformers (ViTs) and their hierarchical variants have achieved strong performance in Computational Pathology (CPath). However, most are pre-trained on single-resolution Whole Slide Images (WSIs), limiting their...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [RoboHarness: A Memory-Augmented Policy Harness for Vision-Language-Action Model Robustness via In-Context Adaptation](http://arxiv.org/abs/2603.24060v3)
  来源：arXiv | 日期：2026-03-25 | 相关度：7.9 | 新颖度：1.7
  匹配主题：foundation_model_agent
  中文摘要：Despite the promise of Vision-Language-Action (VLA) models as generalist robotic controllers, their robustness against perceptual noise and environmental variations in out-of-distribution (OOD) tasks remains fundamentall...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MBA: Multimodal Benchmark and Agents for Real-World Business Ideation](http://arxiv.org/abs/2608.11616v2)
  来源：arXiv | 日期：2026-08-12 | 相关度：6.8 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Agentic systems powered by large language models (LLMs) have opened new opportunities for business ideation. Yet existing approaches remain confined to a text-only paradigm, despite the inherently multimodal nature of re...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BLADE: Better Language Answers through Dialogue and Explanations](http://arxiv.org/abs/2604.03236v2)
  来源：arXiv | 日期：2026-01-31 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large language model (LLM)-based educational assistants often provide direct answers offering little incentive for students to explore or engage with course materials. We present BLADE (Better Language Answers through Di...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Foam-Agent: A Large Language Model-Based Multi-Agent Framework for Automating Computational Fluid Dynamics Workflows](http://arxiv.org/abs/2505.04997v3)
  来源：arXiv | 日期：2025-05-08 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Computational fluid dynamics (CFD) has been the main workhorse of computational physics, yet its steep learning curve and fragmented, multi-stage workflow create significant barriers to entry. We present Foam-Agent, a mu...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CangjieBench: Benchmarking LLMs on a Low-Resource General-Purpose Programming Language](http://arxiv.org/abs/2603.14501v2)
  来源：arXiv | 日期：2026-03-15 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models excel in high-resource programming languages but struggle with low-resource ones. Existing research related to low-resource programming languages primarily focuses on Domain-Specific Languages (DSLs...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [How Significant Are the Real Performance Gains? An Unbiased Evaluation Framework for GraphRAG](http://arxiv.org/abs/2506.06331v2)
  来源：arXiv | 日期：2025-05-31 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：By retrieving contexts from knowledge graphs, graph-based retrieval-augmented generation (GraphRAG) enhances large language models (LLMs) to generate quality answers for user questions. Many GraphRAG methods have been pr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Intern-S2-Preview: Scientific Agentic Foundation Model](http://arxiv.org/abs/2608.13505v1)
  来源：arXiv | 日期：2026-08-13 | 相关度：3.85 | 新颖度：9.33
  匹配主题：foundation_model_agent
  中文摘要：Scientific discovery increasingly requires AI systems that can reason over scientific evidence of heterogeneous modalities, interact with scientific tools and environments, and sustain progress across long task horizons....
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [A corpus-specific clinical RAG system matches or outperforms newer frontier LLMs on HealthBench](http://arxiv.org/abs/2608.12138v1)
  来源：arXiv | 日期：2026-08-12 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：General-purpose large language models (LLMs) have recently been reported to match or exceed specialized clinical AI tools on medical benchmarks, but such comparisons draw on a narrow set of systems and on benchmarks deve...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Agentic genomics: From pipeline automation to autonomous validation.](https://pubmed.ncbi.nlm.nih.gov/42480539/)
  来源：PubMed | 日期：2026-08-12 | 相关度：7.8 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Genomics has entered a phase in which AI agents can autonomously discover, configure, execute, and chain bioinformatics operations from natural-language instructions. We term this paradigm "agentic genomics": the delegat...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Self-Knowledge Retrieval Augmented Generation Framework for Patent Matching](http://arxiv.org/abs/2608.11030v1)
  来源：arXiv | 日期：2026-08-11 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Patent retrieval and matching based on large language models (LLMs) play a vital role in intellectual property protection. However, due to the complex structure of patent documents, dense technical terminology, and multi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Requirements-Augmented Generation for Trustworthy Acceptance Testing of LLM-Based Software](http://arxiv.org/abs/2608.12970v1)
  来源：arXiv | 日期：2026-08-13 | 相关度：5.45 | 新颖度：6.39
  匹配主题：foundation_model_agent
  中文摘要：LLM-based software (LBS) integrates large language models as core components to deliver flexible, personalised responses. Unlike traditional software with deterministic outputs, LBSs exhibit context-dependent, stochastic...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Privacy-Preserving RAG by Concealing Sensitive Information from External LLMs](http://arxiv.org/abs/2608.12675v1)
  来源：arXiv | 日期：2026-08-13 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) is widely used to improve the performance of Large Language Models (LLMs) in answering user queries. Existing privacy research on RAG has focused on preventing unauthorized users from...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [MuseVLA: An Adaptive Multimodal Sensing Vision-Language-Action Model for Robotic Manipulation](http://arxiv.org/abs/2606.17598v2)
  来源：arXiv | 日期：2026-06-16 | 相关度：6.1 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Humans naturally leverage diverse sensing modalities to interact with the physical world, while most Vision-Language-Action (VLA) models for robotics rely solely on RGB observations. This limits their ability to perceive...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LoongReflect: Boosting Long-Horizon Reflection in Search Agents via Global Perspective Distillation](http://arxiv.org/abs/2608.11967v1)
  来源：arXiv | 日期：2026-08-12 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large language model agents increasingly rely on long-horizon reasoning to solve complex tasks involving planning, tool use, and memory. A critical capability in such settings is reflection: assessing trajectory progress...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Enhancing Linux Privilege Escalation Attack Capabilities of Local LLM Agents](http://arxiv.org/abs/2604.27143v2)
  来源：arXiv | 日期：2026-04-29 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Cloud-based Large Language Models (LLMs) can perform autonomous penetration-testing sub-tasks such as Linux privilege escalation, but raise security, privacy, and sovereignty concerns. Locally hosted open-weight models a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Situation Graph Prediction for User Perspective Modeling](http://arxiv.org/abs/2602.13319v2)
  来源：arXiv | 日期：2026-02-10 | 相关度：2.75 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Perspective-aware AI requires modeling evolving internal states---goals, emotions, contexts---not merely preferences. Progress is limited by a data bottleneck: digital footprints are privacy-sensitive and perspective sta...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ScreenShot: A Foundation Model for Few-Shot Combination Drug Screening](http://arxiv.org/abs/2608.12219v1)
  来源：arXiv | 日期：2026-08-12 | 相关度：2.1 | 新颖度：1.75
  匹配主题：未命中具体主题
  中文摘要：Treating patients with combinations of drugs reduces the risk of resistance to any individual drug. Finding effective combinations is difficult because the large search space makes combinatorial screens prohibitively exp...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LakeQuest: A Three-Domain Benchmark for Grounded Question Answering across Data Lakes](http://arxiv.org/abs/2607.12310v3)
  来源：arXiv | 日期：2026-07-14 | 相关度：2.1 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：While modern question answering (QA) systems excel on clean, schema-aligned corpora, real-world knowledge is rarely so neatly packaged. Answering questions over enterprise and scientific data lakes requires systems to na...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SAG: SQL-Retrieval Augmented Generation with Query-Time Dynamic Hyperedges](http://arxiv.org/abs/2608.12129v1)
  来源：arXiv | 日期：2026-08-12 | 相关度：2.1 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：While retrieval-augmented generation (RAG) has proven effective at giving LLMs access to external knowledge, mainstream dense-retrieval implementations remain inherently limited in handling structured constraints and mul...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Comprehensive Empirical Evaluation of Vector Database Systems for Approximate Nearest Neighbor Search: Performance, Quality, and Resource Trade-offs](http://arxiv.org/abs/2608.12812v1)
  来源：arXiv | 日期：2026-08-13 | 相关度：1.4 | 新颖度：6.7
  匹配主题：未命中具体主题
  中文摘要：Vector databases have emerged as critical infrastructure for modern artificial intelligence applications, particularly retrieval-augmented generation (RAG), semantic search, and recommendation systems. Despite their grow...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OmniScientist: An Omni-Modal Omni-Discipline AI Scientist](http://arxiv.org/abs/2608.13558v1)
  来源：arXiv | 日期：2026-08-13 | 相关度：0.7 | 新颖度：8.16
  匹配主题：未命中具体主题
  中文摘要：Recent advances in foundation models have enabled AI scientists to automate increasingly complete research workflows, from hypothesis generation and code execution to manuscript preparation. Yet workflow coverage alone d...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Mechanist: AI as a Scientific Instrument for Discovering the Mechanisms of Intelligence](http://arxiv.org/abs/2608.12036v1)
  来源：arXiv | 日期：2026-08-12 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：AI models have achieved remarkable success across diverse domains, yet the mechanisms underlying their capabilities and the risks they may pose remain poorly understood. As AI development becomes faster and increasingly ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [The EPS Research Astro-RAG Platform: A Unified Open-Science Infrastructure for Cross-Epoch Astrophysical Kinematic Analysis, LLM-Assisted Research Workflows, and Educational Outreach](http://arxiv.org/abs/2605.30384v2)
  来源：arXiv | 日期：2026-05-28 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Correction (August 2026): A previously reported cross-epoch omega sign reversal was caused by a formula implementation error. Using the corrected canonical equation, all eight Tier-1 Z1 rotators yield positive omega valu...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [When Should Multi-Round RAG Stop? Structured Stopping Judgments and Retrieval Reduction in Search-R1](http://arxiv.org/abs/2608.13237v1)
  来源：arXiv | 日期：2026-08-13 | 相关度：0.7 | 新颖度：6.95
  匹配主题：未命中具体主题
  中文摘要：Multi-round retrieval-augmented generation (RAG) must decide when to stop searching as evidence accumulates. Because the deployed policy is determined by the first STOP on each trajectory, this is a sequential selection ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Query Translation vs. Cross-Lingual Embeddings for Sinhala-Tamil E-Government Information Retrieval](http://arxiv.org/abs/2608.12820v1)
  来源：arXiv | 日期：2026-08-13 | 相关度：0.7 | 新颖度：5.97
  匹配主题：未命中具体主题
  中文摘要：This paper presents a comparative evaluation of cross-lingual information retrieval (CLIR) methods for retrieving English government information using Sinhala and Tamil queries. Two CLIR paradigms are investigated: Query...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [DiG-bench: Discovery in Games](http://arxiv.org/abs/2608.12593v1)
  来源：arXiv | 日期：2026-08-12 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Discovery---formulating novel generalizations---is a central part of the scientific process. Despite its importance, there is a gap in the current AI benchmark landscape, with few benchmarks directly probing the capacity...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [DegradeQuery: Counterfactual Tuple Pretraining for Context-Aware PROTAC Degradation Prediction](http://arxiv.org/abs/2608.10595v1)
  来源：arXiv | 日期：2026-08-11 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Proteolysis-targeting chimeras (PROTACs) induce protein degradation by recruiting a target protein to an E3 ubiquitin ligase, making degradation a joint outcome of the degrader molecule and its biological context. Althou...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Video2Track: From Real-World Interaction Videos to Steerable Adversarial Closed-Track Testing for Automated Driving Systems](http://arxiv.org/abs/2608.11592v1)
  来源：arXiv | 日期：2026-08-12 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Closed-track testing plays a fundamental role in the verification and validation of automated driving systems (ADS), particularly for safety-critical scenarios, by enabling reproducible evaluation under controlled condit...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MatchMiner-AI: Open-source, Privacy-preserving Cancer Clinical Trial Matching using Artificial Intelligence](http://arxiv.org/abs/2412.17228v4)
  来源：arXiv | 日期：2024-12-23 | 相关度：2.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Background: Clinical trials are essential to advancing cancer treatments, but fewer than 10% of adults with cancer enroll in therapeutic trials. Open-source AI trial matching tools could democratize access to trial optio...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Reliability of AI Methods in Drug Discovery: Evaluation of Boltz-2 for Structure and Binding Affinity Prediction.](https://pubmed.ncbi.nlm.nih.gov/42579383/)
  来源：PubMed | 日期：2026-08-11 | 相关度：2.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Despite continuing hype about the role of AI in drug discovery, no "AI-discovered drugs" have so far received regulatory approval. Here we assess one of the latest AI-based tools in this domain. Boltz-2, a recently devel...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Static analysis-guided agentic AI translation enables Rust as a full stack bioinformatics language](http://arxiv.org/abs/2608.13029v1)
  来源：arXiv | 日期：2026-08-13 | 相关度：1.7 | 新颖度：6.33
  匹配主题：未命中具体主题
  中文摘要：The field of bioinformatics struggles with legacy code - old code that is commonly used but may no longer have a maintainer, or may be written in an now-unfamiliar language (e.g. Perl, Fortran). This incurs maintenance c...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [How to Spend Your Oracle Budget: Practical Guidance for Protein Structure Prediction Models](http://arxiv.org/abs/2608.12192v1)
  来源：arXiv | 日期：2026-08-12 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Foundation models for protein structure prediction remain unreliable on certain targets. External oracles can flag and correct these failures, but biological oracles are expensive, making oracle budget a critical constra...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [D3D-GEN: Robot-Aware Domain-Grounded Interactive 3D World Generation for Social Robotics](http://arxiv.org/abs/2608.11876v1)
  来源：arXiv | 日期：2026-08-12 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Training and validation of Embodied AI for social navigation critically depends on realistic simulation environments, yet many current approaches fail to find a balance between realism and simulability. We propose D3D-GE...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CAR: Query-Guided Confidence-Aware Reranking for Retrieval-Augmented Generation](http://arxiv.org/abs/2605.04495v2)
  来源：arXiv | 日期：2026-05-06 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) relies on evidence ranking to determine what information is exposed to the generator, yet existing retrieval and reranking methods primarily estimate query--document relevance. Releva...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Most biomedical publications show signs of LLM-assisted writing](http://arxiv.org/abs/2608.10715v1)
  来源：arXiv | 日期：2026-08-11 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Over the past several years, LLM-powered chatbots and agents have become widely used as a tool for academic writing. LLM-assisted writing can be valuable by removing language barriers but at the same time causes concerns...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [QV-PIC: Query-Aware Visual Position-Independent Caching for Efficient RAG Serving](http://arxiv.org/abs/2608.12121v1)
  来源：arXiv | 日期：2026-08-12 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) repeatedly prefills identical text chunks across queries, incurring redundant computations. Position-Independent Caching (PIC) mitigates it by reusing precomputed Key-Value (KV) acros...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Theranostic innovation in infectious lung diseases: integrating biotechnology and nanotechnology for precision medicine.](https://pubmed.ncbi.nlm.nih.gov/42549821/)
  来源：PubMed | 日期：2026-08-11 | 相关度：4.45 | 新颖度：0.25
  匹配主题：pathogenomics, application_monitoring
  中文摘要：Infectious lung diseases, such as pneumonia, tuberculosis, COVID-19, influenza, and emerging fungal infections, are major causes of illness and death worldwide. Traditional methods have serious limitations such as diagno...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [PCR and molecular diagnostics: Biotechnologic integration in clinical laboratories.](https://pubmed.ncbi.nlm.nih.gov/42586250/)
  来源：PubMed | 日期：2026-08-12 | 相关度：3.45 | 新颖度：5.25
  匹配主题：pathogenomics, application_monitoring
  中文摘要：A new generation of molecular tests has revolutionized laboratory medicine through allowing for quick, sensitive, and precise identification of the pathogen; genetic mutation or alteration; and disease-related bio-marker...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Machine learning for population-level risk prediction of future cholangiocarcinoma.](https://pubmed.ncbi.nlm.nih.gov/42585990/)
  来源：PubMed | 日期：2026-08-12 | 相关度：3.05 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：The poor prognosis of cholangiocarcinoma (CCA) is largely driven by rapid, asymptomatic disease progression, which usually results in a late diagnosis in the absence of established screening strategies. An early, cost-ef...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial intelligence in pediatric medical genetics and genomics.](https://pubmed.ncbi.nlm.nih.gov/42516066/)
  来源：PubMed | 日期：2026-08-11 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：人工智能（AI）正迅速且不均衡地融入医学及社会各领域。本综述重点探讨了 AI 在儿科基因组学领域的最新进展。文章阐述了 AI 及其子类型的通用定义，并介绍了最新的 AI 应用。随后，文章概述了 AI 在儿科基因组学多个环节的应用与测试，包括：识别潜在遗传病患者并辅助诊断过程；在实验室遗传检测流程中的实施；以及 AI 如何支持患者管理、新药发现及遗传病治疗研究。总体而言，AI 正以多种方式应用于儿科基因组学，该领域将因 AI 发生剧变。本...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Who Speaks Matters: Authority-Aware Multi-View RAG over Italian Parliamentary Proceedings](http://arxiv.org/abs/2608.13410v1)
  来源：arXiv | 日期：2026-08-13 | 相关度：0.7 | 新颖度：7.35
  匹配主题：未命中具体主题
  中文摘要：Parliamentary proceedings are a primary record of democratic deliberation, yet their volume and fragmentation make multi-perspective access difficult for citizens, journalists, and researchers. Applying Retrieval-Augment...
  为什么值得看：Who Speaks Matters: Authority-Aware Mult 与你的主题有弱匹配，暂时保留作低优先级跟踪。

- [GEM: A Generative Embedding Model Bridging Reasoning and Retrieval](http://arxiv.org/abs/2608.13200v1)
  来源：arXiv | 日期：2026-08-13 | 相关度：0.7 | 新颖度：6.84
  匹配主题：未命中具体主题
  中文摘要：Modern LLMs excel at reasoning and instruction following, enabling users to express complex and diverse information needs. However, conventional retrievers largely rely on surface-level matching between queries and docum...
  为什么值得看：GEM: A Generative Embedding Model Bridgi 与你的主题有弱匹配，暂时保留作低优先级跟踪。
