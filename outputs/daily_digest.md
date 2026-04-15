# 每日论文监控日报 (2026-04-15)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 51 篇新论文。

## 抓取状态

- arXiv：成功，命中 46 篇
- PubMed：成功，命中 30 篇
- bioRxiv：成功，命中 10 篇
- medRxiv：成功，命中 7 篇

## 最值得看

### Foundation Model / Agent

- [CALM-VLM: CALIBRATION AND SELECTIVE PREDICTION IN VISION-LANGUAGE MODELS FOR RELIABLE BRAIN MRI CLASSIFICATION](https://www.biorxiv.org/content/10.64898/2026.04.10.717865v1)
  来源：bioRxiv | 日期：2026-04-14 | 相关度：8.5 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in vision-language models (VLMs) have demonstrated strong multimodal capabilities for medical image analysis. However, their confidence in diagnostic predictions is often unclear, limiting adoption in cli...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Generation-Augmented Generation: A Plug-and-Play Framework for Private Knowledge Injection in Large Language Models](http://arxiv.org/abs/2601.08209v4)
  来源：arXiv | 日期：2026-01-13 | 相关度：7.5 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：In domains such as materials science, biomedicine, and finance, high-stakes deployment of large language models (LLMs) requires injecting private, domain-specific knowledge that is proprietary, fast-evolving, and under-r...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DocSeeker: Structured Visual Reasoning with Evidence Grounding for Long Document Understanding](http://arxiv.org/abs/2604.12812v1)
  来源：arXiv | 日期：2026-04-14 | 相关度：6.8 | 新颖度：7.74
  匹配主题：foundation_model_agent
  中文摘要：Existing Multimodal Large Language Models (MLLMs) suffer from significant performance degradation on the long document understanding task as document length increases. This stems from two fundamental challenges: 1) a low...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [NaviRAG: Towards Active Knowledge Navigation for Retrieval-Augmented Generation](http://arxiv.org/abs/2604.12766v1)
  来源：arXiv | 日期：2026-04-14 | 相关度：6.55 | 新颖度：8.15
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) typically relies on a flat retrieval paradigm that maps queries directly to static, isolated text segments. This approach struggles with more complex tasks that require the conditiona...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [WikiSeeker: Rethinking the Role of Vision-Language Models in Knowledge-Based Visual Question Answering](http://arxiv.org/abs/2604.05818v2)
  来源：arXiv | 日期：2026-04-07 | 相关度：7.5 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Multi-modal Retrieval-Augmented Generation (RAG) has emerged as a highly effective paradigm for Knowledge-Based Visual Question Answering (KB-VQA). Despite recent advancements, prevailing methods still primarily depend o...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AdversarialCoT: Single-Document Retrieval Poisoning for LLM Reasoning](http://arxiv.org/abs/2604.12201v1)
  来源：arXiv | 日期：2026-04-14 | 相关度：6.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) enhances large language model (LLM) reasoning by retrieving external documents, but also opens up new attack surfaces. We study knowledge-base poisoning attacks in RAG, where an attac...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Pipette: Encoding scientific literature into an executable Skill Graph for multi-agent bioinformatics](https://www.biorxiv.org/content/10.64898/2026.04.08.717332v1)
  来源：bioRxiv | 日期：2026-04-12 | 相关度：6.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：The cost of genomic sequencing has fallen by several orders of magnitude, yet data analysis remains a bottleneck concentrated among researchers with specialized computational expertise. While Large Language Models can ge...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ALL-FEM: Agentic Large Language models Fine-tuned for Finite Element Methods](http://arxiv.org/abs/2603.21011v2)
  来源：arXiv | 日期：2026-01-08 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Finite element (FE) analysis guides the design and verification of nearly all manufactured objects. It is at the core of computational engineering, enabling simulation of complex physical systems, from fluids and solids ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic Discovery with Active Hypothesis Exploration for Visual Recognition](http://arxiv.org/abs/2604.12999v1)
  来源：arXiv | 日期：2026-04-14 | 相关度：5.45 | 新颖度：7.72
  匹配主题：foundation_model_agent
  中文摘要：We introduce HypoExplore, an agentic framework that formulates neural architecture discovery for visual recognition as a hypothesis-driven scientific inquiry. Given a human-specified high-level research direction, HypoEx...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Thought-Retriever: Don't Just Retrieve Raw Data, Retrieve Thoughts for Memory-Augmented Agentic Systems](http://arxiv.org/abs/2604.12231v1)
  来源：arXiv | 日期：2026-04-14 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have transformed AI research thanks to their powerful internal capabilities and knowledge. However, existing LLMs still fail to effectively incorporate the massive external knowledge when int...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Think Parallax: Solving Multi-Hop Problems via Multi-View Knowledge-Graph-Based Retrieval-Augmented Generation](http://arxiv.org/abs/2510.15552v4)
  来源：arXiv | 日期：2025-10-17 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) still struggle with multi-hop reasoning over knowledge-graphs (KGs), and we identify a previously overlooked structural reason for this difficulty: Transformer attention heads naturally speci...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Safety at Scale: A Comprehensive Survey of Large Model and Agent Safety](http://arxiv.org/abs/2502.05206v6)
  来源：arXiv | 日期：2025-02-02 | 相关度：4.75 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：The rapid advancement of large models, driven by their exceptional abilities in learning and generalization through large-scale pre-training, has reshaped the landscape of Artificial Intelligence (AI). These models are n...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OctoTools: An Agentic Framework with Extensible Tools for Complex Reasoning](http://arxiv.org/abs/2502.11271v2)
  来源：arXiv | 日期：2025-02-16 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Solving complex reasoning tasks may involve visual understanding, domain knowledge retrieval, numerical calculation, and multi-step reasoning. Existing methods augment large language models (LLMs) with external tools but...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EMBER: Autonomous Cognitive Behaviour from Learned Spiking Neural Network Dynamics in a Hybrid LLM Architecture](http://arxiv.org/abs/2604.12167v1)
  来源：arXiv | 日期：2026-04-14 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：We present (Experience-Modulated Biologically-inspired Emergent Reasoning), a hybrid cognitive architecture that reorganises the relationship between large language models (LLMs) and memory: rather than augmenting an LLM...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Benchmarking Foundation Models with Retrieval-Augmented Generation in Olympic-Level Physics Problem Solving](http://arxiv.org/abs/2510.00919v3)
  来源：arXiv | 日期：2025-10-01 | 相关度：6.8 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) with foundation models has achieved strong performance across diverse tasks, but their capacity for expert-level reasoning-such as solving Olympiad-level physics problems-remains larg...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Transforming External Knowledge into Triplets for Enhanced Retrieval in RAG of LLMs](http://arxiv.org/abs/2604.12610v1)
  来源：arXiv | 日期：2026-04-14 | 相关度：4.75 | 新颖度：7.48
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) mitigates hallucination in large language models (LLMs) by incorporating external knowledge during generation. However, the effectiveness of RAG depends not only on the design of the ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Prompt-Only Gene-Circuit Modeling with a Large Language Model Simulates the synNotch Spheroids.](https://pubmed.ncbi.nlm.nih.gov/41968604/)
  来源：PubMed | 日期：2026-04-12 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Morphogenesis emerges from gene regulatory circuits that translate biochemical cues into spatially organized cell fates; yet, constructing quantitative simulations of these processes remains technically demanding. Here, ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [TriFit: Trimodal Fusion with Protein Dynamics for Mutation Fitness Prediction](http://arxiv.org/abs/2604.12026v1)
  来源：arXiv | 日期：2026-04-13 | 相关度：7.1 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Predicting the functional impact of single amino acid substitutions (SAVs) is central to understanding genetic disease and engineering therapeutic proteins. While protein language models and structure-based methods have ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Multi-Agent Orchestration for Knowledge Extraction and Retrieval: AI Expert System for GPCRs](https://www.biorxiv.org/content/10.64898/2026.04.10.696782v1)
  来源：bioRxiv | 日期：2026-04-14 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：We present GPCR-Nexus, an AI-driven platform for integrated exploration of G protein coupled receptor (GPCR) biology that unifies structured databases with unstructured scientific literature. The system combines a GPCR /...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A transcriptomics-native foundation model for universal cell representation and virtual cell synthesis](https://www.biorxiv.org/content/10.64898/2026.04.12.718016v1)
  来源：bioRxiv | 日期：2026-04-14 | 相关度：5.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Current single-cell foundation models rely on language-model architectures that ignore transcriptomic data distributions, often underperforming specialized methods. We introduce xVERSE, a transcriptomics-native foundatio...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Towards Autonomous Mechanistic Reasoning in Virtual Cells](http://arxiv.org/abs/2604.11661v2)
  来源：arXiv | 日期：2026-04-13 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have recently gained significant attention as a promising approach to accelerate scientific discovery. However, their application in open-ended scientific domains such as biology remains limi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [LLM-Driven Target Trial Emulation with Human-in-the-Loop Validation for Randomized Trial: Automated Protocol Extraction and Real-World Outcome Evaluation{Psi}](https://www.medrxiv.org/content/10.64898/2026.04.09.26350523v1)
  来源：medRxiv | 日期：2026-04-13 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Target trial emulation (TTE) enables causal inference from observational data but remains bottlenecked by manual, expert-dependent protocol operationalization. While large language models (LLMs) have advanced clinical kn...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GRASP: Gene-relation adaptive soft prompt for scalable and generalizable gene network inference with large language models](https://www.biorxiv.org/content/10.1101/2025.10.20.683485v2)
  来源：bioRxiv | 日期：2026-04-14 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Gene networks (GNs) encode diverse molecular relationships and are central to interpreting cellular function and disease. The heterogeneity of interaction types has led to computational methods specialized for particular...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Representation geometry shapes task performance in vision-language modeling for CT enterography](http://arxiv.org/abs/2604.13021v1)
  来源：arXiv | 日期：2026-04-14 | 相关度：5.45 | 新颖度：7.78
  匹配主题：foundation_model_agent
  中文摘要：Computed tomography (CT) enterography is a primary imaging modality for assessing inflammatory bowel disease (IBD), yet the representational choices that best support automated analysis of this modality are unknown. We p...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Advancing Multi-Agent RAG Systems with Minimalist Reinforcement Learning](http://arxiv.org/abs/2505.17086v4)
  来源：arXiv | 日期：2025-05-20 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) equipped with modern Retrieval-Augmented Generation (RAG) systems often employ multi-turn interaction pipelines to interface with search engines for complex reasoning tasks. However, such mul...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Hubble: An LLM-Driven Agentic Framework for Safe, Diverse, and Reproducible Alpha Factor Discovery](http://arxiv.org/abs/2604.09601v2)
  来源：arXiv | 日期：2026-03-09 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Automated alpha discovery is difficult because the search space of formulaic factors is combinatorial, the signal-to-noise ratio in daily equity data is low, and unconstrained program generation is operationally unsafe. ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ARGen: Affect-Reinforced Generative Augmentation towards Vision-based Dynamic Emotion Perception](http://arxiv.org/abs/2604.12255v1)
  来源：arXiv | 日期：2026-04-14 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Dynamic facial expression recognition in the wild remains challenging due to data scarcity and long-tail distributions, which hinder models from effectively learning the temporal dynamics of scarce emotions. To address t...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Molecular subtypes of the Alzheimer's disease spectrum: Multimodal biomarker integration, mechanistic validation, and adaptive clinical translation.](https://pubmed.ncbi.nlm.nih.gov/41975594/)
  来源：PubMed | 日期：2026-04-14 | 相关度：7.0 | 新颖度：5.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Alzheimer's disease exhibits considerable heterogeneity in its clinical progression, neuropathological features, and underlying etiological mechanisms. However, current clinical diagnosis and treatment primarily rely on ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Knowledge Is Not Static: Order-Aware Hypergraph RAG for Language Models](http://arxiv.org/abs/2604.12185v1)
  来源：arXiv | 日期：2026-04-14 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) enhances large language models by grounding outputs in retrieved knowledge. However, existing RAG methods including graph- and hypergraph-based approaches treat retrieved evidence as ...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Beyond Relevance: On the Relationship Between Retrieval and RAG Information Coverage](http://arxiv.org/abs/2603.08819v3)
  来源：arXiv | 日期：2026-03-09 | 相关度：3.45 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) systems combine document retrieval with a generative model to address complex information seeking tasks like report generation. While the relationship between retrieval quality and ge...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [UBio-MolFM: A Universal Molecular Foundation Model for Bio-Systems](http://arxiv.org/abs/2602.17709v2)
  来源：arXiv | 日期：2026-02-13 | 相关度：2.4 | 新颖度：2.0
  匹配主题：未命中具体主题
  中文摘要：All-atom molecular simulation serves as a quintessential ``computational microscope'' for understanding the machinery of life, yet it remains fundamentally limited by the trade-off between quantum-mechanical (QM) accurac...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AffectAgent: Collaborative Multi-Agent Reasoning for Retrieval-Augmented Multimodal Emotion Recognition](http://arxiv.org/abs/2604.12735v1)
  来源：arXiv | 日期：2026-04-14 | 相关度：2.1 | 新颖度：7.35
  匹配主题：未命中具体主题
  中文摘要：LLM-based multimodal emotion recognition relies on static parametric memory and often hallucinates when interpreting nuanced affective states. In this paper, given that single-round retrieval-augmented generation is high...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond Factual Grounding: The Case for Opinion-Aware Retrieval-Augmented Generation](http://arxiv.org/abs/2604.12138v1)
  来源：arXiv | 日期：2026-04-13 | 相关度：2.1 | 新颖度：6.75
  匹配主题：未命中具体主题
  中文摘要：RAG systems have transformed how LLMs access external knowledge, but we find that current implementations exhibit a bias toward factual, objective content, as evidenced by existing benchmarks and datasets that prioritize...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Human-AI Collaboration for Scaling Agile Regression Testing: An Agentic-AI Teammate from Manual to Automated Testing](http://arxiv.org/abs/2603.08190v2)
  来源：arXiv | 日期：2026-03-09 | 相关度：2.1 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Automated regression testing is essential for maintaining rapid, high-quality delivery in Agile and Scrum organizations. Many teams, including Hacon (a Siemens company), face a persistent gap: validated test specificatio...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LOLGORITHM: Funny Comment Generation Agent For Short Videos](http://arxiv.org/abs/2604.09729v2)
  来源：arXiv | 日期：2026-04-09 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：短视频平台已成为多媒体信息传播的核心，评论在驱动用户参与、传播及算法反馈中起着关键作用。然而，现有方法（如视频摘要和直播弹幕生成）难以生成符合特定平台文化和语言规范的真实评论。本文提出 LOLGORITHM，一种用于风格化短视频评论生成的模块化多智能体（Multi-agent）框架。该框架支持六种可控评论风格，由三个核心模块组成：视频内容摘要、视频分类，以及结合语义检索和热梗增强的评论生成模块。研究者构建了一个包含 3,267 个视频和...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Memory as Metabolism: A Design for Companion Knowledge Systems](http://arxiv.org/abs/2604.12034v1)
  来源：arXiv | 日期：2026-04-13 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation remains the dominant pattern for giving LLMs persistent memory, but a visible cluster of personal wiki-style memory architectures emerged in April 2026 -- design proposals from Karpathy, Me...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Micro-Dexterity in Biological Micromanipulation: Embodiment, Perception, and Control](http://arxiv.org/abs/2604.11640v1)
  来源：arXiv | 日期：2026-04-13 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：微尺度操纵在受控运动和定向运输方面已取得显著进展，但生物医学应用仍需与生物微型对象进行精确且自适应的交互。在微观尺度下，操纵主要通过三类平台实现：作为移动智能体进行物理交互的具身微型机器人、产生非接触式捕获或操纵力的场介导系统，以及通过远程驱动物理工具交互的外部驱动末端执行器。与宏观操纵不同，这些系统运行在流体、受限且表面力占主导的环境中，具有惯性可忽略、界面力显著以及目标柔软、异质且脆弱等特点，导致刚体接触、稳定抓取和丰富本体感受等经...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Empirical Evaluation of PDF Parsing and Chunking for Financial Question Answering with RAG](http://arxiv.org/abs/2604.12047v1)
  来源：arXiv | 日期：2026-04-13 | 相关度：2.05 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：PDF文件主要面向人类阅读而非自动化处理，其包含的文本、表格和图像等异质内容为解析和信息提取带来了巨大挑战。尽管检索增强生成（RAG）系统在自动化PDF处理方面展现出潜力，但目前尚缺乏关于不同组件和设计选择如何影响系统性能的全面研究。本文针对问答（QA）这一特定语言理解任务，利用两个金融领域基准测试（包括新生成的开源基准 TableQuest）开展了系统性研究。我们评估了多种PDF解析器和分块策略（涉及不同的重叠度设置），并探讨了它们在...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Leveraging Residual Graph Convolutional Networks with Cross-Attention Mechanisms for High-Accuracy Protein Function Prediction.](https://pubmed.ncbi.nlm.nih.gov/41861353/)
  来源：PubMed | 日期：2026-04-13 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：蛋白质功能的精确确定对于阐明细胞过程和病理机制至关重要，有助于推动靶向药物设计。尽管湿实验方法仍是功能鉴定的金标准，但其周期长、成本高且劳动强度大，难以满足大规模蛋白质序列的注释需求。本研究提出了 RCHGO，这是一种新型深度学习框架，旨在利用配备交叉注意力机制的残差图卷积网络（RGCNs），直接从蛋白质序列推断基因本体（GO）注释。在 1,493 个非冗余蛋白质上的全面基准测试结果显示，RCHGO 的性能优于 16 种现有的先进方法。...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CAGenMol: Condition-Aware Diffusion Language Model for Goal-Directed Molecular Generation](http://arxiv.org/abs/2604.11483v1)
  来源：arXiv | 日期：2026-04-13 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Goal-directed molecular generation requires satisfying heterogeneous constraints such as protein--ligand compatibility and multi-objective drug-like properties, yet existing methods often optimize these constraints in is...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Enhancing Multilingual RAG Systems with Debiased Language Preference-Guided Query Fusion](http://arxiv.org/abs/2601.02956v3)
  来源：arXiv | 日期：2026-01-06 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Multilingual Retrieval-Augmented Generation (mRAG) systems often exhibit a perceived preference for high-resource languages, particularly English, resulting in the widespread adoption of English pivoting. While prior stu...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Legal2LogicICL: Improving Generalization in Transforming Legal Cases to Logical Formulas via Diverse Few-Shot Learning](http://arxiv.org/abs/2604.11699v1)
  来源：arXiv | 日期：2026-04-13 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：This work aims to improve the generalization of logic-based legal reasoning systems by integrating recent advances in NLP with legal-domain adaptive few-shot learning techniques using LLMs. Existing logic-based legal rea...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AtlasKV: Augmenting LLMs with Billion-Scale Knowledge Graphs in 20GB VRAM](http://arxiv.org/abs/2510.17934v2)
  来源：arXiv | 日期：2025-10-20 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) has shown some success in augmenting large language models (LLMs) with external knowledge. However, as a non-parametric knowledge integration paradigm for LLMs, RAG methods heavily re...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Beyond RAG for Cyber Threat Intelligence: A Systematic Evaluation of Graph-Based and Agentic Retrieval](http://arxiv.org/abs/2604.11419v1)
  来源：arXiv | 日期：2026-04-13 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Cyber threat intelligence (CTI) analysts must answer complex questions over large collections of narrative security reports. Retrieval-augmented generation (RAG) systems help language models access external knowledge, bu...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Retrievals Can Be Detrimental: Unveiling the Backdoor Vulnerability of Retrieval-Augmented Diffusion Models](http://arxiv.org/abs/2501.13340v4)
  来源：arXiv | 日期：2025-01-23 | 相关度：3.45 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Diffusion models (DMs) have recently demonstrated remarkable generation capability. However, their training generally requires huge computational resources and large-scale datasets. To solve these, recent studies empower...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Siamese Foundation Models for Crystal Structure Prediction](http://arxiv.org/abs/2503.10471v2)
  来源：arXiv | 日期：2025-03-13 | 相关度：1.7 | 新颖度：6.75
  匹配主题：未命中具体主题
  中文摘要：从化学成分预测晶体结构是材料发现中的核心挑战，其复杂的3D几何特性使其区别于蛋白质折叠等领域。本文提出了基于扩散的晶体全能模型（DAO），这是一个集成了结构生成器和能量预测器两个孪生基础模型的预训练-微调框架。生成器通过两阶段流水线在包含稳定和不稳定结构的大规模数据集上进行预训练，并利用预测器松弛不稳定配置以引导生成采样。在两个知名基准测试中，预训练显著提升了多种骨干架构的性能。消融研究证实了生成器与预测器之间的协同效应。研究进一步在三...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Lyra 2.0: Explorable Generative 3D Worlds](http://arxiv.org/abs/2604.13036v1)
  来源：arXiv | 日期：2026-04-14 | 相关度：0.7 | 新颖度：7.54
  匹配主题：未命中具体主题
  中文摘要：视频生成的进展为3D场景创建提供了新范式：通过生成受相机控制的视频模拟场景漫游，再利用前馈重建技术将其提升为3D模型。然而，在大规模复杂环境中，长轨迹生成面临空间遗忘（重新访问旧区域时产生结构幻觉）和时间漂移（自回归误差累积导致几何扭曲）的挑战。本文提出 Lyra 2.0 框架，旨在生成持久且可探索的大规模3D世界。为解决空间遗忘，该框架维护每帧3D几何信息并将其仅用于信息路由，通过检索相关历史帧并建立与目标视角的密集对应关系，同时依靠...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CoRoVA: Compressed Representations for Vector-Augmented Code Completion](http://arxiv.org/abs/2510.19644v2)
  来源：arXiv | 日期：2025-10-22 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation has emerged as one of the most effective approaches for code completion enhancement, especially when repository-level context is important. However, adding this extra retrieved context sign...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Leveraging LLMs and Heterogeneous Knowledge Graphs for Persona-Driven Session-Based Recommendation](http://arxiv.org/abs/2604.06928v2)
  来源：arXiv | 日期：2026-04-08 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Session-based recommendation systems (SBRS) aim to capture user's short-term intent from interaction sequences. However, the common assumption of anonymous sessions limits personalization, particularly under sparse or co...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Bridging Trials and Real Life in Fixed-Duration BTKi-Venetoclax for CLL: A Delphi-Enhanced Synthesis Incorporating Artificial Intelligence (AI) Benchmarks.](https://pubmed.ncbi.nlm.nih.gov/41974594/)
  来源：PubMed | 日期：2026-04-13 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：针对慢性淋巴细胞白血病（CLL）中固定疗程（FD）BTK抑制剂（BTKi）联合维奈克拉方案的患者选择仍存在不确定性，主要因临床试验人群通常比现实世界患者更年轻、更健康。本研究旨在为意大利坎帕尼亚地区的临床医生提供衔接试验证据与常规实践的实用指南。通过改进的德尔菲法，9名血液学家评估了BTKi-维奈克拉方案在合并症、基因组学（TP53/del(17p)、IGHV状态、复杂核型）及物流（照护支持、就医距离、给药能力）三个领域的决策影响。基于...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Retrieval as a Decision: Training-Free Adaptive Gating for Efficient RAG](http://arxiv.org/abs/2511.09803v2)
  来源：arXiv | 日期：2025-11-12 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) improves factuality but retrieving for every query often hurts quality while inflating tokens and latency. We propose Training-free Adaptive Retrieval Gating (TARG), a single-shot pol...
  为什么值得看：Retrieval as a Decision: Training-Free A 与你的主题有弱匹配，暂时保留作低优先级跟踪。
