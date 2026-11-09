# 每日论文监控日报 (2026-11-09)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 28 篇新论文。

## 抓取状态

- arXiv：成功，命中 23 篇
- PubMed：成功，命中 28 篇
- bioRxiv：成功，命中 14 篇
- medRxiv：成功，命中 8 篇

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [Multi-agent LLM teams improve differential recall on curated cases but underperform on emergency working-label matching: a two-cohort, two-family evaluation](https://www.medrxiv.org/content/10.64898/2026.09.24.26363897v4)
  来源：medRxiv | 日期：2026-11-06 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Background. Whether multi-agent large language model (LLM) pipelines help, add nothing, or underperform a single call may depend on the input and scoring contract rather than the architecture; these boundary conditions a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic Pipeline for Large-Scale Clinical Data Queries in Enterprise Electronic Health Records](https://www.medrxiv.org/content/10.64898/2026.11.05.26367378v1)
  来源：medRxiv | 日期：2026-11-06 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Using electronic health record (EHR) data to answer clinical research questions is challenging. It requires understanding the research question, finding relevant information across different sources, and combining that i...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CacheGraft: Enhancing Retrieval-Augmented Generation via Latent-Space Document Enrichment](http://arxiv.org/abs/2611.07393v2)
  来源：arXiv | 日期：2026-11-05 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Recent work in machine learning has demonstrated that transformer-based language model agents can communicate state not only through text, but also directly in latent space via key-value (KV) caches. In this paper, we ar...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Discovering formally verified quantum programs with AI](http://arxiv.org/abs/2611.09822v1)
  来源：arXiv | 日期：2026-11-06 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：The timeline by which quantum computers can solve breakthrough problems in science depends on improved quantum algorithms as much as on better hardware. Such algorithmic advances are typically achieved through many years...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Typed-Centrality Grounding for Agentic GraphRAG: A Symbolic Approach for Agentic Reasoning](http://arxiv.org/abs/2611.09414v1)
  来源：arXiv | 日期：2026-11-06 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Knowledge Graphs (KGs) and Large Language Models (LLMs) represent two approaches for knowledge representation and reasoning over heterogeneous data. Recent research has explored their integration through Graph Retrieval-...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ROAM: Retrieval-Augmented Optimization for Feasible Multi-Day Itinerary Planning](http://arxiv.org/abs/2611.09407v1)
  来源：arXiv | 日期：2026-11-06 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) can draft plausible travel itineraries, but the plans they produce are frequently infeasible: attractions are grouped into days without regard for geography, opening hours are ignored, and a ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [RadMultiBench: A Reproducible Dual-Task Benchmark Exposing the Limits of Pre-Trained Vision-Language Models Across Thoracic and Breast Imaging](https://www.biorxiv.org/content/10.64898/2026.11.04.764428v1)
  来源：bioRxiv | 日期：2026-11-06 | 相关度：7.1 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：We present RadMultiBench, a multimodal benchmark of 6,148 medical images paired with expert radiological impressions across five categories--Breast Cancer, Lung Benign, Lung Malignant, Pneumonia, and Tuberculosis--target...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Zero-Shot Protein-Ligand Binding Site Prediction from Protein Sequence and SMILES](https://www.biorxiv.org/content/10.1101/2025.09.28.679103v2)
  来源：bioRxiv | 日期：2026-11-07 | 相关度：5.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Accurate identification of protein-ligand binding sites is critical for mechanistic biology and drug discovery, yet predictive performance varies substantially across ligand families and data-availability regimes. We pre...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Definitions, Label Names, or Demonstrations? Auditing What Governs LLM Annotation](http://arxiv.org/abs/2611.09457v1)
  来源：arXiv | 日期：2026-11-06 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly used to annotate social-science texts, but high accuracy does not establish that they apply researcher-supplied category definitions: predictions may instead reflect prior as...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Contrastive Distribution Matching for Amortized Sequential Monte Carlo in Discrete Diffusion](http://arxiv.org/abs/2605.23346v2)
  来源：arXiv | 日期：2026-05-22 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Discrete diffusion models have emerged as powerful frameworks for generating structured categorical data. However, efficiently sampling from reward-tilted distributions remains a fundamental challenge. While Twisted Sequ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RAG-Enhanced LLMs for Interactive Explainability in Clinical Decision Support Systems](http://arxiv.org/abs/2611.09232v1)
  来源：arXiv | 日期：2026-11-06 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Artificial Intelligence (AI) is increasingly embedded in high-risks decision-making systems across domains such as healthcare, finance, and the judicial system. As reliance on predictive models grows, so does the demand ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [pLM-bVAE: protein language model-enhanced binary representation improves quantum annealing-based protein sequence design](https://www.biorxiv.org/content/10.64898/2026.11.05.764447v1)
  来源：bioRxiv | 日期：2026-11-06 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Quantum annealing (QA) has been explored as an approach for protein design in vast combinatorial sequence spaces. Applying QA to protein sequence design requires amino acid sequences to be encoded as binary vectors, and ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Generative Latent Priors for Interpreting and Steering Protein Language Models](http://arxiv.org/abs/2611.09818v1)
  来源：arXiv | 日期：2026-11-06 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Dominant methods for interpreting large models impose strong structural assumptions. Generative Latent Priors (GLP) are a complementary approach: a diffusion model that learns the distribution of a frozen model's activat...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Knowledge Graph-based Retrieval-Augmented Generation for Schema Matching](http://arxiv.org/abs/2501.08686v2)
  来源：arXiv | 日期：2025-01-15 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Traditional similarity-based schema matching methods fail to resolve semantic ambiguities and conflicts in complex, domain-specific mappings due to a lack of commonsense and domain-specific knowledge. In parallel, large ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 其他

- [Agentic AI Scientists Are Not Built For Autonomous Scientific Discovery](http://arxiv.org/abs/2605.08956v3)
  来源：arXiv | 日期：2026-05-09 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：A growing body of work pursues AI scientists capable of end-to-end autonomous scientific discovery. This position paper argues that although they already function as co-scientists, agentic AI scientists are not built for...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Towards an analytical framework for investigating the neurophysiological influence of social context in speech perception](https://www.biorxiv.org/content/10.64898/2026.11.05.764590v1)
  来源：bioRxiv | 日期：2026-11-06 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Social information plays an important role in everyday speech communication, yet existing neurophysiological approaches provide limited means of isolating its contribution during naturalistic speech perception. Here, we ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Knowledge Database of Physical Activity Interventions for Hypertension using Large Language Models](https://www.medrxiv.org/content/10.64898/2026.10.22.26366246v3)
  来源：medRxiv | 日期：2026-11-06 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Physical exercise lowers blood pressure, but guidelines provide broad recommendations that rarely account for age, comorbidities, medications and hypertension severity. A structured, queryable resource of exercise interv...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [GRAC: Graph-Based Retrieval-Augmented Captioning for Surgical Scene Description](http://arxiv.org/abs/2611.09866v1)
  来源：arXiv | 日期：2026-11-06 | 相关度：3.05 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Purpose: Surgical operative reports support procedural documentation, surgical training, performance assessment, and workflow review. However, extracting meaningful information often requires extensive manual review and ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OMG-Agent: Toward Robust Missing Modality Generation with Decoupled Coarse-to-Fine Agentic Workflows](http://arxiv.org/abs/2602.04144v2)
  来源：arXiv | 日期：2026-02-04 | 相关度：2.75 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Data incompleteness severely impedes the reliability of multimodal systems. Existing reconstruction methods face distinct bottlenecks: conventional parametric/generative models are prone to hallucinations due to over-rel...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EIN-RECAP: Evidence-Grounded Multi-Agent Summarization and Retrieval of Infectious-Disease Expert Discussions](https://www.medrxiv.org/content/10.64898/2026.11.05.26367381v1)
  来源：medRxiv | 日期：2026-11-06 | 相关度：2.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Infectious disease experts exchange practical knowledge through clinical discussions, but identifying relevant information across years of conversations is difficult. These discussions often contain differing opinions an...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Towards an Autonomous AI Steward for Large-Scale Physics Experiments: Integrating Causal Diagnostics, RAG, and Conformal Prediction](http://arxiv.org/abs/2611.09298v1)
  来源：arXiv | 日期：2026-11-06 | 相关度：2.1 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Long-term particle physics experiments face critical operational challenges: monitoring non-stationary machine data streams and preserving tacit expert knowledge. We present the "Helmholtz Co-Pilot," a hybrid Multi-Agent...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Nebula: Distributed Position-Independent Caching for LLM Serving](http://arxiv.org/abs/2611.09474v1)
  来源：arXiv | 日期：2026-11-06 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Modern LLM workflows, such as retrieval-augmented generation (RAG) and LLM agents, build long prompts from multiple independent text segments, making prefill a major source of computation. Reusing KV caches is therefore ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Detecting Knowledge Inconsistencies Across Text, Tables, and Knowledge Graphs](http://arxiv.org/abs/2607.25959v3)
  来源：arXiv | 日期：2026-07-28 | 相关度：0.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Wikipedia and Wikidata are widely used for information access, LLM pre-training, and retrieval-augmented generation. Their knowledge is deeply connected but scattered across text, tables, and knowledge graphs. This raise...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Intentmaking and Sensemaking: Human Interaction with AI-Guided Mathematical Discovery](http://arxiv.org/abs/2605.05921v2)
  来源：arXiv | 日期：2026-05-07 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Artificial intelligence offers powerful paradigms for scientific discovery, orchestrating autonomous inner search loops over long horizons. However, discovery remains bottlenecked by the friction of the outer human-AI lo...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [CauloBrowser 2.0: an AI powered update](https://www.biorxiv.org/content/10.64898/2026.11.05.764773v1)
  来源：bioRxiv | 日期：2026-11-06 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：CauloBrowser is a systems-biology database for Caulobacter crescentus that organizes the largest repository of experimental data for this model bacterium. The original CauloBrowser provided a web interface for accessing ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Atomic Trajectory Modeling with State Space Models for Biomolecular Dynamics](http://arxiv.org/abs/2603.17633v2)
  来源：arXiv | 日期：2026-03-18 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Understanding the dynamic behavior of biomolecules is fundamental to elucidating biological function and facilitating drug discovery.While Molecular Dynamics (MD) simulations provide a rigorous physical basis for studyin...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Agentic AI for Healthcare Claim Denial Analysis: A Policy-Grounded Framework for Privacy Preservation](http://arxiv.org/abs/2611.09423v1)
  来源：arXiv | 日期：2026-11-06 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：In the healthcare sector, claim denials impose significant financial and administrative burdens, emphasizing the need for automated and trustworthy decision-support systems. This paper proposes a modular Agentic Artifici...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Multimodal AI in Oral Cancer: A PRISMA-Guided Systematic Review.](https://pubmed.ncbi.nlm.nih.gov/42999821/)
  来源：PubMed | 日期：2026-01-01 | 相关度：3.75 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Oral cancer presents significant diagnostic and prognostic challenges, often due to late-stage detection and tumour heterogeneity. Recent advancements in artificial intelligence (AI), particularly deep learning (DL) and ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
