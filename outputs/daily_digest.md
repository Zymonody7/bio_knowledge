# 每日论文监控日报 (2026-11-04)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 64 篇新论文。

## 抓取状态

- arXiv：成功，命中 55 篇
- PubMed：成功，命中 153 篇
- bioRxiv：成功，命中 8 篇
- medRxiv：成功，命中 14 篇

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [Applications of large language model in general practice: a qualitative interview study with professionals and patients](https://www.medrxiv.org/content/10.64898/2026.10.30.26366911v1)
  来源：medRxiv | 日期：2026-11-01 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Background: Workload is increasing in general practice. Large language models (LLMs) are a promising tool that could relieve part of this workload. However, existing studies offer little insight into how professionals an...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Variantscape: Retrospective Study of Large Language Model-Based Extraction of Variant-Treatment-Cancer Associations from Published Oncology Abstracts](https://www.medrxiv.org/content/10.64898/2026.08.02.26359492v2)
  来源：medRxiv | 日期：2026-11-02 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Objectives: Precision oncology relies on accurate interpretation of tumour-detected gene variants, to guide personalised treatment decisions. However, interpretation of variants in context requires extensive information ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [El Agente Fármaco: A Scalable AI Scientist for Drug Discovery](http://arxiv.org/abs/2611.03832v1)
  来源：arXiv | 日期：2026-11-02 | 相关度：6.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Computational drug discovery offers a growing range of tools for proposing and evaluating molecules, but combining them and deciding what to do next still requires substantial expert effort. Here, we introduce El Agente ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DAT: Dynamic Alpha Tuning for Hybrid Retrieval in Retrieval-Augmented Generation](http://arxiv.org/abs/2503.23013v2)
  来源：arXiv | 日期：2025-03-29 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Hybrid retrieval techniques in Retrieval-Augmented Generation (RAG) systems enhance information retrieval by combining dense and sparse (e.g., BM25-based) retrieval methods. However, existing approaches struggle with ada...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DARE: Aligning LLM Agents with the R Statistical Ecosystem via Distribution-Aware Retrieval](http://arxiv.org/abs/2603.04743v2)
  来源：arXiv | 日期：2026-03-05 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Large Language Model (LLM) agents excel at automating data science workflows, yet often underutilize rigorous statistical methods in R. Existing Retrieval-Augmented Generation (RAG) approaches rely on semantic similarity...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Toward Agentic AI-Ready Workflows in Built Environment Organizations: Knowledge Structures and Interoperability Challenges](http://arxiv.org/abs/2611.02286v1)
  来源：arXiv | 日期：2026-11-01 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：The rise of agentic artificial intelligence (AI) in the built environment is shifting attention from isolated AI tools toward autonomous systems that reason, plan, and act across project and organizational workflows. The...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EvoMemState: Evolving Memory State for Personal Agents](http://arxiv.org/abs/2611.03743v1)
  来源：arXiv | 日期：2026-11-02 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Long-term memory enables large language model (LLM) agents to provide continuous personalized assistance by retaining user information across interactions. Existing systems support this process through fact extraction, o...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CONFIRM: Governing Scientific Reporting for Trustworthy Agentic Neuroimaging](http://arxiv.org/abs/2611.01449v2)
  来源：arXiv | 日期：2026-11-01 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language model (LLM) agents can autonomously run neuroimaging analyses from research questions to reported findings. Existing agentic systems use tools to check that code runs and reported values match its output, ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond Isolated Dots: Benchmarking Structured Table Construction as Deep Knowledge Extraction](http://arxiv.org/abs/2507.16271v3)
  来源：arXiv | 日期：2025-07-22 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly expected to extract and synthesize structured information from complex real-world documents, yet they typically produce unstructured, hard-to-verify paragraph-style outputs. ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RecoAtlas: A Benchmark and RL Environment for LLM Recommendation Agents Optimizing Set-Level Utility](http://arxiv.org/abs/2605.18805v2)
  来源：arXiv | 日期：2026-05-11 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：LLM recommender agents increasingly produce structured reports: sets of items accompanied by natural-language justifications. Yet existing benchmarks often focus on reranking small candidate sets or judging reports prima...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Knowledge Database of Physical Activity Interventions for Hypertension using Large Language Models](https://www.medrxiv.org/content/10.64898/2026.10.22.26366246v2)
  来源：medRxiv | 日期：2026-11-03 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Physical exercise lowers blood pressure, but guidelines provide broad recommendations that rarely account for age, comorbidities, medications and hypertension severity. A structured, queryable resource of exercise interv...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [vLLM Hook v1: A Plug-in for Programming Model Internals on vLLM](http://arxiv.org/abs/2603.06588v2)
  来源：arXiv | 日期：2026-02-02 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Modern artificial intelligence models are deployed on inference engines to optimize runtime efficiency and resource allocation, particularly for transformer-based large language models. The vLLM project is a major open-s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ScienceVision: Can AI Observe and Reason Like a Scientist?](http://arxiv.org/abs/2611.04087v1)
  来源：arXiv | 日期：2026-11-02 | 相关度：3.75 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Scientific discovery builds on accurate observations interpreted through domain knowledge and reasoning. For scientific 3D data, this requires understanding structures and spatial relationships, from protein contacts to ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [EpiLens: Lightweight RAG for Epidemiological Knowledge Acquisition](http://arxiv.org/abs/2610.26730v2)
  来源：arXiv | 日期：2026-10-19 | 相关度：6.7 | 新颖度：5.25
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：To prepare for future outbreaks, researchers need to know what studies have been done and what data they use. Mapping a large literature by hand is slow, while large language models alone can misstate or conflate sources...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Enhancing Stock Market Information Retrieval with Retrieval-Augmented Generation](http://arxiv.org/abs/2611.03747v1)
  来源：arXiv | 日期：2026-11-02 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Natural Language Processing (NLP) has been widely applied in financial domains, enabling automated analysis and retrieval of stock market information. However, traditional NLP-based systems often struggle with maintainin...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Ablating Design Choices for Protein Ensemble Generators Across Structural Regimes](http://arxiv.org/abs/2611.05055v1)
  来源：arXiv | 日期：2026-11-03 | 相关度：6.45 | 新颖度：6.81
  匹配主题：foundation_model_agent
  中文摘要：Generative models of protein conformational ensembles inherit much of their design from structure prediction for folded proteins. Ordered and disordered proteins, however, occupy distinct structural regimes, and we inves...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A Deep Learning Model for Prediction of Unknown Gene Functionality: Gene Bio-BERT.](https://pubmed.ncbi.nlm.nih.gov/42573472/)
  来源：PubMed | 日期：2026-11-01 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：The Human Genome Project (HGP) was a large international research effort that timelined between 1990 and 2003, marking the successful mapping of the entire human genome. Despite the promising performance of deep learning...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Protein large language model-assisted one-to-one gene homology mapping in cross-species single-cell transcriptome integration.](https://pubmed.ncbi.nlm.nih.gov/42855280/)
  来源：PubMed | 日期：2026-11-03 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Cross-species integration of single-cell transcriptomes requires establishing gene correspondences to enable comparative analysis of expression profiles across organisms. Current approaches predominantly rely on Ensembl ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ES-Merging: Biological MLLM Merging via Embedding Space Signals](http://arxiv.org/abs/2603.14405v3)
  来源：arXiv | 日期：2026-03-15 | 相关度：6.1 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Biological multimodal large language models (MLLMs) have emerged as powerful foundation models for scientific discovery. However, existing models are specialized to a single modality, limiting their ability to solve inhe...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Decoding antibody-antigen recognition: the BL8 language and its application in calibrating deep learning predictions](https://www.biorxiv.org/content/10.64898/2026.10.30.763264v1)
  来源：bioRxiv | 日期：2026-11-02 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Antibodies are central to immunology and therapeutics, and understanding how they recognize antigens is essential to rational drug design. This recognition depends on the interplay of interface geometry, physicochemical ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [HERIT: Enabling Global Access to Hanja-to-English Historical Translation by Mitigating Temporal Bias](http://arxiv.org/abs/2611.04949v1)
  来源：arXiv | 日期：2026-11-03 | 相关度：4.75 | 新颖度：6.87
  匹配主题：foundation_model_agent
  中文摘要：Historical archives are invaluable for multidisciplinary research but remain inaccessible globally due to severe language barriers. While manual translation is prohibitively expensive and time-consuming, simply applying ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Generative artificial intelligence in medical oncology: A clinically focused narrative review of large language, vision-language, and agentic artificial intelligence systems.](https://pubmed.ncbi.nlm.nih.gov/42912826/)
  来源：PubMed | 日期：2026-11-01 | 相关度：8.5 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Rapid advances in cancer genetics and genomics, pathophysiology, diagnostics, and therapeutics have substantially increased the complexity of clinical oncology. Integrating large and diverse data streams into timely, pat...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [TRIO: Task Refinement with Individual Optimization for Retrieval-Augmented Generation](http://arxiv.org/abs/2611.02810v1)
  来源：arXiv | 日期：2026-11-02 | 相关度：5.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：This paper studies retrieval-augmented generation (RAG), which leverages external knowledge to improve the performance of language models. Despite the remarkable progress, current RAG approaches are still far from satisf...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [IAMRAGBENCH: Benchmarking Authorization Expansions in LLM-Generated AWS IAM Policies under RAG Poisoning](http://arxiv.org/abs/2611.03431v1)
  来源：arXiv | 日期：2026-11-02 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) using retrieval-augmented generation (RAG) can synthesize Amazon Web Services (AWS) Identity and Access Management (IAM) policies from tasks and operational documents. Attacker-controlled con...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SearchInject: Retrieval Exposure Control for Indirect Prompt Injection in Language-Model Search](http://arxiv.org/abs/2611.02643v1)
  来源：arXiv | 日期：2026-11-02 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：An indirect prompt injection can affect a search-augmented large language model only after its carrier page reaches model context. SearchInject controls this admission decision with a joint score combining retrieval rele...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HistoTx: Early fusion of H&E images and spatial transcriptomics at varying spatial transcriptomics resolution with self-supervised learning](http://arxiv.org/abs/2611.02681v1)
  来源：arXiv | 日期：2026-11-02 | 相关度：4.85 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Spatial transcriptomics maps gene expression across tissue sections and, when integrated with whole slide images, jointly captures both morphological architecture and molecular activity to provide a rich, multimodal view...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multi-Teacher Reasoning Distillation for LLM Recommendation with Self-Exploration](http://arxiv.org/abs/2611.02457v1)
  来源：arXiv | 日期：2026-11-02 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Reasoning-augmented recommender systems (RecSys) enhance user preference modeling by generating reasoning trajectories over historical interactions before making recommendations. Knowledge distillation provides a practic...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Reimagining computational quantum research with AI scientists](http://arxiv.org/abs/2611.02833v1)
  来源：arXiv | 日期：2026-11-02 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：AI scientists are expanding automated research across scientific domains, yet their ability to turn the scientific record into a foundation for autonomous discovery remains elusive. Here we uncover a fundamental barrier ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [IBDome: An Integrated Molecular, Histopathological, and Clinical Atlas of Inflammatory Bowel Diseases.](https://pubmed.ncbi.nlm.nih.gov/42269946/)
  来源：PubMed | 日期：2026-11-01 | 相关度：3.75 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Multiomic and multimodal datasets with detailed clinical annotations offer significant potential to advance understanding of inflammatory bowel diseases (IBDs), refine diagnostics, and enable personalized therapeutic str...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Mindscape-Aware Retrieval Augmented Generation for Improved Long Context Understanding](http://arxiv.org/abs/2512.17220v3)
  来源：arXiv | 日期：2025-12-19 | 相关度：2.1 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Humans understand long and complex texts by relying on a holistic semantic representation of the content. This global view helps organize prior knowledge, interpret new information, and integrate evidence dispersed acros...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [QueryFlow: Multi-Hop Graph Retrieval with Adaptive Query Evolution](http://arxiv.org/abs/2611.04625v1)
  来源：arXiv | 日期：2026-11-03 | 相关度：1.4 | 新颖度：6.46
  匹配主题：未命中具体主题
  中文摘要：Multi-hop retrieval-augmented generation (RAG) supports Web information seeking and fact verification by recovering complementary evidence across related pages within a limited retrieval budget. Scoring evidence independ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Auditing Escalation Reliability in Healthcare LLM Agents: A Perturbation-Controlled Benchmark of Workflow-State Failures](http://arxiv.org/abs/2610.21270v2)
  来源：arXiv | 日期：2026-10-15 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Trustworthy biomedical AI requires reliable action selection when evidence is missing, stale, conflicting, or late, not only accurate answers on static inputs. We instantiate an episode-level evaluation protocol as 400 s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Toward an Evidence-Based Template for Agent Instruction Files: An Empirical Study of Adoption, Consistency, and Maintenance](http://arxiv.org/abs/2611.02383v1)
  来源：arXiv | 日期：2026-11-02 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：AI coding agents rely on repository-level instruction files to understand project conventions, development workflows, and constraints. However, different agents support different instruction formats, and limited empirica...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Fairway: Load-Aware KV Cache Reuse for LLM Prefill Scheduling](http://arxiv.org/abs/2611.02082v1)
  来源：arXiv | 日期：2026-11-01 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：LLM-based applications often employ agentic workflows and retrieval-augmented generation (RAG), which build long prompts from shared context. When prefixes are shared across requests, serving engines reuse the key-value ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Constructing a Regional Slang Lexicon for Electricity Demands via Soft-Label Bidirectional Anchoring and Active Learning](http://arxiv.org/abs/2611.04231v1)
  来源：arXiv | 日期：2026-11-03 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Power-grid customer service increasingly relies on community social media, where customers describe outages, billing, and equipment faults in informal regional dialect. Such messages exhibit non-standard morphology, sema...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [When Debate Amplifies Risk: Social-Bias Vulnerabilities in Multi-Agent Safety Deliberation](http://arxiv.org/abs/2611.04289v1)
  来源：arXiv | 日期：2026-11-03 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented Web applications increasingly employ multi-agent debate (MAD) to aggregate conflicting, noisy, and heterogeneous information, yet deliberation is fundamentally a social process susceptible to interper...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Anchor: Augmented Cross-Layer Recurrent State for Long-Context Retrieval in Test-Time Training](http://arxiv.org/abs/2611.04327v1)
  来源：arXiv | 日期：2026-11-03 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Parameter-efficient linearization turns a pretrained autoregressive Transformer into an efficient model by hybridizing sliding-window attention (SWA) with a constant-size recurrent memory. But does every layer's recurren...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Retrieval-Enhanced Cultural Evaluation for Social Media Translation Training](http://arxiv.org/abs/2611.02009v1)
  来源：arXiv | 日期：2026-11-01 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Social media translation requires preserving meaning while capturing the cultural nuances of user-generated content (UGC). However, gaps in the cultural knowledge of LLM-based evaluators can lead to inaccurate assessment...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Revisiting RAG Retrievers: An Information Theoretic Benchmark](http://arxiv.org/abs/2602.21553v2)
  来源：arXiv | 日期：2026-02-25 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) systems rely critically on the retriever module to surface relevant context for large language models. Although numerous retrievers have recently been proposed, each built on differen...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [EviCast: Forecasting Retrieval Gains Through Shared Response Calibration](http://arxiv.org/abs/2611.02387v1)
  来源：arXiv | 日期：2026-11-02 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) extends large language models with external evidence, yet relevant evidence does not ensure that a generator can use it. Indiscriminate retrieval can degrade task performance while ad...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Molecular Prior Networks](http://arxiv.org/abs/2611.05103v1)
  来源：arXiv | 日期：2026-11-03 | 相关度：1.7 | 新颖度：8.16
  匹配主题：未命中具体主题
  中文摘要：Predicting affinity between small molecules and their protein targets remains one of the central problems in drug discovery. Due to the substantial cost of wet-lab experiments, machine learning models of drug-target affi...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Reliability Stress Testing of RAG Retrieval under Query-Relevant Corpus Poisoning](http://arxiv.org/abs/2611.04264v1)
  来源：arXiv | 日期：2026-11-03 | 相关度：0.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：External text can affect a retrieval-augmented generation (RAG) system only after the retriever admits it to the model context. We stress this admission step while varying document content, attacker query information, pe...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [From Scientific Observations to Mechanisms: Benchmarking Hypothesis Generation by AI Scientists](http://arxiv.org/abs/2610.05197v2)
  来源：arXiv | 日期：2026-10-04 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Data-driven mechanistic hypotheses are essential to scientific discovery because they explain how underlying processes produce observed phenomena. AI agents and AI scientists increasingly support scientific data analysis...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [From FAIR to AI-FAIR Metadata-First Infrastructure for AI-Enabled Science](http://arxiv.org/abs/2611.03327v1)
  来源：arXiv | 日期：2026-11-02 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Artificial intelligence (AI) technologies and their capabilities have advanced rapidly over the past few years, leading to widespread interest and adoption in the biological and ecological sciences. However, the data inf...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Preprocessing Choices in Fine-Tuning Data Matter: Utility and Demographic Sensitivity in LLM-Based Recommendation](http://arxiv.org/abs/2611.03113v1)
  来源：arXiv | 日期：2026-11-02 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have introduced a generative approach to recommendation, producing item lists from textual representations of user histories and item information. However, this generative setting raises chal...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Kinetics and Evolution-guided Design of High Fidelity CRISPR-Cas Endonucleases](https://www.biorxiv.org/content/10.64898/2026.07.06.736881v2)
  来源：bioRxiv | 日期：2026-11-02 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Finding high-fidelity CRISPR-Cas variants is critical for both the precision of in vitro DNA detection and the safety of in vivo gene-editing therapeutics. However, the large size of the Cas enzymes and the distinct sele...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [From DNA to drug discovery AI models for cardiovascular precision medicine.](https://pubmed.ncbi.nlm.nih.gov/42269859/)
  来源：PubMed | 日期：2026-11-01 | 相关度：4.45 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Cardiovascular diseases remain the world's leading cause of death-yet the molecular mechanisms linking genetic variation to clinical outcomes are still poorly mapped. Recent advances in artificial intelligence (AI), espe...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Physical Diffusion Policy via MPM-Guided 3D Gaussian Simulation](http://arxiv.org/abs/2611.04493v1)
  来源：arXiv | 日期：2026-11-03 | 相关度：2.05 | 新颖度：5.4
  匹配主题：foundation_model_agent
  中文摘要：Learning robust manipulation policies for diverse everyday objects remains challenging because objects with different materials exhibit distinct deformation and contact dynamics. While diffusion policies provide a powerf...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CryoQSeg: robust particle segmentation for cryo-EM with Qwen-Image-Edit.](https://pubmed.ncbi.nlm.nih.gov/42878722/)
  来源：PubMed | 日期：2026-11-01 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Accurate particle picking remains a critical step in cryo-electron microscopy (cryo-EM) single-particle analysis, and the field has witnessed the development of a broad spectrum of approaches - from classical template-ba...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CellPlex: Benchmarking Single-Cell Spatial Proteomics Prediction from H&E](http://arxiv.org/abs/2611.02506v1)
  来源：arXiv | 日期：2026-11-02 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Spatial proteomics measures tens of proteins in every cell of a tissue section, but its cost confines it to small research cohorts, whereas hematoxylin and eosin (H\&E) slides exist for nearly every patient. Inferring si...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Panoramic modelling of single-cell transcriptomes at scale with CellNet](http://arxiv.org/abs/2610.21943v2)
  来源：arXiv | 日期：2026-10-15 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Comprehensively characterizing cellular landscapes to elucidate cell diversity is a central goal in biology. Recent advances in single-cell profiling have created unprecedented opportunities for this endeavor by capturin...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AI-Driven Multiomics Biomarkers for Precision Oncology: Navigating the Translational Gap and Regulatory Hurdles.](https://pubmed.ncbi.nlm.nih.gov/42560117/)
  来源：PubMed | 日期：2026-11-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：本综述探讨了精准肿瘤学中多组学技术与人工智能（AI）的整合应用，重点关注生物标志物的发现与个性化治疗策略。研究指出，临床转化过程中面临着数据异质性、验证困难、算法偏见、监管复杂性及伦理问题等挑战。文章批判性地评估了集成化技术如何通过支持基因组学、转录组学、蛋白质组学、代谢组学和影像组学来促进精准医疗。研究团队检索了2020年至2025年间PubMed、Web of Science和Scopus数据库的相关文献，提出了一个包含多参数数据生...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SemFlowRAG: Directed Semantic Flow from Abstraction to Evidence for Complex Reasoning](http://arxiv.org/abs/2606.28447v2)
  来源：arXiv | 日期：2026-06-26 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) enhanced by Knowledge Graphs has shown promise in complex multi-hop reasoning tasks. However, existing graph-based retrieval methods typically rely on flat, undirected topologies. Dur...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Transforming one health antimicrobial resistance surveillance in resource-limited countries (RLCs): From point-of-care diagnostics to AI-driven decision support.](https://pubmed.ncbi.nlm.nih.gov/42810525/)
  来源：PubMed | 日期：2026-11-01 | 相关度：5.95 | 新颖度：0.25
  匹配主题：pathogenomics, application_monitoring
  中文摘要：Antimicrobial resistance (AMR) is a major and escalating global problem, particularly for resource-limited countries (RLCs) with limited capacity to diagnose diseases, inadequate surveillance systems, insufficient antimi...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Identifying interstitial lung disease with large language models on clinical notes and claims](https://www.medrxiv.org/content/10.64898/2026.10.30.26366942v1)
  来源：medRxiv | 日期：2026-11-02 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Interstitial lung disease (ILD) is a potentially fatal toxicity of immune checkpoint inhibitors and antibody-drug conjugates. Drug-safety studies in healthcare databases identify ILD with claims-based algorithms that tra...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Microfluidic approaches to next- generation sequencing library preparation: innovations, clinical integration and point-of-care settings.](https://pubmed.ncbi.nlm.nih.gov/42802333/)
  来源：PubMed | 日期：2026-11-01 | 相关度：4.65 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Next-generation sequencing (NGS) has revolutionized genomics by enabling high-throughput, cost-effective analysis of nucleic acids for both research and clinical use. Despite advances in sequencing technology, library pr...
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

- [Conversational Multi-Agentic Network-Driven Disease Module Identification and Drug Repurposing Prediction With ChatDRex: Platform Development Study.](https://pubmed.ncbi.nlm.nih.gov/42976355/)
  来源：PubMed | 日期：2026-11-03 | 相关度：3.05 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Repurposing approved drugs offers a time- and cost-effective alternative to traditional drug development. However, in silico prediction of repurposing candidates is challenging and requires the effective collaboration of...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Radiation-Induced Intracranial Aneurysm After Cranial Radiation Therapy: Hemodynamic Considerations in a Long-Term Glioblastoma Survivor.](https://pubmed.ncbi.nlm.nih.gov/41932648/)
  来源：PubMed | 日期：2026-01-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Long-term survival after glioblastoma (GB) remains uncommon; however, advances in genomic research and contemporary multimodal therapy have increased the number of long-term survivors. In these patients, late effects of ...
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
