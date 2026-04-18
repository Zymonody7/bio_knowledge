# 每日论文监控日报 (2026-04-18)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 63 篇新论文。

## 抓取状态

- arXiv：成功，命中 44 篇
- PubMed：成功，命中 39 篇
- bioRxiv：成功，命中 35 篇
- medRxiv：成功，命中 11 篇

## 最值得看

### Foundation Model / Agent

- [A tri-modal contrastive learning framework for protein representation learning.](https://pubmed.ncbi.nlm.nih.gov/41990738/)
  来源：PubMed | 日期：2026-04-15 | 相关度：9.15 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Protein foundation models, particularly protein language models, have shown strong success in learning meaningful protein representations using transformer architectures pretrained on large-scale datasets through self-su...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Can Multimodal Large Language Models Visually Interpret Auditory Brainstem Responses?](https://www.medrxiv.org/content/10.64898/2026.04.15.26350944v1)
  来源：medRxiv | 日期：2026-04-17 | 相关度：8.9 | 新颖度：6.2
  匹配主题：foundation_model_agent
  中文摘要：Introduction: Auditory brainstem response (ABR) is a standard objective method for estimating hearing threshold, especially in patients who cannot reliably participate in behavioral audiometry. However, ABR interpretatio...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Blinded Comparative Evaluation of Clinical and AI-Generated Responses to Otologic Patient Queries](https://www.medrxiv.org/content/10.64898/2026.04.14.26350677v1)
  来源：medRxiv | 日期：2026-04-15 | 相关度：7.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：ObjectiveThe objective of this study is to assess the quality, empathy, and readability of large language model (LLM) responses regarding otologic questions from patients as they compare to verified physician responses i...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [CROssBARv2: A Unified Computational Framework for Heterogeneous Biomedical Data Representation and LLM-Driven Exploration](https://www.biorxiv.org/content/10.64898/2026.04.12.718028v1)
  来源：bioRxiv | 日期：2026-04-15 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Biomedical discovery is hindered by fragmented, modality-specific repositories and uneven metadata, limiting integrative analysis, accessibility, and reproducibility. To address these challenges, we present CROssBARv2, a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HARVEST: Unlocking the Dark Bioactivity Data of Pharmaceutical Patents via Agentic AI](https://www.biorxiv.org/content/10.64898/2026.03.15.711910v2)
  来源：bioRxiv | 日期：2026-04-17 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Pharmaceutical patents contain vast Structure-Activity Relationship tables documenting protein-ligand binding data. While technically public, this information remains computationally inaccessible and effectively dark, tr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Fine-Tuning PubMedBERT for Hierarchical Condition Category Classification](https://www.medrxiv.org/content/10.64898/2026.04.13.26350814v1)
  来源：medRxiv | 日期：2026-04-15 | 相关度：7.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Automating Hierarchical Condition Category (HCC) assignment directly from unstructured electronic health record (EHR) notes remains an important but understudied problem in clinical informatics. We present HCC-Coder, an ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Democratizing Scientific Publishing: A Local, Multi-Agent LLM Framework for Objective Manuscript Editing](https://www.medrxiv.org/content/10.64898/2026.04.13.26350761v1)
  来源：medRxiv | 日期：2026-04-17 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Manuscript preparation is a critical bottleneck in scientific publishing, yet existing AI writing tools require cloud transmission of sensitive content, creating data-confidentiality barriers for clinical researchers. We...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Retrieve, Then Classify: Corpus-Grounded Automation of Clinical Value Set Authoring](http://arxiv.org/abs/2604.14616v1)
  来源：arXiv | 日期：2026-04-16 | 相关度：7.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Clinical value set authoring -- the task of identifying all codes in a standardized vocabulary that define a clinical concept -- is a recurring bottleneck in clinical quality measurement and phenotyping. A natural approa...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [VideoStir: Understanding Long Videos via Spatio-Temporally Structured and Intent-Aware RAG](http://arxiv.org/abs/2604.05418v3)
  来源：arXiv | 日期：2026-04-07 | 相关度：6.8 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Scaling multimodal large language models (MLLMs) to long videos is constrained by limited context windows. While retrieval-augmented generation (RAG) is a promising remedy by organizing query-relevant visual evidence int...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DocSeeker: Structured Visual Reasoning with Evidence Grounding for Long Document Understanding](http://arxiv.org/abs/2604.12812v2)
  来源：arXiv | 日期：2026-04-14 | 相关度：6.8 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Existing Multimodal Large Language Models (MLLMs) suffer from significant performance degradation on the long document understanding task as document length increases. This stems from two fundamental challenges: 1) a low...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LinkLlama: Enabling Large Language Model for Chemically Reasonable Linker Design](https://www.biorxiv.org/content/10.64898/2026.04.15.718690v1)
  来源：bioRxiv | 日期：2026-04-16 | 相关度：6.55 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Fragment-based drug discovery (FBDD) relies heavily on the design of chemically viable linkers to connect fragments binding to different pocket regions into potent lead molecules. While recent generative models have adva...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AI4S-SDS: A Neuro-Symbolic Solvent Design System via Sparse MCTS and Differentiable Physics Alignment](http://arxiv.org/abs/2603.03686v3)
  来源：arXiv | 日期：2026-03-04 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Automated design of chemical formulations is a cornerstone of materials science, yet it requires navigating a high-dimensional combinatorial space involving discrete compositional choices and continuous geometric constra...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Large Language Models to Enhance Business Process Modeling: Past, Present, and Future Trends](http://arxiv.org/abs/2604.14034v1)
  来源：arXiv | 日期：2026-04-15 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in Generative Artificial Intelligence, particularly Large Language Models (LLMs), have stimulated growing interest in automating or assisting Business Process Modeling tasks using natural language. Severa...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [EVEE: Interpretable variant effect prediction from genomic foundation model embeddings](https://www.biorxiv.org/content/10.64898/2026.04.10.717844v2)
  来源：bioRxiv | 日期：2026-04-15 | 相关度：9.6 | 新颖度：1.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Predicting the clinical significance of genetic variants remains a central challenge in genomic medicine, with most observed variants classified as variants of uncertain significance. Here we show that representations fr...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MetaMuse: A Multi-Agent AI System for Biomedical Metadata Curation and Harmonization](https://www.biorxiv.org/content/10.64898/2026.04.12.718044v1)
  来源：bioRxiv | 日期：2026-04-15 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Inconsistent and unstructured metadata in public biomedical repositories, such as the Gene Expression Omnibus (GEO), severely limits data discoverability and research reproducibility. To address this, we introduce MO_SCP...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Towards a Universal Foundation Model for Protein Dynamics: A Multi-Chain Tree-Structured Framework with Transformer Propagators](http://arxiv.org/abs/2502.05909v3)
  来源：arXiv | 日期：2025-02-09 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Simulating large-scale protein dynamics using traditional all-atom molecular dynamics (MD) remains computationally prohibitive. We present a unified, universal framework for coarse-grained molecular dynamics (CG-MD) that...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Generative design of intrinsically disordered proteins based on conditioned protein language models: Data is the limit](https://www.biorxiv.org/content/10.64898/2026.04.14.718363v1)
  来源：bioRxiv | 日期：2026-04-16 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Intrinsically disordered proteins and regions (IDRs) are central to a multitude of biological processes. Despite extensive studies of their structural and physicochemical properties, the rational design of IDRs with defi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [PathwaySeeker: Evidence-Grounded AI Reasoning over Organism-Specific Metabolic Networks](https://www.biorxiv.org/content/10.64898/2026.04.14.718256v1)
  来源：bioRxiv | 日期：2026-04-17 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Metabolic activity is not an intrinsic property of an organism, but an emergent state shaped by environmental and experimental context. Despite recent advances in large language models (LLMs) and multi-omics profiling, c...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Training-Free Cross-Lingual Dysarthria Severity Assessment via Phonological Subspace Analysis in Self-Supervised Speech Representations](https://www.medrxiv.org/content/10.64898/2026.04.12.26350731v1)
  来源：medRxiv | 日期：2026-04-17 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Dysarthric speech severity assessment typically requires either trained clinicians or supervised machine learning models built from labelled pathological speech data, limiting scalability across languages and clinical se...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A Conversational Artificial Intelligence Framework for Comparative Pathway-Level Profiling of Sezary Syndrome and Primary Cutaneous CD8+ Aggressive Epidermotropic Cytotoxic T-Cell Lymphoma (PCAECTCL)](https://www.medrxiv.org/content/10.64898/2026.04.15.26350992v1)
  来源：medRxiv | 日期：2026-04-17 | 相关度：4.7 | 新颖度：5.75
  匹配主题：pathogenomics
  中文摘要：Background: Sezary syndrome (SS) is an aggressive leukemic variant of cutaneous T-cell lymphoma (CTCL) with distinct clinical and biological features compared to rarer entities such as primary cutaneous CD8+ aggressive e...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Discovery of the rosalexin pathway expands the modular network of maize diterpenoid chemical defenses.](https://www.biorxiv.org/content/10.64898/2026.04.15.718773v1)
  来源：bioRxiv | 日期：2026-04-17 | 相关度：4.7 | 新颖度：5.25
  匹配主题：pathogenomics
  中文摘要：The evolutionary expansion of specialized metabolism has shaped the ability of plants to adapt to combined pathogen, pest, and other environmental pressures. For instance, the duplication and divergence of ancestral gibb...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Aakhyan: An AI-Powered Vernacular Patient Communication Platform for Oncology in Resource-Limited Settings - System Architecture and Pilot Randomised Trial Protocol](https://www.medrxiv.org/content/10.64898/2026.04.15.26350965v1)
  来源：medRxiv | 日期：2026-04-17 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Inadequate discharge communication is a well-documented contributor to medication non-adherence, missed follow-ups, and preventable readmissions across healthcare systems worldwide. In resource-limited oncology settings,...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Evaluating Large Language Models for Transparent Quality-of-Care Measurement in Children with ADHD](https://www.medrxiv.org/content/10.64898/2026.04.12.26350732v1)
  来源：medRxiv | 日期：2026-04-17 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：ImportanceGuideline-concordant care for young children with attention-deficit/hyperactivity disorder (ADHD) includes recommending parent training in behavior management (PTBM) as first-line treatment. However, assessing ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Simulated Reasoning and Self-Verification for Psychiatric Diagnosis in Generalist Large Language Models: Comparative Evaluation](https://www.medrxiv.org/content/10.1101/2025.09.05.25335196v2)
  来源：medRxiv | 日期：2026-04-17 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：BackgroundLarge language models (LLMs), and, more recently, large reasoning models (LRMs) have rapidly garnered significant interest for application in psychiatry and behavioral health. However, recent studies have ident...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Beyond Arrow's Impossibility: Fairness as an Emergent Property of Multi-Agent Collaboration](http://arxiv.org/abs/2604.13705v1)
  来源：arXiv | 日期：2026-04-15 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Fairness in language models is typically studied as a property of a single, centrally optimized model. As large language models become increasingly agentic, we propose that fairness emerges through interaction and exchan...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [UrbanClipAtlas: A Visual Analytics Framework for Event and Scene Retrieval in Urban Videos](http://arxiv.org/abs/2604.15225v1)
  来源：arXiv | 日期：2026-04-16 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Extracting actionable insights from long-duration urban videos is often labor-intensive: analysts must manually sift through raw footage to pinpoint target events or uncover broader behavioral trends. In this work, we pr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MIND: AI Co-Scientist for Material Research](http://arxiv.org/abs/2604.13699v1)
  来源：arXiv | 日期：2026-04-15 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have enabled agentic AI systems for scientific discovery, but most approaches remain limited to textbased reasoning without automated experimental verification. We propose MIND, an LLM-driven...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [El Agente Forjador: Task-Driven Agent Generation for Quantum Simulation](http://arxiv.org/abs/2604.14609v1)
  来源：arXiv | 日期：2026-04-16 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：AI for science promises to accelerate the discovery process. The advent of large language models (LLMs) and agentic workflows enables the expediting of a growing range of scientific tasks. However, most of the current ge...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ProRank: Prompt Warmup via Reinforcement Learning for Small Language Models Reranking](http://arxiv.org/abs/2506.03487v3)
  来源：arXiv | 日期：2025-06-04 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Reranking is fundamental to information retrieval and retrieval-augmented generation, with recent Large Language Models (LLMs) significantly advancing reranking quality. Most current works rely on large-scale LLMs (>7B p...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ORION: An agentic reasoning construct for the analysis of complex human immune profiling](https://www.biorxiv.org/content/10.64898/2026.04.13.718286v1)
  来源：bioRxiv | 日期：2026-04-16 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：The capacity to generate high-dimensional biological datasets has outpaced the ability to interpret them. Technologies such as phage immunoprecipitation and sequencing (PhIP-seq) enable proteome-scale profiling of antibo...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [UniDoc-RL: Coarse-to-Fine Visual RAG with Hierarchical Actions and Dense Rewards](http://arxiv.org/abs/2604.14967v1)
  来源：arXiv | 日期：2026-04-16 | 相关度：4.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) extends Large Vision-Language Models (LVLMs) with external visual knowledge. However, existing visual RAG systems typically rely on generic retrieval signals that overlook the fine-gr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RACER: Retrieval-Augmented Contextual Rapid Speculative Decoding](http://arxiv.org/abs/2604.14885v1)
  来源：arXiv | 日期：2026-04-16 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Autoregressive decoding in Large Language Models (LLMs) generates one token per step, causing high inference latency. Speculative decoding (SD) mitigates this through a guess-and-verify strategy, but existing training-fr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Distinct Multimodal Imaging Correlates of Depression in Middle-Aged Adults With and Without a Family History of Alzheimer Disease](https://www.biorxiv.org/content/10.64898/2026.04.13.717731v1)
  来源：bioRxiv | 日期：2026-04-17 | 相关度：2.05 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Background: Depression is associated with risk for late-onset Alzheimer&aposs disease (LOAD), but its underlying pathogenesis in at-risk individuals remains unclear. We examined multimodal imaging correlates of depressiv...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CheMLT-F: multitask learning in biochemistry through transformer fusion.](https://pubmed.ncbi.nlm.nih.gov/41992362/)
  来源：PubMed | 日期：2026-04-16 | 相关度：1.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：药物研发因需在庞大化学空间内筛选有效性、毒性和理化性质而进展缓慢。本文提出 CheMLT-F，一种紧凑的多任务 Transformer 模型，通过融合分子和蛋白质序列编码器，学习涵盖 680 多个终点的统一表征，包括多种毒性、理化性质和药物-靶点相互作用（DTI）。在 13 个公开基准测试中，CheMLT-F 在毒性分类方面达到 SOTA 水平，在理化性质预测上创下新纪录，并在 KIBA 和 Davis 数据集的药物-靶点亲和力预测中保...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Mamba-SSM with LLM Reasoning for Biomarker Discovery: Causal Feature Refinement via Chain-of-Thought Gene Evaluation](http://arxiv.org/abs/2604.14334v1)
  来源：arXiv | 日期：2026-04-15 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：深度序列模型的梯度显著性分析可高效识别候选生物标志物，但生成的基因列表常受组织成分混杂因素干扰，导致下游分类器性能下降。本研究探讨了大型语言模型（LLM）的思维链（CoT）推理能否忠实过滤这些混杂因素，以及推理质量如何驱动下游性能。研究者在 TCGA-BRCA RNA-seq 数据集上训练了 Mamba 状态空间模型（SSM），并提取梯度显著性排名前 50 的基因；随后利用 DeepSeek-R1 通过结构化 CoT 对每个候选基因进行...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Don't Retrieve, Navigate: Distilling Enterprise Knowledge into Navigable Agent Skills for QA and RAG](http://arxiv.org/abs/2604.14572v1)
  来源：arXiv | 日期：2026-04-16 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）虽能为大语言模型（LLM）提供外部证据，但模型通常仅作为搜索结果的被动消费者，无法感知语料库的组织结构或未检索到的内容，限制了其回溯或整合分散证据的能力。本文提出 Corpus2Skill 框架，在离线阶段将文档语料库蒸馏为分层技能目录，并在推理时由 LLM 智能体进行导航。该编译流程通过迭代聚类文档、生成各层级的 LLM 摘要，并将其物化为可导航的技能文件树。在服务阶段，智能体获得语料库的全景视图，通过逐级细化的...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SGA-MCTS: Decoupling Planning from Execution via Training-Free Atomic Experience Retrieval](http://arxiv.org/abs/2604.14712v1)
  来源：arXiv | 日期：2026-04-16 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：大型语言模型（LLM）在解决现实任务时需要复杂的多步决策能力，但现有规划方法在推理搜索的高延迟与监督微调的泛化性限制之间存在权衡。为此，研究者提出了SGA-MCTS框架，将LLM规划建模为非参数化检索过程。在离线阶段，该框架利用蒙特卡洛树搜索（MCTS）探索解空间，并将高保真轨迹蒸馏为“状态-目标-动作”（SGA）原子。这些原子是去词汇化的原语，通过将具体实体抽象为符号槽位，保留了可重用的因果逻辑并去除了领域特定噪声。在在线阶段，检索增...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond Black-Box Interventions: Latent Probing for Faithful Retrieval-Augmented Generation](http://arxiv.org/abs/2510.12460v3)
  来源：arXiv | 日期：2025-10-14 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）系统常面临上下文忠实度不足的问题，生成的响应往往与提供的背景信息冲突，或未能充分利用证据。现有方法如特定提示词、解码校准或偏好优化多将大语言模型（LLM）视为黑盒，缺乏评估知识冲突发生时机与原因的可靠机制，导致其稳健性差且依赖大量数据。本研究通过分析模型内部推理过程发现，冲突与对齐的知识状态在模型的潜空间中是线性可分的，且上下文噪声会系统性地增加这些表征的熵。据此，研究者提出了 ProbeRAG 框架，包含三个阶段...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Batch Effects In Brain Foundation Model Embeddings](http://arxiv.org/abs/2604.14441v1)
  来源：arXiv | 日期：2026-04-15 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Foundation models show strong potential for large-scale, high-dimensional biomedical applications, yet their ability to capture relevant neurobiological characteristics remains underexplored. We systematically evaluate e...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Intermediate Layers Encode Optimal Biological Representations in Single-Cell Foundation Models](http://arxiv.org/abs/2604.14838v1)
  来源：arXiv | 日期：2026-04-16 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Current single-cell foundation model benchmarks universally extract final layer embeddings, assuming these represent optimal feature spaces. We systematically evaluate layer-wise representations from scFoundation (100M p...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [LR-Robot: An Human-in-the-Loop LLM Framework for Systematic Literature Reviews with Applications in Financial Research](http://arxiv.org/abs/2604.14793v1)
  来源：arXiv | 日期：2026-04-16 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：The exponential growth of financial research has rendered traditional systematic literature reviews (SLRs) increasingly impractical, as manual screening and narrative synthesis struggle to keep pace with the scale and co...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Longevity Bench: Are SotA LLMs ready for aging research?](https://www.biorxiv.org/content/10.64898/2026.01.12.698650v3)
  来源：bioRxiv | 日期：2026-04-15 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Aging is a core biological process observed in most species and tissues, which is studied with a vast array of technologies. We argue that the abilities of AI systems to emulate aging and to accurately interpret biodata ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [BarrierBench: Evaluating Large Language Models for Safety Verification in Dynamical Systems](http://arxiv.org/abs/2511.09363v2)
  来源：arXiv | 日期：2025-11-12 | 相关度：4.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Safety verification of dynamical systems via barrier certificates is essential for ensuring correctness in autonomous applications. Synthesizing these certificates involves discovering mathematical functions with current...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [VRAG-DFD: Verifiable Retrieval-Augmentation for MLLM-based Deepfake Detection](http://arxiv.org/abs/2604.13660v2)
  来源：arXiv | 日期：2026-04-15 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：In Deepfake Detection (DFD) tasks, researchers proposed two types of MLLM-based methods: complementary combination with small DFD detectors, or static forgery knowledge injection.The lack of professional forgery knowledg...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Efficient generation of epitope-targeted de novo antibodies with Germinal](https://www.biorxiv.org/content/10.1101/2025.09.19.677421v3)
  来源：bioRxiv | 日期：2026-04-15 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Obtaining novel antibodies against specific protein targets is a widely important yet experimentally laborious process. Meanwhile, computational methods for antibody design have been limited by low success rates that cur...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Enhancing Large Language Models with Retrieval Augmented Generation for Software Testing and Inspection Automation](http://arxiv.org/abs/2604.15270v1)
  来源：arXiv | 日期：2026-04-16 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：In this paper, we focus on automating two of the widely used Verification and Validation (V&V) activities in the Software Development Lifecycle (SDLC): Software testing and software inspection (also known as review). Con...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ROSE: Retrieval-Oriented Segmentation Enhancement](http://arxiv.org/abs/2604.14147v1)
  来源：arXiv | 日期：2026-04-15 | 相关度：6.1 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Existing segmentation models based on multimodal large language models (MLLMs), such as LISA, often struggle with novel or emerging entities due to their inability to incorporate up-to-date knowledge. To address this cha...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Predicting Antibody Self-Association with Sequence Structure Fusion Models: The Central Role of CSI-BLI in Early Developability Screening](https://www.biorxiv.org/content/10.64898/2026.04.13.718222v1)
  来源：bioRxiv | 日期：2026-04-15 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Antibody-based biologics are expanding rapidly, yet challenges in development from self-association, high viscosity, aggregation, and unfavorable clearance underscore the need for accurate in silico screening. Clone self...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Enhancing Mental Health Counseling Support in Bangladesh using Culturally-Grounded Knowledge](http://arxiv.org/abs/2604.14576v1)
  来源：arXiv | 日期：2026-04-16 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) show promise in generating supportive responses for mental health and counseling applications. However, their responses often lack cultural sensitivity, contextual grounding, and clinically a...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Zero-Effort Image-to-Music Generation: An Interpretable RAG-based VLM Approach](http://arxiv.org/abs/2509.22378v2)
  来源：arXiv | 日期：2025-09-26 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Recently, Image-to-Music (I2M) generation has garnered significant attention, with potential applications in fields such as gaming, advertising, and multi-modal art creation. However, due to the ambiguous and subjective ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Query pipeline optimization for cancer patient question answering systems](http://arxiv.org/abs/2412.14751v2)
  来源：arXiv | 日期：2024-12-19 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) mitigates hallucination in Large Language Models (LLMs) by using query pipelines to retrieve relevant external information and grounding responses in retrieved knowledge. However, que...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Guaranteeing Knowledge Integration with Joint Decoding for Retrieval-Augmented Generation](http://arxiv.org/abs/2604.08046v2)
  来源：arXiv | 日期：2026-04-09 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) significantly enhances Large Language Models (LLMs) by providing access to external knowledge. However, current research primarily focuses on retrieval quality, often overlooking the ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Automatically Inferring Teachers' Geometric Content Knowledge: A Skills Based Approach](http://arxiv.org/abs/2604.13666v1)
  来源：arXiv | 日期：2026-04-15 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Assessing teachers' geometric content knowledge is essential for geometry instructional quality and student learning, but difficult to scale. The Van Hiele model characterizes geometric reasoning through five hierarchica...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Contrastive multimodal deep learning for survival prediction in grade 2/3 gliomas.](https://pubmed.ncbi.nlm.nih.gov/41987576/)
  来源：PubMed | 日期：2026-04-15 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Accurate survival prediction for grade 2/3 glioma patients remains challenging due to tumor biological heterogeneity and limitations of current prognostic methods that rely on single-modality data. We developed a multimo...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MAB-DQA: Addressing Query Aspect Importance in Document Question Answering with Multi-Armed Bandits](http://arxiv.org/abs/2604.08952v2)
  来源：arXiv | 日期：2026-04-10 | 相关度：2.75 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Document Question Answering (DQA) involves generating answers from a document based on a user's query, representing a key task in document understanding. This task requires interpreting visual layouts, which has prompted...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ASTRA: Enhancing Multi-Subject Generation with Retrieval-Augmented Pose Guidance and Disentangled Position Embedding](http://arxiv.org/abs/2604.13938v1)
  来源：arXiv | 日期：2026-04-15 | 相关度：2.1 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Subject-driven image generation has shown great success in creating personalized content, but its capabilities are largely confined to single subjects in common poses. Current approaches face a fundamental conflict when ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Rag Performance Prediction for Question Answering](http://arxiv.org/abs/2604.07985v2)
  来源：arXiv | 日期：2026-04-09 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：本研究针对问答任务，探讨了如何预测使用检索增强生成（RAG）相较于不使用 RAG 所能获得的性能增益。研究团队系统评估了多种原本为特定检索（ad hoc retrieval）设计的检索前（pre-retrieval）和检索后（post-retrieval）预测指标。此外，研究还深入分析了几种生成后（post-generation）预测指标，并提出了一种全新的预测方法，该方法在实验中展现了最优的预测质量。结果表明，最有效的预测方案是一种新...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A Unified Model and Document Representation for On-Device Retrieval-Augmented Generation](http://arxiv.org/abs/2604.14403v1)
  来源：arXiv | 日期：2026-04-15 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：传统的检索增强生成（RAG）通常依赖云端服务器，这带来了隐私泄露、高昂的维护成本、高延迟及对互联网的依赖。端侧 RAG 通过在本地执行完整流程解决了这些问题，特别适用于查询财务文档、联系方式和病史等敏感个人信息。然而，端侧部署必须平衡有限的内存和磁盘空间：既要限制生成模型的上下文大小以管理 KV 缓存和注意力机制的内存占用，又要最小化嵌入向量的存储以节省磁盘。本研究提出了一种统一模型，该模型能够压缩 RAG 上下文，并利用相同的表示进行...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [CoDaS: AI Co-Data-Scientist for Biomarker Discovery via Wearable Sensors](http://arxiv.org/abs/2604.14615v1)
  来源：arXiv | 日期：2026-04-16 | 相关度：2.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Scientific discovery in digital health requires converting continuous physiological signals from wearable devices into clinically actionable biomarkers. We introduce CoDaS (AI Co-Data-Scientist), a multi-agent system tha...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Toward Agentic RAG for Ukrainian](http://arxiv.org/abs/2604.14896v1)
  来源：arXiv | 日期：2026-04-16 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：本研究针对乌克兰语的代理式检索增强生成（Agentic RAG）进行了初步探索，该工作是在 UNLP 2026 多领域文档理解共享任务框架下开展的。系统架构结合了两阶段检索流程（利用 BGE-M3 模型进行初步检索并配合 BGE 重排序）以及基于 Qwen2.5-3B-Instruct 构建的轻量化代理层，该代理层具备查询改写（query rephrasing）和答案重试循环（answer-retry loops）功能。实验分析表明，检...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [How Retrieved Context Shapes Internal Representations in RAG](http://arxiv.org/abs/2602.20091v2)
  来源：arXiv | 日期：2026-02-23 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) enhances large language models (LLMs) by conditioning generation on retrieved external documents, but the effect of retrieved context is often non-trivial. In realistic retrieval sett...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents](http://arxiv.org/abs/2601.03236v2)
  来源：arXiv | 日期：2026-01-06 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Memory-Augmented Generation (MAG) extends Large Language Models with external memory to support long-context reasoning, but existing approaches largely rely on semantic similarity over monolithic memory stores, entanglin...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [Feedback Adaptation for Retrieval-Augmented Generation](http://arxiv.org/abs/2604.06647v2)
  来源：arXiv | 日期：2026-04-08 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) systems are typically evaluated under static assumptions, despite being frequently corrected through user or expert feedback in deployment. Existing evaluation protocols focus on over...
  为什么值得看：Feedback Adaptation for Retrieval-Augmen 与你的主题有弱匹配，暂时保留作低优先级跟踪。
