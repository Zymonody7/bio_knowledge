# 每日论文监控日报 (2026-11-24)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 48 篇新论文。

## 抓取状态

- arXiv：成功，命中 48 篇
- PubMed：成功，命中 30 篇
- bioRxiv：成功，命中 17 篇
- medRxiv：成功，命中 5 篇

## 最值得看

### Foundation Model / Agent

- [MAPLE: A hierarchical Multimodal Assistant for Pathology vision-Language Evaluation using logic and reasoning](https://www.biorxiv.org/content/10.64898/2026.11.21.768223v1)
  来源：bioRxiv | 日期：2026-11-23 | 相关度：8.9 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Pathological diagnosis requires integration of cellular morphology, tissue architecture, and clinical context across gigapixel whole-slide images (WSIs), yet existing vision-language models remain constrained to patch-ba...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Cross-modal RAG: Sub-dimensional Text-to-Image Retrieval-Augmented Generation](http://arxiv.org/abs/2505.21956v4)
  来源：arXiv | 日期：2025-05-28 | 相关度：7.9 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Text-to-image generation increasingly demands access to domain-specific, fine-grained, and rapidly evolving knowledge that pretrained models cannot fully capture, necessitating the integration of retrieval methods. Exist...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A2Holo: Dual-Stream Flow Matching of 3D Structure and a Protein Language Model for Conformational Transition Prediction](https://www.biorxiv.org/content/10.64898/2026.11.20.768033v1)
  来源：bioRxiv | 日期：2026-11-23 | 相关度：7.8 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Modelling a ligand-bound holo conformation from a ligand-free apo conformation is essential in structure-based drug discovery. We present A2Holo, which casts apo-to-holo prediction as flow matching between two experiment...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The unedited acceptance rate: a review-fidelity metric for human-in-the-loop clinical AI](https://www.medrxiv.org/content/10.64898/2026.11.19.26368546v1)
  来源：medRxiv | 日期：2026-11-23 | 相关度：7.55 | 新颖度：6.2
  匹配主题：foundation_model_agent
  中文摘要：Objective. Guidance for large language model (LLM) drafting in clinical care relies on human review, yet review is rarely measured as a control. We aimed to define computable measures of review fidelity, establish which ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MAASAI: A Tool-Augmented Multi-Agent System for Astronomical Data Analysis](http://arxiv.org/abs/2611.31088v1)
  来源：arXiv | 日期：2026-11-23 | 相关度：6.8 | 新颖度：7.62
  匹配主题：foundation_model_agent
  中文摘要：Modern astronomical workflows require the coordinated use of specialised software, scientific archives, heterogeneous data, and domain-specific knowledge. Advances in large language models and multimodal foundation model...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Machine learning prediction of antimicrobial resistance in respiratory metagenomes](https://www.biorxiv.org/content/10.64898/2026.11.20.768127v1)
  来源：bioRxiv | 日期：2026-11-23 | 相关度：9.5 | 新颖度：6.75
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Background: Targeted therapy for patients with suspected respiratory infections traditionally requires bacterial culture followed by phenotypic antimicrobial susceptibility testing (AST), a process that can take up to 5 ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [SAE-Audit: Clinical-Trial Prediction via Inference-Time Optimization of Black-Box LLMs Audited by Sparse Autoencoder Evidence](http://arxiv.org/abs/2611.29368v1)
  来源：arXiv | 日期：2026-11-22 | 相关度：7.8 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Clinical trials are costly and often take years to complete, making early outcome prediction valuable for trial planning. Large language models (LLMs) are increasingly used to forecast clinical-trial outcomes, yet their ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Thermodynamically Guided CRISPR Spacer Optimization: Strategy-Dependent Off-Target Trade-Offs.](https://pubmed.ncbi.nlm.nih.gov/43070968/)
  来源：PubMed | 日期：2026-11-23 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Most CRISPR-Cas9 design tools select guide RNAs (gRNAs) by ranking predefined candidates rather than actively optimizing them. Here we instead formulate SpCas9 spacer refinement as a constrained search problem, in which ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HealthFound: a health world model for quantitative reasoning on longitudinal health profiles](https://www.medrxiv.org/content/10.64898/2026.10.03.26364142v2)
  来源：medRxiv | 日期：2026-11-22 | 相关度：7.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Medical large language models have shown promise in medical knowledge retrieval and clinical reasoning but remain limited in quantitative reasoning over longitudinal health data, partly due to the lack of effective data ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Contextualizing Biological Language Models across Modalities via Logit-Space Contrastive Alignment](http://arxiv.org/abs/2606.18703v2)
  来源：arXiv | 日期：2026-06-17 | 相关度：7.1 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Pretrained biological language models encode rich probabilistic structure through native token distributions, but multimodal adaptation typically aligns hidden representations or replaces the native likelihood interface ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RumiFold: Teaching an LLM to Natively Fold Proteins and Reason About Their Function](http://arxiv.org/abs/2611.29444v1)
  来源：arXiv | 日期：2026-11-22 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Can we teach a general-purpose language model to fold proteins? And if so, what does learning to fold enable beyond structure prediction itself? We introduce RumiFold, a pretrained chat model that learns to predict prote...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Local Errors to System Failures: Modeling and Benchmarking Error Propagation in Multi-Agent LLM Systems](http://arxiv.org/abs/2611.31063v1)
  来源：arXiv | 日期：2026-11-23 | 相关度：6.15 | 新颖度：7.33
  匹配主题：foundation_model_agent
  中文摘要：In multi-agent systems (MAS) built on large language models (LLMs), errors can propagate through intermediate messages and compromise final answers. However, outcome-based evaluation obscures how agents amplify, attenuat...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Deciphering state bridges via a single-cell large language model](https://www.biorxiv.org/content/10.64898/2026.11.21.768275v1)
  来源：bioRxiv | 日期：2026-11-23 | 相关度：6.15 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Large-scale single-cell transcriptomic data provide a new avenue for precision medicine by uncovering cellular heterogeneity. However, systematic comparison of remodeling patterns across various biological states remains...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LLM-Based Assistant for Dog Care Guidance](http://arxiv.org/abs/2611.29286v1)
  来源：arXiv | 日期：2026-11-22 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：This study investigates whether domain grounding through Retrieval-Augmented Generation (RAG) and parameter-efficient fine-tuning using Low-Rank Adaptation (LoRA) can enhance the accuracy and reliability of pet care advi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ReproBAIT: Can coding agents build their own biological AI tools?](http://arxiv.org/abs/2610.19810v2)
  来源：arXiv | 日期：2026-10-14 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models are increasingly competent at leveraging scientific knowledge and existing computational tools to execute complex workflows. At present, little information exists on their ability to reconstruct too...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Automatic Occupational Coding through Retrieval-Augmented Generation](http://arxiv.org/abs/2611.31051v1)
  来源：arXiv | 日期：2026-11-23 | 相关度：5.45 | 新颖度：7.06
  匹配主题：foundation_model_agent
  中文摘要：Annually 1.9 million deaths and 89.7 million disability-adjusted life years are caused by exposure to agents during work (e.g., welding fumes, silica dust, and noise pollution). To improve worker health, high-quality exp...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SHAKTI: Evidence-Grounded Conversational AI for Nutrition and Health](http://arxiv.org/abs/2611.29988v1)
  来源：arXiv | 日期：2026-11-23 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) answer many diet and health questions but can state unsupported claims and cite sources that do not support them. We present SHAKTI (Smart Health Advisor for Knowledge-based Tailored Interven...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Segment Anything In-Context via Visual Demonstrations](http://arxiv.org/abs/2611.29896v1)
  来源：arXiv | 日期：2026-11-23 | 相关度：4.75 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：We present the Segment Anything Model via Visual Demonstrations (SAYD), a foundation model for in-context segmentation. Given visual demos comprising prompt images and their segmentation masks, SAYD segments coherent reg...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BMAM: Brain-inspired Multi-Agent Memory Framework](http://arxiv.org/abs/2601.20465v2)
  来源：arXiv | 日期：2026-01-28 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Language-model-based agents operating over extended interaction horizons face persistent challenges in preserving temporally grounded information and maintaining behavioral consistency across sessions, a failure mode we ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Unleashing the Value of Raw Point Clouds for 3D Understanding with LLMs](http://arxiv.org/abs/2611.29194v1)
  来源：arXiv | 日期：2026-11-22 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Standard 3D point cloud language models typically rely on pretrained point encoders to extract 3D features and project them into representations processable by large language models (LLMs). However, these encoders are of...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MusicRec: Audio, Lyrics, and Engagement Feature Enrichment for Music Recommendation](http://arxiv.org/abs/2606.00125v2)
  来源：arXiv | 日期：2026-05-28 | 相关度：3.45 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Music recommendation systems typically treat songs as opaque tokens, relying on interaction histories that overlook semantic or acoustic content. Prior LLM-augmented, multimodal, and text-enhanced sequential recommenders...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [DeepQuest: From Knowledge Gaps to Scientific Discovery in Alzheimer's Disease](http://arxiv.org/abs/2611.26343v2)
  来源：arXiv | 日期：2026-11-19 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Automating experiments does not necessarily advance scientific understanding. Research agents must identify meaningful knowledge gaps, determine what available data can resolve, and assess whether their findings advance ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Fine-Tuning Large Language Models for Relation Extraction within a Retrieval-Augmented Generation Framework](http://arxiv.org/abs/2406.14745v3)
  来源：arXiv | 日期：2024-06-20 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Information Extraction (IE) plays a pivotal role in transforming unstructured data into structured formats, such as Knowledge Graphs. One of the main tasks within IE is Relation Extraction (RE), which identifies relation...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Enabling Validation for Robust Few-Shot Recognition](http://arxiv.org/abs/2506.04713v5)
  来源：arXiv | 日期：2025-06-05 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：A key challenge in Few-Shot Recognition (FSR) is the scarcity of labeled task-specific data for training. Contemporary methods mitigate this challenge by exploiting pretrained Vision-Language Models (VLMs) for their lear...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Graph-based Nearest Neighbors with Dynamic Updates via Random Walks](http://arxiv.org/abs/2512.18060v2)
  来源：arXiv | 日期：2025-12-19 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Approximate nearest neighbor search (ANN) is a common way to retrieve relevant search results, especially now in the context of large language models and retrieval augmented generation. One of the most widely used algori...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Enhancing Code Consistency in AI Research with Large Language Models and Retrieval-Augmented Generation](http://arxiv.org/abs/2502.00611v2)
  来源：arXiv | 日期：2025-02-02 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Ensuring that code accurately reflects the algorithms and methods described in research papers is critical for maintaining credibility and fostering trust in AI research. This paper presents a novel system designed to ve...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SGR3 Model: Scene Graph Retrieval-Reasoning Model in 3D](http://arxiv.org/abs/2603.04614v3)
  来源：arXiv | 日期：2026-03-04 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：3D scene graphs provide a structured representation of object entities and their relationships, enabling high-level interpretation and reasoning for robots while remaining intuitively understandable to humans. Existing a...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CogRAG: Tackling Heterogeneous Cognitive Demands in RAG via Stratified Retrieval and Reasoning](http://arxiv.org/abs/2604.25928v3)
  来源：arXiv | 日期：2026-04-01 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) frameworks typically process all queries through a one-size-fits-all pipeline, ignoring the heterogeneous cognitive demands of different tasks. This cognitive-blind approach causes tw...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Genome-to-Image Translation: Reconstructing Escherichia coli Morphology from Genomic Sequences](http://arxiv.org/abs/2611.31132v1)
  来源：arXiv | 日期：2026-11-23 | 相关度：5.75 | 新颖度：6.45
  匹配主题：foundation_model_agent
  中文摘要：Antimicrobial resistance in Escherichia coli is established in routine practice by culture-based susceptibility testing, which is slow relative to the clinical need for an early treatment decision. Resistance status also...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Structure-Exploiting Hierarchical Retrieval for Long Narrative Documents: A Precision-Oriented Alternative to Learned Abstraction Trees](http://arxiv.org/abs/2611.29966v1)
  来源：arXiv | 日期：2026-11-23 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation over book-length documents must locate a small, coherent set of passages inside tens of thousands of tokens. Flat dense retrieval ignores document structure; RAPTOR instead builds a hierarc...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [Retrieval-Augmented Generation in the Agentic Era: Tradition, Present, and Prospect](http://arxiv.org/abs/2611.30181v1)
  来源：arXiv | 日期：2026-11-23 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) couples frozen language models with external, updatable knowledge, so that generation is grounded in retrieved evidence rather than in parametric memory alone. This work maps RAG in t...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [From Head to Tail: LLM-Augmented Sequential Recommendation and Trade-off Optimization](http://arxiv.org/abs/2611.31052v1)
  来源：arXiv | 日期：2026-11-23 | 相关度：0.7 | 新颖度：6.82
  匹配主题：未命中具体主题
  中文摘要：Recommender systems exhibit popularity bias, often under-serving long-tail and cold-start items with sparse interaction data. We propose a group-specific data augmentation approach that leverages LLMs to generate synthet...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Clever Hans to Hypotheses: Interpreting EEG Foundational Transformers with LRP](http://arxiv.org/abs/2605.11885v2)
  来源：arXiv | 日期：2026-05-12 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Emerging foundation models (FMs) in electroencephalography (EEG) promise a path to scale deep learning in diagnostics and brain-computer interfaces despite data scarcity, yet their opaque nature remains a barrier to wide...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [FOLD: Position-Free Far Memory with Local Order for Long-Context Speculative Decoding](http://arxiv.org/abs/2610.20392v2)
  来源：arXiv | 日期：2026-10-14 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Speculative decoding accelerates LLM generation through lightweight drafting and parallel verification. It is particularly promising for long inputs, where KV-cache access costs can be amortized over multiple accepted to...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Steering Automated Scientific Discovery via Audited Epistemic Exploration](http://arxiv.org/abs/2611.25214v2)
  来源：arXiv | 日期：2026-11-18 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Scientific discovery requires revisiting the hypotheses in light of new evidence and identifying promising directions beyond those already explored. However, research agents often make claims that are not supported by th...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [S$^2$LMR: Supervised Sequential Long-Context Multi-Step Retriever](http://arxiv.org/abs/2611.28995v1)
  来源：arXiv | 日期：2026-11-21 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Multi-step retrieval over long contexts is a key capability for retrieval-augmented generation, but strong existing approaches are costly and complex to train. Supervised retrievers are far simpler and cheaper, yet they ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Who Makes the Decision? Auditing an Agentic LLM Pipeline for Illicit Cryptocurrency Transaction Monitoring](http://arxiv.org/abs/2611.29829v1)
  来源：arXiv | 日期：2026-11-22 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Agentic pipelines that combine graph detectors, deterministic rules, retrieval-augmented generation and an LLM judge are being proposed to monitor illicit cryptocurrency flows and to write regulation-citing justification...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MemChain: Learning Interpretable Memory Traces for Memory-Augmented LLM Agents](http://arxiv.org/abs/2607.24097v2)
  来源：arXiv | 日期：2026-07-27 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Memory-augmented LLM agents typically answer queries by retrieving relevant memories and feeding them directly to an answer model. This retrieval-as-evidence paradigm assumes retrieved memories are already suitable for r...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [TUSI: A Citation-Grounded Graph-Based Benchmark for Retrieval-Augmented Generation in Persian Legal Question Answering](http://arxiv.org/abs/2611.21823v2)
  来源：arXiv | 日期：2026-11-16 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Evaluating retrieval-augmented generation (RAG) systems in Persian law remains challenging because benchmarks lack realism, grounding, and coverage of legal reasoning. Existing resources are either synthetically generate...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Beyond Single-Turn Privacy: Training-Data Leakage in Conversational RAG](http://arxiv.org/abs/2611.28748v1)
  来源：arXiv | 日期：2026-11-21 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) is known to reduce training-data leakage in single-turn interactions, but whether this protection persists over multi-turn conversations is unclear. We introduce CRELT (Conversational...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [ALIoTh: Orchestrating Multi-Agent LLMs for Autonomous IoT Penetration Testing](http://arxiv.org/abs/2611.25809v2)
  来源：arXiv | 日期：2026-11-19 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Penetration testing in Internet of Things (IoT) environments, especially those composed of various different devices, e.g., smart plugs, smart cameras, and smart doors, presents great challenges across the phases of info...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GENECraft: A Function- and Prior-Constrained Discrete Dynamical System for Controllable Regulatory DNA Design](https://www.biorxiv.org/content/10.64898/2026.11.16.767190v2)
  来源：bioRxiv | 日期：2026-11-22 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Designing regulatory DNA requires reconciling two complementary modeling paradigms: genomic language models (gLMs) capture evolutionary syntax without guaranteeing targeted regulatory activity, whereas sequence-to-functi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MH-RAG-DIVE: Dynamic and Cost-Efficient Multi-Hop RAG Evaluation via Tree-Cached Dialogue Simulation](http://arxiv.org/abs/2611.30335v1)
  来源：arXiv | 日期：2026-11-23 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Quality assessment is essential for determining whether changes to a Retrieval-Augmented Generation system improve or maintain its performance. However, existing evaluation approaches often rely on single-turn or single-...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RAVEN: A Self-RAG Based Agent for Threat Classification and Response](http://arxiv.org/abs/2611.25832v2)
  来源：arXiv | 日期：2026-11-19 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Security event analysis in large enterprises can be overwhelming, as each alert typically requires manual in- spection by human operators. This process is time-consuming and prone to inconsistencies, especially in high-v...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [From Technical Performance to Clinical Impact: Challenges and Opportunities for AI Modelling of CKD Progression.](https://pubmed.ncbi.nlm.nih.gov/43066646/)
  来源：PubMed | 日期：2026-11-21 | 相关度：3.75 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Chronic kidney disease (CKD) is a major global health burden, with highly heterogeneous trajectories ranging from long-term stability to rapid progression towards kidney failure and kidney replacement therapy. Accurate p...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [The Therapeutic Pipeline: Future Treatments and Precision Medicine.](https://pubmed.ncbi.nlm.nih.gov/43025460/)
  来源：PubMed | 日期：2026-11-23 | 相关度：3.7 | 新颖度：0.25
  匹配主题：pathogenomics
  中文摘要：Rare interstitial lung diseases (ILDs) represent a heterogeneous group of disorders characterized by various pathogenic mechanisms, clinical presentations, prognoses, and therapeutic challenges. Among these, acid sphingo...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [CRC tumor antigens and immune escape: Designing peptide vaccines for colorectal Cancer.](https://pubmed.ncbi.nlm.nih.gov/43072318/)
  来源：PubMed | 日期：2026-11-23 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Colorectal cancer (CRC) is a leading cause of global cancer mortality, with current therapies often limited by toxicity and resistance. Immunotherapy, particularly peptide-based vaccines, represents a promising alternati...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [SuSi-RAG: A Hybrid Graph RAG for Equipment Maintenance](http://arxiv.org/abs/2611.30588v1)
  来源：arXiv | 日期：2026-11-23 | 相关度：0.7 | 新颖度：5.52
  匹配主题：未命中具体主题
  中文摘要：In the manufacturing domain, equipment maintenance tasks depend on expert knowledge. Their documentation is often stored in heterogeneous formats and sources. The enhancement of LLMs with Retrieval-Augmented Generation (...
  为什么值得看：SuSi-RAG: A Hybrid Graph RAG for Equipme 与你的主题有弱匹配，暂时保留作低优先级跟踪。
