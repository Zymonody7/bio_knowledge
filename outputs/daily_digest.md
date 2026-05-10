# 每日论文监控日报 (2026-05-10)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 36 篇新论文。

## 抓取状态

- arXiv：成功，命中 25 篇
- PubMed：成功，命中 40 篇
- bioRxiv：成功，命中 15 篇
- medRxiv：成功，命中 8 篇

## 最值得看

### 方法创新

- [Protein language model-guided generative design of affinity peptides for chromatographic purification of lentiviral vectors.](https://pubmed.ncbi.nlm.nih.gov/41833101/)
  来源：PubMed | 日期：2026-05-10 | 相关度：7.15 | 新颖度：8.94
  匹配主题：foundation_model_agent
  中文摘要：Lentiviral vectors (LVs) have emerged as the most promising tool for cell and gene therapy. However, LVs are very fragile and sensitive to shear stress, buffer pH and salt concentration, resulting in serious hurdles in d...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [Multi-Modal LLM based Image Captioning in ICT: Bridging the Gap Between General and Industry Domain](http://arxiv.org/abs/2601.09298v2)
  来源：arXiv | 日期：2026-01-14 | 相关度：7.9 | 新颖度：1.2
  匹配主题：foundation_model_agent
  中文摘要：In the information and communications technology (ICT) industry, training a domain-specific large language model (LLM) or constructing a retrieval-augmented generation system requires a substantial amount of high-value d...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [JARVIS: An Evidence-Grounded Retrieval System for Interpretable Deceptive Reviews Adjudication](http://arxiv.org/abs/2602.12941v2)
  来源：arXiv | 日期：2026-02-13 | 相关度：7.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Deceptive reviews, refer to fabricated feedback designed to artificially manipulate the perceived quality of products. Within modern e-commerce ecosystems, these reviews remain a critical governance challenge. Despite ad...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LatentRAG: Latent Reasoning and Retrieval for Efficient Agentic RAG](http://arxiv.org/abs/2605.06285v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：6.55 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Single-step retrieval-augmented generation (RAG) provides an efficient way to incorporate external information for simple question answering tasks but struggles with complex questions. Agentic RAG extends this paradigm b...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BioTool: A Comprehensive Tool-Calling Dataset for Enhancing Biomedical Capabilities of Large Language Models](http://arxiv.org/abs/2605.05758v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Despite the success of large language models (LLMs) on general-purpose tasks, their performance in highly specialized domains such as biomedicine remains unsatisfactory. A key limitation is the inability of LLMs to effec...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [STAT: A multi-agent framework for integrated and interactive spatial transcriptomics analysis](https://www.biorxiv.org/content/10.64898/2026.05.01.722244v2)
  来源：bioRxiv | 日期：2026-05-07 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：空间转录组学（ST）分析通常涉及跨平台的多种计算方法，导致研究人员在数据整合上耗费过多时间。目前的 AI 方案要么将空间数据过度简化为通用的单细胞表格，要么在缺乏中间审查的情况下自主运行，阻碍了空间生物学中至关重要的视觉和迭代分析。为此，我们开发了 STAT，一个多智能体（multi-agent）框架，旨在通过对话式交互提高空间分析的易用性，同时保持透明度和控制力。STAT 集成了持久会话、共享交互式组织查看器和分阶段技能感知流水线。在...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [UPhAIR: A Hybrid Pipeline for Generating Understandable Post-hoc AI Reports in Glioma IDH Mutation Status Prediction](https://www.medrxiv.org/content/10.64898/2026.05.01.26349658v1)
  来源：medRxiv | 日期：2026-05-08 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Clinical adoption of machine learning (ML) in medical imaging is limited by the lack of interpretability. To address this, we present understandable post-hoc artificial intelligence reports (UPhAIR), a pipeline designed ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Towards autonomous biology: Compiler-Verified Protocols as a Foundation for Real World AI Execution](https://www.biorxiv.org/content/10.64898/2026.05.05.720956v1)
  来源：bioRxiv | 日期：2026-05-07 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence has advanced from analyzing experimental data to autonomously generating hypotheses, designing experiments, and coordinating closed loop discovery. Yet the translation from computational reasoning...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Transforming the cytokine literature into a resource for experimental analysis and discovery](https://www.biorxiv.org/content/10.64898/2026.05.04.722753v1)
  来源：bioRxiv | 日期：2026-05-07 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Cytokine biology is dispersed across hundreds of thousands of publications, making it difficult to use systematically when interpreting new experiments. Large language models (LLMs) can assist with focused literature int...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [SLiMNet: a deep learning model to detect short linear motifs using protein large language model representations and paired inputs](https://www.biorxiv.org/content/10.64898/2026.05.04.722713v1)
  来源：bioRxiv | 日期：2026-05-07 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Short linear motifs (SLiMs) are short (3-15 amino acids in length) segments within intrinsically disordered regions (IDRs) that mediate transient protein-protein interactions as well as other functions such as stability ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Knowledge Graphs, the Missing Link in Agentic AI-based Formal Verification](http://arxiv.org/abs/2605.06434v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in Large Language Models (LLMs) have enabled workflows that generate SystemVerilog Assertions (SVAs) from natural-language specifications, with the potential to accelerate Formal Verification (FV). Howeve...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Prompt-engineering improves clinical safety of large language models for opioid equipotency conversion](https://www.medrxiv.org/content/10.64898/2026.05.06.26352590v1)
  来源：medRxiv | 日期：2026-05-08 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Background: Large language models (LLMs) are increasingly used in medical education and clinical decision-making, but their reliability in high-risk medication dosing remains unclear. Opioid rotation is a common task req...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MAT-Cell: A Multi-Agent Tree-Structured Reasoning Framework for Batch-Level Single-Cell Annotation](http://arxiv.org/abs/2604.06269v2)
  来源：arXiv | 日期：2026-04-07 | 相关度：5.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Automated single-cell annotation is difficult when the most abundant genes are not the most discriminative ones, or when a target state is poorly covered by a fixed reference atlas. GPTCelltype-style one-shot prompting a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Cited but Not Verified: Parsing and Evaluating Source Attribution in LLM Deep Research Agents](http://arxiv.org/abs/2605.06635v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) power deep research agents that synthesize information from hundreds of web sources into cited reports, yet these citations cannot be reliably verified. Current approaches either trust models...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LLM-Driven Design Space Exploration of FPGA-based Accelerators](http://arxiv.org/abs/2605.05920v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Designing field-programmable gate array (FPGA)-based accelerators for modern artificial intelligence workloads requires navigating a large and complex hardware design space encompassing architectural parameters, dataflow...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AI CFD Scientist: Toward Open-Ended Computational Fluid Dynamics Discovery with Physics-Aware AI Agents](http://arxiv.org/abs/2605.06607v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Recent LLM-based agents have closed substantial portions of the scientific discovery loop in software-only machine-learning research, in chemistry, and in biology. Extending the same loop to high-fidelity physical simula...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CAPTAIN: a multimodal foundation model pretrained on co-assayed single-cell RNA and protein.](https://pubmed.ncbi.nlm.nih.gov/42098152/)
  来源：PubMed | 日期：2026-05-07 | 相关度：4.45 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：蛋白质作为细胞功能的终端执行者，编码了基因组和转录组程序的表型结果。尽管转录组谱是易于获取的代理指标，但它们无法完全替代定义细胞表型的蛋白质组景观。目前的单细胞基础模型大多仅在转录组上进行训练，导致对细胞状态的刻画存在偏差。为解决此限制，本研究推出了 CAPTAIN，这是一种多模态基础模型，在超过 400 万个具有并发测量转录组和 382 种精选表面蛋白的单细胞（涵盖多种人类和小鼠组织）上进行了预训练。结果显示，CAPTAIN 通过建模...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BioResearcher: Scenario-Guided Multi-Agent for Translational Medicine](http://arxiv.org/abs/2605.05985v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：转化医学要求将模糊的开发目标转化为包含文献、临床试验、专利及定量多组学分析的证据合成，且必须保留标识符、不确定性和可追溯性。通用基础模型及现有的多智能体系统往往难以处理异构生物医学来源所需的、可审计的特定场景工作流。本文提出 Ingenix BioResearcher，这是一种场景引导的多智能体系统。该系统将查询映射至版本化的研究手册，通过 30 多个工具和机器学习端点委派给专业子智能体，并将结构化数据库访问与用于基因组规模分析的沙箱代...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BioMedArena: An Open-source Toolkit for Building and Evaluating Biomedical Deep Research Agents](http://arxiv.org/abs/2605.06177v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：1.4 | 新颖度：1.5
  匹配主题：未命中具体主题
  中文摘要：当前构建生物医学深度研究智能体（Agent）面临严重的“胶水代码”冗余和评估标准不一的挑战，导致同一模型在不同框架下的表现难以公平比较。为此，本研究推出了开源工具包 BioMedArena，旨在消除“单篇论文工程税”并提供公平的竞技场。该工具包将生物医学智能体评估解耦为基准加载、工具暴露、工具选择、执行模式、上下文管理和评分六个核心层。BioMedArena 集成了跨 9 个功能家族的 147 个生物医学基准和 75 个专业工具，支持通...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [An Agent-Oriented Pluggable Experience-RAG Skill for Experience-Driven Retrieval Strategy Orchestration](http://arxiv.org/abs/2605.03989v2)
  来源：arXiv | 日期：2026-05-05 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）系统通常假设单一固定的检索流程足以应对各类异构任务，但事实性问答、多跳推理和科学验证对检索策略具有不同的偏好。本文提出 Experience-RAG Skill，这是一种面向智能体（Agent）的可插拔检索编排层，位于智能体与检索器池之间。该技能通过分析当前场景、咨询经验记忆并选择合适的检索策略，最终向智能体返回结构化的证据。在固定候选池的实验中，Experience-RAG Skill 在 BeIR/nq、BeI...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Intentmaking and Sensemaking: Human Interaction with AI-Guided Mathematical Discovery](http://arxiv.org/abs/2605.05921v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：人工智能为科学发现提供了强大的新工具，但有效利用这些系统所需的交互范式仍有待探索。本文介绍了一项针对 11 位数学专家的形成性用户研究结果，这些专家使用名为 AlphaEvolve 的进化编码智能体（Agent）来解决其专业领域内的前沿问题。研究识别并描述了一种被称为“意图构建”（intentmaking）的独特工作流，即通过与系统的主动交互来不断发现、定义和完善实验目标的迭代过程。我们将此视为“意义构建”（sensemaking）的自...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [ChatIBD: design, safeguards, and early international use of a guideline-grounded generative AI tool for inflammatory bowel disease (IBD) professionals](https://www.medrxiv.org/content/10.64898/2026.05.06.26352526v1)
  来源：medRxiv | 日期：2026-05-07 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：本研究描述了ChatIBD的设计、运行保障及早期使用情况。ChatIBD是一个专为炎症性肠病（IBD）专业人士设计的生成式AI平台。该平台采用检索增强生成（RAG）技术，基于精选的IBD指南语料库进行问答。技术实现上，系统结合了混合语义与关键词检索、查询扩展及重排序，并强制模型仅依据检索到的材料回答并返回引用链接。安全保障措施包括集成欧洲药品管理局（EMA）的固定药物剂量信息、用户反馈捕获以及临床医生对标记输出的审查。在2025年10月...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [LCC-LLM: Leveraging Code-Centric Large Language Models for Malware Attribution](http://arxiv.org/abs/2605.05807v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：4.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：LLMs are increasingly explored for malware analysis; however, current LLM-based malware attribution remains limited by unsupported indicators and insufficient code-level grounding for identifying malicious and vulnerable...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [LeakDojo: Decoding the Leakage Threats of RAG Systems](http://arxiv.org/abs/2605.05818v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：4.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) enables large language models (LLMs) to leverage external knowledge, but also exposes valuable RAG databases to leakage attacks. As RAG systems grow more complex and LLMs exhibit stro...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Transforming Semi-structured Variant Assessments into Computable Clinical Assertions: A Pilot Study for AI-Assisted Curation](https://www.medrxiv.org/content/10.64898/2026.05.07.26352456v1)
  来源：medRxiv | 日期：2026-05-08 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：基因组医学依赖专家对基因变异的评估，但由于缺乏易于获取的基因组知识，这一过程受到严重阻碍。尽管 ClinVar 和 CIViC 等资源支持结构化数据共享，但上游产生的大量变异解释数据与这些资源不兼容，导致了知识孤岛。本研究评估了一种将半结构化变异分类知识转化为可计算临床断言的策略，该策略遵循全球基因组学与健康联盟（GA4GH）的基因组知识标准规范。研究人员通过程序化方式将电子表格中的体细胞癌症临床意义分类映射到 GA4GH 变异注释规范...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [How to make the most of your masked language model for protein engineering](http://arxiv.org/abs/2603.10302v2)
  来源：arXiv | 日期：2026-03-11 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：A plethora of protein language models have been released in recent years. Yet comparatively little work has addressed how to best sample from them to optimize desired biological properties. We fill this gap by proposing ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Steering Sequence Generation in Protein Language Models through Iterative Lookback Monte Carlo Sampling](https://www.biorxiv.org/content/10.64898/2026.05.01.722156v1)
  来源：bioRxiv | 日期：2026-05-07 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Protein language models (pLMs) leverage large-scale evolutionary data to generate novel sequences, but steering generation toward desired physicochemical properties without sacrificing diversity remains a major challenge...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Event-Causal RAG: A Retrieval-Augmented Generation Framework for Long Video Reasoning in Complex Scenarios](http://arxiv.org/abs/2605.06185v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：5.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Recent large vision-language models have achieved strong performance on short- and medium-length video understanding, yet they remain inadequate for ultra-long or even infinite video reasoning, where models must preserve...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Latent Abstraction for Retrieval-Augmented Generation](http://arxiv.org/abs/2604.17866v2)
  来源：arXiv | 日期：2026-04-20 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) has become a standard approach for enhancing large language models (LLMs) with external knowledge, mitigating hallucinations, and improving factuality. However, existing systems rely ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CMS4-focused multi-omic integration enhances antigen target identification in colorectal cancer](https://www.biorxiv.org/content/10.64898/2026.05.04.722755v1)
  来源：bioRxiv | 日期：2026-05-07 | 相关度：1.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：结直肠癌（CRC）中CMS4亚型预后较差且治疗选择有限。本研究构建了一个协调的多组学CRC知识库，旨在识别具有转化潜力的CMS4特异性抗原靶点。通过专有的AI驱动数据搜索与整理技术，整合了79个转录组数据集（包含5,033个肿瘤和161个正常样本），并结合3个大体RNA-seq参考集、2个单细胞图谱和8个蛋白质注释数据库，形成了规模空前的多组学知识库。研究利用共识分子亚型（CMS）推断捕获CMS4特异性表达模式，并应用加权有效性与安全性...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Autoencoder/RandomForest-TabPFN for Cross-Cancer Metabolomics: Prostate and Breast Cancer Diagnosis Using Paper Spray and Ion Mobility-Mass Spectrometry Techniques.](https://pubmed.ncbi.nlm.nih.gov/42096511/)
  来源：PubMed | 日期：2026-05-07 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：准确快速地诊断前列腺癌（PC）和乳腺癌（BC）对改善患者预后至关重要。本研究提出了一种整合自动编码器（Autoencoder）、基于随机森林（Random Forest）的特征选择和表格先验数据拟合网络（TabPFN）的新型预测方法，用于分析癌症代谢组学数据。研究利用纸喷雾电离质谱（PSI-MS）和流动注射-行波离子迁移质谱（FI-TWIM-MS）获取了PC患者的尿液与血清样本数据，以及BC患者穿刺活检的代谢和脂质组特征。实验结果显示，...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Retrieval from Within: An Intrinsic Capability of Attention-Based Models](http://arxiv.org/abs/2605.05806v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）通常将检索和生成视为两个独立的系统。本研究探讨了基于注意力的编码器-解码器模型是否可以直接从其内部表示中进行检索。我们提出了 INTRA（通过注意力的内在检索）框架，在该框架中，解码器的注意力查询直接对预编码的证据块进行评分，并将其作为生成的上下文进行复用。通过这种设计，INTRA 实现了检索与生成的统一，消除了传统 RAG 流水线中检索器与生成器之间的不匹配问题。此外，该设计通过在不同查询之间复用预计算的编码器状...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Reinforced Informativeness Optimization for Long-Form Retrieval-Augmented Generation](http://arxiv.org/abs/2505.20825v2)
  来源：arXiv | 日期：2025-05-27 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：长篇问答（LFQA）要求从多源证据中合成连贯且有事实依据的回复，这使得强化学习（RL）的奖励设计至关重要。然而，标准奖励机制通常假设存在唯一目标或精确匹配，适用于短篇问答但难以应用于 LFQA，导致现有 RAG 系统缺乏可验证的奖励机制，优化过程不稳定。本文提出 RioRAG 框架，旨在实现可验证的信息量优化。首先，RioRAG 将“信息量”定义为可衡量且可外部验证的 RL 目标。其次，该框架采用以“金块（nugget）”为中心的验证方...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [DentaCoPilot: An LLM-Augmented Next-Procedure Recommender for General Dentistry, Designed for Dentist Augmentation](https://www.medrxiv.org/content/10.64898/2026.05.07.26352635v1)
  来源：medRxiv | 日期：2026-05-08 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Background. Commercial dental artificial intelligence in 2026 is overwhelmingly diagnostic: caries, calculus, periapical, and bone-level detection on radiographs. The clinically harder question that follows every diagnos...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [A Versatile AI Agent for Rare Disease Diagnosis and Risk Gene Prioritization](http://arxiv.org/abs/2605.06226v1)
  来源：arXiv | 日期：2026-05-07 | 相关度：2.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：准确及时的诊断对罕见病治疗至关重要，但现有诊断流程常面临评估周期长和准确率低的问题。为此，我们推出了 Hygieia，这是一种多模态 AI 智能体（Agent）系统，旨在通过整合表型特征、遗传谱图和临床记录等多元数据来支持精准诊断。Hygieia 采用基于路由（router-based）和知识增强的框架，有效缓解了模型幻觉，并能针对不同疾病类别定制诊断策略。该系统特别突出了对罕见病相关基因组风险因素的优先级排序功能，并提供置信度评分以辅...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial intelligence in cancer diagnostics: a primer for clinicians and scientists.](https://pubmed.ncbi.nlm.nih.gov/42097285/)
  来源：PubMed | 日期：2026-05-07 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：人工智能（AI）正通过实现更精确的诊断、预测治疗反应、改善预后及提供个性化治疗方案，迅速改变癌症护理模式。随着 AI 工具日益嵌入诊断流程和临床决策，理解其潜力和局限性对于确保安全有效的应用至关重要。本文为肿瘤学家、病理学家、临床研究人员和医疗技术人员提供了一份关于 AI 整合进癌症诊断和治疗反应的入门指南。该指南重点关注 AI 在数字病理学、液体活检和临床决策支持中的应用，同时涵盖放射学、基因组学和基于电子健康记录（EHR）分析的相关...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
