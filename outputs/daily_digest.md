# 每日论文监控日报 (2026-05-26)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 52 篇新论文。

## 抓取状态

- arXiv：成功，命中 48 篇
- PubMed：成功，命中 30 篇
- bioRxiv：成功，命中 16 篇
- medRxiv：成功，命中 6 篇

## 最值得看

### Foundation Model / Agent

- [Towards Reliable Fetal Ultrasound Interpretation with Multi-Agent Collaboration](http://arxiv.org/abs/2605.25357v1)
  来源：arXiv | 日期：2026-05-25 | 相关度：8.5 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Automated fetal ultrasound interpretation requires a workflow from visual perception, including plane recognition and anatomical segmentation, to clinical understanding, including biometric measurement and diagnostic rep...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Decision-Making with Lightweight Confidence-Aware Language Model for Autonomous Driving](http://arxiv.org/abs/2605.25393v1)
  来源：arXiv | 日期：2026-05-25 | 相关度：7.9 | 新颖度：6.7
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) and Multimodal LLMs (MLLMs) have demonstrated immense potential in autonomous driving (AD) by offering human-like reasoning and open-world generalization. However, the excessive computational...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Predicting Influenza Virus Host Tropism and Zoonotic Spillover Risk from Protein Sequences](https://www.biorxiv.org/content/10.64898/2026.05.21.726772v1)
  来源：bioRxiv | 日期：2026-05-24 | 相关度：10.0 | 新颖度：5.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Novel infectious diseases, predominantly originating from non-human animals, pose a significant threat to global public health and economic stability. Avian influenza virus presents an especially significant challenge du...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ProteomeLM: A proteome-scale language model enables accurate and rapid prediction of protein-protein interactions and gene essentiality across taxa.](https://pubmed.ncbi.nlm.nih.gov/42160340/)
  来源：PubMed | 日期：2026-05-26 | 相关度：6.45 | 新颖度：9.13
  匹配主题：foundation_model_agent
  中文摘要：Language models trained on biological sequences are advancing inference tasks from the scale of single proteins to that of genomic neighborhoods. Here, we introduce ProteomeLM, a transformer-based language model that uni...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [Digital Registrar: A Schema-First Framework for Multi-Cancer Privacy-Preserving Pathology Abstraction via Local LLMs](https://www.medrxiv.org/content/10.1101/2025.10.21.25338475v9)
  来源：medRxiv | 日期：2026-05-23 | 相关度：8.9 | 新颖度：1.7
  匹配主题：foundation_model_agent
  中文摘要：手术病理报告包含精细的癌症诊断数据，但其自由文本格式阻碍了自动化登记和二次分析。本研究开发了“Digital Registrar”框架，其核心是基于美国病理学家协会（CAP）标准的临床本体，通过严格类型的分层架构和 DSPy 签名实现。该系统涵盖 10 种主要癌症类型，涉及 193 个登记字段，包括淋巴结组和手术切缘等复杂变量。研究利用 DSPy 框架构建了与模型无关的提取流水线，并在单块 48GB GPU 上测试了本地部署的可行性。实...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MyeGPT: an AI agent for Multiple Myeloma](https://www.medrxiv.org/content/10.64898/2026.05.14.26353252v2)
  来源：medRxiv | 日期：2026-05-23 | 相关度：7.55 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Today, advancements in our understanding of cancer biology are increasingly attributed to large-scale clinical-molecular datasets. The case in point for multiple myeloma - the second-most prevalent haematological maligna...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Carbon: Decoding the Language of Life](https://www.biorxiv.org/content/10.64898/2026.05.22.727119v1)
  来源：bioRxiv | 日期：2026-05-25 | 相关度：7.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Genomic foundation models have emerged alongside the rapid progress of large language models, offering a promising framework for learning general-purpose sequence priors for DNA understanding, generation, and design. Thi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LLM-as-a-Judge in Healthcare: A Scoping Analysis of Applications, Methods, and Human Alignment](http://arxiv.org/abs/2605.25273v1)
  来源：arXiv | 日期：2026-05-24 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly deployed across healthcare applications, including clinical documentation, diagnostic reasoning, medicine recommendation, and medical education. Their outputs are largely uns...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ORACAL: A Robust and Explainable Multimodal Framework for Smart Contract Vulnerability Detection with Causal Graph Enrichment](http://arxiv.org/abs/2603.28128v2)
  来源：arXiv | 日期：2026-03-30 | 相关度：6.8 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Although Graph Neural Networks (GNNs) have shown promise for smart contract vulnerability detection, they still face significant limitations. Homogeneous graph models fail to capture the interplay between control flow an...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PennySynth: RAG-Driven Data Synthesis for Automated Quantum Code Generation](http://arxiv.org/abs/2605.25572v1)
  来源：arXiv | 日期：2026-05-25 | 相关度：6.55 | 新颖度：7.04
  匹配主题：foundation_model_agent
  中文摘要：The growing complexity of quantum programming frameworks has exposed a critical limitation in existing large language model (LLM)-based code assistants: general-purpose models hallucinate PennyLane-specific gate names, m...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SPARK: Search Personalization via Agent-Driven Retrieval and Knowledge-sharing](http://arxiv.org/abs/2512.24008v3)
  来源：arXiv | 日期：2025-12-30 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Personalized search demands the ability to model users' evolving, multi-dimensional information needs; a challenge for systems constrained by static profiles or monolithic retrieval pipelines. We present SPARK (Search Pe...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evo-Attacker: Memory-Augmented Reinforcement Learning for Long-Horizon Tool Attacks on LLM-MAS](http://arxiv.org/abs/2605.25389v1)
  来源：arXiv | 日期：2026-05-25 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：While Large Language Model-based Multi-Agent Systems (LLM-MAS) demonstrate remarkable capabilities in solving complex tasks by orchestrating specialized agents and external tools, the implicit trust in tool outputs creat...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SpatialClaw: A Memory-Augmented Autonomous Ecosystem for Spatial Omics Analysis](https://www.biorxiv.org/content/10.64898/2026.05.21.723451v1)
  来源：bioRxiv | 日期：2026-05-25 | 相关度：6.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：While the expansion of spatial omics has revolutionized our ability to dissect tissue architecture, the accumulation of incompatible computational methods has heavily fragmented end-to-end analysis, rendering complex wor...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Cross-Model Variability in Large Language Model Triage Behavior for Potential Stroke Symptoms](https://www.medrxiv.org/content/10.64898/2026.05.22.26353904v1)
  来源：medRxiv | 日期：2026-05-25 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Background: Stroke is a time-sensitive neurological emergency in which early EMS activation and presentation to definitive care are cornerstones of effective therapy. Large language models (LLMs) are increasingly consult...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [What Makes a Medical Checker Trainable? Diagnosing Signal Collapse and Reward Hacking in Checker-Guided RAG for Biomedical QA](http://arxiv.org/abs/2605.25988v1)
  来源：arXiv | 日期：2026-05-25 | 相关度：5.45 | 新颖度：7.82
  匹配主题：foundation_model_agent
  中文摘要：Medical RAG needs evidence-grounded claims, so plugging a claim-level NLI checker into retrieval-augmented RL is intuitive. \textbf{We find that the checker's \emph{output distribution} during training, not its held-out ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The Multilingual Curse at the Retrieval Layer: Evidence from Amharic](http://arxiv.org/abs/2605.24556v1)
  来源：arXiv | 日期：2026-05-23 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Multilingual retrieval increasingly underpins cross-lingual question answering and retrieval-augmented generation. Strong zero-shot scores on multilingual benchmarks are often taken as evidence that current encoders tran...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [G-DRAGON: Geospatial Reasoning and Dynamic Planning for Retrieval-Augmented Outdoor Navigation](http://arxiv.org/abs/2605.25646v1)
  来源：arXiv | 日期：2026-05-25 | 相关度：5.45 | 新颖度：6.28
  匹配主题：foundation_model_agent
  中文摘要：Autonomous ground robots operating in large-scale outdoor environments require both robust long-range navigation and fine-grained ''last-mile'' exploration. Current advances in visual-language navigation (VLN) work well ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Multimodal 3D Foundation Model for Light Sheet Fluorescence Microscopy Enables Few-Shot Segmentation, Classification, and Deblurring](http://arxiv.org/abs/2605.26026v1)
  来源：arXiv | 日期：2026-05-25 | 相关度：3.45 | 新颖度：8.19
  匹配主题：foundation_model_agent
  中文摘要：Light sheet fluorescence microscopy (LSM) enables high-resolution, three-dimensional (3D) imaging of biological specimens, providing rich volumetric data for studying cellular organization, pathology, and vascular networ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [CliPepPI: Scalable prediction of domain-peptide specificityusing contrastive learning](https://www.biorxiv.org/content/10.64898/2026.03.18.712595v2)
  来源：bioRxiv | 日期：2026-05-24 | 相关度：7.65 | 新颖度：1.25
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Domain-peptide interactions mediate a significant fraction of cellular protein networks, yet accurately predicting their specificity remains challenging. Peptide motifs typically have short, fuzzy sequence profiles, and ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Macaron-A2UI: A Model for Generative UI in Personal Agents](http://arxiv.org/abs/2605.24830v1)
  来源：arXiv | 日期：2026-05-24 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：As personal agents evolve to handle complex, user-centric tasks, static plain-text chat is rapidly becoming a bottleneck. Generative UI emerges as the necessary new interface layer, dynamically synthesizing the right con...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Retrieval-Augmented Detection of Potentially Abusive Clauses in Chilean Terms of Service](http://arxiv.org/abs/2605.26019v1)
  来源：arXiv | 日期：2026-05-25 | 相关度：4.75 | 新颖度：7.16
  匹配主题：foundation_model_agent
  中文摘要：Online Terms of Service often function as contracts of adhesion, creating asymmetries that may expose consumers to potentially abusive clauses. In Chile, assessing such clauses is legally challenging because some provisi...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [AstroRAG -- A Pagerank-Based Retrieval-Augmented Generation Pipeline for Question Answering in Astronomy](http://arxiv.org/abs/2605.25039v1)
  来源：arXiv | 日期：2026-05-24 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) demonstrate strong performance in natural language processing but often generate factual errors when relying solely on parametric knowledge. Retrieval-Augmented Generation (RAG) mitigates the...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [STREAM: A Data-Centric Framework for Mining High-Value Task-Oriented Dialogues from Streaming Media](http://arxiv.org/abs/2605.25162v1)
  来源：arXiv | 日期：2026-05-24 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models for vertical domains are bottlenecked by the scarcity of complex, domain-specific task-oriented dialogues. Existing data acquisition pipelines face a persistent trilemma: expert annotation is expens...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [EfficientGraph-RAG: Structured Retrieval-State Management for Cross-Task Retrieval-Augmented Generation](http://arxiv.org/abs/2605.25379v1)
  来源：arXiv | 日期：2026-05-25 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) has become the standard way to ground large language models in external knowledge, but many systems still organize evidence as flat chunks and retrieve it through largely unstructured...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Large language model inference of macromolecular complex composition via model consensus and experimental data integration](https://www.biorxiv.org/content/10.64898/2026.05.20.726735v1)
  来源：bioRxiv | 日期：2026-05-23 | 相关度：7.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are poised to reshape how biologists retrieve specialized knowledge at scale. Yet their performance on deep, domain-specific queries is poorly defined because much biological information resi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A Generative Approach for Semantic Auditing of Electronic Health Records](http://arxiv.org/abs/2507.02628v2)
  来源：arXiv | 日期：2025-07-03 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：The reliability of clinical artificial intelligence (AI) depends on high-quality data, yet Electronic Health Records are often inconsistent with existing scientific knowledge. Current quality assessments are limited: the...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Computational prediction resolves thousands of homooligomeric phage protein structures](https://www.biorxiv.org/content/10.64898/2026.05.24.727406v1)
  来源：bioRxiv | 日期：2026-05-25 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Bacteriophages (phages) play essential roles in microbial systems, yet most phage proteins remain poorly characterised. Protein tertiary and quaternary structure information contributes valuable information about protein...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MimirRAG: A Multi-Agent RAG Framework for Financial Data Retrieval with Metadata Integration](http://arxiv.org/abs/2605.25030v1)
  来源：arXiv | 日期：2026-05-24 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) systems offer a promising approach to reduce hallucinations and improve answer accuracy in large language models (LLMs), a requirement for reliable, financial analysis where answers m...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Leveraging Spreading Activation for Improved Document Retrieval in Knowledge-Graph-Based RAG Systems](http://arxiv.org/abs/2512.15922v3)
  来源：arXiv | 日期：2025-12-17 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Despite initial successes and a variety of architectures, retrieval-augmented generation systems still struggle to reliably retrieve and connect the multi-step evidence required for complicated reasoning tasks. Most of t...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering](http://arxiv.org/abs/2601.03014v3)
  来源：arXiv | 日期：2026-01-06 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Traditional Retrieval-Augmented Generation (RAG) effectively supports single-hop question answering with large language models but faces significant limitations in multi-hop question answering tasks, which require combin...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [PlanRAG-Audio: Planning and Retrieval Augmented Generation for Long-form Audio Understanding](http://arxiv.org/abs/2605.20414v2)
  来源：arXiv | 日期：2026-05-19 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Long-form audio understanding poses significant challenges for large audio language models (LALMs) due to the extreme length of audio sequences and the need to reason over heterogeneous acoustic cues distributed over tim...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Extraction of Human Phenotype Ontology (HPO) Concepts from Clinical Notes Utilizing Large Language Models (LLM) with Model Context Protocol (MCP)](https://www.medrxiv.org/content/10.64898/2026.05.23.26353963v1)
  来源：medRxiv | 日期：2026-05-25 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Background: Accurate extraction of Human Phenotype Ontology (HPO) terms from clinical notes is essential for variant prioritization and genetic diagnosis. Large language models (LLMs) often struggle to balance precision,...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [NiCLIP: Neuroimaging contrastive language-image pretraining model for predicting text from brain activation images](https://www.biorxiv.org/content/10.1101/2025.06.14.659706v3)
  来源：bioRxiv | 日期：2026-05-23 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Predicting cognitive processes from brain activation maps has remained an open question within the neuroscience community for many years. Meta-analytic functional decoding methods aim to tackle this issue by providing a ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MultiPUFFIN: A Multimodal Domain-Constrained Foundation Model for Molecular Property Prediction of Small Molecules](http://arxiv.org/abs/2603.00857v2)
  来源：arXiv | 日期：2026-03-01 | 相关度：2.75 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：MultiPUFFIN is a domain-informed multimodal foundation model for predicting thermophysical properties of small molecules, addressing a critical gap in chemical engineering, drug discovery, and materials science. Existing...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [H$^{2}$MT: Semantic Hierarchy-Aware Hierarchical Memory Transformer](http://arxiv.org/abs/2605.24930v1)
  来源：arXiv | 日期：2026-05-24 | 相关度：2.75 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Transformer-based LLMs achieve strong results on many language tasks; however, long inputs remain challenging because context windows are finite, and prefill latency and memory grow rapidly with prompt length. Flat token...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [When Reasoning Hurts: Source-Aware Evaluation of Frontier LLMs for Clinical SOAP Note Generation](http://arxiv.org/abs/2605.24902v1)
  来源：arXiv | 日期：2026-05-24 | 相关度：2.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：Reasoning-enabled LLMs perform strongly on medical reasoning benchmarks, but it remains unclear whether these gains transfer to structured clinical documentation; we investigate this question using SOAP note generation f...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LipoAgent: Coordinating Fine-Tuned LLM Agents for Safer Lipid Design](http://arxiv.org/abs/2605.25250v1)
  来源：arXiv | 日期：2026-05-24 | 相关度：2.1 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Lipid nanoparticles (LNPs) are among the most clinically mature platforms for nucleic acid delivery, yet designing lipids that are both effective and biologically safe remains a major bottleneck. In practical screening, ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AutoSOTA: An End-to-End Automated Research System for State-of-the-Art AI Model Discovery](http://arxiv.org/abs/2604.05550v2)
  来源：arXiv | 日期：2026-04-07 | 相关度：2.1 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Artificial intelligence research increasingly depends on prolonged cycles of reproduction, debugging, and iterative refinement to achieve State-Of-The-Art (SOTA) performance, creating a growing need for systems that can ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AutoSG: LLM-Driven Solver Generation Solely from Task Prompts for Expensive Optimization](http://arxiv.org/abs/2605.25658v1)
  来源：arXiv | 日期：2026-05-25 | 相关度：2.05 | 新颖度：6.06
  匹配主题：foundation_model_agent
  中文摘要：Expensive optimization tasks are ubiquitous in real-world applications, demanding highly specialized solvers. While LLM-driven automated solver generation shows promise, current paradigms face three critical issues when ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SMDD-Bench: Can LLMs Solve Real-World Small Molecule Drug Design Tasks?](http://arxiv.org/abs/2605.21740v2)
  来源：arXiv | 日期：2026-05-20 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：LLM agents have incredible potential for scientific discovery applications. However, the performance of LLM agents on real-world, small molecule drug design (SMDD) tasks across diverse chemistries and targets is unclear....
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AutoResearchClaw: Self-Reinforcing Autonomous Research with Human-AI Collaboration](http://arxiv.org/abs/2605.20025v2)
  来源：arXiv | 日期：2026-05-19 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Automating scientific discovery requires more than generating papers from ideas. Real research is iterative: hypotheses are challenged from multiple perspectives, experiments fail and inform the next attempt, and lessons...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Retrieval as Reasoning: Self-Evolving Agent-Native Retrieval via LLM-Wiki](http://arxiv.org/abs/2605.25480v1)
  来源：arXiv | 日期：2026-05-25 | 相关度：1.4 | 新颖度：5.74
  匹配主题：未命中具体主题
  中文摘要：LLM agents require retrieval to behave less like one-shot context fetching and more like reasoning: searching, reading, traversing, and deciding when evidence is sufficient. However, Retrieval-Augmented Generation (RAG) ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Hybrid Deep Searcher: Scalable Parallel and Sequential Search Reasoning](http://arxiv.org/abs/2508.19113v3)
  来源：arXiv | 日期：2025-08-26 | 相关度：0.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Large reasoning models (LRMs) combined with retrieval-augmented generation (RAG) have enabled deep research agents capable of multi-step reasoning with external knowledge retrieval. However, we find that existing approac...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Iterate Until Retrieved: Factual Nugget Optimization for Discoverable Continual Corrections in Agentic RAG](http://arxiv.org/abs/2605.25641v1)
  来源：arXiv | 日期：2026-05-25 | 相关度：0.7 | 新颖度：6.01
  匹配主题：未命中具体主题
  中文摘要：Agentic retrieval-augmented generation (RAG) systems in complex B2B (business-to-business) settings may often receive free-form response feedback. Rather than generic feedback signals such as style, preference, or overal...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [PerSoMed: A Large-Scale Balanced Dataset for Persian Social Media Text Classification](http://arxiv.org/abs/2602.19333v2)
  来源：arXiv | 日期：2026-02-22 | 相关度：1.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：This research introduces the first large-scale, well-balanced Persian social media text classification dataset, specifically designed to address the lack of comprehensive resources in this domain. The dataset comprises 3...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Interpreting Omics Data Analysis with Large Language Models for Disease Target and Drug Discovery](https://www.biorxiv.org/content/10.64898/2026.04.30.721768v2)
  来源：bioRxiv | 日期：2026-05-23 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：在生物医学发现中，整合文献先验知识对于解释数值组学数据以识别疾病靶点和药物至关重要。单纯的大语言模型（LLMs）虽能快速检索疾病机制，但由于缺乏队列特异性的定量证据，其输出在靶点和药物优先级排序上往往泛泛且不可靠。本研究提出了一种溯源感知的“Text-to-Target”框架，将模式约束的多模型LLM检索与数值组学数据分析相结合。核心设计是模态感知融合步骤：将候选对象划分为重叠支持的锚点、仅检索的隐藏枢纽和网络涌现的新颖节点，并在拓扑约...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Specification-Based Code-Text-Code Reengineering for LLM-Mediated Software Evolution](http://arxiv.org/abs/2605.25232v1)
  来源：arXiv | 日期：2026-05-24 | 相关度：2.05 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Direct Code2Code transformation remains challenging to control because it can preserve surface-level syntax while introducing semantic drift, hidden behavioral changes, loss of traceability, non-idiomatic target implemen...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [An Efficient and Privacy-Preserving Architecture for Cross-Institutional Collaborative RAG](http://arxiv.org/abs/2605.25716v1)
  来源：arXiv | 日期：2026-05-25 | 相关度：1.4 | 新颖度：6.52
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) empowers LLMs with external knowledge, making cross-institutional domain-specific knowledge base integration a highly promising deployment paradigm. Despite this potential, strict pri...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [BioGraphX-RNA: A Universal Physicochemical Graph Encoding for Interpretable RNA Subcellular Localization Prediction](https://www.biorxiv.org/content/10.64898/2026.02.23.707573v2)
  来源：bioRxiv | 日期：2026-05-24 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：RNA subcellular localization is a critical determinant of cellular function. However, current computational approaches often operate as "black boxes," overlooking the complex interplay among sequence, structure, and phys...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Micro-Swarm Locomotion Optimization in Dynamic Flow using Multi-Objective Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2605.25025v1)
  来源：arXiv | 日期：2026-05-24 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Coordinating micro-robotic swarms in physiologically realistic, time-dependent fluid environments remains an unsolved challenge for biomedical and environmental applications. We present a hybrid Computational Fluid Dynam...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [AI and longevity medicine: unlocking predictive and preventive strategies for healthy aging.](https://pubmed.ncbi.nlm.nih.gov/42184901/)
  来源：PubMed | 日期：2026-05-24 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Longevity medicine is transforming healthcare by shifting the focus from disease treatment toward the preservation of function, resilience, and healthspan. In parallel, artificial intelligence (AI) has emerged as a power...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [What Gets Cited: Competitive GEO in AI Answer Engines](http://arxiv.org/abs/2605.25517v1)
  来源：arXiv | 日期：2026-05-25 | 相关度：2.1 | 新颖度：6.11
  匹配主题：未命中具体主题
  中文摘要：AI answer engines generate answers from retrieved pages but cite only a few sources. This makes visibility depend not just on ranking, but on being cited. We study competitive Generative Engine Optimization (GEO): when t...
  为什么值得看：What Gets Cited: Competitive GEO in AI A 与你的主题有弱匹配，暂时保留作低优先级跟踪。
