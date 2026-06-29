# 每日论文监控日报 (2026-06-29)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 22 篇新论文。

## 抓取状态

- arXiv：成功，命中 8 篇
- PubMed：成功，命中 35 篇
- bioRxiv：成功，命中 19 篇
- medRxiv：成功，命中 5 篇

## 最值得看

### 方法创新

- [EpiESM-GA: Resource-Efficient Protein Foundation Model Features for Equitable B-Cell Epitope Prediction](https://www.biorxiv.org/content/10.64898/2026.06.22.733745v1)
  来源：bioRxiv | 日期：2026-06-26 | 相关度：9.8 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Prediction of B-cell epitopes can assist in reducing costly wet-lab screening in vaccine design, diagnostics, and antibody discovery. However, current predictors often suffer from noisy labels, weak generalization, and s...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [SPEAK: Spatial Prompting with Expert Aligned Knowledge for Tissue Domain Identification in Spatial Transcriptomics](https://www.biorxiv.org/content/10.64898/2026.06.22.733750v1)
  来源：bioRxiv | 日期：2026-06-26 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Spatially resolved transcriptomic (SRT) data requires spatial domain identification to enable tissue microenvironment-specific downstream analyses. Here we present SPEAK (Spatial Prompting with Expert-Aligned Knowledge),...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Historical Perspectives in Medicine using a Large Language Model: Emulating an 18th Century Physician](https://www.medrxiv.org/content/10.64898/2026.02.10.26345990v3)
  来源：medRxiv | 日期：2026-06-26 | 相关度：7.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：18世纪医学文献记录了临床推理演变的关键时期，但其在现代医学教育中的整合程度有限。本研究开发了一个受历史约束的大语言模型（LLM）教育平台，旨在模拟18世纪医生的诊断推理、语言风格和概念框架。研究采用现代GPT架构，通过严格的指令约束，将其知识范围限制在精心挑选的6本17至18世纪基础医学著作中，并设置护栏以防止出现时代错误术语和现代医学概念。评估通过将模型的诊断和治疗方案与原始历史文献进行定性对比，并将其应用于现代临床案例以展示古今差...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Event-Grounded Question Answering over Long Audio via Structured Retrieval](http://arxiv.org/abs/2602.14612v5)
  来源：arXiv | 日期：2026-02-16 | 相关度：6.55 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：Answering natural-language questions over multi-hour audio requires both event recognition and temporal grounding. Current large audio-language models perform well on short clips, but are limited by context length, query...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic Episodic Control](http://arxiv.org/abs/2506.01442v2)
  来源：arXiv | 日期：2025-06-02 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Reinforcement learning (RL) remains fundamentally limited by poor data efficiency and weak generalization. Prior episodic RL methods attempt to alleviate this via external memory modules, yet they suffer from two key lim...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Simplified Sparse Attention via Gist Tokens](http://arxiv.org/abs/2604.20920v2)
  来源：arXiv | 日期：2026-04-22 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Sparse attention can reduce the cost of long-context inference, but most variants introduce new architectural components. We introduce Simplified Sparse Attention (SSA), a simpler approach to sparse attention that requir...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Two-Stage Fine-Tuning for Protein Sequence Generation with Targeted Amino-Acid Composition](http://arxiv.org/abs/2606.27939v1)
  来源：arXiv | 日期：2026-06-26 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Protein language models are standard priors for biological sequence generation, but steering them toward explicit distributional design targets remains largely unexplored. We study a constrained protein generation proble...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Effective structure-aware protein alignment via residue-level contrastive learning](https://www.biorxiv.org/content/10.1101/2024.03.09.583681v2)
  来源：bioRxiv | 日期：2026-06-27 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Protein alignment is indispensable for biological discovery, supporting structure comparison, functional annotation, and evolutionary inference. While structure-based methods are highly effective at detecting structural ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Integrating artificial intelligence and multi-omics data for precision oncology in endometrial cancer: a narrative review.](https://pubmed.ncbi.nlm.nih.gov/42366266/)
  来源：PubMed | 日期：2026-06-29 | 相关度：3.75 | 新颖度：8.99
  匹配主题：foundation_model_agent
  中文摘要：Endometrial cancer (EC) is the most common gynaecological malignancy worldwide, yet the prognosis for advanced and recurrent disease remains poor, highlighting the need for improved diagnostic, prognostic, and therapeuti...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Clinically aligned rationale generation for glaucoma subtype classification via a knowledge-distilled language model](https://www.medrxiv.org/content/10.64898/2026.06.15.26355522v1)
  来源：medRxiv | 日期：2026-06-26 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Automated glaucoma subtype classification from clinical notes remains clinically unactionable without subspecialty-aligned explanations supporting clinician-facing deployment. We extended our Ci-SSGAN with a GPT-5.2-to-Q...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Agentic AI for Structural Elucidation and Discovery of Drug Metabolites from Mass Spectrometry Data](https://www.biorxiv.org/content/10.64898/2026.06.23.734138v1)
  来源：bioRxiv | 日期：2026-06-26 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：The majority of chemical signals detected in public metabolomics repositories remain structurally undefined. Large language models (LLMs) are probabilistic systems whose capacity to generate outputs beyond their training...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [An APOC1+ inflammatory CAF-like state drives a senescent, treatment-resistant niche in rheumatoid arthritis](https://www.biorxiv.org/content/10.64898/2026.04.17.718831v4)
  来源：bioRxiv | 日期：2026-06-28 | 相关度：3.05 | 新颖度：0.25
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：ObjectivesRheumatoid arthritis (RA) synovitis frequently persists despite cytokine-targeted therapies, suggesting the existence of pathogenic stromal programs that sustain chronic inflammation independently of canonical ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agent-Native Immune System: Architecture, Taxonomy, and Engineering](http://arxiv.org/abs/2606.28270v1)
  来源：arXiv | 日期：2026-06-26 | 相关度：2.4 | 新颖度：5.5
  匹配主题：pathogenomics
  中文摘要：The transition from static chat bots to autonomous agents--equipped with persistent memory, tool-use protocols, and multi-agent collaboration--has fundamentally expanded the AI threat landscape. Current defense mechanism...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Performance of Google NotebookLM for AI-assisted data extraction and consensus statement generation in a heterogenous systematic review on inflammatory bowel disease, obesity, and cardiometabolic comorbidities: A Methodological Report](https://www.medrxiv.org/content/10.64898/2026.06.16.26355773v1)
  来源：medRxiv | 日期：2026-06-26 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Background: Large language models (LLMs) offer promise for systematic review data extraction, but performance in complex multidisciplinary domains and utility for clinical statement generation remain insufficiently descr...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Towards Automating Scientific Review with Google's Paper Assistant Tool](http://arxiv.org/abs/2606.28277v1)
  来源：arXiv | 日期：2026-06-26 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Artificial intelligence is driving a revolution in scientific discovery, accelerating everything from hypothesis generation to mathematical theorem proving. However, this rapid acceleration is creating a systemic challen...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Long-stranded XNA-cssDNA hybrids for robust data storage.](https://pubmed.ncbi.nlm.nih.gov/42341119/)
  来源：PubMed | 日期：2026-06-26 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：DNA is a promising medium for data storage due to its high density and low energy cost. Long-stranded DNA with minimal indexing improves storage density but suffers from poor stability. To address this, we introduce a lo...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Machine Learning for Microbial Cell Factories: Pathway Design, Enzyme Engineering, and Metabolic Regulation.](https://pubmed.ncbi.nlm.nih.gov/42359840/)
  来源：PubMed | 日期：2026-06-26 | 相关度：2.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Microbial cell factories represent sustainable platforms for the production of fuels, chemicals, and therapeutics, but their development is limited by challenges in pathway discovery, enzyme optimization, and metabolic r...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [UTRGen: A unified framework for full-spectrum design of mRNA 5' UTRs](https://www.biorxiv.org/content/10.64898/2026.06.26.734691v1)
  来源：bioRxiv | 日期：2026-06-27 | 相关度：1.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：The 5' untranslated region (5' UTR) is a key regulatory element that governs mRNA translation and protein output. However, existing computational methods typically address isolated tasks such as functional prediction or ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Quantitative Assessment of Environmental Blood Contamination in Interventional Radiology Operating Rooms: A Cross-Sectional Study.](https://pubmed.ncbi.nlm.nih.gov/42364880/)
  来源：PubMed | 日期：2026-06-27 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Healthcare-associated infections remain a global threat to patient safety, with contaminated environmental surfaces serving as important pathogen transmission vectors. Interventional radiology operating rooms are high-fr...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SHIFT: Gate-Modulated Activation Steering for Knowledge Conflict Mitigation in Retrieval-Augmented Generation](http://arxiv.org/abs/2606.27786v1)
  来源：arXiv | 日期：2026-06-26 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) enhances LLMs by incorporating external knowledge to support response generation. However, conflicts between retrieved context and parametric knowledge have emerged as a critical chal...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [OncoGen.AI: an integrated platform for automated genomic analysis and reporting in precision oncology.](https://pubmed.ncbi.nlm.nih.gov/42362719/)
  来源：PubMed | 日期：2026-06-27 | 相关度：4.6 | 新颖度：1.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：The translation of complex cancer genomics into clinically actionable insights is a critical bottleneck in precision oncology. To automate the entire workflow, we present OncoGen.AI, an end-to-end, containerized platform...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Response consistency of ChatGPT-4o for Type 2 Diabetes Nutrition and Physical-activity Recommendations: A Pilot NLP-based Assessment of GPT outputs](https://www.medrxiv.org/content/10.64898/2026.06.23.26356399v1)
  来源：medRxiv | 日期：2026-06-26 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Generative AI tools such as ChatGPT are increasingly used by the public to seek guidance on diet and physical activity for type 2 diabetes (T2D) prevention and management. However, the consistency of model outputs across...
  为什么值得看：medRxiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。
