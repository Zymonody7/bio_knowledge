# 每日论文监控日报 (2026-08-20)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 59 篇新论文。

## 抓取状态

- arXiv：成功，命中 50 篇
- PubMed：成功，命中 54 篇
- bioRxiv：成功，命中 7 篇
- medRxiv：成功，命中 21 篇

## 最值得看

### Foundation Model / Agent

- [Modality-chain reasoning enables multimodal protein modelling and design](https://www.biorxiv.org/content/10.1101/2025.07.21.665832v3)
  来源：bioRxiv | 日期：2026-08-18 | 相关度：10.0 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Reasoning has emerged as a central capability of large language models, yet how it should be formulated for scientific foundation models remains unclear because scientific knowledge is distributed across interdependent, ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Reducing Technician Search Burden: A Multimodal RAG for Cessna 172 Maintenance Manual](http://arxiv.org/abs/2608.18465v1)
  来源：arXiv | 日期：2026-08-19 | 相关度：7.9 | 新颖度：6.05
  匹配主题：foundation_model_agent
  中文摘要：Proper use of the aircraft maintenance manual is essential for correct maintenance, providing procedures, diagrams, cautions, and specifications. However, technicians often avoid consulting it because it is difficult to ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Comprehensive Review of Large Language Models for Nanophotonics: From Surrogate Modeling to Autonomous Design](http://arxiv.org/abs/2608.18279v1)
  来源：arXiv | 日期：2026-08-18 | 相关度：7.5 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Metasurfaces have revolutionized the development of photonic devices by enabling unprecedented precision in light manipulation. However, their design processes are often constrained by computationally expensive simulatio...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [From Output Errors to Workflow Harm: A Practitioner-Audit Method for LLM-Mediated Research](https://www.medrxiv.org/content/10.64898/2026.08.13.26360414v1)
  来源：medRxiv | 日期：2026-08-17 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：ObjectiveFormal large language model (LLM) evaluations score isolated prompts, but clinicians and health-informatics researchers meet model failures inside multi-step workflows where erroneous output can alter procedures...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TTSD-FAR: Test-Time Self-Distillation with Fisher-Anchored Restoration for Missing-Modality Emotion Recognition in LVLMs](http://arxiv.org/abs/2608.18386v1)
  来源：arXiv | 日期：2026-08-18 | 相关度：7.5 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large video-language models (LVLMs) have shown remarkable performance on multimodal tasks like multimodal emotion recognition (ER) in the wild. ER is inherently multimodal, requiring a joint understanding of facial expre...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multimodal Language Models Benchmarked Against the NRC Reactor Operator Licensing Examination: Fine-Tuning and Retrieval Strategies](http://arxiv.org/abs/2607.22067v2)
  来源：arXiv | 日期：2026-07-24 | 相关度：7.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Competence claims for a language model in a safety-critical domain are credible when measured against a standard the domain already enforces. We evaluate an open-weight 31-billion-parameter multimodal model (Gemma 4 31B-...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SMA: Who Said That? Auditing Membership Leakage in Semi-Black-box RAG Controlling](http://arxiv.org/abs/2508.09105v3)
  来源：arXiv | 日期：2025-08-12 | 相关度：7.5 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) and its Multimodal Retrieval-Augmented Generation (MRAG) significantly improve the knowledge coverage and contextual understanding of Large Language Models (LLMs) by introducing exter...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Large Language Models Generate Stigmatizing Language During Reasoning Over Real-World Clinical Data](https://www.medrxiv.org/content/10.64898/2026.08.12.26360210v2)
  来源：medRxiv | 日期：2026-08-19 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Stigmatizing language in clinical documentation, which conveys negative stereotypes, attitudes, or judgments toward patients, is a recognized source of documentation bias and is associated with poorer care and adverse he...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A contextualised protein language model reveals the functional syntax of bacterial evolution](https://www.biorxiv.org/content/10.1101/2025.07.20.665723v3)
  来源：bioRxiv | 日期：2026-08-17 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Bacteria have evolved a vast diversity of functions and behaviours that are currently incompletely understood and poorly predicted from DNA sequence alone. To understand the syntax of bacterial evolution and discover gen...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ReasFlow: Assisting Reasoning-Centric Scientific Discovery in Applied Mathematics via a Knowledge-Based Multi-Agent System](http://arxiv.org/abs/2607.14178v3)
  来源：arXiv | 日期：2026-07-15 | 相关度：6.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in Large Language Models have fueled autonomous AI agents capable of tackling complex scientific tasks, yet existing automated research systems remain predominantly focused on empirically driven domains w...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Automating Parent Selection Configuration in Genetic Programming with Agentic AI](http://arxiv.org/abs/2608.17172v1)
  来源：arXiv | 日期：2026-08-17 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：We investigate whether agentic artificial intelligence can automate parts of the process of designing genetic programming systems by introducing an agentic framework that identifies and implements parent selection algori...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MITRE-SAGE: A Multi-Agent Cybersecurity Question-Answering Model](http://arxiv.org/abs/2608.16921v2)
  来源：arXiv | 日期：2026-08-03 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Effective cybersecurity operations require timely and accurate analysis of large-scale heterogeneous security information; however, analysts increasingly struggle with information overload, alert fatigue, and time-constr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Storage to Access: Verifiable Activation of Parametric Knowledge in LLMs via Explicit Priming and Implicit Reasoning](http://arxiv.org/abs/2608.18581v1)
  来源：arXiv | 日期：2026-08-19 | 相关度：4.75 | 新颖度：6.91
  匹配主题：foundation_model_agent
  中文摘要：Although Large Language Models (LLMs) encode rich factual knowledge in their parameters, reliably recalling and verifying such knowledge remains a key bottleneck in factual question answering. Existing end-to-end methods...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [MTS-Bench: A Manchester Triage System Benchmark for Language Model Triage Safety](https://www.medrxiv.org/content/10.64898/2026.08.04.26359651v2)
  来源：medRxiv | 日期：2026-08-18 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：BackgroundGeneral purpose language models such as ChatGPT are increasingly used by physicians and triage nurses during emergency triage. A recent study reported 51.6% undertriage of emergencies when patients queried Chat...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Event-Causal RAG: A Retrieval-Augmented Generation Framework for Long Video Reasoning in Complex Scenarios](http://arxiv.org/abs/2605.06185v2)
  来源：arXiv | 日期：2026-05-07 | 相关度：4.75 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Large vision-language models perform well on short- and medium-length video understanding but still struggle to maintain coherent event memory and recover long-range relationships in ultra-long videos. End-to-end methods...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [SINDI: An Efficient Index for Sparse Vector Approximate Maximum Inner Product Search](http://arxiv.org/abs/2509.08395v4)
  来源：arXiv | 日期：2025-09-10 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Sparse vector Maximum Inner Product Search (MIPS) is crucial in multi-path retrieval for Retrieval-Augmented Generation (RAG). Recent inverted index-based and graph-based algorithms have achieved high search accuracy wit...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Retrieval-Augmented Large Language Models for Clinically Aligned Adverse Event Coding in Acute Myeloid Leukemia Clinical Trials](https://www.medrxiv.org/content/10.64898/2026.08.17.26360282v1)
  来源：medRxiv | 日期：2026-08-18 | 相关度：7.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Background: Adverse event (AE) coding is essential for safety monitoring in oncology clinical trials, particularly in acute myeloid leukemia (AML), where intensive therapies are associated with frequent and heterogeneous...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ChatPlanner: A Large Language Model Framework for Personalized Public Transit Routing](http://arxiv.org/abs/2606.15315v2)
  来源：arXiv | 日期：2026-06-13 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Personalized public transit routing in public transit systems remains challenging due to the difficulty of capturing and integrating diverse user preferences into routing algorithms. This paper presents ChatPlanner, a no...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Off-Manifold Collapse in Guided Protein Language Models](http://arxiv.org/abs/2608.18597v1)
  来源：arXiv | 日期：2026-08-19 | 相关度：5.75 | 新颖度：5.97
  匹配主题：foundation_model_agent
  中文摘要：Protein language models are widely used priors for protein sequence design, and a growing body of work controls them at inference time as an alternative to fine-tuning. Such guidance faces a dilemma: mild enough to prese...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Learning What to Fail On: Failure-Mode Contextual Bandits for Adversarial Data Curation](http://arxiv.org/abs/2608.18681v1)
  来源：arXiv | 日期：2026-08-19 | 相关度：4.75 | 新颖度：6.77
  匹配主题：foundation_model_agent
  中文摘要：We introduce a failure-aware adversarial retrieval-augmented framework for improving robustness in natural language understanding. Rather than selecting synthetic examples with a fixed reward threshold, our method formul...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [CACSurv: Concordance-Aligned Comparative Learning with Large Language Models for Cancer Survival Prediction](http://arxiv.org/abs/2608.16594v1)
  来源：arXiv | 日期：2026-08-17 | 相关度：7.8 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Cancer survival prediction supports treatment planning, risk stratification, and follow-up management. Existing methods use structured clinical variables, whole-slide images, genomic profiles, or multimodal inputs, while...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [From Lectures to Learning Outcomes: Meaningful Integration of AI-Generated Content in Pre-Clerkship Medical Training](https://www.medrxiv.org/content/10.1101/2025.05.13.25327518v2)
  来源：medRxiv | 日期：2026-08-17 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Background Large Language Models (LLMs) can efficiently synthesize educational content, yet few studies have evaluated standardized, LLM-powered curricular interventions and their effects on medical student learning. Met...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SGHA: Evidence-Grounded Research Problem Discovery with Local Language Models](http://arxiv.org/abs/2608.17501v1)
  来源：arXiv | 日期：2026-08-18 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Recent efforts toward fully automated AI scientists have demonstrated that language-model agents can generate hypotheses, execute experiments, and draft scientific manuscripts. However, during the early stages of researc...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [REFINE: Closing the Loop Between Large Language Models and Symbolic Rules in Clinical NLP](https://www.medrxiv.org/content/10.64898/2026.08.11.26360118v1)
  来源：medRxiv | 日期：2026-08-17 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Symbolic clinical natural language processing (NLP) systems remain widely used for extracting clinical concepts from electronic health record (EHR) narratives, but maintaining rule resources requires extensive manual err...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PertMind: Eliciting Emergent Biological Reasoning in LLM via Reinforcement Learning on Cellular Perturbation Data](http://arxiv.org/abs/2608.16419v1)
  来源：arXiv | 日期：2026-08-17 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models can describe mechanisms, yet scalable post-training still depends on costly, manually curated biological reasoning traces. Here we show that cellular perturbation atlases can instead become reinforc...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Do Large Language Models Play Six Degrees of Separation? Measuring Topological Compression in Long-Context Manifolds](http://arxiv.org/abs/2608.17950v1)
  来源：arXiv | 日期：2026-08-18 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) demonstrate remarkable multi-hop reasoning capabilities over long contexts, yet the internal mechanisms enabling these distant cognitive leaps remain poorly understood. Traditional attention-...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Towards Safer RAG: Only Agents Capable of System 2 Thinking may Access Untrusted Documents](http://arxiv.org/abs/2608.17153v1)
  来源：arXiv | 日期：2026-08-17 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) has significantly enhanced the performance of large language models (LLMs), yet these systems remain vulnerable to knowledge-poisoning attacks, in which misinformation in retrieved do...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Self-Reported Side Effects Among Reddit Users Taking Nonapproved Retatrutide](https://www.medrxiv.org/content/10.64898/2026.05.28.26352819v2)
  来源：medRxiv | 日期：2026-08-18 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Gray-market retatrutide use is increasing, but patient safety experiences remain poorly characterized. This cross-sectional analysis examined Reddit posts and comments from retatrutide-specific and broader peptide or wei...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [H$^{2}$MT: Semantic Hierarchy-Aware Hierarchical Memory Transformer](http://arxiv.org/abs/2605.24930v2)
  来源：arXiv | 日期：2026-05-24 | 相关度：2.75 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Transformer-based LLMs achieve strong results on many language tasks; however, long inputs remain challenging because context windows are finite, and prefill latency and memory grow rapidly with prompt length. Flat token...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CanLegalRAGBench: Evaluating Retrieval-Augmented Generation on Canadian Case Law](http://arxiv.org/abs/2605.30497v2)
  来源：arXiv | 日期：2026-05-28 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：RAG-based legal assistants have been growing in popularity, but LLM hallucinations remain a key issue and potentially undermines justice. While benchmarks have been developed to evaluate progress, many rely on synthetic ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CTIFoundry: An Agent-Native Corpus Scaffold for Cyber Threat Intelligence](http://arxiv.org/abs/2608.18613v1)
  来源：arXiv | 日期：2026-08-19 | 相关度：0.7 | 新颖度：6.52
  匹配主题：未命中具体主题
  中文摘要：Cyber threat intelligence (CTI) is increasingly consumed not by human analysts but by LLM agents that compose multi-step investigations at query time. The harness side of this shift has matured rapidly (planning loops, t...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Mechanist: AI as a Scientific Instrument for Discovering the Mechanisms of Intelligence](http://arxiv.org/abs/2608.12036v2)
  来源：arXiv | 日期：2026-08-12 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：AI models have achieved remarkable success across diverse domains, yet the mechanisms underlying their capabilities and the risks they may pose remain poorly understood. As AI development becomes faster and increasingly ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CABLE: Extending the Reach of Memory Retrieval via Complementary Antecedent-Based Linking and Expansion](http://arxiv.org/abs/2608.17911v1)
  来源：arXiv | 日期：2026-08-18 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：As LLM agents operate across structured workflows and sessions, preserving long-term history does not ensure that later contexts can recover relevant evidence through a bounded memory interface. We study this evidence-re...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [GEqTrain: A Configuration-Driven Framework for Retargeting Equivariant Graph Neural Networks Across 3D Scientific Tasks](http://arxiv.org/abs/2607.19083v3)
  来源：arXiv | 日期：2026-07-21 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Equivariant graph neural networks provide a powerful modeling language for three-dimensional scientific data, but their reuse is often limited by implementations tied to specific tasks, outputs, and training regimes. We ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [SimulRAG: Simulator-based RAG for Grounding LLMs in Long-form Scientific QA](http://arxiv.org/abs/2509.25459v4)
  来源：arXiv | 日期：2025-09-29 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) show promise in generating long-form scientific explanations that synthesize evidence and connect multiple factors. However, in long-form scientific question answering, LLMs often hallucinate...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [MissDiag: Diagnostic Evaluation of Incomplete-Knowledge Robustness in KGQA and KG-RAG](http://arxiv.org/abs/2608.18489v1)
  来源：arXiv | 日期：2026-08-19 | 相关度：0.7 | 新颖度：5.93
  匹配主题：未命中具体主题
  中文摘要：Knowledge graph question answering (KGQA) and knowledge-graph-based retrieval-augmented generation (KG-RAG) aim to ground answers in explicit graph evidence, but real-world knowledge graphs are often sparse, outdated, an...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Efficient exploration of sequence space enables rapid generation of functional genome editors](https://www.biorxiv.org/content/10.64898/2026.08.16.745112v1)
  来源：bioRxiv | 日期：2026-08-17 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：The problem of how protein sequences translate into defined functions remains largely unsolved despite decades of progress. New methods to efficiently explore protein sequence space will help to shed light on these seque...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Fine-Grained Structural Classification of Biosynthetic Gene Cluster-Encoded Products.](https://pubmed.ncbi.nlm.nih.gov/42606533/)
  来源：PubMed | 日期：2026-08-17 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Biosynthetic gene clusters (BGCs) are responsible the biosynthesis of many natural products, including a multitude of effective therapeutics and their precursors. Advances in genomic data collection as well as computatio...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [How to make the most of your masked language model for protein engineering](http://arxiv.org/abs/2603.10302v3)
  来源：arXiv | 日期：2026-03-11 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：A plethora of protein language models have been released in recent years. Yet comparatively little work has addressed how to best sample from them to optimize desired biological properties. We fill this gap by proposing ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [DSPrompt: Dynamic Soft Prompt Defense Against M-RAG Corruption](http://arxiv.org/abs/2608.16536v1)
  来源：arXiv | 日期：2026-08-17 | 相关度：3.45 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Multimodal Retrieval Augmented Generation (M-RAG) is increasingly vulnerable to adversarial attacks where malicious data are crafted to produce embeddings that align with benign entries in the vector space, deceiving ret...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Spatial omics illuminates tumor heterogeneity.](https://pubmed.ncbi.nlm.nih.gov/42320479/)
  来源：PubMed | 日期：2026-08-17 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Intratumoral heterogeneity (ITH) is the coexistence of diverse cancer cell states, genotypes, and microenvironmental niches within a single tumor and is a major driver of therapeutic resistance and disease progression. W...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Hypergraph-based Multimodal Retrieval-Augmented Generation with Incremental Refinement](http://arxiv.org/abs/2608.16628v1)
  来源：arXiv | 日期：2026-08-17 | 相关度：2.75 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Modern Multimodal Retrieval-Augmented Generation (M-RAG) systems are fundamentally limited by the binary connectivity paradigm of traditional simple graphs, which fails to capture the intricate, high-order correlations a...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Predicting the Benefit of Retrieval Augmentation in Open-Domain Question Answering](http://arxiv.org/abs/2604.07985v3)
  来源：arXiv | 日期：2026-04-09 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：While retrieval augmented generation has become a common approach for enhancing question answering systems, retrieval is not universally advantageous. We study the problem of predicting whether incorporating external ret...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Parametric Knowledge in RAG-SFT for Domain-Specific Document Generation](http://arxiv.org/abs/2603.23047v2)
  来源：arXiv | 日期：2026-03-24 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) fine-tuning has shown substantial improvements over vanilla RAG, yet most studies target document question answering, leaving open whether these gains transfer to specialized tasks. W...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CLAIR-Fin: An Adversarial Multi-Agent Framework for Claim-Level Verification and Adaptive Debate in Cross-Modal Financial QA](http://arxiv.org/abs/2608.13706v2)
  来源：arXiv | 日期：2026-08-13 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Existing defenses against hallucination in retrieval-augmented and multi-agent pipelines remain partial: evidence is trusted despite modality disagreement, debate verifies an aggregate report rather than individual claim...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MERIT: Efficient In-Place Deletion for Dynamic Graph-Based Approximate Nearest Neighbor Indexes](http://arxiv.org/abs/2607.29173v3)
  来源：arXiv | 日期：2026-07-31 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Graph-based indexes have become the dominant approach to approximate nearest neighbor search (ANNS) over high-dimensional data and play a crucial role in real-world applications such as retrieval-augmented generation, re...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [How Do Agents Fail on AutoResearch: End-to-End Diagnostic Evaluation on 100 Real-World Frontier Research Tasks](http://arxiv.org/abs/2608.14905v2)
  来源：arXiv | 日期：2026-08-14 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：AI has long assisted scientific research, but the rapid advance of LLMs and agentic scaffolds is reshaping the landscape; a single system can now carry whole-stage research from an initial hypothesis all the way to final...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CoAL-RAG: A Complexity-Aware Legal Retrieval-Augmented Generation Method](http://arxiv.org/abs/2608.17536v1)
  来源：arXiv | 日期：2026-08-18 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Legal consultation questions exhibit multi-level complexity. A single retrieval strategy often leads to over-reasoning for simple questions and poor interpretability for complex ones, making it difficult to meet the requ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SAKE: Structured Agentic Knowledge Extrapolation for Complex LLM Reasoning via Reinforcement Learning](http://arxiv.org/abs/2505.15062v6)
  来源：arXiv | 日期：2025-05-21 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Knowledge extrapolation is the process of inferring novel information by combining and extending existing knowledge that is explicitly available. It is essential for solving complex questions in specialized domains where...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [VDGR-RAG: Vectors, Directories, Graphs, and Reflection Are All You Need for Unified Reasoning over Hierarchical Enterprise Knowledge](http://arxiv.org/abs/2608.07994v2)
  来源：arXiv | 日期：2026-08-08 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) is essential for enterprise knowledge question answering (QA), particularly in domains with complex product documentation like telecommunications. However, existing RAG approaches lar...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Performance of an Ambient Generative AI Documentation Tool in a Linguistically Diverse Clinical Setting](https://www.medrxiv.org/content/10.64898/2026.08.14.26360467v1)
  来源：medRxiv | 日期：2026-08-17 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Ambient artificial intelligence scribes are being increasingly used in healthcare to improve efficiency and reduce provider clinical documentation burden, yet their performance across linguistically diverse patient popul...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [An injection-molded focal filter-integrated AI platform for cost-effective and highly sensitive molecular point-of-care testing.](https://pubmed.ncbi.nlm.nih.gov/42610358/)
  来源：PubMed | 日期：2026-08-18 | 相关度：2.7 | 新颖度：0.25
  匹配主题：pathogenomics
  中文摘要：The growing global demand for precise and accessible diagnostics underscores the need for decentralized, laboratory-grade molecular testing solutions. Current platforms are hindered by the high cost and fragility of glas...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Research progress of AI assisted nano-SERS technology in rapid identification of multi species oral pathogenic biofilms.](https://pubmed.ncbi.nlm.nih.gov/42613464/)
  来源：PubMed | 日期：2026-08-19 | 相关度：2.45 | 新颖度：5.75
  匹配主题：application_monitoring
  中文摘要：Complex multispecies microbial communities that are oral pathogenic biofilms are linked to significant oral infections, such as dental caries, periodontitis, peri-implantitis, and chronic endodontic infection. In order t...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial intelligence for predicting BCG response in non-muscle-invasive bladder cancer: a systematic review.](https://pubmed.ncbi.nlm.nih.gov/42605566/)
  来源：PubMed | 日期：2026-08-17 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：To systematically identify, appraise and synthesise artificial intelligence (AI) and machine-learning (ML) models that predict treatment response and clinical outcomes after intravesical bacillus Calmette-Guérin (BCG) in...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [COMA: A Compositional Misleading Attack Class on Security-RAG, and a Causal Counterfactual Defense](http://arxiv.org/abs/2608.17960v1)
  来源：arXiv | 日期：2026-08-18 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Every document a security copilot retrieves can be true, instruction-free, and non-contradictory --- and the copilot can still be driven to assess a critical, exploitable vulnerability correctly and then recommend a reme...
  为什么值得看：COMA: A Compositional Misleading Attack  与你的主题有弱匹配，暂时保留作低优先级跟踪。

- [GRIP: Grounded Reasoning via Information-Restricted Premises](http://arxiv.org/abs/2608.16776v2)
  来源：arXiv | 日期：2026-08-17 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：High-capacity encoders in retrieval-augmented generation (RAG) can let the query dominate the latent state, leaving retrieved evidence functionally irrelevant. We call this failure mode query dominance. To address it, we...
  为什么值得看：GRIP: Grounded Reasoning via Information 与你的主题有弱匹配，暂时保留作低优先级跟踪。

- [Empowering Polymeric Materials Discovery by Artificial Intelligence](http://arxiv.org/abs/2606.20753v2)
  来源：arXiv | 日期：2026-06-18 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Polymeric materials underpin modern technologies spanning energy storage, microelectronics, healthcare and sustainable manufacturing. Yet their rational design remains exceptionally challenging because material performan...
  为什么值得看：Empowering Polymeric Materials Discovery 与你的主题有弱匹配，暂时保留作低优先级跟踪。

- [Preference Is Not Intervention: The Structure and Stability Boundaries of Reader-Specific Evidence Utility](http://arxiv.org/abs/2608.17781v1)
  来源：arXiv | 日期：2026-08-18 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：ML systems increasingly condition decisions on downstream model identity, but this is useful only if model-specific differences form reusable structure rather than input-local interactions. We test this in retrieval-augm...
  为什么值得看：Preference Is Not Intervention: The Stru 与你的主题有弱匹配，暂时保留作低优先级跟踪。

- [Quo Vadis? Scientific Discovery in the Age of Artificial Intelligence](http://arxiv.org/abs/2608.17970v1)
  来源：arXiv | 日期：2026-08-18 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：This paper examines the growing role of AI in scientific discovery. It first surveys the rapid rise of AI capabilities, especially in reasoning, abstraction, planning, and long-horizon task execution, before turning to s...
  为什么值得看：Quo Vadis? Scientific Discovery in the A 与你的主题有弱匹配，暂时保留作低优先级跟踪。
