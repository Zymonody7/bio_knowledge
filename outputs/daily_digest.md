# 每日论文监控日报 (2026-07-07)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 37 篇新论文。

## 抓取状态

- arXiv：成功，命中 34 篇
- PubMed：成功，命中 46 篇
- bioRxiv：成功，命中 13 篇
- medRxiv：成功，命中 6 篇

## 最值得看

### Foundation Model / Agent

- [Toward Trustworthy Large Language Model Agents in Healthcare](http://arxiv.org/abs/2607.05055v1)
  来源：arXiv | 日期：2026-07-06 | 相关度：6.55 | 新颖度：7.91
  匹配主题：foundation_model_agent
  中文摘要：Healthcare appointment scheduling remains a persistent operational bottleneck, driven by manual coordination, fragmented legacy systems, and high administrative overhead. These inefficiencies constrain provider availabil...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [LLMs for Agentic Home Energy Management](http://arxiv.org/abs/2607.04569v1)
  来源：arXiv | 日期：2026-07-06 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Home Energy Management Systems (HEMS) can reduce residential electricity costs and support demand response, but adoption is limited by the difficulty of translating household preferences into technical scheduling constra...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Biological Motifs for Agentic Control](http://arxiv.org/abs/2607.04240v1)
  来源：arXiv | 日期：2026-07-05 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：The transition of Large Language Models (LLMs) from passive generators to autonomous agents has introduced significant challenges in reliability, security, and state management. Current agentic architectures are often co...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CausalGame: Benchmarking Causal Thinking of LLM Agents in Games](http://arxiv.org/abs/2607.04293v1)
  来源：arXiv | 日期：2026-07-05 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Building AI Scientist agents with Large Language Models (LLMs) has recently attracted growing attention. Since scientific discovery fundamentally relies on uncovering causal relationships from observations, the capabilit...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [When Simpler Is Better: Evaluating Translation Pipelines for Medieval Latin Manuscripts](http://arxiv.org/abs/2607.03836v1)
  来源：arXiv | 日期：2026-07-04 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Despite remarkable progress in machine translation, Vision Language Models (VLMs) struggle on historical manuscripts, a domain that stresses core Natural Language Processing (NLP) capabilities: low-resource transliterati...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [BindRNAgen: Protein-binding RNA sequence generation using latent diffusion models.](https://pubmed.ncbi.nlm.nih.gov/42409279/)
  来源：PubMed | 日期：2026-07-06 | 相关度：5.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：RNA-binding proteins (RBPs) are pivotal regulators of gene expression, and their dysregulation is implicated in a wide range of human diseases. Designing synthetic RNA molecules to modulate RBP activity represents a prom...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AI-guided CRISPR screening reveals therapeutic targets in psoriasis.](https://pubmed.ncbi.nlm.nih.gov/42409798/)
  来源：PubMed | 日期：2026-07-06 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Psoriasis affects over 125 million people globally. Biologics targeting the IL-17/IL-17RA axis are effective but require systemic administration, are costly, and are unsuitable for some patients. Developing topical small...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MLS-Bench: A Holistic and Rigorous Assessment of AI Systems on Building Better AI](http://arxiv.org/abs/2605.08678v3)
  来源：arXiv | 日期：2026-05-09 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Modern AI progress has been driven by ML methods that are generalizable across settings and scalable to larger regimes. As large language models demonstrate advanced capabilities in reasoning, coding, and engineering tas...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Clinical Impact, Diagnostic Performance, and Prognostic Implications of Plasma Metagenomic Next-Generation Sequencing in Solid Organ Transplant Recipients](https://www.medrxiv.org/content/10.64898/2026.07.02.26357172v1)
  来源：medRxiv | 日期：2026-07-06 | 相关度：7.4 | 新颖度：5.5
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Introduction: Plasma metagenomic next-generation sequencing (mNGS) may detect pathogens in solid organ transplant (SOT) recipients, but optimal patient selection and result interpretation remain uncertain. Methods: Physi...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Medi-Gemma: A Hybrid Clinical Decision Support System Integrating Deterministic EMR Analytics and Retrieval-Augmented Generation](http://arxiv.org/abs/2607.04907v1)
  来源：arXiv | 日期：2026-07-06 | 相关度：6.45 | 新颖度：6.43
  匹配主题：foundation_model_agent
  中文摘要：Deploying Large Language Models (LLMs) in high-stakes clinical settings remains limited by structural hallucinations, weak deterministic reasoning over tabular patient data, and omissions in vector retrieval. This paper ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Triple-Phase Multimodal Knowledge Aggregation Framework for Microbial Keratitis Subtype Diagnosis on Slit-Lamp Photography](http://arxiv.org/abs/2607.03740v1)
  来源：arXiv | 日期：2026-07-04 | 相关度：6.4 | 新颖度：6.0
  匹配主题：sequencing_bioinformatics, foundation_model_agent, application_monitoring
  中文摘要：Microbial keratitis requires rapid pathogen identification to guide treatment, but culture- and PCR-based diagnostics are slow and resource-intensive. We developed a triple-phase multimodal framework for bacterial-versus...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Detecting Hallucinations in Retrieval-Augmented Generation through Grounding-Aware Sensitivity by Perturbation (GASP)](http://arxiv.org/abs/2607.04223v1)
  来源：arXiv | 日期：2026-07-05 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) reduces but does not eliminate hallucination, and existing detectors return a single answer-level score that does not indicate which sentence is unsupported, or why. To close this gap...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [TogoMCP: Natural Language Querying of Life-Science Knowledge Graphs via Schema-Guided LLMs and the Model Context Protocol](https://www.biorxiv.org/content/10.64898/2026.03.19.713030v3)
  来源：bioRxiv | 日期：2026-07-06 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Querying the RDF Portal knowledge graph maintained by DBCLS, which aggregates approximately 60 life-science databases, requires proficiency in both SPARQL and database-specific RDF schemas, placing this resource beyond t...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [GestaltMML: Enhancing Rare Genetic Disease Diagnosis through Multimodal Machine Learning Combining Facial Images and Clinical Text](http://arxiv.org/abs/2312.15320v3)
  来源：arXiv | 日期：2023-12-23 | 相关度：3.75 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Individuals with suspected rare genetic disorders often undergo multiple clinical evaluations, imaging studies, laboratory tests, and genetic tests over a prolonged period of time, a process commonly described as the dia...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multimodal temporal mapping of macrophage transcriptome remodeling during Salmonella infection](https://www.biorxiv.org/content/10.64898/2026.07.04.736507v1)
  来源：bioRxiv | 日期：2026-07-06 | 相关度：3.05 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Macrophages are equipped to eliminate invading pathogens, yet several intracellular bacteria exploit them as replicative niches. Salmonella enterica serovar Typhimurium subverts host immunity by injecting effector protei...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [FLOWR.ROOT - A flow matching-based foundation model for joint multi-purpose structure-aware 3D ligand generation and affinity prediction.](https://pubmed.ncbi.nlm.nih.gov/42409794/)
  来源：PubMed | 日期：2026-07-06 | 相关度：2.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：We present FLOWR.ROOT, an SE(3)-equivariant flow-matching foundation model that unifies pocket-aware 3D ligand generation with multi-endpoint binding affinity prediction (pIC 50 , pK i , pK d , pEC 50 ) and pLDDT-based c...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Rethinking Scientific Discovery in an Agentic Era](http://arxiv.org/abs/2607.03863v1)
  来源：arXiv | 日期：2026-07-04 | 相关度：2.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Artificial intelligence has advanced scientific discovery, but most AI4Science systems remain fragmented tools that rely on humans to coordinate problem formulation, literature grounding, model use, simulation, validatio...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ContextNest: Verifiable Context Governance for Autonomous AI Agent](http://arxiv.org/abs/2607.02116v2)
  来源：arXiv | 日期：2026-07-02 | 相关度：2.1 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Autonomous AI agents increasingly depend on external knowledge stores, yet most retrieval pipelines provide relevance without durable guarantees of provenance, version identity, integrity, traceability, or point-in-time ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Memory-Orchestrated Semantic System (MOSS): An Auditable Agentic Memory Architecture](http://arxiv.org/abs/2607.04391v1)
  来源：arXiv | 日期：2026-07-05 | 相关度：2.1 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Long-term memory remains a structural weakness of AI agents. The dominant approach, retrieval-augmented generation (RAG), relies on embedding-based similarity search, which is opaque by construction, difficult to audit, ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic Retrieval-Augmented Generation for Financial Document Question Answering](http://arxiv.org/abs/2605.05409v2)
  来源：arXiv | 日期：2026-05-06 | 相关度：1.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：Financial document question answering (QA) demands complex multi-step numerical reasoning over heterogeneous evidence--structured tables, textual narratives, and footnotes--scattered across corporate filings. Existing re...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MAM-AI: An On-Device Medical Retrieval-Augmented Generation System for Nurses and Midwives in Zanzibar](http://arxiv.org/abs/2606.29580v3)
  来源：arXiv | 日期：2026-06-28 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Maternal and newborn mortality remain among the highest in sub-Saharan Africa, where midwifery care is often delivered by nurses who lack midwifery training to international standards, and consulting authoritative guidan...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Risk-Constrained Freshness-Aware Semantic Caching for Open-Web Retrieval-Augmented LLMs](http://arxiv.org/abs/2607.04281v1)
  来源：arXiv | 日期：2026-07-05 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Semantic caching reduces the latency and cost of retrieval-augmented generation (RAG) by serving cached answers to semantically similar queries, but most existing methods do not model the time-varying freshness of open-w...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Diagnosing and Mitigating Compounding Failures in Agentic Persuasion via Taxonomic Strategy Retrieval](http://arxiv.org/abs/2606.24976v3)
  来源：arXiv | 日期：2026-06-23 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Foundation-model agents in multi-step, open-ended environments frequently suffer from compounding errors, where early mistakes contaminate long-horizon trajectories. While Multi-Agent Debate (MAD) succeeds in determinist...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Candidate-Constrained Retrieval-Augmented Generation for LongEval-RAG: System Design and Empirical Analysis](http://arxiv.org/abs/2607.04008v1)
  来源：arXiv | 日期：2026-07-04 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：We present a candidate-constrained retrieval-augmented generation system for LongEval-RAG, where each query is associated with an organizer-provided candidate set and all retrieved evidence and final citations must remai...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Knowledge Base Poisoning Attacks and Defense for Policy-Aware LLM-RAG Framework](http://arxiv.org/abs/2607.04379v1)
  来源：arXiv | 日期：2026-07-05 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：This paper presents an adversarial security study of the Policy-Aware LLM Retrieval-Augmented Generation (PA-LLM-RAG) framework for Internet of Battlefield Things (IoBT) mission control. We propose Query-Agnostic Semanti...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Estimating Individual Tree Height and Species from UAV Imagery](http://arxiv.org/abs/2603.23669v2)
  来源：arXiv | 日期：2026-03-24 | 相关度：0.7 | 新颖度：6.75
  匹配主题：未命中具体主题
  中文摘要：Accurate estimation of forest biomass, a major carbon sink, relies heavily on tree-level traits such as height and species. Unoccupied Aerial Vehicles (UAVs) capturing high-resolution imagery from a single RGB camera off...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Compressing the Validation Bottleneck: An Agentic Self-Driving Lab for Scientific Discovery](http://arxiv.org/abs/2607.04508v1)
  来源：arXiv | 日期：2026-07-05 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Agentic AI-for-Science can automate ideation, planning, and analysis, but final validation still depends on real experiments. A self-driving lab (SDL) can execute those experiments, yet the loop still has bottlenecks: th...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [mamabench and mamaretrieval: Benchmarks for Evaluating Medical Retrieval-Augmented Generation in Maternal, Neonatal, and Reproductive Health](http://arxiv.org/abs/2606.29467v3)
  来源：arXiv | 日期：2026-06-28 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Medical question-answering benchmarks rarely cover the maternal, neonatal, child, and reproductive-health questions a nurse-midwife asks, and, to our knowledge, no public chunk-level relevance benchmark exists for matern...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Search Beyond What Can Be Taught: Evolving the Knowledge Boundary in Agentic Visual Generation](http://arxiv.org/abs/2607.05382v1)
  来源：arXiv | 日期：2026-07-06 | 相关度：0.7 | 新颖度：8.4
  匹配主题：未命中具体主题
  中文摘要：Visual generators excel at rendering, but they confidently fabricate what they do not know. User requests are unbounded, evolving, and deeply long-tailed: new characters, trending entities, post-cutoff events, and more. ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Hybrid privacy-aware semantic search: SVD-truncated document geometry and CKKS-encrypted query reranking under a restricted threat model](http://arxiv.org/abs/2606.26373v3)
  来源：arXiv | 日期：2026-06-24 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Dense embeddings power semantic search and Retrieval-Augmented Generation, yet a leaked vector database leaks the text behind it, since embeddings invert with high fidelity. The textbook defences are extreme--homomorphic...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Identification of race-specific QTL and candidate genes for Aphanomyces root rot resistance in alfalfa (Medicago sativa L.).](https://pubmed.ncbi.nlm.nih.gov/42132231/)
  来源：PubMed | 日期：2026-07-06 | 相关度：6.75 | 新颖度：0.25
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：Aphanomyces root rot (ARR), caused by the oomycete Aphanomyces euteiches, is one of the most devastating diseases of alfalfa in the United States. Two pathogenic races of A. euteiches have been identified, with most comm...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A Unified Molecular Graph and Protein Language Model Framework for Predicting Human Drug-Hormone Receptor Interactions with Structure-Aware Validation.](https://pubmed.ncbi.nlm.nih.gov/42402023/)
  来源：PubMed | 日期：2026-07-05 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Hormones regulate many essential biological processes by interacting with specific receptors that control gene expression, metabolism, growth, and immune function. Because numerous therapeutic compounds can influence or ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Hierarchical Evidence-Driven Reasoning for Long Document Understanding](http://arxiv.org/abs/2607.04625v1)
  来源：arXiv | 日期：2026-07-06 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) streamlines long-document understanding by leveraging retrieval mechanisms to restrict input images to a highly curated subset. However, existing multimodal RAG pipelines primarily fa...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers?](http://arxiv.org/abs/2606.24530v2)
  来源：arXiv | 日期：2026-06-23 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：We introduce NatureBench, a cross-discipline benchmark of 90 tasks distilled from peer-reviewed Nature-family publications, designed to evaluate whether AI coding agents can move beyond reproduction toward discovery on r...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Beyond Item Order: Temporal Gap Tokenization for Generative Recommendation with Semantic IDs](http://arxiv.org/abs/2607.03918v1)
  来源：arXiv | 日期：2026-07-04 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Semantic-ID-based generative recommendation has recently emerged as a scalable paradigm for sequential recommendation, where each item is represented by a compact sequence of discrete codes and next-item prediction is fo...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Exploiting Structural Properties for Efficient Constraint-Aware HNSW Hyperparameter Tuning](http://arxiv.org/abs/2607.04630v1)
  来源：arXiv | 日期：2026-07-06 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Vector databases (VectorDBs) are a core component of modern retrieval systems, including Retrieval-Augmented Generation (RAG), where efficient Approximate Nearest Neighbor Search (ANNS) is critical. Among ANNS algorithms...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 其他

- [MIRAGE: Defending Long-Form RAG Against Misinformation Pollution](http://arxiv.org/abs/2607.05069v1)
  来源：arXiv | 日期：2026-07-06 | 相关度：0.7 | 新颖度：7.68
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) improves factuality by grounding LLMs in external evidence, but real-world retrieval is often polluted: semantically relevant passages may contain subtle misinformation, misleading fr...
  为什么值得看：MIRAGE: Defending Long-Form RAG Against  与你的主题有弱匹配，暂时保留作低优先级跟踪。
