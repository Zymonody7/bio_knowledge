# 每日论文监控日报 (2026-09-12)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 48 篇新论文。

## 抓取状态

- arXiv：成功，命中 34 篇
- PubMed：成功，命中 51 篇
- bioRxiv：成功，命中 11 篇
- medRxiv：成功，命中 11 篇

## 最值得看

### 产品应用 / 监测落地

- [Identification and characterisation of bacterial pathogens through Large Language Model-assisted text mining](https://www.biorxiv.org/content/10.1101/2025.07.29.667369v2)
  来源：bioRxiv | 日期：2026-09-09 | 相关度：10.0 | 新颖度：6.0
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Compiling and characterising the diversity of bacterial pathogens of humans is a critical challenge to tackle infection risk, especially in the context of global antimicrobial resistance, climate change, and changing dem...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 可追踪

### Foundation Model / Agent

- [MisEdu-RAG: A Misconception-Aware Dual-Hypergraph RAG for Novice Math Teachers](http://arxiv.org/abs/2604.04036v2)
  来源：arXiv | 日期：2026-04-05 | 相关度：6.55 | 新颖度：2.2
  匹配主题：foundation_model_agent
  中文摘要：Novice math teachers often encounter students' mistakes that are difficult to diagnose and remediate. Misconceptions are especially challenging because teachers must explain what went wrong and how to solve them. Althoug...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Designing a Robust LLM-Based Evaluation System for Agentic AI in Drug Discovery Through Human Alignment](http://arxiv.org/abs/2608.21057v2)
  来源：arXiv | 日期：2026-08-21 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Agentic large language model (LLM) systems are reshaping scientific workflows in chemistry and drug discovery, but evaluating their open-ended, tool-augmented outputs remains a fundamental bottleneck. The LLM-as-a-Judge ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ToxicRAG: Compromising Retrieval-Augmented Generation Systems via Single-Shot Knowledge Poisoning Attacks](http://arxiv.org/abs/2609.11082v1)
  来源：arXiv | 日期：2026-09-10 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) can ground large language model (LLM) outputs in external evidence, but it also exposes the system to knowledge poisoning. Representative attacks use multiple injected documents or te...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [REVA: Reusable Evidence View Aggregation for Context-Efficient RAG Serving](http://arxiv.org/abs/2609.11209v1)
  来源：arXiv | 日期：2026-09-10 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) improves knowledge-intensive large language model (LLM) applications by conditioning generation on retrieved documents, but longer contexts increase latency, key-value (KV) cache memo...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agent-driven Model Development for RNA 3D Structure Prediction](https://www.biorxiv.org/content/10.64898/2026.09.08.749228v2)
  来源：bioRxiv | 日期：2026-09-10 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language model (LLM) agents have shown promise in driving scientific discovery, but their effectiveness in complex, real-world biological problems remains underexplored. We ask whether a general-purpose LLM agent c...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Learning the Language of the Microbiome with Transformers](https://www.biorxiv.org/content/10.64898/2026.05.02.722381v4)
  来源：bioRxiv | 日期：2026-09-10 | 相关度：5.45 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：Self-supervised pretraining has become central to biological machine learning, yet microbiome data remains comparatively underexplored in terms of both modeling approaches and evaluation frameworks. To address this gap, ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Genomic language model for predicting enhancers and their allele-specific activity in the human genome.](https://pubmed.ncbi.nlm.nih.gov/42723633/)
  来源：PubMed | 日期：2026-09-10 | 相关度：5.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Predicting and deciphering the regulatory logic of enhancers remains a significant challenge due to their complex sequence features and the absence of consistent genetic or epigenetic signatures that distinguish them fro...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Accuracy Overstates Evidence Grounding and Abstention Reliability in Mammography Vision-Language Models](https://www.medrxiv.org/content/10.64898/2026.09.10.26361944v1)
  来源：medRxiv | 日期：2026-09-11 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Answer accuracy alone cannot determine whether a Vision-Language Model (VLM) relies on clinically relevant mammographic evidence or recognizes when that evidence is unavailable. We introduce an evidence-grounded selectiv...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Deep generative models in biological sequence and structure analysis and design.](https://pubmed.ncbi.nlm.nih.gov/42716354/)
  来源：PubMed | 日期：2026-09-09 | 相关度：8.5 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Deep generative models have transformed biological sequence modeling from predictive analysis toward increasingly controllable design. Early biological applications of Variational Autoencoders (VAEs) and Generative Adver...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [NeoGen-BC: A synergistic framework combining generative protein language models and multi-window deep learning for designing shared neoantigens in breast cancer.](https://pubmed.ncbi.nlm.nih.gov/42721858/)
  来源：PubMed | 日期：2026-09-09 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Breast cancer, particularly hormone receptor-positive (HR + ) and triple-negative (TNBC) subtypes, is often immunologically "cold," limiting immunotherapy efficacy. Neoantigen-based vaccines hold promise but face challen...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Sampling in structure-token space enables accurate prediction of multiple protein conformations](https://www.biorxiv.org/content/10.64898/2026.03.03.708411v3)
  来源：bioRxiv | 日期：2026-09-09 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Protein function is fundamentally mediated by ensembles of distinct metastable states. However, existing methods, such as AlphaFold 3, typically exhibit a bias toward predicting a single dominant state, failing to captur...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Context Matters in LLM-Assisted Qualitative Data Analysis: Workflow Development and Multidimensional Evaluation in Health Research](https://www.medrxiv.org/content/10.64898/2026.09.07.26362410v1)
  来源：medRxiv | 日期：2026-09-11 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly used for qualitative analysis, but strong language performance does not guarantee strong interpretation when meaning depends on method and context. We developed a context-spe...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Advancing One Health genomics in Africa: opportunities and challenges for outbreak and antimicrobial resistance control.](https://pubmed.ncbi.nlm.nih.gov/42262139/)
  来源：PubMed | 日期：2026-09-10 | 相关度：8.3 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：SUMMARYAfrica's ongoing struggles with emerging epidemics and antimicrobial resistance (AMR) underscore the urgency of integrating pathogen genomics and surveillance systems into the continent's One Health strategy, part...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Fine-Tuning Large Language Models for Structured Extraction of Infectious Disease-Related Information From Clinical Notes in Japanese Primary Care: Development and Internal Validation Study.](https://pubmed.ncbi.nlm.nih.gov/42721099/)
  来源：PubMed | 日期：2026-09-10 | 相关度：7.45 | 新颖度：0.5
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：The COVID-19 pandemic highlighted the importance of timely infectious disease surveillance. In Japan, conventional sentinel and claims-based systems incur reporting lags and capture limited clinical detail, whereas free-...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Generative model of patient health states and pan-cancer risk stratification](https://www.medrxiv.org/content/10.64898/2026.09.09.26362676v1)
  来源：medRxiv | 日期：2026-09-11 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：While large language models are powerful generators of new text, forecasting disease progression from longitudinal health histories remains a challenging problem. We introduce GenEHR, an autoregressive generative model t...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [CARRE: Counterfactual Action Retrieval and Reason Evaluation for Explainable Churn Prescription](http://arxiv.org/abs/2609.09766v2)
  来源：arXiv | 日期：2026-09-09 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Churn models typically identify high-risk customers but do not specify which feasible retention action should be considered or why that action is appropriate. We present CARRE (Counterfactual Action Retrieval and Reason ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Natural Language Access to Domain-Specific Metadata: A Reusable Framework for LLM Query Generation](http://arxiv.org/abs/2607.18029v2)
  来源：arXiv | 日期：2026-07-20 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Researchers need to answer ad-hoc questions about the contents of domain-specific archives but often lack the expertise to write structured queries on the metadata. We show that when domain vocabulary and semantics are c...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Customized large language models can outperform Community Notes in correcting misinformation](http://arxiv.org/abs/2403.11169v6)
  来源：arXiv | 日期：2024-03-17 | 相关度：6.1 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Addressing misinformation in real-world settings is challenging: content is often multimodal; factuality judgments are nuanced and context-dependent; new events emerge rapidly across domains; corrections must be timely, ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Vague2Detect: Handling Ambiguous Prompts in Knowledge-Based Open-World Detection](http://arxiv.org/abs/2609.09949v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Real-world detectors must often interpret functional or ambiguous prompts, yet conventional models such as YOLO remain restricted to fixed class lists. Even open-vocabulary models like YOLO-World frequently misalign vagu...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RAG-Safety-Bench: Reliable Evaluation of Retrieval-Augmented LLM Safety](http://arxiv.org/abs/2609.11758v1)
  来源：arXiv | 日期：2026-09-10 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Allowing large language models (LLMs) to retrieve information from a set of trusted documents can increase reliability and reduce hallucination. However, recent work has demonstrated that retrieval-augmented generation (...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LM-X: Explainable Vision--Language--Action Modeling via Progress, Event, and Uncertainty Prediction](http://arxiv.org/abs/2608.25757v4)
  来源：arXiv | 日期：2026-08-26 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large-scale vision--language--action (VLA) policies have advanced generalist robot control, yet most remain stimulus-to-action black boxes: actions are exposed, but their explanatory state is not. They provide no native ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The Answer Path and the Grounding Instruction in LLM Question Answering over Knowledge Graphs](http://arxiv.org/abs/2609.10237v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：A graph retrieval-augmented generation pipeline chooses which triples to put in the prompt, a syntax to write them in, an order to write them in, and a sentence telling the model what to do with them. We vary all four ov...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Document Silos to Process Intelligence: A Multi-Layer Knowledge Graph for CMC Process Development](http://arxiv.org/abs/2609.11493v1)
  来源：arXiv | 日期：2026-09-10 | 相关度：2.1 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Chemistry, Manufacturing and Controls (CMC) process development generates an enormous body of technical information across a multi-stage, knowledge-intensive continuum from drug discovery to commercial manufacturing. Thi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [KVShareArena: KV-Cache Reuse Across Contexts and Model Checkpoints](http://arxiv.org/abs/2609.10266v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：LLM serving systems already reuse KV caches, but only when the reused text sits at the very start of the prompt. Two growing workloads break this condition: a retrieval-augmented generation server assembles a different s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Your Retriever Already Knows: Distribution-Shape QPP for RAG Retrieval Sufficiency](http://arxiv.org/abs/2609.11646v1)
  来源：arXiv | 日期：2026-09-10 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Standard Retrieval-Augmented Generation (RAG) pipelines often provide no reliable inference-time signal of whether retrieval succeeded; on ambiguous or out-of-scope queries, generation may then hallucinate. Motivated by ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Glyph: A Multi-Strategy Agentic System for Column Description and Sensitivity-Ontology Tagging of Enterprise Data Catalogs](http://arxiv.org/abs/2609.10430v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Enterprise data lakes accumulate tables faster than human stewards can document or classify them, leaving columns with missing descriptions and unassigned governance labels. This documentation debt undermines data discov...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Novel Target Combinations in Lung Squamous Cell Carcinoma proposed by the Emet AI Research Environment and supported by discovery stage experimentation](https://www.biorxiv.org/content/10.64898/2026.09.04.749404v1)
  来源：bioRxiv | 日期：2026-09-09 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Early drug discovery is frequently bottlenecked by target identification, a challenge that becomes particularly difficult in complex diseases driven by overlapping, redundant pathways rather than a single dominant driver...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LiteRAG: Cost-Efficient Graph-Based Retrieval-Augmented Generation](http://arxiv.org/abs/2609.10239v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Graph-based retrieval can improve multi-hop question answering, but existing approaches often incur high query-time costs and produce diffuse, oversized contexts that reduce generation efficiency. We present LiteRAG, a g...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RCL: A Retrieval-Confidence Layer for Detecting Insufficient Context in Enterprise Retrieval-Augmented Code Generation](http://arxiv.org/abs/2609.11023v1)
  来源：arXiv | 日期：2026-09-10 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) for code generation has been studied extensively on public repositories, where a model's parametric knowledge often compensates for imperfect retrieval. This breaks down in enterprise...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [TimelyRAG: Semantic-Temporal Hybrid Retrieval for Time-Critical Question Answering in Overlapping-Evolving Documents](http://arxiv.org/abs/2609.11572v1)
  来源：arXiv | 日期：2026-09-10 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Although large language models (LLMs) and retrieval-augmented generation (RAG) have advanced open-domain question answering (QA), they remain unreliable when documents evolve through amendments. Existing time-sensitive r...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [MOSAIC: Query-Aware Exploration Policy Adaptation for GraphRAG](http://arxiv.org/abs/2609.11065v1)
  来源：arXiv | 日期：2026-09-10 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Graph Retrieval-Augmented Generation (GraphRAG) can connect evidence distributed across a corpus graph, but most systems use largely shared exploration procedures across queries. This creates a structural mismatch: direc...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [HyLnc: a hybrid deep learning and feature-based approach for long non-coding RNA prediction.](https://pubmed.ncbi.nlm.nih.gov/42716909/)
  来源：PubMed | 日期：2026-09-09 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Long non-coding RNAs (lncRNAs) play important roles in gene regulation, development and disease, yet accurate identification of lncRNAs from transcriptomic data remains a major computational challenge. Existing methods o...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [From Retrieval to Weights: Parametric Individualization of Small Language Models with Individual Text Corpora](http://arxiv.org/abs/2609.10155v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：We approach a cognitive simulation perspective on episodic and semantic memory in multiple-choice question answering by incorporating text from individual text corpora (ITC) into retrieval-augmented generation and DoRA f...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Guaranteeing Faithful Evidence Extraction in Speculative Retrieval-Augmented Generation](http://arxiv.org/abs/2609.10046v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：4.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) are increasingly used as interfaces for information retrieval, but they remain prone to hallucinations and faithfulness errors, in which the generated answers diverge from the retrieved evide...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Atlas: Efficient Verifiable Semantic Search](http://arxiv.org/abs/2609.11841v1)
  来源：arXiv | 日期：2026-09-10 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Semantic search is a core primitive of modern applications, powering recommender systems, web search, and retrieval-augmented generation for language models. The provider controls the index and query execution, leaving c...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AutoScreen: AI Co-Scientist System for Target Discovery in Functional Genomics](https://www.biorxiv.org/content/10.64898/2026.09.06.749678v1)
  来源：bioRxiv | 日期：2026-09-10 | 相关度：2.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：Target discovery in functional genomics remains largely manual and time-consuming, lacking systematic tools for efficient and reproducible gene-level hypothesis generation. We introduce AutoScreen, an AI co-scientist sys...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Enabling Knowledge Graph Understanding at Scale with the EXplore Your Graphs ENgine (EXYGEN)](http://arxiv.org/abs/2609.11569v1)
  来源：arXiv | 日期：2026-09-10 | 相关度：2.1 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：We present EXYGEN (EXplore Your Graphs ENgine), a framework for knowledge graph (KG) understanding that enables conversational access to KGs at scale. We address two questions in sequence. First, how effectively can LLMs...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Generative machine learning unlocks the first proteome-wide image of human cells](https://www.biorxiv.org/content/10.64898/2026.03.31.715748v3)
  来源：bioRxiv | 日期：2026-09-10 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：The spatial organization of proteins within cells governs virtually all cellular functions, yet current imaging can simultaneously visualize only tens of proteins, orders of magnitude below the thousands populating a sin...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Better Together: Complementary Query Rewriting Under a Strong RAG Baseline](http://arxiv.org/abs/2609.05637v2)
  来源：arXiv | 日期：2026-09-04 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：A popular way to improve Retrieval-Augmented Generation (RAG) is to rewrite the user's question into several variants and search with all of them. We test whether this actually helps once the underlying search is already...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Fine-Tuning a KV Cache Concatenation-Aware Model or Recomputing KV Caches? Why Not Both?](http://arxiv.org/abs/2609.09768v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：In Retrieval-Augmented Generation (RAG) systems, a large number of retrieved chunks are concatenated to form the input context so that users can receive high-quality responses based on external knowledge. As a result, th...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ICEGR: An Intent-Coherent End-to-End Generative Retrieval Framework for E-commerce Search](http://arxiv.org/abs/2608.29652v3)
  来源：arXiv | 日期：2026-08-30 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Generative Retrieval (GR) is promising for e-commerce search, yet existing methods struggle to maintain query-intent consistency throughout the training pipeline. First, semantic ID (SID) construction based on static pro...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [When do cheap embeddings beat protein language models? A theoretically-grounded hashing sketch for biological sequence classification](http://arxiv.org/abs/2512.10147v2)
  来源：arXiv | 日期：2025-12-10 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：\textbf{Motivation:} Pre-trained protein language models (PLMs) such as ESM-2 have become the default representation for biological sequence tasks, but they are computationally heavy and require GPUs both for embedding a...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Multimodal genomic surveillance for respiratory pathogens at four U.S. international airports: A comparison of air, wastewater, clinical, and national surveillance data.](https://pubmed.ncbi.nlm.nih.gov/42715246/)
  来源：PubMed | 日期：2026-01-01 | 相关度：5.0 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Early detection of outbreaks and emerging pathogens is critical for public health and global biosecurity. Airports, as major international travel hubs with dense, enclosed populations, are high-risk settings for disease ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Therapeutic melanoma vaccines: Platforms, neoantigen strategies, and emerging combination immunotherapies.](https://pubmed.ncbi.nlm.nih.gov/42724148/)
  来源：PubMed | 日期：2026-01-01 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Melanoma has emerged as a major focus of cancer immunotherapy research because of its highly immunogenic nature and responsiveness to immune-based treatments. Therapeutic melanoma vaccines are designed to stimulate tumor...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Evaluation of AI-assisted summarisation of tertiary clinical genomics reports: results of the QNOMX-VHIR-CPSP-001 Phase 1 study](https://www.medrxiv.org/content/10.64898/2026.09.10.26362656v1)
  来源：medRxiv | 日期：2026-09-11 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Background. Comprehensive genomic reports in oncology contain complex molecular information that must be translated into concise summaries for treating clinicians. Manual summarisation is time-intensive, and robust evide...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Ensembling LLMs for AI-Augmented Cybersecurity Software Requirements Generation](http://arxiv.org/abs/2609.10316v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Translating high-level controls from security standards into concrete, system-specific requirements is central to cybersecurity requirements engineering. Large language models (LLMs) can accelerate this labor-intensive, ...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [VikingRAG: Accurate and Token-efficient Retrieval-augmented Generation over Structured Documents](http://arxiv.org/abs/2609.11390v1)
  来源：arXiv | 日期：2026-09-10 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：State-of-the-art retrieval-augmented generation (RAG) methods exploit document structures to acquire sufficient evidence, but often incur substantial token costs. To reduce structural-context tokens without compromising ...
  为什么值得看：VikingRAG: Accurate and Token-efficient  与你的主题有弱匹配，暂时保留作低优先级跟踪。
