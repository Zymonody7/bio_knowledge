# 每日论文监控日报 (2026-07-05)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 32 篇新论文。

## 抓取状态

- arXiv：成功，命中 24 篇
- PubMed：成功，命中 45 篇
- bioRxiv：成功，命中 15 篇
- medRxiv：成功，命中 5 篇

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [MMIR-TCM: Memory-Integrated Multimodal Inference and Retrieval for TCM Clinical Decision Support](http://arxiv.org/abs/2607.01814v1)
  来源：arXiv | 日期：2026-07-02 | 相关度：8.9 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Traditional Chinese Medicine (TCM) diagnosis, particularly through tongue inspection, faces persistent challenges in subjectivity and reproducibility. The application of multimodal artificial intelligence to TCM clinical...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RD-OMICS: An Integrative Multi-Omics Data Inventory in Rare Diseases](https://www.biorxiv.org/content/10.64898/2026.06.29.735296v1)
  来源：bioRxiv | 日期：2026-07-03 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Rare diseases (RD) impact over 30 million individuals in the United States, yet fewer than 5% of the identified conditions have FDA-approved treatments. Progress in RD research is hindered by small patient cohorts, biolo...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BLAgent: Agentic RAG for File-Level Bug Localization](http://arxiv.org/abs/2605.17965v2)
  来源：arXiv | 日期：2026-05-18 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Bug localization remains a key bottleneck for large language model (LLM)-based software maintenance, where accurately identifying faulty code is essential for debugging, root cause analysis, triage, and automated program...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Rethinking peptide developability with sequence-only models: interpretable screening of microplastic-binding peptides with gated query pooling.](https://pubmed.ncbi.nlm.nih.gov/42232867/)
  来源：PubMed | 日期：2026-07-02 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Designing peptides for microplastic targeting is intrinsically multi-objective: sequence motifs that promote adsorption to hydrophobic polymers frequently elevate developability risks, including hemolysis, non-specific a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [TumorCLIP: Radiology-informed vision-language alignment for interpretable MRI-based brain tumor classification](https://www.medrxiv.org/content/10.64898/2026.03.11.26348155v2)
  来源：medRxiv | 日期：2026-07-02 | 相关度：6.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Accurate classification of brain tumors from MRI is critical for guiding clinical decision-making; however, existing deep learning models are often hindered by limited interpretability and pronounced sensitivity to hyper...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [StructureSAFE: A structure-aware chemical language model for unified hit identification and lead optimization](https://www.biorxiv.org/content/10.64898/2026.06.28.735128v1)
  来源：bioRxiv | 日期：2026-07-02 | 相关度：7.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Structure-based generative models (SBGMs) hold great promises for accelerating drug discovery by enabling target-aware molecular design. However, existing approaches face fundamental challenges: three-dimensional graph-b...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 其他

- [Comparing Artificial Intelligence versus Human Screening in Systematic Reviews](https://www.medrxiv.org/content/10.64898/2026.07.01.26356995v1)
  来源：medRxiv | 日期：2026-07-02 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：IntroductionSystematic reviews are essential for informing health policy and practice. Artificial intelligence (AI) automates the article screening process and produces time savings, although the performance of AI screen...
  为什么值得看：medRxiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Lynx: Progressive Speculative Quantization for accelerating KV Transfer in Long-Context Inference](http://arxiv.org/abs/2607.01831v1)
  来源：arXiv | 日期：2026-07-02 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Long-context inference is increasingly common in large language model (LLM) serving, driven by retrieval-augmented generation and agentic systems. In disaggregated inference, these workloads require transferring large Ke...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [StatEval: A Comprehensive Benchmark for Large Language Models in Statistics](http://arxiv.org/abs/2510.09517v2)
  来源：arXiv | 日期：2025-10-10 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Despite rapid advances in large language models (LLMs), statistical reasoning remains underrepresented in existing LLM benchmarks, which often do not reflect the layered, proof-driven nature of real statistical practice....
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ChemGraph-XANES: An Agentic Framework for XANES Simulation and Curation](http://arxiv.org/abs/2604.16205v2)
  来源：arXiv | 日期：2026-04-17 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Computational X-ray absorption near-edge structure (XANES) is widely used to interpret local coordination environments, oxidation states, and electronic structure in chemically complex systems. In practice, routine compu...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ResearchClawBench: A Benchmark for End-to-End Autonomous Scientific Research](http://arxiv.org/abs/2606.07591v4)
  来源：arXiv | 日期：2026-05-28 | 相关度：2.5 | 新颖度：1.5
  匹配主题：未命中具体主题
  中文摘要：AI coding agents are increasingly used for scientific work, but their end-to-end autonomous research capability remains difficult to verify. We present ResearchClawBench, a benchmark for evaluating autonomous scientific ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ContextNest: Verifiable Context Governance for Autonomous AI Agent](http://arxiv.org/abs/2607.02116v1)
  来源：arXiv | 日期：2026-07-02 | 相关度：2.1 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Autonomous AI agents increasingly depend on external knowledge stores, yet most retrieval pipelines provide relevance without durable guarantees of provenance, version identity, integrity, traceability, or point-in-time ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Traceable Fault Diagnosis for Battery Energy Storage Systems via Retrieval-Augmented Multi-Agent O&M Assistant](http://arxiv.org/abs/2607.01992v1)
  来源：arXiv | 日期：2026-07-02 | 相关度：2.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large-scale battery energy storage systems (BESSs) require O&M decisions that combine alarms, cell-level measurements, device topology, diagnostic tables, historical cases, and maintenance documents. Monitoring platforms...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [GeneBench-Pro: Evaluating Multistage Statistical Reasoning in Genomics, Quantitative Biology, and Translational Biomedicine](https://www.biorxiv.org/content/10.64898/2026.06.29.735386v3)
  来源：bioRxiv | 日期：2026-07-02 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：We introduce GeneBench-Pro, an expanded and improved version of GeneBench that comprises harder problems across a wider breadth of domains. GeneBench-Pro is a benchmark for AI agents performing realistic multi-stage scie...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Optimizing RAG Rerankers with LLM Feedback via Reinforcement Learning](http://arxiv.org/abs/2604.02091v2)
  来源：arXiv | 日期：2026-04-02 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Rerankers play a pivotal role in refining retrieval results for Retrieval-Augmented Generation. However, current reranking models are typically optimized on static human annotated relevance labels in isolation, decoupled...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MAM-AI: An On-Device Medical Retrieval-Augmented Generation System for Nurses and Midwives in Zanzibar](http://arxiv.org/abs/2606.29580v2)
  来源：arXiv | 日期：2026-06-28 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Maternal and newborn mortality remain among the highest in sub-Saharan Africa, where midwifery care is often delivered by nurses who lack midwifery training to international standards, and consulting authoritative guidan...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Know Your Source: A Public Knowledge Store for Media Background Checks](http://arxiv.org/abs/2607.02383v1)
  来源：arXiv | 日期：2026-07-02 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：LLM-based retrieval-augmented generation (RAG) is increasingly used for automated fact-checking (AFC) and related tasks. By grounding LLM outputs in retrieved evidence, RAG-based systems provide transparent justification...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Memora: A Harmonic Memory Representation Balancing Abstraction and Specificity](http://arxiv.org/abs/2602.03315v2)
  来源：arXiv | 日期：2026-02-03 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Agent memory systems must accommodate continuously growing information while supporting efficient, context-aware retrieval for downstream tasks. Abstraction is essential for scaling agent memory, yet it often comes at th...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [FCDC: Nonvolatile Charge-Domain Attention with HZO Ferroelectric Capacitors](http://arxiv.org/abs/2605.28208v3)
  来源：arXiv | 日期：2026-05-27 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Transformer decoding is increasingly constrained by the key-value (KV) cache it must keep resident and re-read across a long session. We present the Ferroelectric Charge-Domain Compute Cell (FCDC), a hafnium-zirconium-ox...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [mamabench and mamaretrieval: Benchmarks for Evaluating Medical Retrieval-Augmented Generation in Maternal, Neonatal, and Reproductive Health](http://arxiv.org/abs/2606.29467v2)
  来源：arXiv | 日期：2026-06-28 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Medical question-answering benchmarks rarely cover the maternal, neonatal, child, and reproductive-health questions a nurse-midwife asks, and, to our knowledge, no public chunk-level relevance benchmark exists for matern...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Efficient and valid large molecule generation via self-supervised generative models.](https://pubmed.ncbi.nlm.nih.gov/42399464/)
  来源：PubMed | 日期：2026-07-03 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：The realm of molecular design, particularly for large molecules, presents unique challenges and opportunities in drug discovery and materials science. Large molecule design is inherently more complex and less explored co...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [EssTFNet: integration of adaptive time-frequency and DNA language models for interpretable human essential gene prediction.](https://pubmed.ncbi.nlm.nih.gov/42398069/)
  来源：PubMed | 日期：2026-07-03 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Essential genes are defined as indispensable for an organism's survival. The loss of function of these genes results in cell death or an inability to complete the normal life cycle. Research on essential genes is pivotal...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Improving Cancer Driver Gene Prediction using Biological knowledge-guided Prompts for LLM.](https://pubmed.ncbi.nlm.nih.gov/42397991/)
  来源：PubMed | 日期：2026-07-03 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Accurately identifying cancer driver genes is crucial for understanding cancer and developing therapies. However, challenges such as limited sample sizes and insufficient differentiation of gene characteristics hinder cu...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Affinage: genome-scale mechanistic gene annotation from the published literature](http://arxiv.org/abs/2607.02217v1)
  来源：arXiv | 日期：2026-07-02 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Understanding the mechanistic function of a gene is a critical starting point for biology. However, for much of the human proteome that knowledge is scattered across thousands of primary papers or remains poorly establis...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Alternative routes to universal diversity scaling in component systems: from proteomes to large language models](http://arxiv.org/abs/2607.02221v1)
  来源：arXiv | 日期：2026-07-02 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Remarkably common statistical laws characterize the diversity scaling and its fluctuations across a wide range of complex "component systems". These regularities are often interpreted as signatures of an underlying innov...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Evaluating Chunking Strategies for Retrieval-Augmented Generation on Academic Texts](http://arxiv.org/abs/2607.01852v1)
  来源：arXiv | 日期：2026-07-02 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) systems use the question-answering capabilities of Large Language Models (LLMs) to access information outside their parameters. We evaluate if cluster-based semantic chunking improves...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CheckRLM: Effective Knowledge-Thought Coherence Checking in Retrieval-Augmented Reasoning](http://arxiv.org/abs/2607.02262v1)
  来源：arXiv | 日期：2026-07-02 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Reasoning Language Models (RLMs) have significantly improved performance on complex tasks by extending the reasoning chain. However, these chains are prone to containing factual errors, particularly in knowledge-intensiv...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Engineering phage endolysins and receptor-binding proteins for foodborne pathogen control and detection: A review and AI-driven framework.](https://pubmed.ncbi.nlm.nih.gov/42001688/)
  来源：PubMed | 日期：2026-07-02 | 相关度：2.65 | 新颖度：0.25
  匹配主题：sequencing_bioinformatics
  中文摘要：Antimicrobial resistance exacerbates food safety risks, highlighting the need for novel, matrix-tolerant control and detection tools. Phage-derived endolysins and receptor-binding proteins (RBPs) offer high specificity, ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CausalSteward: An Agentic Divide-Conquer-Combine Copilot for Causal Discovery](http://arxiv.org/abs/2607.01936v1)
  来源：arXiv | 日期：2026-07-02 | 相关度：2.1 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Learning causal models from high-dimensional data is a significant challenge, particularly in real-world settings where violations of core assumptions lead to causal identifiability issues. Although massive amounts of pr...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Multi-modality Graph Representation Learning for Malignant Cell Identification from scRNA-seq using DeepMalignant](https://www.biorxiv.org/content/10.64898/2026.06.29.734828v1)
  来源：bioRxiv | 日期：2026-07-03 | 相关度：1.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Distinguishing malignant from normal cells in single-cell RNA sequencing data remains a critical yet challenging task in cancer genomics. Existing methods often suffer from poor precision, limited generalizability across...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Artificial intelligence in molecular diagnostics for pandemic preparedness.](https://pubmed.ncbi.nlm.nih.gov/42396845/)
  来源：PubMed | 日期：2026-07-03 | 相关度：3.65 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Molecular diagnostics focusing on the detection and analysis of nucleic acids, are indispensable tools for early pathogen identification, transmission monitoring, and genomic surveillance during pandemics. Recent technol...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Trust, mistrust, and the promise of AI in genomics for African populations.](https://pubmed.ncbi.nlm.nih.gov/42296962/)
  来源：PubMed | 日期：2026-07-02 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Artificial intelligence (AI) is rapidly reshaping genomic medicine, yet its benefits remain unevenly distributed due to the profound under-representation of African populations in genomic datasets and persistent legacies...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
