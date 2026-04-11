# 每日论文监控日报 (2026-04-11)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 49 篇新论文。

## 抓取状态

- arXiv：成功，命中 42 篇
- PubMed：成功，命中 40 篇
- bioRxiv：成功，命中 30 篇
- medRxiv：成功，命中 1 篇

## 最值得看

### Foundation Model / Agent

- [Figures as Interfaces: Toward LLM-Native Artifacts for Scientific Discovery](http://arxiv.org/abs/2604.08491v1)
  来源：arXiv | 日期：2026-04-09 | 相关度：7.9 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are transforming scientific workflows, not only through their generative capabilities but also through their emerging ability to use tools, reason about data, and coordinate complex analytica...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Efficient and Effective Internal Memory Retrieval for LLM-Based Healthcare Prediction](http://arxiv.org/abs/2604.07659v1)
  来源：arXiv | 日期：2026-04-08 | 相关度：7.15 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) hold significant promise for healthcare, yet their reliability in high-stakes clinical settings is often compromised by hallucinations and a lack of granular medical context. While Retrieval ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [STAnalyzer: Transparent Spatial Transcriptomics Analysis via an Agentic Architecture](https://www.biorxiv.org/content/10.64898/2026.04.06.716827v1)
  来源：bioRxiv | 日期：2026-04-09 | 相关度：8.5 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Spatial transcriptomics enables high resolution profiling of gene expression within spatial contexts, yet its potential is often hindered by fragmented toolchains, intricate parameters, and cognitive bottlenecks of inter...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [WildAlert: A Real-Time, AI-Driven Early Warning System for Wildlife Health and Ecological Threat Detection](https://www.biorxiv.org/content/10.64898/2026.04.07.716505v1)
  来源：bioRxiv | 日期：2026-04-10 | 相关度：9.2 | 新颖度：5.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent, application_monitoring
  中文摘要：Emerging infections and environmental disruptions increasingly threaten wildlife and ecosystem health. Free-ranging wildlife often serve as early indicators of ecological instability, making timely detection of morbidity...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 可追踪

### Foundation Model / Agent

- [A survey on large language models in biology and chemistry.](https://pubmed.ncbi.nlm.nih.gov/41258076/)
  来源：PubMed | 日期：2026-04-08 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：人工智能正通过提供适应生物系统复杂性的可扩展计算框架重塑生物医学研究。其核心是生物/化学语言模型（包括大语言模型），这些模型将分子结构重新概念化为一种适用于先进计算技术的“语言”。本文批判性地审视了这些模型在生物学和化学中的作用，追踪了其从分子表示到分子生成与优化的演变。综述涵盖了生物大分子和有机小分子的关键表示策略，包括蛋白质和核苷酸序列、单细胞数据、基于字符串的化学格式、基于图的编码以及三维点云，并分析了其在AI应用中的优劣。讨论进...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Towards Effective Long Video Understanding of Multimodal Large Language Models via One-shot Clip Retrieval](http://arxiv.org/abs/2512.08410v2)
  来源：arXiv | 日期：2025-12-09 | 相关度：6.8 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Due to excessive memory overhead, most Multimodal Large Language Models (MLLMs) can only process videos of limited frames. In this paper, we propose an effective and efficient paradigm to remedy this shortcoming, termed ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SUPERGLASSES: Benchmarking Vision Language Models as Intelligent Agents for AI Smart Glasses](http://arxiv.org/abs/2602.22683v2)
  来源：arXiv | 日期：2026-02-26 | 相关度：6.8 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：The rapid advancement of AI-powered smart glasses-one of the hottest wearable devices-has unlocked new frontiers for multimodal interaction, with Visual Question Answering (VQA) over external knowledge sources emerging a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CLEAR: Context Augmentation from Contrastive Learning of Experience via Agentic Reflection](http://arxiv.org/abs/2604.07487v1)
  来源：arXiv | 日期：2026-04-08 | 相关度：6.55 | 新颖度：6.7
  匹配主题：foundation_model_agent
  中文摘要：Large language model agents rely on effective model context to obtain task-relevant information for decision-making. Many existing context engineering approaches primarily rely on the context generated from the past expe...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multi-Agent Orchestration for High-Throughput Materials Screening on a Leadership-Class System](http://arxiv.org/abs/2604.07681v1)
  来源：arXiv | 日期：2026-04-09 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：The integration of Artificial Intelligence (AI) with High-Performance Computing (HPC) is transforming scientific workflows from human-directed pipelines into adaptive systems capable of autonomous decision-making. Large ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Detecting RAG Advertisements Across Advertising Styles](http://arxiv.org/abs/2603.04925v2)
  来源：arXiv | 日期：2026-03-05 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) enable a new form of advertising for retrieval-augmented generation (RAG) systems in which organic responses are blended with contextually relevant ads. The prospect of such "generated native...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions](http://arxiv.org/abs/2604.08304v1)
  来源：arXiv | 日期：2026-04-09 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) significantly enhances large language models (LLMs) but introduces novel security risks through external knowledge access. While existing studies cover various RAG vulnerabilities, th...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Automated Extraction and Meta-Analysis of a Century of Motor-Unit Research with NeuromechaniX](https://www.biorxiv.org/content/10.64898/2026.04.08.717204v1)
  来源：bioRxiv | 日期：2026-04-10 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：The scientific literature on human motor units and electromyography (EMG) spans over a century (1925-2025), comprising research impossible to synthesize manually. We introduce NeuromechaniX, a domain-specific platform fo...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [One Shot Dominance: Knowledge Poisoning Attack on Retrieval-Augmented Generation Systems](http://arxiv.org/abs/2505.11548v4)
  来源：arXiv | 日期：2025-05-15 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) enhanced with Retrieval-Augmented Generation (RAG) have shown improved performance in generating accurate responses. However, the dependence on external knowledge bases introduces potential s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SubSearch: Intermediate Rewards for Unsupervised Guided Reasoning in Complex Retrieval](http://arxiv.org/abs/2604.07415v1)
  来源：arXiv | 日期：2026-04-08 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are probabilistic in nature and perform more reliably when augmented with external information. As complex queries often require multi-step reasoning over the retrieved information, with no c...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [From Binary Groundedness to Support Relations: Towards a Reader-Centred Taxonomy for Comprehension of AI Output](http://arxiv.org/abs/2604.08082v1)
  来源：arXiv | 日期：2026-04-09 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Generative AI tools often answer questions using source documents, e.g., through retrieval augmented generation. Current groundedness and hallucination evaluations largely frame the relationship between an answer and its...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [DCD: Domain-Oriented Design for Controlled Retrieval-Augmented Generation](http://arxiv.org/abs/2604.07590v1)
  来源：arXiv | 日期：2026-04-08 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) is widely used to ground large language models in external knowledge sources. However, when applied to heterogeneous corpora and multi-step queries, Naive RAG pipelines often degrade ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [KEO: Knowledge Extraction on OMIn via Knowledge Graphs and RAG for Safety-Critical Aviation Maintenance](http://arxiv.org/abs/2510.05524v2)
  来源：arXiv | 日期：2025-10-07 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：We present Knowledge Extraction on OMIn (KEO), a domain-specific knowledge extraction and reasoning framework with large language models (LLMs) in safety-critical contexts. Using the Operations and Maintenance Intelligen...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Causal Prediction of TP53 Variant Pathogenicity Using a Perturbation-Informed Protein Language Model.](https://pubmed.ncbi.nlm.nih.gov/41955512/)
  来源：PubMed | 日期：2026-04-09 | 相关度：10.0 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：准确预测变异的功能影响对于理解人类疾病（特别是 TP53 等癌症相关基因）至关重要。尽管高通量突变分析提升了变异效应预测（VEP）能力，但通用型模型在错义突变分类上仍存在局限。本研究开发了 CaVepP53，这是一种针对 TP53 特化的预测模型，通过扰动实验变异数据对蛋白质语言模型（PLM）进行微调。该模型通过计算野生型与突变体嵌入向量之间的欧几里得距离，并结合逻辑变换推导置信度评分，实现对突变致病性的量化分类。基准测试表明，CaVe...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ViralMap: Predicting Features in Viral Proteins from Primary Sequence](https://www.biorxiv.org/content/10.64898/2026.04.07.716565v1)
  来源：bioRxiv | 日期：2026-04-09 | 相关度：7.65 | 新颖度：5.75
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Modern viral vaccines are designed to elicit an immune response against viral proteins that mediate infection, making those proteins important targets for characterization and engineering. To improve vaccine efficacy, th...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Towards a Universal Foundation Model for Protein Dynamics: A Multi-Chain Tree-Structured Framework with Transformer Propagators](http://arxiv.org/abs/2502.05909v2)
  来源：arXiv | 日期：2025-02-09 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Simulating large-scale protein dynamics using traditional all-atom molecular dynamics (MD) remains computationally prohibitive. We present a unified, universal framework for coarse-grained molecular dynamics (CG-MD) that...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Sampling protein structural token space enables accurate prediction of multiple conformations](https://www.biorxiv.org/content/10.64898/2026.03.03.708411v2)
  来源：bioRxiv | 日期：2026-04-08 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Protein function is fundamentally mediated by ensembles of distinct metastable states. However, existing methods, such as AlphaFold 3, typically exhibit a bias toward predicting a single dominant state, failing to captur...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Structure-Based and Stability-Validated Prioritization of BACE1 Inhibitors Integrating Meta-Ensemble QSAR and Molecular Dynamics](https://www.biorxiv.org/content/10.64898/2026.04.07.716920v1)
  来源：bioRxiv | 日期：2026-04-10 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Alzheimers disease remains an unmet therapeutic challenge, and no {beta}-secretase (BACE1) inhibitor has achieved clinical approval. A major limitation of prior discovery efforts is reliance on single-parameter optimizat...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Learning to Search: A Decision-Based Agent for Knowledge-Based Visual Question Answering](http://arxiv.org/abs/2604.07146v2)
  来源：arXiv | 日期：2026-04-08 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Knowledge-based visual question answering (KB-VQA) requires vision-language models to understand images and use external knowledge, especially for rare entities and long-tail facts. Most existing retrieval-augmented gene...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Quantifying Scientific Consensus in Biomedical Hypotheses via LLM-Assisted Literature Screening](https://www.biorxiv.org/content/10.64898/2026.04.06.716861v1)
  来源：bioRxiv | 日期：2026-04-09 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Systematic literature reviews are labor-intensive tasks in biomedical research. While Large Language Models (LLMs) using Retrieval-Augmented Generation (RAG) techniques have enhanced information accessibility, the inhere...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Guaranteeing Knowledge Integration with Joint Decoding for Retrieval-Augmented Generation](http://arxiv.org/abs/2604.08046v1)
  来源：arXiv | 日期：2026-04-09 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) significantly enhances Large Language Models (LLMs) by providing access to external knowledge. However, current research primarily focuses on retrieval quality, often overlooking the ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 其他

- [Efficient Federated Search for Retrieval-Augmented Generation using Lightweight Routing](http://arxiv.org/abs/2502.19280v2)
  来源：arXiv | 日期：2025-02-26 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) achieve remarkable performance across domains but remain prone to hallucinations and inconsistencies. Retrieval-augmented generation (RAG) mitigates these issues by augmenting model inputs wi...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Active Hypothesis Testing under Computational Budgets with Applications to GWAS and LLM](http://arxiv.org/abs/2512.01423v2)
  来源：arXiv | 日期：2025-12-01 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：In large-scale hypothesis testing, computing exact $p$-values or $e$-values is often resource-intensive, creating a need for budget-aware inferential methods. We propose a general framework for active hypothesis testing ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Title: Multimodal profiling reveals Mycobacterium tuberculosis restricts lung mitochondrial immunometabolism to promote pathogenesis](https://www.biorxiv.org/content/10.64898/2026.04.07.717012v1)
  来源：bioRxiv | 日期：2026-04-10 | 相关度：3.05 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Early events in the lung that shape protective immune responses to M. tuberculosis (Mtb) infection are not well understood but are critical for developing better vaccines and immunomodulatory therapies for tuberculosis. ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HyperMem: Hypergraph Memory for Long-Term Conversations](http://arxiv.org/abs/2604.08256v1)
  来源：arXiv | 日期：2026-04-09 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：长期记忆对于对话智能体维持连贯性、跟踪持久任务以及在长对话中提供个性化交互至关重要。然而，现有的检索增强生成（RAG）和基于图的存储方法主要依赖成对关系，难以捕捉多个元素之间的联合依赖等高阶关联，导致检索结果碎片化。为此，我们提出了 HyperMem，一种基于超图的分层存储架构，利用超边显式建模此类关联。HyperMem 将存储结构化为主题（topics）、情节（episodes）和事实（facts）三个层面，并通过超边将相关情节及其事...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ReRec: Reasoning-Augmented LLM-based Recommendation Assistant via Reinforcement Fine-tuning](http://arxiv.org/abs/2604.07851v1)
  来源：arXiv | 日期：2026-04-09 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：随着大语言模型（LLM）的兴起，开发能够处理复杂查询并提供个性化、推理驱动建议的智能推荐助手需求日益增长。尽管基于 LLM 的推荐系统展现出潜力，但在多步推理方面仍面临挑战。为此，我们提出了 ReRec，一种新型强化微调（RFT）框架，旨在提升 LLM 在复杂推荐任务中的推理能力。该框架包含三个核心组件：(1) 双图增强奖励塑造，整合了 NDCG@K 等推荐指标以及查询对齐和偏好对齐分数，为 LLM 优化提供细粒度奖励信号；(2) 推理...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Progressive Multimodal Search and Reasoning for Knowledge-Intensive Visual Question Answering](http://arxiv.org/abs/2509.00798v6)
  来源：arXiv | 日期：2025-08-31 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：知识密集型视觉问答（VQA）需要图像内容之外的外部知识，要求精确的视觉定位以及视觉与文本信息的连贯整合。尽管多模态检索增强生成（RAG）通过引入外部知识库取得了显著进展，但现有方法多采用单次处理框架，往往无法获取充足知识，且缺乏修正错误推理的机制。本文提出 PMSR（渐进式多模态搜索与推理）框架，通过逐步构建结构化推理轨迹来增强知识获取与综合。PMSR 利用基于最新记录和整体轨迹的双范围查询，从异构知识库中检索多样化知识。随后，通过组合...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PRIME: Training Free Proactive Reasoning via Iterative Memory Evolution for User-Centric Agent](http://arxiv.org/abs/2604.07645v1)
  来源：arXiv | 日期：2026-04-08 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：在复杂长程任务的人机协作中，开发自主工具使用智能体已成为前沿课题。多轮交互中用户需求的动态性和不确定性带来了巨大挑战，智能体不仅要调用工具，还需通过有效沟通迭代完善对用户意图的理解。尽管强化学习有所进展，但现有方法训练成本高昂，且在长程交互中难以进行轮次级的信用分配。为此，我们提出 PRIME（通过迭代记忆演化的主动推理），这是一种无梯度学习框架，通过显式经验积累而非昂贵的参数优化实现智能体持续进化。PRIME 将多轮交互轨迹提炼为结构...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [ChunQiuTR: Time-Keyed Temporal Retrieval in Classical Chinese Annals](http://arxiv.org/abs/2604.06997v1)
  来源：arXiv | 日期：2026-04-08 | 相关度：4.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval shapes how language models access and ground knowledge in retrieval-augmented generation (RAG). In historical research, the target is often not an arbitrary relevant passage, but the exact record for a specific...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [A Systematic Study of Retrieval Pipeline Design for Retrieval-Augmented Medical Question Answering](http://arxiv.org/abs/2604.07274v1)
  来源：arXiv | 日期：2026-04-08 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have demonstrated strong capabilities in medical question answering; however, purely parametric models often suffer from knowledge gaps and limited factual grounding. Retrieval-augmented gene...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [OpenClassGen: A Large-Scale Corpus of Real-World Python Classes for LLM Research](http://arxiv.org/abs/2504.15564v2)
  来源：arXiv | 日期：2025-04-22 | 相关度：1.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：针对现有类级代码生成数据集规模不足（如 ClassEval 仅 100 个类，RealClassEval 仅 400 个类）限制模型评估的问题，本文推出了 OpenClassGen，这是一个包含从 2,970 个开源项目中提取的 324,843 个 Python 类的大规模语料库。该数据集将人工编写的类与包含签名及文档字符串的自包含骨架配对，并集成了涵盖复杂性、耦合度、内聚性和继承属性的 27 项静态代码指标。研究者在包含 300 个类...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Mitigating Hallucination on Hallucination in RAG via Ensemble Voting](http://arxiv.org/abs/2603.27253v2)
  来源：arXiv | 日期：2026-03-28 | 相关度：4.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) aims to reduce hallucinations in Large Language Models (LLMs) by integrating external knowledge. However, RAG introduces a critical challenge: hallucination on hallucination," where f...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Enhancing Multilingual RAG Systems with Debiased Language Preference-Guided Query Fusion](http://arxiv.org/abs/2601.02956v2)
  来源：arXiv | 日期：2026-01-06 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Multilingual Retrieval-Augmented Generation (mRAG) systems often exhibit a perceived preference for high-resource languages, particularly English, resulting in the widespread adoption of English pivoting. While prior stu...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Representation, Alignment, and Generation: A Comprehensive Survey of Foundation Models for Non-Invasive Brain Decoding](https://www.biorxiv.org/content/10.64898/2025.11.30.691403v2)
  来源：bioRxiv | 日期：2026-04-08 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：The ability to decode human thoughts, intentions, and perceptions directly from non-invasive brain recordings holds transformative potential for healthcare, communication, and human-computer interaction. However, transla...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [DTCRS: Dynamic Tree Construction for Recursive Summarization](http://arxiv.org/abs/2604.07012v1)
  来源：arXiv | 日期：2026-04-08 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) mitigates the hallucination problem of Large Language Models (LLMs) by incorporating external knowledge. Recursive summarization constructs a hierarchical summary tree by clustering t...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Modification-aware AI enables terminal chemical modifications for peptide design and discovers potent antimicrobials](https://www.biorxiv.org/content/10.64898/2026.04.09.717597v1)
  来源：bioRxiv | 日期：2026-04-10 | 相关度：3.35 | 新颖度：5.5
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Antimicrobial resistance (AMR) is an escalating global health threat, intensifying the urgent need for novel antibiotics. Here, we introduce Termini, a generative machine learning (ML) framework that integrates peptide g...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A Massively Scalable Ligand-Protein Dissociation Dynamic Database Derived from Atomistic Molecular Modelling](http://arxiv.org/abs/2604.06761v1)
  来源：arXiv | 日期：2026-04-08 | 相关度：2.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：药物-蛋白质相互作用的动力学对药物设计至关重要，但该领域目前缺乏大规模动态数据。本研究推出了 DD-03B，这是一个大规模可扩展数据库，提供广泛配体-蛋白质复合物的全原子解离动力学轨迹。利用并扩展了经过验证的计算流程，研究者为来自 PDBbind+v2020R1 的 19,037 个复合物生成了解离轨迹，包含约 3 亿个模拟帧，总数据量达 40 TB。针对这些具有实验结合亲和力（kd）但通常缺乏实测解离速率（koff）的系统，研究通过轨...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AI-Guided Structure-Aware Modeling and Thermal Proteomics Reveal Direct Demethylzeylasteral-ACLY Interaction](https://www.biorxiv.org/content/10.64898/2026.04.07.717093v1)
  来源：bioRxiv | 日期：2026-04-08 | 相关度：1.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：鉴定生物活性天然产物的直接分子靶点是化学生物学的核心挑战。本研究提出了一种集成实验与计算的闭环框架，结合基质增强热蛋白质组学与整体图神经网络（HoloGNN），用于系统地筛选并验证蛋白质-配体相互作用。HoloGNN 在 PDBbind 数据集基准测试中达到了当前最先进（SOTA）的性能。研究人员将该框架应用于 50 种结构多样的天然产物，成功鉴定出去甲基扁蒴藤素（Demethylzeylasteral）是 ACLY（三磷酸腺苷柠檬酸裂...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Co-design for Trustworthy AI: An Interpretable and Explainable Tool for Type 2 Diabetes Prediction Using Genomic Polygenic Risk Scores](http://arxiv.org/abs/2604.08217v1)
  来源：arXiv | 日期：2026-04-09 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：多基因风险评分（PRS）是量化复杂性状和临床疾病遗传易感性的重要方法，已在肥胖、癌症和2型糖尿病（T2DM）的早期筛查与个性化治疗中展现出潜力。然而，PRS 目前面临缺乏可解释性工具的局限。为解决此问题，首尔大学研究团队开发了 eXplainable PRS (XPRS) 可视化工具。该工具利用 Shapley Additive Explanations (SHAP) 算法将 PRS 分解为基因级和单核苷酸多态性（SNP）贡献得分，为驱...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Rag Performance Prediction for Question Answering](http://arxiv.org/abs/2604.07985v1)
  来源：arXiv | 日期：2026-04-09 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：本研究针对问答任务中检索增强生成（RAG）相对于不使用 RAG 时的性能增益预测问题展开探讨。研究评估了多种最初为即时检索设计的检索前（pre-retrieval）和检索后（post-retrieval）预测指标。此外，研究还分析了几种生成后（post-generation）预测指标，并提出了一种在该研究中表现最佳的新型预测方法。实验结果表明，最有效的预测方案是一种新型监督学习预测器，该预测器通过显式建模问题、检索到的段落以及生成的答案...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AnomalyAgent: Agentic Industrial Anomaly Synthesis via Tool-Augmented Reinforcement Learning](http://arxiv.org/abs/2604.07900v1)
  来源：arXiv | 日期：2026-04-09 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：工业异常生成是缓解异常检测任务中数据稀缺问题的关键。现有方法多依赖单步生成机制，缺乏复杂推理与迭代优化能力，难以生成语义真实的异常样本。本文提出 AnomalyAgent，一种具备自我反思、知识检索和迭代改进能力的异常合成智能体。该智能体配备了提示词生成（PG）、图像生成（IG）、质量评估（QE）、知识检索（KR）和掩码生成（MG）五种工具，实现了闭环优化。为提升决策与反思能力，研究者利用真实异常图像构建结构化轨迹，并设计了监督微调（S...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [DQA: Diagnostic Question Answering for IT Support](http://arxiv.org/abs/2604.05350v2)
  来源：arXiv | 日期：2026-04-07 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：企业 IT 支持交互本质上具有诊断性质，需要从模糊的用户报告中通过迭代收集证据来识别根本原因。虽然检索增强生成（RAG）能提供历史案例参考，但标准多轮 RAG 系统缺乏明确的诊断状态，难以在多轮对话中积累证据并解决相互竞争的假设。本文提出 DQA（诊断问答）框架，该框架维持持久的诊断状态，并在根本原因层面（而非单个文档层面）聚合检索到的案例。DQA 结合了对话式查询重写、检索聚合和状态条件响应生成，以支持在企业延迟和上下文限制下的系统化...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Leveraging LLMs and Heterogeneous Knowledge Graphs for Persona-Driven Session-Based Recommendation](http://arxiv.org/abs/2604.06928v1)
  来源：arXiv | 日期：2026-04-08 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：基于会话的推荐系统（SBRS）旨在从交互序列中捕捉用户的短期意图，但匿名会话的假设限制了其在数据稀疏或冷启动场景下的个性化能力。本文提出一种画像驱动的 SBRS 框架，通过异构知识图谱（KG）显式建模从交互中推断的潜在用户画像，并将其整合至数据驱动的推荐流程中。该框架采用两阶段架构：个性化信息提取与利用。在提取阶段，构建整合了用户-项目、项目-项目、项目-特征关联及 DBpedia 元数据的异构 KG，并利用大语言模型（LLM）生成的项...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [CRISPR/Cas12a: A Comprehensive Review from Structural Foundations to Applications in Nucleic Acid Precision Detection.](https://pubmed.ncbi.nlm.nih.gov/41889087/)
  来源：PubMed | 日期：2026-04-08 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：CRISPR/Cas12a 技术凭借其独特的反向切割（trans-cleavage）活性，已从基因编辑工具演变为强大的分子检测工具。本文系统阐述了 Cas12a 的结构基础与分子机制，重点探讨了该技术如何将特定核酸识别转化为级联信号放大。其应用涵盖病原体诊断、物种鉴定、食品安全及中药材鉴别。通过与等温扩增及多模态检测平台集成，Cas12a 推动了分子诊断向便携化、可视化和定量化方向发展。文章进一步讨论了在灵敏度、定量准确性、crRNA ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Why teaching resists automation in an AI-inundated era: Human judgment, non-modular work, and the limits of delegation](http://arxiv.org/abs/2604.07285v1)
  来源：arXiv | 日期：2026-04-08 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Debates about artificial intelligence (AI) in education often portray teaching as a modular and procedural job that can increasingly be automated or delegated to technology. This brief communication paper argues that suc...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。
