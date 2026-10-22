# 每日论文监控日报 (2026-10-22)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 59 篇新论文。

## 抓取状态

- arXiv：成功，命中 63 篇
- PubMed：成功，命中 25 篇
- bioRxiv：失败，命中 0 篇，错误：('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
- medRxiv：成功，命中 16 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [AI-Empowered Multimodal Data Integration and Knowledge Discovery for Pharmacovigilance](https://www.medrxiv.org/content/10.64898/2026.10.20.26365969v1)
  来源：medRxiv | 日期：2026-10-21 | 相关度：8.9 | 新颖度：6.2
  匹配主题：foundation_model_agent
  中文摘要：Biomedical artificial intelligence (AI) increasingly relies on heterogeneous data sources, yet differences in data structure, terminology, evidence quality, and provenance complicate their integration into reliable knowl...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [ProMORNA: An End-to-End Generative Framework for Full-Length mRNA Design](http://arxiv.org/abs/2605.01513v2)
  来源：arXiv | 日期：2026-05-02 | 相关度：7.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Designing therapeutic messenger RNA (mRNA) requires generating full-length transcripts that optimally balance intracellular stability and translation efficiency. While generative models have advanced mRNA design, existin...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [VGL-stGen: Learning a shared multimodal model for lung histology and spatial transcriptomics](http://arxiv.org/abs/2610.28266v1)
  来源：arXiv | 日期：2026-10-20 | 相关度：8.9 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：VGL-stGen is a multimodal large language model adapted from a pretrained medical vision-language model using paired lung H&E and spatial transcriptomics with single-cell references. Training integrates image-expression a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LongHisDoc: A Comprehensive Benchmark for Chinese Long Historical Document Understanding](http://arxiv.org/abs/2610.14531v2)
  来源：arXiv | 日期：2026-10-10 | 相关度：7.5 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Chinese historical documents are invaluable cultural treasures, but their complexity poses significant comprehension challenges for non-specialists. Despite the success of Large Language Models (LLMs) and Large Vision-La...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Small Average Error, Wide Individual Error: General-Purpose LLMs Estimating Energy Intake from Meal Photos in a Feeding Trial](http://arxiv.org/abs/2610.26538v2)
  来源：arXiv | 日期：2026-10-19 | 相关度：7.1 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Photo-based estimation of food energy could ease dietary assessment, and general-purpose multimodal large language models (LLMs) make such estimates easy to obtain. Most evaluations use one photo taken before eating and ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TabAgent: Distilling LLM Agent Components into Cheap Classifiers](http://arxiv.org/abs/2602.16429v2)
  来源：arXiv | 日期：2026-02-18 | 相关度：6.55 | 新颖度：6.7
  匹配主题：foundation_model_agent
  中文摘要：Agentic systems, AI architectures that autonomously execute multi-step workflows to achieve complex goals, are often built using repeated large language model (LLM) calls for closed-set decision tasks such as routing, sh...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multi-agent LLM diagnostic teams improve differential recall on curated cases and reverse on real emergency notes: a label-level reversal without a clinician-judged safety difference](https://www.medrxiv.org/content/10.64898/2026.09.24.26363897v3)
  来源：medRxiv | 日期：2026-10-21 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Background. Multi-agent large language model (LLM) pipelines are proposed for diagnostic support, but when they help or harm is unknown: evaluations use curated case reports, rarely include budget-matched controls, or is...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [EHRAdapt: Adapting Pretrained Language Models to Electronic Health Records with Semantic Priors for Rare Clinical Events](http://arxiv.org/abs/2609.34007v2)
  来源：arXiv | 日期：2026-09-27 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Electronic health records (EHRs) encode clinical histories as (time, modality, code) tuples, whereas pretrained language models expect text tokens. Serializing tuples as text inflates sequence length and repeatedly encod...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Towards Explainable Industrial Anomaly Detection via Knowledge-Guided Latent Reasoning](http://arxiv.org/abs/2602.09850v3)
  来源：arXiv | 日期：2026-02-10 | 相关度：6.1 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Industrial anomaly detection demands precise reasoning over fine-grained defect patterns. However, existing multimodal large language models (MLLMs), pretrained on general-domain data, often struggle to capture category-...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Automated Materials Data and Knowledge Extraction using Machine Learning and Large Language Models](http://arxiv.org/abs/2610.29895v1)
  来源：arXiv | 日期：2026-10-21 | 相关度：5.45 | 新颖度：8.1
  匹配主题：foundation_model_agent
  中文摘要：Over the past decade, substantial efforts have been devoted to developing machine learning (ML) methods for extracting materials data and, where possible, materials knowledge directly from the scientific literature. This...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TENET: One Step Toward Test-Driven Development for Repository-Level Code Generation](http://arxiv.org/abs/2509.24148v6)
  来源：arXiv | 日期：2025-09-29 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Test-Driven Development (TDD) is a widely adopted practice that requires developers to create and execute tests alongside implementation. With recent advances in Large Language Models (LLMs), developers can shift from ma...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From prompting to evidence-based translation: A RAG+prompt system for Japanese-Chinese translation and its pedagogical potential](http://arxiv.org/abs/2605.03387v2)
  来源：arXiv | 日期：2026-05-05 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Large language models perform well on high-resource pairs but are less reliable for Japanese-Chinese sentences containing noun-modifying clause constructions (NMCCs). This study evaluates a retrieval-augmented generation...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SIREN (Luring LLMs onto the Rocks): PAIR-Driven Preference Manipulation in Web-RAG Recommenders](http://arxiv.org/abs/2607.21951v4)
  来源：arXiv | 日期：2026-07-24 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：This paper investigates the adversarial manipulation of the ranked recommendations produced by web-augmented large language models (LLMs). When an LLM answers a recommendation query by retrieving and reading live webpage...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Real PMIDs, Wrong Papers: Harness Design for Biomedical Claim-Verification Agents](http://arxiv.org/abs/2610.29812v1)
  来源：arXiv | 日期：2026-10-21 | 相关度：4.75 | 新颖度：6.67
  匹配主题：foundation_model_agent
  中文摘要：Literature-searching language agents are becoming a standard component of scientific assistants for the life sciences, yet there is little controlled evidence on which parts of their harness matter. We run a controlled a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Performance of Contemporary Large Language Models on the National Prosthodontic Resident Examination: A Multi-Year Comparative Study](https://www.medrxiv.org/content/10.64898/2026.10.19.26365937v1)
  来源：medRxiv | 日期：2026-10-21 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Purpose: To compare the performance of three large language models (LLMs), ChatGPT-o1, Grok 3, and Gemini 2.0 Pro, on the American College of Prosthodontists' National Prosthodontic Resident Examination (NPRE). Materials...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DynaCI: Generating GitHub Actions Workflows via Dynamic Analysis](http://arxiv.org/abs/2610.29890v1)
  来源：arXiv | 日期：2026-10-21 | 相关度：3.45 | 新颖度：7.33
  匹配主题：foundation_model_agent
  中文摘要：Continuous Integration (CI) is an essential practice that automatically validates code changes through builds and tests. However, configuring CI workflows remains challenging, as modern software often features complex ar...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [DNA augmentations for semi-supervised learning in genomic sequence classification.](https://pubmed.ncbi.nlm.nih.gov/42898793/)
  来源：PubMed | 日期：2026-12-01 | 相关度：6.75 | 新颖度：4.75
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：Semi-supervised learning (SSL) is a natural fit for genomics, where unlabeled sequences are abundant but high-quality labels are scarce due to costly curation. However, most SSL pipelines rely on generic perturbations th...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Predictor-Guided Latent Space Codon Optimization for Maximizing Protein Expression](http://arxiv.org/abs/2610.03098v2)
  来源：arXiv | 日期：2026-10-02 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Codon optimization, the process of selecting synonymous codons to improve mRNA translation efficiency and protein expression, is central to therapeutic protein production and mRNA vaccines, yet it remains a hard problem....
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [NeoGen-BC: A synergistic framework combining generative protein language models and multi-window deep learning for designing shared neoantigens in breast cancer.](https://pubmed.ncbi.nlm.nih.gov/42721858/)
  来源：PubMed | 日期：2026-10-22 | 相关度：7.15 | 新颖度：3.74
  匹配主题：foundation_model_agent
  中文摘要：Breast cancer, particularly hormone receptor-positive (HR + ) and triple-negative (TNBC) subtypes, is often immunologically "cold," limiting immunotherapy efficacy. Neoantigen-based vaccines hold promise but face challen...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ArtSeek: Deep artwork understanding via multimodal in-context reasoning and late interaction retrieval](http://arxiv.org/abs/2507.21917v2)
  来源：arXiv | 日期：2025-07-29 | 相关度：6.8 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Analyzing digitized artworks requires both visual interpretation and deep artistic, contextual, and historical knowledge. We introduce ArtSeek, a multimodal framework for art analysis that combines multimodal large langu...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MADDIE: Multi-Agent Drug Discovery Engine](http://arxiv.org/abs/2610.16975v3)
  来源：arXiv | 日期：2026-10-12 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Drug discovery remains a resource-intensive and time-consuming process, involving billions of dollars and a decade of development to advance a drug to market. While many in silico tools have accelerated this process, ope...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Large language model classifies prior evidence in gene-phenotype associations](https://www.medrxiv.org/content/10.64898/2026.10.17.26365766v1)
  来源：medRxiv | 日期：2026-10-19 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：The growing scale of genome-wide and rare-variant association studies is shifting the bottleneck from discovery to interpretation, which requires positioning each new association against prior evidence. We present PESTO ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Retrieval Augmented Generation Compositionality](http://arxiv.org/abs/2610.29722v1)
  来源：arXiv | 日期：2026-10-21 | 相关度：5.45 | 新颖度：7.24
  匹配主题：foundation_model_agent
  中文摘要：Retrieval Augmented Generation (RAG) grounds large language models in external knowledge. Modern pipelines combine embedding, chunking, retrieval, reranking, query augmentation, context compression, and agentic verificat...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [From Prompts to Posteriors: Can LLM Agents Perform Bayesian Inference in Context?](http://arxiv.org/abs/2610.29331v1)
  来源：arXiv | 日期：2026-10-21 | 相关度：5.45 | 新颖度：6.24
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly applied across the scientific discovery pipeline, from synthesizing literature to generating hypotheses to informing experimental design. A unifying principle behind these ta...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MAPS: Macro-Adaptive Parallel Reasoning for Regulating Search Momentum in Retrieval-Augmented Generation](http://arxiv.org/abs/2610.29792v1)
  来源：arXiv | 日期：2026-10-21 | 相关度：4.75 | 新颖度：7.13
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) improves the performance of Large Language Models (LLMs) by retrieving external knowledge. Recently, some RAG methods interleave reasoning and retrieval, enabling LLMs to progressivel...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Plan First, Act Later: Streaming Reasoning for Executable Memory in Robot Control](http://arxiv.org/abs/2610.29329v1)
  来源：arXiv | 日期：2026-10-21 | 相关度：4.75 | 新颖度：5.98
  匹配主题：foundation_model_agent
  中文摘要：Long-horizon robot manipulation requires a robot to remember task-relevant information beyond its short observation window. Existing memory-augmented policies typically retrieve relevant information from history and reas...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ExpEvolve: Structuring and Reusing Experience for Open-Ended Discovery](http://arxiv.org/abs/2610.29303v1)
  来源：arXiv | 日期：2026-10-21 | 相关度：4.75 | 新颖度：5.41
  匹配主题：foundation_model_agent
  中文摘要：Evolutionary coding agents such as AlphaEvolve are one of the notable successes in using Large Language Models (LLMs) to build AI Scientists. These agents tackle open-ended scientific problems by iteratively improving an...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Source-linked multispecialty clinical reasoning and tumour-board decision-making in colorectal cancer](https://www.medrxiv.org/content/10.64898/2026.10.19.26365647v1)
  来源：medRxiv | 日期：2026-10-21 | 相关度：7.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Clinical records preserve patient findings and final recommendations but rarely capture how specialists select evidence, develop alternative interpretations, disagree, and converge on a management strategy. We describe a...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [A general-purpose System One decision model for clinical records](http://arxiv.org/abs/2610.27099v1)
  来源：arXiv | 日期：2026-10-19 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Clinical care, health-system operations and biomedical discovery depend on extracting reliable answers from patient records, yet applying diverse clinical questions across entire populations remains computationally expen...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Building AI Research Teams for Autonomous Discovery of Linear Attention Architectures](http://arxiv.org/abs/2610.28887v1)
  来源：arXiv | 日期：2026-10-20 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Autonomous agents can increasingly propose ideas, modify code, and run experiments, creating an opportunity to accelerate scientific discovery using teams of collaborative AI researchers. To escape local minima in the di...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [ProMemAgent: Long-Horizon Proactive Assistance with Context-Aware Prospective Memory from Sensory Perceptions](http://arxiv.org/abs/2610.27400v1)
  来源：arXiv | 日期：2026-10-19 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Large language model (LLM) agents are moving beyond reactive responses toward proactive assistance that anticipates user needs without explicit requests. However, existing proactive agents primarily address immediate nee...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [WorldScape Policy 2.0: Empowering Steerable World Action Modeling with Reasoning-Augmented Memory and In-Context Learning](http://arxiv.org/abs/2607.18840v3)
  来源：arXiv | 日期：2026-07-21 | 相关度：6.1 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：World Action Models (WAMs) offer a promising paradigm for robotic manipulation by jointly modeling visual state transitions and robot actions. However, existing WAMs are constrained by limited temporal context, coarse ep...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The Effectiveness and Durability of Pretraining Data Filtering in Protein Language Models](http://arxiv.org/abs/2610.26651v1)
  来源：arXiv | 日期：2026-10-19 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Pretraining filtering is one of the most common safeguards for open-weight language models. Here we study its effectiveness, durability and scalability using the ESM-2 family of protein language models. We find that filt...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [recAMPLIFY: Large-Scale Pretraining of Recursive Protein Language Models](http://arxiv.org/abs/2610.26747v1)
  来源：arXiv | 日期：2026-10-19 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Protein language models (pLMs) are powerful tools for protein annotation and mutation-effect prediction, but progress has largely depended on scaling model size and data, making them expensive and prone to memorization. ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Magnolia: A Persistent-Memory Agent Framework for Computational Chemistry](http://arxiv.org/abs/2610.27230v1)
  来源：arXiv | 日期：2026-10-19 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Chemistry has recently entered a high-data regime as molecular databases from high-throughput platforms or computational studies have become available. Increasing automation within the chemical sciences leads to a more d...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RAG-NIMBF: A Non-Invasive, Modular Benchmarking Framework for Automated RAG Configuration Analysis](http://arxiv.org/abs/2610.27816v1)
  来源：arXiv | 日期：2026-10-20 | 相关度：5.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) has become the dominant paradigm for grounding the outputs of large language models (LLM) in external knowledge. However, practitioners are faced with a vast configuration space compr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RANGER: Retrieval Agent for Navigating Graphs with Semantic Evaluation Rewards](http://arxiv.org/abs/2610.28010v1)
  来源：arXiv | 日期：2026-10-20 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：The integration of Large Language Models and Reinforcement Learning offers a promising direction for complex sequential decision-making tasks, such as multi-hop question answering over knowledge graphs. While LLMs provid...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Multimodal Engineering GraphRAG Framework for Post-Wind-Event Building Assessment and Recovery Inference](http://arxiv.org/abs/2610.28216v1)
  来源：arXiv | 日期：2026-10-20 | 相关度：2.75 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Post-event building assessment requires linking observed physical damage to its consequences for safety, habitability, functionality, and recovery. Yet post-disaster evidence is often heterogeneous, incomplete, and distr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CanLegalRAGBench: Evaluating Retrieval-Augmented Generation on Canadian Case Law](http://arxiv.org/abs/2605.30497v3)
  来源：arXiv | 日期：2026-05-28 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：RAG-based legal assistants have been growing in popularity, but LLM hallucinations remain a key issue and potentially undermines justice. While benchmarks have been developed to evaluate progress, many rely on synthetic ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multi-Agent AI Design of a Nanowatt Biomedical Low-Pass Filter from Topology to Layout](http://arxiv.org/abs/2610.28677v1)
  来源：arXiv | 日期：2026-10-19 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：We demonstrate a multi-agent framework that takes an analog circuit from topology synthesis to layout. A researcher agent directs schematic and layout agents, a four-tier memory stores the specification and lessons, and ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic AI -- Physicist Collaboration in Experimental Particle Physics: A Proof-of-Concept Measurement with LEP Open Data](http://arxiv.org/abs/2603.05735v3)
  来源：arXiv | 日期：2026-03-05 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：We present an agentic measurement of the thrust distribution in $e^{+}e^{-}$ collisions at $\sqrt{s}=91.2$ GeV using ALEPH archived data. This work was carried out through an AI agent-physicist collaboration, using inter...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Auto-Director: Leveraging Multi-Agent Collaboration for Autonomous Video Editing](http://arxiv.org/abs/2610.28346v1)
  来源：arXiv | 日期：2026-10-20 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Autonomous video editing from open-world resources remains a challenging problem in multimedia content creation. Retrieval-based methods are constrained by fixed source material and lack creative flexibility, while gener...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OptScientist: Automated Discovery of Optimization Laws](http://arxiv.org/abs/2610.28562v1)
  来源：arXiv | 日期：2026-10-20 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Many scientific phenomena are best understood as outcomes of underlying optimization problems, yet automated scientific discovery has largely focused on recovering equations that describe observed input-output patterns. ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DiscoveryRSI: Recursively Learning to Discover Valuable Hypotheses](http://arxiv.org/abs/2610.23839v2)
  来源：arXiv | 日期：2026-10-16 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Scientific discovery requires developing worthwhile hypotheses into practical investigations, yet learning from this evolving research process remains challenging. We introduce an operational definition of valuable and t...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Context-Aware Prompt Injection Detection via Small Language Models in RAG Pipelines: nokast-secureRAG](http://arxiv.org/abs/2610.28364v1)
  来源：arXiv | 日期：2026-10-20 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Local Retrieval-Augmented Generation (RAG) systems are vulnerable to indirect prompt injection and retrieval poisoning, where malicious instructions in retrieved content are mistaken for trusted input. We present nokast-...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Learning Marginal Viewpoint Utility for Budgeted Evidence Selection in RAG](http://arxiv.org/abs/2610.29234v1)
  来源：arXiv | 日期：2026-10-21 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation over multi-viewpoint queries must preserve distinct answers and positions from the retrieved evidence while operating under a fixed context budget. We introduce LMVU, a lightweight ranker t...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [A Unified HI Rotation Curve Database for 122 Dwarf and Irregular Galaxies](http://arxiv.org/abs/2605.22163v2)
  来源：arXiv | 日期：2026-05-21 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：We present a unified HI rotation curve database for 122 dwarf and irregular galaxies drawn from three Local Volume surveys, the Local Volume HI Survey (LVHIS; 32 galaxies), VLA-ANGST (29) and LITTLE THINGS (26), and from...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [DeclineCraft: A RAG Abstention Benchmark for Jointly Measuring Combined Retrieval and Parametric Knowledge](http://arxiv.org/abs/2610.28340v1)
  来源：arXiv | 日期：2026-10-20 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Reliable retrieval-augmented generation (RAG) requires recognizing when neither retrieved documents nor parametric knowledge supports an answer. We introduce DeclineCraft, a dynamic abstention benchmark whose unanswerabl...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [WorldSR: Harnessing World Knowledge Search for Grounded Image Super-Resolution](http://arxiv.org/abs/2610.28423v1)
  来源：arXiv | 日期：2026-10-20 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Generative-prior-based super-resolution (SR) methods leverage implicit knowledge learned from large-scale models to enhance low-resolution inputs. However, such priors are inherently stochastic and optimized for diverse ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [ProtSent: Protein Sentence Transformers](http://arxiv.org/abs/2605.06830v2)
  来源：arXiv | 日期：2026-05-07 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Protein language models produce rich per-residue representations, but the sequence embeddings obtained by mean-pooling them are never trained to place related proteins near one another, so the geometry that retrieval, cl...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Orthogonal Boundary Unlearning for Dual-Use Concepts in Large Language Models](http://arxiv.org/abs/2610.27490v1)
  来源：arXiv | 日期：2026-10-20 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Mitigating catastrophic risks from large language models requires excising hazardous operational capabilities, such as cyberwarfare exploitation and pathogen enhancement, without degrading benign scientific utility. In t...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [IDEAgent: Agentic Quality-Diversity Search for Research Idea Generation](http://arxiv.org/abs/2607.22375v2)
  来源：arXiv | 日期：2026-07-24 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have significantly advanced the automation of scientific discovery. However, existing systems share a core limitation: they optimize ideas independently for either Quality or Diversity. This ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Secure Multimodal Federated Optimization via Hierarchical DNA-Based Key Management](http://arxiv.org/abs/2610.27644v1)
  来源：arXiv | 日期：2026-10-20 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Federated optimization over heterogeneous multimodal data enables distributed institutions to collaboratively optimize a shared model using medical images, genomic profiles, clinical records, and physiological signals wi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Graph Topology Meets Energy-Driven Pathfinding: Preserving Contextual Consistency in Retrieval-Augmented Generation](http://arxiv.org/abs/2610.29933v1)
  来源：arXiv | 日期：2026-10-21 | 相关度：2.75 | 新颖度：7.67
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) frequently integrates knowledge graphs (KGs) for complex multi-hop question answering. However, their performance is increasingly bottlenecked by the knowledge structuring and reasoni...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GenoMAS: Guided Multi-Agent Programming for Scientific Discovery from Genomic Data](http://arxiv.org/abs/2507.21035v4)
  来源：arXiv | 日期：2025-07-28 | 相关度：2.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Gene expression analysis holds the key to many biomedical discoveries, yet extracting insights from raw transcriptomic data remains challenging due to the complexity of multiple large, semi-structured files and the need ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [PersonalAI 2.0: Enhancing knowledge graph traversal/retrieval with planning mechanism for Personalized LLM Agents](http://arxiv.org/abs/2605.13481v4)
  来源：arXiv | 日期：2026-05-13 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：We introduce PersonalAI 2.0 (PAI-2), a novel framework designed to enhance LLM-based systems through integration of external knowledge graphs (KGs). The proposed approach addresses key limitations of existing Graph Retri...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Quality and transcript-grounded clinical-risk error burden of AI-generated vs allied health professional clinical notes: a paired simulation study across four disciplines](https://www.medrxiv.org/content/10.64898/2026.10.16.26365719v1)
  来源：medRxiv | 日期：2026-10-19 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Background: Ambient artificial-intelligence (AI) scribes are being deployed beyond medicine into allied-health practice, but comparative evidence mainly concerns physician documentation. Objective: To compare quality and...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [HGASurv: Hierarchical Granularity-Aware Multimodal Integration for Survival Prediction](http://arxiv.org/abs/2610.26357v2)
  来源：arXiv | 日期：2026-10-19 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Multimodal survival prediction jointly analyzes histopathological whole-slide images (WSIs), genomic profiles, and clinical variables to stratify patients by risk. However, existing approaches often inadequately account ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [C$^2$U in RAG: Compositional Concept Unlearning in Retrieval-Augmented Generation](http://arxiv.org/abs/2610.29223v1)
  来源：arXiv | 日期：2026-10-21 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation can expose unwanted concepts through retrieved evidence even when the generator is moderated. We study query-side concept suppression with a fixed encoder and document index. Compositional ...
  为什么值得看：C$^2$U in RAG: Compositional Concept Unl 与你的主题有弱匹配，暂时保留作低优先级跟踪。
