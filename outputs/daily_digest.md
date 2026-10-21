# 每日论文监控日报 (2026-10-21)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 62 篇新论文。

## 抓取状态

- arXiv：成功，命中 61 篇
- PubMed：成功，命中 23 篇
- bioRxiv：成功，命中 15 篇
- medRxiv：成功，命中 9 篇

## 最值得看

### Foundation Model / Agent

- [VGL-stGen: Learning a shared multimodal model for lung histology and spatial transcriptomics](http://arxiv.org/abs/2610.28266v1)
  来源：arXiv | 日期：2026-10-20 | 相关度：8.9 | 新颖度：7.4
  匹配主题：foundation_model_agent
  中文摘要：VGL-stGen is a multimodal large language model adapted from a pretrained medical vision-language model using paired lung H&E and spatial transcriptomics with single-cell references. Training integrates image-expression a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LongHisDoc: A Comprehensive Benchmark for Chinese Long Historical Document Understanding](http://arxiv.org/abs/2610.14531v2)
  来源：arXiv | 日期：2026-10-10 | 相关度：7.5 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Chinese historical documents are invaluable cultural treasures, but their complexity poses significant comprehension challenges for non-specialists. Despite the success of Large Language Models (LLMs) and Large Vision-La...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [DNA augmentations for semi-supervised learning in genomic sequence classification.](https://pubmed.ncbi.nlm.nih.gov/42898793/)
  来源：PubMed | 日期：2026-12-01 | 相关度：6.75 | 新颖度：9.75
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：Semi-supervised learning (SSL) is a natural fit for genomics, where unlabeled sequences are abundant but high-quality labels are scarce due to costly curation. However, most SSL pipelines rely on generic perturbations th...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

## 可追踪

### Foundation Model / Agent

- [Figures as Interfaces: Toward LLM-Native Artifacts for Scientific Discovery](http://arxiv.org/abs/2604.08491v3)
  来源：arXiv | 日期：2026-04-09 | 相关度：7.9 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are transforming scientific workflows, not only through their generative capabilities but also through their emerging ability to use tools, reason about data, and coordinate complex analytica...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [NeuroPilot: Longitudinal intravital neural imaging across scales and modalities through an agentic platform](https://www.biorxiv.org/content/10.64898/2026.10.18.759043v1)
  来源：bioRxiv | 日期：2026-10-19 | 相关度：7.5 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Longitudinal intravital imaging is essential for understanding how neural populations evolve across behavioral states, yet converting large-scale recordings into biological insight remains a fundamental challenge because...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Explore or Confirm? LLM Agents Misallocate Measurements Under Noise](http://arxiv.org/abs/2610.25111v1)
  来源：arXiv | 日期：2026-10-18 | 相关度：7.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：As model reasoning gets cheaper, the physical experiment becomes the slow and costly step in discovery. Each experiment returns a noisy reading: a high value can mean a good candidate or a lucky draw. With a fixed budget...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Small Average Error, Wide Individual Error: General-Purpose LLMs Estimating Energy Intake from Meal Photos in a Feeding Trial](http://arxiv.org/abs/2610.26538v1)
  来源：arXiv | 日期：2026-10-19 | 相关度：7.1 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Photo-based estimation of food energy could ease dietary assessment, and general-purpose multimodal large language models (LLMs) make such estimates easy to obtain. Most evaluations use one photo taken before eating and ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ProMemAgent: Long-Horizon Proactive Assistance with Context-Aware Prospective Memory from Sensory Perceptions](http://arxiv.org/abs/2610.27400v1)
  来源：arXiv | 日期：2026-10-19 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Large language model (LLM) agents are moving beyond reactive responses toward proactive assistance that anticipates user needs without explicit requests. However, existing proactive agents primarily address immediate nee...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [WorldScape Policy 2.0: Empowering Steerable World Action Modeling with Reasoning-Augmented Memory and In-Context Learning](http://arxiv.org/abs/2607.18840v3)
  来源：arXiv | 日期：2026-07-21 | 相关度：6.1 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：World Action Models (WAMs) offer a promising paradigm for robotic manipulation by jointly modeling visual state transitions and robot actions. However, existing WAMs are constrained by limited temporal context, coarse ep...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Magnolia: A Persistent-Memory Agent Framework for Computational Chemistry](http://arxiv.org/abs/2610.27230v1)
  来源：arXiv | 日期：2026-10-19 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Chemistry has recently entered a high-data regime as molecular databases from high-throughput platforms or computational studies have become available. Increasing automation within the chemical sciences leads to a more d...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RAG-NIMBF: A Non-Invasive, Modular Benchmarking Framework for Automated RAG Configuration Analysis](http://arxiv.org/abs/2610.27816v1)
  来源：arXiv | 日期：2026-10-20 | 相关度：5.45 | 新颖度：6.86
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) has become the dominant paradigm for grounding the outputs of large language models (LLM) in external knowledge. However, practitioners are faced with a vast configuration space compr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RANGER: Retrieval Agent for Navigating Graphs with Semantic Evaluation Rewards](http://arxiv.org/abs/2610.28010v1)
  来源：arXiv | 日期：2026-10-20 | 相关度：5.45 | 新颖度：6.82
  匹配主题：foundation_model_agent
  中文摘要：The integration of Large Language Models and Reinforcement Learning offers a promising direction for complex sequential decision-making tasks, such as multi-hop question answering over knowledge graphs. While LLMs provid...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MedMCP: An Open Agentic Ecosystem for Medical Imaging Workflows](https://www.biorxiv.org/content/10.64898/2026.10.12.758708v1)
  来源：bioRxiv | 日期：2026-10-19 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Deep learning has driven rapid progress in medical image analysis, with methods for tasks such as organ segmentation, anomaly detection, and radiology report generation now matching or surpassing expert performance on se...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Context-Aware Prompt Injection Detection via Small Language Models in RAG Pipelines: nokast-secureRAG](http://arxiv.org/abs/2610.28364v1)
  来源：arXiv | 日期：2026-10-20 | 相关度：6.15 | 新颖度：7.83
  匹配主题：foundation_model_agent
  中文摘要：Local Retrieval-Augmented Generation (RAG) systems are vulnerable to indirect prompt injection and retrieval poisoning, where malicious instructions in retrieved content are mistaken for trusted input. We present nokast-...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [ArtSeek: Deep artwork understanding via multimodal in-context reasoning and late interaction retrieval](http://arxiv.org/abs/2507.21917v2)
  来源：arXiv | 日期：2025-07-29 | 相关度：6.8 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Analyzing digitized artworks requires both visual interpretation and deep artistic, contextual, and historical knowledge. We introduce ArtSeek, a multimodal framework for art analysis that combines multimodal large langu...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MADDIE: Multi-Agent Drug Discovery Engine](http://arxiv.org/abs/2610.16975v2)
  来源：arXiv | 日期：2026-10-12 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Drug discovery remains a resource-intensive and time-consuming process, involving billions of dollars and a decade of development to advance a drug to market. While many in silico tools have accelerated this process, ope...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Large language model classifies prior evidence in gene-phenotype associations](https://www.medrxiv.org/content/10.64898/2026.10.17.26365766v1)
  来源：medRxiv | 日期：2026-10-19 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：The growing scale of genome-wide and rare-variant association studies is shifting the bottleneck from discovery to interpretation, which requires positioning each new association against prior evidence. We present PESTO ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Orthogonal Boundary Unlearning for Dual-Use Concepts in Large Language Models](http://arxiv.org/abs/2610.27490v1)
  来源：arXiv | 日期：2026-10-20 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Mitigating catastrophic risks from large language models requires excising hazardous operational capabilities, such as cyberwarfare exploitation and pathogen enhancement, without degrading benign scientific utility. In t...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [IDEAgent: Agentic Quality-Diversity Search for Research Idea Generation](http://arxiv.org/abs/2607.22375v2)
  来源：arXiv | 日期：2026-07-24 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have significantly advanced the automation of scientific discovery. However, existing systems share a core limitation: they optimize ideas independently for either Quality or Diversity. This ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [A general-purpose System One decision model for clinical records](http://arxiv.org/abs/2610.27099v1)
  来源：arXiv | 日期：2026-10-19 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Clinical care, health-system operations and biomedical discovery depend on extracting reliable answers from patient records, yet applying diverse clinical questions across entire populations remains computationally expen...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Cognitive cartography of mammalian brains using meta-analysis of AI experts](https://www.biorxiv.org/content/10.64898/2025.12.01.691701v2)
  来源：bioRxiv | 日期：2026-10-19 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：No individual mind can fully grasp the complexity of modern neuroscientific literature. Where human experts flag, the latest AI models excel. Here we show how frontier large language models can systematically and quantit...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PigGPA: A Domain-Constrained Agent for Porcine Genomic Breeding with Verifiable Tool Execution](https://www.biorxiv.org/content/10.64898/2026.10.18.759908v1)
  来源：bioRxiv | 日期：2026-10-19 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Large language model agents can plan and execute scientific analyses, but successful task completion does not establish whether analytical decisions remain consistent across independent sessions or whether computations f...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RAGLeak: Supply-Chain Privacy Backdoors in Retrieval-Augmented Generation](http://arxiv.org/abs/2610.25937v1)
  来源：arXiv | 日期：2026-10-19 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) enables large language models to access external knowledge during inference, but its reliance on external knowledge bases also introduces new attack surfaces. Existing data extraction...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The Effectiveness and Durability of Pretraining Data Filtering in Protein Language Models](http://arxiv.org/abs/2610.26651v1)
  来源：arXiv | 日期：2026-10-19 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Pretraining filtering is one of the most common safeguards for open-weight language models. Here we study its effectiveness, durability and scalability using the ESM-2 family of protein language models. We find that filt...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [recAMPLIFY: Large-Scale Pretraining of Recursive Protein Language Models](http://arxiv.org/abs/2610.26747v1)
  来源：arXiv | 日期：2026-10-19 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Protein language models (pLMs) are powerful tools for protein annotation and mutation-effect prediction, but progress has largely depended on scaling model size and data, making them expensive and prone to memorization. ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Bayesian Model Discovery with Language Models: Closing the Loop between Hypotheses and Experiments](http://arxiv.org/abs/2610.25747v1)
  来源：arXiv | 日期：2026-10-19 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Scientific model discovery requires proposing candidate models of an unknown system and designing experiments that discriminate among them. However, LLM-based approaches typically rely on in-context learning to predict o...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Multimodal Engineering GraphRAG Framework for Post-Wind-Event Building Assessment and Recovery Inference](http://arxiv.org/abs/2610.28216v1)
  来源：arXiv | 日期：2026-10-20 | 相关度：2.75 | 新颖度：6.82
  匹配主题：foundation_model_agent
  中文摘要：Post-event building assessment requires linking observed physical damage to its consequences for safety, habitability, functionality, and recovery. Yet post-disaster evidence is often heterogeneous, incomplete, and distr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [When Seeing Is Not Believing -- A Benchmark for Search-Grounded Video Misinformation Detection](http://arxiv.org/abs/2606.04098v2)
  来源：arXiv | 日期：2026-06-02 | 相关度：2.75 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Video misinformation increasingly operates at the semantic and evidential level: authentic footage may be selectively edited, temporally reordered, spliced across sources, or augmented with AI-generated content to constr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [StrucChunk: Structure-Aware Retrieval for Legal Document RAG](http://arxiv.org/abs/2610.26313v1)
  来源：arXiv | 日期：2026-10-19 | 相关度：2.75 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) can ground LLM outputs in domain-specific knowledge, but legal documents are hard: standard chunking fragments hierarchical argument structure, and generic embeddings struggle with bo...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Auto-Director: Leveraging Multi-Agent Collaboration for Autonomous Video Editing](http://arxiv.org/abs/2610.28346v1)
  来源：arXiv | 日期：2026-10-20 | 相关度：1.4 | 新颖度：7.54
  匹配主题：未命中具体主题
  中文摘要：Autonomous video editing from open-world resources remains a challenging problem in multimedia content creation. Retrieval-based methods are constrained by fixed source material and lack creative flexibility, while gener...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Right Facts, Wrong Rule: Scope-Transfer Poisoning of Retrieval-Augmented Generation](http://arxiv.org/abs/2609.35155v2)
  来源：arXiv | 日期：2026-09-28 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) systems use external documents for facts and rules that guide answers. We study rule-scope misapplication, where a rule valid within its documented scope is applied to a question outs...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AGR: Agentic Generative Retrieval with Tool-Augmented Search](http://arxiv.org/abs/2610.26831v1)
  来源：arXiv | 日期：2026-10-19 | 相关度：1.4 | 新颖度：1.5
  匹配主题：未命中具体主题
  中文摘要：Large-scale search and recommendation systems derive much of their retrieval quality from rich, heterogeneous features, yet existing generative retrieval (GR) methods struggle to exploit such feature ecosystems efficient...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic AI -- Physicist Collaboration in Experimental Particle Physics: A Proof-of-Concept Measurement with LEP Open Data](http://arxiv.org/abs/2603.05735v3)
  来源：arXiv | 日期：2026-03-05 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：We present an agentic measurement of the thrust distribution in $e^{+}e^{-}$ collisions at $\sqrt{s}=91.2$ GeV using ALEPH archived data. This work was carried out through an AI agent-physicist collaboration, using inter...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OptScientist: Automated Discovery of Optimization Laws](http://arxiv.org/abs/2610.28562v1)
  来源：arXiv | 日期：2026-10-20 | 相关度：0.7 | 新颖度：7.66
  匹配主题：未命中具体主题
  中文摘要：Many scientific phenomena are best understood as outcomes of underlying optimization problems, yet automated scientific discovery has largely focused on recovering equations that describe observed input-output patterns. ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DiscoveryRSI: Recursively Learning to Discover Valuable Hypotheses](http://arxiv.org/abs/2610.23839v2)
  来源：arXiv | 日期：2026-10-16 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Scientific discovery requires developing worthwhile hypotheses into practical investigations, yet learning from this evolving research process remains challenging. We introduce an operational definition of valuable and t...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Iterate Until Retrieved: Factual Nugget Optimization for Discoverable Continual Corrections in Agentic RAG](http://arxiv.org/abs/2605.25641v2)
  来源：arXiv | 日期：2026-05-25 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Agentic retrieval-augmented generation (RAG) systems in business-to-business settings may often receive free-form response feedback. Rather than generic feedback signals such as style, preference, or overall response qua...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [EpiLens: Lightweight RAG for Epidemiological Knowledge Acquisition](http://arxiv.org/abs/2610.26730v1)
  来源：arXiv | 日期：2026-10-19 | 相关度：6.7 | 新颖度：0.25
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：To prepare for future outbreaks, researchers need to know what studies have been done and what data they use. Mapping a large literature by hand is slow, while large language models alone can misstate or conflate sources...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [VLegal-Bench: Cognitively Grounded Benchmark for Vietnamese Legal Reasoning of Large Language Models](http://arxiv.org/abs/2512.14554v6)
  来源：arXiv | 日期：2025-12-16 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：The rapid advancement of large language models (LLMs) has enabled new possibilities for applying artificial intelligence within the legal domain. Nonetheless, the complexity, hierarchical organization, and frequent revis...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Benchmark for Structured Retrieval-Augmented Generation in Perovskite Photovoltaics](http://arxiv.org/abs/2610.25575v1)
  来源：arXiv | 日期：2026-10-18 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：While retrieval-augmented language models increasingly serve as literature assistants in the physical sciences, existing benchmarks evaluate them primarily on qualitative text overlap or through model-based scoring rathe...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Conditional information Retrieval for Longitudinal Survey Harmonisation](http://arxiv.org/abs/2610.26173v1)
  来源：arXiv | 日期：2026-10-19 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Identifying conceptually equivalent questions across different surveys is a challenging information retrieval task where surface-level textual similarity is insufficient. Two questions may be lexically similar yet assess...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [WorldSR: Harnessing World Knowledge Search for Grounded Image Super-Resolution](http://arxiv.org/abs/2610.28423v1)
  来源：arXiv | 日期：2026-10-20 | 相关度：0.7 | 新颖度：7.41
  匹配主题：未命中具体主题
  中文摘要：Generative-prior-based super-resolution (SR) methods leverage implicit knowledge learned from large-scale models to enhance low-resolution inputs. However, such priors are inherently stochastic and optimized for diverse ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [DeclineCraft: A RAG Abstention Benchmark for Jointly Measuring Combined Retrieval and Parametric Knowledge](http://arxiv.org/abs/2610.28340v1)
  来源：arXiv | 日期：2026-10-20 | 相关度：0.7 | 新颖度：7.28
  匹配主题：未命中具体主题
  中文摘要：Reliable retrieval-augmented generation (RAG) requires recognizing when neither retrieved documents nor parametric knowledge supports an answer. We introduce DeclineCraft, a dynamic abstention benchmark whose unanswerabl...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Auditing Tool Traces in Agentic LLMs: Source Localization and Counterfactual Dependence Testing](http://arxiv.org/abs/2610.25540v1)
  来源：arXiv | 日期：2026-10-18 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Agentic LLMs increasingly support scientific prediction by grounding decisions in external evidence. In biology, they promise accurate, interpretable predictions for important problems by integrating complex experimental...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Large-Scale Biomedical RAG: Corpus Scaling, Document Representation, and Efficiency Trade-offs](http://arxiv.org/abs/2610.26339v1)
  来源：arXiv | 日期：2026-10-19 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：We present a controlled, large-scale evaluation of how corpus scale, document representation, and reranking affect the effectiveness and efficiency of biomedical Retrieval-Augmented Generation (RAG) systems. Retrieval co...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [ProtSent: Protein Sentence Transformers](http://arxiv.org/abs/2605.06830v2)
  来源：arXiv | 日期：2026-05-07 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Protein language models produce rich per-residue representations, but the sequence embeddings obtained by mean-pooling them are never trained to place related proteins near one another, so the geometry that retrieval, cl...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Beyond Better Models: Barriers and a Path Forward in Generalisable TCR Antigen Specificity Prediction](https://www.biorxiv.org/content/10.64898/2026.10.12.758456v1)
  来源：bioRxiv | 日期：2026-10-18 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：T cells are at the centre of adaptive immunity, protecting the organism against infection and cancer. T cell receptors (TCRs), expressed on the surface of T cells, enable the recognition of target cells through interacti...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Steered Not Stirred: Effective Reward Tilting using Surrogate Reward Mixing](http://arxiv.org/abs/2610.25502v1)
  来源：arXiv | 日期：2026-10-18 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Continuous-time generative models, from diffusion models, flow matching, and now flow maps, owe their practical value to high-fidelity generation and steerability. In many applications, a ground-truth latent ``oracle'' r...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Network organization of protein binding-site landscapes across scales](https://www.biorxiv.org/content/10.64898/2026.10.17.759831v1)
  来源：bioRxiv | 日期：2026-10-19 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Studying protein binding sites helps explain ligand recognition and selectivity, informing drug development and repurposing. Here, we combine protein language model embeddings with network analysis to investigate how loc...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Latent Abstraction for Retrieval-Augmented Generation](http://arxiv.org/abs/2604.17866v3)
  来源：arXiv | 日期：2026-04-20 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) has become a standard approach for enhancing large language models (LLMs) with external knowledge, mitigating hallucinations, and improving factuality. However, existing systems rely ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [REATS: LLM Reasoning-based Ensemble Learning for Adaptive Time Series Forecasting](http://arxiv.org/abs/2608.10149v2)
  来源：arXiv | 日期：2026-08-10 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Due to the diversity of real-world time series, no single forecasting model consistently dominates across all samples. Ensemble learning addresses this by combining complementary model strengths, yet existing methods rel...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Secure Multimodal Federated Optimization via Hierarchical DNA-Based Key Management](http://arxiv.org/abs/2610.27644v1)
  来源：arXiv | 日期：2026-10-20 | 相关度：3.05 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Federated optimization over heterogeneous multimodal data enables distributed institutions to collaboratively optimize a shared model using medical images, genomic profiles, clinical records, and physiological signals wi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GenoMAS: Guided Multi-Agent Programming for Scientific Discovery from Genomic Data](http://arxiv.org/abs/2507.21035v4)
  来源：arXiv | 日期：2025-07-28 | 相关度：2.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Gene expression analysis holds the key to many biomedical discoveries, yet extracting insights from raw transcriptomic data remains challenging due to the complexity of multiple large, semi-structured files and the need ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [DeepD enables efficient genome modeling and controllable long-context sequence generation across domains of life](https://www.biorxiv.org/content/10.64898/2026.10.13.758170v1)
  来源：bioRxiv | 日期：2026-10-18 | 相关度：2.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Genome foundation models hold great potential for advancing biological research, but modeling diverse complex genomes and generating controllable genome-scale sequences remain challenging. We present DeepD, a phylogeny-i...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [DiMOS: Doob-Guided Inference-Time Multi-Objective Search for Scientific Design](http://arxiv.org/abs/2610.05808v2)
  来源：arXiv | 日期：2026-10-05 | 相关度：2.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Scientific design often requires jointly satisfying multiple objectives and constraints. Pretrained masked diffusion models provide a generative foundation for this task, but fine-tuning them to meet these objectives and...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Variable sparsity non-negative matrix and tensor factorization algorithms and their applications in cancer genomics](https://www.biorxiv.org/content/10.64898/2026.10.19.760022v1)
  来源：bioRxiv | 日期：2026-10-19 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：The field of oncology has experienced significant advancements in novel therapies and molecular diagnostics to personalize initial cancer treatments. However, cancer's propensity for evolution and resistance to therapies...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Coordinated Networking for On-Device Agent-Augmented Real-Time Communication](http://arxiv.org/abs/2607.22854v2)
  来源：arXiv | 日期：2026-07-24 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：AI agents are enabling a new paradigm of agent-augmented real-time communication (RTC), where humans focus on high-level collaboration, while agents autonomously retrieve, analyze, and generate information in real time t...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Registration is a Representation Problem: Solving Whole-Body PET/CT Registration](http://arxiv.org/abs/2610.18804v2)
  来源：arXiv | 日期：2026-10-13 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Raw image intensities are a poor surrogate for similarity across images in correspondence problems. Further, while auxiliary segmentation labels can provide semantic identification and improve matching, they can assign o...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [E-Layout: Layout-Stage Logic Restructuring via RL-Optimized Equality-Saturated Graph Retrieval-Augmented Generation](http://arxiv.org/abs/2610.26432v1)
  来源：arXiv | 日期：2026-10-19 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Achieving high sign-off performance in advanced ICs increasingly depends on layout-stage optimization under realistic physical conditions. While recent efforts have moved toward synthesis-layout fusion, most existing wor...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Quality and transcript-grounded clinical-risk error burden of AI-generated vs allied health professional clinical notes: a paired simulation study across four disciplines](https://www.medrxiv.org/content/10.64898/2026.10.16.26365719v1)
  来源：medRxiv | 日期：2026-10-19 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Background: Ambient artificial-intelligence (AI) scribes are being deployed beyond medicine into allied-health practice, but comparative evidence mainly concerns physician documentation. Objective: To compare quality and...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [A synthetic MALDI-TOF MS atlas for microbial classification across hospitals](https://www.biorxiv.org/content/10.64898/2026.10.19.759651v1)
  来源：bioRxiv | 日期：2026-10-19 | 相关度：1.7 | 新颖度：6.75
  匹配主题：未命中具体主题
  中文摘要：Matrix-Assisted Laser Desorption/Ionization Time-of-Flight (MALDI-TOF) mass spectrometry (MS) is central to routine clinical microbiology for species identification. Its combination with machine learning is constrained b...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [HGASurv: Hierarchical Granularity-Aware Multimodal Integration for Survival Prediction](http://arxiv.org/abs/2610.26357v2)
  来源：arXiv | 日期：2026-10-19 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Multimodal survival prediction jointly analyzes histopathological whole-slide images (WSIs), genomic profiles, and clinical variables to stratify patients by risk. However, existing approaches often inadequately account ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Neighborhood-Aware Unlearning for Generative Recommendation](http://arxiv.org/abs/2610.27232v1)
  来源：arXiv | 日期：2026-10-19 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Generative recommendation predicts items by autoregressively generating semantic identifiers (SIDs), whose tokens are shared across semantically related items. With this paradigm gaining adoption, the question of how to ...
  为什么值得看：Neighborhood-Aware Unlearning for Genera 与你的主题有弱匹配，暂时保留作低优先级跟踪。
