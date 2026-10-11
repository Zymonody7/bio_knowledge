# 每日论文监控日报 (2026-10-11)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 29 篇新论文。

## 抓取状态

- arXiv：成功，命中 18 篇
- PubMed：成功，命中 35 篇
- bioRxiv：成功，命中 10 篇
- medRxiv：成功，命中 5 篇

## 最值得看

### 产品应用 / 监测落地

- [Cross-cohort Mamography]{Representation-dependent domain adaptation for cross-cohort generalization of mammography diagnostic models](https://www.biorxiv.org/content/10.64898/2026.10.01.756041v1)
  来源：bioRxiv | 日期：2026-10-08 | 相关度：7.15 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Background: Artificial intelligence (AI) models for mammography can achieve high diagnostic performance when training and test data originate from similar populations and imaging environments, but performance often deter...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 可追踪

### Foundation Model / Agent

- [Multilingual Disparities in Large Language Model-Based Symptom Detection for Global Disease Surveillance: Evaluation Study.](https://pubmed.ncbi.nlm.nih.gov/42854221/)
  来源：PubMed | 日期：2026-10-09 | 相关度：8.15 | 新颖度：1.25
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：Symptom detection is essential in global disease surveillance to detect potential outbreaks, as symptoms are the first observable signs of infection. To reflect real-time ground truth conditions during pandemics, social ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Security Meta-Model for Retrieval-Augmented Generation Systems](http://arxiv.org/abs/2610.11893v1)
  来源：arXiv | 日期：2026-10-08 | 相关度：7.5 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) systems extend large language models (LLMs) with external knowledge through a multi-stage pipeline. While this architecture can improve the factual grounding of generated answers, it ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Large Language Models for Structured Information Extraction from German Histopathology Reports - Hepatocellular Carcinoma](https://www.medrxiv.org/content/10.64898/2026.10.07.26364402v1)
  来源：medRxiv | 日期：2026-10-08 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Background: Clinical registries and institutional quality control (QC) in pathology heavily depend on complex histopathological data. However, critical tumor characteristics are mostly locked in unstructured free-text re...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Large language model consensus for reliable research cohort construction from radiology reports: a retrospective cohort study](https://www.medrxiv.org/content/10.64898/2026.10.06.26364312v1)
  来源：medRxiv | 日期：2026-10-08 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Background Large-scale retrospective studies often require researchers to adjudicate outcomes or cohort eligibility from unstructured clinical records. Manual review can provide reliable labels but is difficult to scale....
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Forms of LLM-Integrated Applications from LLM-Chats to Autonomous AI Agent System](http://arxiv.org/abs/2610.11899v1)
  来源：arXiv | 日期：2026-10-08 | 相关度：6.55 | 新颖度：1.2
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly embedded as components in software systems, marketed under labels such as chatbot, copilot, retrieval-augmented generation, workflow, coding agent and AI agent. Whether these...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DiverScan: attention-guided exploratory analysis of animal behaviour across diverse comparative experiments](https://www.biorxiv.org/content/10.64898/2026.10.01.755818v1)
  来源：bioRxiv | 日期：2026-10-08 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：High-throughput tracking yields rich time-series data of animal behaviour, yet extracting biological insight remains a bottleneck, even for simple control--treatment comparisons. Existing analyses struggle to pinpoint th...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [VINTER: a generative vision-language model for annotating and interrogating spatial tissues](https://www.biorxiv.org/content/10.64898/2026.10.01.752251v1)
  来源：bioRxiv | 日期：2026-10-08 | 相关度：7.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Spatial transcriptomics links gene expression to tissue structure, yet current models learn embeddings whose meaning is assigned afterwards or read histology without measured expression. Tissue decisions are therefore ra...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Protein large language model-assisted one-to-one gene homology mapping in cross-species single-cell transcriptome integration.](https://pubmed.ncbi.nlm.nih.gov/42855280/)
  来源：PubMed | 日期：2026-10-09 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Cross-species integration of single-cell transcriptomes requires establishing gene correspondences to enable comparative analysis of expression profiles across organisms. Current approaches predominantly rely on Ensembl ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SpatialOmicsLab: an integrated research environment for AI co-scientists in spatial transcriptomics](https://www.biorxiv.org/content/10.64898/2026.10.01.756049v1)
  来源：bioRxiv | 日期：2026-10-08 | 相关度：5.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Spatial profiling is moving from method development into a central platform for biological discovery and clinical translation, but analyzing such complex data has become the bottleneck of scientific discovery. Translatin...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Position-wise Fold-Switch Prediction in Metamorphic Proteins: A Comparison of Handcrafted and Language Model Features](https://www.biorxiv.org/content/10.64898/2026.09.30.755750v1)
  来源：bioRxiv | 日期：2026-10-08 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：In this work, we focus on predicting fold-switching phenomena observed in certain protein structures. Proteins that undergo fold-switching are called metamorphic proteins. We model fold-switch prediction in proteins as a...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [LM-X: Explainable Vision--Language--Action Modeling via Progress, Event, and Uncertainty Prediction](http://arxiv.org/abs/2608.25757v5)
  来源：arXiv | 日期：2026-08-26 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large-scale vision--language--action (VLA) policies have advanced generalist robot control, yet most remain stimulus-to-action black boxes: actions are exposed, but their explanatory state is not. They provide no native ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond Sequences: Distilling Structured Decision Memory for LLM Recommendation](http://arxiv.org/abs/2610.11501v1)
  来源：arXiv | 日期：2026-10-08 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Despite the adoption of large language models (LLMs) in recommendation systems, prevailing approaches mostly model single-type behaviors (e.g., views or purchases). Even when incorporating multiple behaviors, existing me...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Personalization Matters: Long-Horizon Conversation Agent with User-Centric Information in Online Shopping Interactions](http://arxiv.org/abs/2610.11375v1)
  来源：arXiv | 日期：2026-10-08 | 相关度：3.45 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Personalized conversational shopping requires maintaining preference consistency over multi-turn interactions, where users reveal constraints gradually. Existing approaches often rely on static profiles and do not explic...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Zatom-2: Multitask Pretraining on Atomistic Data for Generative Modeling across Domains](http://arxiv.org/abs/2610.11454v1)
  来源：arXiv | 日期：2026-10-08 | 相关度：3.1 | 新颖度：1.75
  匹配主题：未命中具体主题
  中文摘要：Unified atomistic modeling has the potential to accelerate discovery in chemistry, materials science, and biology by bridging data-rich chemical domains and data-scarce biological contexts. However, existing generative a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ORCAGen: Orchestrating Context-Aware Malware Deception with RAG-Guided Generative AI](http://arxiv.org/abs/2610.12415v1)
  来源：arXiv | 日期：2026-10-08 | 相关度：2.5 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Malware defenses often remove or isolate suspicious programs as quickly as possible. While effective for containment, this approach can also waste an opportunity to observe attacker behavior and deploy targeted counterme...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators](http://arxiv.org/abs/2606.26294v3)
  来源：arXiv | 日期：2026-06-24 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Self-improving agents are state-of-the-art on agentic coding benchmarks, yet their search methods assume a stationary evaluation criterion. This ignores a central feature of evolution: species adapt as their environments...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Event-Centric Memory with Query-Aware Graph Augmentation for Long-Term Conversational Agents](http://arxiv.org/abs/2610.11920v1)
  来源：arXiv | 日期：2026-10-08 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：For persistent and personalized conversational agents, memory systems can enable them to remember, update, and reason over long histories by storing past interactions and retrieving relevant information. Existing memory ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [MAP4CS: A Multi-dimensional Data Pruning Framework for Efficient Code Retriever Fine-tuning](http://arxiv.org/abs/2610.11727v1)
  来源：arXiv | 日期：2026-10-08 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) has become a cornerstone in software engineering for enhancing Large Language Models (LLMs) with domain-specific knowledge. However, adapting retrievers to evolving code repositories ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Quantifying performance inflation from hidden sample dependence in biomedical image classification benchmarks](https://www.biorxiv.org/content/10.64898/2026.10.01.755883v1)
  来源：bioRxiv | 日期：2026-10-08 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Machine learning benchmarks often treat image files as independent observations, although multiple files may represent repeated views or other related samples. Prior work has shown that non-independent partitioning can i...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [The structural context of mutations in proteins predicts their effect on antibiotic resistance.](https://pubmed.ncbi.nlm.nih.gov/42852653/)
  来源：PubMed | 日期：2026-10-09 | 相关度：5.55 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：In Mycobacterium tuberculosis , a prevalent and deadly pathogen, resistance to antibiotics evolves primarily through non-synonymous mutations in proteins. Sequence-based analyses can uncover the genetic basis of antibiot...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Validated Semantic Scoring Improves Filtering of Generic Concepts from Knowledge-Graphs for Drug Repurposing Queries](https://www.biorxiv.org/content/10.64898/2026.09.29.755063v2)
  来源：bioRxiv | 日期：2026-10-08 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：When an ontology-based biomedical knowledge graph (a KG, containing information about genes, pathways, phenotypes, and molecular interactions) is analyzed using a computational reasoning system, the system can return unw...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Advancing genetic pathogenicity prediction with three-dimensional proteoform-phenotype analysis](https://www.medrxiv.org/content/10.64898/2026.10.07.26364649v1)
  来源：medRxiv | 日期：2026-10-09 | 相关度：3.65 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Ascertaining the pathogenicity and clinical relevance of genetic mutations is a longstanding challenge across human disease. This is particularly relevant for genes with many variants of unknown significance (VUS), such ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Retrieval-Augmented Generation for Predicting Cellular Responses to Gene Perturbation](http://arxiv.org/abs/2603.07233v2)
  来源：arXiv | 日期：2026-03-07 | 相关度：2.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Predicting transcriptional responses to genetic perturbations is fundamental to functional genomics and therapeutic discovery. Recent deep learning models have shown promise in single-cell perturbation response predictio...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [A Zero-Shot Decision Model (Jev) Matches a Trained Classifier but Ranks Its Own Errors Worse: Calibrated, Split-Conformal Next-Procedure Recommendation in General Dentistry](https://www.medrxiv.org/content/10.64898/2026.05.07.26352635v5)
  来源：medRxiv | 日期：2026-10-10 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：2026年的商业牙科AI主要集中在影像学诊断（如龋齿、牙槽骨检测），但针对“下一步该做什么”的临床决策支持仍是难题。本研究推出DentaCoPilot，这是一款基于结构化病历推荐后续操作的系统。该系统可输出当前牙科术语（CDT）代码的Top-K概率分布、置信度标签、在信息不足时的弃权标志以及基于病历的解释理由。研究对比了4种传统基准（如XGBoost、CNN-RNN）与6种大语言模型（LLM）变体（如Claude Sonnet/Opus...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [CoPoE: Multimodal Fusion via Decomposable Disease-Coordinate Product-of-Experts for Missing-Modality Alzheimer's Diagnosis](http://arxiv.org/abs/2610.11394v1)
  来源：arXiv | 日期：2026-10-08 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Multimodal Alzheimer's disease (AD) diagnosis benefits from integrating heterogeneous clinical, imaging, genomic, and biomarker evidence, but clinical cohorts frequently suffer from irregular modality missingness. Existi...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [GLM-RAG: Graph Language Models for Graph-Based Retrieval-Augmented Generation](http://arxiv.org/abs/2607.28397v2)
  来源：arXiv | 日期：2026-07-30 | 相关度：4.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) over knowledge graphs requires retrievers that can effectively capture both graph structure and semantic information. Recent approaches have explored graph neural network (GNN)-based ...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [Is Memorization Context-Sensitive? Prefix-Based Extraction Beyond Isolated Prefixes](http://arxiv.org/abs/2610.12085v1)
  来源：arXiv | 日期：2026-10-08 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) can expose memorized training sequences under prefix-based extraction: given a prefix from a training example, the model may assign high probability to the original continuation. In deployed ...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [The Geometry of Hierarchical Navigation: Accuracy and Query Cost for Point Process Input](http://arxiv.org/abs/2610.12312v1)
  来源：arXiv | 日期：2026-10-08 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Large-scale information retrieval systems, including retrieval-augmented generation (RAG) and recommendation engines, widely use multi-layered hierarchical data structures for ultra-fast approximate nearest-neighbor sear...
  为什么值得看：The Geometry of Hierarchical Navigation: 与你的主题有弱匹配，暂时保留作低优先级跟踪。
