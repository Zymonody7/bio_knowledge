# 每日论文监控日报 (2026-05-12)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 48 篇新论文。

## 抓取状态

- arXiv：成功，命中 51 篇
- PubMed：成功，命中 40 篇
- bioRxiv：成功，命中 15 篇
- medRxiv：成功，命中 2 篇

## 最值得看

### Foundation Model / Agent

- [SAR-RAG: ATR Visual Question Answering by Semantic Search, Retrieval, and MLLM Generation](http://arxiv.org/abs/2602.04712v2)
  来源：arXiv | 日期：2026-02-04 | 相关度：7.9 | 新颖度：6.2
  匹配主题：foundation_model_agent
  中文摘要：We present a visual-context image-retrieval-augmented generation (ImageRAG)- assisted AI agent for automatic target recognition (ATR) of synthetic aperture radar (SAR) imagery. SAR is a remote sensing method used in defe...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PPI2Text: Captioning Protein-Protein Interactions with Coordinate-Aligned Pair-Map Decoding](http://arxiv.org/abs/2605.08924v1)
  来源：arXiv | 日期：2026-05-09 | 相关度：7.8 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Protein-protein interaction (PPI) modeling has been widely studied as a binary or multi-label classification task. While emerging multimodal large language models (LLMs) can now describe single proteins, they remain unab...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Geospatial-Temporal Sensemaking of Remote Sensing Activity Detections with Multimodal Large Language Model](http://arxiv.org/abs/2605.10739v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：7.5 | 新颖度：8.07
  匹配主题：foundation_model_agent
  中文摘要：We introduce SMART-HC-VQA, a Sentinel-2-based visual question answering dataset derived from the IARPA SMART Heavy Construction dataset, designed for spatiotemporal analysis of human activity. The dataset transforms cons...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Meow-Omni 1: A Multimodal Large Language Model for Feline Ethology](http://arxiv.org/abs/2605.09152v1)
  来源：arXiv | 日期：2026-05-09 | 相关度：7.5 | 新颖度：7.25
  匹配主题：foundation_model_agent
  中文摘要：Deciphering animal intent is a fundamental challenge in computational ethology, largely because of semantic aliasing, the phenomenon where identical external signals (e.g., a cat's purr) correspond to radically different...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MicroWorld: Empowering Multimodal Large Language Models to Bridge the Microscopic Domain Gap with Multimodal Attribute Graph](http://arxiv.org/abs/2605.10120v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：7.5 | 新颖度：6.72
  匹配主题：foundation_model_agent
  中文摘要：Multimodal large language models (MLLMs) show remarkable potential for scientific reasoning, yet their performance in specialized domains such as microscopy remains limited by the scarcity of domain-specific training dat...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TRACER: Verifiable Generative Provenance for Multimodal Tool-Using Agents](http://arxiv.org/abs/2605.09934v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：7.5 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Multimodal large language models increasingly solve vision-centric tasks by calling external tools for visual inspection, OCR, retrieval, calculation, and multi-step reasoning. Current tool-using agents usually expose th...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [DocSeeker: Structured Visual Reasoning with Evidence Grounding for Long Document Understanding](http://arxiv.org/abs/2604.12812v5)
  来源：arXiv | 日期：2026-04-14 | 相关度：6.8 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Existing Multimodal Large Language Models (MLLMs) suffer from significant performance degradation on the long document understanding task as document length increases. This stems from two fundamental challenges: 1) a low...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Theory of Multilevel Interactive Equilibrium in NeuroAI](http://arxiv.org/abs/2605.10505v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：6.55 | 新颖度：7.58
  匹配主题：foundation_model_agent
  中文摘要：We propose a game-theoretic framework for adaptive multi-agent intelligent systems. Unlike classical game theory, which often treats strategies as primitive objects chosen by perfectly rational agents, the proposed frame...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Merlin: Deterministic Byte-Exact Deduplication for Lossless Context Optimization in Large Language Model Inference](http://arxiv.org/abs/2605.09990v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：6.55 | 新颖度：7.06
  匹配主题：foundation_model_agent
  中文摘要：Data-intensive applications, ranging from large-scale retrieval systems to advanced data pipelines, are increasingly bottlenecked by the processing of highly redundant text corpora. We present Merlin, a local-first, agno...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RAG-HAR: Retrieval Augmented Generation-based Human Activity Recognition](http://arxiv.org/abs/2512.08984v2)
  来源：arXiv | 日期：2025-12-06 | 相关度：6.55 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：Human Activity Recognition (HAR) underpins applications in healthcare, rehabilitation, fitness tracking, and smart environments, yet existing deep learning approaches demand dataset-specific training, large labeled corpo...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [NyayaAI: An AI-Powered Legal Assistant Using Multi-Agent Architecture and Retrieval-Augmented Generation](http://arxiv.org/abs/2605.10155v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：6.55 | 新颖度：6.55
  匹配主题：foundation_model_agent
  中文摘要：Legal information in India remains largely inaccessible due to the complexity of legal language and the sheer volume of legal documentation involved in research and case analysis. This paper presents NyayaAI, an AI-power...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Towards Verifiable and Self-Correcting AI Physicists for Quantum Many-Body Simulations](http://arxiv.org/abs/2604.00149v2)
  来源：arXiv | 日期：2026-03-31 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：While large language models (LLMs) promise to revolutionize automated scientific discovery, their application in rigorous real-world physical research is stalled by two critical barriers: a lack of realistic evaluation b...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Architecture Matters More Than Scale: A Comparative Study of Retrieval and Memory Augmentation for Financial QA Under SME Compute Constraints](http://arxiv.org/abs/2604.17979v2)
  来源：arXiv | 日期：2026-04-20 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：The rapid adoption of artificial intelligence (AI) and large language models (LLMs) is transforming financial analytics by enabling natural language interfaces for reporting, decision support, and automated reasoning. Ho...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RFAmpDesigner: A Self-Evolving Multi-Agent LLM Framework for Automated Radio Frequency Amplifier Design](http://arxiv.org/abs/2605.10093v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：6.15 | 新颖度：6.15
  匹配主题：foundation_model_agent
  中文摘要：Automating radio frequency (RF) amplifier design remains challenging because existing methods suffer from the curse of dimensionality, weak use of domain knowledge, and poor transferability, leading to low data efficienc...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MolRGen: A Training and Evaluation Setting for De Novo Molecular Generation with Reasonning Models](http://arxiv.org/abs/2603.18256v2)
  来源：arXiv | 日期：2026-03-18 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Recent reasoning-based large language models have shown strong performance on tasks with verifiable outcomes, but their use in de novo molecular generation remains limited by the lack of training environments where rewar...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PathISE: Learning Informative Path Supervision for Knowledge Graph Question Answering](http://arxiv.org/abs/2605.10791v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：5.45 | 新颖度：7.93
  匹配主题：foundation_model_agent
  中文摘要：Knowledge Graph Question Answering (KGQA) aims to answer user questions by reasoning over Knowledge Graphs (KGs). Recent KGQA methods mainly follow the retrieval-augmented generation paradigm to ground Large Language Mod...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Natural Language Processing: A Comprehensive Practical Guide from Tokenisation to RLHF](http://arxiv.org/abs/2605.03799v2)
  来源：arXiv | 日期：2026-05-05 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：This preprint presents a systematic, research-oriented practicum that guides the reader through the entire modern NLP pipeline: from tokenisation and vectorisation to fine-tuning of large language models, retrieval-augme...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ANCHOR: Abductive Network Construction with Hierarchical Orchestration for Reliable Probability Inference in Large Language Models](http://arxiv.org/abs/2605.10328v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：4.75 | 新颖度：6.21
  匹配主题：foundation_model_agent
  中文摘要：A central challenge in large-scale decision-making under incomplete information is estimating reliable probabilities. Recent approaches leverage Large Language Models (LLMs) to generate explanatory factors and elicit coa...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [VulTriage: Triple-Path Context Augmentation for LLM-Based Vulnerability Detection](http://arxiv.org/abs/2605.09461v1)
  来源：arXiv | 日期：2026-05-10 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Automated vulnerability detection is a fundamental task in software security, yet existing learning-based methods still struggle to capture the structural dependencies, domain-specific vulnerability knowledge, and comple...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PrimeKG-CL: A Continual Graph Learning Benchmark on Evolving Biomedical Knowledge Graphs](http://arxiv.org/abs/2605.10529v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：3.1 | 新颖度：8.16
  匹配主题：未命中具体主题
  中文摘要：Biomedical knowledge graphs underwrite drug repurposing and clinical decision support, yet the upstream ontologies they depend on update on independent cycles that add millions of edges and deprecate hundreds of thousand...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Generating Leakage-Free Benchmarks for Robust RAG Evaluation](http://arxiv.org/abs/2605.08838v1)
  来源：arXiv | 日期：2026-05-09 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) is widely used to augment large language models (LLMs) with external knowledge. However, many benchmark datasets, designed to test RAG performance, comprise many questions that can al...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Unified genomic and chemical representations enable bidirectional biosynthetic gene cluster and natural product retrieval.](https://pubmed.ncbi.nlm.nih.gov/42106434/)
  来源：PubMed | 日期：2026-05-09 | 相关度：8.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Natural product discovery is increasingly driven by the ability to analyze microbial genomes for biosynthetic gene clusters (BGCs) that encode secondary metabolites. While existing approaches have successfully linked BGC...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MedMeta: A Benchmark for LLMs in Synthesizing Meta-Analysis Conclusion from Medical Studies](http://arxiv.org/abs/2605.09661v1)
  来源：arXiv | 日期：2026-05-10 | 相关度：7.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have saturated standard medical benchmarks that test factual recall, yet their ability to perform higher-order reasoning, such as synthesizing evidence from multiple sources, remains critical...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Protein language model-guided generative design of affinity peptides for chromatographic purification of lentiviral vectors.](https://pubmed.ncbi.nlm.nih.gov/41833101/)
  来源：PubMed | 日期：2026-05-10 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Lentiviral vectors (LVs) have emerged as the most promising tool for cell and gene therapy. However, LVs are very fragile and sensitive to shear stress, buffer pH and salt concentration, resulting in serious hurdles in d...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [PTM-dCN: Latent Space Control for Post-translational Modification-aware Protein Design](https://www.biorxiv.org/content/10.64898/2026.05.06.714367v1)
  来源：bioRxiv | 日期：2026-05-11 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Post-translational modifications (PTMs) are critical for protein function, yet their precise design by harnessing site specific information derived from native proteins remains challenging. Here, we present a deep learni...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [The Truth Lies Somewhere in the Middle (of the Generated Tokens)](http://arxiv.org/abs/2605.09969v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：How should hidden states generated autoregressively be collapsed into a representation that reflects a language model's internal state? Despite tokens being generated under causal masking, we find that mean pooling acros...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Grounded Satirical Generation with RAG](http://arxiv.org/abs/2605.10853v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：5.45 | 新颖度：8.04
  匹配主题：foundation_model_agent
  中文摘要：Humor generation remains challenging task for Large Language Models (LLMs), due to their subjective nature. We focus on satire, a form of humor strongly shaped by context. In this work, we present a novel pipeline for gr...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GRC: Unifying Reasoning-Driven Generation, Retrieval and Compression](http://arxiv.org/abs/2605.09100v1)
  来源：arXiv | 日期：2026-05-09 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Text embedding and generative tasks are usually trained separately based on large language models (LLMs) nowadays. This causes a large amount of training cost and deployment effort. Context compression is also a challeng...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Assessment of RAG and Fine-Tuning for Industrial Question-Answering-Applications](http://arxiv.org/abs/2605.09533v1)
  来源：arXiv | 日期：2026-05-10 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) are increasingly employed in enterprise question-answering (QA) systems, requiring adaptation to domain-specific knowledge. Among the most prevalent methods for incorporating such knowledge a...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ArchRAG: Attributed Community-based Hierarchical Retrieval-Augmented Generation](http://arxiv.org/abs/2502.09891v4)
  来源：arXiv | 日期：2025-02-14 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) has proven effective in integrating external knowledge into large language models (LLMs) for solving question-answer (QA) tasks. The state-of-the-art RAG approaches often use the grap...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Understand and Accelerate Memory Processing Pipeline for Disaggregated LLM Inference](http://arxiv.org/abs/2603.29002v2)
  来源：arXiv | 日期：2026-03-30 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Modern large language models (LLMs) increasingly depends on efficient long-context processing and generation mechanisms, including sparse attention, retrieval-augmented generation (RAG), and compressed contextual memory,...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Route Before Retrieve: Activating Latent Routing Abilities of LLMs for RAG vs. Long-Context Selection](http://arxiv.org/abs/2605.10235v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：4.75 | 新颖度：5.98
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in large language models (LLMs) have expanded the context window to beyond 128K tokens, enabling long-document understanding and multi-source reasoning. A key challenge, however, lies in choosing between ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 其他

- [Agentic AI Scientists Are Not Built For Autonomous Scientific Discovery](http://arxiv.org/abs/2605.08956v1)
  来源：arXiv | 日期：2026-05-09 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：A growing body of work pursues AI scientists capable of end-to-end autonomous scientific discovery. This position paper argues that although they already function as co-scientists, agentic AI scientists are not built for...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Polymer-Agent: Large Language Model Agent for Polymer Design.](https://pubmed.ncbi.nlm.nih.gov/42048526/)
  来源：PubMed | 日期：2026-05-11 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：按需聚合物发现对于从生物医学应用到增强材料的各个行业都至关重要。传统的聚合物实验涉及漫长的试错过程，消耗大量资源。虽然机器学习在性能预测和潜空间搜索方面加速了科学发现，但受限于基础设施，实验室研究人员往往难以直接调用代码和模型来提取特定结构与性能。本文提出了 Polymer-Agent，这是一个集成在终端中的闭环聚合物结构-性能预测框架，用于早期聚合物发现。该框架利用大语言模型（LLM）的推理能力，为用户提供性能预测、性能导向的聚合物结...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Prompt-engineering improves clinical safety of large language models for opioid equipotency conversion](https://www.medrxiv.org/content/10.64898/2026.05.06.26352590v2)
  来源：medRxiv | 日期：2026-05-09 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Background: Large language models (LLMs) are increasingly used in medical education and clinical decision-making, but their reliability in high-risk medication dosing remains unclear. Opioid rotation is a common task req...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Knowledge Poisoning Attacks on Medical Multi-Modal Retrieval-Augmented Generation](http://arxiv.org/abs/2605.10253v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：2.75 | 新颖度：6.77
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) is a widely adopted paradigm for enhancing LLMs in medical applications by incorporating expert multimodal knowledge during generation. However, the underlying retrieval databases may...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [No Mean Feat: Simple, Strong Baselines for Context Compression](http://arxiv.org/abs/2510.20797v2)
  来源：arXiv | 日期：2025-10-23 | 相关度：1.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：上下文压缩通过将冗长的输入替换为更短的预计算表示，旨在降低 Transformer 模型的推理成本，这对于检索增强生成（RAG）具有重要意义。然而，由于评估标准和基准不统一，该领域的进展难以衡量。本研究设计了一个标准且易于复现的上下文压缩评估套件 BenchPress，并针对英语阅读理解任务提出了简单且高性能的基准方法。BenchPress 支持跨模型规模、数据集、压缩比以及短程（<1K token）到中程（<8K token）上下文的...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The Override Gap: A Magnitude Account of Knowledge Conflict Failure in Hypernetwork-Based Instant LLM Adaptation](http://arxiv.org/abs/2604.23750v2)
  来源：arXiv | 日期：2026-04-26 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：基于超网络的 LLM 瞬时适配方法（如 Doc-to-LoRA）能通过单次前向传播将文档知识内化至模型权重，但在处理知识冲突时存在系统性失效：当文档内容与预训练知识矛盾时，深度事实的准确率会骤降至 46.4%。研究表明，这种失效本质上是“幅度（Magnitude）”问题而非表征问题。超网络生成的适配器边际在不同文档间基本恒定，而预训练知识的边际随训练频率增长，导致深度冲突在结构上处于劣势。实验通过 194 个冲突案例证实，准确率随基座模...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MDGYM: Benchmarking AI Agents on Molecular Simulations](http://arxiv.org/abs/2605.08941v1)
  来源：arXiv | 日期：2026-05-09 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：AI驱动的科学发现取决于AI智能体能否自主设计并执行复杂的计算工作流。分子动力学（MD）模拟是测试这一能力的理想场景，因为它要求将物理直觉转化为语法和语义正确的输入脚本，推理初始及边界条件，诊断数值不稳定的轨迹，并根据物理定律解释输出。本文推出了MDGYM，这是一个包含169个专家策划的MD模拟基准测试，涵盖了LAMMPS和GROMACS两个广泛使用的软件包，并设有三个难度等级。研究评估了Claude Code、Codex和OpenHa...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [The landscape of structural variation in pediatric cancer.](https://pubmed.ncbi.nlm.nih.gov/41825442/)
  来源：PubMed | 日期：2026-05-11 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：结构变异（SVs）占儿童癌症驱动变异的60%以上。本研究通过对1,616例儿童和2,203例成人全基因组（WGS）的泛癌分析显示，儿童癌症的SV负荷在不同癌种间存在约100倍的差异。与成人脑肿瘤和实体瘤相比，儿童的SV负荷降低了6至16倍，但在血液恶性肿瘤中两者相当。研究发现，受SV破坏最严重的基因在儿童癌症中多为驱动基因，而在成人癌症中则多为脆性位点。在儿童急性淋巴细胞白血病中，RAG重组信号序列附近的复发性SV热点会同时破坏免疫位点...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [ASTRA-QA: A Benchmark for Abstract Question Answering over Documents](http://arxiv.org/abs/2605.10168v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：0.7 | 新颖度：6.84
  匹配主题：未命中具体主题
  中文摘要：基于文档的问答（QA）日益涉及抽象性问题，这类问题要求从长文档或多篇文档中整合分散信息，生成连贯答案。然而，现有基准测试和评估方法对该场景支持不足，往往缺乏稳定的抽象参考，或依赖粗略的相似性指标及不稳定的两两比较。为此，我们推出了 ASTRA-QA，一个针对文档抽象问答的基准测试。ASTRA-QA 包含 869 个基于学术论文和新闻文档的 QA 实例，涵盖五种抽象问题类型和三种受控检索范围。每个实例均配备了明确的评估标注，包括答案主题集...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Governing AI-Assisted Security Operations: A Design Science Framework for Operational Decision Support](http://arxiv.org/abs/2605.09534v1)
  来源：arXiv | 日期：2026-05-10 | 相关度：2.75 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：随着生成式人工智能（AI）、检索增强生成（RAG）和编码智能体（Agents）在工程管理中的应用，如何在不损害问责制、隐私、成本控制和可审计性的前提下将其引入高风险运营职能成为关键。本研究提出，AI 辅助的运营决策支持在规模化自动化之前，应作为一种受控的工程能力进行管理。研究以安全运营中心（SOC）为背景，利用 Kusto 查询语言（KQL）和 Microsoft Azure 安全功能作为技术实例。尽管 KQL 通常是只读的，但 AI ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [eSkip2 prioritizes exon-skipping antisense oligonucleotide target regions across exon--intron contexts](https://www.biorxiv.org/content/10.64898/2026.05.05.722571v1)
  来源：bioRxiv | 日期：2026-05-11 | 相关度：1.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：用于外显子跳跃的反义寡核苷酸（ASO）正越来越多地被用于纠正致病性剪接，但由于调控信息分布在外显子、内含子和剪接接头中，合理选择目标区域仍具挑战。本研究提出了 eSkip2，这是一个利用外显子-内含子联合序列背景优先排序 ASO 目标区域的框架。eSkip2 结合了基因组预训练基础模型的迁移学习，以及 ASO 活性和单核苷酸变异（SNV）衍生的剪接扰动数据的联合训练，且无需实验性 ASO 标签即可适应特定的目标位点。在涵盖规范外显子、伪...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Validation of an AI-Powered Automated Colony Analysis Platform Across Eight ISO Microbiological Methods: A Multi-Pathogen, Multi-Matrix Performance Study](https://www.biorxiv.org/content/10.64898/2026.05.08.723721v1)
  来源：bioRxiv | 日期：2026-05-09 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：手动菌落计数是食品微生物质控中依赖操作员且限制效率的关键环节。本研究对 Reshape Smart Incubator（一种基于自动成像和机器学习的菌落分析系统）进行了前瞻性多中心验证，涵盖 8 种 ISO 微生物标准方法。研究共分析了 887 张培养皿，涉及李斯特菌和沙门氏菌的定性检测，以及总菌落数（TVC）、蜡样芽孢杆菌、肠杆菌科、凝固酶阳性葡萄球菌、霉菌酵母及乳酸菌的定量计数。自动化结果以 3 名及以上资深技术人员的共识为基准。结...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Qwen Goes Brrr: Off-the-Shelf RAG for Ukrainian Multi-Domain Document Understanding](http://arxiv.org/abs/2605.10296v1)
  来源：arXiv | 日期：2026-05-11 | 相关度：0.7 | 新颖度：6.11
  匹配主题：未命中具体主题
  中文摘要：本研究针对第五届UNLP多领域文档理解共享任务，提出了一种检索增强生成（RAG）流水线，旨在从乌克兰语PDF文档集中回答多项选择题并定位支持页面。该系统基于三个核心理念：PDF的上下文分块、问题感知的稠密检索、以及同时基于问题和答案选项的重排序，最后通过少量重排序段落进行约束性答案生成。系统架构采用Qwen3-Embedding-8B执行检索，微调后的Qwen3-Reranker-8B进行段落排序，并由Qwen3-32B完成最终答案选择...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Response-G1: Explicit Scene Graph Modeling for Proactive Streaming Video Understanding](http://arxiv.org/abs/2605.07575v2)
  来源：arXiv | 日期：2026-05-08 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：主动流式视频理解要求视频大语言模型（Video-LLMs）在视频展开过程中自主决定响应时机。现有方法由于对视觉证据采用隐式且与查询无关的建模，往往难以准确把握响应条件。本文提出 Response-G1 框架，通过场景图（Scene Graphs）在累积的视频证据与查询预期的响应条件之间建立显式的结构化对齐。该框架包含三个无需微调的阶段：(1) 从流式视频片段中生成在线查询引导的场景图；(2) 基于内存检索语义最相关的历史场景图；(3) ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [A Versatile AI Agent for Rare Disease Diagnosis and Risk Gene Prioritization](http://arxiv.org/abs/2605.06226v2)
  来源：arXiv | 日期：2026-05-07 | 相关度：2.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：准确及时的诊断对于罕见病治疗至关重要，但现有临床流程往往面临评估周期长和准确率低的问题。为解决这些局限性，我们推出了 Hygieia，这是一个多模态 AI Agent 系统，旨在通过整合表型特征、基因组谱和临床记录来支持精准疾病诊断。Hygieia 采用了基于路由（router-based）和知识增强的框架，旨在缓解大模型的幻觉问题，并针对不同疾病类别定制诊断策略。该系统能够优先排序罕见病相关的基因组风险因素，并提供置信度评分以辅助临床...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Byte-Exact Deduplication in Retrieval-Augmented Generation: A Three-Regime Empirical Analysis Across Public Benchmarks](http://arxiv.org/abs/2605.09611v1)
  来源：arXiv | 日期：2026-05-10 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：本研究针对检索增强生成（RAG）流程中的字节级块去重（byte-exact chunk-level deduplication）进行了实证分析。研究测量了三种不同运行场景下的上下文缩减效果：学术检索（基于2220万个BeIR段落，缩减0.16%）、构建的企业模式（缩减24.03%）以及多轮对话AI（缩减80.34%）。为验证去重后的质量保持情况，研究采用五人评委校准小组，对Google Gemini 2.5 Flash、Anthropi...
  为什么值得看：Byte-Exact Deduplication in Retrieval-Au 与你的主题有弱匹配，暂时保留作低优先级跟踪。
