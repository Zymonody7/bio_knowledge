# 每日论文监控日报 (2026-04-02)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 55 篇新论文。

## 抓取状态

- arXiv：成功，命中 55 篇
- PubMed：成功，命中 128 篇
- bioRxiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='api.biorxiv.org', port=443): Read timed out. (read timeout=60)
- medRxiv：失败，命中 0 篇，错误：('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [Large Language Models for Variant-Centric Functional Evidence Mining](http://arxiv.org/abs/2604.00075v1)
  来源：arXiv | 日期：2026-03-31 | 相关度：7.8 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Functional evidence is essential for clinical interpretation of genomic variants, but identifying relevant studies and translating experimental results into structured evidence remains labor intensive. We developed a ben...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [From Hindsight to Foresight: Self-Encouraged Hindsight Distillation for Knowledge-based Visual Question Answering](http://arxiv.org/abs/2511.11132v2)
  来源：arXiv | 日期：2025-11-14 | 相关度：7.5 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Knowledge-based Visual Question Answering (KBVQA) necessitates external knowledge incorporation beyond cross-modal understanding. Existing KBVQA methods either utilize implicit knowledge in multimodal large language mode...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ReAG: Reasoning-Augmented Generation for Knowledge-based Visual Question Answering](http://arxiv.org/abs/2511.22715v2)
  来源：arXiv | 日期：2025-11-27 | 相关度：7.5 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Multimodal Large Language Models (MLLMs) have shown impressive capabilities in jointly understanding text, images, and videos, often evaluated via Visual Question Answering (VQA). However, even state-of-the-art MLLMs str...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Incorporating LLM Embeddings for Variation Across the Human Genome](http://arxiv.org/abs/2509.20702v2)
  来源：arXiv | 日期：2025-09-25 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in large language model (LLM) embeddings have enabled powerful representations for biological data, but most applications to date focus on gene-level information. We present one of the first systematic fr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ATP-Bench: Towards Agentic Tool Planning for MLLM Interleaved Generation](http://arxiv.org/abs/2603.29902v1)
  来源：arXiv | 日期：2026-03-31 | 相关度：6.8 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Interleaved text-and-image generation represents a significant frontier for Multimodal Large Language Models (MLLMs), offering a more intuitive way to convey complex information. Current paradigms rely on either image ge...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A novel three-step approach to forecast firm-specific technology convergence opportunity via multi-dimensional feature fusion](http://arxiv.org/abs/2604.00803v1)
  来源：arXiv | 日期：2026-04-01 | 相关度：6.55 | 新颖度：7.38
  匹配主题：foundation_model_agent
  中文摘要：As a crucial innovation paradigm, technology convergence (TC) is gaining ever-increasing attention. Yet, existing studies primarily focus on predicting TC at the industry level, with little attention paid to TC forecast ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Med.ai ASK: an agentic system for biomedical question answering.](https://pubmed.ncbi.nlm.nih.gov/41911379/)
  来源：PubMed | 日期：2026-03-30 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Intelligent agent-driven research co-pilots, leveraging advances in generative AI, are transforming how scientists access biomedical knowledge. This paper presents Med.ai ASK, an agentic question-answering system designe...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EventChat: Implementation and user-centric evaluation of a large language model-driven conversational recommender system for exploring leisure events in an SME context](http://arxiv.org/abs/2407.04472v4)
  来源：arXiv | 日期：2024-07-05 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) present an enormous evolution in the strategic potential of conversational recommender systems (CRS). Yet to date, research has predominantly focused upon technical frameworks to implement LL...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BloClaw: An Omniscient, Multi-Modal Agentic Workspace for Next-Generation Scientific Discovery](http://arxiv.org/abs/2604.00550v1)
  来源：arXiv | 日期：2026-04-01 | 相关度：6.45 | 新颖度：6.48
  匹配主题：foundation_model_agent
  中文摘要：The integration of Large Language Models (LLMs) into life sciences has catalyzed the development of "AI Scientists." However, translating these theoretical capabilities into deployment-ready research environments exposes...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Towards Verifiable and Self-Correcting AI Physicists for Quantum Many-Body Simulations](http://arxiv.org/abs/2604.00149v1)
  来源：arXiv | 日期：2026-03-31 | 相关度：6.15 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in automated scientific discovery have shown remarkable promise across frontier research domains, with agent systems driven by large language models (LLMs) emerging as powerful tools for physics research....
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG](http://arxiv.org/abs/2501.09136v4)
  来源：arXiv | 日期：2025-01-15 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have advanced artificial intelligence by enabling human-like text generation and natural language understanding. However, their reliance on static training data limits their ability to respon...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Empowering AI data scientists using a multi-agent LLM framework with self-evolving capabilities for autonomous, tool-aware biomedical data analyses.](https://pubmed.ncbi.nlm.nih.gov/41912700/)
  来源：PubMed | 日期：2026-03-30 | 相关度：6.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence agents are emerging as powerful applications of large language models (LLMs), automating complex tasks and enabling scientific data exploration. However, their use in biomedical data analysis rema...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [To Memorize or to Retrieve: Scaling Laws for RAG-Considerate Pretraining](http://arxiv.org/abs/2604.00715v1)
  来源：arXiv | 日期：2026-04-01 | 相关度：5.45 | 新颖度：7.09
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) improves language model (LM) performance by providing relevant context at test time for knowledge-intensive situations. However, the relationship between parametric knowledge acquired...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SCPatcher: Automated Smart Contract Code Repair via Retrieval-Augmented Generation and Knowledge Graph](http://arxiv.org/abs/2604.00687v1)
  来源：arXiv | 日期：2026-04-01 | 相关度：5.45 | 新颖度：6.47
  匹配主题：foundation_model_agent
  中文摘要：Smart contract vulnerabilities can cause substantial financial losses due to the immutability of code after deployment. While existing tools detect vulnerabilities, they cannot effectively repair them. In this paper, we ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The Energy Footprint of LLM-Based Environmental Analysis: LLMs and Domain Products](http://arxiv.org/abs/2604.00053v1)
  来源：arXiv | 日期：2026-03-31 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：As large language models (LLMs) are increasingly used in domain-specific applications, including climate change and environmental research, understanding their energy footprint has become an important concern. The growin...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Truncated Step-Level Sampling with Process Rewards for Retrieval-Augmented Reasoning](http://arxiv.org/abs/2602.23440v3)
  来源：arXiv | 日期：2026-02-26 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Reinforcement learning has emerged as an effective paradigm for training large language models to interleave reasoning with search engine calls. However, existing approaches face a fundamental credit assignment problem: ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BIOGEN: Evidence-Grounded Multi-Agent Reasoning Framework for Transcriptomic Interpretation in Antimicrobial Resistance](http://arxiv.org/abs/2510.16082v4)
  来源：arXiv | 日期：2025-10-17 | 相关度：4.1 | 新颖度：6.25
  匹配主题：pathogenomics
  中文摘要：Interpreting gene clusters derived from RNA sequencing (RNA-seq) remains a persistent challenge in functional genomics, particularly in antimicrobial resistance studies where mechanistic context is essential for downstre...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Nemotron ColEmbed V2: Top-Performing Late Interaction Embedding Models for Visual Document Retrieval](http://arxiv.org/abs/2602.03992v2)
  来源：arXiv | 日期：2026-02-03 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) systems have been popular for generative applications, powering language models by injecting external knowledge. Companies have been trying to leverage their large catalog of document...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [What an Autonomous Agent Discovers About Molecular Transformer Design: Does It Transfer?](http://arxiv.org/abs/2603.28015v1)
  来源：arXiv | 日期：2026-03-30 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Deep learning models for drug-like molecules and proteins overwhelmingly reuse transformer architectures designed for natural language, yet whether molecular sequences benefit from different designs has not been systemat...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Building evidence-based knowledge graphs from full-text literature for disease-specific biomedical reasoning](http://arxiv.org/abs/2603.28325v2)
  来源：arXiv | 日期：2026-03-30 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Biomedical knowledge resources often either preserve evidence as unstructured text or compress it into flat triples that omit study design, provenance, and quantitative support. Here we present EvidenceNet, a framework a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Mimosa Framework: Toward Evolving Multi-Agent Systems for Scientific Research](http://arxiv.org/abs/2603.28986v1)
  来源：arXiv | 日期：2026-03-30 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Current Autonomous Scientific Research (ASR) systems, despite leveraging large language models (LLMs) and agentic architectures, remain constrained by fixed workflows and toolsets that prevent adaptation to evolving task...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MA-SAPO: Multi-Agent Reasoning for Score-Aware Prompt Optimization](http://arxiv.org/abs/2510.16635v2)
  来源：arXiv | 日期：2025-10-18 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Prompt optimization has become a practical way to improve the performance of Large Language Models (LLMs) without retraining. However, most existing frameworks treat evaluation as a black box, relying solely on outcome s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Toward AI foundation models for epidemics: Promise, challenges, and paths forward.](https://pubmed.ncbi.nlm.nih.gov/41824492/)
  来源：PubMed | 日期：2026-03-31 | 相关度：4.4 | 新颖度：1.5
  匹配主题：pathogenomics
  中文摘要：基础模型（如 GPT、GenCast、AlphaFold）正在改变科学发现，但在流行病建模领域尚未实现类似变革。传统模型通常针对特定病原体，在应对如 SARS-CoV-2 等突发疫情时难以快速生成洞察。本文探讨了将基础模型范式扩展到流行病学的可能性：即构建一个能捕捉跨病原体、人群和环境的传染病动力学共享原理的预训练模型。该模型仅需少量数据即可微调至新场景，实现快速预测、推理和响应，对资源匮乏地区尤为重要。文章指出，流行病学见解与现代 A...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Graph Vector Field: A Unified Framework for Multimodal Health Risk Assessment from Heterogeneous Wearable and Environmental Data Streams](http://arxiv.org/abs/2603.28115v1)
  来源：arXiv | 日期：2026-03-30 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：数字健康研究在动态图疾病模型、单纯复形拓扑学习和多模态专家混合架构（MoE）方面取得了进展，但这些领域仍处于割裂状态。本文提出图向量场（GVF）框架，将健康风险建模为随时间变化的单纯复形上的向量值场，结合了离散微分几何算子与模态结构化的专家混合模型。风险被表示为向量值上链（cochain），其演化由 Hodge 拉普拉斯算子和离散外演算算子参数化，通过 Helmholtz-Hodge 分解为势驱动（恰当）、循环类（余恰当）和拓扑约束（调...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Latent-Y: A Lab-Validated Autonomous Agent for De Novo Drug Design](http://arxiv.org/abs/2603.29727v2)
  来源：arXiv | 日期：2026-03-31 | 相关度：2.5 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Drug discovery relies on iterative expert workflows that are slow to parallelize and difficult to scale. Here we introduce Latent-Y, an AI agent that autonomously executes complete antibody design campaigns from text pro...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CliffSearch: Structured Agentic Co-Evolution over Theory and Code for Scientific Algorithm Discovery](http://arxiv.org/abs/2604.01210v1)
  来源：arXiv | 日期：2026-04-01 | 相关度：2.1 | 新颖度：8.58
  匹配主题：未命中具体主题
  中文摘要：Scientific algorithm discovery is iterative: hypotheses are proposed, implemented, stress-tested, and revised. Current LLM-guided search systems accelerate proposal generation, but often under-represent scientific struct...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Visionary Look at Vibe Researching](http://arxiv.org/abs/2604.00945v1)
  来源：arXiv | 日期：2026-04-01 | 相关度：2.1 | 新颖度：7.48
  匹配主题：未命中具体主题
  中文摘要：Vibe researching is an emerging paradigm in which human researchers provide high-level direction and critical judgment while LLM-based agents handle the labor-intensive execution of literature review, experimentation, da...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PluriHopRAG: Exhaustive, Recall-Sensitive QA Through Corpus-Specific Document Structure Learning](http://arxiv.org/abs/2510.14377v2)
  来源：arXiv | 日期：2025-10-16 | 相关度：2.1 | 新颖度：6.75
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) has been used in question answering (QA) systems to improve performance when relevant information is in one (single-hop) or multiple (multi-hop) passages. However, many real life scen...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The Future of AI is Many, Not One](http://arxiv.org/abs/2603.29075v1)
  来源：arXiv | 日期：2026-03-30 | 相关度：2.1 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：The way we're thinking about generative AI right now is fundamentally individual. We see this not just in how users interact with models but also in how models are built, how they're benchmarked, and how commercial and r...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Experience as a Compass: Multi-agent RAG with Evolving Orchestration and Agent Prompts](http://arxiv.org/abs/2604.00901v1)
  来源：arXiv | 日期：2026-04-01 | 相关度：1.4 | 新颖度：7.64
  匹配主题：未命中具体主题
  中文摘要：多智能体检索增强生成（Multi-agent RAG）通过角色分工支持多步、多来源的复杂推理任务。然而，现有方法依赖静态行为和固定编排，在多样化的多跳任务中表现脆弱。本文识别了两个关键局限：缺乏持续自适应的编排机制，以及个体智能体缺乏行为层面的学习。为此，我们提出了 HERA 框架，旨在协同演化多智能体编排和特定角色的提示词。在全局层面，HERA 通过奖励引导的采样和经验积累，优化针对特定查询的智能体拓扑结构。在局部层面，角色感知提示词...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Certifiably Robust RAG against Retrieval Corruption](http://arxiv.org/abs/2405.15556v2)
  来源：arXiv | 日期：2024-05-24 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）易受检索污染攻击的影响，即在检索结果中注入恶意段落会导致模型生成错误的响应。本文提出了 RobustRAG，这是首个针对检索污染攻击具有可证明鲁棒性（Certifiable Robustness）的防御框架。RobustRAG 的核心思想是“隔离后聚合”策略：首先将检索到的段落隔离到不相交的组中，基于每组连接的段落分别生成大语言模型（LLM）响应，随后通过安全聚合算法处理这些响应以获得鲁棒输出。为实现该框架，作者设...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CivicShield: A Cross-Domain Defense-in-Depth Framework for Securing Government-Facing AI Chatbots Against Multi-Turn Adversarial Attacks](http://arxiv.org/abs/2603.29062v1)
  来源：arXiv | 日期：2026-03-30 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：基于大语言模型（LLM）的政府服务聊天机器人在安全方面存在严重漏洞，多轮对抗性攻击对现有防御措施的成功率超过90%。为此，本研究提出了CivicShield，一个面向政府AI聊天机器人的跨域深度防御框架。该框架借鉴了网络安全、形式验证、生物免疫系统、航空安全和零信任密码学，引入了七层防御体系：(1)基于能力的访问控制零信任基础；(2)边界输入验证；(3)意图分类语义防火墙；(4)带有安全不变式的对话状态机；(5)行为异常检测；(6)多模...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Owl-AuraID 1.0: An Intelligent System for Autonomous Scientific Instrumentation and Scientific Data Analysis](http://arxiv.org/abs/2603.29828v1)
  来源：arXiv | 日期：2026-03-31 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：科学发现日益依赖高通量表征，但自动化进程受限于封闭的图形用户界面（GUI）以及现有基于 API 系统泛化能力不足的问题。本文提出 Owl-AuraID，这是一种软硬件协作的具身智能体系统，采用原生 GUI 范式，通过与人类专家相同的界面操作仪器。其以技能为核心的框架将 Type-1（GUI 操作）和 Type-2（数据分析）技能整合到端到端工作流中，实现了物理样本处理与科学解释的连接。Owl-AuraID 在十类精密仪器和多种工作流中展...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Benchmarking Filtered Approximate Nearest Neighbor Search Algorithms on Transformer-based Embedding Vectors](http://arxiv.org/abs/2507.21989v3)
  来源：arXiv | 日期：2025-07-29 | 相关度：0.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：随着文本、图像和音频嵌入模型的进步，检索增强生成（RAG）和推荐系统等领域取得了显著进展。这些应用通常要求在满足基于项目属性的过滤条件的同时，高效检索嵌入空间中与给定查询接近的项目，即过滤近似最近邻搜索（FANNS）。通过深入的文献分析，研究人员发现当前缺乏包含最先进 Transformer 文本嵌入向量、且具备丰富真实世界属性（涵盖多种属性类型和值分布）的公开数据集。为填补这一空白，本研究推出了 arxiv-for-fanns 数据集...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [UniAI-GraphRAG: Synergizing Ontology-Guided Extraction, Multi-Dimensional Clustering, and Dual-Channel Fusion for Robust Multi-Hop Reasoning](http://arxiv.org/abs/2603.25152v2)
  来源：arXiv | 日期：2026-03-26 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）系统在处理复杂推理、多跳查询及特定领域问答时面临显著挑战。尽管现有的 GraphRAG 框架在结构化知识组织方面取得了进展，但在跨行业适应性、社区报告完整性和检索性能上仍存在局限。本文提出 UniAI-GraphRAG，一种基于开源 GraphRAG 的增强框架。该框架引入了三大核心创新：(1) 本体引导的知识提取，利用预定义 Schema 引导大语言模型（LLM）准确识别特定领域实体与关系；(2) 多维社区聚类策...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Multilingual Medical Reasoning for Question Answering with Large Language Models](http://arxiv.org/abs/2512.05658v2)
  来源：arXiv | 日期：2025-12-05 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) with reasoning capabilities have recently demonstrated strong potential in medical Question Answering (QA). Existing approaches are largely English-focused and primarily rely on distillation ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [From sequence to structure: A comprehensive review of deep learning models for RNA structure prediction.](https://pubmed.ncbi.nlm.nih.gov/41650708/)
  来源：PubMed | 日期：2026-04-01 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：RNA structure prediction remains one of the most challenging problems in computational biology, with significant implications for understanding gene regulation, drug design, and synthetic biology. While deep learning has...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Towards a Medical AI Scientist](http://arxiv.org/abs/2603.28589v1)
  来源：arXiv | 日期：2026-03-30 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Autonomous systems that generate scientific hypotheses, conduct experiments, and draft manuscripts have recently emerged as a promising paradigm for accelerating discovery. However, existing AI Scientists remain largely ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Sampling at intermediate temperatures is optimal for training large language models in protein structure prediction](http://arxiv.org/abs/2603.29529v1)
  来源：arXiv | 日期：2026-03-31 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：We investigate the parameter space of transformer models trained on protein sequence data using a statistical mechanics framework, sampling the loss landscape at varying temperatures by Langevin dynamics to characterize ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Natural language processing of biomedical text to map and prioritize protein-disease associations in HFpEF.](https://pubmed.ncbi.nlm.nih.gov/41780317/)
  来源：PubMed | 日期：2026-04-01 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：The validation of promising clinical biomarkers, molecular mechanisms, and novel drug targets in cardiovascular disease (CVD) is hindered by a vast and fragmented biomedical literature, which now exceeds 38 million publi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A Systematic Framework for Enterprise Knowledge Retrieval: Leveraging LLM-Generated Metadata to Enhance RAG Systems](http://arxiv.org/abs/2512.05411v2)
  来源：arXiv | 日期：2025-12-05 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：In enterprise settings, efficiently retrieving relevant information from large and complex knowledge bases is essential for operational productivity and informed decision-making. This research presents a systematic empir...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GUIDE: Resolving Domain Bias in GUI Agents through Real-Time Web Video Retrieval and Plug-and-Play Annotation](http://arxiv.org/abs/2603.26266v2)
  来源：arXiv | 日期：2026-03-27 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Large vision-language models have endowed GUI agents with strong general capabilities for interface understanding and interaction. However, due to insufficient exposure to domain-specific software operation data during t...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Understand and Accelerate Memory Processing Pipeline for Disaggregated LLM Inference](http://arxiv.org/abs/2603.29002v1)
  来源：arXiv | 日期：2026-03-30 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Modern large language models (LLMs) increasingly depends on efficient long-context processing and generation mechanisms, including sparse attention, retrieval-augmented generation (RAG), and compressed contextual memory,...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Novel Deep-Learning Unsupervised Domain Adaptation Method for Mitigating Batch, Strain, and Instrument Variations to Enhance Raman Spectroscopy-Based Bacterial Pathogen Identification.](https://pubmed.ncbi.nlm.nih.gov/41842761/)
  来源：PubMed | 日期：2026-03-31 | 相关度：4.4 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：The escalating threat of antibiotic resistance demands a rapid and accurate pathogen identification. While Raman spectroscopy combined with deep learning supports fast detection, model robustness remains compromised by d...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Hypergraph Foundation Model.](https://pubmed.ncbi.nlm.nih.gov/41433164/)
  来源：PubMed | 日期：2026-04-01 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：超图神经网络 (HGNNs) 通过超边连接多个顶点，能有效建模蛋白质相互作用和社交网络等领域的高阶复杂关系，减少信息损失。由于超图数据兼具顶点特征与复杂的结构信息，开发其基础模型具有挑战性。本研究提出了 Hyper-FM，一种用于多领域知识提取的超图基础模型。该模型核心包含：用于顶点特征表示的“分层高阶邻居引导顶点知识嵌入”以及用于提取结构信息的“分层多超图引导结构知识提取”。此外，研究者构建了 11 个文本属性超图数据集，旨在推动 H...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Functional impact assessment of tissue-specific missense variants in the PTPRH gene using a multi-tool computational framework.](https://pubmed.ncbi.nlm.nih.gov/41570449/)
  来源：PubMed | 日期：2026-04-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：癌症由破坏细胞过程的遗传改变驱动，其中蛋白酪氨酸磷酸酶受体H型（PTPRH）基因在癌症进展中具有双重作用。本研究采用计算机模拟框架评估了PTPRH的组织特异性错义变异。研究从COSMIC数据库中鉴定出478个独特错义变异，通过fathmm、PROVEAN、PolyPhen-2、SIFT等8种计算工具筛选出14个一致预测为有害的变异。随后利用MUpro、I-Mutant等工具进行稳定性分析，发现其中10个变异可能破坏蛋白质稳定性。进化保守...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Drift-Aware Continual Tokenization for Generative Recommendation](http://arxiv.org/abs/2603.29705v1)
  来源：arXiv | 日期：2026-03-31 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：生成式推荐通常采用两阶段流程：首先通过可学习的分词器将项目映射为离散标记序列（即标识符），随后由自回归生成式推荐模型（GRM）基于这些标识符进行预测。近期研究在分词器中引入了协同信号，使具有相似用户行为模式的项目获得相似编码，显著提升了推荐质量。然而，现实环境持续演变：新项目会导致标识符冲突和偏移，而新交互则引发既有项目的协同漂移（如共现模式和流行度变化）。全量重训分词器和 GRM 成本极高，而直接微调分词器会改变多数既有项目的标记序列...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Kwame 2.0: Human-in-the-Loop Generative AI Teaching Assistant for Large Scale Online Coding Education in Africa](http://arxiv.org/abs/2603.29159v1)
  来源：arXiv | 日期：2026-03-31 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：针对资源受限环境下大规模在线编程课程的教学支持难题，本文推出了 Kwame 2.0。这是一款基于检索增强生成（RAG）技术的双语（英法）生成式 AI 助教，部署于面向非洲学习者的移动端编程课程 SuaCode 的人机协同论坛中。Kwame 2.0 通过检索课程材料生成上下文相关的回答，并鼓励人工监督与社区参与。在一项跨越 15 个月、涵盖 35 个非洲国家、15 个班次及 3,717 名注册用户的纵向研究中，评估结果显示，Kwame 2...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Doctor-RAG: Failure-Aware Repair for Agentic Retrieval-Augmented Generation](http://arxiv.org/abs/2604.00865v1)
  来源：arXiv | 日期：2026-04-01 | 相关度：0.7 | 新颖度：7.3
  匹配主题：未命中具体主题
  中文摘要：智能体检索增强生成（Agentic RAG）已成为处理多跳问答和复杂知识推理的主流范式，其在推理过程中交织检索与推理步骤。然而，随着推理轨迹增长，失败风险显著增加。现有方法通常仅停留在诊断阶段，或需重新运行整个流水线，导致巨大的计算开销和推理冗余。本文提出 Doctor-RAG (DR-RAG)，这是一种统一的“诊断-修复”框架，通过显式的错误定位和前缀重用，实现对 Agentic RAG 失败的最小成本干预。DR-RAG 将处理过程分...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RAGShield: Provenance-Verified Defense-in-Depth Against Knowledge Base Poisoning in Government Retrieval-Augmented Generation Systems](http://arxiv.org/abs/2604.00387v1)
  来源：arXiv | 日期：2026-04-01 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：联邦机构部署的面向公民服务的RAG系统易受知识库投毒攻击，研究表明仅需10个对抗性段落即可达到98.2%的检索成功率。本研究提出RAGShield，一个借鉴软件供应链溯源验证的五层深度防御框架。该框架包含：(1)受C2PA启发的加密文档认证，在摄入阶段拦截未签名或伪造文档；(2)优先考虑已验证来源的信任加权检索；(3)利用形式化污点格和跨源矛盾检测识别内部威胁；(4)具备可审计引用的溯源感知生成；(5)映射至15个控制族的NIST SP...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CQ-CiM: Hardware-Aware Embedding Shaping for Robust CiM-Based Retrieval](http://arxiv.org/abs/2602.20083v3)
  来源：arXiv | 日期：2026-02-23 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：在边缘设备上部署检索增强生成（RAG）面临传统架构下大规模数据移动和计算带来的延迟挑战。存内计算（CiM）架构通过在交叉杆结构中直接进行向量搜索来解决这一瓶颈。然而，高精度、高维度的嵌入向量与 CiM 低精度、低维度的阵列约束（如 2 位单元、512x512 阵列）之间存在“表示鸿沟”，限制了其在 RAG 中的应用。现有的数据整形方法将维度压缩和量化分开处理，导致数据保真度下降，且难以区分性能损失源于电路设计还是输入数据。本文提出 CQ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Artificial intelligence and multi-omics convergence in breast cancer: Revolutionizing diagnosis, prognostication, and precision oncology.](https://pubmed.ncbi.nlm.nih.gov/41616992/)
  来源：PubMed | 日期：2026-04-01 | 相关度：3.75 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Breast cancer (BC) is a highly heterogeneous malignancy and remains a major cause of cancer-related mortality among women worldwide. Advances in multi-omics profiling spanning genomics, transcriptomics, epigenomics, prot...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Multi-omics biomarkers in psychiatric disorders diagnosis and stratification.](https://pubmed.ncbi.nlm.nih.gov/41655615/)
  来源：PubMed | 日期：2026-04-01 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：The precise diagnosis and stratification of psychiatric disorders remain formidable challenges in modern medicine, hindered by the absence of objective biomarkers and reliance on subjective clinical criteria. Recent adva...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Comparative evaluation of multimodal point-of-care tests to differentiate gram-negative from gram-positive infections in critically ill adults: a diagnostic accuracy study.](https://pubmed.ncbi.nlm.nih.gov/41535672/)
  来源：PubMed | 日期：2026-04-01 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Patients with suspected sepsis often receive broad-spectrum antibiotics before culture results are available. A rapid point-of-care test (POCT) that indicates Gram-negative (GN) versus Gram-positive (GP) infection could ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Link Prediction for Event Logs in the Process Industry](http://arxiv.org/abs/2508.09096v3)
  来源：arXiv | 日期：2025-08-12 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：在基于图的检索增强生成（RAG）时代，链路预测是提升领域特定数据质量的关键预处理步骤。流程工业中的知识管理利用 RAG 应用优化运营并确保安全，但面临交接班日志（shift books）中事件记录碎片化的挑战，即属于同一事件的相关记录往往被分散存储。这种碎片化阻碍了向生产现场用户推荐既往解决方案。为解决该问题，本研究开发了一种记录链接模型，并将其定义为跨文档共指消解（CDCR）任务。该模型结合了先进的 CDCR 模型与自然语言推理（NL...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。
