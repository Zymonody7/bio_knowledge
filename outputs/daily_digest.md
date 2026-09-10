# 每日论文监控日报 (2026-09-10)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 51 篇新论文。

## 抓取状态

- arXiv：成功，命中 42 篇
- PubMed：成功，命中 67 篇
- bioRxiv：成功，命中 10 篇
- medRxiv：成功，命中 11 篇

## 最值得看

### Foundation Model / Agent

- [Bridging the Semantic-Utility Gap in Multimodal RAG via Generator-in-the-Loop Alignment](http://arxiv.org/abs/2609.08188v1)
  来源：arXiv | 日期：2026-09-08 | 相关度：7.5 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Vision-language models (VLMs) augmented with retrieval-augmented generation (RAG) benefit from access to external evidence. However, standard retrievers and rerankers optimize for semantic similarity rather than answer u...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Deep generative models in biological sequence and structure analysis and design.](https://pubmed.ncbi.nlm.nih.gov/42716354/)
  来源：PubMed | 日期：2026-09-09 | 相关度：8.5 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Deep generative models have transformed biological sequence modeling from predictive analysis toward increasingly controllable design. Early biological applications of Variational Autoencoders (VAEs) and Generative Adver...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [Structure-based Transfer Learning](http://arxiv.org/abs/2609.08487v1)
  来源：arXiv | 日期：2026-09-08 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Transfer learning improves estimation in a target study using information from related sources. Classical transfer learning is typically data-based, requiring access to the source data or to a model fitted on them. Neith...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Large language model-driven knowledge graph learning for herb-macromolecule interaction prediction and functional analysis.](https://pubmed.ncbi.nlm.nih.gov/42705563/)
  来源：PubMed | 日期：2026-09-07 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：The rapid accumulation of biological macromolecule data has created an urgent need for computational methods capable of characterizing the functional roles of macromolecular targets in complex therapeutic systems. Tradit...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Auditing Large Language Model-Generated Digital Standardized Patients for Demographic Bias: A Simulation Study with HIV Pre-Exposure Prophylaxis Screening as a Tracer Condition](https://www.medrxiv.org/content/10.64898/2026.09.01.26361928v1)
  来源：medRxiv | 日期：2026-09-07 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are entering clinical training as digital standardized patients (DSPs), simulated patient encounters the model scripts and portrays. Demographic associations learned from corpus co-occurrence...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Comparative Study in Surgical AI: Potential and Limitations of Data, Compute, and Scaling](https://www.medrxiv.org/content/10.64898/2026.03.26.26349455v5)
  来源：medRxiv | 日期：2026-09-07 | 相关度：6.8 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：本研究探讨了人工智能在外科图像分析领域的潜力与局限，特别是针对神经外科手术器械检测这一核心任务。研究人员评估了2023年至2026年初发布的19个开源视觉语言模型（VLM）的零样本性能，结果显示仅有一个模型略微超过13.4%的基准线。通过使用LoRA微调Gemma 3 27B模型生成结构化JSON预测，准确率提升至47.63%；而采用专用分类头的方法进一步将准确率提高到51.08%。实验发现，即使将可训练参数增加近三个数量级，验证集准确...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Using Reward Uncertainty to Induce Diverse Behaviour in Reinforcement Learning](http://arxiv.org/abs/2606.03962v2)
  来源：arXiv | 日期：2026-06-02 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Classical reinforcement learning (RL) typically seeks a deterministic policy that maximizes the expected sum of a scalar reward. Yet, modern applications such as language model fine-tuning or scientific discovery demand ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TianoForge: An Automated Bug Triage Approach for the TianoCore UEFI Firmware Development Community](http://arxiv.org/abs/2608.23259v2)
  来源：arXiv | 日期：2026-08-24 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：We propose a novel approach to bug triage in the TianoCore open-source UEFI firmware development ecosystem. This integrated approach, called TianoForge, deploys the state of the art in artificial intelligence, specifical...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CARRE: Counterfactual Action Retrieval and Reason Evaluation for Explainable Churn Prescription](http://arxiv.org/abs/2609.09766v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：6.15 | 新颖度：6.29
  匹配主题：foundation_model_agent
  中文摘要：Churn models typically identify high-risk customers but do not specify which feasible retention action should be considered or why that action is appropriate. We present CARRE (Counterfactual Action Retrieval and Reason ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [KARE-RAG: Knowledge-Aware Refinement and Enhancement for RAG](http://arxiv.org/abs/2506.02503v2)
  来源：arXiv | 日期：2025-06-03 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) equips large language models with external knowledge and is central to knowledge-intensive tasks. As RAG systems enter real-world use, generators must reliably leverage retrieved evid...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Vague2Detect: Handling Ambiguous Prompts in Knowledge-Based Open-World Detection](http://arxiv.org/abs/2609.09949v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：5.45 | 新颖度：6.63
  匹配主题：foundation_model_agent
  中文摘要：Real-world detectors must often interpret functional or ambiguous prompts, yet conventional models such as YOLO remain restricted to fixed class lists. Even open-vocabulary models like YOLO-World frequently misalign vagu...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [QO-Bench: Diagnosing Query-Operator-Preserving Retrieval over Typed Event Tuples](http://arxiv.org/abs/2606.04646v2)
  来源：arXiv | 日期：2026-06-03 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Many real-world questions over business, legal, and scientific corpora are natural-language versions of database-style queries over records latent in text. Existing retrieval-augmented generation (RAG) systems are optimi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Individual Text Corpora Predict User-Specific Knowledge: Benchmarks of Individualized Knowledge Simulation](http://arxiv.org/abs/2609.08532v1)
  来源：arXiv | 日期：2026-09-08 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：This study examines whether individual text corpora (ICs) from search histories can be used to simulate individual knowledge. We collected ICs from 316 adults, who answered 36 multiple-choice knowledge items, and compare...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Noēsis: Deterministic-First Retrieval with Two-Tier Context Hydration for Factuality-Critical Queries on Small Local Models](http://arxiv.org/abs/2609.07663v1)
  来源：arXiv | 日期：2026-09-07 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：A wrong number is worse than no answer. Across factuality-critical domains -- audience metrics, scheduling and rights in media; dosages and lab values in healthcare; figures and citations in finance and legal -- a confid...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The Answer Path and the Grounding Instruction in LLM Question Answering over Knowledge Graphs](http://arxiv.org/abs/2609.10237v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：4.75 | 新颖度：7.19
  匹配主题：foundation_model_agent
  中文摘要：A graph retrieval-augmented generation pipeline chooses which triples to put in the prompt, a syntax to write them in, an order to write them in, and a sentence telling the model what to do with them. We vary all four ov...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LM-X: Explainable Vision--Language--Action Modeling via Progress, Event, and Uncertainty Prediction](http://arxiv.org/abs/2608.25757v4)
  来源：arXiv | 日期：2026-08-26 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large-scale vision--language--action (VLA) policies have advanced generalist robot control, yet most remain stimulus-to-action black boxes: actions are exposed, but their explanatory state is not. They provide no native ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Do LLMs Make More Mistakes If They Do Not Believe the Input Data?](http://arxiv.org/abs/2609.09363v1)
  来源：arXiv | 日期：2026-09-08 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are prone to hallucinating or misinterpreting facts, which impairs their usability in retrieval-augmented generation or data-to-text systems. We analyse how faithfulness of LLMs to provided c...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [NeuroGraph: An AI Graph-Driven Neuro-Symbolic Framework for Explainable Threat Reasoning in Advanced Manufacturing](http://arxiv.org/abs/2609.00604v2)
  来源：arXiv | 日期：2026-09-01 | 相关度：6.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：The growing complexity of cyber-physical attack surfaces in advanced manufacturing has made cyber threat intelligence analysis increasingly difficult. Although large language models and retrieval-augmented generation hav...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MI-PEFT: Mixture-of-Experts Integrated Parameter-Efficient Fine-Tuning Protein Language Models Improves Acidophilic Proteins Classification](http://arxiv.org/abs/2609.08059v1)
  来源：arXiv | 日期：2026-09-07 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Acidophilic proteins that remain stable and functional under highly acidic conditions, are important for industrial biocatalysis, acid-related bioprocessing, and the discovery of acid-stable enzymes. However, their ident...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [HyLnc: a hybrid deep learning and feature-based approach for long non-coding RNA prediction.](https://pubmed.ncbi.nlm.nih.gov/42716909/)
  来源：PubMed | 日期：2026-09-09 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Long non-coding RNAs (lncRNAs) play important roles in gene regulation, development and disease, yet accurate identification of lncRNAs from transcriptomic data remains a major computational challenge. Existing methods o...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [From Retrieval to Weights: Parametric Individualization of Small Language Models with Individual Text Corpora](http://arxiv.org/abs/2609.10155v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：5.45 | 新颖度：6.77
  匹配主题：foundation_model_agent
  中文摘要：We approach a cognitive simulation perspective on episodic and semantic memory in multiple-choice question answering by incorporating text from individual text corpora (ITC) into retrieval-augmented generation and DoRA f...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ReMoMask-2: Latent Retrieval-Augmented Masked Motion Generation](http://arxiv.org/abs/2609.08365v1)
  来源：arXiv | 日期：2026-09-08 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Text-to-motion (T2M) generation maps natural language to human joint movements, aiding gaming, VR, and robotics. Retrieval-Augmented Text-to-Motion (RAG-T2M) improves generation on complex descriptions by conditioning on...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Guaranteeing Faithful Evidence Extraction in Speculative Retrieval-Augmented Generation](http://arxiv.org/abs/2609.10046v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：4.75 | 新颖度：7.16
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) are increasingly used as interfaces for information retrieval, but they remain prone to hallucinations and faithfulness errors, in which the generated answers diverge from the retrieved evide...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Evidence-Aligned Entity Verification for Hallucination Detection in Retrieval-Augmented Generation](http://arxiv.org/abs/2609.08267v1)
  来源：arXiv | 日期：2026-09-08 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Hallucination detection is crucial for large language models (LLMs), as hallucinated content creates significant barriers in applications requiring factual accuracy. Current detection methods mainly depend on internal si...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Reproducing Omitted Temporal Expressions in Japanese News for Retrieval-Augmented Applications](http://arxiv.org/abs/2609.09569v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：News articles often contain omitted temporal expressions, such as day-only or month-only mentions, which must be interpreted with reference to the publication date. When such articles are indexed or processed as standalo...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Multimodal genomic surveillance for respiratory pathogens at four U.S. international airports: A comparison of air, wastewater, clinical, and national surveillance data.](https://pubmed.ncbi.nlm.nih.gov/42715246/)
  来源：PubMed | 日期：2026-01-01 | 相关度：5.0 | 新颖度：5.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Early detection of outbreaks and emerging pathogens is critical for public health and global biosecurity. Airports, as major international travel hubs with dense, enclosed populations, are high-risk settings for disease ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [In RAG We Trust? Measuring Robustness of Retrieval-Augmented Generation Under Document Poisoning](http://arxiv.org/abs/2609.09243v1)
  来源：arXiv | 日期：2026-09-08 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) grounds a language model in retrieved documents, which reduces hallucination but creates a new attack surface: if retrieved text is tampered with, the model may repeat the falsehood. ...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [Ensembling LLMs for AI-Augmented Cybersecurity Software Requirements Generation](http://arxiv.org/abs/2609.10316v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：4.75 | 新颖度：6.83
  匹配主题：foundation_model_agent
  中文摘要：Translating high-level controls from security standards into concrete, system-specific requirements is central to cybersecurity requirements engineering. Large language models (LLMs) can accelerate this labor-intensive, ...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [UKB-KG: Knowledge Graph for Integrating and Enhancing Biomedical Insights from the UK Biobank](https://www.medrxiv.org/content/10.64898/2026.09.02.26361902v1)
  来源：medRxiv | 日期：2026-09-07 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：The UK Biobank (UKB) is a cornerstone of modern biomedical research, providing unparalleled data to advance the understanding, prediction, and treatment of diseases. Its contributions span genetics, genomics, disease pre...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A user-friendly, no-code, application for HIPAA-compliant automated analysis of tabular data at scale](https://www.medrxiv.org/content/10.64898/2026.09.06.26362377v1)
  来源：medRxiv | 日期：2026-09-08 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Background: Clinical research often requires reviewing large volumes of unstructured electronic medical record (EMR) data, a time-consuming task demanding skilled personnel. Large language models (LLMs) like ChatGPT can ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Using large language models to facilitate literature review and data extraction for infectious disease models: COVID-19 as a test case](https://www.medrxiv.org/content/10.64898/2026.09.06.26362399v1)
  来源：medRxiv | 日期：2026-09-08 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Infectious disease transmission models are governed by parameters informed by systematic review of epidemiological literature. Large language models (LLMs) could facilitate this, but the reliability of the results to inf...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic AI-enabled Semantic Commissioning of a Cognitive Digital Twin for Reconfigurable Manufacturing](http://arxiv.org/abs/2609.09503v1)
  来源：arXiv | 日期：2026-09-08 | 相关度：2.5 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Rapid bespoke commissioning of the Cognitive Digital Twin (CDT) is a major challenge in reconfigurable manufacturing. Traditional digital twin (DT) construction methods primarily focus on geometric reconstruction, often ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Central Dogma Transformer II: An AI Microscope for Understanding Cellular Regulatory Mechanisms](http://arxiv.org/abs/2602.08751v4)
  来源：arXiv | 日期：2026-02-09 | 相关度：2.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Motivation: Interpretability is not optional in biology: understanding gene regulation requires models whose learned structure can be directly interrogated, not merely accurate predictors whose internals resist mapping o...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Democratizing Agentic Access to Bioinformatics and Biopharmaceutical Databases and Analyses with BioMCP-TS](https://www.biorxiv.org/content/10.64898/2026.09.03.749120v1)
  来源：bioRxiv | 日期：2026-09-08 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Practitioners want to give AI agents direct access to biomedical databases and analyses, but today that means choosing between dependency-heavy skill packages, data-lookup-focused server tools, and closed vendor platform...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [KVShareArena: KV-Cache Reuse Across Contexts and Model Checkpoints](http://arxiv.org/abs/2609.10266v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：1.4 | 新颖度：7.5
  匹配主题：未命中具体主题
  中文摘要：LLM serving systems already reuse KV caches, but only when the reused text sits at the very start of the prompt. Two growing workloads break this condition: a retrieval-augmented generation server assembles a different s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Glyph: A Multi-Strategy Agentic System for Column Description and Sensitivity-Ontology Tagging of Enterprise Data Catalogs](http://arxiv.org/abs/2609.10430v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：1.4 | 新颖度：7.3
  匹配主题：未命中具体主题
  中文摘要：Enterprise data lakes accumulate tables faster than human stewards can document or classify them, leaving columns with missing descriptions and unassigned governance labels. This documentation debt undermines data discov...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TruthInsightBench: An Evidence-Grounded Benchmark for Automated Evaluation of Open-Ended Scientific Discovery Agents](http://arxiv.org/abs/2609.05079v2)
  来源：arXiv | 日期：2026-09-04 | 相关度：1.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：Autonomous coding agents are increasingly proposed as AI-scientist systems that conduct analyses and write research reports, but executing a prescribed analysis is not the same as making a discovery. Existing benchmarks ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DoGMA: A Central-Dogma-Guided Foundation Model for Multi-Omics Alignment and Multi-Task Learning in Oncology](http://arxiv.org/abs/2608.08148v2)
  来源：arXiv | 日期：2026-08-08 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Attention mechanisms have been widely utilized in modern deep learning, and many existing multi-omics models inherit their conventional use to allow unrestricted bidirectional interactions. However, the fundamental logic...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LiteRAG: Cost-Efficient Graph-Based Retrieval-Augmented Generation](http://arxiv.org/abs/2609.10239v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：0.7 | 新颖度：7.19
  匹配主题：未命中具体主题
  中文摘要：Graph-based retrieval can improve multi-hop question answering, but existing approaches often incur high query-time costs and produce diffuse, oversized contexts that reduce generation efficiency. We present LiteRAG, a g...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ICM-Bench: Person-Level Identity Reasoning in Multimodal Agents with Long-Term Memory](http://arxiv.org/abs/2609.04438v2)
  来源：arXiv | 日期：2026-09-03 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Long-horizon multimodal agents should remember not only what happened but also who participated. This capability depends on linking recurring faces, voices, names, person-associated objects, events, and social relations ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Muscle Memory for Agents: Compile not Merely Retrieve](http://arxiv.org/abs/2608.08995v2)
  来源：arXiv | 日期：2026-08-10 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Memory for LLM agents has converged on a single architectural pattern: store experience as text, embeddings, reflections, or rules; retrieve at inference time; let a general-purpose orchestrator interpret what to do. Thi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ReCite: Agentic Reasoning for Faithful Citation](http://arxiv.org/abs/2609.09156v1)
  来源：arXiv | 日期：2026-09-08 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Accurate citations are the foundation of academic writing, tracing intellectual origins and substantiating core claims. However, manually navigating the growing volume of scientific literature is increasingly difficult, ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [AtlasFold: Protein structure prediction with metagenomic-scale language models](https://www.biorxiv.org/content/10.64898/2026.09.04.749352v1)
  来源：bioRxiv | 日期：2026-09-07 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Protein language models (PLMs) trained on evolutionary sequences learn representations that encode protein structure, enabling direct structure prediction without multiple-sequence alignments (MSAs). Here we present the ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ProMaya: a hierarchical universal Deep Learning framework for accurate and interpretable Protein-Protein interaction identification](https://www.biorxiv.org/content/10.64898/2026.04.03.716278v2)
  来源：bioRxiv | 日期：2026-09-08 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Protein-protein interactions (PPIs) are molecular lego which define the physical states of cells. Accurately identifying PPIs remains challenging due to the interplay of several factors ranging from electrostatic to mole...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Fine-Tuning a KV Cache Concatenation-Aware Model or Recomputing KV Caches? Why Not Both?](http://arxiv.org/abs/2609.09768v1)
  来源：arXiv | 日期：2026-09-09 | 相关度：1.4 | 新颖度：6.05
  匹配主题：未命中具体主题
  中文摘要：In Retrieval-Augmented Generation (RAG) systems, a large number of retrieved chunks are concatenated to form the input context so that users can receive high-quality responses based on external knowledge. As a result, th...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Better Together: Complementary Query Rewriting Under a Strong RAG Baseline](http://arxiv.org/abs/2609.05637v2)
  来源：arXiv | 日期：2026-09-04 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：A popular way to improve Retrieval-Augmented Generation (RAG) is to rewrite the user's question into several variants and search with all of them. We test whether this actually helps once the underlying search is already...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CLAIR-Fin: An Adversarial Multi-Agent Framework for Claim-Level Verification and Adaptive Debate in Cross-Modal Financial QA](http://arxiv.org/abs/2608.13706v3)
  来源：arXiv | 日期：2026-08-13 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Existing defenses against hallucination in retrieval-augmented and multi-agent pipelines remain partial: evidence is trusted despite modality disagreement, debate verifies an aggregate report rather than individual claim...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Evidence-Grounded Retrieval for Investigation Hunt Lead Generation from CTI Reports](http://arxiv.org/abs/2609.08790v1)
  来源：arXiv | 日期：2026-09-08 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Threat hunting increasingly depends on converting unstructured knowledge (e.g., Cyber Threat Intelligence reports) into actionable hunt leads: concise, investigable hypotheses grounded in observable artifacts and adversa...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [PDMR: Passage-Driven Multi-ID Document Retrieval](http://arxiv.org/abs/2609.08762v1)
  来源：arXiv | 日期：2026-09-08 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Generative Retrieval (GR) models map queries directly to document identifiers, replacing conventional retrieval over external sparse or dense indexes with autoregressive identifier generation. However, most generative re...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Reasoning Before Disposition: A Model-Agnostic Cannot-Miss Discipline for Quiet Emergencies and the Case for Deterministic Enforcement](https://www.medrxiv.org/content/10.64898/2026.09.02.26362074v1)
  来源：medRxiv | 日期：2026-09-08 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models now match clinicians on medical-knowledge benchmarks. Whether they can safely triage a patient message is a separate question, and the highest-consequence failure in triage is the emergency that nev...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Machine learning-enabled wastewater-based surveillance for emerging pathogen detection and monitoring: current applications, challenges, and future prospects.](https://pubmed.ncbi.nlm.nih.gov/42704107/)
  来源：PubMed | 日期：2026-09-07 | 相关度：5.0 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Abstract Wastewater-based surveillance (WBS) has become an important public-health tool for tracking community-level circulation of emerging and re-emerging pathogens, but wastewater measurements are not directly interpr...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
