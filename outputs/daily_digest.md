# 每日论文监控日报 (2026-03-31)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 33 篇新论文。

## 抓取状态

- arXiv：成功，命中 37 篇
- PubMed：成功，命中 16 篇
- bioRxiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='api.biorxiv.org', port=443): Read timed out. (read timeout=60)
- medRxiv：成功，命中 6 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [ORACAL: A Robust and Explainable Multimodal Framework for Smart Contract Vulnerability Detection with Causal Graph Enrichment](http://arxiv.org/abs/2603.28128v1)
  来源：arXiv | 日期：2026-03-30 | 相关度：6.8 | 新颖度：7.11
  匹配主题：foundation_model_agent
  中文摘要：Although Graph Neural Networks (GNNs) have shown promise for smart contract vulnerability detection, they still face significant limitations. Homogeneous graph models fail to capture the interplay between control flow an...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Seeing the Scene Matters: Revealing Forgetting in Video Understanding Models with a Scene-Aware Long-Video Benchmark](http://arxiv.org/abs/2603.27259v1)
  来源：arXiv | 日期：2026-03-28 | 相关度：6.8 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Long video understanding (LVU) remains a core challenge in multimodal learning. Although recent vision-language models (VLMs) have made notable progress, existing benchmarks mainly focus on either fine-grained perception...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Comparative Study in Surgical AI: Datasets, Foundation Models, and Barriers to Med-AGI](https://www.medrxiv.org/content/10.64898/2026.03.26.26349455v1)
  来源：medRxiv | 日期：2026-03-28 | 相关度：6.8 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：近年来，AI在多项生物医学任务中已达到或超越人类专家水平，但在外科图像分析基准上表现滞后。外科手术需要整合多模态数据、人类交互及物理效应，因此通用AI模型作为协作工具具有巨大潜力。然而，尽管每年产生数百万小时的手术视频，但数据准备需要极高的专业知识，且训练成本高昂。本研究以2026年最先进的AI方法为基础，针对神经外科手术器械检测进行了案例研究。结果显示，即使是拥有数十亿参数的模型并经过广泛训练，目前的视觉语言模型（VLM）在简单的器械...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Med.ai ASK: an agentic system for biomedical question answering.](https://pubmed.ncbi.nlm.nih.gov/41911379/)
  来源：PubMed | 日期：2026-03-30 | 相关度：6.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Intelligent agent-driven research co-pilots, leveraging advances in generative AI, are transforming how scientists access biomedical knowledge. This paper presents Med.ai ASK, an agentic question-answering system designe...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Heterogeneous Debate Engine: Identity-Grounded Cognitive Architecture for Resilient LLM-Based Ethical Tutoring](http://arxiv.org/abs/2603.27404v1)
  来源：arXiv | 日期：2026-03-28 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) are being increasingly used as autonomous agents in complex reasoning tasks, opening the niche for dialectical interactions. However, Multi-Agent systems implemented with systematically uncon...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [What an Autonomous Agent Discovers About Molecular Transformer Design: Does It Transfer?](http://arxiv.org/abs/2603.28015v1)
  来源：arXiv | 日期：2026-03-30 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Deep learning models for drug-like molecules and proteins overwhelmingly reuse transformer architectures designed for natural language, yet whether molecular sequences benefit from different designs has not been systemat...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Building evidence-based knowledge graphs from full-text literature for disease-specific biomedical reasoning](http://arxiv.org/abs/2603.28325v1)
  来源：arXiv | 日期：2026-03-30 | 相关度：6.15 | 新颖度：7.54
  匹配主题：foundation_model_agent
  中文摘要：Biomedical knowledge resources often either preserve evidence as unstructured text or compress it into flat triples that omit study design, provenance, and quantitative support. Here we present EvidenceNet, a framework a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Red-MIRROR: Agentic LLM-based Autonomous Penetration Testing with Reflective Verification and Knowledge-augmented Interaction](http://arxiv.org/abs/2603.27127v1)
  来源：arXiv | 日期：2026-03-28 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Web applications remain the dominant attack surface in cybersecurity, where vulnerabilities such as SQL injection, XSS, and business logic flaws continue to cause significant data breaches. While penetration testing is e...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Poisoning the Genome: Targeted Backdoor Attacks on DNA Foundation Models](http://arxiv.org/abs/2603.27465v1)
  来源：arXiv | 日期：2026-03-29 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Genomic foundation models trained on DNA sequences have demonstrated remarkable capabilities across diverse biological tasks, from variant effect prediction to genome design. These models are typically trained on massive...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AstraAI: LLMs, Retrieval, and AST-Guided Assistance for HPC Codebases](http://arxiv.org/abs/2603.27423v1)
  来源：arXiv | 日期：2026-03-28 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：We present AstraAI, a command-line interface (CLI) coding framework for high-performance computing (HPC) software development. AstraAI operates directly within a Linux terminal and integrates large language models (LLMs)...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CausalEvolve: Towards Open-Ended Discovery with Causal Scratchpad](http://arxiv.org/abs/2603.14575v2)
  来源：arXiv | 日期：2026-03-15 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：AlphaEvolve 等基于进化的智能体在利用大语言模型（LLMs）构建“AI 科学家”方面取得了显著进展。这些智能体通过迭代改进和演化程序，利用 LLM 的先验知识和推理能力来解决开放式科学问题。然而，现有方法缺乏针对性的演化指导，且无法有效组织和利用过去的演化经验，导致演化效率下降，并在接近性能边界时出现振荡。为弥补这一缺陷，本研究开发了 CausalEvolve，其核心是配备了“因果草稿卡”（Causal Scratchpad）...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Toward AI foundation models for epidemics: Promise, challenges, and paths forward.](https://pubmed.ncbi.nlm.nih.gov/41824492/)
  来源：PubMed | 日期：2026-03-31 | 相关度：4.4 | 新颖度：4.81
  匹配主题：pathogenomics
  中文摘要：基础模型（如 GPT、GenCast、AlphaFold）正在改变科学发现，但在流行病建模领域尚未实现类似变革。传统模型通常针对特定病原体，在应对如 SARS-CoV-2 等突发疫情时难以快速生成洞察。本文探讨了将基础模型范式扩展到流行病学的可能性：即构建一个能捕捉跨病原体、人群和环境的传染病动力学共享原理的预训练模型。该模型仅需少量数据即可微调至新场景，实现快速预测、推理和响应，对资源匮乏地区尤为重要。文章指出，流行病学见解与现代 A...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CiQi-Agent: Aligning Vision, Tools and Aesthetics in Multimodal Agent for Cultural Reasoning on Chinese Porcelains](http://arxiv.org/abs/2603.28474v1)
  来源：arXiv | 日期：2026-03-30 | 相关度：2.75 | 新颖度：8.18
  匹配主题：foundation_model_agent
  中文摘要：针对中国古代瓷器鉴定对历史专业知识和审美敏感度的高要求，本文推出了 CiQi-Agent，这是一个专门用于瓷器智能分析的领域特定多模态 Agent。该 Agent 支持多图输入，集成了视觉工具调用与多模态检索增强生成（RAG）技术，能够针对朝代、年号、窑口、釉色、纹饰和器型六个维度进行细粒度鉴定分析。为实现此能力，研究者构建了大规模专家标注数据集 CiQi-VQA，包含 29,596 件瓷器标本、51,553 张图像及 557,940 ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Retromorphic Testing with Hierarchical Verification for Hallucination Detection in RAG](http://arxiv.org/abs/2603.27752v1)
  来源：arXiv | 日期：2026-03-29 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：大语言模型在检索增强生成（RAG）中仍存在幻觉问题，即生成与检索上下文不符或冲突的陈述。现有的检测方法多为粗粒度的答案级评分，缺乏细粒度的证据诊断。本文提出 RT4CHART 框架，用于评估 RAG 输出对上下文的忠实度。该框架将模型输出分解为独立的可验证断言，并针对检索上下文进行从局部到全局的分层验证。每个断言被标记为蕴含（entailed）、矛盾（contradicted）或无根据（baseless）。RT4CHART 还能将断言级...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Towards Hyper-Efficient RAG Systems in VecDBs: Distributed Parallel Multi-Resolution Vector Search](http://arxiv.org/abs/2511.16681v2)
  来源：arXiv | 日期：2025-11-12 | 相关度：6.8 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) systems have become a dominant approach to augment large language models (LLMs) with external knowledge. However, existing vector database (VecDB) retrieval pipelines rely on flat or ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [VaaS is a Multi-Layer Hallucination Reduction Pipeline for AI-Assisted Science: Production Validation and Prospective Benchmarking](https://www.medrxiv.org/content/10.64898/2026.03.24.26348935v1)
  来源：medRxiv | 日期：2026-03-30 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：The deployment of large language models (LLMs) for science carries an intrinsic risk: hallucination of citations, fabricated drug approvals or clinical trials, and unsupported experimental outcomes. Here we describe the ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Exqutor: Extended Query Optimizer for Vector-augmented Analytical Queries](http://arxiv.org/abs/2512.09695v4)
  来源：arXiv | 日期：2025-12-10 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Vector similarity search is becoming increasingly important for data science pipelines, particularly in Retrieval-Augmented Generation (RAG), where it enhances large language model inference by enabling efficient retriev...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Visualization of Machine Learning Models through Their Spatial and Temporal Listeners](http://arxiv.org/abs/2603.27527v1)
  来源：arXiv | 日期：2026-03-29 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Model visualization (ModelVis) has emerged as a major research direction, yet existing taxonomies are largely organized by data or tasks, making it difficult to treat models as first-class analysis objects. We present a ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Towards a Medical AI Scientist](http://arxiv.org/abs/2603.28589v1)
  来源：arXiv | 日期：2026-03-30 | 相关度：5.75 | 新颖度：7.16
  匹配主题：foundation_model_agent
  中文摘要：Autonomous systems that generate scientific hypotheses, conduct experiments, and draft manuscripts have recently emerged as a promising paradigm for accelerating discovery. However, existing AI Scientists remain largely ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Multilingual Medical Reasoning for Question Answering with Large Language Models](http://arxiv.org/abs/2512.05658v2)
  来源：arXiv | 日期：2025-12-05 | 相关度：5.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) with reasoning capabilities have recently demonstrated strong potential in medical Question Answering (QA). Existing approaches are largely English-focused and primarily rely on distillation ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Q-BIOLAT: Binary Latent Protein Fitness Landscapes for QUBO-Based Optimization](http://arxiv.org/abs/2603.27526v1)
  来源：arXiv | 日期：2026-03-29 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Protein fitness optimization is inherently a discrete combinatorial problem, yet most learning-based approaches rely on continuous representations and are primarily evaluated through predictive accuracy. We introduce Q-B...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Courtroom-Style Multi-Agent Debate with Progressive RAG and Role-Switching for Controversial Claim Verification](http://arxiv.org/abs/2603.28488v1)
  来源：arXiv | 日期：2026-03-30 | 相关度：5.45 | 新颖度：7.71
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) remain unreliable for high-stakes claim verification due to hallucinations and shallow reasoning. While retrieval-augmented generation (RAG) and multi-agent debate (MAD) address this, they ar...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Self-evolving AI agents for protein discovery and directed evolution](http://arxiv.org/abs/2603.27303v1)
  来源：arXiv | 日期：2026-03-28 | 相关度：5.1 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Protein scientific discovery is bottlenecked by the manual orchestration of information and algorithms, while general agents are insufficient in complex domain projects. VenusFactory2 provides an autonomous framework tha...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Mitigating Hallucination on Hallucination in RAG via Ensemble Voting](http://arxiv.org/abs/2603.27253v1)
  来源：arXiv | 日期：2026-03-28 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) aims to reduce hallucinations in Large Language Models (LLMs) by integrating external knowledge. However, RAG introduces a critical challenge: hallucination on hallucination," where f...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Measuring the Unmeasurable: A Diagnostic Sensor for AI Reasoning Pathology in Sequential Clinical Decision-Making](https://www.medrxiv.org/content/10.64898/2026.03.27.26349583v1)
  来源：medRxiv | 日期：2026-03-30 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models achieve impressive accuracy on medical benchmarks that present clinical information as complete vignettes, but their behavior under sequential information delivery, the standard mode of real clinica...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Link Prediction for Event Logs in the Process Industry](http://arxiv.org/abs/2508.09096v3)
  来源：arXiv | 日期：2025-08-12 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：在基于图的检索增强生成（RAG）时代，链路预测是提升领域特定数据质量的关键预处理步骤。流程工业中的知识管理利用 RAG 应用优化运营并确保安全，但面临交接班日志（shift books）中事件记录碎片化的挑战，即属于同一事件的相关记录往往被分散存储。这种碎片化阻碍了向生产现场用户推荐既往解决方案。为解决该问题，本研究开发了一种记录链接模型，并将其定义为跨文档共指消解（CDCR）任务。该模型结合了先进的 CDCR 模型与自然语言推理（NL...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Graph Vector Field: A Unified Framework for Multimodal Health Risk Assessment from Heterogeneous Wearable and Environmental Data Streams](http://arxiv.org/abs/2603.28115v1)
  来源：arXiv | 日期：2026-03-30 | 相关度：3.05 | 新颖度：5.8
  匹配主题：foundation_model_agent
  中文摘要：数字健康研究在动态图疾病模型、单纯复形拓扑学习和多模态专家混合架构（MoE）方面取得了进展，但这些领域仍处于割裂状态。本文提出图向量场（GVF）框架，将健康风险建模为随时间变化的单纯复形上的向量值场，结合了离散微分几何算子与模态结构化的专家混合模型。风险被表示为向量值上链（cochain），其演化由 Hodge 拉普拉斯算子和离散外演算算子参数化，通过 Helmholtz-Hodge 分解为势驱动（恰当）、循环类（余恰当）和拓扑约束（调...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BIOGEN: Evidence-Grounded Multi-Agent Reasoning Framework for Transcriptomic Interpretation in Antimicrobial Resistance](http://arxiv.org/abs/2510.16082v3)
  来源：arXiv | 日期：2025-10-17 | 相关度：2.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：从 RNA-seq 数据中解释基因簇仍具挑战，尤其是在需要机制背景来生成假设的抗生素耐药性（AMR）研究中。传统的富集方法（如 ORA）利用预定义类别总结共表达模块，但结果往往稀疏，且缺乏针对特定基因簇的文献关联解释。本研究提出 BIOGEN，这是一个基于证据的多智能体（Multi-agent）框架，用于 RNA-seq 转录模块的事后解释。该框架集成了生物医学检索、结构化推理和多评论员验证机制，将来自 PubMed 和 UniProt...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [GAAMA: Graph Augmented Associative Memory for Agents](http://arxiv.org/abs/2603.27910v1)
  来源：arXiv | 日期：2026-03-29 | 相关度：2.1 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：跨多会话与用户交互的 AI 智能体需要持久的长期记忆。现有方法如扁平化检索增强生成（RAG）或向量检索，难以捕捉多轮对话中的结构化关联。本文提出 GAAMA，一种图增强关联记忆系统，通过三步流水线构建概念介导的分层知识图谱：1）保留原始对话的逐字片段；2）利用 LLM 提取原子事实和主题级概念节点；3）合成高阶反思。该图谱包含四种节点类型（片段、事实、反思、概念）和五种结构化边，其中概念节点提供跨越式遍历路径。检索过程结合了基于余弦相似...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PubMed Reasoner: Dynamic Reasoning-based Retrieval for Evidence-Grounded Biomedical Question Answering](http://arxiv.org/abs/2603.27335v1)
  来源：arXiv | 日期：2026-03-28 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：可信的生物医学问答（QA）系统不仅需要准确的答案，还需提供可验证的证据。现有的检索增强（RAG）方法缺乏迭代优化查询的机制，而自我反思方法通常在检索完成后才介入。为此，我们提出了 PubMed Reasoner，这是一个包含三个阶段的生物医学问答智能体：1）自我批判查询优化：基于部分检索到的元数据，评估 MeSH 词的覆盖范围、对齐度和冗余度，以增强 PubMed 查询；2）反思性检索：分批处理文章，直到收集到足够的证据；3）基于证据的...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Accelerating Scientific Discovery with Autonomous Goal-evolving Agents](http://arxiv.org/abs/2512.21782v2)
  来源：arXiv | 日期：2025-12-25 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：科学发现智能体通常通过优化科学家指定的定量目标函数来扩展研究边界，但这些目标往往只是不完善的代理指标。本文提出科学自主目标演化智能体（SAGA）以解决目标函数自动化设计的核心需求。SAGA 采用双层架构：外层循环由大语言模型（LLM）智能体组成，负责分析优化结果、提出新目标并将其转化为可计算的评分函数；内层循环则在当前目标下执行方案优化。这种设计实现了对目标空间及其权衡关系的系统性探索，而非将其视为固定输入。研究在抗生素、纳米抗体、功能...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Entropic Claim Resolution: Uncertainty-Driven Evidence Selection for RAG](http://arxiv.org/abs/2603.28444v1)
  来源：arXiv | 日期：2026-03-30 | 相关度：0.7 | 新颖度：6.86
  匹配主题：未命中具体主题
  中文摘要：现有的检索增强生成（RAG）系统主要依赖基于相关性的稠密检索，通过顺序获取文档来最大化与查询的语义相似度。然而，在存在证据冲突或查询本身具有歧义的知识密集型现实场景中，仅靠相关性不足以解决认知不确定性。本文提出了熵权声明解析（ECR），这是一种新型推理算法，将 RAG 推理重新定义为竞争性语义答案假设上的熵最小化过程。与 ReAct 等动作驱动的智能体框架或固定流水线 RAG 架构不同，ECR 通过最大化期望熵减（EER）这一信息价值决...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [FACTUM: Mechanistic Detection of Citation Hallucination in Long-Form RAG](http://arxiv.org/abs/2601.05866v4)
  来源：arXiv | 日期：2026-01-09 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）模型常受引用幻觉困扰，即模型引用的来源实际无法支持其生成的主张。本研究将此类失效重新定义为注意力（读取路径）与前馈网络（召回路径）之间随模型规模演变的协调失败，而非简单的参数知识过度依赖。我们提出了 FACTUM 框架，通过四种机制评分来验证引用可信度：上下文对齐（CAS）、注意力汇聚使用（BAS）、参数力（PFS）和路径对齐（PAS）。分析显示，正确的引用通常具有更高的参数力（PFS）和更强的注意力汇聚（BAS）...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。
