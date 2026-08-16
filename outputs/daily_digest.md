# 每日论文监控日报 (2026-08-16)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 21 篇新论文。

## 抓取状态

- arXiv：成功，命中 20 篇
- PubMed：成功，命中 38 篇
- bioRxiv：失败，命中 0 篇，错误：Expecting value: line 1 column 1 (char 0)
- medRxiv：失败，命中 0 篇，错误：Expecting value: line 1 column 1 (char 0)

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [Natural Language Processing: A Comprehensive Practical Guide from Tokenisation to RLHF](http://arxiv.org/abs/2605.03799v3)
  来源：arXiv | 日期：2026-05-05 | 相关度：7.9 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：This preprint presents a systematic, research-oriented practicum that guides the reader through the entire modern NLP pipeline --- from tokenisation and vectorisation to fine tuning of large language models, retrieval au...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Multi-Resolution Cells to Gigapixel Whole Slide Images Foundation Model for Computational Pathology](http://arxiv.org/abs/2608.03508v2)
  来源：arXiv | 日期：2026-08-04 | 相关度：7.5 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Vision Transformers (ViTs) and their hierarchical variants have achieved strong performance in Computational Pathology (CPath). However, most are pre-trained on single-resolution Whole Slide Images (WSIs), limiting their...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Aligning protein-generative models to experimental fitness with ProteinDPO.](https://pubmed.ncbi.nlm.nih.gov/42601461/)
  来源：PubMed | 日期：2026-08-14 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Biological generative models can predict biological functions without task-specific training data but often under-perform specialized models. This is due to a fundamental 'alignment gap', where the rules learned during u...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Multi-omics precision diagnosis of brucellosis: Advances in biomarker discovery and clinical application.](https://pubmed.ncbi.nlm.nih.gov/42128325/)
  来源：PubMed | 日期：2026-08-15 | 相关度：7.4 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：Brucellosis, a neglected zoonosis caused by intracellular Brucella bacteria, remains a formidable global public health challenge, especially in developing regions. The notorious ability of Brucella to evade host immunity...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Foam-Agent: A Large Language Model-Based Multi-Agent Framework for Automating Computational Fluid Dynamics Workflows](http://arxiv.org/abs/2505.04997v3)
  来源：arXiv | 日期：2025-05-08 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Computational fluid dynamics (CFD) has been the main workhorse of computational physics, yet its steep learning curve and fragmented, multi-stage workflow create significant barriers to entry. We present Foam-Agent, a mu...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [How Significant Are the Real Performance Gains? An Unbiased Evaluation Framework for GraphRAG](http://arxiv.org/abs/2506.06331v2)
  来源：arXiv | 日期：2025-05-31 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：By retrieving contexts from knowledge graphs, graph-based retrieval-augmented generation (GraphRAG) enhances large language models (LLMs) to generate quality answers for user questions. Many GraphRAG methods have been pr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Intern-S2-Preview: Scientific Agentic Foundation Model](http://arxiv.org/abs/2608.13505v1)
  来源：arXiv | 日期：2026-08-13 | 相关度：3.85 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Scientific discovery increasingly requires AI systems that can reason over scientific evidence of heterogeneous modalities, interact with scientific tools and environments, and sustain progress across long task horizons....
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Comprehensive Empirical Evaluation of Vector Database Systems for Approximate Nearest Neighbor Search: Performance, Quality, and Resource Trade-offs](http://arxiv.org/abs/2608.12812v1)
  来源：arXiv | 日期：2026-08-13 | 相关度：1.4 | 新颖度：1.5
  匹配主题：未命中具体主题
  中文摘要：Vector databases have emerged as critical infrastructure for modern artificial intelligence applications, particularly retrieval-augmented generation (RAG), semantic search, and recommendation systems. Despite their grow...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OmniScientist: An Omni-Modal Omni-Discipline AI Scientist](http://arxiv.org/abs/2608.13558v1)
  来源：arXiv | 日期：2026-08-13 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Recent advances in foundation models have enabled AI scientists to automate increasingly complete research workflows, from hypothesis generation and code execution to manuscript preparation. Yet workflow coverage alone d...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [The EPS Research Astro-RAG Platform: A Unified Open-Science Infrastructure for Cross-Epoch Astrophysical Kinematic Analysis, LLM-Assisted Research Workflows, and Educational Outreach](http://arxiv.org/abs/2605.30384v2)
  来源：arXiv | 日期：2026-05-28 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Correction (August 2026): A previously reported cross-epoch omega sign reversal was caused by a formula implementation error. Using the corrected canonical equation, all eight Tier-1 Z1 rotators yield positive omega valu...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Query Translation vs. Cross-Lingual Embeddings for Sinhala-Tamil E-Government Information Retrieval](http://arxiv.org/abs/2608.12820v1)
  来源：arXiv | 日期：2026-08-13 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：This paper presents a comparative evaluation of cross-lingual information retrieval (CLIR) methods for retrieving English government information using Sinhala and Tamil queries. Two CLIR paradigms are investigated: Query...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [When Should Multi-Round RAG Stop? Structured Stopping Judgments and Retrieval Reduction in Search-R1](http://arxiv.org/abs/2608.13237v1)
  来源：arXiv | 日期：2026-08-13 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Multi-round retrieval-augmented generation (RAG) must decide when to stop searching as evidence accumulates. Because the deployed policy is determined by the first STOP on each trajectory, this is a sequential selection ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Requirements-Augmented Generation for Trustworthy Acceptance Testing of LLM-Based Software](http://arxiv.org/abs/2608.12970v1)
  来源：arXiv | 日期：2026-08-13 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：LLM-based software (LBS) integrates large language models as core components to deliver flexible, personalised responses. Unlike traditional software with deterministic outputs, LBSs exhibit context-dependent, stochastic...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Static analysis-guided agentic AI translation enables Rust as a full stack bioinformatics language](http://arxiv.org/abs/2608.13029v1)
  来源：arXiv | 日期：2026-08-13 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：The field of bioinformatics struggles with legacy code - old code that is commonly used but may no longer have a maintainer, or may be written in an now-unfamiliar language (e.g. Perl, Fortran). This incurs maintenance c...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Integrating stemness and epithelial-mesenchymal transition signatures with machine learning identifies RUNX1 as a therapeutic vulnerability in colorectal cancer.](https://pubmed.ncbi.nlm.nih.gov/42372471/)
  来源：PubMed | 日期：2026-08-15 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Colorectal cancer (CC) arises from a complex interplay between genetic and epigenetic alterations within the colorectal mucosa, resulting in unchecked cellular proliferation and tumor development. This complexity results...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Emerging and Re-Emerging Viral Infections in Poultry: Integrating Traditional and AI-Based Control Strategies.](https://pubmed.ncbi.nlm.nih.gov/42599520/)
  来源：PubMed | 日期：2026-08-14 | 相关度：5.45 | 新颖度：0.25
  匹配主题：pathogenomics, application_monitoring
  中文摘要：Poultry production remains significantly challenged by emerging and re-emerging avian viral diseases, which are influenced by host-pathogen interactions, viral evolution, and intensified farming systems. Viruses like avi...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Beyond Morphology: Reframing Lymph-Node Metastasis Prediction Through Clonal Ecology-Decades-Long Genomic Instability and Polyclonal-to-Monoclonal Transitions as the Missing Dimension in Cancer.](https://pubmed.ncbi.nlm.nih.gov/42598790/)
  来源：PubMed | 日期：2026-08-14 | 相关度：3.75 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Recent whole-genome, lineage-tracing, single-cell, and spatial studies have reshaped our understanding of tumor evolution, revealing that cancers can arise from polyclonal populations, undergo decades-long genomic instab...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Machine learning and AI for cancer research and care: a review of applications, limitations, and future directions.](https://pubmed.ncbi.nlm.nih.gov/42599390/)
  来源：PubMed | 日期：2026-08-14 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Machine learning (ML) is transforming cancer research and care by enabling analysis of complex, high-dimensional datasets spanning genomics, transcriptomics, proteomics, imaging, and clinical records. By improving risk s...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Bridging innovation and implementation in laboratory medicine: insights from a global survey on unmet needs and emerging technologies.](https://pubmed.ncbi.nlm.nih.gov/42119761/)
  来源：PubMed | 日期：2026-08-15 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Technological innovation in laboratory medicine is advancing rapidly, driven by artificial intelligence, next-generation sequencing, high-resolution mass spectrometry, novel biomarkers, and decentralized point-of-care te...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [GEM: A Generative Embedding Model Bridging Reasoning and Retrieval](http://arxiv.org/abs/2608.13200v1)
  来源：arXiv | 日期：2026-08-13 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Modern LLMs excel at reasoning and instruction following, enabling users to express complex and diverse information needs. However, conventional retrievers largely rely on surface-level matching between queries and docum...
  为什么值得看：GEM: A Generative Embedding Model Bridgi 与你的主题有弱匹配，暂时保留作低优先级跟踪。

- [Who Speaks Matters: Authority-Aware Multi-View RAG over Italian Parliamentary Proceedings](http://arxiv.org/abs/2608.13410v1)
  来源：arXiv | 日期：2026-08-13 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Parliamentary proceedings are a primary record of democratic deliberation, yet their volume and fragmentation make multi-perspective access difficult for citizens, journalists, and researchers. Applying Retrieval-Augment...
  为什么值得看：Who Speaks Matters: Authority-Aware Mult 与你的主题有弱匹配，暂时保留作低优先级跟踪。
