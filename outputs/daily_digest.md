# 每日论文监控日报 (2026-08-02)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 39 篇新论文。

## 抓取状态

- arXiv：成功，命中 12 篇
- PubMed：成功，命中 184 篇
- bioRxiv：成功，命中 13 篇
- medRxiv：成功，命中 8 篇

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [Agentic-TimesFM-AKI: A Dual LLM-Time Series Framework for Predicting Drug-Induced Acute Kidney Injury with Privacy-Preserving Synthetic Data](https://www.medrxiv.org/content/10.64898/2026.07.30.26359271v1)
  来源：medRxiv | 日期：2026-07-31 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Background: Acute kidney injury (AKI) is a severe complication in intensive care units, frequently exacerbated by synergistic nephrotoxicity from drugs such as Vancomycin and Piperacillin-Tazobactam. Traditional alert sy...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [General-purpose language models integrate structured biological evidence for explainable biological interaction prediction](https://www.biorxiv.org/content/10.64898/2026.06.10.727770v2)
  来源：bioRxiv | 日期：2026-07-30 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Biological interaction inference often requires integrating heterogeneous evidence that differs in biological meaning, provenance, specificity, and reliability. Existing computational approaches typically compress such e...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Growth factor thermostability dataset derived from experimental and computational approaches to accelerate cultured meat development.](https://pubmed.ncbi.nlm.nih.gov/42422031/)
  来源：PubMed | 日期：2026-08-01 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：This project compiled experimentally measured and computationally predicted thermostability data for growth factors (GFs) commonly used in cultured meat and seafood (CM) production. Data were generated on recombinant GFs...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Sparse autoencoders reveal interpretable cell-type programs in single-cell foundation model representations.](https://pubmed.ncbi.nlm.nih.gov/42155660/)
  来源：PubMed | 日期：2026-08-01 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Single-cell foundation models such as scGPT learn rich representations of cellular identity, yet the biological programs encoded in their internal activations remain opaque. We investigate whether sparse autoencoders (SA...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Accelerating inference in genomic and proteomic foundation models via speculative decoding.](https://pubmed.ncbi.nlm.nih.gov/42536416/)
  来源：PubMed | 日期：2026-07-31 | 相关度：7.1 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Genomic and protein foundation models (GFMs and PFMs) have demonstrated strong performance in learning the language of DNA and proteins, but their use in large-scale sequence generation is limited by the latency of autor...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OSCAgent: Accelerating the Discovery of Organic Solar Cells with LLM Agents](http://arxiv.org/abs/2602.04510v2)
  来源：arXiv | 日期：2026-02-04 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Organic solar cells (OSCs) hold great promise for sustainable energy, but discovering high-performance materials is time-consuming and costly. Existing molecular generation methods can aid the design of OSC molecules, bu...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Keyphrase Identification Using Minimal Labeled Data with Hierarchical Contexts and Transfer Learning](https://www.medrxiv.org/content/10.1101/2023.01.26.23285060v4)
  来源：medRxiv | 日期：2026-07-30 | 相关度：6.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Background: Interoperable clinical decision support system (CDSS) rules provide a pathway to interoperability, a well-recognized challenge in health information technology. Building an ontology facilitates creating inter...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [LLM-powered Functional Gene Set Summarization with genesetGPT](https://www.biorxiv.org/content/10.64898/2026.07.27.741117v1)
  来源：bioRxiv | 日期：2026-07-30 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Transcriptomics datasets generated using next-generation sequencing techniques such as single cell RNA-sequencing (scRNA-seq) and spatially-resolved transcriptomics (SRT) allow researchers to study patterns in gene expre...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Illuminating the Ligandable Proteome with AI Protein Profiling](https://www.biorxiv.org/content/10.1101/2025.09.07.670677v3)
  来源：bioRxiv | 日期：2026-07-30 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Most human proteins lack chemical probes or pharmaceutical modulators, leaving much of the proteome unexplored. Activity-based protein profiling has enabled proteome-scale discovery of protein-ligand interactions and cov...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Zero-shot document-level biomedical relation extraction via scenario-based prompt design in two-stage with LLM.](https://pubmed.ncbi.nlm.nih.gov/41762612/)
  来源：PubMed | 日期：2026-08-01 | 相关度：6.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Document-level biomedical relation extraction is a crucial task due to the complex interactions among multiple entities distributed across lengthy scientific texts. Traditional supervised methods are constrained by their...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Artificial intelligence in clinical metagenomic pathogen detection: A critical review of pipeline integrations, challenges, and future directions.](https://pubmed.ncbi.nlm.nih.gov/42289215/)
  来源：PubMed | 日期：2026-08-01 | 相关度：8.25 | 新颖度：1.75
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：Metagenomic next-generation sequencing (mNGS) has expanded the scope of clinical diagnostics by enabling culture-independent detection of microorganisms in patient samples. However, mNGS clinical utility remains constrai...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [A Neuro-Symbolic Knowledge Graph and Large Language Model Hybrid Architecture for Multi-Modality Mental Health Counseling](https://www.medrxiv.org/content/10.64898/2026.07.29.26359268v1)
  来源：medRxiv | 日期：2026-07-31 | 相关度：7.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Background: Depression and anxiety are managed largely between clinical visits, yet outpatient care lacks scalable, accountable mechanisms for between-visit support. Large language models converse fluently but fuse clini...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Large language models enable consensus-level interpretation in metagenomic diagnostics](https://www.medrxiv.org/content/10.64898/2026.07.29.26358751v1)
  来源：medRxiv | 日期：2026-07-31 | 相关度：7.4 | 新颖度：1.5
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Abstract Metagenomic sequencing can detect a broad range of pathogens, but interpreting which detections are clinically relevant requires expert adjudication that is difficult to scale and standardize. Here we present di...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Applications of Machine Learning, Natural Language Processing, and Generative Artificial Intelligence in Dermatology Education and Research: A Scoping Review.](https://pubmed.ncbi.nlm.nih.gov/41981908/)
  来源：PubMed | 日期：2026-08-01 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence (AI) is being increasingly used in dermatology education and research as digital health data expands and large language models (LLMs) advance. This scoping review synthesized current applications,...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [MemHarness: Memory Is Reconstructed, Not Replayed](http://arxiv.org/abs/2607.28272v1)
  来源：arXiv | 日期：2026-07-30 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieving past experiences has become a common strategy to enhance large language model agents. However, most existing memory-augmented agents treat retrieved experiences as static records to be replayed verbatim, injec...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OptGraph: Large Language Models Enhanced Evolutionary Optimization Via Graph Retrieval-Augmented Generation](http://arxiv.org/abs/2607.27918v1)
  来源：arXiv | 日期：2026-07-30 | 相关度：4.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have emerged as a powerful tool for automated evolutionary optimization, but existing methods remain limited in pattern reuse, error-aware refinement, and retrieval robustness across diverse ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DualG-MRAG: Decoupling Macro-Reasoning and Micro-Matching for Multimodal Retrieval-Augmented Generation](http://arxiv.org/abs/2607.28580v1)
  来源：arXiv | 日期：2026-07-30 | 相关度：3.45 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：While Multimodal Retrieval-Augmented Generation (MM-RAG) has shown promising results, it still struggles with complex multi-hop reasoning tasks. Existing methods primarily focus on independent instance-level matching, wh...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Interpretable deep learning model of circulating genomics for quantitative survival prediction in advanced non-small cell lung cancer.](https://pubmed.ncbi.nlm.nih.gov/41649698/)
  来源：PubMed | 日期：2026-08-01 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Accurate quantitative survival prediction in advanced non-small cell lung cancer (NSCLC) remains an unmet clinical need. While liquid biopsy is widely used, single circulating tumor DNA (ctDNA) shows limited predictive p...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BM25 Wins at Scale: A Scaling Study of Retrieval-Augmented Generation Paradigms](http://arxiv.org/abs/2607.26497v2)
  来源：arXiv | 日期：2026-07-29 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）涵盖了词法检索、稠密检索、基于图的索引及智能体搜索等多种范式，但这些范式通常在单一语料规模的基准上进行评估，导致其准确性与成本随规模扩展的规律尚不明确。本研究通过 28 个严格嵌套的层级（语料规模跨度约 450 倍）开展受控实验，在保持问题集和核心相关文档不变的前提下，评估了不同范式的准确率、构建与查询 Token 消耗及延迟。结果显示，RAG 性能表现出随规模变化的交叉现象：在极小规模语料下，文件系统智能体表现最...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MEDIAREF: A Public Knowledge Store for Media Background Checks](http://arxiv.org/abs/2607.02383v3)
  来源：arXiv | 日期：2026-07-02 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：基于大语言模型（LLM）的检索增强生成（RAG）正广泛应用于自动事实核查（AFC）及相关任务。RAG系统通过检索证据为输出提供透明依据，并允许独立于底层模型更新外部信息。然而，现有方法通常假设检索到的证据是可靠的，而现实世界的信息可能存在冲突、过时或源自不可靠及有偏见的渠道。针对这一挑战，近期研究提出了“来源批判性推理”，通过媒体背景调查（MBCs）评估证据来源的可信度，以支持下游的事实验证。但生成MBCs往往依赖昂贵的专有搜索API，...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Negative controls reveal volume-driven confounding in radiomics and imaging foundation model features](http://arxiv.org/abs/2607.28423v1)
  来源：arXiv | 日期：2026-07-30 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：影像组学和影像基础模型有望提供肿瘤生物学的非侵入性生物标志物，但其预测特征可能仅反映肿瘤体积或采集伪影，而非有意义的图像空间结构。本研究推出了开源框架 READII-2-ROQC，利用保持体积的阴性对照来评估影像组学和深度影像特征是否捕捉到了独立的空间信号。该框架通过可配置的随机化策略，在肿瘤、背景和全图区域生成体素扰动图像，并对比原始图像与对照图像的特征行为及模型性能。研究人员将该框架应用于三个公共癌症影像队列，处理了 3,552 个...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RRM: Experience-Driven Reflective Retrieval Memory for Long-Horizon Multimodal Reasoning](http://arxiv.org/abs/2607.28156v1)
  来源：arXiv | 日期：2026-07-30 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：现有的多模态长期记忆智能体主要利用外部存储来克服长视频的上下文限制，但大多侧重于“存储什么”而非“如何检索”。当检索不准确或反复失败时，现有智能体缺乏从既往任务轨迹中诊断失败并调整未来搜索策略的机制。本文提出反思性检索记忆（RRM）框架，用于长程多模态推理。RRM 在以实体为中心的多模态记忆图基础上，增加了反思性经验记忆，旨在从历史任务轨迹中提取可迁移的程序化检索知识。与保存当前视频事实证据的片段或语义记忆不同，反思性经验记忆捕捉的是跨...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [ChatIBD: design, safeguards, and early international use of a guideline-grounded generative AI tool for inflammatory bowel disease (IBD) professionals](https://www.medrxiv.org/content/10.64898/2026.05.06.26352526v2)
  来源：medRxiv | 日期：2026-07-30 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：本研究描述了ChatIBD的设计、运行保障及早期使用情况。ChatIBD是一个专为炎症性肠病（IBD）专业人士设计的生成式AI平台。该平台采用检索增强生成（RAG）技术，基于精选的IBD指南语料库进行问答。技术实现上，系统结合了混合语义与关键词检索、查询扩展及重排序，并强制模型仅依据检索到的材料回答并返回引用链接。安全保障措施包括集成欧洲药品管理局（EMA）的固定药物剂量信息、用户反馈捕获以及临床医生对标记输出的审查。在2025年10月...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [VESTIGE: A Knowledge-Guided Masking Strategy for Corruption-Aware Fine-Tuning of Genomic Transformers, Validated on Ancient DNA Reconstruction](http://arxiv.org/abs/2607.27712v1)
  来源：arXiv | 日期：2026-07-30 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Standard masked-language-model fine-tuning applies a uniform masking probability across every token position, assuming reconstruction difficulty is position-agnostic. When the degradation process is characterised and con...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [ConMem: Contribution-Aware Memory for Long-Horizon Manufacturing Inspection Logs](http://arxiv.org/abs/2607.28126v1)
  来源：arXiv | 日期：2026-07-30 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：针对长周期钢铁设备检查中异构记录推理的挑战，现有检索增强生成（RAG）系统将历史日志视为静态语料库，且未评估记录的诊断价值，导致无法及时报告早期风险。为此，本文提出 ConMem，一种面向 LLM 辅助设备检查的贡献感知记忆框架，支持人机协同的早期风险筛查。ConMem 首先将检查日志分割为功能性证据单元，随后通过 Shapley 风格的估计方法评估每个记忆单元对下游诊断的贡献，并在有限内存预算下保留高价值证据。实验结果显示，ConMe...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Cross-Attention Over RNA And Protein Sequences Enables Generalizable Interaction Prediction](https://www.biorxiv.org/content/10.64898/2026.04.22.720174v2)
  来源：bioRxiv | 日期：2026-07-31 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Computational predictions are essential to characterize the RNA-protein interaction landscape, yet a persistent gap between benchmark performance and practical utility suggests that current models have limited generaliza...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Artificial Intelligence in Food-Nutrition-Health Research: From Multimodal Data Integration to Precision Intervention.](https://pubmed.ncbi.nlm.nih.gov/42535509/)
  来源：PubMed | 日期：2026-08-01 | 相关度：4.5 | 新颖度：1.0
  匹配主题：foundation_model_agent, application_monitoring
  中文摘要：Artificial intelligence (AI) is transforming food-nutrition-health research by enabling pattern recognition in complex, high-dimensional datasets that traditional hypothesis-driven approaches cannot address. This review ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Deep learning-enabled ratiometric signal transduction for portable and intelligent colorimetric LAMP biosensing of Vibrio vulnificus.](https://pubmed.ncbi.nlm.nih.gov/42031193/)
  来源：PubMed | 日期：2026-08-01 | 相关度：2.65 | 新颖度：0.25
  匹配主题：sequencing_bioinformatics
  中文摘要：Vibrio vulnificus is a highly lethal zoonotic pathogen associated with seafood consumption and aquaculture environments, demanding rapid and reliable on-site molecular diagnostics. Here, we report an intelligent biosensi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CREB gene regulation as a blood biomarker of neural sensitivity to social threat.](https://pubmed.ncbi.nlm.nih.gov/41905489/)
  来源：PubMed | 日期：2026-08-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：社会威胁会增强炎症反应并增加相关疾病风险，识别对社会威胁具有高度神经敏感性的个体对制定预防协议至关重要。本研究探讨了外周血中cAMP反应元件结合蛋白（CREB）转录因子活性是否可作为中枢神经系统（CNS）对社会威胁敏感性的生物标志物。研究利用一项随机对照试验的基线数据（n=44，平均年龄19.4岁），结合功能磁共振成像（fMRI）与外周血采样。通过基于TELiS启动子的生物信息学方法评估CREB基因调节活性，并利用改良蒙特利尔成像压力测...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Toward Bridging the Gap from Artificial Intelligence in Clinical Research to Clinical Practice in Rheumatology: The Mayo Experience.](https://pubmed.ncbi.nlm.nih.gov/42409435/)
  来源：PubMed | 日期：2026-08-01 | 相关度：4.85 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：This article highlights Mayo Clinic's pioneering efforts to integrate artificial intelligence (AI) and machine learning into rheumatology, focusing on genomics, imaging, pathology, and clinical data science to improve di...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [From signal to action: integrating emerging technologies into mosquito-borne disease control.](https://pubmed.ncbi.nlm.nih.gov/42532764/)
  来源：PubMed | 日期：2026-07-30 | 相关度：3.65 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Mosquito-borne disease control is increasingly challenged by transmission patterns that evade established tools. This review examines emerging technologies across the surveillance-to-intervention pathway. Smart traps, AI...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial Intelligence in Clinical Genetics: Current Applications and Challenges.](https://pubmed.ncbi.nlm.nih.gov/42443618/)
  来源：PubMed | 日期：2026-08-01 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：多组学、二代测序（NGS）和长读长测序技术已深刻改变医学遗传学实践。由于每位患者涉及数万至数百万个变异及复杂的生化模式，复杂病例的解读往往需要耗费大量人力。海量数据集的出现使传统分析方法难以为继。人工智能（AI）为处理临床遗传学中日益增长的基因组与表型数据提供了高效手段，目前已应用于变异优先排序与解读、罕见病筛查及精准医学等领域。然而，受限于特定人群代表性不足、伦理争议及数据治理等问题，这些技术向常规临床转化的过程依然困难。目前大多数 ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Bridging Trials and Real Life in Fixed-Duration BTKi-Venetoclax for CLL: A Delphi-Enhanced Synthesis Incorporating Artificial Intelligence (AI) Benchmarks.](https://pubmed.ncbi.nlm.nih.gov/41974594/)
  来源：PubMed | 日期：2026-08-01 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：针对慢性淋巴细胞白血病（CLL）中固定疗程（FD）BTK抑制剂（BTKi）联合维奈克拉方案的患者选择，本研究旨在弥合临床试验与真实世界实践的差距。研究采用改进的德尔菲法，由意大利坎帕尼亚地区的9名血液学家参与，重点评估了合并症、基因组学（TP53/del(17p)、IGHV状态、复杂核型）及物流因素（照护支持、就医距离、给药能力）对一线治疗决策的影响。基于2014-2025年的系统综述制定了12项陈述，共识标准设定为≥75%一致性。结果...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Nursing roles, competencies, and education in precision oncology: a scoping review.](https://pubmed.ncbi.nlm.nih.gov/42500353/)
  来源：PubMed | 日期：2026-08-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：护士在精准癌症护理路径中发挥着关键作用，支持基因组检测的整合并提供以患者为中心的持续护理。本范围综述旨在梳理护士在精准癌症护理中的角色、能力要求及相关教育现状。研究遵循JBI方法，系统检索了MEDLINE、Embase等数据库，并利用生成式人工智能（GenAI）对灰色文献中的国际研究生及继续教育项目进行了检索。研究共纳入52篇文献（44篇涉及角色/能力，23篇涉及教育干预）和65个教育项目。结果识别出五大护理角色主题：基因组风险评估与分...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Multi-omic biomarkers of neoadjuvant treatment response in rectal cancer: A narrative review.](https://pubmed.ncbi.nlm.nih.gov/42250371/)
  来源：PubMed | 日期：2026-08-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：直肠癌对新辅助治疗的反应具有高度异质性，这增加了器官保留策略中患者筛选的复杂性。本综述回顾了2015年以来关于直肠癌新辅助治疗反应预测因子的研究，涵盖六大领域：基因组与分子生物标志物、影像学标志物、组织病理学与数字病理标志物、液体活检（cfDNA/ctDNA）、患者来源的肿瘤模型以及微生物组相关标志物。研究表明，治疗反应受肿瘤内在特征、免疫微环境和间质特征的共同影响。免疫富集型肿瘤（如高CD8+ T细胞浸润、CMS1/iCMS3亚型、高...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [ASO Special Article: Proceedings of the Inaugural Joint US-India Cancer Dialogue: Accelerating Collaboration to Advance Cancer Prevention, Early Detection, Treatment, and Care.](https://pubmed.ncbi.nlm.nih.gov/42166060/)
  来源：PubMed | 日期：2026-08-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：癌症是美印两国的主要死因。2023年6月印度总理访美期间，两国承诺建立美印癌症对话机制，旨在通过结构化双边努力应对共同的癌症挑战。本文概述了2024年8月在新德里举行的首届美印癌症对话联合会议的筹备步骤与议程。通过由政府、科学和临床领导者参与的结构化共识制定流程，确定了双边合作的优先领域。筹备工作包括由美国临床肿瘤学会（ASCO）主办的技术工作组会议，涵盖预防、早期检测、治疗、临床试验和实施科学。会议最终确定了多项核心合作方向：扩大HP...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial intelligence, omics, and biomarkers: Redefining lung cancer early detection.](https://pubmed.ncbi.nlm.nih.gov/42105533/)
  来源：PubMed | 日期：2026-08-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：肺癌是全球死亡率最高的癌症，主要归因于早期干预手段有限。目前的筛查方法受限于侵入性、辐射暴露及早期灵敏度低等问题，亟需创新技术。本综述探讨了结合生物标志物、组学技术与人工智能（AI）的早期检测新兴工具。肿瘤细胞释放的特定生物标志物（如细胞成分、核酸片段、蛋白质片段或代谢物）可通过非侵入性体液检测获取。将生物标志物与蛋白质组学、基因组学或多组学结合，可提供不同癌症亚型和阶段分子特征的全面见解。机器学习和深度学习等AI工具进一步提升了这些技...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [RGTFormer: Predicting mutation-associated multi-drug resistance in Mycobacterium tuberculosis using a categorical gated transformer and relational graph convolutional network.](https://pubmed.ncbi.nlm.nih.gov/41722285/)
  来源：PubMed | 日期：2026-08-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：结核分枝杆菌引起的多重耐药结核病是全球公共卫生面临的重大挑战。耐药性通常由药物靶基因的单核苷酸突变引起，因此早期预测对于有效治疗至关重要。本研究提出了一种名为 RGTFormer 的新型深度学习模型，该模型结合了分类门控 Transformer 和关系图卷积网络（RGCN），用于预测 6 个关键耐药基因的突变是否会导致对一线抗结核药物的耐药性。RGTFormer 整合了突变的序列特征和结构特征，利用 RGCN 捕捉突变之间的依赖关系，并...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [GLM-RAG: Graph Language Models for Graph-Based Retrieval-Augmented Generation](http://arxiv.org/abs/2607.28397v1)
  来源：arXiv | 日期：2026-07-30 | 相关度：4.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) over knowledge graphs requires retrievers that can effectively capture both graph structure and semantic information. Recent approaches have explored graph neural network (GNN)-based ...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。
