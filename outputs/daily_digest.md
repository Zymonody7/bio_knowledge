# 每日论文监控日报 (2026-10-08)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 50 篇新论文。

## 抓取状态

- arXiv：成功，命中 52 篇
- PubMed：成功，命中 51 篇
- bioRxiv：失败，命中 0 篇，错误：500 Server Error: Internal Server Error
- medRxiv：失败，命中 0 篇，错误：500 Server Error: Internal Server Error

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [AI-Assisted Computational Reproducibility on the FABRIC Testbed](http://arxiv.org/abs/2606.25879v2)
  来源：arXiv | 日期：2026-06-24 | 相关度：7.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Computational reproducibility remains difficult despite being central to scientific research. In this paper, we show how the international FABRIC testbed, combined with a large language model (LLM) coding agent through L...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 产品应用 / 监测落地

- [Towards Explainable Conversational AI for Early Diagnosis with Large Language Models](http://arxiv.org/abs/2512.17559v2)
  来源：arXiv | 日期：2025-12-19 | 相关度：7.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Healthcare systems around the world are grappling with issues such as inefficient diagnostics, rising costs, and limited access to specialists. These challenges often contribute to delays in treatment and poorer health o...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 可追踪

### Foundation Model / Agent

- [Aligning Multimodal Patient Evidence with Biomedical Knowledge Graphs for Clinical LLMs](http://arxiv.org/abs/2610.06685v1)
  来源：arXiv | 日期：2026-10-05 | 相关度：8.5 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Clinical questions often depend on linking a patient's multimodal evidence to external biomedical knowledge, yet existing predictive systems rarely represent such links explicitly, so they can neither be traced to their ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Speak to a Protein: An Interactive Multimodal Co-Scientist](http://arxiv.org/abs/2510.17826v2)
  来源：arXiv | 日期：2025-10-01 | 相关度：7.8 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Building a working mental model of a protein typically requires weeks of reading, cross-referencing crystal and predicted structures, and inspecting ligand complexes, an effort that is slow, unevenly accessible, and ofte...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DrugMCTS: a drug repurposing framework combining multi-agent, RAG and Monte Carlo Tree Search](http://arxiv.org/abs/2507.07426v4)
  来源：arXiv | 日期：2025-07-10 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in large language models have demonstrated considerable potential in scientific domains such as drug repositioning. However, their effectiveness remains constrained when reasoning extends beyond the knowl...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Survey of Secure Retrieval-Augmented Generation](http://arxiv.org/abs/2604.08304v4)
  来源：arXiv | 日期：2026-04-09 | 相关度：6.8 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) improves large language models (LLMs) with external knowledge, but this access path creates security risks distinct from inherent prompt-only or parametric-model flaws. We frame secur...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Tutor, Not Solver: Designing a Guardrailed AI Assistant for Learning in Higher Education: A Design Case of PeteChat](http://arxiv.org/abs/2606.09845v2)
  来源：arXiv | 日期：2026-04-27 | 相关度：6.55 | 新颖度：6.2
  匹配主题：foundation_model_agent
  中文摘要：Generative artificial intelligence (AI) tutors hold significant promise for higher education, yet designing systems that scaffold learning without undermining academic integrity remains an open design challenge. This pap...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [KadiAssistant: A conversational AI Agent for information retrieval in Kadi4Mat](http://arxiv.org/abs/2605.18850v2)
  来源：arXiv | 日期：2026-05-13 | 相关度：6.55 | 新颖度：1.2
  匹配主题：foundation_model_agent
  中文摘要：We introduce KadiAssistant, a privacy-by-design AI assistant integrated into the Kadi research data ecosystem, enabling researchers to efficiently access, aggregate, and synthesize information from heterogeneous, privacy...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning](http://arxiv.org/abs/2602.08234v2)
  来源：arXiv | 日期：2026-02-09 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large Language Model (LLM) agents have shown stunning results in complex tasks, yet they often operate in isolation, failing to learn from past experiences. Existing memory-based methods primarily store raw trajectories,...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Robotic Ultra-Long-Horizon Manipulation Skills via Human-guided Lifelong Code Generation](http://arxiv.org/abs/2509.18597v3)
  来源：arXiv | 日期：2025-09-23 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) can translate natural-language instructions for robotic manipulation into executable code, but ambiguity, noisy generations, and limited context windows make ultra-long-horizon tasks unreliab...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [RECAST: Learning to Compute the Right Context through Adaptive Evidence Routing](http://arxiv.org/abs/2610.10507v1)
  来源：arXiv | 日期：2026-10-07 | 相关度：5.45 | 新颖度：7.76
  匹配主题：foundation_model_agent
  中文摘要：Large language models are increasingly applied to tasks grounded in long, heterogeneous information sources. Conventional Retrieval-Augmented Generation (RAG) relies on fixed similarity-based retrieval, while agentic var...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Omics data discovery agents: Agent-supported retrieval, reanalysis, and synthesis of published omics data.](https://pubmed.ncbi.nlm.nih.gov/42837398/)
  来源：PubMed | 日期：2026-10-06 | 相关度：7.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：The biomedical literature contains a vast collection of omics studies, yet most published data remain functionally inaccessible for computational reuse. When raw data are deposited in public repositories, essential infor...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SERA-IDS: Structured Experience Retrieval-Augmented Intrusion Detection with Small Language Models](http://arxiv.org/abs/2610.03999v2)
  来源：arXiv | 日期：2026-10-02 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) offer a flexible approach to network intrusion detection, but direct classification of numerical flow records can be unreliable without traffic- specific decision boundaries. Retrieval-augmen...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [PertMind: Eliciting Emergent Biological Reasoning in LLM via Reinforcement Learning on Cellular Perturbation Data](http://arxiv.org/abs/2608.16419v3)
  来源：arXiv | 日期：2026-08-17 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models can describe mechanisms, yet scalable post-training still depends on costly, manually curated biological reasoning traces. Here we show that cellular perturbation atlases can instead become reinforc...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Bridging the Evidence-to-Execution Gap:A Reflective Agent for Multi-Objective Peptide Design](http://arxiv.org/abs/2610.06190v1)
  来源：arXiv | 日期：2026-10-05 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) can reason over scientific literature to devise design strategies, yet fail to reliably implement them for biological sequences. While protein generative models learn sequence patterns, they ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Guideline-Augmented Multi-Agent Framework for Schema-as-Code Biomedical Named Entity Recognition](http://arxiv.org/abs/2610.02970v2)
  来源：arXiv | 日期：2026-10-02 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have shown promising potential for biomedical named entity recognition (BioNER) through instruction following and in-context learning. However, existing LLM-based BioNER methods still face tw...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic AutoRAG: RAG Pipeline Optimization through Reasoning-Driven Agents](http://arxiv.org/abs/2610.08452v1)
  来源：arXiv | 日期：2026-10-06 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) is a widely used approach for grounding large language models (LLMs) in external knowledge. However, configuring a pipeline is an expensive hyperparameter optimization problem over ma...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery](http://arxiv.org/abs/2603.08127v2)
  来源：arXiv | 日期：2026-03-09 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：The increasing adoption of Large Language Models (LLMs) has enabled AI scientists to perform complex end-to-end scientific discovery tasks requiring coordination of specialized roles, including idea generation and experi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ShanLiangRen: A Nutrition Agent for Personalized Daily Meal Planning](http://arxiv.org/abs/2610.07886v1)
  来源：arXiv | 日期：2026-10-06 | 相关度：2.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Dietary nutrition planning plays an important role in chronic disease management and maintaining a healthy body. In applications, it must simultaneously satisfy personalized constraints and reasonable multidimensional nu...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Pretraining Shapes Spectral Structure: Architecture- and Strategy-Conditional Prediction of OOD Robustness in Foundation Models](http://arxiv.org/abs/2610.09709v1)
  来源：arXiv | 日期：2026-10-07 | 相关度：1.7 | 新颖度：6.05
  匹配主题：未命中具体主题
  中文摘要：Can we determine whether a foundation model will generalize out-of-distribution (OOD) before any target data is available? Existing diagnostics require source or target data, which rules them out before a target domain e...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Cross-Agent Learning Signals Enable Coordinated Role-Decomposed LLM Training](http://arxiv.org/abs/2606.10684v2)
  来源：arXiv | 日期：2026-06-09 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Agentic search systems must coordinate evidence acquisition and response generation, yet existing approaches either couple both roles under a single agent objective or decompose them without disentangling their respectiv...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Finding the Right Balance: Relevance and Diversity in LLM Retrieval](http://arxiv.org/abs/2610.09412v1)
  来源：arXiv | 日期：2026-10-07 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Retrieval diversification is widely available in retrieval-augmented generation (RAG) frameworks, yet prior studies disagree on whether it improves retrieval and answer quality. We show that its effectiveness varies prim...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Retrieval-Augmented Generation Must Move Beyond Factual Grounding to Represent Diverse Opinions](http://arxiv.org/abs/2604.12138v5)
  来源：arXiv | 日期：2026-04-13 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) systems are built on an unexamined assumption - that queries have correct answers and retrieval should converge toward them. This position paper argues that this creates a factual bia...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [How High Is 0.6? Floors, Ceilings, and Headroom in Interpretability Probing](http://arxiv.org/abs/2610.08544v1)
  来源：arXiv | 日期：2026-10-06 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Probes are the workhorse of interpretability. If a model's hidden states predict a variable, the model is said to represent it. But a probe score has no fixed meaning. An $R^2$ of 0.6 may only reflect what the input alre...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RAG-PIBench: A Leakage-Aware Benchmark for Prompt-Injection Detection in Trustworthy RAG Systems](http://arxiv.org/abs/2610.08571v1)
  来源：arXiv | 日期：2026-10-06 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) systems are vulnerable to prompt-injection attacks embedded in retrieved content. We introduce RAG-PIBench, a benchmark for RAG-style prompt-injection detection containing 4,876 conte...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [UNREAL: Unifying Retrieval and Long-Context with a Single Model](http://arxiv.org/abs/2610.08463v1)
  来源：arXiv | 日期：2026-10-06 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Long-context inference and Retrieval-Augmented Generation (RAG) handle evidence selection at vastly different scales, from a single long prompt to an entire corpus. We ask whether a single model-internal mechanism can se...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RamanBench: A Large-Scale Benchmark for Machine Learning on Raman Spectroscopy](http://arxiv.org/abs/2605.02003v3)
  来源：arXiv | 日期：2026-05-03 | 相关度：0.7 | 新颖度：6.75
  匹配主题：未命中具体主题
  中文摘要：Machine Learning (ML) has transformed many scientific fields, yet key applications still lack standardized benchmarks. Raman spectroscopy, a widely used technique for non-invasive molecular analysis, is one such field wh...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Does Document Structure Help Dense Retrieval? A Placebo-Controlled Ablation of Four Mechanisms Across Two Corpora](http://arxiv.org/abs/2610.10170v1)
  来源：arXiv | 日期：2026-10-07 | 相关度：0.7 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation systems increasingly rely on document-structure treatments: structure-aligned chunking, LLM-generated chunk contexts, heading-path metadata, and hierarchical two-stage retrieval. Separate s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EntroPrefill: Renyi-Guided Context Pruning with Conditional Stability Guarantees for Retrieval-Augmented Generation](http://arxiv.org/abs/2610.09757v1)
  来源：arXiv | 日期：2026-10-07 | 相关度：0.7 | 新颖度：5.66
  匹配主题：未命中具体主题
  中文摘要：Mid-prefill pruning can reduce the sequence processed by deeper transformer layers, but attention concentration alone does not certify that discarded context is dispensable. We formulate EntroPrefill as a Renyi-guided pr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BioStudyBench: Evaluating Agents on Post-Cutoff Biomedical Studies](http://arxiv.org/abs/2610.07614v1)
  来源：arXiv | 日期：2026-10-06 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：We evaluate whether AI agents can match the reported findings of published biomedical studies using public data. Existing evaluations do not consistently separate analysis from prior knowledge or retrieval of the publish...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evolving in Thought Space: Training a Small Model at Test Time Unlocks Better Discoveries](http://arxiv.org/abs/2610.06269v1)
  来源：arXiv | 日期：2026-10-05 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Open-ended scientific discovery often requires repeatedly proposing and evaluating candidate solutions. LLM-based systems can support this process by generating and refining executable solutions from verifier feedback. M...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [From Chunks to Functional Evidence: Function-Aware Retrieval for EDA Documentation QA](http://arxiv.org/abs/2610.09361v1)
  来源：arXiv | 日期：2026-10-07 | 相关度：0.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) is widely used to ground answers in documents. For complex technical documentation, however, the primary bottleneck is often not model reasoning but a mismatch between a query and the...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Trustworthy Domain-Specific AI for Structured Knowledge Retrieval and Reasoning](http://arxiv.org/abs/2610.08894v1)
  来源：arXiv | 日期：2026-10-06 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：This dissertation presents a scalable architecture for transforming unstructured, domain-specific text into structured knowledge for retrieval and reasoning. It integrates semi-automatic corpus curation, semantic structu...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Uncovering Hierarchical Structure in LLM Embeddings Using Geometric and Topological Measures](http://arxiv.org/abs/2512.20926v3)
  来源：arXiv | 日期：2025-12-24 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：The rapid advancement of large language models (LLMs) has driven major advances across scientific domains, yet the hierarchical, geometric, and topological structure of their embedding spaces remains poorly understood. I...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Entropy-Guided Reverse-Causal AI to Identify Upstream Bottleneck Genes for Alzheimer's Drug Discovery](http://arxiv.org/abs/2610.08736v1)
  来源：arXiv | 日期：2026-10-06 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Identifying upstream regulators that connect several disease processes to therapeutic interventions is a central objective in Alzheimer's disease drug discovery. We propose an entropy-guided reverse-causal framework that...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [EC-RAG: Event Chain Retrieval-Augmented Generation for Long Video Understanding](http://arxiv.org/abs/2610.08674v1)
  来源：arXiv | 日期：2026-10-06 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Current large video-language models (LVLMs) still face challenges when dealing with long videos, mainly because frames are often processed independently, making it difficult to capture temporal dependencies across events...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Simultaneous detection of influenza and SARS-CoV-2 on an AI-nanopore multiplex platform.](https://pubmed.ncbi.nlm.nih.gov/42831434/)
  来源：PubMed | 日期：2026-10-05 | 相关度：2.65 | 新颖度：0.75
  匹配主题：sequencing_bioinformatics
  中文摘要：Seasonal influenza and SARS-CoV-2 co-circulate and present overlapping symptoms, creating demand for rapid multiplex diagnostics beyond the sensitivity limits of antigen tests and the infrastructure requirements of nucle...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RegNetAgents: A Multi-Agent Framework for Cross-Network Regulatory Driver Identification in Cancer Genomics](http://arxiv.org/abs/2607.14097v3)
  来源：arXiv | 日期：2026-04-16 | 相关度：2.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：We introduce RegNetAgents, an AI-oriented multi-agent framework for structured, query-driven regulatory candidate identification across heterogeneous gene regulatory networks. It integrates bulk tumor (TCGA) and single-c...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [De novo design of monoclonal and bispecific antibodies with OFAntibody](http://arxiv.org/abs/2610.09548v1)
  来源：arXiv | 日期：2026-10-07 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Recent advances in generative protein design have enabled de novo antibody generation with explicit target and epitope conditioning. However, most existing approaches remain formulated around a single antigen-antibody in...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SPLATIFY: Reproduce, Discover, Innovate! From Papers and Ideas to Trainable 3DGS Code](http://arxiv.org/abs/2610.09116v1)
  来源：arXiv | 日期：2026-10-06 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：The rapid growth of 3D Gaussian Splatting (3DGS) research demands significant effort to reimplement papers before building on them. We introduce SPLATIFY, a multi-agent framework that converts 3DGS papers into trainable ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Attention via Black-Box Vector Search](http://arxiv.org/abs/2610.10135v1)
  来源：arXiv | 日期：2026-10-07 | 相关度：0.7 | 新颖度：6.41
  匹配主题：未命中具体主题
  中文摘要：Sparse attention mechanisms estimate attention over $n$ tokens using a small subset of keys. Many existing approaches use maximum inner product search (MIPS) to retrieve the heaviest keys, which motivates the following q...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Retrieval Is Not Enough: Refreshing Memory for Frozen Time-Series Forecasters](http://arxiv.org/abs/2610.07834v2)
  来源：arXiv | 日期：2026-10-06 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented time-series forecasting uses the continuations of historical segments similar to the current context as references for a forecaster. Most existing methods build the retrieval memory once from the trai...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RAPO-Sol: Retrieval-Augmented Preference Optimization for Repository-Level Solidity Code Generation](http://arxiv.org/abs/2610.08429v2)
  来源：arXiv | 日期：2026-10-06 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Smart contracts written in Solidity manage assets, permissions, and irreversible state changes, making code generation both useful and security-critical. Repository-level Solidity generation is challenging because models...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SIFT: Search Intent-to-Filter Transformer for Multi-Task Personalized Filter Ranking at Airbnb](http://arxiv.org/abs/2610.07810v1)
  来源：arXiv | 日期：2026-10-06 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Search filters help guests navigate vast catalogs in two-sided marketplaces like Airbnb, and recommending the right filters can meaningfully lift booking conversion. Many such production filter-ranking systems, however, ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Current laboratory diagnostics for tuberculosis: from conventional approaches to next-generation molecular and immunological technologies.](https://pubmed.ncbi.nlm.nih.gov/42836916/)
  来源：PubMed | 日期：2026-10-06 | 相关度：5.0 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Tuberculosis (TB) remains a major global public health concern despite advances in diagnosis and treatment. Early and accurate diagnosis is essential for timely treatment initiation, interruption of transmission, and eff...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Microfluidic approaches to next- generation sequencing library preparation: innovations, clinical integration and point-of-care settings.](https://pubmed.ncbi.nlm.nih.gov/42802333/)
  来源：PubMed | 日期：2026-10-07 | 相关度：4.65 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Next-generation sequencing (NGS) has revolutionized genomics by enabling high-throughput, cost-effective analysis of nucleic acids for both research and clinical use. Despite advances in sequencing technology, library pr...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [BEACON-SP: Ontology-Grounded GraphRAG Framework for Clinical Suicide Risk Assessment](http://arxiv.org/abs/2610.09026v1)
  来源：arXiv | 日期：2026-10-06 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：We present BEACON-SP, an ontology-grounded Graph Retrieval-Augmented Generation (GraphRAG) framework for clinician-facing decision support in behavioral health settings such as suicide prevention, where effective assessm...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [HealthcareNLP: where are we and what is next?](http://arxiv.org/abs/2512.08617v2)
  来源：arXiv | 日期：2025-12-09 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：This tutorial focused on Healthcare Domain Applications of NLP, what we have achieved around HealthcareNLP, and the challenges that lie ahead for the future. Existing reviews in this domain either overlook some important...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Invisible Infrastructure at Risk: Funding Crises Threaten Global Bioscience Research.](https://pubmed.ncbi.nlm.nih.gov/42842927/)
  来源：PubMed | 日期：2026-10-07 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Modern biology depends on invisible infrastructure that is essential yet precariously funded. Millions of biological observations are interpreted through resources that sit beneath routine scientific practice, largely un...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Can AI Agents Make Open-Ended Scientific Discovery? Evidence from Station](http://arxiv.org/abs/2610.08927v1)
  来源：arXiv | 日期：2026-10-06 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Recent AI systems have made rapid progress in scientific discovery when given well-defined metrics, but whether they can autonomously undertake open-ended scientific discovery remains unclear. We investigate AI's ability...
  为什么值得看：Can AI Agents Make Open-Ended Scientific 与你的主题有弱匹配，暂时保留作低优先级跟踪。
