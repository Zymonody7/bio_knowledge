# 每日论文监控日报 (2026-11-14)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 45 篇新论文。

## 抓取状态

- arXiv：成功，命中 34 篇
- PubMed：成功，命中 45 篇
- bioRxiv：成功，命中 19 篇
- medRxiv：成功，命中 11 篇

## 最值得看

### Foundation Model / Agent

- [LUNA-FM: a subword foundation model for long non-coding RNAs for functional inference.](https://pubmed.ncbi.nlm.nih.gov/43023405/)
  来源：PubMed | 日期：2026-11-13 | 相关度：7.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：RNA foundation models (FMs) have shown promise for RNA identification and functional annotation. However, many use single-nucleotide tokenization, which produces long input sequences and can increase computational costs ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [LLM Representations Rival Traditional Predictors and Enhance Multimodal Prediction of APOE4 and Aβ-Burden](https://www.medrxiv.org/content/10.64898/2026.11.09.26367620v2)
  来源：medRxiv | 日期：2026-11-12 | 相关度：7.8 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Spontaneous language offers a scalable, noninvasive approach for identifying biological indicators of preclinical Alzheimer's disease (AD). We examined prediction of APOE4 carrier status and cerebral amyloid-beta burden ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Automating postmarketing pharmacovigilance with large language model agents](https://www.medrxiv.org/content/10.64898/2026.11.10.26367711v1)
  来源：medRxiv | 日期：2026-11-12 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Postmarketing pharmacovigilance relies on spontaneous adverse event reporting and labor-intensive observational studies, which suffer from underreporting and delayed risk detection. Large language model (LLM) agents coul...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DrSai: an agentic AI system toward autonomous physics analysis workflows at BESIII](http://arxiv.org/abs/2604.22541v2)
  来源：arXiv | 日期：2026-04-24 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：High Energy Physics (HEP) experiments like BESIII produce petabyte-scale data. Extracting physics results requires complex workflows (simulation, reconstruction, statistical analysis, etc.) that traditionally take expert...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [NIBench: benchmarking autonomous AI agents for execution, skill evolution and scientific judgment in neuroimaging](http://arxiv.org/abs/2611.15831v1)
  来源：arXiv | 日期：2026-11-11 | 相关度：6.8 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Autonomous AI agents are increasingly used to automate biomedical research, creating a growing need to benchmark their capabilities on real scientific data and workflows. Their reliability in neuroimaging remains insuffi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DrugCoding: A Scientific Programming Agent for Drug Discovery](http://arxiv.org/abs/2611.13651v2)
  来源：arXiv | 日期：2026-11-10 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Drug discovery involves multiple interconnected research stages, including molecular design, property prediction, and virtual screening. These processes are characterized by complex workflows, interdependent computationa...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MENTOR: An Evidence-Informed Large Language Model-Based Multi-Agent System for Efficient Selection of Institution-Specific Negative Control Outcomes](https://www.medrxiv.org/content/10.64898/2026.11.10.26367768v1)
  来源：medRxiv | 日期：2026-11-12 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Objective Negative control outcomes (NCOs) help detect and correct systematic error in observational studies, yet their selection remains largely manual. The Common Evidence Model (CEM) can generate candidate lists, but ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond Sequence and Structure: Pretraining PLMs on Continuous Biophysical Fields](https://www.biorxiv.org/content/10.64898/2026.11.09.765464v1)
  来源：bioRxiv | 日期：2026-11-11 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：We introduce the Biophysical Transformer, a protein language model that adds continuous biophysical fields as a third pretraining signal beside sequence and structure. A Poisson-Boltzmann solver computes the electrostati...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DE-Rigor-Agent: An Agentic Workflow for Assumption-Aware Differential Expression Analysis of Bulk RNA-seq Data](https://www.biorxiv.org/content/10.64898/2026.11.09.765522v1)
  来源：bioRxiv | 日期：2026-11-11 | 相关度：6.15 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Differential expression (DE) methods for bulk RNA-seq differ in their statistical assumptions, input data requirements, and supported study designs. Large language model (LLM) agents can automate DE analysis, but they ma...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Enrollees and Early Lessons from an Agentic Healthcare Platform with Physicians in the Loop](https://www.medrxiv.org/content/10.64898/2026.11.12.26367291v1)
  来源：medRxiv | 日期：2026-11-13 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Agentic healthcare platforms that combine large language models with physician oversight are growing quickly, but little is known about who uses them. We characterized 3,223 enrollees of Lotus AI, a free, physician-super...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [BenchmarkHub: an open-source platform for reproducible evaluation of large language models in healthcare](https://www.medrxiv.org/content/10.64898/2026.11.11.26367866v1)
  来源：medRxiv | 日期：2026-11-13 | 相关度：6.1 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Background: Large language models (LLMs) are solely judged by their scores on biomedical benchmarks, yet these scores are rarely reproducible since the prompts, inference settings and model builds are seldom reported. We...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [AI-Driven Reconstruction of Online Health Narratives Using Agent-Action-Outcome Modeling: Algorithm Development and Validation.](https://pubmed.ncbi.nlm.nih.gov/43024829/)
  来源：PubMed | 日期：2026-11-13 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：People share health experiences online as stories, not isolated facts. Most computational systems reduce these narratives to keywords or claims, overlooking the agency, causality, and interpretation that determine whethe...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [The Confessions of a Protein Language Model: Steering, Activations, and What Predicted Confidence Cannot Certify](https://www.biorxiv.org/content/10.64898/2026.11.10.765136v1)
  来源：bioRxiv | 日期：2026-11-11 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Protein generate-and-screen pipelines use interventions and readouts to select candidates, but rarely test whether these track their intended targets. We audit published repetition steering, ESMFold confidence, and an ac...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Coarse-tuning to improve a protein foundation model for a domain of proteins: the example of outer membrane beta barrels](https://www.biorxiv.org/content/10.64898/2026.11.09.765412v1)
  来源：bioRxiv | 日期：2026-11-12 | 相关度：3.95 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Foundation models for proteins have shown great potential in addressing a wide range of challenges in computational molecular biology. State-of-the-art models are trained on large and diverse corpora of protein sequences...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Toward precision nanomedicine via artificial intelligence guided design and prediction.](https://pubmed.ncbi.nlm.nih.gov/43025814/)
  来源：PubMed | 日期：2026-11-13 | 相关度：3.75 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence (AI) is advancing nanomedicine development by linking formulation variables and biological context with delivery, therapeutic efficacy, and safety. This review examines AI assisted formulation des...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [VArify: A Visual Analytics System for Verifying Knowledge Enhanced Large Language Model Responses in Food Science](http://arxiv.org/abs/2606.10177v2)
  来源：arXiv | 日期：2026-06-08 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Graph Retrieval-Augmented Generation (GraphRAG) grounds Large Language Model (LLM) responses in structured, domain-specific knowledge. However, verification remains difficult because errors can arise at multiple layers: ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CauProphet: Teaching Agents to Develop Causal Cognition like Humans](http://arxiv.org/abs/2610.32477v3)
  来源：arXiv | 日期：2026-10-23 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large language model (LLM) agents increasingly support long-horizon tasks by leveraging external memory and past experience. However, existing agents mainly retrieve records or summaries, lacking the ability to form and ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DeePEn - A Depth sensitive benchmark for Protein Engineering](https://www.biorxiv.org/content/10.64898/2026.06.09.731073v2)
  来源：bioRxiv | 日期：2026-11-12 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Recent progress in modeling techniques and high-throughput screening has significantly enhanced the accessibility of protein engineering. Nevertheless, further progress gets hindered by the lack of robust benchmarks that...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Benchmark Self-Triage (BeST): Comparing Self-Triage Systems and Multiple Generations of OpenAI Models Against Preliminary Expert Consensus](https://www.medrxiv.org/content/10.64898/2026.10.12.26365287v2)
  来源：medRxiv | 日期：2026-11-12 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：As digital self-triage becomes more widely used, quality assurance requires evaluation of both emergency recognition and overall agreement with clinical judgement, including how these outcomes differ across generations o...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OpticalRAG: Pixel-Space Compression for Token-Efficient Retrieval-Augmented Generation](http://arxiv.org/abs/2611.13675v2)
  来源：arXiv | 日期：2026-11-10 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) is bottlenecked by the token budget of large language models: feeding long documents into the context window is expensive, while aggressive textual compression discards fine-grained i...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [An auditable harness for biomolecular dynamics simulations by AI agents](https://www.biorxiv.org/content/10.64898/2026.11.09.765490v1)
  来源：bioRxiv | 日期：2026-11-11 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：AI agents now generate biological hypotheses faster than they can be tested. Hypotheses stated at the atomic level can be examined with molecular dynamics (MD) simulations. For new questions without a reference, trust in...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CRINN: Contrastive Reinforcement Learning for Approximate Nearest Neighbor Search](http://arxiv.org/abs/2508.02091v5)
  来源：arXiv | 日期：2025-08-04 | 相关度：2.1 | 新颖度：1.75
  匹配主题：未命中具体主题
  中文摘要：Approximate nearest-neighbor search (ANNS) algorithms have become increasingly critical for recent AI applications, particularly in retrieval-augmented generation (RAG) and agent-based LLM applications. In this paper, we...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Food Critic: An Agentic Visualization System for Auditable Restaurant-Safety Reasoning](http://arxiv.org/abs/2611.15843v1)
  来源：arXiv | 日期：2026-11-11 | 相关度：2.1 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Generative AI agents are increasingly being embedded into visualization systems that can search data, invoke tools, summarize evidence, and produce recommendations. However, when agents rely solely on their own knowledge...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Toward Agentic Retrieval-Augmented Generation for Enterprise Retail Workflows over Heterogeneous Data Sources](http://arxiv.org/abs/2610.25096v2)
  来源：arXiv | 日期：2026-10-18 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Enterprise retail workflows require agents to chain evidence across heterogeneous sources, from structured product and order records to unstructured inquiries and reviews, yet existing agentic RAG benchmarks rarely captu...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DISCERN: Preserve at Write, Resolve at Read for Persistent LLM-Agent Memory](http://arxiv.org/abs/2611.15729v1)
  来源：arXiv | 日期：2026-11-11 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Enterprise agents accumulate memory across dozens of sessions in which facts contradict, get superseded, and blur as similarly named entities collide in embedding space. The field treats this as a retrieval problem; we s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CURATOR: Scalable Fine-grained Evidence Selection for Retrieval-Augmented Generation using Decision Models](http://arxiv.org/abs/2611.16366v1)
  来源：arXiv | 日期：2026-11-12 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) provides entire retrieved passages to the LLM, even though only a handful of spans within them contain the evidence pertaining to the question. While precise selection of these spans ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TabOmics: A Small, Open Tabular Foundation Model for Wide Omics Data](http://arxiv.org/abs/2611.15329v1)
  来源：arXiv | 日期：2026-11-11 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Omics studies often produce tables with thousands to tens of thousands of molecular features and few samples. Tabular foundation models use diverse strategies to predict labels for such tables, with some relying on in-co...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AstroMemBench: A Benchmark for Memory Systems in Embodied Spacecraft Agents](http://arxiv.org/abs/2611.16590v1)
  来源：arXiv | 日期：2026-11-12 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Long-term spacecraft autonomy requires embodied agents to use operational history under communication delays, time-critical operations, environmental uncertainty, complex physical interactions, power and computational co...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AutoOntic: Automatic Ontology Induction from Text for Knowledge Graph Construction](http://arxiv.org/abs/2611.15467v1)
  来源：arXiv | 日期：2026-11-11 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Graph-based retrieval-augmented generation depends on the quality of the knowledge graph (KG) it retrieves over, yet schema-free LLM-based extraction pipelines typically produce flat graphs: deduplicated entities and rel...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RMIT-ADM+S at TREC RAG 2026: Research Agents, Retriever Ablations, and Open-Weight Replication](http://arxiv.org/abs/2611.16425v1)
  来源：arXiv | 日期：2026-11-12 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：We describe the RMIT-ADM+S team's participation in the TREC 2026 Retrieval-Augmented Generation (RAG) track using the ClimbMix corpus. We submitted seven research-agent runs using proprietary OpenAI and open-weight model...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [RNA Small-Molecule Binding-Site Prediction by Integrating RNA Language Models and Structural Geometry](https://www.biorxiv.org/content/10.64898/2026.11.10.765632v1)
  来源：bioRxiv | 日期：2026-11-11 | 相关度：4.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：RNAs are emerging as promising therapeutic targets, and small-molecule binding can modulate their structure and function, creating opportunities for therapeutic development. Accurate identification of RNA small-molecule ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Efficient VLA Inference via Retrieval-Based Speculation and Hardware Acceleration](http://arxiv.org/abs/2611.11098v2)
  来源：arXiv | 日期：2026-11-08 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Vision-language-action (VLA) models enable robots to understand and execute complex instructions, but their autoregressive (AR) action generation introduces significant latency on resource-constrained robotic platforms. ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Assessing the Capacity of Genomic Language Models to Generate Informative Embeddings of Viral Genome Fragments](https://www.biorxiv.org/content/10.64898/2026.11.09.765411v1)
  来源：bioRxiv | 日期：2026-11-11 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Genomic language models (gLMs) trained on large volumes of nucleotide sequences are becoming an alternative to classical methods in metagenomic analysis, particularly for studying genomic "dark matter". In this work, we ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Privilege and confidentiality in generative AI workflows](http://arxiv.org/abs/2607.05479v2)
  来源：arXiv | 日期：2026-07-06 | 相关度：2.1 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Generative AI (GenAI) systems store and process client data in three distinct ways: in the model's parameters through training and memorisation, in the context window during a live session, and in knowledge databases for...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Pointing the Way, Hiding the Destination: Practical Private Dense Retrieval at Scale](http://arxiv.org/abs/2608.25735v3)
  来源：arXiv | 日期：2026-08-26 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Hosted retrieval-augmented generation (RAG) and semantic search allow users to query valuable provider-held corpora, raising two competing demands: to hide each query and chosen result, yet reveal only the documents that...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [AI for Biologists: The Knowledge Boundaries of Foundation Models in the Age of Agentic Systems](http://arxiv.org/abs/2611.17015v1)
  来源：arXiv | 日期：2026-11-12 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence (AI) is changing how biological research is done. Biological foundation models trained on millions of nucleotides, protein, and single-cell measurements predict protein structures, mutation effect...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Protein Language Models Fail To Capture Contact Predictions Under Invariant Relabeling](http://arxiv.org/abs/2611.16881v1)
  来源：arXiv | 日期：2026-11-12 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Protein language models (pLMs) produce highly accurate contact maps from single-sequence inputs. People often take this accuracy as proof that these models implicitly learn invariant coevolutionary statistics, extracting...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Faithful in Steps: Improving Generalization and Citation in RAG via Query Decomposition](http://arxiv.org/abs/2611.15538v1)
  来源：arXiv | 日期：2026-11-11 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augment generation is a prevalent strategy to mitigate hallucinations of LLMs. The attributable RAG (RAGQ) generates quotes for its answers. The quotes indicate which input contexts support the RAG to derive th...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Automatic Knowledge Graph Construction and Query for Earthquake Catalogs](http://arxiv.org/abs/2607.24984v2)
  来源：arXiv | 日期：2026-07-27 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：In recent years, the number of events in earthquake catalogs has significantly increased due to the utilization of more effective deep learning based detectors and phase pickers but answering open ended questions such as...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [The Therapeutic Pipeline: Future Treatments and Precision Medicine.](https://pubmed.ncbi.nlm.nih.gov/43025460/)
  来源：PubMed | 日期：2026-11-13 | 相关度：3.7 | 新颖度：5.25
  匹配主题：pathogenomics
  中文摘要：rare interstitial lung diseases (ILDs) represent a heterogeneous group of disorders characterized by various pathogenic mechanisms, clinical presentations, prognoses, and therapeutic challenges. Among these, acid sphingo...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Deep Learning-Enabled Magnetic Bead-Capture Fluorescence In Situ Hybridization Enables Multiplex Identification and Digital Counting of Pathogenic Bacteria.](https://pubmed.ncbi.nlm.nih.gov/43014755/)
  来源：PubMed | 日期：2026-11-11 | 相关度：3.2 | 新颖度：0.25
  匹配主题：application_monitoring
  中文摘要：Urinary tract infections (UTIs) are among the most prevalent infectious diseases worldwide. For complicated and antimicrobial-resistant cases, timely diagnosis is critical for guiding targeted therapy and improving patie...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [PDO Drug Screening Data for Evaluating and Training AI Drug Response Prediction Models](http://arxiv.org/abs/2611.15769v1)
  来源：arXiv | 日期：2026-11-11 | 相关度：2.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Anti-cancer drug response prediction (DRP) is critically important for precision oncology and therapeutic development. Currently, most DRP models are developed using drug screening data from immortalized cancer cell line...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Multimodal single-cell analyses reveal distinct fusion-regulated transcriptional programs in Ewing sarcoma.](https://pubmed.ncbi.nlm.nih.gov/43012345/)
  来源：PubMed | 日期：2026-11-11 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Ewing sarcoma (EwS) is a fusion-driven malignancy, peaking in adolescence. Although EwS tumors are driven uniquely by EWS::FLI1 and related fusions, patient outcomes vary greatly. If and how tumor plasticity of EWS::FLI1...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Precision Neurology in Alzheimer's Disease: Genomics to Drug Optimization for Effective Therapeutic Intervention.](https://pubmed.ncbi.nlm.nih.gov/43018845/)
  来源：PubMed | 日期：2026-11-12 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Alzheimer's disease (AD) exhibits high clinical and biological heterogeneity, which complicates the development of one-size-fits-all therapeutic strategies. Standard trial designs can mask subgroup-specific effects, high...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [NEVEN: An Open-Source Polyglot Infrastructure Bridging Statistical Computing and Spreadsheet Workflows for Reproducible Research](http://arxiv.org/abs/2611.15676v1)
  来源：arXiv | 日期：2026-11-11 | 相关度：2.05 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：We present NEVEN, an open-source infrastructure that embeds R, Julia, Python, Quarto, and JavaScript visualization libraries into Excel through native worksheet formulas. Users run econometric estimators, solve different...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。
