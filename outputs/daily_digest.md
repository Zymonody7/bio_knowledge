# 每日论文监控日报 (2026-06-28)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 30 篇新论文。

## 抓取状态

- arXiv：成功，命中 14 篇
- PubMed：成功，命中 46 篇
- bioRxiv：成功，命中 15 篇
- medRxiv：成功，命中 10 篇

## 最值得看

### Foundation Model / Agent

- [SPEAK: Spatial Prompting with Expert Aligned Knowledge for Tissue Domain Identification in Spatial Transcriptomics](https://www.biorxiv.org/content/10.64898/2026.06.22.733750v1)
  来源：bioRxiv | 日期：2026-06-26 | 相关度：7.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Spatially resolved transcriptomic (SRT) data requires spatial domain identification to enable tissue microenvironment-specific downstream analyses. Here we present SPEAK (Spatial Prompting with Expert-Aligned Knowledge),...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [EpiESM-GA: Resource-Efficient Protein Foundation Model Features for Equitable B-Cell Epitope Prediction](https://www.biorxiv.org/content/10.64898/2026.06.22.733745v1)
  来源：bioRxiv | 日期：2026-06-26 | 相关度：9.8 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：Prediction of B-cell epitopes can assist in reducing costly wet-lab screening in vaccine design, diagnostics, and antibody discovery. However, current predictors often suffer from noisy labels, weak generalization, and s...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [Evaluating Generative Video AI for Standardized Psychiatric Patient Simulation With Graded Hygiene Deterioration.](https://www.medrxiv.org/content/10.64898/2026.06.22.26356153v1)
  来源：medRxiv | 日期：2026-06-25 | 相关度：8.9 | 新颖度：1.7
  匹配主题：foundation_model_agent
  中文摘要：IntroductionA clinicians initial assessment during the mental status examination (MSE) places substantial weight on a patients general appearance, grooming, and hygiene. However, the logistical difficulty of producing si...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Historical Perspectives in Medicine using a Large Language Model: Emulating an 18th Century Physician](https://www.medrxiv.org/content/10.64898/2026.02.10.26345990v3)
  来源：medRxiv | 日期：2026-06-26 | 相关度：7.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：18世纪医学文献记录了临床推理演变的关键时期，但其在现代医学教育中的整合程度有限。本研究开发了一个受历史约束的大语言模型（LLM）教育平台，旨在模拟18世纪医生的诊断推理、语言风格和概念框架。研究采用现代GPT架构，通过严格的指令约束，将其知识范围限制在精心挑选的6本17至18世纪基础医学著作中，并设置护栏以防止出现时代错误术语和现代医学概念。评估通过将模型的诊断和治疗方案与原始历史文献进行定性对比，并将其应用于现代临床案例以展示古今差...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CellOS: Learning a World Model of Cellular State through Joint Embedding Prediction](https://www.biorxiv.org/content/10.64898/2026.06.18.733163v2)
  来源：bioRxiv | 日期：2026-06-25 | 相关度：7.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Foundation models learned from single-cell transcriptomes are central to the prospect of AI virtual cell that can represent, query and predict cellular state. However, most current single-cell foundation models learn fro...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Training-Free Generation of Protein Sequences from Small Family Alignments via Stochastic Attention](http://arxiv.org/abs/2603.14717v2)
  来源：arXiv | 日期：2026-03-16 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Generating novel protein sequences that respect a family's statistical constraints typically requires training deep generative models on thousands to millions of examples. Yet most protein families are small: the median ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Semantic Early-Stopping for Iterative LLM Agent Loops](http://arxiv.org/abs/2606.27009v1)
  来源：arXiv | 日期：2026-06-25 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Multi-agent large language model (LLM) loops, for example a Writer that drafts and a Critic that revises, are almost always terminated by a fixed iteration cap (max_iterations). This is a syntactic kill-switch: it is bli...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic AI for Structural Elucidation and Discovery of Drug Metabolites from Mass Spectrometry Data](https://www.biorxiv.org/content/10.64898/2026.06.23.734138v1)
  来源：bioRxiv | 日期：2026-06-26 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：The majority of chemical signals detected in public metabolomics repositories remain structurally undefined. Large language models (LLMs) are probabilistic systems whose capacity to generate outputs beyond their training...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [NanoCellAnnotator: Formalizing Expert Cell Type Annotation with Large Language Models](https://www.biorxiv.org/content/10.64898/2026.06.21.728965v1)
  来源：bioRxiv | 日期：2026-06-25 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Motivation: Cell-type annotation in spatial transcriptomics is challenging due to sparse gene panels, spatial heterogeneity, and limited availability of tissue-matched reference atlases. Recent approaches have explored l...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [A Reproducible Clinical Decision-Support Suite on MIMIC-IV](https://www.medrxiv.org/content/10.64898/2026.06.23.26356380v1)
  来源：medRxiv | 日期：2026-06-25 | 相关度：7.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：This work is a direct extension and modernisation of zMeds 2021 clinical AI/ML modelling effort, which established the companys first intensive-care risk models on earlier critical-care data. Here we re-platform that wor...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Clinically aligned rationale generation for glaucoma subtype classification via a knowledge-distilled language model](https://www.medrxiv.org/content/10.64898/2026.06.15.26355522v1)
  来源：medRxiv | 日期：2026-06-26 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Automated glaucoma subtype classification from clinical notes remains clinically unactionable without subspecialty-aligned explanations supporting clinician-facing deployment. We extended our Ci-SSGAN with a GPT-5.2-to-Q...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [OncoGen.AI: an integrated platform for automated genomic analysis and reporting in precision oncology.](https://pubmed.ncbi.nlm.nih.gov/42362719/)
  来源：PubMed | 日期：2026-06-27 | 相关度：4.6 | 新颖度：6.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：The translation of complex cancer genomics into clinically actionable insights is a critical bottleneck in precision oncology. To automate the entire workflow, we present OncoGen.AI, an end-to-end, containerized platform...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Agents That Know Too Much: A Data-Centric Survey of Privacy in LLM Agents](http://arxiv.org/abs/2606.26627v1)
  来源：arXiv | 日期：2026-06-25 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Large language model agents increasingly query databases, search document collections, call external APIs, remember past interactions, and act on a user's behalf. As they move from answering questions to operating over s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [KARLA: Knowledge-base Augmented Retrieval for Language Models](http://arxiv.org/abs/2606.26807v1)
  来源：arXiv | 日期：2026-06-25 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：We propose a new method that allows an LLM to automatically pull in factual knowledge from a knowledge base during token generation. This means that (1)~factual knowledge in the LLM output can be updated without retraini...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The Geometry of Updates: Fisher Alignment at Vocabulary Scale](http://arxiv.org/abs/2606.27242v1)
  来源：arXiv | 日期：2026-06-25 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Training-free source selection for LLM families with shared vocabularies arises in scientific string domains such as SMILES, protein, and genomic sequences, where candidate corpora share a tokenizer but differ in predict...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MIRROR: Novelty-Constrained Memory-Guided MCTS Red-Teaming for Agentic RAG](http://arxiv.org/abs/2606.26793v1)
  来源：arXiv | 日期：2026-06-25 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Multimodal agentic retrieval-augmented generation (RAG) systems expand the attack surface beyond prompt injection to include text poisoning, image injection, direct-query attacks, and orchestrator-level tool manipulation...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Socratic agents for autonomous scientific discovery in high-dimensional physical systems](http://arxiv.org/abs/2606.26722v1)
  来源：arXiv | 日期：2026-06-25 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：The automation of scientific discovery has reached an inflection point. While AI systems now operate instruments, optimize parameters and generate hypotheses, most remain procedural: they execute workflows fixed by human...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Performance of Google NotebookLM for AI-assisted data extraction and consensus statement generation in a heterogenous systematic review on inflammatory bowel disease, obesity, and cardiometabolic comorbidities: A Methodological Report](https://www.medrxiv.org/content/10.64898/2026.06.16.26355773v1)
  来源：medRxiv | 日期：2026-06-26 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Background: Large language models (LLMs) offer promise for systematic review data extraction, but performance in complex multidisciplinary domains and utility for clinical statement generation remain insufficiently descr...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Prompt, Plan, Extract: Zero-Shot Agentic LLMs Workflows for Lung Pathology Extraction from Clinical Narratives](http://arxiv.org/abs/2606.19852v2)
  来源：arXiv | 日期：2026-06-18 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Information extraction from pathology reports is essential for cancer staging, tumor registry population. Yet key data remains embedded in narrative reports, making manual extraction labor-intensive and error-prone. Trad...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [ESM2-BiMamba: A Length-Adaptive Hybrid Framework for Efficient Concurrent Prediction of DNA-Binding Proteins and DNA-Binding Residue Sites.](https://pubmed.ncbi.nlm.nih.gov/42348910/)
  来源：PubMed | 日期：2026-06-25 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Accurate identification of DNA-binding proteins (DBPs) and their DNA-binding residue sites (DBSs) is essential for understanding gene regulatory processes. Despite recent progress achieved by protein language models, cur...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Sutra: Tensor-Op RNNs as a Compilation Target for Vector Symbolic Architectures](http://arxiv.org/abs/2605.20919v3)
  来源：arXiv | 日期：2026-05-20 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Sutra is a typed, purely functional programming language whose compiled forward pass is a PyTorch neural network. The compiler beta-reduces the whole program -- primitives, control flow, string I/O -- to one fused tensor...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Ambiguity-Aware Multi-Stage Cell-Type Annotation for Spatial Transcriptomics](https://www.biorxiv.org/content/10.64898/2026.06.21.733596v1)
  来源：bioRxiv | 日期：2026-06-25 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Spatial transcriptomics enables characterization of cellular organization in intact tissue, but robust cell type annotation remains challenging due to heterogeneous expression profiles, mixed populations, and transitiona...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Long-stranded XNA-cssDNA hybrids for robust data storage.](https://pubmed.ncbi.nlm.nih.gov/42341119/)
  来源：PubMed | 日期：2026-06-26 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：DNA is a promising medium for data storage due to its high density and low energy cost. Long-stranded DNA with minimal indexing improves storage density but suffers from poor stability. To address this, we introduce a lo...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [LCAi: Life Cycle Assessment with big data fusion and retrieval-augmented generation-assisted interpretation](http://arxiv.org/abs/2606.26857v1)
  来源：arXiv | 日期：2026-06-25 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：The interpretation phase of life cycle assessment often lacks structured mechanisms for translating quantified improvement opportunities addressing environmental hotspots into actionable strategic pathways under technolo...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Machine Learning for Microbial Cell Factories: Pathway Design, Enzyme Engineering, and Metabolic Regulation.](https://pubmed.ncbi.nlm.nih.gov/42359840/)
  来源：PubMed | 日期：2026-06-26 | 相关度：2.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Microbial cell factories represent sustainable platforms for the production of fuels, chemicals, and therapeutics, but their development is limited by challenges in pathway discovery, enzyme optimization, and metabolic r...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Quantitative Assessment of Environmental Blood Contamination in Interventional Radiology Operating Rooms: A Cross-Sectional Study.](https://pubmed.ncbi.nlm.nih.gov/42364880/)
  来源：PubMed | 日期：2026-06-27 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Healthcare-associated infections remain a global threat to patient safety, with contaminated environmental surfaces serving as important pathogen transmission vectors. Interventional radiology operating rooms are high-fr...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Mapping Parkinson's Disease Progression through Deep Plasma Proteomics and Functional Genomics](https://www.biorxiv.org/content/10.64898/2026.01.19.699565v3)
  来源：bioRxiv | 日期：2026-06-25 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Parkinsons disease (PD) is a progressive neurodegenerative disorder lacking disease-modifying therapies, and its clinical management is limited by the absence of accessible biomarkers for tracking disease progression and...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [PhysRAG: Enhancing Physics-Awareness in Video Generation via Retrieval-Augmented Generation](http://arxiv.org/abs/2606.26916v1)
  来源：arXiv | 日期：2026-06-25 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Developing physically aware video generation models remains a significant challenge due to the difficulty in capturing diverse physical phenomena, such as thermal dynamics, mechanics, and optics. In this work, we introdu...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 其他

- [Response consistency of ChatGPT-4o for Type 2 Diabetes Nutrition and Physical-activity Recommendations: A Pilot NLP-based Assessment of GPT outputs](https://www.medrxiv.org/content/10.64898/2026.06.23.26356399v1)
  来源：medRxiv | 日期：2026-06-26 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Generative AI tools such as ChatGPT are increasingly used by the public to seek guidance on diet and physical activity for type 2 diabetes (T2D) prevention and management. However, the consistency of model outputs across...
  为什么值得看：medRxiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [Eyes-on-Me: Scalable RAG Poisoning through Transferable Attention-Steering Attractors](http://arxiv.org/abs/2510.00586v3)
  来源：arXiv | 日期：2025-10-01 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Existing data poisoning attacks on retrieval-augmented generation (RAG) systems scale poorly because they require costly optimization of poisoned documents for each target phrase. We introduce Eyes-on-Me, a modular attac...
  为什么值得看：Eyes-on-Me: Scalable RAG Poisoning throu 与你的主题有弱匹配，暂时保留作低优先级跟踪。
