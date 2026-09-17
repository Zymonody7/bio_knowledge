# 每日论文监控日报 (2026-09-17)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 49 篇新论文。

## 抓取状态

- arXiv：成功，命中 60 篇
- PubMed：成功，命中 64 篇
- bioRxiv：失败，命中 0 篇，错误：503 Server Error: Service Unavailable
- medRxiv：失败，命中 0 篇，错误：('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [MedSAM3: Delving into Segment Anything with Medical Concepts](http://arxiv.org/abs/2511.19046v2)
  来源：arXiv | 日期：2025-11-24 | 相关度：7.8 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Medical image segmentation is fundamental for biomedical discovery. Existing methods lack generalizability and demand extensive, time-consuming manual annotation for new clinical application. Here, we propose MedSAM-3, a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HypoEvolve: Genetic Algorithms Enable Multi-Agent LLMs to Discover Scientific Hypotheses](http://arxiv.org/abs/2609.15938v1)
  来源：arXiv | 日期：2026-09-14 | 相关度：7.55 | 新颖度：1.2
  匹配主题：foundation_model_agent
  中文摘要：Scientific agents contribute to hypothesis discovery by synthesizing evidence, assessing proposals, and developing new explanations. Recent systems combine scientific agents with evolutionary search through critique, com...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multi-Agent Collaboration for Automated Design Exploration on High Performance Computing Systems](http://arxiv.org/abs/2603.11515v2)
  来源：arXiv | 日期：2026-03-12 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Today's scientific challenges, from climate modeling to Inertial Confinement Fusion design to novel material design, require exploring huge design spaces. In order to enable high-impact scientific discovery, we need to s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Enhancing Accessibility of Medical Texts through Large Language Model-Driven Plain Language Adaptation](http://arxiv.org/abs/2609.17398v1)
  来源：arXiv | 日期：2026-09-15 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：This paper addresses the challenge of making complex healthcare information more accessible through automated Plain Language Adaptation (PLA). PLA aims to simplify technical medical language, bridging a critical gap betw...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SegTME-UNI2: A Foundation Model-Based Framework for Generalisable Multiclass Cell Segmentation and LLM-Driven Tumour Microenvironment Characterisation in Histopathology](http://arxiv.org/abs/2606.17702v3)
  来源：arXiv | 日期：2026-06-16 | 相关度：6.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Characterising the TME from routine H&E-stained histology images requires simultaneous cell segmentation, biological feature extraction, and interpretable clinical reporting. We present SegTME-UNI2, a unified framework a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Where Should Agents Live? Energy-Memory Characterization of Agentic AI for the Edge-Cloud Continuum](http://arxiv.org/abs/2609.18283v1)
  来源：arXiv | 日期：2026-09-16 | 相关度：5.45 | 新颖度：6.33
  匹配主题：foundation_model_agent
  中文摘要：As telecommunication networks evolve toward autonomous 5G-Advanced and 6G operations, agentic artificial intelligence (AI) workflows, where large language models (LLMs) execute multi-step reasoning, invoke diagnostic too...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Abstention vs. Hallucination: Benchmarking LLM Source Attribution for Scientific Citations](http://arxiv.org/abs/2405.02228v5)
  来源：arXiv | 日期：2024-05-03 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) increasingly generate citation-backed responses, yet citation hallucination remains a major challenge for trustworthy scientific information access. We introduce REASONS, a benchmark of 12,72...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Long-Context Demonstration Selection Using State Space Models](http://arxiv.org/abs/2609.17888v1)
  来源：arXiv | 日期：2026-09-15 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：We study the problem of demonstration selection, which involves selecting a subset of examples for prepending to a query to a language model. This problem is closely related to in-context learning and language model infe...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [When Is Graph Structure Worth Its Cost? The Case for Structure Pricing in Retrieval-Augmented Generation](http://arxiv.org/abs/2609.18099v1)
  来源：arXiv | 日期：2026-09-16 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Graph-based retrieval-augmented generation (RAG) can help answer questions that require information from many documents. However, building a graph often requires many language-model calls during ingestion. It is therefor...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Knowledge-Graph Based Augmentation versus Retrieval Augmented Generation for Cultural-Related Question Answering](http://arxiv.org/abs/2609.18317v1)
  来源：arXiv | 日期：2026-09-16 | 相关度：6.55 | 新颖度：7.42
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) suffer from a long-tail deficit: culturally specific facts, particularly those concerning underrepresented regions such as Latin America, appear too rarely in pretraining corpora to be reliab...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [SurgRAW: Multi-Agent Workflow with Chain of Thought Reasoning for Robotic Surgical Video Analysis](http://arxiv.org/abs/2503.10265v3)
  来源：arXiv | 日期：2025-03-13 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Robotic-assisted surgery (RAS) is central to modern surgery, driving the need for intelligent systems with accurate scene understanding. Most existing surgical AI methods rely on isolated, task-specific models, leading t...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Protein function-conditioned language models for variant effect prediction and controllable design.](https://pubmed.ncbi.nlm.nih.gov/42136025/)
  来源：PubMed | 日期：2026-09-15 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Protein function-conditioned generative modeling can unify two core goals in protein engineering: predicting the effects of sequence variants and designing new sequences that satisfy functional constraints. We present a ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [LLMs as Master Forgers: Generating Synthetic Time Series Data for Manufacturing](http://arxiv.org/abs/2609.16155v1)
  来源：arXiv | 日期：2026-09-14 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：This paper presents a novel framework leveraging Large Language Models (LLMs) to generate synthetic time series data for manufacturing processes. Motivated by the scarcity of labeled time-series data in real-world manufa...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Democratizing Clinical Tumor Whole Genome Sequencing: 18-hour End-to-end Analysis via Trillion-parameter Large Language Models Locally Deployed on Consumer-grade Hardware](http://arxiv.org/abs/2609.17620v1)
  来源：arXiv | 日期：2026-09-14 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Whole genome sequencing (WGS) is essential for precision oncology, yet its clinical adoption remains limited by prohibitive computational costs and multi-day turnaround times. This work presents a fully localized low-res...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [HyLnc: a hybrid deep learning and feature-based approach for long non-coding RNA prediction.](https://pubmed.ncbi.nlm.nih.gov/42716909/)
  来源：PubMed | 日期：2026-12-31 | 相关度：5.75 | 新颖度：4.75
  匹配主题：foundation_model_agent
  中文摘要：Long non-coding RNAs (lncRNAs) play important roles in gene regulation, development and disease, yet accurate identification of lncRNAs from transcriptomic data remains a major computational challenge. Existing methods o...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [ContextSniper: AntTrail's Token-Efficient Code Memory for Repository-Level Program Repair](http://arxiv.org/abs/2607.01916v6)
  来源：arXiv | 日期：2026-07-02 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large language model agents can repair real repository issues, but they often spend large context budgets on whole-file reads, broad searches, and long terminal outputs where useful evidence is mixed with irrelevant code...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CASCADE: An Agentic Regulatory Network Framework for Patient-Data-Validated Downstream Perturbation Prediction](http://arxiv.org/abs/2608.05359v2)
  来源：arXiv | 日期：2026-08-05 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：CASCADE is an agentic framework that predicts downstream transcriptional effects of gene perturbation from precomputed ARACNe regulatory networks, exposed via MCP. Prior work validates such tools by checking whether pred...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Atria Dawn: The Dawn of Agentic Superintelligence](http://arxiv.org/abs/2609.15818v1)
  来源：arXiv | 日期：2026-09-14 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：As AI agents become participants in the development of their successors, they reshape both the production of intelligence and the role of human researchers. We introduce Atria Dawn Preview, a foundation agentic language ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AquiLLM: Evaluating Faithfulness in Open-Weight RAG-LLM Systems for Scientific Research](http://arxiv.org/abs/2609.16519v1)
  来源：arXiv | 日期：2026-09-15 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Scientific research increasingly relies on large, heterogeneous data sources, motivating interest in retrieval-augmented generation (RAG) systems that provide natural language access to scientific knowledge and research ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CLEAR: Cross-Source Evidence Adjudication for Large Language Models in Medicine](http://arxiv.org/abs/2609.16301v1)
  来源：arXiv | 日期：2026-09-14 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Medical knowledge evolves continuously, whereas the parametric knowledge encoded in large language models (LLMs) is fixed at training time. External retrieval, including retrieval-augmented generation (RAG), can provide ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Smarter by the Moment: Environment-Driven Dynamic Policies for Continual LLM Improvement](http://arxiv.org/abs/2609.16800v1)
  来源：arXiv | 日期：2026-09-15 | 相关度：4.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have achieved remarkable progress across diverse domains, but continual adaptation to evolving tasks and environments remains a key challenge. Existing memory-augmented approaches retrieve in...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AI-Driven Drug-Target Interaction Prediction: From Data Representation to Model Design.](https://pubmed.ncbi.nlm.nih.gov/42734525/)
  来源：PubMed | 日期：2026-09-14 | 相关度：3.75 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Drug-target interaction (DTI) prediction is central to drug discovery, target identification, and drug repurposing. With the rapid growth of biomedical data and advances in artificial intelligence (AI), DTI prediction ha...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Community-tailored One Health educational intervention to enhance knowledge and practices for zoonotic disease prevention in rural Thailand: A protocol for a prospective cluster randomised controlled Trial in Chanthaburi, Thailand (Saan Suk trial).](https://pubmed.ncbi.nlm.nih.gov/42743166/)
  来源：PubMed | 日期：2026-01-01 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Zoonotic infectious disease risk arises at human-animal-environment interfaces where pathogen spillover can occur. Rural communities living in biodiverse settings may experience frequent contact with wildlife and shared ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CompArt: Operationalizing Aesthetic Alignment in Text-to-Image Generation via Principles of Art](http://arxiv.org/abs/2503.12018v2)
  来源：arXiv | 日期：2025-03-15 | 相关度：2.75 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Text-to-Image (T2I) diffusion models have made rapid progress on semantic alignment (generating what is described in the prompt), yet users still lack reliable control over aesthetic composition (how visual elements are ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OpenAI4S: Code as Action, Science as Sessions](http://arxiv.org/abs/2609.15096v1)
  来源：arXiv | 日期：2026-09-14 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：AI co-scientists could accelerate computational research, but over a long-running study the workflow also has to stay inspectable, resumable and reproducible, which requires persistent computational state and provenance....
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [WFM: Wiki Foundation Model for Complex Agentic Reasoning](http://arxiv.org/abs/2609.18182v1)
  来源：arXiv | 日期：2026-09-16 | 相关度：1.4 | 新颖度：6.53
  匹配主题：未命中具体主题
  中文摘要：Real-world agents fundamentally require persistent non-parametric knowledge for dynamic reasoning, i.e., long-term memory and retrieval-augmented generation. While graphs have shown reliable advantages in providing struc...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Notes2Skills: From Lab Notebooks to Certainty-Aware Scientific Agent Skills](http://arxiv.org/abs/2606.11897v2)
  来源：arXiv | 日期：2026-06-10 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Scientific discovery workflows rely heavily on lab notes, where researchers record observations, interpret uncertain results, and plan follow-up experiments. Unlike polished publications, lab notes preserve evolving scie...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [VoxMind: An End-to-End Agentic Spoken Dialogue System](http://arxiv.org/abs/2604.15710v2)
  来源：arXiv | 日期：2026-04-17 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Recent end-to-end spoken dialogue models enable natural interaction. However, as user demands become increasingly complex, models that rely solely on conversational abilities often struggle to cope. Incorporating agentic...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Navigating Sparse Evidence: Agentic Visual RAG via Explicit Context Selection and Consolidation](http://arxiv.org/abs/2609.15800v1)
  来源：arXiv | 日期：2026-09-14 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Visual Retrieval-Augmented Generation (VRAG) empowers models to navigate and answer queries about visually rich documents by retrieving relevant page images as visual evidence and reasoning over their content. However, e...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PaperDoctor: Evidence-Grounded and Actionable Feedback for Scientific Papers in Progress](http://arxiv.org/abs/2609.16995v1)
  来源：arXiv | 日期：2026-09-15 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Autoresearch agents are reshaping the research ecosystem, but they can also let flawed claims enter the literature at scale. Human advisors catch such issues in drafts through careful, traceable feedback, yet advisor-sty...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [InceptionRAG: Stealthy Poisoning Attack Against Retrieval-Augmented Generation](http://arxiv.org/abs/2609.16818v1)
  来源：arXiv | 日期：2026-09-15 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) systems enhance large language models (LLMs) with external knowledge but have been demonstrated to be vulnerable to corpus poisoning. Existing poisoning attacks against RAG largely fo...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Exploring LLMs and RAG for Plausible and Explainable Material Prediction of Vehicle Components](http://arxiv.org/abs/2609.18437v1)
  来源：arXiv | 日期：2026-09-16 | 相关度：2.5 | 新颖度：6.73
  匹配主题：未命中具体主题
  中文摘要：In this work, we explore whether LLMs can accurately predict and explain plausible materials for vehicle components such as brake discs or fuel injectors without requiring extensive fine-tuning. We test and evaluate thre...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [CiteGuard-RAG: A Validation-Centered AI System for Evidence-Grounded Question Answering](http://arxiv.org/abs/2609.15830v1)
  来源：arXiv | 日期：2026-09-14 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) can improve access to complex information; however, retrieving evidence alone does not ensure that answers are grounded, citation-valid, or appropriately refused. This paper introduce...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Contiguity, Not Importance: Budgeted Repair of Stale KV Caches After Document Edits](http://arxiv.org/abs/2609.17983v1)
  来源：arXiv | 日期：2026-09-16 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：KV-cache reuse can reduce inference cost in retrieval-augmented generation and agentic systems, but cached contexts may become stale when retrieved knowledge, working memory, or user state is edited. Under causal self-at...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [RECTIFY: An Interactive Workbench for Post-Evaluation RAG Diagnosis, Repair, and Verification](http://arxiv.org/abs/2609.16764v1)
  来源：arXiv | 日期：2026-09-15 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) evaluators can identify failures such as weak retrieval, poor grounding, incomplete answers, and unsupported generation, but they rarely help developers decide what to repair next. We...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [ScienceBuddy: Recursive-in-Recursive Self-Improvement for Interactive Scientific Agents](http://arxiv.org/abs/2609.17523v1)
  来源：arXiv | 日期：2026-09-15 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：We introduce and release ScienceBuddy, an interactive scientific research workspace that brings continually improving scientific agents into researchers' everyday workflows. ScienceBuddy supports researchers in carrying ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Query-Aware Source-Risk Triage for Retrieval-Augmented Generation](http://arxiv.org/abs/2609.16564v1)
  来源：arXiv | 日期：2026-09-15 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) pipelines may omit a source's material relationship to the query. We study a pre-generation triage layer that treats this relationship as query dependent. The method routes canonical ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [SaltyMeta: a curated benchmark and protein language model-informed web tool for salty peptide prediction](http://arxiv.org/abs/2609.16809v1)
  来源：arXiv | 日期：2026-09-15 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Excess sodium intake remains a major public health challenge, while salty and saltiness-enhancing peptides offer a potential route to preserve sensory saltiness in reduced-sodium foods. Machine-learning studies of salty ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SpecLens: LLM-Based Verilog Generation with Specification-Derived Constraints via Behavioral Divergence](http://arxiv.org/abs/2609.16729v1)
  来源：arXiv | 日期：2026-09-15 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have recently shown promise in Verilog generation, but producing functionally correct RTL directly from natural-language specifications remains a highly challenging task. Existing approaches ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [DriveMCP: An Agentic AI framework for Advanced Driver Assistance System](http://arxiv.org/abs/2609.17247v1)
  来源：arXiv | 日期：2026-09-15 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：An agentic AI driver-assistance framework that integrates perception, compliance reasoning, vehicle-state interpretation, and safety arbitration into a modular and auditable pipeline. The architecture, referred to as Dri...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [LLM Inference in a Flash!](http://arxiv.org/abs/2609.16161v1)
  来源：arXiv | 日期：2026-09-14 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have shown impressive capabilities across a range of natural language processing tasks, and LLM inference has emerged as a critical workload for enabling downstream applications. The demands ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RegNetAgents: A Multi-Agent Framework for Cross-Network Regulatory Driver Identification in Cancer Genomics](http://arxiv.org/abs/2607.14097v2)
  来源：arXiv | 日期：2026-04-16 | 相关度：2.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：We introduce RegNetAgents, an AI-oriented multi-agent framework for structured, query-driven regulatory candidate identification across heterogeneous gene regulatory networks. The system enables unified analysis of bulk ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Seeing Through the MiRAGE: Evaluating Multimodal Retrieval Augmented Generation](http://arxiv.org/abs/2510.24870v3)
  来源：arXiv | 日期：2025-10-28 | 相关度：2.1 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：We introduce MiRAGE, an evaluation framework for retrieval-augmented generation (RAG) from multimodal sources. As audiovisual media becomes a more prevalent source of information online, RAG systems must integrate such m...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [One Size Does Not Fit All! Dynamic Retriever and Generator Selection for RAG](http://arxiv.org/abs/2609.17709v1)
  来源：arXiv | 日期：2026-09-15 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) systems typically employ fixed retriever and generator configurations across queries, despite substantial differences in query complexity and information needs, leading to inefficient...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Predicting Partial Answer Quality and Utility in Agentic Retrieval-Augmented Generation](http://arxiv.org/abs/2609.16453v1)
  来源：arXiv | 日期：2026-09-15 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Agentic Retrieval-Augmented Generation (RAG) has become a promising paradigm for multi-hop question answering, where a reasoning model iteratively issues queries to a retriever and incorporates newly retrieved context in...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ORDER: Task-Conditioned Routing for Retrieval-Augmented Generation](http://arxiv.org/abs/2609.17012v1)
  来源：arXiv | 日期：2026-09-15 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) pipelines typically rely on a fixed indexing and retrieval configuration determined at preprocessing time. This one-size-fits-all design is ill-suited to domain-expert settings, where...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Development of an AI-Based smartphone application for rapid tick identification and geospatial mapping: A pilot study.](https://pubmed.ncbi.nlm.nih.gov/42735788/)
  来源：PubMed | 日期：2026-09-14 | 相关度：4.4 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：Tick-borne diseases, particularly spotted fever group rickettsioses in the western regions of Japan, represent an increasing public health concern. Accurate tick identification is clinically important because pathogen tr...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [An injection-molded focal filter-integrated AI platform for cost-effective and highly sensitive molecular point-of-care testing.](https://pubmed.ncbi.nlm.nih.gov/42610358/)
  来源：PubMed | 日期：2026-09-16 | 相关度：2.7 | 新颖度：0.25
  匹配主题：pathogenomics
  中文摘要：The growing global demand for precise and accessible diagnostics underscores the need for decentralized, laboratory-grade molecular testing solutions. Current platforms are hindered by the high cost and fragility of glas...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Artificial intelligence and biosecurity: capabilities, threat pathways, and defense-in-depth governance](http://arxiv.org/abs/2609.16213v1)
  来源：arXiv | 日期：2026-09-14 | 相关度：4.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence is reshaping biological research across an increasingly connected digital-to-physical workflow. General-purpose large language models can retrieve and integrate scientific information, support exp...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。
