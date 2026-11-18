# 每日论文监控日报 (2026-11-18)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 40 篇新论文。

## 抓取状态

- arXiv：成功，命中 45 篇
- PubMed：成功，命中 28 篇
- bioRxiv：成功，命中 10 篇
- medRxiv：成功，命中 8 篇

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [EcoToxFred: A knowledge-graph-grounded conversational agent for exploring ecotoxicological monitoring and hazard data](https://www.biorxiv.org/content/10.1101/2025.07.04.663152v2)
  来源：bioRxiv | 日期：2026-11-15 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Assessing chemical risks to aquatic ecosystems requires the joint interpretation of monitoring data, ecotoxicity data, and derived risk indicators, yet such integrated data are rarely accessible to users without database...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evaluating Language Models as Orchestrators in a Tool-First Biomedical Discovery Platform](https://www.biorxiv.org/content/10.64898/2026.11.13.766436v1)
  来源：bioRxiv | 日期：2026-11-16 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) increasingly orchestrate agentic biomedical discovery systems, but cloud deployment raises concerns about inference cost, data privacy, and governance. Small language models (SLMs) that run o...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Inventa: Decentralized Self-Improving Agents for Autonomous Scientific Discovery](http://arxiv.org/abs/2611.21847v1)
  来源：arXiv | 日期：2026-11-16 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Large language model (LLM) agents can generate research ideas and improve scientific discovery through iterative experimentation. However, increasing the number of agents or iterations does not automatically translate to...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ToolFlood: Beyond Selection -- Hiding Valid Tools from LLM Agents via Semantic Covering](http://arxiv.org/abs/2603.13950v2)
  来源：arXiv | 日期：2026-03-14 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large Language Model (LLM) agents increasingly use external tools for complex tasks and rely on embedding-based retrieval to select a small top-$k$ subset for reasoning. Prior work on attacking these systems competes for...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Retrieving Complementary Evidence for Multi-Hop RAG with Semantic Gain Graphs](http://arxiv.org/abs/2610.15285v2)
  来源：arXiv | 日期：2026-10-11 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Multi-hop retrieval-augmented generation (RAG) requires finding documents whose evidence is useful in combination. Query relevance and graph connectivity help locate related content, but neither directly measures the add...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evaluation of System One Models on Biomedical Texts](https://www.medrxiv.org/content/10.64898/2026.11.15.26368126v1)
  来源：medRxiv | 日期：2026-11-17 | 相关度：5.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Objective To compare the performance and cost of System One models (SOMs) with general-purpose large language models (LLMs) on biomedical tasks and evaluate confidence-based routing. Materials and Methods We evaluated th...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Human-Agentic AI Collaboration Workflow for Trend Analysis of ChatGPT Applications in Healthcare](https://www.medrxiv.org/content/10.64898/2026.11.14.26368120v1)
  来源：medRxiv | 日期：2026-11-17 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Background: With the rapid advancement of artificial intelligence (AI), large language models (LLMs) such as ChatGPT have demonstrated strong potential to transform healthcare research and practice. However, LLMs are pro...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Enhancing Stock Market Information Retrieval with Retrieval-Augmented Generation](http://arxiv.org/abs/2611.03747v2)
  来源：arXiv | 日期：2026-11-02 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Natural Language Processing (NLP) has been widely applied in financial domains, enabling automated analysis and retrieval of stock market information. However, traditional NLP-based systems often struggle with maintainin...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Multi-Granularity Context-Enhanced RAG over Multimodal Knowledge Graphs](http://arxiv.org/abs/2608.25986v2)
  来源：arXiv | 日期：2026-08-26 | 相关度：6.8 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Knowledge graph (KG)-based retrieval-augmented generation (RAG) leverages structured knowledge to provide large language models (LLMs) with high-quality external information. Building on these works, recent studies have ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [StitchRAG: Constructing Compact and Evidence-Preserving Contexts for RAG with Diffusion-Based Stitching](http://arxiv.org/abs/2611.22766v1)
  来源：arXiv | 日期：2026-11-17 | 相关度：4.75 | 新颖度：6.6
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) improves factuality by grounding large language models (LLMs) in external evidence. However, long retrieved contexts incur computational overhead and can even hurt performance due to ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Auditing the adversarial robustness of genomic foundation models with SafeGenes.](https://pubmed.ncbi.nlm.nih.gov/43044595/)
  来源：PubMed | 日期：2026-11-17 | 相关度：4.65 | 新颖度：6.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Genomic foundation models (GFMs) such as evolutionary scale modeling (ESM) are increasingly applied to variant effect prediction in clinical genomics, yet their adversarial robustness remains underexplored. We present Sa...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 其他

- [When Detection Does Not Guarantee Resistance: Reasoning and Poisoned Context in RAG](http://arxiv.org/abs/2608.17153v5)
  来源：arXiv | 日期：2026-08-17 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) exposes large language models to knowledge-poisoning attacks, where misinformation injected into retrieved documents can influence model outputs. Prior work has shown that models may ...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [System 1 agents: a method for local, reliable and fast agentic AI](http://arxiv.org/abs/2611.21053v1)
  来源：arXiv | 日期：2026-11-16 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Agentic artificial intelligence could automate analyses of sensitive clinical data, but current agents depend on large language models (LLMs). Cloud LLMs expose patient data. Local LLMs hallucinate, and an invented value...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond Synthetic Benchmarks: Evaluating LLM Performance on Real-World Class-Level Code Generation](http://arxiv.org/abs/2510.26130v3)
  来源：arXiv | 日期：2025-10-30 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have advanced rapidly from well-studied function-level code generation to emerging repository-level approaches, yet this progression reveals a critical gap: class-level code generation, which...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Discovering formally verified quantum programs with AI](http://arxiv.org/abs/2611.09822v3)
  来源：arXiv | 日期：2026-11-06 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：The timeline by which quantum computers can solve breakthrough problems in science depends on improved quantum algorithms as much as on better hardware. Such algorithmic advances are typically achieved through many years...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AI Companions for Young Adult Caregivers: Practical Advice, Emotional Depth, and the Limits of Metric Evaluation](http://arxiv.org/abs/2611.23147v1)
  来源：arXiv | 日期：2026-11-17 | 相关度：2.5 | 新颖度：8.09
  匹配主题：未命中具体主题
  中文摘要：Young adult caregivers (YACs) are individuals aged 18 to 25 currently taking care of a family member, partner, or friend facing chronic illness. AI companions designed specifically for YACs remain underexplored in prior ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [GAAMA: Graph Augmented Associative Memory for Agents](http://arxiv.org/abs/2603.27910v3)
  来源：arXiv | 日期：2026-03-29 | 相关度：2.1 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：AI agents that talk with users across many sessions need long-term memory to stay coherent and personalized. Existing approaches use either flat retrieval-augmented generation (RAG) that ignores how memories connect, or ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [In-Context Optimization for Retrieval-Augmented Generation: A Gradient-Descent Perspective](http://arxiv.org/abs/2605.26356v2)
  来源：arXiv | 日期：2026-05-25 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：In-context learning has recently been linked to implicit gradient descent in linear self-attention models, suggesting that context can induce a forward-pass update. Retrieval-augmented generation (RAG) also relies on con...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RAG in a Trenchcoat: When Minimal Memory Is Enough for Agentic Systems, and When It Isn't](http://arxiv.org/abs/2611.22179v1)
  来源：arXiv | 日期：2026-11-17 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Agentic memory research has accumulated extraction, supersession, reflection, and graph synthesis on top of retrieval-augmented generation. However, we found that almost none of those primitives earn their cost in our te...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [GuardAgent: A Memory-Augmented Agentic Framework for Adaptive Detection of Adversarial Promotions in LLM-Based Recommendation](http://arxiv.org/abs/2611.22274v1)
  来源：arXiv | 日期：2026-11-17 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：In traditional recommender systems (RSs), textual information typically serves as auxiliary signals for representation learning. In contrast, in LLM-based RSs, textual information becomes the primary medium for recommend...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Autonomous Science Bench: Evaluating AI Agents for Autonomous Scientific Discovery](http://arxiv.org/abs/2610.18449v2)
  来源：arXiv | 日期：2026-10-13 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：AI agents for autonomous scientific discovery must decide which experiments to run under a limited budget. Most benchmarks for science agents provide fixed datasets, while others that support active experimentation large...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SIRI: Self-Internalizing Reinforcement Learning with Intrinsic Skills for LLM Agent Training](http://arxiv.org/abs/2606.02355v2)
  来源：arXiv | 日期：2026-06-01 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Long-horizon LLM agents can benefit from reusable skills, yet existing skill-based methods often rely on external skill generators during training or persistent skill retrieval at inference, increasing engineering comple...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Towards Agentic Scientific Discovery in Distributed Systems](http://arxiv.org/abs/2611.20031v1)
  来源：arXiv | 日期：2026-11-15 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：We investigate when adaptive tool selection helps identify a shared equation across clients with different input coverage. Query-ATLAS (query-conditioned Agentic Tool-based Learning for Aggregating Symbolic Equations) us...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [DeepCDS: Ab initio coding sequence prediction in prokaryotic metagenomic short reads](https://www.biorxiv.org/content/10.64898/2026.06.17.732633v3)
  来源：bioRxiv | 日期：2026-11-15 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Accurate coding sequence prediction in short prokaryotic metagenomic sequences, such as Illumina reads, remains challenging due to sequence fragmentation, unknown sequence origins, and sequencing errors. Here we introduc...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Know Thy Neighbour: Benchmarking Protein Language Model Embedding-Based Annotation Reveals Anisotropy Substantially Impacts Retrieval](https://www.biorxiv.org/content/10.64898/2026.11.13.766344v1)
  来源：bioRxiv | 日期：2026-11-16 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Functional annotation using protein language models (`pLMs') usually proceeds by transferring the function of a query's nearest neighbour in a reference database. A major drawback is that embedding-based annotation trans...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Attribute or Abstain: Evaluating Evidence-Grounded Retrieval on the Low-Resource African Business Web](http://arxiv.org/abs/2611.19900v1)
  来源：arXiv | 日期：2026-11-15 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented systems that research companies are judged by how much they find, yet in markets where public evidence is sparse, a confident answer without support costs more than no answer. We introduce AfriBizClai...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [OpenClassGen: A Large-Scale Corpus of Real-World Python Classes for LLM Research](http://arxiv.org/abs/2504.15564v4)
  来源：arXiv | 日期：2025-04-22 | 相关度：1.4 | 新颖度：1.5
  匹配主题：未命中具体主题
  中文摘要：Existing class-level code generation datasets are either synthetic (ClassEval: 100 classes) or insufficient in scale for modern training needs (RealClassEval: 400 classes), hindering robust evaluation and empirical analy...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [StringQFT: A Multiuse Textbook Resource for AI-Assisted Theoretical Physics](http://arxiv.org/abs/2611.23225v1)
  来源：arXiv | 日期：2026-11-17 | 相关度：0.7 | 新颖度：7.5
  匹配主题：未命中具体主题
  中文摘要：We present StringQFT as a textbook collection for string constructions of quantum field theory and as infrastructure for AI-assisted theoretical physics. The collection comprises 18 volumes, 190 chapters and 3,795 pages,...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [TUSI: A Citation-Grounded Graph-Based Benchmark](http://arxiv.org/abs/2611.21823v1)
  来源：arXiv | 日期：2026-11-16 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Evaluating retrieval-augmented generation (RAG) systems in Persian law remains challenging because benchmarks lack realism, grounding, and coverage of legal reasoning. Existing resources are either synthetically generate...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Noise-Space Reward Alignment for Few-Step Generative Models](http://arxiv.org/abs/2610.21125v2)
  来源：arXiv | 日期：2026-10-15 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Few-step generative models produce high-quality samples in one or a few evaluations. However, steering them toward desired properties remains difficult, especially when only black-box reward evaluations are available. Wh...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Estimating Outpatient Visit Prices from Hospital Price Transparency Data using Large Language Models](http://arxiv.org/abs/2611.20261v1)
  来源：arXiv | 日期：2026-11-15 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Objective: Hospital care prices in the United States have increased substantially, yet patients lack effective tools to access and compare costs. We aimed to develop and evaluate an LLM-based approach for improving acces...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ViSAR: Training-Free Adaptive-$k$ Retrieval for Document Visual Question Answering](http://arxiv.org/abs/2609.02486v3)
  来源：arXiv | 日期：2026-09-02 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Document Visual Question Answering (DocVQA) often leverages Retrieval-Augmented Generation (RAG), where late-interaction encoders are commonly used to identify document pages relevant to a user query, before answer gener...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SGR3 Model: Scene Graph Retrieval-Reasoning Model in 3D](http://arxiv.org/abs/2603.04614v2)
  来源：arXiv | 日期：2026-03-04 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：3D scene graphs provide a structured representation of object entities and their relationships, enabling high-level interpretation and reasoning for robots while remaining intuitively understandable to humans. Existing a...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CogRec: Structure-Cognitive Fast-and-Slow Reasoning for Generative Recommendation](http://arxiv.org/abs/2607.24402v2)
  来源：arXiv | 日期：2026-07-27 | 相关度：2.05 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Generative recommendation reformulates next-item prediction as identifier sequence generation, yet existing methods mainly treat the generated identifiers as target sequences to be memorized, leaving their hierarchical a...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RagHarnessDebugger: Jev-Guided Agentic RAG in Contract Inference Repair Auditing](http://arxiv.org/abs/2611.22991v1)
  来源：arXiv | 日期：2026-11-17 | 相关度：1.4 | 新颖度：6.77
  匹配主题：未命中具体主题
  中文摘要：Agentic systems using retrieval-augmented generation (RAG) must repair their own answers by gathering more evidence, testing alternative policies and deciding if, when, and what repairs are needed. Yet how do we know if ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Beating Hateful Narratives on Social Media with Facts: Retrieval-Augmented Counter-Speech Generation](http://arxiv.org/abs/2510.12316v2)
  来源：arXiv | 日期：2025-10-14 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Online hate speech threatens social cohesion by amplifying discrimination and harmful narratives against marginalized communities. While counter-speech (CS) - fact-based, respectful responses to hate - offers a construct...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Somatic mutation probabilities learned from the DNA sequence](https://www.biorxiv.org/content/10.64898/2026.11.13.766380v1)
  来源：bioRxiv | 日期：2026-11-16 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Somatic mutations distribute heterogeneously over genomes, dependent on immediate sequence context, function, and non-genetic factors. Mutations present the foundation for somatic genome evolution towards age-related dis...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [OICycle: Observe, Infer, and Intervene Cycle for Belief-State Learning in Longitudinal Clinical Decision Making](http://arxiv.org/abs/2611.22826v1)
  来源：arXiv | 日期：2026-11-17 | 相关度：3.05 | 新颖度：6.7
  匹配主题：foundation_model_agent
  中文摘要：Clinical care is a closed loop: clinicians observe partial evidence, infer the patient's state, and intervene, and each intervention determines what is observed next. This makes clinical decision making a partially obser...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [HEmIF-Bench: Benchmarking H&E-to-mIF Models BeyondVirtual-StainFidelity](http://arxiv.org/abs/2611.19905v1)
  来源：arXiv | 日期：2026-11-15 | 相关度：1.7 | 新颖度：1.75
  匹配主题：未命中具体主题
  中文摘要：Hematoxylin and eosin (H&E)-to-multiplex immunofluorescence (mIF) generators predict spatial protein expression from routine histology, yet pixel-level marker reconstruction does not establish downstream utility. We pres...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Security of Deep Research Agents: Attack Surface, Defenses, Benchmarks, and Agenda Seeding against Research Planning](http://arxiv.org/abs/2611.20045v1)
  来源：arXiv | 日期：2026-11-15 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Deep research and agentic search agents autonomously retrieve content from the open web and generate reports with citations, and their outputs are often taken directly as research conclusions. This paper systematizes sec...
  为什么值得看：Security of Deep Research Agents: Attack 与你的主题有弱匹配，暂时保留作低优先级跟踪。
