# 每日论文监控日报 (2026-08-12)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 51 篇新论文。

## 抓取状态

- arXiv：成功，命中 44 篇
- PubMed：成功，命中 37 篇
- bioRxiv：失败，命中 0 篇，错误：('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
- medRxiv：成功，命中 12 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [Proteo-R1: Reasoning Foundation Models for De Novo Protein Design](http://arxiv.org/abs/2605.02937v2)
  来源：arXiv | 日期：2026-05-01 | 相关度：8.9 | 新颖度：6.7
  匹配主题：foundation_model_agent
  中文摘要：Deep learning in de novo protein design has achieved atomic-level fidelity. However, existing models remain largely non-deliberative: they directly synthesize molecular geometries without explicitly reasoning about which...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The Periodic Table of LLM Reasoning: A Structured Survey of Reasoning Paradigms, Methods, and Failure Modes](http://arxiv.org/abs/2606.11470v2)
  来源：arXiv | 日期：2026-06-09 | 相关度：7.5 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Reasoning has become central to how Large Language Models (LLMs) are evaluated and interpreted, spanning Chain-of-Thought (CoT), mathematical problem-solving, multi-hop question answering, code generation, retrieval-augm...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TongGuOCR: A Layout-Aware and Token-Augmented OCR MLLM for Chinese Historical Documents](http://arxiv.org/abs/2608.07917v2)
  来源：arXiv | 日期：2026-08-08 | 相关度：7.5 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Chinese historical documents preserve valuable cultural heritage, but many collections remain accessible only as scanned page images, preventing full-text retrieval, collation, and computational analysis. Optical charact...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Self-Knowledge Retrieval Augmented Generation Framework for Patent Matching](http://arxiv.org/abs/2608.11030v1)
  来源：arXiv | 日期：2026-08-11 | 相关度：6.55 | 新颖度：8.44
  匹配主题：foundation_model_agent
  中文摘要：Patent retrieval and matching based on large language models (LLMs) play a vital role in intellectual property protection. However, due to the complex structure of patent documents, dense technical terminology, and multi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [An Agentic Generative Large Language Model for Treatment Planning of Colorectal Cancer](http://arxiv.org/abs/2608.09142v1)
  来源：arXiv | 日期：2026-08-10 | 相关度：7.55 | 新颖度：1.2
  匹配主题：foundation_model_agent
  中文摘要：Treatment planning in precision oncology requires synthesizing heterogeneous patient information with rapidly evolving clinical guidelines to ensure guideline-concordant care. While large language models (LLMs) show prom...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TRACE: Trustworthy Retrieval-Augmented Conversational Engine](http://arxiv.org/abs/2608.10176v1)
  来源：arXiv | 日期：2026-08-10 | 相关度：6.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Public service chatbots are expected to deliver recommendations from an underlying public service directory, while also making sure that the recommendations respect explicit user constraints. In practice, public service ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SoK: The Attack Surface of Agentic AI - Tools and Autonomy](http://arxiv.org/abs/2603.22928v2)
  来源：arXiv | 日期：2026-03-24 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Recent AI systems combine large language models with tools, external knowledge via retrieval-augmented generation (RAG), and even autonomous multi-agent decision loops. This agentic AI paradigm greatly expands capabiliti...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Contemporary AI lacks the imagination to diverge or negate in science](http://arxiv.org/abs/2606.08251v3)
  来源：arXiv | 日期：2026-06-06 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Bold claims that AI will accelerate scientific discovery have raced ahead of evidence from working scientists, yet large-scale, scientist-in-the-loop evidence is scarce. Here we mount the largest evaluation to date, invi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MetaStrategy: Generative Ranking with Executable LLM Strategies](http://arxiv.org/abs/2608.09440v1)
  来源：arXiv | 日期：2026-08-10 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Industrial recommender systems rank heterogeneous content under coupled user, business, commercial, and experience objectives. Existing generative ranking methods typically construct item sequences directly, making them ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Training Dense Retrievers with Multiple Positive Passages](http://arxiv.org/abs/2602.12727v2)
  来源：arXiv | 日期：2026-02-13 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Modern knowledge-intensive systems, such as retrieval-augmented generation (RAG), rely on effective retrievers to establish the performance ceiling for downstream modules. However, retriever training has been bottlenecke...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [HiHPO: Multimodal Hierarchical Graph Learning for Predicting Missing Protein-Phenotype Associations.](https://pubmed.ncbi.nlm.nih.gov/42574413/)
  来源：PubMed | 日期：2026-08-10 | 相关度：7.8 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Understanding protein-phenotype associations is essential for elucidating disease mechanisms and supporting phenotype-driven diagnosis. Although the Human Phenotype Ontology (HPO) provides a standardized framework for ph...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A Deep Learning Model for Prediction of Unknown Gene Functionality: Gene Bio-BERT.](https://pubmed.ncbi.nlm.nih.gov/42573472/)
  来源：PubMed | 日期：2026-08-10 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：The Human Genome Project (HGP) was a large international research effort that timelined between 1990 and 2003, marking the successful mapping of the entire human genome. Despite the promising performance of deep learning...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [DegradeQuery: Counterfactual Tuple Pretraining for Context-Aware PROTAC Degradation Prediction](http://arxiv.org/abs/2608.10595v1)
  来源：arXiv | 日期：2026-08-11 | 相关度：5.75 | 新颖度：6.4
  匹配主题：foundation_model_agent
  中文摘要：Proteolysis-targeting chimeras (PROTACs) induce protein degradation by recruiting a target protein to an E3 ubiquitin ligase, making degradation a joint outcome of the degrader molecule and its biological context. Althou...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [REATS: LLM Reasoning-based Ensemble Learning for Adaptive Time Series Forecasting](http://arxiv.org/abs/2608.10149v1)
  来源：arXiv | 日期：2026-08-10 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Due to the diversity of real-world time series, no single forecasting model consistently dominates across all samples. Ensemble learning addresses this by combining complementary model strengths, yet existing methods rel...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Decoding Phenotypes: A Framework for Fusing Genomic Language Models and Neuroimaging](http://arxiv.org/abs/2608.08926v1)
  来源：arXiv | 日期：2026-08-09 | 相关度：7.1 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Neuroimaging and genetic testing are two important clinical references for nervous system diseases, offering complementary diagnostic information. However, integrating genomic and neuroimaging data for precise disease di...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Adverse Drug Events Across Data-Production Contexts: Multilingual Detection, Alignment, and Cross-Genre Discourse Analysis](https://www.medrxiv.org/content/10.64898/2026.08.08.26360012v1)
  来源：medRxiv | 日期：2026-08-11 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Adverse drug event (ADE) evidence is produced across patient-generated, clinical, and scientific settings that differ in language, documentation purpose, terminology, and degree of standardization. These differences shap...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Situation Graph Prediction for User Perspective Modeling](http://arxiv.org/abs/2602.13319v2)
  来源：arXiv | 日期：2026-02-10 | 相关度：2.75 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Perspective-aware AI requires modeling evolving internal states---goals, emotions, contexts---not merely preferences. Progress is limited by a data bottleneck: digital footprints are privacy-sensitive and perspective sta...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RAGMesh with FaME-G2E: Long-Form Text-Driven 3D Face Generation and Editing](http://arxiv.org/abs/2608.09186v1)
  来源：arXiv | 日期：2026-08-10 | 相关度：2.75 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Text-driven 3D face generation and editing remains challenging due to the difficulty of translating long-form descriptions into fine-grained facial geometry. Existing methods primarily align global textual semantics with...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Guardian Crawler: Retrieval-First Knowledge Discovery with Bounded LLM Augmentation for Noisy Web Intelligence](http://arxiv.org/abs/2608.08994v1)
  来源：arXiv | 日期：2026-08-10 | 相关度：2.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieving relevant evidence from noisy web data is challenging, particularly in sensitive domains containing incomplete reports, heterogeneous language, and irrelevant content. We present Guardian Crawler, a reproducibl...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Retrieval-Augmented Vision Foundation Models for Robust Leukemia Cell Classification across Multiple Microscopy Datasets](http://arxiv.org/abs/2608.10657v1)
  来源：arXiv | 日期：2026-08-11 | 相关度：1.7 | 新颖度：7.61
  匹配主题：未命中具体主题
  中文摘要：Leukemia cell image classification is challenged by real-world domain shifts from acquisition, staining, illumination, and site protocols, causing single-dataset models to generalize poorly in real clinical scenarios. Th...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AttriMem: Attribution-Guided Process Feedback for Agent Memory Construction](http://arxiv.org/abs/2607.21106v3)
  来源：arXiv | 日期：2026-07-23 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Effective memory is crucial for LLM agents, yet constructing it effectively remains challenging. A memory-construction policy decides what information to extract, store, update, compress, or discard as interactions accum...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Muscle Memory for Agents: Compile not Merely Retrieve](http://arxiv.org/abs/2608.08995v1)
  来源：arXiv | 日期：2026-08-10 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Memory for LLM agents has converged on a single architectural pattern: store experience as text, embeddings, reflections, or rules; retrieve at inference time; let a general-purpose orchestrator interpret what to do. Thi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multi-agent discovery of practical quantum LDPC codes](http://arxiv.org/abs/2608.08996v1)
  来源：arXiv | 日期：2026-08-10 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Quantum low-density parity-check (qLDPC) codes can encode multiple logical qubits using sparse parity checks, yet searching for useful finite-length instances remains a challenging design problem because code performance...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [ArtifactLinker: Linking Scientific Artifacts for Automatic State-of-the-Art Discovery](http://arxiv.org/abs/2605.16902v2)
  来源：arXiv | 日期：2026-05-16 | 相关度：4.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Scientific artifacts such as models and datasets are foundations for research. With the rapid growth of platforms like HuggingFace, researchers now have access to a large number of artifacts. Yet, a key challenge remains...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [CuSearch: Curriculum Rollout Sampling via Search Depth for Agentic RAG](http://arxiv.org/abs/2605.11611v3)
  来源：arXiv | 日期：2026-05-12 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a promising paradigm for training agentic retrieval-augmented generation (RAG) systems from outcome-only supervision. Most existing methods optimize po...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [ConMem: Contribution-Aware Memory for Long-Horizon Manufacturing Inspection Logs](http://arxiv.org/abs/2607.28126v2)
  来源：arXiv | 日期：2026-07-30 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Long-horizon steel-equipment inspection requires reasoning over heterogeneous records accumulated across repeated inspection cycles. Existing retrieval-augmented generation systems treat historical logs as a static corpu...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [What Would Fix This RAG Failure? Auditing Counterfactual Response with Paired Evidence Interventions](http://arxiv.org/abs/2608.08944v1)
  来源：arXiv | 日期：2026-08-09 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：A failed retrieval-augmented generation (RAG) answer can be consistent with several unseen responses to evidence repair. We introduce Pair-ID, an offline audit that holds one query, retrieval state, and reader constant, ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Mind the Hook: Source-Level Auditing of Privacy Defenses in Retrieval-Augmented Generation](http://arxiv.org/abs/2608.09001v1)
  来源：arXiv | 日期：2026-08-10 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Black-box privacy scores for retrieval-augmented generation (RAG) are difficult to interpret unless the audited defense's active pipeline hook is known. We propose an active-path audit: inventory source-level hooks over ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [EvoSNR-Prom: Predicting promoters at single-nucleotide resolution with label-aware transfer learning of the pretrained EVO model.](https://pubmed.ncbi.nlm.nih.gov/42574449/)
  来源：PubMed | 日期：2026-08-10 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：The precise identification of promoters is crucial for understanding gene regulation. Deep learning methods have achieved considerable success in promoter prediction, yet most operate at the sequence level with coarse-gr...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ESM2-BiMamba: A Length-Adaptive Hybrid Framework for Efficient Concurrent Prediction of DNA-Binding Proteins and DNA-Binding Residue Sites.](https://pubmed.ncbi.nlm.nih.gov/42348910/)
  来源：PubMed | 日期：2026-08-10 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Accurate identification of DNA-binding proteins (DBPs) and their DNA-binding residue sites (DBSs) is essential for understanding gene regulatory processes. Despite recent progress achieved by protein language models, cur...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RAG-3DSG: Enhancing 3D Scene Graphs with Re-Shot Guided Retrieval-Augmented Generation](http://arxiv.org/abs/2601.10168v3)
  来源：arXiv | 日期：2026-01-15 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Open-vocabulary 3D Scene Graph (3DSG) can enhance various downstream tasks in robotics by leveraging structured semantic representations, yet current 3DSG construction methods suffer from semantic inconsistencies caused ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [KGCaRe: Explainable Complex Conditional Question Answering using Automatic Knowledge Graph Construction and Context Retrieval with LLMs](http://arxiv.org/abs/2608.09779v1)
  来源：arXiv | 日期：2026-08-10 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Answering complex conditional questions using Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) remains a challenge, particularly in domain-specific contexts where general-purpose LLMs and RAG tend to...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Decoding Leukocyte Dynamics: Functional Biomarkers and Precision Diagnostics in Parasitic Infections.](https://pubmed.ncbi.nlm.nih.gov/42573872/)
  来源：PubMed | 日期：2026-08-10 | 相关度：4.7 | 新颖度：0.25
  匹配主题：pathogenomics
  中文摘要：Parasitic infections affect over 1.5 billion people globally, with leukocytes serving as critical mediators of both protective immunity and immunopathology. Traditional diagnostic approaches relying on static cell counts...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Reliability of AI Methods in Drug Discovery: Evaluation of Boltz-2 for Structure and Binding Affinity Prediction.](https://pubmed.ncbi.nlm.nih.gov/42579383/)
  来源：PubMed | 日期：2026-08-11 | 相关度：2.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Despite continuing hype about the role of AI in drug discovery, no "AI-discovered drugs" have so far received regulatory approval. Here we assess one of the latest AI-based tools in this domain. Boltz-2, a recently devel...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A Computational and Statistical Framework Leveraging AI-Derived CT Phenotypes for Causal Mediation Effects Between Genetic Variants and Disease](https://www.medrxiv.org/content/10.64898/2026.08.05.26359812v1)
  来源：medRxiv | 日期：2026-08-10 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：As the costs of genetic sequencing continue to drop and human genomic biobanks grow in scale, the challenge in genomics has shifted increasingly towards disentangling whether and how associated genetic variants cause dis...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Self-evolving Agentic Customer Support System at LinkedIn](http://arxiv.org/abs/2608.10224v1)
  来源：arXiv | 日期：2026-08-10 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Enterprise support agents operate in rapidly changing environments where policies, product capabilities, and knowledge bases evolve continuously, making static assistants brittle and costly to maintain. We present Linked...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [TreeHop: Efficient Embedding-Level Query Rewriter](http://arxiv.org/abs/2504.20114v3)
  来源：arXiv | 日期：2025-04-28 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) systems face significant challenges in multi-hop question answering (MHQA), where complex queries require synthesizing information across multiple document chunks. Existing approaches...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Most biomedical publications show signs of LLM-assisted writing](http://arxiv.org/abs/2608.10715v1)
  来源：arXiv | 日期：2026-08-11 | 相关度：0.7 | 新颖度：6.26
  匹配主题：未命中具体主题
  中文摘要：Over the past several years, LLM-powered chatbots and agents have become widely used as a tool for academic writing. LLM-assisted writing can be valuable by removing language barriers but at the same time causes concerns...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A case study of evaluating AI agents on a neuroscience data-to-discovery pipeline](http://arxiv.org/abs/2606.07718v2)
  来源：arXiv | 日期：2026-06-05 | 相关度：0.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Agentic AI offers a promising path to automating software development bottlenecks in scientific research pipelines, particularly for stages that take domain experts days to months to build and where correctness and robus...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SAKE: Structured Agentic Knowledge Extrapolation for Complex LLM Reasoning via Reinforcement Learning](http://arxiv.org/abs/2505.15062v5)
  来源：arXiv | 日期：2025-05-21 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Knowledge extrapolation is the process of inferring novel information by combining and extending existing knowledge that is explicitly available. It is essential for solving complex questions in specialized domains where...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [PreGress: Ranking-Native Pre-training and Prompting for Graph Node Ranking](http://arxiv.org/abs/2608.09016v1)
  来源：arXiv | 日期：2026-08-10 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Node ranking is a fundamental problem in graph information retrieval, measuring the relative importance of nodes and supporting a wide range of applications such as influence analysis, recommendation, and graph-based ret...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AkasicDB: Demonstrating Omni RAG with a Unified Vector-Graph-Relational DBMS](http://arxiv.org/abs/2608.09214v1)
  来源：arXiv | 日期：2026-08-10 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Recent Retrieval-Augmented Generation (RAG) systems increasingly combine vector retrieval with structured knowledge, such as Graph RAG and Filtered vector search. However, existing database architectures struggle to supp...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [VeriForge: Mitigating Latent Knowledge Gaps in Narrative Drafting via Mixed-Initiative Scaffolding](http://arxiv.org/abs/2608.09698v1)
  来源：arXiv | 日期：2026-08-10 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Great fiction earns its verisimilitude through precise details, from how a longsword is gripped to pierce armor gaps to why a bleeding corpse cannot yet smell of decay, weaving domain expertise into the fabric of invente...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Protective effects of testosterone replacement therapy on brain tumor outcomes: the Mayo Clinic Experience](https://www.medrxiv.org/content/10.64898/2026.08.07.26359970v1)
  来源：medRxiv | 日期：2026-08-10 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：BackgroundBiological sex and endocrine signaling influence cancer biology, immune response, and therapeutic outcomes. Recent evidence suggests that testosterone signaling may exert brain-context-dependent protective effe...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [A single-patient task exposes a failure of safety alignment in clinical language models](https://www.medrxiv.org/content/10.64898/2026.08.07.26359822v1)
  来源：medRxiv | 日期：2026-08-10 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Safety alignment should persist while a language model performs a task. We tested whether a single-patient triage task suppressed a warning about a second patient. Each case centered on Patient 1; Patient 2's urgent prob...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [AI-based multimodal integration of genomics and electronic health records.](https://pubmed.ncbi.nlm.nih.gov/42576006/)
  来源：PubMed | 日期：2026-08-10 | 相关度：3.75 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：The widespread adoption of electronic health records (EHRs), which capture patient-specific longitudinal information on diagnoses, laboratory tests, clinical procedures, and outcomes, has created unprecedented opportunit...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [A software package for simple and rigorous survival machine learning analysis in biomedical research](https://www.medrxiv.org/content/10.64898/2026.08.05.26359034v1)
  来源：medRxiv | 日期：2026-08-10 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Survival analysis is a fundamental technique in biomedical research for modeling time-to-event data. It enables the identification of prognostic factors in disease, compares survival outcomes across treatment groups, and...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Precision Medicine in Transfusion-Dependent and Non-Transfusion-Dependent β-Thalassemia: Toward Personalized Diagnosis and Therapy.](https://pubmed.ncbi.nlm.nih.gov/42572810/)
  来源：PubMed | 日期：2026-08-10 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：β-thalassemia comprises a clinically heterogeneous group of disorders in which anemia severity, transfusion exposure, iron loading, and organ complications vary widely among individuals. This structured narrative review ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial intelligence in pediatric medical genetics and genomics.](https://pubmed.ncbi.nlm.nih.gov/42516066/)
  来源：PubMed | 日期：2026-08-11 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：人工智能（AI）正迅速且不均衡地融入医学及社会各领域。本综述重点探讨了 AI 在儿科基因组学领域的最新进展。文章阐述了 AI 及其子类型的通用定义，并介绍了最新的 AI 应用。随后，文章概述了 AI 在儿科基因组学多个环节的应用与测试，包括：识别潜在遗传病患者并辅助诊断过程；在实验室遗传检测流程中的实施；以及 AI 如何支持患者管理、新药发现及遗传病治疗研究。总体而言，AI 正以多种方式应用于儿科基因组学，该领域将因 AI 发生剧变。本...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [RAG-Audio: Retrieval-Augmented Generation for Faithful Brain-to-Audio Reconstruction](http://arxiv.org/abs/2608.09331v1)
  来源：arXiv | 日期：2026-08-10 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Brain-to-audio reconstruction is limited by \emph{prior domination}: when a pretrained generator is conditioned on a weak neural signal, it produces realistic but stimulus-inaccurate audio. We introduce RAG-Audio, which ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [FlippedRAG: Black-Box Opinion Manipulation Adversarial Attacks to Retrieval-Augmented Generation Models](http://arxiv.org/abs/2501.02968v7)
  来源：arXiv | 日期：2025-01-06 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) enriches LLMs by dynamically retrieving external knowledge, reducing hallucinations and satisfying real-time information needs. While existing research mainly targets RAG's performanc...
  为什么值得看：FlippedRAG: Black-Box Opinion Manipulati 与你的主题有弱匹配，暂时保留作低优先级跟踪。
