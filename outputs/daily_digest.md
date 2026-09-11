# 每日论文监控日报 (2026-09-11)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 46 篇新论文。

## 抓取状态

- arXiv：成功，命中 44 篇
- PubMed：成功，命中 70 篇
- bioRxiv：失败，命中 0 篇，错误：Expecting value: line 1 column 1 (char 0)
- medRxiv：失败，命中 0 篇，错误：Expecting value: line 1 column 1 (char 0)

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [Structure-based Transfer Learning](http://arxiv.org/abs/2609.08487v1)
  来源：arXiv | 日期：2026-09-08 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Transfer learning improves estimation in a target study using information from related sources. Classical transfer learning is typically data-based, requiring access to the source data or to a model fitted on them. Neith...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MisEdu-RAG: A Misconception-Aware Dual-Hypergraph RAG for Novice Math Teachers](http://arxiv.org/abs/2604.04036v2)
  来源：arXiv | 日期：2026-04-05 | 相关度：6.55 | 新颖度：7.2
  匹配主题：foundation_model_agent
  中文摘要：Novice math teachers often encounter students' mistakes that are difficult to diagnose and remediate. Misconceptions are especially challenging because teachers must explain what went wrong and how to solve them. Althoug...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [REVA: Reusable Evidence View Aggregation for Context-Efficient RAG Serving](http://arxiv.org/abs/2609.11209v1)
  来源：arXiv | 日期：2026-09-10 | 相关度：6.55 | 新颖度：6.89
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) improves knowledge-intensive large language model (LLM) applications by conditioning generation on retrieved documents, but longer contexts increase latency, key-value (KV) cache memo...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Designing a Robust LLM-Based Evaluation System for Agentic AI in Drug Discovery Through Human Alignment](http://arxiv.org/abs/2608.21057v2)
  来源：arXiv | 日期：2026-08-21 | 相关度：6.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Agentic large language model (LLM) systems are reshaping scientific workflows in chemistry and drug discovery, but evaluating their open-ended, tool-augmented outputs remains a fundamental bottleneck. The LLM-as-a-Judge ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ToxicRAG: Compromising Retrieval-Augmented Generation Systems via Single-Shot Knowledge Poisoning Attacks](http://arxiv.org/abs/2609.11082v1)
  来源：arXiv | 日期：2026-09-10 | 相关度：6.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) can ground large language model (LLM) outputs in external evidence, but it also exposes the system to knowledge poisoning. Representative attacks use multiple injected documents or te...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Using Reward Uncertainty to Induce Diverse Behaviour in Reinforcement Learning](http://arxiv.org/abs/2606.03962v2)
  来源：arXiv | 日期：2026-06-02 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Classical reinforcement learning (RL) typically seeks a deterministic policy that maximizes the expected sum of a scalar reward. Yet, modern applications such as language model fine-tuning or scientific discovery demand ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TianoForge: An Automated Bug Triage Approach for the TianoCore UEFI Firmware Development Community](http://arxiv.org/abs/2608.23259v2)
  来源：arXiv | 日期：2026-08-24 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：We propose a novel approach to bug triage in the TianoCore open-source UEFI firmware development ecosystem. This integrated approach, called TianoForge, deploys the state of the art in artificial intelligence, specifical...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CARRE: Counterfactual Action Retrieval and Reason Evaluation for Explainable Churn Prescription](http://arxiv.org/abs/2609.09766v2)
  来源：arXiv | 日期：2026-09-09 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Churn models typically identify high-risk customers but do not specify which feasible retention action should be considered or why that action is appropriate. We present CARRE (Counterfactual Action Retrieval and Reason ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Natural Language Access to Domain-Specific Metadata: A Reusable Framework for LLM Query Generation](http://arxiv.org/abs/2607.18029v2)
  来源：arXiv | 日期：2026-07-20 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Researchers need to answer ad-hoc questions about the contents of domain-specific archives but often lack the expertise to write structured queries on the metadata. We show that when domain vocabulary and semantics are c...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Customized large language models can outperform Community Notes in correcting misinformation](http://arxiv.org/abs/2403.11169v6)
  来源：arXiv | 日期：2024-03-17 | 相关度：6.1 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Addressing misinformation in real-world settings is challenging: content is often multimodal; factuality judgments are nuanced and context-dependent; new events emerge rapidly across domains; corrections must be timely, ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RAG-Safety-Bench: Reliable Evaluation of Retrieval-Augmented LLM Safety](http://arxiv.org/abs/2609.11758v1)
  来源：arXiv | 日期：2026-09-10 | 相关度：5.45 | 新颖度：7.72
  匹配主题：foundation_model_agent
  中文摘要：Allowing large language models (LLMs) to retrieve information from a set of trusted documents can increase reliability and reduce hallucination. However, recent work has demonstrated that retrieval-augmented generation (...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [TimelyRAG: Semantic-Temporal Hybrid Retrieval for Time-Critical Question Answering in Overlapping-Evolving Documents](http://arxiv.org/abs/2609.11572v1)
  来源：arXiv | 日期：2026-09-10 | 相关度：4.75 | 新颖度：7.12
  匹配主题：foundation_model_agent
  中文摘要：Although large language models (LLMs) and retrieval-augmented generation (RAG) have advanced open-domain question answering (QA), they remain unreliable when documents evolve through amendments. Existing time-sensitive r...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Deep generative models in biological sequence and structure analysis and design.](https://pubmed.ncbi.nlm.nih.gov/42716354/)
  来源：PubMed | 日期：2026-09-09 | 相关度：8.5 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Deep generative models have transformed biological sequence modeling from predictive analysis toward increasingly controllable design. Early biological applications of Variational Autoencoders (VAEs) and Generative Adver...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [NeoGen-BC: A synergistic framework combining generative protein language models and multi-window deep learning for designing shared neoantigens in breast cancer.](https://pubmed.ncbi.nlm.nih.gov/42721858/)
  来源：PubMed | 日期：2026-09-09 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Breast cancer, particularly hormone receptor-positive (HR + ) and triple-negative (TNBC) subtypes, is often immunologically "cold," limiting immunotherapy efficacy. Neoantigen-based vaccines hold promise but face challen...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Atlas: Efficient Verifiable Semantic Search](http://arxiv.org/abs/2609.11841v1)
  来源：arXiv | 日期：2026-09-10 | 相关度：4.75 | 新颖度：7.69
  匹配主题：foundation_model_agent
  中文摘要：Semantic search is a core primitive of modern applications, powering recommender systems, web search, and retrieval-augmented generation for language models. The provider controls the index and query execution, leaving c...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Advancing One Health genomics in Africa: opportunities and challenges for outbreak and antimicrobial resistance control.](https://pubmed.ncbi.nlm.nih.gov/42262139/)
  来源：PubMed | 日期：2026-09-10 | 相关度：8.3 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：SUMMARYAfrica's ongoing struggles with emerging epidemics and antimicrobial resistance (AMR) underscore the urgency of integrating pathogen genomics and surveillance systems into the continent's One Health strategy, part...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Fine-Tuning Large Language Models for Structured Extraction of Infectious Disease-Related Information From Clinical Notes in Japanese Primary Care: Development and Internal Validation Study.](https://pubmed.ncbi.nlm.nih.gov/42721099/)
  来源：PubMed | 日期：2026-09-10 | 相关度：7.45 | 新颖度：5.5
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：The COVID-19 pandemic highlighted the importance of timely infectious disease surveillance. In Japan, conventional sentinel and claims-based systems incur reporting lags and capture limited clinical detail, whereas free-...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [When do cheap embeddings beat protein language models? A theoretically-grounded hashing sketch for biological sequence classification](http://arxiv.org/abs/2512.10147v2)
  来源：arXiv | 日期：2025-12-10 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：\textbf{Motivation:} Pre-trained protein language models (PLMs) such as ESM-2 have become the default representation for biological sequence tasks, but they are computationally heavy and require GPUs both for embedding a...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Vague2Detect: Handling Ambiguous Prompts in Knowledge-Based Open-World Detection](http://arxiv.org/abs/2609.09949v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Real-world detectors must often interpret functional or ambiguous prompts, yet conventional models such as YOLO remain restricted to fixed class lists. Even open-vocabulary models like YOLO-World frequently misalign vagu...
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

- [Do LLMs Make More Mistakes If They Do Not Believe the Input Data?](http://arxiv.org/abs/2609.09363v1)
  来源：arXiv | 日期：2026-09-08 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are prone to hallucinating or misinterpreting facts, which impairs their usability in retrieval-augmented generation or data-to-text systems. We analyse how faithfulness of LLMs to provided c...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic AI-enabled Semantic Commissioning of a Cognitive Digital Twin for Reconfigurable Manufacturing](http://arxiv.org/abs/2609.09503v1)
  来源：arXiv | 日期：2026-09-08 | 相关度：2.5 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Rapid bespoke commissioning of the Cognitive Digital Twin (CDT) is a major challenge in reconfigurable manufacturing. Traditional digital twin (DT) construction methods primarily focus on geometric reconstruction, often ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Central Dogma Transformer II: An AI Microscope for Understanding Cellular Regulatory Mechanisms](http://arxiv.org/abs/2602.08751v4)
  来源：arXiv | 日期：2026-02-09 | 相关度：2.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Motivation: Interpretability is not optional in biology: understanding gene regulation requires models whose learned structure can be directly interrogated, not merely accurate predictors whose internals resist mapping o...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Document Silos to Process Intelligence: A Multi-Layer Knowledge Graph for CMC Process Development](http://arxiv.org/abs/2609.11493v1)
  来源：arXiv | 日期：2026-09-10 | 相关度：2.1 | 新颖度：6.94
  匹配主题：未命中具体主题
  中文摘要：Chemistry, Manufacturing and Controls (CMC) process development generates an enormous body of technical information across a multi-stage, knowledge-intensive continuum from drug discovery to commercial manufacturing. Thi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Your Retriever Already Knows: Distribution-Shape QPP for RAG Retrieval Sufficiency](http://arxiv.org/abs/2609.11646v1)
  来源：arXiv | 日期：2026-09-10 | 相关度：1.4 | 新颖度：7.5
  匹配主题：未命中具体主题
  中文摘要：Standard Retrieval-Augmented Generation (RAG) pipelines often provide no reliable inference-time signal of whether retrieval succeeded; on ambiguous or out-of-scope queries, generation may then hallucinate. Motivated by ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DoGMA: A Central-Dogma-Guided Foundation Model for Multi-Omics Alignment and Multi-Task Learning in Oncology](http://arxiv.org/abs/2608.08148v2)
  来源：arXiv | 日期：2026-08-08 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Attention mechanisms have been widely utilized in modern deep learning, and many existing multi-omics models inherit their conventional use to allow unrestricted bidirectional interactions. However, the fundamental logic...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [KVShareArena: KV-Cache Reuse Across Contexts and Model Checkpoints](http://arxiv.org/abs/2609.10266v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：LLM serving systems already reuse KV caches, but only when the reused text sits at the very start of the prompt. Two growing workloads break this condition: a retrieval-augmented generation server assembles a different s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Glyph: A Multi-Strategy Agentic System for Column Description and Sensitivity-Ontology Tagging of Enterprise Data Catalogs](http://arxiv.org/abs/2609.10430v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Enterprise data lakes accumulate tables faster than human stewards can document or classify them, leaving columns with missing descriptions and unassigned governance labels. This documentation debt undermines data discov...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RCL: A Retrieval-Confidence Layer for Detecting Insufficient Context in Enterprise Retrieval-Augmented Code Generation](http://arxiv.org/abs/2609.11023v1)
  来源：arXiv | 日期：2026-09-10 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) for code generation has been studied extensively on public repositories, where a model's parametric knowledge often compensates for imperfect retrieval. This breaks down in enterprise...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LiteRAG: Cost-Efficient Graph-Based Retrieval-Augmented Generation](http://arxiv.org/abs/2609.10239v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Graph-based retrieval can improve multi-hop question answering, but existing approaches often incur high query-time costs and produce diffuse, oversized contexts that reduce generation efficiency. We present LiteRAG, a g...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Muscle Memory for Agents: Compile not Merely Retrieve](http://arxiv.org/abs/2608.08995v2)
  来源：arXiv | 日期：2026-08-10 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Memory for LLM agents has converged on a single architectural pattern: store experience as text, embeddings, reflections, or rules; retrieve at inference time; let a general-purpose orchestrator interpret what to do. Thi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ReCite: Agentic Reasoning for Faithful Citation](http://arxiv.org/abs/2609.09156v1)
  来源：arXiv | 日期：2026-09-08 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Accurate citations are the foundation of academic writing, tracing intellectual origins and substantiating core claims. However, manually navigating the growing volume of scientific literature is increasingly difficult, ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [MOSAIC: Query-Aware Exploration Policy Adaptation for GraphRAG](http://arxiv.org/abs/2609.11065v1)
  来源：arXiv | 日期：2026-09-10 | 相关度：0.7 | 新颖度：5.75
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

- [Reproducing Omitted Temporal Expressions in Japanese News for Retrieval-Augmented Applications](http://arxiv.org/abs/2609.09569v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：News articles often contain omitted temporal expressions, such as day-only or month-only mentions, which must be interpreted with reference to the publication date. When such articles are indexed or processed as standalo...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Enabling Knowledge Graph Understanding at Scale with the EXplore Your Graphs ENgine (EXYGEN)](http://arxiv.org/abs/2609.11569v1)
  来源：arXiv | 日期：2026-09-10 | 相关度：2.1 | 新颖度：7.61
  匹配主题：未命中具体主题
  中文摘要：We present EXYGEN (EXplore Your Graphs ENgine), a framework for knowledge graph (KG) understanding that enables conversational access to KGs at scale. We address two questions in sequence. First, how effectively can LLMs...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Reassessing Semen Analysis: Clinical Insights Beyond Sperm Count and Motility.](https://pubmed.ncbi.nlm.nih.gov/42719549/)
  来源：PubMed | 日期：2026-01-01 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Semen analysis (SA), recognized by the World Health Organization (WHO) as the cornerstone of male infertility evaluation, remains indispensable in reproductive medicine. However, advances in assisted reproductive technol...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ICEGR: An Intent-Coherent End-to-End Generative Retrieval Framework for E-commerce Search](http://arxiv.org/abs/2608.29652v3)
  来源：arXiv | 日期：2026-08-30 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Generative Retrieval (GR) is promising for e-commerce search, yet existing methods struggle to maintain query-intent consistency throughout the training pipeline. First, semantic ID (SID) construction based on static pro...
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

### 产品应用 / 监测落地

- [Multimodal genomic surveillance for respiratory pathogens at four U.S. international airports: A comparison of air, wastewater, clinical, and national surveillance data.](https://pubmed.ncbi.nlm.nih.gov/42715246/)
  来源：PubMed | 日期：2026-01-01 | 相关度：5.0 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Early detection of outbreaks and emerging pathogens is critical for public health and global biosecurity. Airports, as major international travel hubs with dense, enclosed populations, are high-risk settings for disease ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Ensembling LLMs for AI-Augmented Cybersecurity Software Requirements Generation](http://arxiv.org/abs/2609.10316v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Translating high-level controls from security standards into concrete, system-specific requirements is central to cybersecurity requirements engineering. Large language models (LLMs) can accelerate this labor-intensive, ...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [VikingRAG: Accurate and Token-efficient Retrieval-augmented Generation over Structured Documents](http://arxiv.org/abs/2609.11390v1)
  来源：arXiv | 日期：2026-09-10 | 相关度：1.4 | 新颖度：6.93
  匹配主题：未命中具体主题
  中文摘要：State-of-the-art retrieval-augmented generation (RAG) methods exploit document structures to acquire sufficient evidence, but often incur substantial token costs. To reduce structural-context tokens without compromising ...
  为什么值得看：VikingRAG: Accurate and Token-efficient  与你的主题有弱匹配，暂时保留作低优先级跟踪。
