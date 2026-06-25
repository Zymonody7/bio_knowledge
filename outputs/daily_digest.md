# 每日论文监控日报 (2026-06-25)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 45 篇新论文。

## 抓取状态

- arXiv：成功，命中 54 篇
- PubMed：成功，命中 54 篇
- bioRxiv：失败，命中 0 篇，错误：503 Server Error: Service Unavailable
- medRxiv：失败，命中 0 篇，错误：503 Server Error: Service Unavailable

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [Molexar: A Unified Multimodal Molecular Foundation Model for Drug Design](http://arxiv.org/abs/2606.25865v1)
  来源：arXiv | 日期：2026-06-24 | 相关度：8.5 | 新颖度：7.74
  匹配主题：foundation_model_agent
  中文摘要：Molecular generation is a central challenge in drug discovery, requiring models that explore vast chemical space while satisfying diverse design constraints. We present Molexar, a unified multimodal molecular foundation ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AI-Assisted Computational Reproducibility on the FABRIC Testbed](http://arxiv.org/abs/2606.25879v1)
  来源：arXiv | 日期：2026-06-24 | 相关度：7.55 | 新颖度：8.03
  匹配主题：foundation_model_agent
  中文摘要：Computational reproducibility remains difficult despite being central to scientific research. In this paper, we show how the international FABRIC testbed, combined with large language model (LLM) coding assistants throug...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [3D Masked Autoencoders are Robust Learners of Volumetric and Multimodal Cellular Representations for Microscopy](http://arxiv.org/abs/2606.23964v1)
  来源：arXiv | 日期：2026-06-22 | 相关度：7.8 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Self-supervised learning in fluorescence microscopy often relies on 2D projections, despite the inherently three-dimensional nature of cells. We present a systematic comparison of 2D and 3D masked autoencoders (MAE-2D vs...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Improving Factuality of 3D Brain MRI Report Generation with Paired Image-domain Retrieval and Text-domain Augmentation](http://arxiv.org/abs/2411.15490v2)
  来源：arXiv | 日期：2024-11-23 | 相关度：7.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Acute ischemic stroke (AIS) requires time-critical decision-making, where inaccurate interpretation of neuroimaging findings can lead to irreversible disability. Diffusion-weighted imaging (DWI) and apparent diffusion co...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RASC+: Retrieval-Constrained LLM Adjudication for Clinical Value Set Authoring](http://arxiv.org/abs/2606.23992v1)
  来源：arXiv | 日期：2026-06-22 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Clinical value sets define the standardized terminology codes used in quality measurement, phenotyping, cohort construction, and clinical decision support. The recently introduced Retrieval-Augmented Set Completion (RASC...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Event-Grounded Question Answering over Long Audio via Structured Retrieval](http://arxiv.org/abs/2602.14612v4)
  来源：arXiv | 日期：2026-02-16 | 相关度：6.55 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Answering natural-language questions over multi-hour audio requires both event recognition and temporal grounding. Current large audio-language models perform well on short clips, but are limited by context length, query...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Verifiable Manifest Signing and Transparency Enforcement for Secure MCP-Based LLM Pipelines](http://arxiv.org/abs/2601.23132v2)
  来源：arXiv | 日期：2026-01-30 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) are increasingly deployed in tool-driven environments such as healthcare analytics, financial systems, retrieval-augmented generation (RAG), and multi-agent workflows. Although the Model Cont...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LLM-Based Scientific Peer Review: Methods, Benchmarks, and Reliability Challenges](http://arxiv.org/abs/2606.25057v1)
  来源：arXiv | 日期：2026-06-23 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：The rapid growth of scientific submissions has pushed traditional peer review toward its scalability limits, motivating the exploration of large language models (LLMs) as intelligent automated evaluation assistants. Alth...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LLM Program Optimization via Retrieval Augmented Search](http://arxiv.org/abs/2501.18916v2)
  来源：arXiv | 日期：2025-01-31 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Recent work has demonstrated the potential of large language models (LLMs) for program optimization, a key challenge in programming languages. We propose a blackbox adaptation method called Retrieval Augmented Search (RA...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Bridging the Post-discharge Gap: A Traceable Multi-agent Framework for Safe and Continuous Care](http://arxiv.org/abs/2606.25334v1)
  来源：arXiv | 日期：2026-06-24 | 相关度：6.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Post-discharge clinical follow-up is critical for maintaining continuity of care and mitigating long-term health risks. However, traditional follow-up paradigms suffer from shortage of health workforce, fragmented patien...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [CausalRAG2: Hierarchical Causal Knowledge Graph Design for RAG](http://arxiv.org/abs/2602.05143v2)
  来源：arXiv | 日期：2026-02-04 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval augmented generation (RAG) has enhanced large language models by enabling access to external knowledge, with graph-based RAG emerging as a powerful paradigm for structured retrieval and reasoning. However, exis...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [scLLM-DSC: LLM-Knowledge Enhanced Cross-Modal Deep Structural Clustering for Single-Cell RNA Sequencing](http://arxiv.org/abs/2606.13007v2)
  来源：arXiv | 日期：2026-06-11 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Clustering is fundamental to scRNA-seq analysis, serving as a cornerstone for identifying cell populations and resolving tissue heterogeneity. However, existing methods focus on mining numerical statistical patterns, suf...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Long-stranded XNA-cssDNA hybrids for robust data storage.](https://pubmed.ncbi.nlm.nih.gov/42341119/)
  来源：PubMed | 日期：2026-06-26 | 相关度：5.75 | 新颖度：9.25
  匹配主题：foundation_model_agent
  中文摘要：DNA is a promising medium for data storage due to its high density and low energy cost. Long-stranded DNA with minimal indexing improves storage density but suffers from poor stability. To address this, we introduce a lo...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Learning to Erase Private Knowledge from Multi-Documents for Retrieval-Augmented Large Language Models](http://arxiv.org/abs/2504.09910v2)
  来源：arXiv | 日期：2025-04-14 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) is a promising technique for applying LLMs to proprietary domains. However, retrieved documents may contain sensitive knowledge, posing risks of privacy leakage in generative results....
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Dziri Voicebot: An End-to-End Low-Resource Speech-to-Speech Conversational System for Algerian Dialect](http://arxiv.org/abs/2606.26003v1)
  来源：arXiv | 日期：2026-06-24 | 相关度：4.75 | 新颖度：7.6
  匹配主题：foundation_model_agent
  中文摘要：Automatic speech and language technologies are still heavily biased toward high-resource languages, limiting their applicability to dialectal and low-resource settings such as Algerian Dialect. This language presents add...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Hybrid-IR: Dual-Path Hybrid Retrieval with Iterative Reasoning for Complex Medical Question Answering](http://arxiv.org/abs/2606.25338v1)
  来源：arXiv | 日期：2026-06-24 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have shown promising performance across a wide range of biomedical applications, including medical question answering (QA), yet they remain prone to hallucinations and outdated knowledge. Alt...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Invoice Haystack: Benchmarking Document Retrieval and Visual Question Answering Under Strong Visual Homogeneity](http://arxiv.org/abs/2606.25343v1)
  来源：arXiv | 日期：2026-06-24 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Vision Language Models have achieved near-human performance on single-document Visual Question Answering, yet their effectiveness degrades significantly when retrieving information from large collections of visually homo...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [AI-CURA, an automated LLM workflow for high-accuracy genetic variant classification.](https://pubmed.ncbi.nlm.nih.gov/42341082/)
  来源：PubMed | 日期：2026-06-24 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have been extensively tested for incorporation into medical applications in recent years; however, their potential in clinical genetics, particularly in diagnosing rare diseases, remains unde...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Security and Privacy in Retrieval-Augmented Generation: Architectures, Threats, Defenses, and Future Directions for Building Trustworthy Systems](http://arxiv.org/abs/2606.25533v1)
  来源：arXiv | 日期：2026-06-24 | 相关度：5.45 | 新颖度：5.98
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) has emerged as a dominant paradigm for enhancing large language models with external knowledge. By coupling retrieval mechanisms with generative models, RAG systems improve factual gr...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Knowledge-Graph Grounding Helps LLMs Only for Out-of-Training Knowledge: A Controlled Study on Clinical Question Answering](http://arxiv.org/abs/2606.22419v2)
  来源：arXiv | 日期：2026-06-21 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：A recent Nature Medicine study reports that general-purpose frontier LLMs outperform specialized retrieval-augmented clinical tools on medical benchmarks, and that retrieval can hurt strong models. We ask the natural fol...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Transformer-Based Language Models Across Domain Verticals: Architectures, Applications and Critical Assessment](http://arxiv.org/abs/2606.24331v1)
  来源：arXiv | 日期：2026-06-23 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Transformer-based language models have become the default substrate for natural language processing and the pace of new releases has made it hard for practitioners to separate durable ideas from the noise of incremental ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Deep learning integrated plasmonic electrochemical sensing for fast and accurate pathogen detection.](https://pubmed.ncbi.nlm.nih.gov/42342751/)
  来源：PubMed | 日期：2026-06-24 | 相关度：3.35 | 新颖度：5.5
  匹配主题：sequencing_bioinformatics
  中文摘要：The development of plasmonic electrochemical biosensors using the new generation of deep learning algorithms is a potent pathway toward the troublesome, immediate and field-mediable diagnostics of the pathogen. This arti...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TheoremGraph: Bridging Formal and Informal Mathematics](http://arxiv.org/abs/2606.25363v1)
  来源：arXiv | 日期：2026-06-24 | 相关度：2.75 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Mathematical knowledge is organized around statements and their dependencies, but this structure is exposed unevenly: informal papers cite mostly at the document level, while formal libraries record fine-grained dependen...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Poisoned Playbooks: Demystifying Knowledge Poisoning Effects on AI Security Agents](http://arxiv.org/abs/2606.24402v1)
  来源：arXiv | 日期：2026-06-23 | 相关度：2.1 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：AI security agents increasingly rely on Retrieval-Augmented Generation (RAG) to use external security knowledge for vulnerability analysis and exploit reasoning. This creates a new risk: poisoned write-ups can be operati...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From materials to medicine: formulation-driven optimization and clinical prospects of NIR-II optical imaging agents.](https://pubmed.ncbi.nlm.nih.gov/42301123/)
  来源：PubMed | 日期：2026-06-23 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Conventional optical imaging is constrained by photon absorption and multiple scattering in biological tissues. Extending excitation and emission into the second near-infrared window (NIR-II, 1000-1700 nm) markedly suppr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution](http://arxiv.org/abs/2606.25721v1)
  来源：arXiv | 日期：2026-06-24 | 相关度：1.4 | 新颖度：7.07
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate model outputs through malicious retrieved documents. Existing detection methods typically rely on auxiliary classifi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Epistemic Bias Injection: Manipulating LLM Opinion via Selective Context Retrieval](http://arxiv.org/abs/2512.00804v3)
  来源：arXiv | 日期：2025-11-30 | 相关度：1.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：When answering user queries, LLMs often retrieve knowledge from external sources stored in retrieval-augmented generation (RAG) databases. These are often populated from unvetted sources, e.g. the open web, and can conta...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic evolution of physically constrained foundation models](http://arxiv.org/abs/2606.25532v1)
  来源：arXiv | 日期：2026-06-24 | 相关度：1.4 | 新颖度：6.48
  匹配主题：未命中具体主题
  中文摘要：Artificial intelligence increasingly drives automated scientific discovery, yet contemporary generalist agents lack physical grounding, frequently hallucinating hardware-incompatible designs. Here, we present a physicall...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [To Isolate or to Score? Model-Adaptive Assessment for Cost-Efficient Multi-Agent RAG](http://arxiv.org/abs/2606.25191v1)
  来源：arXiv | 日期：2026-06-23 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Multi-agent document assessment for retrieval-augmented generation is computationally expensive, driving practitioners toward smaller, deployable models whose assessment mechanisms remain poorly understood. We conduct a ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Diagnosing and Mitigating Compounding Failures in Agentic Persuasion via Taxonomic Strategy Retrieval](http://arxiv.org/abs/2606.24976v1)
  来源：arXiv | 日期：2026-06-23 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Foundation-model agents in multi-step, open-ended environments frequently suffer from compounding errors, where early mistakes contaminate long-horizon trajectories. While Multi-Agent Debate (MAD) succeeds in determinist...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic AI for Bilevel Long-Term Optimization of Policy-Driven Physical Layer Systems](http://arxiv.org/abs/2606.24416v1)
  来源：arXiv | 日期：2026-06-23 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Network operators' changing policies, service requirements, and stringent real-time constraints render existing methods designed with fixed objectives and constraints ineffective. This paper presents Agentic long-term pe...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BioMedArena: An Open-source Toolkit for Building and Evaluating Biomedical Deep Research Agents](http://arxiv.org/abs/2605.06177v2)
  来源：arXiv | 日期：2026-05-07 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Reproducing and comparing deep research agents today is hard: the same backbone evaluated on the same benchmark can report different accuracies across papers because the harness and tool registry differ, and integrating ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Position: Correct Answer, Wrong Mechanism -- When AI Scientists Defend General Claims Their Own Data Contradicts](http://arxiv.org/abs/2606.23175v1)
  来源：arXiv | 日期：2026-06-22 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：AI scientist systems are described as tools, coauthors, or founders, but we evaluate them as if only the final answer matters. This position paper argues that outcome-only evaluation is insufficient, and that task outcom...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [From Scarce Functional Labels to Label-Aware Generation in Homologous Protein Families](http://arxiv.org/abs/2507.15651v2)
  来源：arXiv | 日期：2025-07-21 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Accurately annotating and controlling protein function from sequence data remains a major challenge in protein engineering, especially when functional labels are scarce within large homologous families. Here, we study a ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [MMed-Bench-IR: A Heterogeneous Benchmark for Multilingual Medical Information Retrieval](http://arxiv.org/abs/2606.24200v1)
  来源：arXiv | 日期：2026-06-23 | 相关度：3.05 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) in clinical settings increasingly requires multilingual retrieval against predominantly English evidence corpora. Multilingual medical retrieval demands three capabilities: cross-ling...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [SP-Mind: An Autonomous Reasoning Agent for Spatial Proteomics Analysis](http://arxiv.org/abs/2606.24235v1)
  来源：arXiv | 日期：2026-06-23 | 相关度：5.8 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Spatial proteomics enables single-cell-resolution characterization of protein expression within tissue architecture, playing a critical role in understanding tumor microenvironments and guiding precision medicine. Howeve...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Privacy-Preserving RAG via Multi-Agent Semantic Rewriting: Achieving Confidentiality Without Compromising Contextual Fidelity](http://arxiv.org/abs/2606.24623v1)
  来源：arXiv | 日期：2026-06-23 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation enhances large language models by incorporating external knowledge, but deploying it in sensitive scenarios risks privacy leakage via malicious prompts. To address this, we propose a multi-...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [VPA-Guard: Defending and Benchmarking Image-to-Video Generation Against Visual Prompt Attacks](http://arxiv.org/abs/2606.25592v1)
  来源：arXiv | 日期：2026-06-24 | 相关度：2.05 | 新颖度：6.38
  匹配主题：foundation_model_agent
  中文摘要：Recent advancements in Image-to-Video (I2V) generation have transformed input images from simple appearance references into interactive control interfaces where visual cues such as arrows, sketches, and emojis orchestrat...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [FeSseqdb: a curated sequence-level database and interpretable machine learning framework for identifying iron-sulfur proteins.](https://pubmed.ncbi.nlm.nih.gov/42337419/)
  来源：PubMed | 日期：2026-06-23 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Iron-sulfur (Fe-S) clusters are ubiquitous cofactors in metalloproteins, supporting essential biological functions such as electron transfer, enzymatic catalysis, and metabolic regulation. Despite their importance, large...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz](http://arxiv.org/abs/2606.25622v1)
  来源：arXiv | 日期：2026-06-24 | 相关度：1.4 | 新颖度：6.22
  匹配主题：未命中具体主题
  中文摘要：The NIS-2 Directive mandates robust Risk Management from thousands of small and medium enterprises. To ensure compliance, companies rely on established standards such as the German IT-Grundschutz (IT-GS) of the Federal O...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A Probabilistic Framework for LLM-Based Model Discovery](http://arxiv.org/abs/2602.18266v2)
  来源：arXiv | 日期：2026-02-20 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Automated methods for discovering mechanistic simulator models from observational data offer a promising path toward accelerating scientific progress. Such methods often take the form of agentic-style iterative workflows...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Modeling and Tracking of Heterogeneous Cell Populations via Open Multi-Agent Systems.](https://pubmed.ncbi.nlm.nih.gov/42329946/)
  来源：PubMed | 日期：2026-06-22 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Understanding cellular dynamics represents a critical challenge in biomedical research. Optical microscopy remains a key technique for observing live-cell behaviors in vitro. This paper introduces an enhanced cell-tracki...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ChartWalker: Benchmarking the Cross-Chart RAG Task with Hierarchical Knowledge Graphs](http://arxiv.org/abs/2606.23997v1)
  来源：arXiv | 日期：2026-06-22 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Cross-Chart Retrieval-Augmented Generation (RAG) is critical for complex multi-modal analytical tasks in scientific, business, and political domains. However, existing benchmarks either focus on tables, which are well-st...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers?](http://arxiv.org/abs/2606.24530v1)
  来源：arXiv | 日期：2026-06-23 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：We introduce NatureBench, a cross-discipline benchmark of 90 tasks distilled from peer-reviewed Nature-family publications, designed to evaluate whether AI coding agents can move beyond reproduction toward discovery on r...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [DeepBD: A Grounded Agentic Workflow for Variant Prioritization and Diagnosis of Genetic Birth Defects](http://arxiv.org/abs/2606.24779v1)
  来源：arXiv | 日期：2026-06-23 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Birth defects are a major cause of fetal loss, neonatal morbidity and long-term disability. In the subset with suspected genetic etiologies, exome and genome sequencing have moved many cases from variant detection to pos...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
