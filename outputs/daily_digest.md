# 每日论文监控日报 (2026-11-02)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 31 篇新论文。

## 抓取状态

- arXiv：成功，命中 13 篇
- PubMed：成功，命中 159 篇
- bioRxiv：成功，命中 10 篇
- medRxiv：成功，命中 6 篇

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [Medical students and clinical teachers experiences and perceptions of using AI-based simulated patients in psychiatry clinical skills training, a qualitative analysis](https://www.medrxiv.org/content/10.64898/2026.10.28.26366085v1)
  来源：medRxiv | 日期：2026-10-30 | 相关度：7.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Objectives: To explore medical students' and clinical teachers' experiences and perceptions of an AI-based simulated patient using a large language model (LLM-ASP) for psychiatry clinical skills training, to inform its d...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Applications of large language model in general practice: a qualitative interview study with professionals and patients](https://www.medrxiv.org/content/10.64898/2026.10.30.26366911v1)
  来源：medRxiv | 日期：2026-11-01 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Background: Workload is increasing in general practice. Large language models (LLMs) are a promising tool that could relieve part of this workload. However, existing studies offer little insight into how professionals an...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DeFT-RAG: Decomposing Multi-Hop Questions into Self-Contained Sub-Questions with Reusable Answers](http://arxiv.org/abs/2610.37826v2)
  来源：arXiv | 日期：2026-10-27 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) lets a large language model (LLM) answer questions by retrieving relevant passages from a large corpus. However, RAG struggles with multi-hop questions, which require chaining facts s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Physics-Audited Agentic Discovery in Scientific Machine Learning](http://arxiv.org/abs/2607.07379v2)
  来源：arXiv | 日期：2026-07-08 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Agentic discovery can yield mechanics surrogates with low validation error that nonetheless violate physical requirements. We present Physics-Audited Agentic SciML (PA-SciML), a framework combining large language model a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SpectRAG: Weighted Chunk Graphs for Token-Budgeted Context Selection in Multi-Hop Retrieval-Augmented Generation](http://arxiv.org/abs/2610.36991v3)
  来源：arXiv | 日期：2026-10-27 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) systems ground large language models (LLMs) by retrieving external evidence and conditioning generation on the retrieved context. Although dense retrieval is effective for local seman...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Harness engineering enables a multi-agent LLM system to generate cross-domain hypotheses beyond single-investigator reach](https://www.biorxiv.org/content/10.64898/2026.10.25.761203v1)
  来源：bioRxiv | 日期：2026-10-30 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly used to generate scientific hypotheses, and a more capable model is widely assumed to drive output quality. We tested this with a biology-focused multi-agent system coupling ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [A Deep Learning Model for Prediction of Unknown Gene Functionality: Gene Bio-BERT.](https://pubmed.ncbi.nlm.nih.gov/42573472/)
  来源：PubMed | 日期：2026-11-01 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：The Human Genome Project (HGP) was a large international research effort that timelined between 1990 and 2003, marking the successful mapping of the entire human genome. Despite the promising performance of deep learning...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Hierarchical Dual-Graph Retrieval for Long-form Audio Reasoning](http://arxiv.org/abs/2610.41390v1)
  来源：arXiv | 日期：2026-10-30 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large audio language models (LALMs) struggle with long-form audio reasoning, as processing entire recordings often limits to capture query-relevant content distributed across distant segments while incurring substantial ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [scAnyOmics: Foundation-Model Distillation for Any-to-Any Completion of Multi-omics Virtual Cells](http://arxiv.org/abs/2610.41399v1)
  来源：arXiv | 日期：2026-10-30 | 相关度：4.45 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in single-cell technologies have enabled the profiling of multiple molecular modalities, including transcriptomics, proteomics, and chromatin accessibility, providing a more comprehensive understanding of...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Generative artificial intelligence in medical oncology: A clinically focused narrative review of large language, vision-language, and agentic artificial intelligence systems.](https://pubmed.ncbi.nlm.nih.gov/42912826/)
  来源：PubMed | 日期：2026-11-01 | 相关度：8.5 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Rapid advances in cancer genetics and genomics, pathophysiology, diagnostics, and therapeutics have substantially increased the complexity of clinical oncology. Integrating large and diverse data streams into timely, pat...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Emerging advances in multimodal AI in cancer immunotherapy: from multi-scale data integration to clinical decision support.](https://pubmed.ncbi.nlm.nih.gov/42791141/)
  来源：PubMed | 日期：2026-10-30 | 相关度：7.8 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Immunotherapy is increasingly reshaping the therapeutic landscape of clinical oncology by inducing effective tumor regression and durable responses in various types of human cancers. However, a substantial fraction of pa...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [IBDome: An Integrated Molecular, Histopathological, and Clinical Atlas of Inflammatory Bowel Diseases.](https://pubmed.ncbi.nlm.nih.gov/42269946/)
  来源：PubMed | 日期：2026-11-01 | 相关度：3.75 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Multiomic and multimodal datasets with detailed clinical annotations offer significant potential to advance understanding of inflammatory bowel diseases (IBDs), refine diagnostics, and enable personalized therapeutic str...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Nereus: A Large-Scale Underwater Dataset for Fine-Grained Attribute Understanding and Grounded Counting Perception](http://arxiv.org/abs/2610.41705v1)
  来源：arXiv | 日期：2026-10-30 | 相关度：2.05 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Underwater imagery records rich ecological information and supports applications such as science communication, fishery monitoring, ecological conservation, and oceanographic research. Beyond general scene understanding,...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Few-shot regulatory sequence design with a genomic language model](https://www.biorxiv.org/content/10.64898/2026.10.28.762639v1)
  来源：bioRxiv | 日期：2026-10-30 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：A central challenge in generative biology is translating knowledge learned from natural sequences and experiments into designs with desired functions. In-context learning (ICL) is an emergent capability of large language...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [dictyBase 2026: a reimplementation of the Dictyostelium model organism database on minimal infrastructure.](https://pubmed.ncbi.nlm.nih.gov/42958965/)
  来源：PubMed | 日期：2026-10-30 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Dictyostelium discoideum is a model organism used to investigate a wide array of biological processes including chemotaxis, cell motility, phagocytosis, multicellular development, and autophagy. Many of its genes have hu...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [From DNA to drug discovery AI models for cardiovascular precision medicine.](https://pubmed.ncbi.nlm.nih.gov/42269859/)
  来源：PubMed | 日期：2026-11-01 | 相关度：4.45 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Cardiovascular diseases remain the world's leading cause of death-yet the molecular mechanisms linking genetic variation to clinical outcomes are still poorly mapped. Recent advances in artificial intelligence (AI), espe...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [From WSIs to Bulk, Spatial and Single-Cell Transcriptomics via Multi-Scale Graph Neural Networks](http://arxiv.org/abs/2610.41692v1)
  来源：arXiv | 日期：2026-10-30 | 相关度：1.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Understanding the spatial distribution of gene expression is key to studying complex diseases like cancer. While Spatial Transcriptomics (ST) and Single-Cell Transcriptomics (scT) provide high-resolution insights, they r...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CryoQSeg: robust particle segmentation for cryo-EM with Qwen-Image-Edit.](https://pubmed.ncbi.nlm.nih.gov/42878722/)
  来源：PubMed | 日期：2026-11-01 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Accurate particle picking remains a critical step in cryo-electron microscopy (cryo-EM) single-particle analysis, and the field has witnessed the development of a broad spectrum of approaches - from classical template-ba...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AI-Driven Multiomics Biomarkers for Precision Oncology: Navigating the Translational Gap and Regulatory Hurdles.](https://pubmed.ncbi.nlm.nih.gov/42560117/)
  来源：PubMed | 日期：2026-11-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：The discussion on precision oncology integrates multiomics technologies and artificial intelligence, specifically addressing biomarker discovery and personalized therapeutic strategies. In this way, clinical translation ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Logic Hijacking of RAG: Single-Document Poisoning via Local Optimization](http://arxiv.org/abs/2610.34829v2)
  来源：arXiv | 日期：2026-10-26 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Single-document corpus poisoning under black-box access poses a severe threat to Retrieval-Augmented Generation (RAG). However, existing attacks predominantly rely on explicit factual refutations or imperative instructio...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Quantum 3xplorer: AI-Native Engine for Next-Generation Quantum Materials Modeling](http://arxiv.org/abs/2610.42108v1)
  来源：arXiv | 日期：2026-10-30 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Quantum-mechanical approaches, such as density functional theory (DFT), underpin much of modern computational materials science and are the primary source of data for AI-driven discovery. Yet the established electronic-s...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Retrieval-Augmented Initialization with Dual-Guided Inversion for Flow-Based Inverse Problem Solvers](http://arxiv.org/abs/2610.41695v1)
  来源：arXiv | 日期：2026-10-30 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Flow models have recently emerged as powerful generative priors for solving inverse problems. Despite their success, most existing flow-based inverse problem solvers initialize the reconstruction process with random Gaus...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Transforming one health antimicrobial resistance surveillance in resource-limited countries (RLCs): From point-of-care diagnostics to AI-driven decision support.](https://pubmed.ncbi.nlm.nih.gov/42810525/)
  来源：PubMed | 日期：2026-11-01 | 相关度：5.95 | 新颖度：0.25
  匹配主题：pathogenomics, application_monitoring
  中文摘要：Antimicrobial resistance (AMR) is a major and escalating global problem, particularly for resource-limited countries (RLCs) with limited capacity to diagnose diseases, inadequate surveillance systems, insufficient antimi...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Development of an AI-Based smartphone application for rapid tick identification and geospatial mapping: A pilot study.](https://pubmed.ncbi.nlm.nih.gov/42735788/)
  来源：PubMed | 日期：2026-11-01 | 相关度：4.4 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：Tick-borne diseases, particularly spotted fever group rickettsioses in the western regions of Japan, represent an increasing public health concern. Accurate tick identification is clinically important because pathogen tr...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial Intelligence-Driven Multiomics Integration in Lung Cancer: From Data Convergence to Precision Phenomics.](https://pubmed.ncbi.nlm.nih.gov/42566262/)
  来源：PubMed | 日期：2026-11-01 | 相关度：3.75 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：肺癌因其广泛的分子异质性、晚期诊断和治疗耐药性，仍是全球癌症死亡的主要原因。高通量组学技术的进步实现了对肿瘤在基因组、表观基因组、转录组、蛋白质组和代谢组等多生物层面的全面表征。然而，单组学分析仅能提供碎片化的肿瘤生物学见解，凸显了整合多组学方法的需求。人工智能（AI），特别是机器学习和深度学习，已成为整合异构数据集并揭示生物学和临床相关模式的强大工具。本综述总结了AI驱动的肺癌多组学整合的最新进展，重点介绍了其在分子分型、生物标志物发...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [AI-based multimodal integration of genomics and electronic health records.](https://pubmed.ncbi.nlm.nih.gov/42576006/)
  来源：PubMed | 日期：2026-11-01 | 相关度：3.75 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：The widespread adoption of electronic health records (EHRs), which capture patient-specific longitudinal information on diagnoses, laboratory tests, clinical procedures, and outcomes, has created unprecedented opportunit...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Harnessing Extracellular Vesicles for Precision Diagnostics and Infectious Disease Management: Integrating Host- and Pathogen-Derived Cues.](https://pubmed.ncbi.nlm.nih.gov/42964774/)
  来源：PubMed | 日期：2026-10-30 | 相关度：2.45 | 新颖度：0.25
  匹配主题：application_monitoring
  中文摘要：Conventional infectious disease diagnostics often rely on detecting pathogen-derived factors or an immune response directed against them to diagnose disease. However, these approaches can lack the specificity to distingu...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Traumatic brain injury: Multi-omics insights into brain aging, neurodegeneration, and precision therapeutics.](https://pubmed.ncbi.nlm.nih.gov/42660464/)
  来源：PubMed | 日期：2026-11-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Traumatic brain injury (TBI) is a major cause of mortality and persistent neurological disability and is increasingly recognized as a potential contributor to accelerated brain aging and long-term neurodegenerative proce...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial intelligence for predicting BCG response in non-muscle-invasive bladder cancer: a systematic review.](https://pubmed.ncbi.nlm.nih.gov/42605566/)
  来源：PubMed | 日期：2026-11-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：To systematically identify, appraise and synthesise artificial intelligence (AI) and machine-learning (ML) models that predict treatment response and clinical outcomes after intravesical bacillus Calmette-Guérin (BCG) in...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial intelligence in pediatric nephrology: current applications and emerging frameworks for evidence generation.](https://pubmed.ncbi.nlm.nih.gov/41739204/)
  来源：PubMed | 日期：2026-11-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Artificial intelligence (AI) is rapidly transforming many areas of medicine. Pediatric nephrology may be a field of particular relevance due to its data-rich environments, rarity of diseases, long-term follow-up needs, a...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Self-Building Labs](http://arxiv.org/abs/2610.23826v2)
  来源：arXiv | 日期：2026-10-16 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Self-driving laboratories (SDLs) accelerate scientific discovery by automating experimental execution and optimization. AI agents can increasingly propose new experiments, but existing SDLs can only run the procedures th...
  为什么值得看：Self-Building Labs 与你的主题有弱匹配，暂时保留作低优先级跟踪。
