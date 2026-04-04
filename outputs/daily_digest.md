# 每日论文监控日报 (2026-04-04)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 43 篇新论文。

## 抓取状态

- arXiv：成功，命中 44 篇
- PubMed：成功，命中 137 篇
- bioRxiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='api.biorxiv.org', port=443): Read timed out. (read timeout=60)
- medRxiv：失败，命中 0 篇，错误：('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [From Hindsight to Foresight: Self-Encouraged Hindsight Distillation for Knowledge-based Visual Question Answering](http://arxiv.org/abs/2511.11132v2)
  来源：arXiv | 日期：2025-11-14 | 相关度：7.5 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Knowledge-based Visual Question Answering (KBVQA) necessitates external knowledge incorporation beyond cross-modal understanding. Existing KBVQA methods either utilize implicit knowledge in multimodal large language mode...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A novel three-step approach to forecast firm-specific technology convergence opportunity via multi-dimensional feature fusion](http://arxiv.org/abs/2604.00803v1)
  来源：arXiv | 日期：2026-04-01 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：As a crucial innovation paradigm, technology convergence (TC) is gaining ever-increasing attention. Yet, existing studies primarily focus on predicting TC at the industry level, with little attention paid to TC forecast ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BloClaw: An Omniscient, Multi-Modal Agentic Workspace for Next-Generation Scientific Discovery](http://arxiv.org/abs/2604.00550v1)
  来源：arXiv | 日期：2026-04-01 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：The integration of Large Language Models (LLMs) into life sciences has catalyzed the development of "AI Scientists." However, translating these theoretical capabilities into deployment-ready research environments exposes...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Memory in the LLM Era: Modular Architectures and Strategies in a Unified Framework](http://arxiv.org/abs/2604.01707v1)
  来源：arXiv | 日期：2026-04-02 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Memory emerges as the core module in the large language model (LLM)-based agents for long-horizon complex tasks (e.g., multi-turn dialogue, game playing, scientific discovery), where memory can enable knowledge accumulat...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Multi-Agent Human-LLM Collaborative Framework for Closed-Loop Scientific Literature Summarization](http://arxiv.org/abs/2604.01452v1)
  来源：arXiv | 日期：2026-04-01 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Scientific discovery is slowed by fragmented literature that requires excessive human effort to gather, analyze, and understand. AI tools, including autonomous summarization and question answering, have been developed to...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Adaptive Stopping for Multi-Turn LLM Reasoning](http://arxiv.org/abs/2604.01413v1)
  来源：arXiv | 日期：2026-04-01 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) increasingly rely on multi-turn reasoning and interaction, such as adaptive retrieval-augmented generation (RAG) and ReAct-style agents, to answer difficult questions. These methods improve a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [GraphWalk: Enabling Reasoning in Large Language Models through Tool-Based Graph Navigation](http://arxiv.org/abs/2604.01610v1)
  来源：arXiv | 日期：2026-04-02 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：The use of knowledge graphs for grounding agents in real-world Q&A applications has become increasingly common. Answering complex queries often requires multi-hop reasoning and the ability to navigate vast relational str...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ByteRover: Agent-Native Memory Through LLM-Curated Hierarchical Context](http://arxiv.org/abs/2604.01599v1)
  来源：arXiv | 日期：2026-04-02 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Memory-Augmented Generation (MAG) extends large language models with external memory to support long-context reasoning, but existing approaches universally treat memory as an external service that agents call into, deleg...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [One Pic is All it Takes: Poisoning Visual Document Retrieval Augmented Generation with a Single Image](http://arxiv.org/abs/2504.02132v4)
  来源：arXiv | 日期：2025-04-02 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) is instrumental for inhibiting hallucinations in large language models (LLMs) through the use of a factual knowledge base (KB). Although PDF documents are prominent sources of knowled...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AI in Insurance: Adaptive Questionnaires for Improved Risk Profiling](http://arxiv.org/abs/2604.02034v1)
  来源：arXiv | 日期：2026-04-02 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Insurance application processes often rely on lengthy and standardized questionnaires that struggle to capture individual differences. Moreover, insurers must blindly trust users' responses, increasing the chances of fra...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Retrieval-Augmented Question Answering over Scientific Literature for the Electron-Ion Collider](http://arxiv.org/abs/2604.02259v1)
  来源：arXiv | 日期：2026-04-02 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：To harness the power of Language Models in answering domain specific specialized technical questions, Retrieval Augmented Generation (RAG) is been used widely. In this work, we have developed a Q\&A application inspired ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Procedural Knowledge at Scale Improves Reasoning](http://arxiv.org/abs/2604.01348v1)
  来源：arXiv | 日期：2026-04-01 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Test-time scaling has emerged as an effective way to improve language models on challenging reasoning tasks. However, most existing methods treat each problem in isolation and do not systematically reuse knowledge from p...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 其他

- [APITestGenie: Generating Web API Tests from Requirements and API Specifications with LLMs](http://arxiv.org/abs/2604.02039v1)
  来源：arXiv | 日期：2026-04-02 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Modern software systems rely heavily on Web APIs, yet creating meaningful and executable test scripts remains a largely manual, time-consuming, and error-prone task. In this paper, we present APITestGenie, a novel tool t...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG](http://arxiv.org/abs/2501.09136v4)
  来源：arXiv | 日期：2025-01-15 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have advanced artificial intelligence by enabling human-like text generation and natural language understanding. However, their reliance on static training data limits their ability to respon...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [To Memorize or to Retrieve: Scaling Laws for RAG-Considerate Pretraining](http://arxiv.org/abs/2604.00715v1)
  来源：arXiv | 日期：2026-04-01 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) improves language model (LM) performance by providing relevant context at test time for knowledge-intensive situations. However, the relationship between parametric knowledge acquired...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SCPatcher: Automated Smart Contract Code Repair via Retrieval-Augmented Generation and Knowledge Graph](http://arxiv.org/abs/2604.00687v1)
  来源：arXiv | 日期：2026-04-01 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Smart contract vulnerabilities can cause substantial financial losses due to the immutability of code after deployment. While existing tools detect vulnerabilities, they cannot effectively repair them. In this paper, we ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Why Gaussian Diffusion Models Fail on Discrete Data?](http://arxiv.org/abs/2604.02028v1)
  来源：arXiv | 日期：2026-04-02 | 相关度：2.75 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Diffusion models have become a standard approach for generative modeling in continuous domains, yet their application to discrete data remains challenging. We investigate why Gaussian diffusion models with the DDPM solve...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Latent-Y: A Lab-Validated Autonomous Agent for De Novo Drug Design](http://arxiv.org/abs/2603.29727v2)
  来源：arXiv | 日期：2026-03-31 | 相关度：2.5 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Drug discovery relies on iterative expert workflows that are slow to parallelize and difficult to scale. Here we introduce Latent-Y, an AI agent that autonomously executes complete antibody design campaigns from text pro...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PluriHopRAG: Exhaustive, Recall-Sensitive QA Through Corpus-Specific Document Structure Learning](http://arxiv.org/abs/2510.14377v2)
  来源：arXiv | 日期：2025-10-16 | 相关度：2.1 | 新颖度：1.75
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) has been used in question answering (QA) systems to improve performance when relevant information is in one (single-hop) or multiple (multi-hop) passages. However, many real life scen...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CliffSearch: Structured Agentic Co-Evolution over Theory and Code for Scientific Algorithm Discovery](http://arxiv.org/abs/2604.01210v1)
  来源：arXiv | 日期：2026-04-01 | 相关度：2.1 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Scientific algorithm discovery is iterative: hypotheses are proposed, implemented, stress-tested, and revised. Current LLM-guided search systems accelerate proposal generation, but often under-represent scientific struct...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Visionary Look at Vibe Researching](http://arxiv.org/abs/2604.00945v1)
  来源：arXiv | 日期：2026-04-01 | 相关度：2.1 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Vibe researching is an emerging paradigm in which human researchers provide high-level direction and critical judgment while LLM-based agents handle the labor-intensive execution of literature review, experimentation, da...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TEDDY: A Family Of Foundation Models For Understanding Single Cell Biology](http://arxiv.org/abs/2503.03485v2)
  来源：arXiv | 日期：2025-03-05 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Understanding the biological mechanisms of disease is crucial for medicine, and in particular, for drug discovery. AI-powered analysis of genome-scale biological data holds great potential in this regard. The increasing ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Optimizing RAG Rerankers with LLM Feedback via Reinforcement Learning](http://arxiv.org/abs/2604.02091v1)
  来源：arXiv | 日期：2026-04-02 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：重排序器（Rerankers）在优化检索增强生成（RAG）的检索结果中起着关键作用。然而，目前的重排序模型通常基于静态的人工标注相关性标签进行孤立优化，与下游生成过程脱节。这种孤立导致了根本性的不匹配：被信息检索指标判定为主题相关的文档，往往无法提供大语言模型（LLM）精确生成答案所需的实际效用。为了弥补这一差距，研究者引入了重排序偏好优化（RRPO），这是一种通过强化学习直接将重排序与 LLM 生成质量对齐的框架。通过将重排序建模为序...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Prior Knowledge Makes It Possible: From Sublinear Graph Algorithms to LLM Test-Time Methods](http://arxiv.org/abs/2510.16609v2)
  来源：arXiv | 日期：2025-10-18 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Test-time augmentation, such as Retrieval-Augmented Generation (RAG) or tool use, critically depends on an interplay between a model's parametric knowledge and externally retrieved information. However, the theoretical u...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Experience as a Compass: Multi-agent RAG with Evolving Orchestration and Agent Prompts](http://arxiv.org/abs/2604.00901v1)
  来源：arXiv | 日期：2026-04-01 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：多智能体检索增强生成（Multi-agent RAG）通过角色分工处理复杂的多步查询，但现有方法因静态行为和固定编排模式，在处理多样化多跳任务时表现脆弱。本文识别出两个核心局限：缺乏持续自适应的编排机制，以及个体智能体缺乏行为层面的学习能力。为此，我们提出了 HERA 框架，旨在协同演化多智能体编排逻辑与特定角色的提示词。在全局层面，HERA 通过奖励引导采样和经验积累来优化针对特定查询的智能体拓扑结构；在局部层面，利用角色感知提示词演...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [HippoMM: Hippocampal-inspired Multimodal Memory for Long Audiovisual Event Understanding](http://arxiv.org/abs/2504.10739v2)
  来源：arXiv | 日期：2025-04-14 | 相关度：0.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：理解长视听体验对计算系统而言仍具挑战，特别是人类情境记忆中核心的时间整合与跨模态关联。我们提出 HippoMM，一种映射海马体机制的计算认知架构。HippoMM 包含三个集成组件：(i) 情节分割，通过检测视听输入变化将视频分割为离散情节，模拟齿状回的模式分离；(ii) 记忆巩固，将情节压缩为保留关键特征的摘要，类似于海马体记忆形成；(iii) 分层记忆检索，先搜索语义摘要，再通过种子片段周围的时间窗口扩展进行跨模态查询，模拟 CA3 ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [From BM25 to Corrective RAG: Benchmarking Retrieval Strategies for Text-and-Table Documents](http://arxiv.org/abs/2604.01733v1)
  来源：arXiv | 日期：2026-04-02 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）系统的性能关键取决于检索质量，但目前尚缺乏针对包含文本和表格数据的异构文档的现代检索方法系统性比较。本研究在一个包含 23,088 个查询和 7,318 份文本表格混合文档的挑战性金融问答基准上，评估了涵盖稀疏、稠密、混合融合、交叉编码重排序、查询扩展、索引增强和自适应检索的十种策略。通过 Recall@k、MRR 和 nDCG 评估检索质量，并利用数字匹配（Number Match）和配对自助法显著性检验评估端到...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Benchmarking Filtered Approximate Nearest Neighbor Search Algorithms on Transformer-based Embedding Vectors](http://arxiv.org/abs/2507.21989v3)
  来源：arXiv | 日期：2025-07-29 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：随着文本、图像和多媒体嵌入模型的进步，检索增强生成（RAG）和推荐系统等领域取得了显著进展。这些应用通常需要在满足特定属性过滤条件的同时，高效检索嵌入空间中与查询向量接近的项目，即过滤近似最近邻搜索（FANNS）。通过文献分析，本研究发现当前缺乏包含最先进 Transformer 文本嵌入向量且具备丰富真实世界属性（涵盖多种类型和值分布）的公开数据集。为填补这一空白，研究者推出了 arxiv-for-fanns 数据集，包含超过 270...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [From sequence to structure: A comprehensive review of deep learning models for RNA structure prediction.](https://pubmed.ncbi.nlm.nih.gov/41650708/)
  来源：PubMed | 日期：2026-04-01 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：RNA structure prediction remains one of the most challenging problems in computational biology, with significant implications for understanding gene regulation, drug design, and synthetic biology. While deep learning has...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Natural language processing of biomedical text to map and prioritize protein-disease associations in HFpEF.](https://pubmed.ncbi.nlm.nih.gov/41780317/)
  来源：PubMed | 日期：2026-04-01 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：针对心血管疾病（CVD）生物标志物和药物靶点验证受限于海量碎片化文献（超过3800万篇）的问题，本研究开发并应用了基于机器学习和自然语言处理（NLP）的VITAL（基于先进语言模型的验证文本挖掘）框架。通过分析全量PubMed摘要，识别出550万篇与六大类CVD相关的文献。以射血分数保留的心衰（HFpEF）为案例，该框架系统地量化并优先排序了蛋白质与疾病的关联。研究确认了BNP、肌钙蛋白-I、半乳糖凝集素-3和肾素等已知标志物，并发现了...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Nemotron ColEmbed V2: Top-Performing Late Interaction Embedding Models for Visual Document Retrieval](http://arxiv.org/abs/2602.03992v2)
  来源：arXiv | 日期：2026-02-03 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) systems have been popular for generative applications, powering language models by injecting external knowledge. Companies have been trying to leverage their large catalog of document...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [BIOGEN: Evidence-Grounded Multi-Agent Reasoning Framework for Transcriptomic Interpretation in Antimicrobial Resistance](http://arxiv.org/abs/2510.16082v5)
  来源：arXiv | 日期：2025-10-17 | 相关度：3.1 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Interpreting gene clusters from RNA sequencing (RNA-seq) remains challenging, especially in antimicrobial resistance studies where mechanistic insight is important for hypothesis generation. Existing pathway enrichment m...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Big data in multiple sclerosis.](https://pubmed.ncbi.nlm.nih.gov/41925198/)
  来源：PubMed | 日期：2026-04-01 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：本综述总结了利用多源大数据和先进分析技术在多发性硬化症（MS）领域取得的关键进展。源自MS大数据的真实世界证据（RWE）显著优化了治疗策略，重新定义了疾病进展概念，并完善了预后模型。RWE强调了早期强化治疗相较于阶梯治疗的长期获益，揭示了减量治疗的风险及妊娠期管理的重要性。此外，研究明确了特定高效疗法的有效性与安全性差异，以及换药的关键预测因子。RWE还强调了“独立于复发活动的进展”（PIRA）是导致成人和儿童MS残疾及长期不良预后的核...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Machine learning-based DNA microarray analysis for disease detection using the MICRO-AI framework.](https://pubmed.ncbi.nlm.nih.gov/41925147/)
  来源：PubMed | 日期：2026-01-01 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：DNA微阵列技术在基因组学中具有重要地位，但其高维度（1.2万-2.2万个基因）、小样本量（155-1097个样本）、噪声及类别不平衡问题挑战了诊断模式的提取。本文提出MICRO-AI框架，用于微阵列数据的自动化疾病诊断。该框架集成了分位数归一化、ComBat批次校正和KNN填补等预处理技术，并采用基于注意力加权的自适应特征选择（结合RFE-CV）以及由GBM、随机森林和SVM组成的异构集成分类器。通过新型注意力特征融合机制，该框架在不...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Hypergraph Foundation Model.](https://pubmed.ncbi.nlm.nih.gov/41433164/)
  来源：PubMed | 日期：2026-04-01 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：超图神经网络（HGNNs）通过超边连接多个顶点，能有效建模蛋白质相互作用和社交网络等领域的高阶复杂关系，增强建模能力并减少信息损失。然而，由于超图数据兼具顶点特征与复杂的结构信息，开发超图基础模型（Foundation Model）面临挑战。本研究提出了 Hyper-FM，一种用于多领域知识提取的超图基础模型。该模型核心包含：用于顶点特征表示的“分层高阶邻居引导的顶点知识嵌入”，以及用于结构信息捕捉的“分层多超图引导的结构知识提取”。此...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Functional impact assessment of tissue-specific missense variants in the PTPRH gene using a multi-tool computational framework.](https://pubmed.ncbi.nlm.nih.gov/41570449/)
  来源：PubMed | 日期：2026-04-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：癌症由破坏细胞过程的遗传改变驱动，其中蛋白酪氨酸磷酸酶受体H型（PTPRH）基因在癌症进展中具有双重作用。本研究采用计算机模拟框架评估了PTPRH的组织特异性错义变异。研究从COSMIC数据库中鉴定出478个独特错义变异，通过fathmm、PROVEAN、PolyPhen-2、SIFT等8种计算工具筛选出14个一致预测为有害的变异。随后利用MUpro、I-Mutant等工具进行稳定性分析，发现其中10个变异可能破坏蛋白质稳定性。进化保守...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SAKE: Structured Agentic Knowledge Extrapolation for Complex LLM Reasoning via Reinforcement Learning](http://arxiv.org/abs/2505.15062v4)
  来源：arXiv | 日期：2025-05-21 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Knowledge extrapolation is the process of inferring novel information by combining and extending existing knowledge that is explicitly available. It is essential for solving complex questions in specialized domains where...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Doctor-RAG: Failure-Aware Repair for Agentic Retrieval-Augmented Generation](http://arxiv.org/abs/2604.00865v1)
  来源：arXiv | 日期：2026-04-01 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：代理检索增强生成（Agentic RAG）已成为处理多跳问答和复杂知识推理的广泛范式，但在长推理轨迹中极易出现故障。现有方法通常仅停留在诊断阶段，或通过重新运行整个流水线来修复，导致巨大的计算开销和冗余推理。本文提出 Doctor-RAG (DR-RAG)，一种统一的诊断与修复框架，通过显式错误定位和前缀重用实现最小成本干预。DR-RAG 将故障处理分为两个阶段：(i) 轨迹级故障诊断与定位，利用覆盖门控分类法（coverage-gat...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Artificial intelligence and multi-omics convergence in breast cancer: Revolutionizing diagnosis, prognostication, and precision oncology.](https://pubmed.ncbi.nlm.nih.gov/41616992/)
  来源：PubMed | 日期：2026-04-01 | 相关度：3.75 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：乳腺癌（BC）具有高度异质性，是全球女性癌症死亡的主要原因。基因组学、转录组学、表观基因组学、蛋白质组学和代谢组学等多组学分析的进展，实现了更精细的亚型分层和肿瘤生物学表征，加速了诊断、预后生物标志物及治疗靶点的发现。然而，受限于组学数据的高维性、异质性、跨平台变异以及单模态分析的局限性，将多层分子信号转化为临床决策支持仍具挑战。本综述总结了多组学如何完善乳腺癌亚型定义，并综合了人工智能（特别是深度学习）在整合多组学与影像、病理及临床变...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Multi-omics biomarkers in psychiatric disorders diagnosis and stratification.](https://pubmed.ncbi.nlm.nih.gov/41655615/)
  来源：PubMed | 日期：2026-04-01 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：精神疾病的精准诊断与分层因缺乏客观生物标志物且依赖主观临床标准而面临挑战。基因组学、转录组学、蛋白质组学、代谢组学和表观基因组学等多组学技术的进展，深化了对精神分裂症、双相情感障碍、重度抑郁症和自闭症谱系障碍等复杂神经精神疾病的理解。本综述评估了精神医学领域多组学研究的现状，重点关注方法学创新、整合策略以及在标志物发现和临床实施中的转化潜力。通过合成不同分子层面的数据，多组学方法能够从系统水平将精神疾病视为受分子、细胞、环境和神经回路相...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Comparative evaluation of multimodal point-of-care tests to differentiate gram-negative from gram-positive infections in critically ill adults: a diagnostic accuracy study.](https://pubmed.ncbi.nlm.nih.gov/41535672/)
  来源：PubMed | 日期：2026-04-01 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：针对脓毒症患者在培养结果前过度使用广谱抗生素的问题，本研究系统评估了区分革兰氏阴性（GN）与革兰氏阳性（GP）感染的即时检测（POCT）方法。研究检索了 2005 年至 2025 年间 86 项相关研究，对 72 项研究进行了定量合成，涵盖宿主反应生物标志物、病原体定向检测、组学测试及临床参数。结果显示，病原体定向快速检测（如 PCR、MALDI-TOF MS）表现出最高的准确性，合并灵敏度和特异性均 >0.90，AUC 达 0.97-...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Generative AI Spotlights the Human Core of Data Science: Implications for Education](http://arxiv.org/abs/2604.02238v1)
  来源：arXiv | 日期：2026-04-02 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：生成式人工智能（GAI）揭示了数据科学中不可还原的人类核心：GAI 的进步应强化而非削弱数据科学教育中对人类推理的关注。GAI 目前已能执行清理、摘要、可视化、建模和报告起草等常规数据科学工作流。然而，最关键的能力仍属于人类，包括问题表述、测量与设计、因果识别、统计与计算推理、伦理问责及意义构建。本文基于 Donoho 的“大数据科学”（GDS）框架，追踪了数据科学从 Tukey 的愿景、监控资本主义商业逻辑到学术项目的演进。通过将 G...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [AI Engineering Blueprint for On-Premises Retrieval-Augmented Generation Systems](http://arxiv.org/abs/2604.01395v1)
  来源：arXiv | 日期：2026-04-01 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）系统在企业环境中日益普及，但严格的数据保护法规限制了许多组织使用云端服务，使得本地化（On-premises）部署成为必然需求。现有的蓝图和参考架构多侧重于云端环境，缺乏企业级组件及全面的本地化实施框架。本文旨在填补这一空白，提出了一套用于构建可扩展企业级本地 RAG 解决方案的 AI 工程蓝图。该蓝图旨在解决集成挑战并简化 RAG 与现有企业基础设施的对接，其核心贡献包括：(1) 使用 4+1 视图模型描述的端到...
  为什么值得看：AI Engineering Blueprint for On-Premises 与你的主题有弱匹配，暂时保留作低优先级跟踪。
