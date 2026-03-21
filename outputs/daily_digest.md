# 每日论文监控日报 (2026-03-21)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 61 篇新论文。

## 抓取状态

- arXiv：成功，命中 45 篇
- PubMed：成功，命中 29 篇
- bioRxiv：成功，命中 30 篇
- medRxiv：成功，命中 18 篇

## 最值得看

### Foundation Model / Agent

- [HViLM: A Foundation Model for Viral Genomics Enables Multi-Task Prediction of Pathogenicity, Transmissibility, and Host Tropism](https://www.biorxiv.org/content/10.64898/2026.03.18.712700v1)
  来源：bioRxiv | 日期：2026-03-20 | 相关度：10.0 | 新颖度：7.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Motivation: The emergence of novel viral pathogens poses critical threats to global health, yet current computational approaches for viral risk assessment are predominantly virus-specific and require extensive retraining...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BioReason-Pro: Advancing Protein Function Prediction with Multimodal Biological Reasoning](https://www.biorxiv.org/content/10.64898/2026.03.19.712954v1)
  来源：bioRxiv | 日期：2026-03-20 | 相关度：8.9 | 新颖度：6.2
  匹配主题：foundation_model_agent
  中文摘要：Protein function annotation is fundamental to understanding biological mechanisms, designing therapeutics, and advancing biomedical research. Current computational methods either rely on shallow sequence similarity or tr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [CliPepPI: Scalable prediction of domain-peptide specificityusing contrastive learning](https://www.biorxiv.org/content/10.64898/2026.03.18.712595v1)
  来源：bioRxiv | 日期：2026-03-20 | 相关度：7.65 | 新颖度：6.25
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Domain-peptide interactions mediate a significant fraction of cellular protein networks, yet accurately predicting their specificity remains challenging. Peptide motifs typically have short, fuzzy sequence profiles, and ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Designing mRNA coding sequence via multimodal reverse translation language modeling with Pro2RNA](https://www.biorxiv.org/content/10.64898/2026.03.18.712790v1)
  来源：bioRxiv | 日期：2026-03-20 | 相关度：8.5 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：mRNA coding sequence design is a critical component in the development of mRNA vaccines, nucleic acid therapeutics, and heterologous gene expression systems. While large language models have recently been successfully ap...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [From Snapshots to Symphonies: The Evolution of Protein Prediction from Static Structures to Generative Dynamics and Multimodal Interactions](http://arxiv.org/abs/2603.18505v1)
  来源：arXiv | 日期：2026-03-19 | 相关度：8.5 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：The protein folding problem has been fundamentally transformed by artificial intelligence, evolving from static structure prediction toward the modeling of dynamic conformational ensembles and complex biomolecular intera...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Caption Injection for Optimization in Generative Search Engine](http://arxiv.org/abs/2511.04080v2)
  来源：arXiv | 日期：2025-11-06 | 相关度：7.9 | 新颖度：1.7
  匹配主题：foundation_model_agent
  中文摘要：Generative Search Engine (GSE) leverages the Retrieval-Augmented Generation (RAG) technique and the Large Language Model (LLM) to integrate multi-source information and provide users with accurate and comprehensive respo...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HARVEST: Unlocking the Dark Bioactivity Data of Pharmaceutical Patents via Agentic AI](https://www.biorxiv.org/content/10.64898/2026.03.15.711910v1)
  来源：bioRxiv | 日期：2026-03-18 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Pharmaceutical patents contain vast Structure-Activity Relationship tables documenting protein- ligand binding data that are technically public yet computationally inaccessible, rendering this wealth of data effectively ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Sentiment in Clinical Notes: A Predictor for Length of Stay?](https://www.medrxiv.org/content/10.64898/2026.03.16.26348553v1)
  来源：medRxiv | 日期：2026-03-18 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：BackgroundLength of stay (LOS) is a critical metric for hospital operational efficiency. While structured clinical data is widely used to predict LOS, unstructured admission notes contain latent prognostic information re...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Protocol to Analysis Plan: Development and Validation of a Large Language Model Pipeline for Statistical Analysis Plan Generation using Artificial Intelligence (SAPAI)](https://www.medrxiv.org/content/10.64898/2026.03.19.26348626v1)
  来源：medRxiv | 日期：2026-03-19 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Background: Statistical Analysis Plans (SAPs) are essential for trial transparency and credibility but are resource-intensive to produce. While Large Language Models (LLMs) have shown promise in drafting protocols, their...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MRD: Multi-resolution Retrieval-Detection Fusion for High-Resolution Image Understanding](http://arxiv.org/abs/2512.02906v3)
  来源：arXiv | 日期：2025-12-02 | 相关度：6.8 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Understanding high-resolution (HR) images remains a critical challenge for multimodal large language models (MLLMs). Recent approaches leverage vision-based retrieval-augmented generation (RAG) to retrieve query-relevant...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Role-Augmented Intent-Driven Generative Search Engine Optimization](http://arxiv.org/abs/2508.11158v2)
  来源：arXiv | 日期：2025-08-15 | 相关度：6.55 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Generative Search Engines (GSEs), powered by Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG), are reshaping information retrieval. While commercial systems (e.g., BingChat, Perplexity.ai) demonstrat...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AI4S-SDS: A Neuro-Symbolic Solvent Design System via Sparse MCTS and Differentiable Physics Alignment](http://arxiv.org/abs/2603.03686v2)
  来源：arXiv | 日期：2026-03-04 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Automated design of chemical formulations is a cornerstone of materials science, yet it requires navigating a high-dimensional combinatorial space involving discrete compositional choices and continuous geometric constra...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MetaBeeAI: an AI pipeline for structured evidence extraction from biological literature](https://www.biorxiv.org/content/10.1101/2025.11.24.690154v2)
  来源：bioRxiv | 日期：2026-03-18 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：The volume and complexity of scientific literature are expanding rapidly, making it increasingly difficult to extract and synthesise information across studies. This challenge is particularly acute in the biological scie...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Large Language Models in Teaching and Learning: Reflections on Implementing an AI Chatbot in Higher Education](http://arxiv.org/abs/2603.17773v1)
  来源：arXiv | 日期：2026-03-18 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：The landscape of education is changing rapidly, shaped by emerging pedagogical approaches, technological innovations such as artificial intelligence (AI), and evolving societal expectations, all of which demand thorough ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MemArchitect: A Policy Driven Memory Governance Layer](http://arxiv.org/abs/2603.18330v1)
  来源：arXiv | 日期：2026-03-18 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Persistent Large Language Model (LLM) agents expose a critical governance gap in memory management. Standard Retrieval-Augmented Generation (RAG) frameworks treat memory as passive storage, lacking mechanisms to resolve ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Grounded Multimodal Retrieval-Augmented Drafting of Radiology Impressions Using Case-Based Similarity Search](http://arxiv.org/abs/2603.17765v1)
  来源：arXiv | 日期：2026-03-18 | 相关度：8.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Automated radiology report generation has gained increasing attention with the rise of deep learning and large language models. However, fully generative approaches often suffer from hallucinations and lack clinical grou...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Coupling codon and protein constraints decouples drivers of variant pathogenicity](https://www.biorxiv.org/content/10.1101/2025.03.12.642937v3)
  来源：bioRxiv | 日期：2026-03-20 | 相关度：7.7 | 新颖度：5.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Predicting the functional impact of genetic variants remains a fundamental challenge in genomics. Existing models focus on protein-intrinsic defects yet overlook regulatory constraints embedded within coding sequences. H...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Leveraging Residual Graph Convolutional Networks with Cross-Attention Mechanisms for High-Accuracy Protein Function Prediction.](https://pubmed.ncbi.nlm.nih.gov/41861353/)
  来源：PubMed | 日期：2026-03-20 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Precise determination of protein functions is essential for elucidating cellular processes and pathological mechanisms, thereby facilitating targeted drug design. Although wet-lab experimental methods remain the gold sta...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [X-Cell: Scaling Causal Perturbation Prediction Across Diverse Cellular Contexts via Diffusion Language Models](https://www.biorxiv.org/content/10.64898/2026.03.18.712807v1)
  来源：bioRxiv | 日期：2026-03-20 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Causal models of cellular systems hold the promise to empower broad biological discovery, including the systematic identification of novel targets for drug discovery. Predicting how genetic and pathway perturbations resh...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Identifying microbial protease allergens through protein language model-guided homology.](https://pubmed.ncbi.nlm.nih.gov/41722567/)
  来源：PubMed | 日期：2026-03-18 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Emerging research links the gut, skin, and oral microbiomes to allergies, with serine proteases (SPs) identified as potential allergens. This study leverages deep learning and pre-trained protein language models (pLMs) t...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [Leveraging Large Language Models to Extract Prognostic Pathology Features in Ewing Sarcoma](https://www.biorxiv.org/content/10.64898/2026.02.20.707103v2)
  来源：bioRxiv | 日期：2026-03-19 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Background: Current risk stratification for Ewing sarcoma relies heavily on clinical factors such as metastatic status, failing to capture histologic heterogeneity as a potential prognostic indicator. Although pathology ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Slides to Chatbots: Enhancing Large Language Models with University Course Materials](http://arxiv.org/abs/2510.22272v2)
  来源：arXiv | 日期：2025-10-25 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have advanced rapidly in recent years. One application of LLMs is to support student learning in educational settings. However, prior work has shown that LLMs still struggle to answer questio...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Unified Language Model for Large Scale Search, Recommendation, and Reasoning](http://arxiv.org/abs/2603.17533v1)
  来源：arXiv | 日期：2026-03-18 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：LLMs are increasingly applied to recommendation, retrieval, and reasoning, yet deploying a single end-to-end model that can jointly support these behaviors over large, heterogeneous catalogs remains challenging. Such sys...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CyberJustice Tutor: An Agentic AI Framework for Cybersecurity Learning via Think-Plan-Act Reasoning and Pedagogical Scaffolding](http://arxiv.org/abs/2603.18470v1)
  来源：arXiv | 日期：2026-03-19 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：The integration of Large Language Models (LLMs) into cybersecurity education for criminal justice professionals is currently hindered by the "statelessness" of reactive chatbots and the risk of hallucinations in high-sta...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PREBA: Surgical Duration Prediction via PCA-Weighted Retrieval-Augmented LLMs and Bayesian Averaging Aggregation](http://arxiv.org/abs/2603.13275v2)
  来源：arXiv | 日期：2026-02-27 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Accurate prediction of surgical duration is pivotal for hospital resource management. Although recent supervised learning approaches-from machine learning (ML) to fine-tuned large language models (LLMs)-have shown strong...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SOORENA: Self-lOOp containing or autoREgulatory Nodes in biological network Analysis](https://www.biorxiv.org/content/10.1101/2025.11.03.685842v4)
  来源：bioRxiv | 日期：2026-03-19 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Autoregulatory mechanisms, in which proteins regulate their own activity or expression, are fundamental to biological networks but are challenging to identify systematically from literature. To address this gap, we prese...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [InferDPT: Privacy-Preserving Inference for Closed-box Large Language Model](http://arxiv.org/abs/2310.12214v8)
  来源：arXiv | 日期：2023-10-18 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs), like ChatGPT, have greatly simplified text generation tasks. However, they have also raised concerns about privacy risks such as data leakage and unauthorized data collection. Existing solut...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Prompt Control-Flow Integrity: A Priority-Aware Runtime Defense Against Prompt Injection in LLM Systems](http://arxiv.org/abs/2603.18433v1)
  来源：arXiv | 日期：2026-03-19 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) deployed behind APIs and retrieval-augmented generation (RAG) stacks are vulnerable to prompt injection attacks that may override system policies, subvert intended behavior, and induce unsafe...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Rule-Based Explanations for Retrieval-Augmented LLM Systems](http://arxiv.org/abs/2510.22689v2)
  来源：arXiv | 日期：2025-10-26 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：If-then rules are widely used to explain machine learning models; e.g., "if employed = no, then loan application = rejected." We present the first proposal to apply rules to explain the emerging class of large language m...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multimodal Model for Computational Pathology:Representation Learning and Image Compression](http://arxiv.org/abs/2603.18660v1)
  来源：arXiv | 日期：2026-03-19 | 相关度：4.85 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Whole slide imaging (WSI) has transformed digital pathology by enabling computational analysis of gigapixel histopathology images. Recent foundation model advances have accelerated progress in computational pathology, fa...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [FinTradeBench: A Financial Reasoning Benchmark for LLMs](http://arxiv.org/abs/2603.19225v1)
  来源：arXiv | 日期：2026-03-19 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Real-world financial decision-making is a challenging problem that requires reasoning over heterogeneous signals, including company fundamentals derived from regulatory filings and trading signals computed from price dyn...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Open Biomedical Knowledge Graphs at Scale: Construction, Federation, and AI Agent Access with Samyama Graph Database](http://arxiv.org/abs/2603.15080v3)
  来源：arXiv | 日期：2026-03-16 | 相关度：3.1 | 新颖度：1.75
  匹配主题：未命中具体主题
  中文摘要：Biomedical knowledge is fragmented across siloed databases -- Reactome for pathways, STRING for protein interactions, ClinicalTrials.gov for study registries, DrugBank for drug vocabularies, DGIdb for drug-gene interacti...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Peripheral Treg-monocyte immune signatures relate to neurodegeneration and prognosis in patients with primary tauopathies](https://www.medrxiv.org/content/10.64898/2026.03.17.26348492v1)
  来源：medRxiv | 日期：2026-03-19 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Background: Neuroinflammation is a common hallmark of primary tauopathies, and is associated with worse clinical outcomes over time. However, accurate prognosis in these disorders remains challenging, and current fluid b...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [IoDResearch: Deep Research on Private Heterogeneous Data via the Internet of Data](http://arxiv.org/abs/2510.01553v2)
  来源：arXiv | 日期：2025-10-02 | 相关度：2.1 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：随着多源、异构和多模态科学数据的快速增长，传统数据管理的局限性日益凸显。现有的深度研究（DeepResearch）工作主要集中在网络搜索，忽视了本地私有数据，导致检索效率低下且不符合 FAIR 原则。为此，我们提出了 IoDResearch，这是一个以私有数据为中心的深度研究框架，实现了“数据互联网”（IoD）范式。该框架将异构资源封装为符合 FAIR 标准的数字对象，并进一步细化为原子知识单元和知识图谱，构建出用于多粒度检索的异构图索...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RADAR: Retrieval-Augmented Detector with Adversarial Refinement for Robust Fake News Detection](http://arxiv.org/abs/2601.03981v2)
  来源：arXiv | 日期：2026-01-07 | 相关度：2.05 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：为了有效应对大语言模型（LLM）生成的虚假信息传播，本文提出了 RADAR（具有对抗性细化的检索增强检测器）。该方法包含一个通过事实扰动重写真实文章的生成器，以及一个利用稠密通道检索（dense passage retrieval）验证主张的轻量级检测器。为了实现有效的协同进化，研究引入了口头对抗反馈（VAF）。VAF 不依赖传统的标量奖励，而是发布结构化的自然语言评论，引导生成器进行更复杂的规避尝试，从而迫使检测器不断适应和改进。在虚...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TopoChunker: Topology-Aware Agentic Document Chunking Framework](http://arxiv.org/abs/2603.18409v1)
  来源：arXiv | 日期：2026-03-19 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）中现有的文档分块方法通常将文本线性化，这种强制线性化剥离了内在的拓扑层级，导致“语义碎片化”并降低检索质量。本文提出 TopoChunker，这是一种基于 Agent 的框架，通过将异构文档映射到结构化中间表示（SIR）来显式保留跨段依赖关系。为平衡结构保真度与计算成本，TopoChunker 采用双 Agent 架构：Inspector Agent 根据成本优化路径动态路由文档，而 Refiner Agent 执...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RPMS: Enhancing LLM-Based Embodied Planning through Rule-Augmented Memory Synergy](http://arxiv.org/abs/2603.17831v1)
  来源：arXiv | 日期：2026-03-18 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：LLM 智能体在封闭具身环境中常因动作需满足严格前提条件（如位置、库存、容器状态）且反馈稀疏而失败。本文识别了两种耦合的失败模式：无效动作生成（P1）和状态漂移（P2），两者会形成退化循环。为此，我们提出 RPMS 架构，通过结构化规则检索强制执行动作可行性，利用轻量级信念状态过滤记忆适用性，并通过“规则优先”仲裁机制解决两者间的冲突。在 ALFWorld 的 134 个未知任务中，RPMS 使 Llama 3.1 8B 的单次尝试成功...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Advancing FAIR Data Management through AI-Assisted Curation of Morphological Data Matrices](https://www.biorxiv.org/content/10.1101/2025.07.08.663621v3)
  来源：bioRxiv | 日期：2026-03-19 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Curation of biological and paleontological datasets is a labor-intensive process that requires standardization and validation to ensure data integrity. In particular, manual curation of datasets is prone to human errors ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [An AI-Driven Decision-Support Tool for Triage of COVID-19 Patients Using Respiratory Microbiome Data](https://www.biorxiv.org/content/10.64898/2026.03.18.712739v1)
  来源：bioRxiv | 日期：2026-03-19 | 相关度：3.2 | 新颖度：0.75
  匹配主题：application_monitoring
  中文摘要：Accurate clinical triage is critical for optimizing decision-making and resource allocation during infectious disease outbreaks such as COVID-19. In this study, we present an AI-driven decision-support tool for the triag...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [LMEB: Long-horizon Memory Embedding Benchmark](http://arxiv.org/abs/2603.12572v2)
  来源：arXiv | 日期：2026-03-13 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：内存嵌入对增强内存系统（如 OpenClaw）至关重要，但现有文本嵌入基准侧重于传统段落检索，无法评估模型处理碎片化、上下文依赖及时间跨度大的长程记忆检索任务的能力。为此，本文推出了长程记忆嵌入基准（LMEB），这是一个评估嵌入模型处理复杂长程记忆检索能力的综合框架。LMEB 涵盖 22 个数据集和 193 个零样本检索任务，分为情景、对话、语义和程序四种记忆类型，包含 AI 生成和人工标注数据。这些类型在抽象程度和时间依赖性上有所不同...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Beyond Muon: MUD (MomentUm Decorrelation) for Faster Transformer Training](http://arxiv.org/abs/2603.17970v1)
  来源：arXiv | 日期：2026-03-18 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Orthogonalized-momentum optimizers such as Muon improve transformer training by approximately whitening/orthogonalizing matrix-valued momentum updates via a short polar-decomposition iteration. However, polar-factor appr...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [HERCULES: an integrative deep-learning framework for predicting RNA-binding propensity and mutation effects at single-residue resolution](https://www.biorxiv.org/content/10.64898/2026.03.17.712455v1)
  来源：bioRxiv | 日期：2026-03-18 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：RNA-binding proteins (RBPs) regulate essential aspects of RNA metabolism, yet accurately identifying RNA-binding domains (RBDs) and quantifying the impact of sequence variation on RNA-binding ability remain challenging. ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ST-PARM: Pareto-Complete Inference-Time Alignment for Multi-Objective Protein Design](https://www.biorxiv.org/content/10.64898/2026.03.17.712483v1)
  来源：bioRxiv | 日期：2026-03-19 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Motivation: Protein engineering is inherently multi-objective: improving one property can degrade others, so practical workflows require generating non-dominated (Pareto-optimal) candidates spanning a trade-off surface. ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RAGXplain: From Explainable Evaluation to Actionable Guidance of RAG Pipelines](http://arxiv.org/abs/2505.13538v2)
  来源：arXiv | 日期：2025-05-18 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) systems couple large language models with external knowledge, yet most evaluation methods report aggregate scores that reveal whether a pipeline underperforms but not where or why. We...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Adaptive Guidance for Retrieval-Augmented Masked Diffusion Models](http://arxiv.org/abs/2603.17677v1)
  来源：arXiv | 日期：2026-03-18 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) improves factual grounding by incorporating external knowledge into language model generation. However, when retrieved context is noisy, unreliable, or inconsistent with the model's p...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [LLM-Augmented Changepoint Detection: A Framework for Ensemble Detection and Automated Explanation](http://arxiv.org/abs/2601.02957v3)
  来源：arXiv | 日期：2026-01-06 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：This paper introduces a novel changepoint detection framework that combines ensemble statistical methods with Large Language Models (LLMs) to enhance both detection accuracy and the interpretability of regime changes in ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [LR-Robot: A Unified Supervised Intelligent Framework for Real-Time Systematic Literature Reviews with Large Language Models](http://arxiv.org/abs/2603.17723v1)
  来源：arXiv | 日期：2026-03-18 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in artificial intelligence (AI) and natural language processing (NLP) have enabled tools to support systematic literature reviews (SLRs), yet existing frameworks often produce outputs that are efficient b...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Retrieval-Augmented LLM Agents: Learning to Learn from Experience](http://arxiv.org/abs/2603.18272v1)
  来源：arXiv | 日期：2026-03-18 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：While large language models (LLMs) have advanced the development of general-purpose agents, achieving robust generalization to unseen tasks remains a significant challenge. Current approaches typically rely on either fin...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [From Study Design to Executable Code: Automating Target Trial Emulation with Large Language Models](https://www.medrxiv.org/content/10.64898/2026.03.13.26348306v2)
  来源：medRxiv | 日期：2026-03-19 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：实施目标试验模拟（TTE）研究并生成端到端可执行分析代码具有极高的技术门槛。本研究开发了 THESEUS 框架，旨在将自由文本形式的研究描述转化为 OHDSI 生态系统中标准化的分析规范和可执行的 Strategus R 脚本。THESEUS 包含两个核心步骤：首先，利用大语言模型（LLM）将研究描述映射到受限的 JSON 模式中实现标准化；其次，将结构化规范转换为 R 脚本，并引入自审计循环进行错误修正。研究评估了 8 种商业 LLM...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Hypothesis-Conditioned Query Rewriting for Decision-Useful Retrieval](http://arxiv.org/abs/2603.19008v1)
  来源：arXiv | 日期：2026-03-19 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) improves Large Language Models (LLMs) by grounding generation in external, non-parametric knowledge. However, when a task requires choosing among competing options, simply grounding g...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [HGP-Mamba: Integrating Histology and Generated Protein Features for Mamba-based Multimodal Survival Risk Prediction](http://arxiv.org/abs/2603.16421v2)
  来源：arXiv | 日期：2026-03-17 | 相关度：3.75 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in multimodal learning have significantly improved cancer survival risk prediction. However, the joint prognostic potential of protein markers and histopathology images remains underexplored, largely due ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Species-specific small models for cell type classification approach the performance of large single cell foundation models](https://www.biorxiv.org/content/10.64898/2026.03.16.711196v1)
  来源：bioRxiv | 日期：2026-03-18 | 相关度：2.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：跨物种细胞类型分类是单细胞转录组学的核心任务。尽管基于数百万单细胞图谱训练的大型基础模型表现强劲，但其庞大的参数量和计算成本限制了可访问性与可解释性。本文引入了 CytoType，一种利用预训练 ESM-2 蛋白质嵌入进行细胞分类的简单可解释模型。CytoType 通过学习转录本嵌入上的线性细胞类型特定权重，在不依赖基因计数信息的情况下，实现了与大型 Transformer 基础模型相当或更高的 F1 分数。研究者还开发了更简化的变体 ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [DaPT: A Dual-Path Framework for Multilingual Multi-hop Question Answering](http://arxiv.org/abs/2603.19097v1)
  来源：arXiv | 日期：2026-03-19 | 相关度：2.05 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：检索增强生成（RAG）系统在解决英语复杂多跳问答（QA）任务方面取得了显著进展，但在跨多语言语料库检索时仍面临挑战：一是缺乏评估多语言多跳（MM-hop）QA能力的基准，二是过度依赖大语言模型的英语语义理解能力。为此，本研究首先将仅限英语的基准翻译成五种语言，构建了多语言多跳QA基准。随后提出了DaPT，一种新型多语言RAG框架。该框架为源语言查询及其英语翻译副本并行生成子问题图，并在合并后采用双语检索与回答策略顺序解决子问题。实验结果...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Atomic Trajectory Modeling with State Space Models for Biomolecular Dynamics](http://arxiv.org/abs/2603.17633v1)
  来源：arXiv | 日期：2026-03-18 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：理解生物分子的动态行为对于阐明生物功能和促进药物发现至关重要。虽然分子动力学（MD）模拟为研究这些动态提供了严谨的物理基础，但在长尺度上计算成本极高。现有的深度生成模型虽能加速构象生成，但往往无法建模时间关系，或仅限于单体蛋白质。为弥补这一缺陷，我们提出了 ATMOS，这是一种基于状态空间模型（SSM）的新型生成框架，旨在为生物分子系统生成原子级 MD 轨迹。ATMOS 集成了基于 Pairformer 的状态转换机制以捕捉长程时间依赖...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Cross-Modal Training Using Xenium Spatial Transcriptomics Enables DINO-DETR Based Detection of Vascular Niches in H&E Whole-Slide Images](https://www.biorxiv.org/content/10.64898/2026.03.17.712266v1)
  来源：bioRxiv | 日期：2026-03-19 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：肿瘤血管系统是胶质瘤进展的关键驱动因素，但常规量化依赖主观病理评估或高成本免疫组化。本研究利用 10x Genomics Xenium 空间转录组数据，从胶质母细胞瘤（GBM）样本的 809,041 个细胞中生成了内皮细胞和周细胞的分子级标注。这些标注被迁移至匹配的 H&E 染色切片，用于训练基于 DINO-DETR 的目标检测模型。模型在 4 张独立 Xenium 患者切片上验证，并应用于 119 例弥漫性胶质瘤（WHO 2-4 级）...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SCALE:Scalable Conditional Atlas-Level Endpoint transport for virtual cell perturbation prediction](http://arxiv.org/abs/2603.17380v2)
  来源：arXiv | 日期：2026-03-18 | 相关度：1.4 | 新颖度：1.5
  匹配主题：未命中具体主题
  中文摘要：虚拟细胞模型旨在通过单细胞测量数据，预测细胞对遗传、化学或细胞因子扰动的反应。然而，大规模扰动预测目前面临训练推理效率低下、高维稀疏表达空间建模不稳定以及评估协议过度强调重建精度而忽视生物学保真度三大瓶颈。本研究提出专门用于虚拟细胞扰动预测的大规模基础模型 SCALE。首先，构建了基于 BioNeMo 的训练和推理框架，在相同系统设置下，预训练速度较现有 SOTA 提升 12.51 倍，推理速度提升 1.29 倍。其次，将扰动预测表述为...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Clinician Experiences with Ambient AI Scribe Technology in Singapore: A Qualitative Study](https://www.medrxiv.org/content/10.64898/2026.03.17.26348627v1)
  来源：medRxiv | 日期：2026-03-19 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Background: The administrative burden of clinical documentation is a recognised contributor to clinician burnout and diminished care quality. Ambient artificial intelligence (AI) scribe technology, which uses large langu...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [A Comprehensive Benchmark of Histopathology Foundation Models for Kidney Digital Pathology Images](http://arxiv.org/abs/2603.15967v2)
  来源：arXiv | 日期：2026-03-16 | 相关度：3.05 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Histopathology foundation models (HFMs), pretrained on large-scale cancer datasets, have advanced computational pathology. However, their applicability to non-cancerous chronic kidney disease remains underexplored, despi...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Advances in spherical nanoparticle-labeled lateral flow immunoassays in the field of clinical detection.](https://pubmed.ncbi.nlm.nih.gov/41736637/)
  来源：PubMed | 日期：2026-03-18 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Lateral flow immunoassay (LFIA), as one of the core technologies of point-of-care testing (POCT), holds significant value in pathogen diagnosis and biomarker analysis. Notably, spherical nanomaterials exhibit high clinic...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [OpenScientist: evaluating an open agentic AI co-scientist to accelerate biomedical discovery](https://www.medrxiv.org/content/10.64898/2026.03.15.26348338v1)
  来源：medRxiv | 日期：2026-03-18 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：医学进步受限于研究人员的时间和专业知识。OpenScientist 是一个开源的智能体 AI（agentic AI）科研助手，旨在通过半自主调查研究人员定义的查询，生成临床相关且可验证的科学见解，从而加速生物医学发现。本研究通过四个临床案例评估了 OpenScientist 的性能：(1) 社区阿尔茨海默病生物标志物队列的预设分析；(2) 血浆蛋白质组生存预测的无监督建模；(3) 具有神经原纤维缠结的神经元的单细胞转录组数据假设调查；(...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Integrative approaches in lung cancer diagnosis: bridging molecular biomarkers and AI driven imaging.](https://pubmed.ncbi.nlm.nih.gov/41830914/)
  来源：PubMed | 日期：2026-03-19 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：肺癌的早期精准检测仍是临床重大挑战，传统诊断手段如X射线和组织活检在早期肿瘤识别中灵敏度有限。本文综述了肺癌生物标志物驱动及技术辅助诊断策略的最新进展，重点探讨了EGFR、ALK等分子标志物的临床相关性，并评估了二代测序（NGS）、ctDNA分析及AI分析工具等新兴方法。研究指出，将分子标志物整合入常规诊断提升了肿瘤分型精度并实现了靶向治疗选择；液体活检等无创手段支持实时肿瘤特征分析与监测。同时，NGS及基因组学、转录组学等多组学技术提...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
