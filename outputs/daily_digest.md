# 每日论文监控日报 (2026-08-21)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 60 篇新论文。

## 抓取状态

- arXiv：成功，命中 51 篇
- PubMed：成功，命中 52 篇
- bioRxiv：成功，命中 14 篇
- medRxiv：成功，命中 10 篇

## 最值得看

### 方法创新

- [INDELVAR: structure-informed prediction of in-frame indel pathogenicity with calibrated PP3/BP4 thresholds](https://www.biorxiv.org/content/10.64898/2026.08.13.737497v1)
  来源：bioRxiv | 日期：2026-08-18 | 相关度：9.6 | 新颖度：5.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：In-frame insertions and deletions are difficult to interpret because their effects depend on both the sequence change and its protein context. We developed INDELVAR, a random forest model for in-frame insertions and dele...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [Modality-chain reasoning enables multimodal protein modelling and design](https://www.biorxiv.org/content/10.1101/2025.07.21.665832v3)
  来源：bioRxiv | 日期：2026-08-18 | 相关度：10.0 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Reasoning has emerged as a central capability of large language models, yet how it should be formulated for scientific foundation models remains unclear because scientific knowledge is distributed across interdependent, ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Autonomous biomedical research with an artificial intelligence agent.](https://pubmed.ncbi.nlm.nih.gov/42424436/)
  来源：PubMed | 日期：2026-08-20 | 相关度：8.5 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Biomedical research is increasingly constrained by repetitive, fragmented workflows that slow discovery. We introduce Biomni, a general-purpose biomedical artificial intelligence agent that autonomously executes diverse ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Reducing Technician Search Burden: A Multimodal RAG for Cessna 172 Maintenance Manual](http://arxiv.org/abs/2608.18465v1)
  来源：arXiv | 日期：2026-08-19 | 相关度：7.9 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Proper use of the aircraft maintenance manual is essential for correct maintenance, providing procedures, diagrams, cautions, and specifications. However, technicians often avoid consulting it because it is difficult to ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Artificial intelligence agents and agentic artificial intelligence applied to precision medicine.](https://pubmed.ncbi.nlm.nih.gov/42617946/)
  来源：PubMed | 日期：2026-08-19 | 相关度：7.8 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Precision medicine seeks to individualise care by integrating multimodal biomedical data, yet most deployed clinical artificial intelligence (AI) remains assistive, providing predictions without managing workflows or ada...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Comprehensive Review of Large Language Models for Nanophotonics: From Surrogate Modeling to Autonomous Design](http://arxiv.org/abs/2608.18279v1)
  来源：arXiv | 日期：2026-08-18 | 相关度：7.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Metasurfaces have revolutionized the development of photonic devices by enabling unprecedented precision in light manipulation. However, their design processes are often constrained by computationally expensive simulatio...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TTSD-FAR: Test-Time Self-Distillation with Fisher-Anchored Restoration for Missing-Modality Emotion Recognition in LVLMs](http://arxiv.org/abs/2608.18386v1)
  来源：arXiv | 日期：2026-08-18 | 相关度：7.5 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large video-language models (LVLMs) have shown remarkable performance on multimodal tasks like multimodal emotion recognition (ER) in the wild. ER is inherently multimodal, requiring a joint understanding of facial expre...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Large Language Models Generate Stigmatizing Language During Reasoning Over Real-World Clinical Data](https://www.medrxiv.org/content/10.64898/2026.08.12.26360210v2)
  来源：medRxiv | 日期：2026-08-19 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Stigmatizing language in clinical documentation, which conveys negative stereotypes, attitudes, or judgments toward patients, is a recognized source of documentation bias and is associated with poorer care and adverse he...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BCIJelly: An integrated ecosystem for brain-computer interface research](https://www.biorxiv.org/content/10.64898/2026.08.13.744531v1)
  来源：bioRxiv | 日期：2026-08-18 | 相关度：6.55 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：Brain-computer interface (BCI) research relies on multistage computational pipelines, but progress has been slowed by fragmented data formats, heterogeneous decoder implementations and hardware-specific deployment toolch...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ReasFlow: Assisting Reasoning-Centric Scientific Discovery in Applied Mathematics via a Knowledge-Based Multi-Agent System](http://arxiv.org/abs/2607.14178v3)
  来源：arXiv | 日期：2026-07-15 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in Large Language Models have fueled autonomous AI agents capable of tackling complex scientific tasks, yet existing automated research systems remain predominantly focused on empirically driven domains w...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PG-LLM: Benchmarking General-Purpose Language Models for Protein Variant Ranking](https://www.biorxiv.org/content/10.64898/2026.07.27.741045v3)
  来源：bioRxiv | 日期：2026-08-19 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：General-purpose frontier language models are being increasingly utilized for protein-design work, yet their ability to understand and evaluate variant effects remains unclear. Here, we introduce PG-LLM, a benchmark compr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Training-Free LLM-Based Recommendation with Post-LLM Item Refinement Using Collaborative Signals](http://arxiv.org/abs/2608.19665v1)
  来源：arXiv | 日期：2026-08-20 | 相关度：5.45 | 新颖度：6.57
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have shown promise for training-free recommendation, but LLM-generated user interests are often too broad for fine-grained item retrieval. Existing methods incorporate collaborative filtering...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Toward Greater Autonomy in Materials Discovery Agents: Unifying Planning, Physics, and Scientists](http://arxiv.org/abs/2506.05616v3)
  来源：arXiv | 日期：2025-06-05 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：We aim at designing language agents with greater autonomy for crystal materials discovery. While most of existing studies restrict the agents to perform specific tasks within predefined workflows, we aim to automate work...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Automated Summarization of Financial News Using Large Language Models and Retrieval-Augmented Generation: An Early Empirical Study (Fall 2023)](http://arxiv.org/abs/2608.19526v1)
  来源：arXiv | 日期：2026-08-20 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Stock market analysts and investors face a daily challenge: too much financial news, too little time. Manually reading and synthesizing hundreds of company-specific articles is impractical, yet missing key information ca...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EchoTrace: Diagnosing Recursive Risks in LLM-Powered Recommender Systems](http://arxiv.org/abs/2602.07442v2)
  来源：arXiv | 日期：2026-02-07 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly integrated into recommender systems as data augmenters, profile generators, and recommendation modules. While these roles can enhance semantic understanding and recommendatio...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [MTS-Bench: A Manchester Triage System Benchmark for Language Model Triage Safety](https://www.medrxiv.org/content/10.64898/2026.08.04.26359651v2)
  来源：medRxiv | 日期：2026-08-18 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：BackgroundGeneral purpose language models such as ChatGPT are increasingly used by physicians and triage nurses during emergency triage. A recent study reported 51.6% undertriage of emergencies when patients queried Chat...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [ArkEval: Benchmarking and Evaluating Automated CodeRepair for ArkTS](http://arxiv.org/abs/2602.08866v2)
  来源：arXiv | 日期：2026-02-09 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models have transformed code generation, enabling unprecedented automation in software development. As mobile ecosystems evolve, HarmonyOS has emerged as a critical platform requiring robust development to...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Single-cell foundation models benefit from cross-modal training: adding proteomics data beats parameter scaling](https://www.biorxiv.org/content/10.64898/2026.08.14.744845v1)
  来源：bioRxiv | 日期：2026-08-19 | 相关度：3.75 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：Leading cellular foundation models have been trained on hundreds of millions of single-cell transcriptomes, with progress increasingly driven by larger datasets and model scaling. Here, we asked whether adding a proteomi...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Retrieval-Augmented Large Language Models for Clinically Aligned Adverse Event Coding in Acute Myeloid Leukemia Clinical Trials](https://www.medrxiv.org/content/10.64898/2026.08.17.26360282v1)
  来源：medRxiv | 日期：2026-08-18 | 相关度：7.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：BackgroundAdverse event (AE) coding is essential for safety monitoring in oncology clinical trials, particularly in acute myeloid leukemia (AML), where intensive therapies are associated with frequent and heterogeneous t...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GridCodex: A RAG-Driven AI Framework for Power Grid Code Reasoning and Compliance](http://arxiv.org/abs/2508.12682v2)
  来源：arXiv | 日期：2025-08-18 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：The global shift towards renewable energy presents unprecedented challenges for the electricity industry, making regulatory reasoning and compliance increasingly vital. Grid codes, the regulations governing grid operatio...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Assessing the Reliability of LLM-Generated Phenotype-Genotype Associations Through External Validation](https://www.biorxiv.org/content/10.64898/2026.08.13.744701v1)
  来源：bioRxiv | 日期：2026-08-18 | 相关度：7.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Background: Phenotype-genotype associations underpin precision medicine by enabling disease prevention, early diagnosis, risk stratification, therapeutic target discovery, and personalized treatment. However, the rapid g...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Integrated evaluation of rapid diagnostic testing, genotypic-phenotypic resistance profiling, and AI-Assisted prediction models for antimicrobial stewardship and clinical outcomes in a resource-limited setting.](https://pubmed.ncbi.nlm.nih.gov/42623344/)
  来源：PubMed | 日期：2026-01-01 | 相关度：4.4 | 新颖度：5.25
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：Antimicrobial resistance (AMR) remains a major global health concern, necessitating timely and accurate diagnostic approaches to guide appropriate therapy. Conventional antibiotic susceptibility testing (AST) is often as...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [TrustRAG: Blockchain-Enhanced RAG via Committee-Based Credibility Scoring](http://arxiv.org/abs/2608.20097v1)
  来源：arXiv | 日期：2026-08-20 | 相关度：4.75 | 新颖度：7.24
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) lets Large Language Models (LLMs) pull in up-to-date, domain-specific information instead of relying only on what they were trained on. Yet most RAG systems still draw from centralize...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [From Retrieved Context to Runtime Control: Adaptive Compression for Edge-based RAG](http://arxiv.org/abs/2608.19535v1)
  来源：arXiv | 日期：2026-08-20 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) improves language-model responses by grounding generation in external passages, which comes with overhead: retrieved context lengthens the prompt, increasing prefill work, KV-cache fo...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [MITRE-SAGE: A Multi-Agent Cybersecurity Question-Answering Model](http://arxiv.org/abs/2608.16921v2)
  来源：arXiv | 日期：2026-08-03 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Effective cybersecurity operations require timely and accurate analysis of large-scale heterogeneous security information; however, analysts increasingly struggle with information overload, alert fatigue, and time-constr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SGHA: Evidence-Grounded Research Problem Discovery with Local Language Models](http://arxiv.org/abs/2608.17501v1)
  来源：arXiv | 日期：2026-08-18 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Recent efforts toward fully automated AI scientists have demonstrated that language-model agents can generate hypotheses, execute experiments, and draft scientific manuscripts. However, during the early stages of researc...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Do Large Language Models Play Six Degrees of Separation? Measuring Topological Compression in Long-Context Manifolds](http://arxiv.org/abs/2608.17950v1)
  来源：arXiv | 日期：2026-08-18 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) demonstrate remarkable multi-hop reasoning capabilities over long contexts, yet the internal mechanisms enabling these distant cognitive leaps remain poorly understood. Traditional attention-...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Self-Reported Side Effects Among Reddit Users Taking Nonapproved Retatrutide](https://www.medrxiv.org/content/10.64898/2026.05.28.26352819v2)
  来源：medRxiv | 日期：2026-08-18 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Gray-market retatrutide use is increasing, but patient safety experiences remain poorly characterized. This cross-sectional analysis examined Reddit posts and comments from retatrutide-specific and broader peptide or wei...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Storage to Access: Verifiable Activation of Parametric Knowledge in LLMs via Explicit Priming and Implicit Reasoning](http://arxiv.org/abs/2608.18581v1)
  来源：arXiv | 日期：2026-08-19 | 相关度：4.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Although Large Language Models (LLMs) encode rich factual knowledge in their parameters, reliably recalling and verifying such knowledge remains a key bottleneck in factual question answering. Existing end-to-end methods...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LODESTAR: Robust Entropy-Based Answer Selection in Retrieval-Augmented Generation for Question Answering -- Directing Frozen-LLM Entropy with a Reinforcement-Learned Prompt Polarizer under Misleading Passages](http://arxiv.org/abs/2608.11922v2)
  来源：arXiv | 日期：2026-08-12 | 相关度：2.75 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Predictive-distribution entropy is a strong answer-selection rule in retrieval-augmented generation (RAG) for question answering: across five QA benchmarks, selecting the answer a frozen respondent LLM produces with the ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [H$^{2}$MT: Semantic Hierarchy-Aware Hierarchical Memory Transformer](http://arxiv.org/abs/2605.24930v2)
  来源：arXiv | 日期：2026-05-24 | 相关度：2.75 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Transformer-based LLMs achieve strong results on many language tasks; however, long inputs remain challenging because context windows are finite, and prefill latency and memory grow rapidly with prompt length. Flat token...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Memory Centric Power Allocation for Multi-Agent Embodied Question Answering](http://arxiv.org/abs/2604.17810v2)
  来源：arXiv | 日期：2026-04-20 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：This paper considers multi-agent embodied question answering (MA-EQA), which enables robot teams to answer queries based on their long-horizon observations. In contrast to existing edge resource management methods that o...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CanLegalRAGBench: Evaluating Retrieval-Augmented Generation on Canadian Case Law](http://arxiv.org/abs/2605.30497v2)
  来源：arXiv | 日期：2026-05-28 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：RAG-based legal assistants have been growing in popularity, but LLM hallucinations remain a key issue and potentially undermines justice. While benchmarks have been developed to evaluate progress, many rely on synthetic ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Mechanist: AI as a Scientific Instrument for Discovering the Mechanisms of Intelligence](http://arxiv.org/abs/2608.12036v2)
  来源：arXiv | 日期：2026-08-12 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：AI models have achieved remarkable success across diverse domains, yet the mechanisms underlying their capabilities and the risks they may pose remain poorly understood. As AI development becomes faster and increasingly ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CTIFoundry: An Agent-Native Corpus Scaffold for Cyber Threat Intelligence](http://arxiv.org/abs/2608.18613v1)
  来源：arXiv | 日期：2026-08-19 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Cyber threat intelligence (CTI) is increasingly consumed not by human analysts but by LLM agents that compose multi-step investigations at query time. The harness side of this shift has matured rapidly (planning loops, t...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CABLE: Extending the Reach of Memory Retrieval via Complementary Antecedent-Based Linking and Expansion](http://arxiv.org/abs/2608.17911v1)
  来源：arXiv | 日期：2026-08-18 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：As LLM agents operate across structured workflows and sessions, preserving long-term history does not ensure that later contexts can recover relevant evidence through a bounded memory interface. We study this evidence-re...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [GEqTrain: A Configuration-Driven Framework for Retargeting Equivariant Graph Neural Networks Across 3D Scientific Tasks](http://arxiv.org/abs/2607.19083v3)
  来源：arXiv | 日期：2026-07-21 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Equivariant graph neural networks provide a powerful modeling language for three-dimensional scientific data, but their reuse is often limited by implementations tied to specific tasks, outputs, and training regimes. We ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Event-Causal RAG: A Retrieval-Augmented Generation Framework for Long Video Reasoning in Complex Scenarios](http://arxiv.org/abs/2605.06185v2)
  来源：arXiv | 日期：2026-05-07 | 相关度：4.75 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Large vision-language models perform well on short- and medium-length video understanding but still struggle to maintain coherent event memory and recover long-range relationships in ultra-long videos. End-to-end methods...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [SINDI: An Efficient Index for Sparse Vector Approximate Maximum Inner Product Search](http://arxiv.org/abs/2509.08395v4)
  来源：arXiv | 日期：2025-09-10 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Sparse vector Maximum Inner Product Search (MIPS) is crucial in multi-path retrieval for Retrieval-Augmented Generation (RAG). Recent inverted index-based and graph-based algorithms have achieved high search accuracy wit...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Scientific Data Skills: Enabling Agent-Ready Scientific Data Services at Scale](http://arxiv.org/abs/2608.19625v1)
  来源：arXiv | 日期：2026-08-20 | 相关度：0.7 | 新颖度：6.56
  匹配主题：未命中具体主题
  中文摘要：Scientific data are increasingly used by AI agents, yet existing dataset representations provide limited support for autonomous discovery, interpretation, and invocation. This limitation stems from the fragmentation of s...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [MissDiag: Diagnostic Evaluation of Incomplete-Knowledge Robustness in KGQA and KG-RAG](http://arxiv.org/abs/2608.18489v1)
  来源：arXiv | 日期：2026-08-19 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Knowledge graph question answering (KGQA) and knowledge-graph-based retrieval-augmented generation (KG-RAG) aim to ground answers in explicit graph evidence, but real-world knowledge graphs are often sparse, outdated, an...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Off-Manifold Collapse in Guided Protein Language Models](http://arxiv.org/abs/2608.18597v1)
  来源：arXiv | 日期：2026-08-19 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Protein language models are widely used priors for protein sequence design, and a growing body of work controls them at inference time as an alternative to fine-tuning. Such guidance faces a dilemma: mild enough to prese...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Learning What to Fail On: Failure-Mode Contextual Bandits for Adversarial Data Curation](http://arxiv.org/abs/2608.18681v1)
  来源：arXiv | 日期：2026-08-19 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：We introduce a failure-aware adversarial retrieval-augmented framework for improving robustness in natural language understanding. Rather than selecting synthetic examples with a fixed reward threshold, our method formul...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [An Agentic RAG and Evaluation Framework for Assurance Case Generation: Industrial Use Case for the EU Cyber Resilience Act Compliance](http://arxiv.org/abs/2608.19509v1)
  来源：arXiv | 日期：2026-08-19 | 相关度：2.05 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Complying with the EU Cyber Resilience Act (CRA) is a resource-intensive challenge for SMEs due to the complexity of cybersecurity conformity assessment. Yet, it is essential for demonstrating regulatory compliance and e...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Multimodal cell communication networks nominate immunotherapies for RCC subgroups with discrete T cell recruitment or expansion](https://www.biorxiv.org/content/10.64898/2026.08.17.744644v1)
  来源：bioRxiv | 日期：2026-08-18 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Renal cell carcinoma (RCC) is amongst the most immune-infiltrated solid tumours, but only a small subset of patients achieves durable response to immune checkpoint blockade therapy. Efforts to characterize the immune mic...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Parametric Knowledge in RAG-SFT for Domain-Specific Document Generation](http://arxiv.org/abs/2603.23047v2)
  来源：arXiv | 日期：2026-03-24 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) fine-tuning has shown substantial improvements over vanilla RAG, yet most studies target document question answering, leaving open whether these gains transfer to specialized tasks. W...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Predicting the Benefit of Retrieval Augmentation in Open-Domain Question Answering](http://arxiv.org/abs/2604.07985v3)
  来源：arXiv | 日期：2026-04-09 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：While retrieval augmented generation has become a common approach for enhancing question answering systems, retrieval is not universally advantageous. We study the problem of predicting whether incorporating external ret...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CLAIR-Fin: An Adversarial Multi-Agent Framework for Claim-Level Verification and Adaptive Debate in Cross-Modal Financial QA](http://arxiv.org/abs/2608.13706v2)
  来源：arXiv | 日期：2026-08-13 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Existing defenses against hallucination in retrieval-augmented and multi-agent pipelines remain partial: evidence is trusted despite modality disagreement, debate verifies an aggregate report rather than individual claim...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Bootstrap Theory of Representational Emergence (TBER): Explanatory Insufficiency, Transition Regimes, and the Emergence of New Representational Levels](http://arxiv.org/abs/2606.07303v4)
  来源：arXiv | 日期：2026-06-05 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Representation learning is central to modern machine learning, yet most research focuses on optimizing representations after a framework has been selected. The Bootstrap Theory of Representational Emergence (TBER) addres...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CoAL-RAG: A Complexity-Aware Legal Retrieval-Augmented Generation Method](http://arxiv.org/abs/2608.17536v1)
  来源：arXiv | 日期：2026-08-18 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Legal consultation questions exhibit multi-level complexity. A single retrieval strategy often leads to over-reasoning for simple questions and poor interpretability for complex ones, making it difficult to meet the requ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SAKE: Structured Agentic Knowledge Extrapolation for Complex LLM Reasoning via Reinforcement Learning](http://arxiv.org/abs/2505.15062v6)
  来源：arXiv | 日期：2025-05-21 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Knowledge extrapolation is the process of inferring novel information by combining and extending existing knowledge that is explicitly available. It is essential for solving complex questions in specialized domains where...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MERIT: Efficient In-Place Deletion for Dynamic Graph-Based Approximate Nearest Neighbor Indexes](http://arxiv.org/abs/2607.29173v3)
  来源：arXiv | 日期：2026-07-31 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Graph-based indexes have become the dominant approach to approximate nearest neighbor search (ANNS) over high-dimensional data and play a crucial role in real-world applications such as retrieval-augmented generation, re...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [How Do Agents Fail on AutoResearch: End-to-End Diagnostic Evaluation on 100 Real-World Frontier Research Tasks](http://arxiv.org/abs/2608.14905v2)
  来源：arXiv | 日期：2026-08-14 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：AI has long assisted scientific research, but the rapid advance of LLMs and agentic scaffolds is reshaping the landscape; a single system can now carry whole-stage research from an initial hypothesis all the way to final...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [An injection-molded focal filter-integrated AI platform for cost-effective and highly sensitive molecular point-of-care testing.](https://pubmed.ncbi.nlm.nih.gov/42610358/)
  来源：PubMed | 日期：2026-08-18 | 相关度：2.7 | 新颖度：0.25
  匹配主题：pathogenomics
  中文摘要：The growing global demand for precise and accessible diagnostics underscores the need for decentralized, laboratory-grade molecular testing solutions. Current platforms are hindered by the high cost and fragility of glas...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Research progress of AI assisted nano-SERS technology in rapid identification of multi species oral pathogenic biofilms.](https://pubmed.ncbi.nlm.nih.gov/42613464/)
  来源：PubMed | 日期：2026-08-19 | 相关度：2.45 | 新颖度：0.75
  匹配主题：application_monitoring
  中文摘要：Complex multispecies microbial communities that are oral pathogenic biofilms are linked to significant oral infections, such as dental caries, periodontitis, peri-implantitis, and chronic endodontic infection. In order t...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [COMA: A Compositional Misleading Attack Class on Security-RAG, and a Causal Counterfactual Defense](http://arxiv.org/abs/2608.17960v1)
  来源：arXiv | 日期：2026-08-18 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Every document a security copilot retrieves can be true, instruction-free, and non-contradictory --- and the copilot can still be driven to assess a critical, exploitable vulnerability correctly and then recommend a reme...
  为什么值得看：COMA: A Compositional Misleading Attack  与你的主题有弱匹配，暂时保留作低优先级跟踪。

- [What Makes a Good Fiqh Retriever? Answer Retrieval for Arabic Islamic Jurisprudence](http://arxiv.org/abs/2608.20246v1)
  来源：arXiv | 日期：2026-08-20 | 相关度：0.7 | 新颖度：7.6
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation is used for Islamic question answering, but most systems are evaluated end-to-end, making retrieval failures difficult to isolate from generation failures. We study answer-bearing retrieval...
  为什么值得看：What Makes a Good Fiqh Retriever? Answer 与你的主题有弱匹配，暂时保留作低优先级跟踪。

- [GRIP: Grounded Reasoning via Information-Restricted Premises](http://arxiv.org/abs/2608.16776v2)
  来源：arXiv | 日期：2026-08-17 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：High-capacity encoders in retrieval-augmented generation (RAG) can let the query dominate the latent state, leaving retrieved evidence functionally irrelevant. We call this failure mode query dominance. To address it, we...
  为什么值得看：GRIP: Grounded Reasoning via Information 与你的主题有弱匹配，暂时保留作低优先级跟踪。

- [Preference Is Not Intervention: The Structure and Stability Boundaries of Reader-Specific Evidence Utility](http://arxiv.org/abs/2608.17781v1)
  来源：arXiv | 日期：2026-08-18 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：ML systems increasingly condition decisions on downstream model identity, but this is useful only if model-specific differences form reusable structure rather than input-local interactions. We test this in retrieval-augm...
  为什么值得看：Preference Is Not Intervention: The Stru 与你的主题有弱匹配，暂时保留作低优先级跟踪。

- [Quo Vadis? Scientific Discovery in the Age of Artificial Intelligence](http://arxiv.org/abs/2608.17970v1)
  来源：arXiv | 日期：2026-08-18 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：This paper examines the growing role of AI in scientific discovery. It first surveys the rapid rise of AI capabilities, especially in reasoning, abstraction, planning, and long-horizon task execution, before turning to s...
  为什么值得看：Quo Vadis? Scientific Discovery in the A 与你的主题有弱匹配，暂时保留作低优先级跟踪。
