# 每日论文监控日报 (2026-05-07)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 55 篇新论文。

## 抓取状态

- arXiv：成功，命中 44 篇
- PubMed：成功，命中 39 篇
- bioRxiv：成功，命中 13 篇
- medRxiv：成功，命中 9 篇

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [From Knowledge to Action: Outcomes of the 2025 Large Language Model (LLM) Hackathon for Applications in Materials Science and Chemistry](http://arxiv.org/abs/2605.03205v1)
  来源：arXiv | 日期：2026-05-04 | 相关度：7.9 | 新颖度：1.2
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are rapidly changing how researchers in materials science and chemistry discover, organize, and act on scientific knowledge. This paper analyzes a broad set of community-developed LLM applica...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Historical Perspectives in Medicine using a Large Language Model: Emulating an 18th Century Physician](https://www.medrxiv.org/content/10.64898/2026.02.10.26345990v2)
  来源：medRxiv | 日期：2026-05-04 | 相关度：7.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：18世纪医学文献记录了临床推理演变的关键时期，但其在现代医学教育中的整合程度有限。本研究开发了一个受历史约束的大语言模型（LLM）教育平台，旨在模拟18世纪医生的诊断推理、语言风格和概念框架。研究采用现代GPT架构，通过严格的指令约束，将其知识范围限制在精心挑选的6本17至18世纪基础医学著作中，并设置护栏以防止出现时代错误术语和现代医学概念。评估通过将模型的诊断和治疗方案与原始历史文献进行定性对比，并将其应用于现代临床案例以展示古今差...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Extracting adverse event nature, severity, timelines and resulting interventions from clinical notes of patients receiving CAR-T therapy using large language models.](https://www.medrxiv.org/content/10.64898/2026.04.28.26351782v1)
  来源：medRxiv | 日期：2026-05-05 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Chimeric Antigen Receptor T-cell (CAR-T) therapy, where genetically engineered patient T cells target tumor antigens, has transformed care for hematologic malignancies but requires careful tracking of adverse events (AEs...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multilingual Evaluation of a Large Language Model-Based Primary Care Chatbot](https://www.medrxiv.org/content/10.64898/2026.05.03.26352241v1)
  来源：medRxiv | 日期：2026-05-05 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Pre-visit planning has the potential to reduce EHR documentation burden while improving workflow efficiency, care quality, and patient-provider engagement. Large language model (LLM) chatbots show promise for supporting ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Mirage to Grounding: Towards Reliable Multimodal Circuit-to-Verilog Code Generation](http://arxiv.org/abs/2604.27969v2)
  来源：arXiv | 日期：2026-04-30 | 相关度：6.8 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Multimodal large language models (MLLMs) are increasingly used to translate visual artifacts into code, from UI mockups into HTML to scientific plots into Python scripts. A circuit diagram can be viewed as a visual domai...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [GRAIL: A Deep-Granularity Hybrid Resonance Framework for Real-Time Agent Discovery via SLM-Enhanced Indexing](http://arxiv.org/abs/2605.02489v2)
  来源：arXiv | 日期：2026-05-04 | 相关度：6.55 | 新颖度：6.7
  匹配主题：foundation_model_agent
  中文摘要：As the ecosystem of Large Language Model (LLM)-based agents expands rapidly, efficient and accurate Agent Discovery becomes a critical bottleneck for large-scale multi-agent collaboration. Existing approaches typically f...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Benchmarking Retrieval Strategies for Biomedical Retrieval-Augmented Generation: A Controlled Empirical Study](http://arxiv.org/abs/2605.02520v1)
  来源：arXiv | 日期：2026-05-04 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) offers a well-established path to grounding large language model (LLM) outputs in external knowledge, yet the question of which retrieval strategy works best in a high-stakes domain s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [GENERator-v2: Reconciling Coarse Tokenization with Single-Nucleotide Resolution in Genomic Language Modeling](https://www.biorxiv.org/content/10.64898/2026.01.27.702015v2)
  来源：bioRxiv | 日期：2026-05-04 | 相关度：6.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：基因组基础模型旨在从DNA序列中学习通用表示，但在处理长程上下文、单核苷酸分辨率与计算效率的矛盾时面临挑战。本文提出了GENERator-v2，从训练目标和数据构建角度重新设计了长上下文基因组模型。研究引入了“分解核苷酸监督”（FNS）技术，通过概率边缘化将高效的k-mer分词与单核苷酸似然对齐；同时采用“基因组压缩预训练”（GCP），通过聚焦于基因中心和调控区域来重塑训练分布。这些技术使标准Transformer模型在不牺牲单核苷酸精...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Effect of Large Language Models on P300 Speller Performance with Cross-Subject Training](https://www.biorxiv.org/content/10.1101/2025.10.28.685216v2)
  来源：bioRxiv | 日期：2026-05-05 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Amyotrophic lateral sclerosis (ALS), a progressive neuromuscular degenerative disease, rapidly impairs communication within years of onset. This loss of communication necessitates assistive technologies to restore intera...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [LABBench2: An Improved Benchmark for AI Systems Performing Biology Research](http://arxiv.org/abs/2604.09554v2)
  来源：arXiv | 日期：2026-02-04 | 相关度：4.75 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Optimism for accelerating scientific discovery with AI continues to grow. Current applications of AI in scientific research range from training dedicated foundation models on scientific data to agentic autonomous hypothe...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [SARS-CoV-2 Nsp1 suppresses the canonical NF-κB pathway by promoting ubiquitin-dependent degradation of TAK1 kinase.](https://pubmed.ncbi.nlm.nih.gov/42081588/)
  来源：PubMed | 日期：2026-05-04 | 相关度：7.65 | 新颖度：0.25
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：SARS-CoV-2表达的免疫调节蛋白通过干扰宿主抗病毒防御，在COVID-19的发病机制中发挥关键作用。本研究通过整合预训练蛋白质语言模型（pLM）和免疫相关通路中的基因权重，建立了一种新型预测算法，用于量化SARS-CoV-2蛋白对宿主免疫系统的扰动。研究结果显示，经典NF-κB通路在病毒感染过程中受到动态调节，其中非结构蛋白1（Nsp1）能显著抑制由其他病毒蛋白或促炎细胞因子（如IL-1β）诱导的NF-κB通路激活。分子机制研究表...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Patient2Sentence: Large Language Model-based Semantic Compression for Oncology Trial Eligibility Screening](https://www.medrxiv.org/content/10.1101/2025.11.14.25340276v2)
  来源：medRxiv | 日期：2026-05-05 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Efficient clinical trial recruitment in oncology is constrained by the need to interpret long, heterogeneous electronic health records (EHRs) that remain largely unstructured and difficult to automate. We present Patient...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Enhancing Visual Question Answering with Multimodal LLMs via Chain-of-Question Guided Retrieval-Augmented Generation](http://arxiv.org/abs/2605.03790v1)
  来源：arXiv | 日期：2026-05-05 | 相关度：6.8 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：With advances in multimodal research and deep learning, Multimodal Large Language Models (MLLMs) have emerged as a powerful paradigm for a wide range of multimodal tasks. As a core problem in vision-language research, Vi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Species-specific transformer models of bacterial gene order and content for genomic surveillance tasks](https://www.biorxiv.org/content/10.64898/2026.04.28.721069v2)
  来源：bioRxiv | 日期：2026-05-04 | 相关度：6.55 | 新颖度：1.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Transformer模型在生物数据表征方面表现出色，但通用大模型在特定领域任务中常被分类受限的模型超越。本研究针对细菌病原体流行病学分析，开发了物种特异性Transformer模型PanBART。该模型基于大肠杆菌（Escherichia coli）和肺炎链球菌（Streptococcus pneumoniae）的基因含量和基因顺序进行训练，并与最先进的非Transformer基因组流行病学方法进行了基准测试。结果显示，PanBART...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Graph-Augmented LLMs for Swiss MP Ideology Prediction](http://arxiv.org/abs/2605.04643v1)
  来源：arXiv | 日期：2026-05-06 | 相关度：5.45 | 新颖度：6.66
  匹配主题：foundation_model_agent
  中文摘要：Approximating the ideological position of Members of Parliament (MPs) is a fundamental task in political science, helping researchers understand legislative behavior, party alignment, and policy preferences. While Large ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [DiCLIP: Diffusion Model Enhances CLIP's Dense Knowledge for Weakly Supervised Semantic Segmentation](http://arxiv.org/abs/2605.04593v1)
  来源：arXiv | 日期：2026-05-06 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Weakly Supervised Semantic Segmentation (WSSS) with image-level labels typically leverages Class Activation Maps (CAMs) to achieve pixel-level predictions. Recently, Contrastive Language-Image Pre-training (CLIP) has bee...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Understanding LoRA as Knowledge Memory: An Empirical Analysis](http://arxiv.org/abs/2603.01097v2)
  来源：arXiv | 日期：2026-03-01 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Continuous knowledge updating for pre-trained large language models (LLMs) is increasingly necessary yet remains challenging. Although inference-time methods like In-Context Learning (ICL) and Retrieval-Augmented Generat...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Evaluating the Potential Impact of AI on Urinary Tract Infection Diagnosis in the Emergency Department Across Demographic Groups: Retrospective Cohort Study.](https://pubmed.ncbi.nlm.nih.gov/42090580/)
  来源：PubMed | 日期：2026-05-06 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Urinary tract infection (UTI) is a common emergency department (ED) presentation but can be challenging to diagnose; both overdiagnosis and underdiagnosis are common, and older adults may be at particular risk of misdiag...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Automation of Systematic Reviews with Large Language Models](https://www.medrxiv.org/content/10.1101/2025.06.13.25329541v4)
  来源：medRxiv | 日期：2026-05-04 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：系统综述（SR）是循证决策的核心，但其过程耗时且易出错。本研究验证了一种基于大语言模型（LLM）的工作流 otto-SR，旨在自动化文献筛选、数据提取和偏倚风险评估三项繁重任务。研究分四阶段进行：第一阶段在 32,357 条引文中测试，otto-SR 的筛选灵敏度（96.7%）显著优于人类研究员（81.7%）；第二阶段在 4,495 个数据点中测试，其提取准确率（93.1%）高于人类（79.7%）；第三阶段在偏倚风险评估（ROB2、Ne...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Deep Graph-Language Fusion for Structure-Aware Code Generation](http://arxiv.org/abs/2605.03689v1)
  来源：arXiv | 日期：2026-05-05 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Pre-trained Language Models (PLMs) have the potential to transform software development tasks. However, despite significant advances, current PLMs struggle to capture the structured and relational attributes of code, suc...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Natural Language Processing: A Comprehensive Practical Guide from Tokenisation to RLHF](http://arxiv.org/abs/2605.03799v1)
  来源：arXiv | 日期：2026-05-05 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：This preprint presents a systematic, research-oriented practicum that guides the reader through the entire modern NLP pipeline: from tokenisation and vectorisation to fine-tuning of large language models, retrieval-augme...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic publications: redesigning scientific publishing in the age of thinking large language models](http://arxiv.org/abs/2505.13246v2)
  来源：arXiv | 日期：2025-05-19 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Purpose: This paper introduces the concept of "Agentic Publication," a novel LLM-driven framework designed to complement traditional scientific publishing by transforming papers into interactive knowledge systems that ad...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From prompting to evidence-based translation: A RAG+prompt system for Japanese-Chinese translation and its pedagogical potential](http://arxiv.org/abs/2605.03387v1)
  来源：arXiv | 日期：2026-05-05 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Large language models perform well on high-resource pairs but are less reliable for Japanese-Chinese sentences containing noun-modifying clause constructions (NMCCs). This study evaluates a retrieval-augmented generation...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond Rules: LLM-Powered Linting for Quantum Programs](http://arxiv.org/abs/2605.03943v1)
  来源：arXiv | 日期：2026-05-05 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：As quantum computing transitions from theoretical experimentation to its practical application, the reliability of quantum software has become a critical bottleneck. Traditional static analysis techniques for quantum pro...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Can large language models approximate human perceptions of disease severity? An evaluation using Global Burden of Disease 2010 disability weights](https://www.medrxiv.org/content/10.64898/2026.05.02.26352261v1)
  来源：medRxiv | 日期：2026-05-04 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：伤残权重（DW）是衡量健康损失严重程度、估算全球疾病负担（GBD）中伤残调整寿命年的核心指标。传统 DW 估算依赖高成本的人口调查，难以快速更新。本研究评估了大型语言模型（LLM）通过结构化判断任务模拟人类对疾病严重程度感知的潜力。研究采用 GBD 2010 中的 222 种健康状态，利用 GPT-5 和 Claude 4.5 等四种模型进行了 24,531 对两两比较。结果显示，LLM 与 GBD 2010 DW 排名高度一致（Spe...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Systematic contextual biases in SegmentNT potentially relevant to other nucleotide transformer models](https://www.biorxiv.org/content/10.1101/2025.04.09.647946v2)
  来源：bioRxiv | 日期：2026-05-05 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in large language models (LLMs) have extended to genomic applications, yet model robustness relative to context is unclear. Here, we demonstrate two intrinsic biases (input sequence length and nucleotide ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Do Multimodal RAG Systems Leak Data? A Comprehensive Evaluation of Membership Inference and Image Caption Retrieval Attacks](http://arxiv.org/abs/2601.17644v3)
  来源：arXiv | 日期：2026-01-25 | 相关度：2.75 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：The growing adoption of multimodal Retrieval-Augmented Generation (mRAG) pipelines for vision-centric tasks (e.g., visual QA) introduces important privacy challenges. In particular, while mRAG provides a practical capabi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evolving Idea Graphs with Learnable Edits-and-Commits for Multi-Agent Scientific Ideation](http://arxiv.org/abs/2605.04922v1)
  来源：arXiv | 日期：2026-05-06 | 相关度：2.1 | 新颖度：7.78
  匹配主题：未命中具体主题
  中文摘要：LLM-empowered multi-agent systems offer new potential to accelerate scientific discovery by generating novel research ideas. However, existing methods typically coordinate agents through temporary texts, such as drafts o...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ContextPilot: Fast Long-Context Inference via Context Reuse](http://arxiv.org/abs/2511.03475v4)
  来源：arXiv | 日期：2025-11-05 | 相关度：2.1 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：AI applications increasingly depend on long-context inference, where LLMs consume substantial context to support stronger reasoning. Common examples include retrieval-augmented generation, agent memory layers, and multi-...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Q-RAG: Long Context Multi-step Retrieval via Value-based Embedder Training](http://arxiv.org/abs/2511.07328v2)
  来源：arXiv | 日期：2025-11-10 | 相关度：2.1 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）通过过滤相关上下文来提升大语言模型（LLM）性能，减少幻觉并降低推理成本。然而，现有RAG方法多关注单步检索，难以应对需多步搜索的复杂问题。近期出现的多步检索方法通常涉及微调小型LLM，这不仅资源消耗大，且限制了大型LLM的使用。本研究提出Q-RAG，一种通过强化学习（RL）微调嵌入模型（Embedder）进行多步检索的新方法。Q-RAG为开放域问答提供了一种具有竞争力的资源高效型替代方案，并在BabiLong和R...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CAR: Query-Guided Confidence-Aware Reranking for Retrieval-Augmented Generation](http://arxiv.org/abs/2605.04495v1)
  来源：arXiv | 日期：2026-05-06 | 相关度：1.4 | 新颖度：6.03
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) depends on document ranking to provide useful evidence for generation, but conventional reranking methods mainly optimize query-document relevance rather than generation usefulness. A...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [In Line with Context: Repository-Level Code Generation via Context Inlining](http://arxiv.org/abs/2601.00376v3)
  来源：arXiv | 日期：2026-01-01 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：仓库级代码生成要求模型理解整个代码库中函数、类和模块间的复杂依赖关系。现有方法如检索增强生成（RAG）或基于上下文的函数选择往往依赖表面相似性，难以捕捉深层语义依赖。本文提出 InlineCoder 框架，通过将未完成函数内联到其调用图中，将复杂的仓库理解任务转化为更简单的函数级编码任务。InlineCoder 首先生成一个名为“锚点（anchor）”的草稿补全，用于近似下游依赖并进行基于困惑度的置信度评估。该锚点驱动双向内联过程：一是...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Biological Spatial Priors Regularize Foundation Model Representations for Cross-Site MSI Generalization in Colorectal Cancer](http://arxiv.org/abs/2605.02660v1)
  来源：arXiv | 日期：2026-05-04 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：从常规 H&E 染色全切片图像（WSIs）预测微卫星不稳定（MSI）状态是分子检测的一种实用替代方案，但模型在跨机构应用时往往泛化性较差。尽管基础模型表征具有通用性，但仍会编码特定站点的纹理特征。本研究探讨了源自 MSI 组织学的瓦片级空间先验是否能引导表征学习站点不变特征。研究引入了基于外周距离编码的生物学空间先验，以反映肿瘤浸润边缘的克罗恩样外周淋巴细胞反应，并评估了反映局部淋巴细胞与肿瘤比例的免疫邻域编码。这些先验被注入 Tran...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [InvisibleInk: High-Utility and Low-Cost Text Generation with Differential Privacy](http://arxiv.org/abs/2507.02974v3)
  来源：arXiv | 日期：2025-06-30 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：随着基于大语言模型（LLM）的长文本生成在检索增强生成（RAG）和推理时间扩展等范式中取得进展，如何安全地将私有信息融入生成过程仍是关键挑战。本文提出 InvisibleInk，这是一个针对敏感参考文本提供严格差分隐私（DP）保证的高可扩展长文本生成框架。该框架将 LLM 下一个词元分布的采样过程解释为对 Logits 的指数机制，并提出两项创新：首先，通过隔离并仅对模型 Logits 中相对于公共 Logits 的敏感信息进行裁剪，显...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RamanBench: A Large-Scale Benchmark for Machine Learning on Raman Spectroscopy](http://arxiv.org/abs/2605.02003v2)
  来源：arXiv | 日期：2026-05-03 | 相关度：0.7 | 新颖度：6.75
  匹配主题：未命中具体主题
  中文摘要：机器学习已改变多个科学领域，但拉曼光谱这一非侵入性分子分析技术仍缺乏标准化基准。由于数据集碎片化、评估不一致及模型难以捕捉光谱结构，该领域进展受限。为此，我们推出了 RamanBench，这是首个大规模、完全可重复的拉曼光谱机器学习基准。它统一了跨 4 个领域的 74 个数据集（其中 16 个为首次发布），包含 325,668 条光谱，涵盖多种实验条件下的分类与回归任务。我们采用标准化协议评估了 28 种模型，包括传统方法（如 PLS）...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Experiment-as-Code Labs: A Declarative Stack for AI-Driven Scientific Discovery](http://arxiv.org/abs/2605.04375v1)
  来源：arXiv | 日期：2026-05-06 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：为了释放 AI for Science 的全部潜力，必须将智能体从纯数字环境扩展到物理实验室。智能体在现实实验室中的控制与探索能力至关重要，因为物理实验仍是科学发现的基石。尽管自动化实验室正通过可编程 API 实现软件控制，但在强大的 AI 智能体与自动化设备之间仍存在鸿沟。本文提出“实验即代码（EaC）实验室”范式，其核心是将实验编码为声明式配置，并可编译为设备级 API。在该架构中，AI 智能体负责提出假设并编写声明式实验配置；系统...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [An Agent-Oriented Pluggable Experience-RAG Skill for Experience-Driven Retrieval Strategy Orchestration](http://arxiv.org/abs/2605.03989v1)
  来源：arXiv | 日期：2026-05-05 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）系统通常假设单一固定的检索流程足以应对各类异构任务，但事实性问答、多跳推理和科学验证对检索策略具有不同的偏好。本文提出了 Experience-RAG Skill，这是一种面向智能体（Agent）的可插拔检索编排层，位于智能体与检索器池之间。该技术通过分析当前场景、咨询经验记忆并选择合适的检索策略，最终向智能体返回结构化的证据。在固定候选池的实验中，Experience-RAG Skill 在 BeIR/nq、Be...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [A Multi-Survey Machine-Readable Corpus of Milky Way Globular Cluster Parameters for Retrieval-Augmented Generation Applications](http://arxiv.org/abs/2605.03099v1)
  来源：arXiv | 日期：2026-05-04 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：We present the Milky Way Globular Cluster Corpus v1.3.1, a unified machinereadable database of fundamental parameters for 174 Milky Way globular clusters assembled from four independent published surveys. Each cluster re...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [AgenticPosesRanker: An Agentic AI Framework for Physically Grounded Ranking of Protein-Ligand Docking Poses](http://arxiv.org/abs/2605.03707v1)
  来源：arXiv | 日期：2026-05-05 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Scoring functions remain the principal bottleneck in molecular docking: they routinely fail to rank near-native poses above decoys, and their composite single-score design obscures the physicochemical basis of each ranki...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Do Larger Models Really Win in Drug Discovery?A Benchmark Assessment of Model Scaling in AI-Driven Molecular Property and Activity Prediction](https://www.biorxiv.org/content/10.64898/2026.04.29.721568v1)
  来源：bioRxiv | 日期：2026-05-04 | 相关度：4.75 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：本研究评估了分子基础模型与通用大语言模型在药物研发中的“规模中心论”假设，即大型预训练模型是否优于小型化学信息学模型和特定任务的图神经网络（GNN）。研究涵盖22个分子属性和活性终点，包括公开的ADMET、Tox21基准及两个内部抗感染数据集（包含49,266个抗结核和2,088个抗疟疾数据）。在167,056次基于结构相似性划分的五折交叉验证评估中，传统机器学习模型（如RF(ECFP4)和ExtraTrees）在10个主要指标任务中获...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Benchmarking open-source tools for in silico antiviral drug discovery](http://arxiv.org/abs/2605.04265v1)
  来源：arXiv | 日期：2026-05-05 | 相关度：2.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：Antivirals are uniquely positioned to be deployed quickly during a new outbreak, especially when repurposed from approved drugs. Yet there are no FDA-approved antivirals for the majority of viral families with pandemic p...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [TCRTransBench: A Comprehensive Benchmark for Bidirectional TCR-Peptide Sequence Generation](http://arxiv.org/abs/2605.04762v1)
  来源：arXiv | 日期：2026-05-06 | 相关度：1.7 | 新颖度：7.33
  匹配主题：未命中具体主题
  中文摘要：T-cell receptor (TCR) interactions with antigenic peptides underpin adaptive immunity and are pivotal for personalized immunotherapy and vaccine development. Despite recent progress, computational modeling of TCR-peptide...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [SURE-RAG: Sufficiency and Uncertainty-Aware Evidence Verification for Selective Retrieval-Augmented Generation](http://arxiv.org/abs/2605.03534v1)
  来源：arXiv | 日期：2026-05-05 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）虽能将答案锚定在检索段落中，但检索并不等同于验证：相关段落未必能充分证明答案。本文针对选择性 RAG 回答提出了证据充分性验证框架 SURE-RAG。该框架旨在预测给定证据对候选答案是支持、反驳还是证据不足，并在未确立支持时拒绝回答。SURE-RAG 基于“证据充分性是集合级属性”的观察，认为独立段落评分无法检测缺失的推理环（hops）或未解决的冲突。该协议通过共享的配对级“主张-证据”验证器产生局部关系分布，并将...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Performance of Large Language Models as a Tool for Primary Care Consultations: Evaluation Study](https://www.medrxiv.org/content/10.64898/2026.04.29.26352082v1)
  来源：medRxiv | 日期：2026-05-04 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：自2022年ChatGPT发布以来，大语言模型（LLMs）在处理健康咨询等敏感且重要的信息需求方面演进迅速。本研究旨在识别生成式AI系统在应对关键医疗健康信息时的核心优劣势。研究采用问答（Q&A）形式，将用户查询作为输入，模型生成的回答作为输出。评估框架由两组不同专业的临床专家组成，从三个维度进行评价：医疗共识遵循程度、是否存在不当或错误信息、以及对用户的潜在危害性。实验选取了GPT-4o mini、Llama 3和MedLlama 3...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Guidance for high-quality functional gene embeddings from large language models](https://www.biorxiv.org/content/10.64898/2026.04.30.721875v1)
  来源：bioRxiv | 日期：2026-05-04 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly used to generate gene embeddings, yet systematic benchmarks of prompting strategies and practical guidance for obtaining biologically meaningful representations remain limite...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A-CODE: Fully Atomic Protein Co-Design with Unified Multimodal Diffusion](http://arxiv.org/abs/2605.03360v1)
  来源：arXiv | 日期：2026-05-05 | 相关度：3.75 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：We present A-CODE, a fully atomic unified one-stage protein co-design model that simultaneously refines discrete atom types and continuous atom coordinates. Unlike predominant two-stage methods that cascade structure des...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MoLF: Mixture-of-Latent-Flow for Pan-Cancer Spatial Gene Expression Prediction from Histology](http://arxiv.org/abs/2602.02282v2)
  来源：arXiv | 日期：2026-02-02 | 相关度：2.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：Inferring spatial transcriptomics (ST) from histology enables scalable histogenomic profiling, yet current methods are largely restricted to single-tissue models. This fragmentation fails to leverage biological principle...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Multiscale brain-wide mapping of α-synuclein-driven dopaminergic degeneration and white matter impairment in α-synucleinopathy mice](https://www.biorxiv.org/content/10.64898/2025.12.05.692595v2)
  来源：bioRxiv | 日期：2026-05-05 | 相关度：2.05 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：The spatiotemporal relationships among -synuclein inclusion formation, dopaminergic degeneration, and white matter microstructural changes remain poorly defined. To address this, we unilaterally injected preformed fibril...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [DoGMaTiQ: Automated Generation of Question-and-Answer Nuggets for Report Evaluation](http://arxiv.org/abs/2605.04458v1)
  来源：arXiv | 日期：2026-05-06 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：随着检索增强生成（RAG）系统的广泛应用，长篇引用报告的评估受到关注。评估框架的核心是使用原子事实（nuggets）来衡量报告对查询相关信息的覆盖度。传统上，nuggets 表现为简短陈述，而近期研究转向问答（QA）形式，以实现更细粒度的评估，将信息需求（问题）与满足需求的多样化内容（答案）解耦。然而，手动为每个主题策划 nugget 集耗时费力，在跨语言环境下尤为困难。为此，我们提出了 DoGMaTiQ，一个分三阶段生成高质量 QA ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Architectural Constraints Alignment in AI-assisted, Platform-based Service Development](http://arxiv.org/abs/2605.04973v1)
  来源：arXiv | 日期：2026-05-06 | 相关度：0.7 | 新颖度：6.88
  匹配主题：未命中具体主题
  中文摘要：AI辅助开发工具虽能实现服务的快速原型化，但往往缺乏对生产环境所需的架构约束、基础设施依赖和组织标准的认知，导致生成的产物表现脆弱且部署受限。本文提出一种检索增强的脚手架（scaffolding）方法，将基于平台的代码生成与智能体澄清循环（agentic clarification loops）相结合，旨在暴露并解决架构约束中的歧义。通过将模板检索与结构化交互相结合，该方法在服务脚手架搭建过程中嵌入了生产相关的考量。评估结果表明，与通用...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Fight Poison with Poison: Enhancing Robustness in Few-shot Machine-Generated Text Detection with Adversarial Training](http://arxiv.org/abs/2605.02374v1)
  来源：arXiv | 日期：2026-05-04 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：机器生成文本（MGT）检测对于监管信息生态至关重要，但现有检测器在少样本场景下表现不佳，且易受“拟人化”对抗攻击。本文从威胁建模视角出发，研究了仅输出黑盒设置下的检测器漏洞，并提出 REACT 框架。该框架通过对抗训练提升少样本检测的性能与鲁棒性，其核心是耦合一个拟人化攻击者与目标检测器：攻击者利用检索增强生成（RAG）制造高仿真对抗样本以规避检测，而检测器通过对比学习目标从对抗样本中学习，以稳定少样本表示。通过交替更新实现两者的协同进...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RAG over Thinking Traces Can Improve Reasoning Tasks](http://arxiv.org/abs/2605.03344v1)
  来源：arXiv | 日期：2026-05-05 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）在知识密集型任务中表现出色，但在数学和代码生成等推理密集型任务中效果有限。本文挑战了这一观点，指出限制不在于RAG本身，而在于语料库的选择。研究者提出检索“思考轨迹”（thinking traces），即在解决问题过程中产生的中间思维路径，而非传统文档。研究表明，思考轨迹是强大的检索源。为此，本文引入了T3方法，通过离线方式将这些轨迹转换为结构化、易于检索的表示形式，以提高可用性。在AIME 2025-2026、L...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 其他

- [Beyond Similarity Search: A Unified Data Layer for Production RAG Systems](http://arxiv.org/abs/2605.03275v1)
  来源：arXiv | 日期：2026-05-05 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) systems have become the standard architecture for grounding large language models in organizational knowledge. Yet production deployments consistently expose a gap between clean proto...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [Evaluating Retrieval-Augmented Generation for Explainable Malware Analysis](http://arxiv.org/abs/2605.03140v1)
  来源：arXiv | 日期：2026-05-04 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) are increasingly being used as security engineering tools to summarize and explain malware behavior to analysts. A common assumption is that Retrieval-Augmented Generation (RAG) improves expl...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [How Does Chunking Affect Retrieval-Augmented Code Completion? A Controlled Empirical Study](http://arxiv.org/abs/2605.04763v1)
  来源：arXiv | 日期：2026-05-06 | 相关度：0.7 | 新颖度：6.83
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）在代码补全中依赖分块（chunking）将源文件分割为可检索单元，但现有分块策略的选择往往缺乏实证依据。本研究通过受控实验，系统评估了分块对代码补全质量的影响。实验涵盖了四种代表性策略（函数、声明、滑动窗口和 cAST），结合 4 种检索器、5 种生成器及 9 种参数配置，在 RepoEval 和 CrossCodeEval 两个基准上开展了 864 组实验。结果显示，分块策略对 RAG 代码补全具有显著统计学影响...
  为什么值得看：How Does Chunking Affect Retrieval-Augme 与你的主题有弱匹配，暂时保留作低优先级跟踪。
