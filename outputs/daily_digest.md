# 每日论文监控日报 (2026-03-17)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 37 篇新论文。

## 抓取状态

- arXiv：成功，命中 44 篇
- PubMed：成功，命中 25 篇
- bioRxiv：失败，命中 0 篇，错误：504 Server Error: Gateway Timeout
- medRxiv：成功，命中 3 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [Intelligent Co-Design: An Interactive LLM Framework for Interior Spatial Design via Multi-Modal Agents](http://arxiv.org/abs/2603.15341v1)
  来源：arXiv | 日期：2026-03-16 | 相关度：7.9 | 新颖度：8.5
  匹配主题：foundation_model_agent
  中文摘要：In architectural interior design, miscommunication frequently arises as clients lack design knowledge, while designers struggle to explain complex spatial relationships, leading to delayed timelines and financial losses....
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Open Biomedical Knowledge Graphs at Scale: Construction, Federation, and AI Agent Access with Samyama Graph Database](http://arxiv.org/abs/2603.15080v1)
  来源：arXiv | 日期：2026-03-16 | 相关度：7.15 | 新颖度：7.4
  匹配主题：foundation_model_agent
  中文摘要：Biomedical knowledge is fragmented across siloed databases -- Reactome for pathways, STRING for protein interactions, Gene Ontology for functional annotations, ClinicalTrials.gov for study registries, and dozens more. Re...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [KEPo: Knowledge Evolution Poison on Graph-based Retrieval-Augmented Generation](http://arxiv.org/abs/2603.11501v2)
  来源：arXiv | 日期：2026-03-12 | 相关度：6.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Graph-based Retrieval-Augmented Generation (GraphRAG) constructs the Knowledge Graph (KG) from external databases to enhance the timeliness and accuracy of Large Language Model (LLM) generations. However, this reliance o...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OrgForge: A Multi-Agent Simulation Framework for Verifiable Synthetic Corporate Corpora](http://arxiv.org/abs/2603.14997v1)
  来源：arXiv | 日期：2026-03-16 | 相关度：6.15 | 新颖度：7.14
  匹配主题：foundation_model_agent
  中文摘要：Evaluating retrieval-augmented generation (RAG) pipelines requires corpora where ground truth is knowable, temporally structured, and cross-artifact properties that real-world datasets rarely provide cleanly. Existing re...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ToolFlood: Beyond Selection -- Hiding Valid Tools from LLM Agents via Semantic Covering](http://arxiv.org/abs/2603.13950v1)
  来源：arXiv | 日期：2026-03-14 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Model (LLM) agents increasingly use external tools for complex tasks and rely on embedding-based retrieval to select a small top-k subset for reasoning. As these systems scale, the robustness of this retri...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic Exploration of Physics Models](http://arxiv.org/abs/2509.24978v5)
  来源：arXiv | 日期：2025-09-29 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：The process of scientific discovery relies on an interplay of observations, analysis, and hypothesis generation. Machine learning is increasingly being adopted to address individual aspects of this process. However, it r...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CangjieBench: Benchmarking LLMs on a Low-Resource General-Purpose Programming Language](http://arxiv.org/abs/2603.14501v1)
  来源：arXiv | 日期：2026-03-15 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models excel in high-resource programming languages but struggle with low-resource ones. Existing research related to low-resource programming languages primarily focuses on Domain-Specific Languages (DSLs...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Cropping outperforms dropout as an augmentation strategy for self-supervised training of text embeddings](http://arxiv.org/abs/2508.03453v2)
  来源：arXiv | 日期：2025-08-05 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Text embeddings, i.e. vector representations of entire texts, play an important role in many NLP applications, such as retrieval-augmented generation, clustering, or visualizing collections of texts for data exploration....
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Research Paradigm of Materials Science Tetrahedra with Artificial Intelligence](http://arxiv.org/abs/2603.13744v1)
  来源：arXiv | 日期：2026-03-14 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：The classical material tetrahedron that represents the Structure-Property-Processing-Performance-Characterization relationship is the most important research paradigm in materials science so far. It has served as a proto...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CausalEvolve: Towards Open-Ended Discovery with Causal Scratchpad](http://arxiv.org/abs/2603.14575v1)
  来源：arXiv | 日期：2026-03-15 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Evolve-based agent such as AlphaEvolve is one of the notable successes in using Large Language Models (LLMs) to build AI Scientists. These agents tackle open-ended scientific problems by iteratively improving and evolvin...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [The Impact of Ideological Discourses in RAG: A Case Study with COVID-19 Treatments](http://arxiv.org/abs/2603.14838v1)
  来源：arXiv | 日期：2026-03-16 | 相关度：4.75 | 新颖度：5.56
  匹配主题：foundation_model_agent
  中文摘要：This paper studies the impact of retrieved ideological texts on the outputs of large language models (LLMs). While interest in understanding ideology in LLMs has recently increased, little attention has been given to thi...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [SeekRBP: Leveraging Sequence-Structure Integration with Reinforcement Learning for Receptor-Binding Protein Identification](http://arxiv.org/abs/2603.04748v2)
  来源：arXiv | 日期：2026-03-05 | 相关度：7.1 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Motivation: Receptor-binding proteins (RBPs) initiate viral infection and determine host specificity, serving as key targets for phage engineering and therapy. However, the identification of RBPs is complicated by their ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [QA-Dragon: Query-Aware Dynamic RAG System for Knowledge-Intensive Visual Question Answering](http://arxiv.org/abs/2508.05197v2)
  来源：arXiv | 日期：2025-08-07 | 相关度：6.8 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) has been introduced to mitigate hallucinations in Multimodal Large Language Models (MLLMs) by incorporating external knowledge into the generation process, and it has become a widely ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Expert Mind: A Retrieval-Augmented Architecture for Expert Knowledge Preservation in the Energy Sector](http://arxiv.org/abs/2603.14541v1)
  来源：arXiv | 日期：2026-03-15 | 相关度：6.8 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：The departure of subject-matter experts from industrial organizations results in the irreversible loss of tacit knowledge that is rarely captured through conventional documentation practices. This paper proposes Expert M...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [APEX-Searcher: Augmenting LLMs' Search Capabilities through Agentic Planning and Execution](http://arxiv.org/abs/2603.13853v1)
  来源：arXiv | 日期：2026-03-14 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG), based on large language models (LLMs), serves as a vital approach to retrieving and leveraging external knowledge in various domain applications. When confronted with complex multi-h...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ES-Merging: Biological MLLM Merging via Embedding Space Signals](http://arxiv.org/abs/2603.14405v1)
  来源：arXiv | 日期：2026-03-15 | 相关度：6.1 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Biological multimodal large language models (MLLMs) have emerged as powerful foundation models for scientific discovery. However, existing models are specialized to a single modality, limiting their ability to solve inhe...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Unlocking Enzyme Discovery: A High-Resolution Gene Cluster Database Powered by Phylogenetic Insights and Machine Learning.](https://pubmed.ncbi.nlm.nih.gov/41837859/)
  来源：PubMed | 日期：2026-03-16 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：High-throughput sequencing has generated vast genomic repositories that remain under-annotated, hampering enzyme discovery. We present an integrated pipeline that (i) builds a high-resolution, cross-kingdom phylogenetic ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RESCUE: Retrieval Augmented Secure Code Generation](http://arxiv.org/abs/2510.18204v2)
  来源：arXiv | 日期：2025-10-21 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Despite recent advances, Large Language Models (LLMs) still generate vulnerable code. Retrieval-Augmented Generation (RAG) has the potential to enhance LLMs for secure code generation by incorporating external security k...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RAG-3DSG: Enhancing 3D Scene Graphs with Re-Shot Guided Retrieval-Augmented Generation](http://arxiv.org/abs/2601.10168v2)
  来源：arXiv | 日期：2026-01-15 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Open-vocabulary 3D Scene Graph (3DSG) can enhance various downstream tasks in robotics by leveraging structured semantic representations, yet current 3DSG construction methods suffer from semantic inconsistencies caused ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [QiboAgent: a practitioner's guideline to open source assistants for Quantum Computing code development](http://arxiv.org/abs/2603.15538v1)
  来源：arXiv | 日期：2026-03-16 | 相关度：4.75 | 新颖度：7.48
  匹配主题：foundation_model_agent
  中文摘要：We introduce QiboAgent, a reference implementation designed to serve as a practitioner's guideline for developing specialized coding assistants in Quantum Computing middleware. Addressing the limitations in scientific so...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Retrieval-augmented Decoding for Improving Truthfulness in Open-ended Generation](http://arxiv.org/abs/2508.02184v2)
  来源：arXiv | 日期：2025-08-04 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Ensuring truthfulness in large language models (LLMs) remains a critical challenge for reliable text generation. While supervised fine-tuning and reinforcement learning with human feedback have shown promise, they requir...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [$p^2$RAG: Privacy-Preserving RAG Service Supporting Arbitrary Top-$k$ Retrieval](http://arxiv.org/abs/2603.14778v1)
  来源：arXiv | 日期：2026-03-16 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) enables large language models to use external knowledge, but outsourcing the RAG service raises privacy concerns for both data owners and users. Privacy-preserving RAG systems address...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [MedPriv-Bench: Benchmarking the Privacy-Utility Trade-off of Large Language Models in Medical Open-End Question Answering](http://arxiv.org/abs/2603.14265v1)
  来源：arXiv | 日期：2026-03-15 | 相关度：7.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in Retrieval-Augmented Generation (RAG) have enabled large language models (LLMs) to ground outputs in clinical evidence. However, connecting LLMs with external databases introduces the risk of contextual...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [ClimateAgents: A Multi-Agent Research Assistant for Social-Climate Dynamics Analysis](http://arxiv.org/abs/2603.13840v1)
  来源：arXiv | 日期：2026-03-14 | 相关度：3.45 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：The complex interaction between social behaviors and climate change requires more than traditional data-driven prediction; it demands interpretable and adaptive analytical frameworks capable of integrating heterogeneous ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Retrieve, Schedule, Reflect: LLM Agents for Chip QoR Optimization](http://arxiv.org/abs/2603.13767v1)
  来源：arXiv | 日期：2026-03-14 | 相关度：2.75 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：现代芯片设计要求在严格的上市时间约束下，对时序、功耗和面积进行多目标优化（QoR）。尽管EDA工具集成了强大的优化算法，但实现高QoR仍高度依赖专家进行有效的长程调度。为实现芯片设计自动化，本文提出了一种基于大语言模型（LLM）的智能体框架，通过与EDA工具直接交互来调度优化任务。该智能体利用检索增强生成（RAG）将自然语言形式的专业知识转化为搜索树，并结合帕累托驱动的QoR反馈进行语言反思，以进一步提升调度质量。实验结果表明，与强化学...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Benchmarking LLM-based agents for single-cell omics analysis](http://arxiv.org/abs/2508.13201v3)
  来源：arXiv | 日期：2025-08-16 | 相关度：2.5 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：单细胞组学数据的激增暴露了传统手动分析工作流的局限性。AI 智能体（Agents）通过自适应规划、可执行代码生成、可追溯决策和实时知识融合，为该领域带来了范式转变，但缺乏全面的基准测试阻碍了其发展。本研究引入了一种新型基准评估系统，旨在严格评估智能体在单细胞组学分析中的能力。该系统包含：一个兼容多种智能体框架和 LLM 的统一平台；涵盖认知程序合成、协作、执行效率、生物信息学知识整合和任务完成质量的多维指标；以及 50 个涵盖多组学、物...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Benchmarking Open-Source PPG Foundation Models for Biological Age Prediction](http://arxiv.org/abs/2603.14030v1)
  来源：arXiv | 日期：2026-03-14 | 相关度：2.4 | 新颖度：7.0
  匹配主题：未命中具体主题
  中文摘要：本研究评估了开源光电容积脉搏波（PPG）基础模型在生物年龄预测中的表现。研究发现，在 212,231 名英国生物样本库（UK Biobank）受试者上训练的特定任务模型（AI-PPG Age）在处理不同临床人群数据时失效：无论真实年龄如何，其预测值均坍缩在 38-67 岁的狭窄范围内。相比之下，无年龄训练目标的通用基础模型在相同数据上实现了更低的误差。研究在 PulseDB 的 906 名手术患者上评估了 Pulse-PPG、PaPaG...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Central Dogma Transformer II: An AI Microscope for Understanding Cellular Regulatory Mechanisms](http://arxiv.org/abs/2602.08751v3)
  来源：arXiv | 日期：2026-02-09 | 相关度：2.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：当前的生物 AI 模型普遍缺乏可解释性，其内部表示往往无法对应到可供研究者检验的生物学关系。为了解决这一问题，研究者开发了 CDT-II 模型，其架构直接模拟中心法则：包含 DNA 自注意力、RNA 自注意力以及用于模拟转录控制的交叉注意力机制，且仅需基因组嵌入和原始单细胞表达数据作为输入。在 K562 细胞系的 CRISPRi 扰动数据测试中（完全排除 5 个基因进行验证），CDT-II 预测扰动效应的平均相关系数 r 达到 0.84...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HindSight: Evaluating Research Idea Generation via Future Impact](http://arxiv.org/abs/2603.15164v1)
  来源：arXiv | 日期：2026-03-16 | 相关度：1.4 | 新颖度：6.88
  匹配主题：未命中具体主题
  中文摘要：评估 AI 生成的研究思路通常依赖 LLM 评委或专家小组，这具有主观性且脱离实际研究影响力。本研究提出 HindSight，一种基于时间切分的评估框架，通过将生成的思路与真实的未来出版物进行匹配，并根据引用影响力和发表期刊/会议进行评分来衡量思路质量。该框架设定时间截止点 T，限制生成系统仅使用 T 之前的文献，随后将其输出与未来 30 个月内发表的论文进行对比。在 10 个 AI/ML 研究主题上的实验显示：LLM 作为评委无法区分...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The Active Discoverer Framework: Towards Autonomous Physics Reasoning through Neuro-Symbolic LaTeX Synthesis](http://arxiv.org/abs/2601.06117v3)
  来源：arXiv | 日期：2026-01-03 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：现代人工智能在统计插值方面表现出色，但在理论物理和数学所需的精确推理上存在根本缺陷。本研究识别出“浮点墙（Float Wall）”现象，即由于标准浮点表示和BPE分词导致神经外推在超过 $10^{16}$ 量级时发生灾难性崩溃。为此，我们提出了 Active Discoverer 框架，这是一种专为不变性发现设计的数字原生神经符号架构。其核心是 NumberNet，一种采用最低有效位（LSB）序列编码的孪生算术 Transformer，...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Cross-RAG: Zero-Shot Retrieval-Augmented Time Series Forecasting via Cross-Attention](http://arxiv.org/abs/2603.14709v1)
  来源：arXiv | 日期：2026-03-16 | 相关度：0.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：时间序列基础模型（TSFMs）通过在多样化领域的大规模预训练展现了强大的表达能力，但在处理未见数据集的零样本预测时，其泛化能力仍受限。检索增强预测通过引入外部知识库来缓解这一问题，但现有方法通常依赖固定数量的检索样本，容易引入无关干扰信息。为此，本研究提出了 Cross-RAG，这是一种零样本检索增强预测框架，能够选择性地关注与查询相关的检索样本。Cross-RAG 通过查询-检索交叉注意力机制（query-retrieval cros...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Rethinking Evaluation in Retrieval-Augmented Personalized Dialogue: A Cognitive and Linguistic Perspective](http://arxiv.org/abs/2603.14217v1)
  来源：arXiv | 日期：2026-03-15 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：在认知科学和语言学理论中，对话被视为一种基于连贯性、一致性和共同理解的协作活动，而非独立话语的简单堆砌。然而，当前的开放域和个性化对话系统仍主要采用 BLEU、ROUGE 和 F1 等表面词汇相似性指标作为核心评估标准，这些指标无法捕捉对话质量的深层维度。本研究以检索增强的个性化对话框架 LAPDOG 为案例，重新审视了其评估方法。通过引入人类评判员和大型语言模型（LLM）评判员，研究识别了现有评估实践中的多项局限，包括对话历史损坏、检...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Grounding World Simulation Models in a Real-World Metropolis](http://arxiv.org/abs/2603.15583v1)
  来源：arXiv | 日期：2026-03-16 | 相关度：0.7 | 新颖度：8.1
  匹配主题：未命中具体主题
  中文摘要：本研究探讨了世界模拟模型如何渲染真实存在的城市而非虚构环境。以往的生成式世界模型虽能合成视觉合理的图像，但内容多为虚构。我们提出了首尔世界模型（SWM），这是一个锚定于真实首尔市的城市级世界模型。SWM 通过对附近街景图像进行检索增强调节，实现了自回归视频生成。针对检索参考与动态场景的时间不一致、轨迹多样性有限及车辆采集数据稀疏等挑战，我们采用了跨时间配对、支持多样相机轨迹的大规模合成数据集，以及从稀疏街景合成连贯视频的视图插值管线。此...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [From Study Design to Executable Code: Automating Target Trial Emulation with Large Language Models](https://www.medrxiv.org/content/10.64898/2026.03.13.26348306v1)
  来源：medRxiv | 日期：2026-03-14 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：实施目标试验模拟（TTE）研究并生成端到端可执行分析代码具有极高的技术门槛。本研究开发了 THESEUS 框架，旨在将自由文本形式的研究描述转化为 OHDSI 生态系统中标准化的分析规范和可执行的 Strategus R 脚本。THESEUS 包含两个核心步骤：首先，利用大语言模型（LLM）将研究描述映射到受限的 JSON 模式中实现标准化；其次，将结构化规范转换为 R 脚本，并引入自审计循环进行错误修正。研究评估了 8 种商业 LLM...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [PRISM: Enhancing Protein Inverse Folding through Fine-Grained Retrieval on Structure-Sequence Multimodal Representations](http://arxiv.org/abs/2510.11750v2)
  来源：arXiv | 日期：2025-10-12 | 相关度：3.05 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：蛋白质逆折叠（根据目标3D结构设计序列）是蛋白质工程的核心，但受限于巨大的序列空间和局部结构约束。现有深度学习方法虽有较高恢复率，但缺乏显式机制来复用天然蛋白质中保守的细粒度结构-序列模式。为此，研究者提出了PRISM，一种用于逆折叠的多模态检索增强生成（RAG）框架。PRISM从已知蛋白质中检索潜在基序（motif）的细粒度表示，并利用混合自交叉注意力解码器进行整合。该模型被表述为潜变量概率模型，并通过高效近似实现，兼顾了理论基础与实...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GlobalRAG: Enhancing Global Reasoning in Multi-hop Question Answering via Reinforcement Learning](http://arxiv.org/abs/2510.20548v4)
  来源：arXiv | 日期：2025-10-23 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：强化学习在提升检索增强生成（RAG）方面展现出潜力，但在多跳问答（QA）任务中仍面临全局规划缺失和执行不忠实（如查询构建不当、证据使用不一致）两大挑战。为此，本研究提出 GlobalRAG 强化学习框架，旨在增强多跳问答中的全局推理能力。该框架将复杂问题分解为多个子目标，协调检索与推理过程，并对证据进行迭代优化。为了引导模型学习，研究引入了“规划质量奖励”和“子目标完成奖励”，以促进连贯规划和可靠的子目标执行。此外，采用渐进式权重退火策...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Integrative Approaches in Lung Cancer Diagnosis: Bridging Molecular Biomarkers and AI Driven Imaging.](https://pubmed.ncbi.nlm.nih.gov/41830914/)
  来源：PubMed | 日期：2026-03-14 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：传统的肺癌诊断方法（如X射线、CT、支气管镜和组织活检）在早期检测方面存在局限。近期，分子生物学与计算技术的进步推动了诊断范式的转变。本综述分析了将EGFR、ALK、KRAS、BRAF、MET及PD-L1表达等分子生物标志物整合入常规诊断，以实现精准分型和治疗选择。液体活检和循环肿瘤DNA（ctDNA）等先进技术为肿瘤特征分析和实时监测提供了非侵入性手段。二代测序（NGS）及基因组学、转录组学、蛋白质组学等多组学方法提供了肿瘤微环境的详...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
