# 每日论文监控日报 (2026-03-18)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 55 篇新论文。

## 抓取状态

- arXiv：成功，命中 52 篇
- PubMed：成功，命中 27 篇
- bioRxiv：成功，命中 20 篇
- medRxiv：成功，命中 4 篇

## 最值得看

### Foundation Model / Agent

- [ELISA: An Interpretable Hybrid Generative AI Agent for Expression-Grounded Discovery in Single-Cell Genomics](http://arxiv.org/abs/2603.11872v2)
  来源：arXiv | 日期：2026-03-12 | 相关度：7.55 | 新颖度：7.5
  匹配主题：foundation_model_agent
  中文摘要：Translating single-cell RNA sequencing (scRNA-seq) data into mechanistic biological hypotheses remains a critical bottleneck, as agentic AI systems lack direct access to transcriptomic representations while expression fo...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [VarDCL: A Multimodal PLM-Enhanced Framework for Missense Variant Effect Prediction via Self-distilled Contrastive Learning](https://www.biorxiv.org/content/10.64898/2026.03.13.711612v1)
  来源：bioRxiv | 日期：2026-03-17 | 相关度：10.0 | 新颖度：6.0
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Abstract. Missense variants are a common type of genetic mutation that can alter the structure and function of proteins, thereby affecting the normal physiological processes of organisms. Accurately distinguishing damagi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [An Interpretable Machine Learning Framework for Non-Small Cell Lung Cancer Drug Response Analysis](http://arxiv.org/abs/2603.16330v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：7.15 | 新颖度：7.29
  匹配主题：foundation_model_agent
  中文摘要：Lung cancer is a condition where there is abnormal growth of malignant cells that spread in an uncontrollable fashion in the lungs. Some common treatment strategies are surgery, chemotherapy, and radiation which aren't t...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 可追踪

### Foundation Model / Agent

- [Intelligent Co-Design: An Interactive LLM Framework for Interior Spatial Design via Multi-Modal Agents](http://arxiv.org/abs/2603.15341v1)
  来源：arXiv | 日期：2026-03-16 | 相关度：7.9 | 新颖度：1.7
  匹配主题：foundation_model_agent
  中文摘要：In architectural interior design, miscommunication frequently arises as clients lack design knowledge, while designers struggle to explain complex spatial relationships, leading to delayed timelines and financial losses....
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AutothinkRAG: Complexity-Aware Control of Retrieval-Augmented Reasoning for Image-Text Interaction](http://arxiv.org/abs/2603.05551v2)
  来源：arXiv | 日期：2026-03-05 | 相关度：7.5 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Multimodal document question answering requires retrieving dispersed evidence from visually rich long documents and performing reliable reasoning over heterogeneous information. Existing multimodal RAG systems remain lim...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OmicClaw: executable and reproducible natural-language multi-omics analysis over the unified OmicVerse ecosystem.](https://www.biorxiv.org/content/10.64898/2026.03.13.711464v1)
  来源：bioRxiv | 日期：2026-03-17 | 相关度：7.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Advances in bulk, single-cell and spatial omics have transformed biological discovery, yet analysis remains fragmented across packages with incompatible interfaces, heterogeneous dependencies and limited workflow reprodu...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Toward Experimentation-as-a-Service in 5G/6G: The Plaza6G Prototype for AI-Assisted Trials](http://arxiv.org/abs/2603.16356v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：6.55 | 新颖度：7.34
  匹配主题：foundation_model_agent
  中文摘要：This paper presents Plaza6G, the first operational Experiment-as-a-Service (ExaS) platform unifying cloud resources with next-generation wireless infrastructure. Developed at CTTC in Barcelona, Plaza6G integrates GPU-acc...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond the Embedding Bottleneck: Adaptive Retrieval-Augmented 3D CT Report Generation](http://arxiv.org/abs/2603.15822v1)
  来源：arXiv | 日期：2026-03-16 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Automated radiology report generation from 3D CT volumes often suffers from incomplete pathology coverage. We provide empirical evidence that this limitation stems from a representational bottleneck: contrastive 3D CT em...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RadAnnotate: Large Language Models for Efficient and Reliable Radiology Report Annotation](http://arxiv.org/abs/2603.16002v1)
  来源：arXiv | 日期：2026-03-16 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Radiology report annotation is essential for clinical NLP, yet manual labeling is slow and costly. We present RadAnnotate, an LLM-based framework that studies retrieval-augmented synthetic reports and confidence-based se...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Protein Design with Agent Rosetta: A Case Study for Specialized Scientific Agents](http://arxiv.org/abs/2603.15952v1)
  来源：arXiv | 日期：2026-03-16 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are capable of emulating reasoning and using tools, creating opportunities for autonomous agents that execute complex scientific tasks. Protein design provides a natural testbed: although mac...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights](http://arxiv.org/abs/2603.16817v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：5.45 | 新颖度：8.26
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) frequently hallucinate, limiting their reliability in knowledge-intensive applications. Retrieval-augmented generation (RAG) and conformal factuality have emerged as potential ways to address...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Automating Skill Acquisition through Large-Scale Mining of Open-Source Agentic Repositories: A Framework for Multi-Agent Procedural Knowledge Extraction](http://arxiv.org/abs/2603.11808v2)
  来源：arXiv | 日期：2026-03-12 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：The transition from monolithic large language models (LLMs) to modular, skill-equipped agents represents a fundamental architectural shift in artificial intelligence deployment. While general-purpose models demonstrate r...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Toward Reliable Scientific Visualization Pipeline Construction with Structure-Aware Retrieval-Augmented LLMs](http://arxiv.org/abs/2603.16057v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Scientific visualization pipelines encode domain-specific procedural knowledge with strict execution dependencies, making their construction sensitive to missing stages, incorrect operator usage, or improper ordering. Th...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Retrieval-Augmented Sketch-Guided 3D Building Generation](http://arxiv.org/abs/2603.16612v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：3.45 | 新颖度：8.09
  匹配主题：foundation_model_agent
  中文摘要：In the early design stage of Japanese detached houses, the lack of a unified design representation among clients, sales representatives, and designers leads to design drift and inefficient feedback. Usually, sketches han...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Machines acquire scientific taste from institutional traces](http://arxiv.org/abs/2603.16659v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：6.45 | 新颖度：7.95
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence matches or exceeds human performance on tasks with verifiable answers, from protein folding to Olympiad mathematics. Yet the capacity that most governs scientific advance is not reasoning but tast...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Exploring different approaches to customize language models for domain-specific text-to-code generation](http://arxiv.org/abs/2603.16526v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：5.45 | 新颖度：8.17
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have demonstrated strong capabilities in generating executable code from natural language descriptions. However, general-purpose models often struggle in specialized programming contexts wher...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Detecting Manuscripts Related to Computable Phenotypes Using a Transformer-based Language Model](https://www.biorxiv.org/content/10.64898/2026.03.12.711165v1)
  来源：bioRxiv | 日期：2026-03-16 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Objective: The demand for a comprehensive phenomics library, which requires identifying computable phenotype definitions and associated metadata from an ever-expanding biomedical literature, presents a significant, labor...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Artificial Intelligence for Automated, Highly Accurate, and Scalable Multimodal EHR Data Abstraction](https://www.medrxiv.org/content/10.64898/2026.03.16.26348522v1)
  来源：medRxiv | 日期：2026-03-17 | 相关度：7.8 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Electronic health records (EHRs) contain rich multimodal data but remain underutilized for populating clinical registries due to the time and cost of manual abstraction. We developed an AI driven pipeline to automate dat...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SeekRBP: Leveraging Sequence-Structure Integration with Reinforcement Learning for Receptor-Binding Protein Identification](http://arxiv.org/abs/2603.04748v2)
  来源：arXiv | 日期：2026-03-05 | 相关度：7.1 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Motivation: Receptor-binding proteins (RBPs) initiate viral infection and determine host specificity, serving as key targets for phage engineering and therapy. However, the identification of RBPs is complicated by their ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RNAElectra: An ELECTRA-Style RNA Foundation Model for RNA Regulatory Inference](https://www.biorxiv.org/content/10.64898/2026.03.15.711950v1)
  来源：bioRxiv | 日期：2026-03-17 | 相关度：6.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：RNA regulation governs gene expression through sequence-encoded mechanisms such as RNA structure formation, protein binding, chemical modification, and RNA-RNA targeting, with regulatory rules spanning both nucleotide-sc...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [APEX-Searcher: Augmenting LLMs' Search Capabilities through Agentic Planning and Execution](http://arxiv.org/abs/2603.13853v2)
  来源：arXiv | 日期：2026-03-14 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG), based on large language models (LLMs), serves as a vital approach to retrieving and leveraging external knowledge in various domain applications. When confronted with complex multi-h...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Identification of disease-specific alleles and gene duplications from 1,600 Haemophilus influenzae genomes using predicted protein analyses from an unsupervised language model and clinical metadata](https://www.biorxiv.org/content/10.64898/2026.03.12.711436v1)
  来源：bioRxiv | 日期：2026-03-15 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Haemophilus influenzae, a Gram-negative bacterium that is an obligate commensal of the human nasopharynx, is associated with both acute and chronic infections of the ears, adenoids, sinuses, and lungs, as well as pelvic ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [When Stability Fails: Hidden Failure Modes Of LLMS in Data-Constrained Scientific Decision-Making](http://arxiv.org/abs/2603.15840v1)
  来源：arXiv | 日期：2026-03-16 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly used as decision-support tools in data-constrained scientific workflows, where correctness and validity are critical. However, evaluation practices often emphasize stability ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AGRAG: Advanced Graph-based Retrieval-Augmented Generation for LLMs](http://arxiv.org/abs/2511.05549v2)
  来源：arXiv | 日期：2025-11-02 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Graph-based retrieval-augmented generation (Graph-based RAG) has demonstrated significant potential in enhancing Large Language Models (LLMs) with structured knowledge. However, existing methods face three critical chall...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [LLM-Augmented Changepoint Detection: A Framework for Ensemble Detection and Automated Explanation](http://arxiv.org/abs/2601.02957v2)
  来源：arXiv | 日期：2026-01-06 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：This paper introduces a novel changepoint detection framework that combines ensemble statistical methods with Large Language Models (LLMs) to enhance both detection accuracy and the interpretability of regime changes in ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [LLM-Driven Discovery of High-Entropy Catalysts via Retrieval-Augmented Generation](http://arxiv.org/abs/2603.15712v1)
  来源：arXiv | 日期：2026-03-16 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：CO2 reduction requires efficient catalysts, yet materials discovery remains bottlenecked by 10-20 year development cycles requiring deep domain expertise. This paper demonstrates how large language models can assist the ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SentGraph: Hierarchical Sentence Graph for Multi-hop Retrieval-Augmented Question Answering](http://arxiv.org/abs/2601.03014v2)
  来源：arXiv | 日期：2026-01-06 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Traditional Retrieval-Augmented Generation (RAG) effectively supports single-hop question answering with large language models but faces significant limitations in multi-hop question answering tasks, which require combin...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Novel Deep-Learning Unsupervised Domain Adaptation Method for Mitigating Batch, Strain, and Instrument Variations to Enhance Raman Spectroscopy-Based Bacterial Pathogen Identification.](https://pubmed.ncbi.nlm.nih.gov/41842761/)
  来源：PubMed | 日期：2026-03-17 | 相关度：4.4 | 新颖度：5.25
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：The escalating threat of antibiotic resistance demands a rapid and accurate pathogen identification. While Raman spectroscopy combined with deep learning supports fast detection, model robustness remains compromised by d...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [HGP-Mamba: Integrating Histology and Generated Protein Features for Mamba-based Multimodal Survival Risk Prediction](http://arxiv.org/abs/2603.16421v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：3.75 | 新颖度：7.86
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in multimodal learning have significantly improved cancer survival risk prediction. However, the joint prognostic potential of protein markers and histopathology images remains underexplored, largely due ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [CoNVict: An Agentic AI System for Copy Number Variation Prioritization in Rare Disease Diagnosis](https://www.medrxiv.org/content/10.64898/2026.03.16.26348493v1)
  来源：medRxiv | 日期：2026-03-17 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Copy number variants (CNVs) are established contributors to rare genetic disorders, yet their clinical interpretation remains challenging in diagnostic genomics. Large CNVs frequently encompass multiple functional region...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [OrgForge: A Multi-Agent Simulation Framework for Verifiable Synthetic Corporate Corpora](http://arxiv.org/abs/2603.14997v1)
  来源：arXiv | 日期：2026-03-16 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Evaluating retrieval-augmented generation (RAG) pipelines requires corpora where ground truth is knowable, temporally structured, and cross-artifact properties that real-world datasets rarely provide cleanly. Existing re...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic Exploration of Physics Models](http://arxiv.org/abs/2509.24978v5)
  来源：arXiv | 日期：2025-09-29 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：The process of scientific discovery relies on an interplay of observations, analysis, and hypothesis generation. Machine learning is increasingly being adopted to address individual aspects of this process. However, it r...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Cropping outperforms dropout as an augmentation strategy for self-supervised training of text embeddings](http://arxiv.org/abs/2508.03453v2)
  来源：arXiv | 日期：2025-08-05 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Text embeddings, i.e. vector representations of entire texts, play an important role in many NLP applications, such as retrieval-augmented generation, clustering, or visualizing collections of texts for data exploration....
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CausalEvolve: Towards Open-Ended Discovery with Causal Scratchpad](http://arxiv.org/abs/2603.14575v1)
  来源：arXiv | 日期：2026-03-15 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Evolve-based agent such as AlphaEvolve is one of the notable successes in using Large Language Models (LLMs) to build AI Scientists. These agents tackle open-ended scientific problems by iteratively improving and evolvin...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Open Biomedical Knowledge Graphs at Scale: Construction, Federation, and AI Agent Access with Samyama Graph Database](http://arxiv.org/abs/2603.15080v2)
  来源：arXiv | 日期：2026-03-16 | 相关度：3.1 | 新颖度：6.75
  匹配主题：未命中具体主题
  中文摘要：Biomedical knowledge is fragmented across siloed databases -- Reactome for pathways, STRING for protein interactions, ClinicalTrials.gov for study registries, DrugBank for drug vocabularies, DGIdb for drug-gene interacti...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Benchmarking LLM-based agents for single-cell omics analysis](http://arxiv.org/abs/2508.13201v3)
  来源：arXiv | 日期：2025-08-16 | 相关度：2.5 | 新颖度：1.5
  匹配主题：未命中具体主题
  中文摘要：单细胞组学数据的激增暴露了传统手动分析工作流的局限性。AI 智能体（Agents）通过自适应规划、可执行代码生成、可追溯决策和实时知识融合，为该领域带来了范式转变，但缺乏全面的基准测试阻碍了其发展。本研究引入了一种新型基准评估系统，旨在严格评估智能体在单细胞组学分析中的能力。该系统包含：一个兼容多种智能体框架和 LLM 的统一平台；涵盖认知程序合成、协作、执行效率、生物信息学知识整合和任务完成质量的多维指标；以及 50 个涵盖多组学、物...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Central Dogma Transformer II: An AI Microscope for Understanding Cellular Regulatory Mechanisms](http://arxiv.org/abs/2602.08751v3)
  来源：arXiv | 日期：2026-02-09 | 相关度：2.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：现有的生物 AI 模型普遍缺乏可解释性，其内部表示难以对应到可验证的生物学关系。CDT-II 提出了一种模拟“中心法则”的架构，包含 DNA 自注意力、RNA 自注意力和用于转录控制的交叉注意力模块，仅需基因组嵌入和原始单细胞表达数据即可运行。在 K562 细胞系的 CRISPRi 数据测试中，CDT-II 在 5 个完全预留基因的扰动效果预测上达到了平均相关系数 r = 0.84，并成功恢复了 GFI1B 调节网络（6.6 倍富集，P...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [IndexRAG: Bridging Facts for Cross-Document Reasoning at Index Time](http://arxiv.org/abs/2603.16415v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：2.1 | 新颖度：7.59
  匹配主题：未命中具体主题
  中文摘要：多跳问答（QA）要求跨多个文档进行推理，但现有的检索增强生成（RAG）方法通常依赖于需要额外在线处理的图方法或迭代式多步推理。本文提出 IndexRAG，一种将跨文档推理从在线推理阶段转移到离线索引阶段的新方法。IndexRAG 通过识别文档间共享的桥接实体，生成作为独立可检索单元的“桥接事实”，该过程无需额外的模型训练或微调。在 HotpotQA、2WikiMultiHopQA 和 MuSiQue 三个主流多跳问答基准测试上的实验结果...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [On Theoretically-Driven LLM Agents for Multi-Dimensional Discourse Analysis](http://arxiv.org/abs/2602.13713v2)
  来源：arXiv | 日期：2026-02-14 | 相关度：2.1 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：识别话语中重构（reformulation）的策略性用途是计算论证领域的核心挑战。虽然大语言模型（LLM）擅长检测表面相似性，但往往难以捕捉重构的语用功能（如在修辞话语中的作用）。本文提出一种比较式多智能体框架，旨在量化引入显式理论知识对该任务的增益。研究利用标注的政治辩论数据集，建立了涵盖五种重构功能的新标准：减弱（Deintensification）、增强（Intensification）、具体化（Specification）、泛化...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CARE: A Molecular-Guided Foundation Model with Adaptive Region Modeling for Whole Slide Image Analysis](http://arxiv.org/abs/2602.21637v3)
  来源：arXiv | 日期：2026-02-25 | 相关度：1.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：基础模型在计算病理学中取得了显著成功，但现有模型多依赖于非组织形态学定制的自然图像骨干网络，忽视了病理感兴趣区域（ROI）的异质性与非均匀组织结构，难以捕捉孤立切片之外的连贯组织架构。为此，研究者提出了跨模态自适应区域编码器（CARE），这是一种能自动将全扫描切片（WSI）划分为多个形态相关区域的病理基础模型。CARE 采用两阶段预训练策略：首先在 34,277 张无分割标注的 WSI 上进行自监督单模态预训练以学习形态表征；随后进入跨...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Programming Biomolecular Interactions with All-Atom Generative Model](https://www.biorxiv.org/content/10.64898/2026.03.12.711044v1)
  来源：bioRxiv | 日期：2026-03-15 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：生物分子相互作用是细胞生命的核心，涵盖从小分子到核酸和蛋白质的多种模态。尽管分子识别遵循共同的物理化学原理，但目前的分子设计策略在不同模态间仍是分离的。本文提出了 AnewOmni，这是一个在超过 500 万个生物分子复合物上训练的统一生成框架，通过在原子分辨率下组装具有化学意义的构建块，实现了跨尺度的可迁移分子设计。研究引入了可编程图提示（graph prompts），支持用户定义的化学、拓扑和几何引导，以探索非常规化学结构。通过捕获...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HindSight: Evaluating LLM-Generated Research Ideas via Future Impact](http://arxiv.org/abs/2603.15164v2)
  来源：arXiv | 日期：2026-03-16 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：评估 AI 生成的科研想法通常依赖于 LLM 评委或专家小组，这具有主观性且与实际研究影响力脱节。本研究引入了 HindSight，这是一种基于时间分割的评估框架，通过将生成的想法与真实的未来出版物进行匹配，并根据引用影响力和发表平台水平进行评分，从而衡量想法的质量。该框架设定一个时间截止点 T，限制生成系统仅能访问 T 之前的文献，随后将其输出与 T 之后 30 个月内发表的论文进行对比。在 10 个 AI/ML 研究主题上的实验揭示...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Selective Memory for Artificial Intelligence: Write-Time Gating with Hierarchical Archiving](http://arxiv.org/abs/2603.15994v1)
  来源：arXiv | 日期：2026-03-16 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）通常无差别地存储所有内容，导致噪声积累并降低准确性；而参数化方法将知识压缩进权重，无法进行选择性更新。本研究借鉴生物记忆机制，提出“写入时门控”（write-time gating）技术，利用综合显著性评分（来源声誉、新颖性、可靠性）过滤输入的知识对象，并维护版本链以保留历史状态。在无标注标签的真实大模型评估中，写入门控实现了 100% 的准确率，而未门控存储仅为 13%。实验发现，在 8:1 的干扰项比例下，读取...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The Active Discoverer Framework: Towards Autonomous Physics Reasoning through Neuro-Symbolic LaTeX Synthesis](http://arxiv.org/abs/2601.06117v3)
  来源：arXiv | 日期：2026-01-03 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：现代人工智能在统计插值方面表现出色，但在理论物理和数学所需的精确推理上存在根本缺陷。本文识别了“浮点墙”（Float Wall）现象，即由于标准浮点表示和BPE分词导致神经外推在超过 10^16 量级时发生灾难性崩溃。为解决此问题，我们提出了 Active Discoverer 框架，这是一种专为不变性发现设计的数字原生神经符号架构。其核心是 NumberNet，一种采用最低有效位（LSB）序列编码的孪生算术 Transformer，实...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [The Impact of Ideological Discourses in RAG: A Case Study with COVID-19 Treatments](http://arxiv.org/abs/2603.14838v1)
  来源：arXiv | 日期：2026-03-16 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：This paper studies the impact of retrieved ideological texts on the outputs of large language models (LLMs). While interest in understanding ideology in LLMs has recently increased, little attention has been given to thi...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Exposing Blindspots: Cultural Bias Evaluation in Generative Image Models](http://arxiv.org/abs/2510.20042v2)
  来源：arXiv | 日期：2025-10-22 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：生成式图像模型在产生视觉效果的同时常误导文化表征。本研究针对以往研究多集中于文本到图像（T2I）系统而忽视图像到图像（I2I）编辑的现状，构建了一个涵盖6个国家、8个大类及36个子类模式的统一评估框架。研究采用时代感知提示词，在标准化协议下对开源模型的T2I生成和I2I编辑进行跨国家、跨时代和跨类别的审计。评估方法结合了标准自动指标、文化感知检索增强视觉问答（RAG-VQA）以及母语专家的视觉评判。研究发现：在国家无关提示下，模型默认呈...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Grounding World Simulation Models in a Real-World Metropolis](http://arxiv.org/abs/2603.15583v1)
  来源：arXiv | 日期：2026-03-16 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：本文提出了首尔世界模型（SWM），这是一种锚定于真实城市环境的城市级世界模拟模型。与以往合成虚构环境的生成式世界模型不同，SWM 通过检索增强调节（retrieval-augmented conditioning）邻近街景图像，实现了自回归视频生成。针对检索参考图与动态目标场景间的时间错位、轨迹多样性受限以及车载采集数据稀疏等挑战，研究团队采用了跨时空配对、大规模合成数据集以及视图插值流水线，从稀疏街景中合成连贯的训练视频。此外，引入“...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [ES-Merging: Biological MLLM Merging via Embedding Space Signals](http://arxiv.org/abs/2603.14405v1)
  来源：arXiv | 日期：2026-03-15 | 相关度：6.1 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Biological multimodal large language models (MLLMs) have emerged as powerful foundation models for scientific discovery. However, existing models are specialized to a single modality, limiting their ability to solve inhe...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Unlocking Enzyme Discovery: A High-Resolution Gene Cluster Database Powered by Phylogenetic Insights and Machine Learning.](https://pubmed.ncbi.nlm.nih.gov/41837859/)
  来源：PubMed | 日期：2026-03-16 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：High-throughput sequencing has generated vast genomic repositories that remain under-annotated, hampering enzyme discovery. We present an integrated pipeline that (i) builds a high-resolution, cross-kingdom phylogenetic ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RAG-3DSG: Enhancing 3D Scene Graphs with Re-Shot Guided Retrieval-Augmented Generation](http://arxiv.org/abs/2601.10168v2)
  来源：arXiv | 日期：2026-01-15 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Open-vocabulary 3D Scene Graph (3DSG) can enhance various downstream tasks in robotics by leveraging structured semantic representations, yet current 3DSG construction methods suffer from semantic inconsistencies caused ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [QiboAgent: a practitioner's guideline to open source assistants for Quantum Computing code development](http://arxiv.org/abs/2603.15538v1)
  来源：arXiv | 日期：2026-03-16 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：We introduce QiboAgent, a reference implementation designed to serve as a practitioner's guideline for developing specialized coding assistants in Quantum Computing middleware. Addressing the limitations in scientific so...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Using image classifiers to predict CMT2A disease-relevant mitochondrial motility phenotypes in iPSC motor neurons](https://www.biorxiv.org/content/10.64898/2026.03.16.712192v1)
  来源：bioRxiv | 日期：2026-03-17 | 相关度：2.65 | 新颖度：5.75
  匹配主题：sequencing_bioinformatics
  中文摘要：Charcot-Marie-Tooth disease type 2A (CMT2A) is a genetic disease characterized by autosomal dominant MFN2 mutations and dysregulated mitochondrial trafficking. While there is currently no FDA-approved CMT2A therapy, the ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Open-Source Reproduction and Explainability Analysis of Corrective Retrieval Augmented Generation](http://arxiv.org/abs/2603.16169v1)
  来源：arXiv | 日期：2026-03-17 | 相关度：1.4 | 新颖度：5.97
  匹配主题：未命中具体主题
  中文摘要：纠正性检索增强生成（CRAG）通过评估检索文档质量并触发纠正措施，显著提升了 RAG 系统的鲁棒性。然而，原始 CRAG 实现依赖 Google Search API 和闭源模型权重，限制了学术复现与私有化部署。本研究展示了 CRAG 的完全开源复现方案，将专有 Web 搜索替换为 Wikipedia API，并将原 LLaMA-2 生成器替换为 Phi-3-mini-4k-instruct。我们在 PopQA 和 ARC-Challe...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GlobalRAG: Enhancing Global Reasoning in Multi-hop Question Answering via Reinforcement Learning](http://arxiv.org/abs/2510.20548v4)
  来源：arXiv | 日期：2025-10-23 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：强化学习（RL）在改进检索增强生成（RAG）方面展现了潜力，但在多跳问答（QA）中仍受限于缺乏全局规划和执行不忠实（阻碍了查询构建和证据的一致性使用）。本文提出 GlobalRAG，一个旨在增强多跳问答全局推理能力的强化学习框架。GlobalRAG 将复杂问题分解为子目标，协调检索与推理过程，并迭代优化证据。为了引导这一过程，研究者引入了“规划质量奖励”和“子目标完成奖励”，以鼓励连贯的规划和可靠的子目标执行。此外，该框架采用渐进式权重...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [A Comprehensive Benchmark of Histopathology Foundation Models for Kidney Histopathology](http://arxiv.org/abs/2603.15967v1)
  来源：arXiv | 日期：2026-03-16 | 相关度：3.05 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Histopathology foundation models (HFMs), pretrained on large-scale cancer datasets, have advanced computational pathology. However, their applicability to non-cancerous chronic kidney disease remains underexplored, despi...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
