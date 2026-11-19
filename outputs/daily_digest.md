# 每日论文监控日报 (2026-11-19)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 46 篇新论文。

## 抓取状态

- arXiv：成功，命中 47 篇
- PubMed：成功，命中 34 篇
- bioRxiv：成功，命中 13 篇
- medRxiv：成功，命中 8 篇

## 最值得看

### Foundation Model / Agent

- [GenNA: Conditional generation of nucleotide sequences guided by natural language annotations.](https://pubmed.ncbi.nlm.nih.gov/43050525/)
  来源：PubMed | 日期：2026-11-20 | 相关度：8.5 | 新颖度：10.0
  匹配主题：foundation_model_agent
  中文摘要：Deciphering the mapping between biomolecular sequences and complex biological functions is a central challenge in genomics. While existing generative nucleotide models capture sequence distributions, they lack explicit a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [LUNA-FM: a subword foundation model for long non-coding RNAs for functional inference.](https://pubmed.ncbi.nlm.nih.gov/43023405/)
  来源：PubMed | 日期：2026-12-01 | 相关度：7.55 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：RNA foundation models (FMs) have shown promise for RNA identification and functional annotation. However, many use single-nucleotide tokenization, which produces long input sequences and can increase computational costs ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Hybrid RAG Framework for Deceptive Review Detection: Integrating RoBERTa-LoRA, FAISS-Based Retrieval, and LLM Reasoning](http://arxiv.org/abs/2611.24049v1)
  来源：arXiv | 日期：2026-11-18 | 相关度：6.55 | 新颖度：6.2
  匹配主题：foundation_model_agent
  中文摘要：The growth of deceptive online opinions poses a critical risk of misinformation and fraud. This paper proposes a Retrieval-Augmented Generation (RAG) system to automatically distinguish spam reviews. The architecture int...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Large language models recover archival pathology data and identify NSE as a candidate prognostic marker in Ewing sarcoma](https://www.biorxiv.org/content/10.64898/2026.02.20.707103v3)
  来源：bioRxiv | 日期：2026-11-16 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Background: Current risk stratification for Ewing sarcoma relies heavily on clinical factors such as metastatic status, failing to capture histologic heterogeneity as a potential prognostic indicator. Although pathology ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evaluating Language Models as Orchestrators in a Tool-First Biomedical Discovery Platform](https://www.biorxiv.org/content/10.64898/2026.11.13.766436v1)
  来源：bioRxiv | 日期：2026-11-16 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) increasingly orchestrate agentic biomedical discovery systems, but cloud deployment raises concerns about inference cost, data privacy, and governance. Small language models (SLMs) that run o...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The Effectiveness and Durability of Pretraining Data Filtering in Protein Language Models](http://arxiv.org/abs/2610.26651v2)
  来源：arXiv | 日期：2026-10-19 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Pretraining filtering is one of the most common safeguards for open-weight language models. Here we study its effectiveness, durability and scalability using the ESM-2 family of protein language models. We find that filt...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HYPER: Hypothesis-Guided Planning for Evidence-Seeking Retrieval](http://arxiv.org/abs/2603.19008v2)
  来源：arXiv | 日期：2026-03-19 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) improves Large Language Models (LLMs) by grounding generation in external, non-parametric knowledge. However, when a task requires choosing among competing possibilities, such as a di...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Glyph: An Interpretability Engine for AI-Driven Scientific Discovery from Clinical Data](http://arxiv.org/abs/2611.08922v2)
  来源：arXiv | 日期：2026-11-06 | 相关度：4.45 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Automated scientific discovery has the potential to advance understanding of disease mechanisms and accelerate identification of early disease markers. Manual data annotation is infeasible at population scale, motivating...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [KnowledgeClaw: Towards Agentic Knowledge Engineering via Omnimodal Hypergraphs](http://arxiv.org/abs/2611.24294v1)
  来源：arXiv | 日期：2026-11-18 | 相关度：3.45 | 新颖度：6.82
  匹配主题：foundation_model_agent
  中文摘要：Knowledge engineering (KE) turns raw files into a reasoning-ready knowledge base, a task now within reach of LLM agents. KE has progressed from chunk and graph retrieval-augmented generation (RAG) to memory agents, agent...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Language-guided domain adaptation improves protein sequence representations for antimicrobial resistance analysis](https://www.biorxiv.org/content/10.64898/2026.11.04.764426v3)
  来源：bioRxiv | 日期：2026-11-16 | 相关度：10.0 | 新颖度：1.0
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent, application_monitoring
  中文摘要：Antimicrobial resistance (AMR) in bacterial pathogens complicates infectious disease management. Protein sequences encode molecular features underlying resistance functions such as antibiotic inactivation and drug efflux...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Multi-Granularity Context-Enhanced RAG over Multimodal Knowledge Graphs](http://arxiv.org/abs/2608.25986v2)
  来源：arXiv | 日期：2026-08-26 | 相关度：6.8 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Knowledge graph (KG)-based retrieval-augmented generation (RAG) leverages structured knowledge to provide large language models (LLMs) with high-quality external information. Building on these works, recent studies have ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Lacuna: Cryptic Binding Pocket Discovery via Conformational Ensemble Analysis](https://www.biorxiv.org/content/10.64898/2026.08.14.744956v3)
  来源：bioRxiv | 日期：2026-11-16 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Lacuna, an open-source Python tool for discovering cryptic binding pockets: sites that are absent or too small to detect in the unbound structure of a protein, RNA or DNA and open only during conformational fluctuation. ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Evidence-Based Credit Assignment for Search-Augmented Language Models](http://arxiv.org/abs/2611.23824v1)
  来源：arXiv | 日期：2026-11-18 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Reinforcement learning from terminal answer rewards enables search-augmented language models to interleave reasoning and retrieval without step-level annotations, yet outcome supervision assigns identical credit to every...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Agentic AI versus pediatric emergency physicians for differential diagnosis of acutely ill and injured children](https://www.medrxiv.org/content/10.64898/2026.11.16.26367440v1)
  来源：medRxiv | 日期：2026-11-18 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Background Misdiagnosis and delayed diagnosis of children in pediatric emergency departments lead to complications, and are particularly problematic in settings with limited pediatric expertise. Large language models (LL...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [TCC-RAG: Temporal Causal Chain-Guided RAG for Temporal Knowledge Graph Question Answering](http://arxiv.org/abs/2610.38366v2)
  来源：arXiv | 日期：2026-10-28 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in large language models (LLMs) have spurred growing interest in temporal knowledge graph question answering (TKGQA). Most existing methods rely on semantic retrieval augmented generation (RAG), which suf...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [System 1 agents: a method for local, reliable and fast agentic AI](http://arxiv.org/abs/2611.21053v1)
  来源：arXiv | 日期：2026-11-16 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Agentic artificial intelligence could automate analyses of sensitive clinical data, but current agents depend on large language models (LLMs). Cloud LLMs expose patient data. Local LLMs hallucinate, and an invented value...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Inventa: Decentralized Self-Improving Agents for Autonomous Scientific Discovery](http://arxiv.org/abs/2611.21847v1)
  来源：arXiv | 日期：2026-11-16 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Large language model (LLM) agents can generate research ideas and improve scientific discovery through iterative experimentation. However, increasing the number of agents or iterations does not automatically translate to...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ToolFlood: Beyond Selection -- Hiding Valid Tools from LLM Agents via Semantic Covering](http://arxiv.org/abs/2603.13950v2)
  来源：arXiv | 日期：2026-03-14 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large Language Model (LLM) agents increasingly use external tools for complex tasks and rely on embedding-based retrieval to select a small top-$k$ subset for reasoning. Prior work on attacking these systems competes for...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Retrieving Complementary Evidence for Multi-Hop RAG with Semantic Gain Graphs](http://arxiv.org/abs/2610.15285v2)
  来源：arXiv | 日期：2026-10-11 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Multi-hop retrieval-augmented generation (RAG) requires finding documents whose evidence is useful in combination. Query relevance and graph connectivity help locate related content, but neither directly measures the add...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evaluation of System One Models on Biomedical Texts](https://www.medrxiv.org/content/10.64898/2026.11.15.26368126v1)
  来源：medRxiv | 日期：2026-11-17 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Objective To compare the performance and cost of System One models (SOMs) with general-purpose large language models (LLMs) on biomedical tasks and evaluate confidence-based routing. Materials and Methods We evaluated th...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Human-Agentic AI Collaboration Workflow for Trend Analysis of ChatGPT Applications in Healthcare](https://www.medrxiv.org/content/10.64898/2026.11.14.26368120v1)
  来源：medRxiv | 日期：2026-11-17 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Background: With the rapid advancement of artificial intelligence (AI), large language models (LLMs) such as ChatGPT have demonstrated strong potential to transform healthcare research and practice. However, LLMs are pro...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Discovering formally verified quantum programs with AI](http://arxiv.org/abs/2611.09822v3)
  来源：arXiv | 日期：2026-11-06 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：The timeline by which quantum computers can solve breakthrough problems in science depends on improved quantum algorithms as much as on better hardware. Such algorithmic advances are typically achieved through many years...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EcoXAI: Autonomous Agentic Ecosystem for Explainable Artificial Intelligence and Biomedical Discovery](https://www.biorxiv.org/content/10.64898/2026.07.08.737358v5)
  来源：bioRxiv | 日期：2026-11-16 | 相关度：3.1 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：随着生物医学数据集和知识图谱在规模与复杂性上的增长，从海量数据中提取可操作见解成为研究瓶颈。EcoXAI 引入了一种模块化、可定制且容器化的多智能体（Multi-agent）系统，旨在利用智能体编排和循环工程的最新进展，同时解决 AI 幻觉和工作流碎片化问题。该系统将分析过程结构化为明确的流水线执行阶段，降低了临床和转化研究人员的计算门槛。EcoXAI 采用执行驱动的自主框架取代了单一的 AI 文本界面，利用专门的生物信息学智能体提供基...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AI Companions for Young Adult Caregivers: Practical Advice, Emotional Depth, and the Limits of Metric Evaluation](http://arxiv.org/abs/2611.23147v1)
  来源：arXiv | 日期：2026-11-17 | 相关度：2.5 | 新颖度：1.5
  匹配主题：未命中具体主题
  中文摘要：Young adult caregivers (YACs) are individuals aged 18 to 25 currently taking care of a family member, partner, or friend facing chronic illness. AI companions designed specifically for YACs remain underexplored in prior ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Toward Agentic Retrieval-Augmented Generation for Enterprise Retail Workflows over Heterogeneous Data Sources](http://arxiv.org/abs/2610.25096v3)
  来源：arXiv | 日期：2026-10-18 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Enterprise retail workflows require agents to chain evidence across heterogeneous sources, from structured product and order records to unstructured inquiries and reviews, yet existing agentic RAG benchmarks rarely captu...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Capability Framework for Evaluating Agentic AI Platforms in Regulated Enterprises](http://arxiv.org/abs/2611.24039v1)
  来源：arXiv | 日期：2026-11-18 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Agentic AI platforms-systems in which LLM agents plan, invoke tools, retain memory and coordinate to change the state of enterprise systems-are being procured faster than they can be measured. Public agent benchmarks sco...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MemeLogos: Knowledge-Driven Retrieval-Augmented Reasoning for Harmful Meme Detection](http://arxiv.org/abs/2610.15463v3)
  来源：arXiv | 日期：2026-10-11 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：With the rapid proliferation of social media, harmful memes have become a growing threat to online ecosystems. Their harmfulness is often implicitly conveyed through complex interactions among visual, textual, and contex...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Ethical Risks of Medical AI Agents and a Governance Framework: A Systematic Review of Current Applications and Policy Responses.](https://pubmed.ncbi.nlm.nih.gov/43048115/)
  来源：PubMed | 日期：2026-11-17 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：This systematic review identified ethical risks associated with medical AI agents and developed a governance framework adapted to China's healthcare context. PubMed, Web of Science, China National Knowledge Infrastructur...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [In-Context Optimization for Retrieval-Augmented Generation: A Gradient-Descent Perspective](http://arxiv.org/abs/2605.26356v2)
  来源：arXiv | 日期：2026-05-25 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：In-context learning has recently been linked to implicit gradient descent in linear self-attention models, suggesting that context can induce a forward-pass update. Retrieval-augmented generation (RAG) also relies on con...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RAG in a Trenchcoat: When Minimal Memory Is Enough for Agentic Systems, and When It Isn't](http://arxiv.org/abs/2611.22179v1)
  来源：arXiv | 日期：2026-11-17 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Agentic memory research has accumulated extraction, supersession, reflection, and graph synthesis on top of retrieval-augmented generation. However, we found that almost none of those primitives earn their cost in our te...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [GuardAgent: A Memory-Augmented Agentic Framework for Adaptive Detection of Adversarial Promotions in LLM-Based Recommendation](http://arxiv.org/abs/2611.22274v1)
  来源：arXiv | 日期：2026-11-17 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：In traditional recommender systems (RSs), textual information typically serves as auxiliary signals for representation learning. In contrast, in LLM-based RSs, textual information becomes the primary medium for recommend...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SIRI: Self-Internalizing Reinforcement Learning with Intrinsic Skills for LLM Agent Training](http://arxiv.org/abs/2606.02355v2)
  来源：arXiv | 日期：2026-06-01 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Long-horizon LLM agents can benefit from reusable skills, yet existing skill-based methods often rely on external skill generators during training or persistent skill retrieval at inference, increasing engineering comple...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Know Thy Neighbour: Benchmarking Protein Language Model Embedding-Based Annotation Reveals Anisotropy Substantially Impacts Retrieval](https://www.biorxiv.org/content/10.64898/2026.11.13.766344v1)
  来源：bioRxiv | 日期：2026-11-16 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Functional annotation using protein language models (`pLMs') usually proceeds by transferring the function of a query's nearest neighbour in a reference database. A major drawback is that embedding-based annotation trans...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Enhancing Stock Market Information Retrieval with Retrieval-Augmented Generation](http://arxiv.org/abs/2611.03747v2)
  来源：arXiv | 日期：2026-11-02 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Natural Language Processing (NLP) has been widely applied in financial domains, enabling automated analysis and retrieval of stock market information. However, traditional NLP-based systems often struggle with maintainin...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [TUSI: A Citation-Grounded Graph-Based Benchmark](http://arxiv.org/abs/2611.21823v1)
  来源：arXiv | 日期：2026-11-16 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Evaluating retrieval-augmented generation (RAG) systems in Persian law remains challenging because benchmarks lack realism, grounding, and coverage of legal reasoning. Existing resources are either synthetically generate...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [StringQFT: A Multiuse Textbook Resource for AI-Assisted Theoretical Physics](http://arxiv.org/abs/2611.23225v1)
  来源：arXiv | 日期：2026-11-17 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：We present StringQFT as a textbook collection for string constructions of quantum field theory and as infrastructure for AI-assisted theoretical physics. The collection comprises 18 volumes, 190 chapters and 3,795 pages,...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Noise-Space Reward Alignment for Few-Step Generative Models](http://arxiv.org/abs/2610.21125v2)
  来源：arXiv | 日期：2026-10-15 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Few-step generative models produce high-quality samples in one or a few evaluations. However, steering them toward desired properties remains difficult, especially when only black-box reward evaluations are available. Wh...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ViSAR: Training-Free Adaptive-$k$ Retrieval for Document Visual Question Answering](http://arxiv.org/abs/2609.02486v3)
  来源：arXiv | 日期：2026-09-02 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Document Visual Question Answering (DocVQA) often leverages Retrieval-Augmented Generation (RAG), where late-interaction encoders are commonly used to identify document pages relevant to a user query, before answer gener...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [StitchRAG: Constructing Compact and Evidence-Preserving Contexts for RAG with Diffusion-Based Stitching](http://arxiv.org/abs/2611.22766v1)
  来源：arXiv | 日期：2026-11-17 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) improves factuality by grounding large language models (LLMs) in external evidence. However, long retrieved contexts incur computational overhead and can even hurt performance due to ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Auditing the adversarial robustness of genomic foundation models with SafeGenes.](https://pubmed.ncbi.nlm.nih.gov/43044595/)
  来源：PubMed | 日期：2026-11-17 | 相关度：4.65 | 新颖度：1.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Genomic foundation models (GFMs) such as evolutionary scale modeling (ESM) are increasingly applied to variant effect prediction in clinical genomics, yet their adversarial robustness remains underexplored. We present Sa...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Beating Hateful Narratives on Social Media with Facts: Retrieval-Augmented Counter-Speech Generation](http://arxiv.org/abs/2510.12316v2)
  来源：arXiv | 日期：2025-10-14 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Online hate speech threatens social cohesion by amplifying discrimination and harmful narratives against marginalized communities. While counter-speech (CS) - fact-based, respectful responses to hate - offers a construct...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RagHarnessDebugger: Jev-Guided Agentic RAG in Contract Inference Repair Auditing](http://arxiv.org/abs/2611.22991v1)
  来源：arXiv | 日期：2026-11-17 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Agentic systems using retrieval-augmented generation (RAG) must repair their own answers by gathering more evidence, testing alternative policies and deciding if, when, and what repairs are needed. Yet how do we know if ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Somatic mutation probabilities learned from the DNA sequence](https://www.biorxiv.org/content/10.64898/2026.11.13.766380v1)
  来源：bioRxiv | 日期：2026-11-16 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Somatic mutations distribute heterogeneously over genomes, dependent on immediate sequence context, function, and non-genetic factors. Mutations present the foundation for somatic genome evolution towards age-related dis...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [OICycle: Observe, Infer, and Intervene Cycle for Belief-State Learning in Longitudinal Clinical Decision Making](http://arxiv.org/abs/2611.22826v1)
  来源：arXiv | 日期：2026-11-17 | 相关度：3.05 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Clinical care is a closed loop: clinicians observe partial evidence, infer the patient's state, and intervene, and each intervention determines what is observed next. This makes clinical decision making a partially obser...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [When Detection Does Not Guarantee Resistance: Reasoning and Poisoned Context in RAG](http://arxiv.org/abs/2608.17153v5)
  来源：arXiv | 日期：2026-08-17 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) exposes large language models to knowledge-poisoning attacks, where misinformation injected into retrieved documents can influence model outputs. Prior work has shown that models may ...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [Quantifying the Intrusiveness of Retrofitting Retrieval-Augmented Generation onto Legacy Software Systems](http://arxiv.org/abs/2611.23931v1)
  来源：arXiv | 日期：2026-11-18 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Enterprises increasingly add retrieval-augmented generation (RAG) to existing REST and monolithic systems, usually by writing an ad hoc HTTP call into a handler, and have no way to quantify how intrusive that choice is. ...
  为什么值得看：Quantifying the Intrusiveness of Retrofi 与你的主题有弱匹配，暂时保留作低优先级跟踪。
