# 每日论文监控日报 (2026-07-02)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 81 篇新论文。

## 抓取状态

- arXiv：成功，命中 58 篇
- PubMed：成功，命中 200 篇
- bioRxiv：成功，命中 14 篇
- medRxiv：成功，命中 14 篇

## 最值得看

### Foundation Model / Agent

- [ClinRAG-GRAPH: Clinical-prior Retrieval-Augmented Graph Model with Domain Adversarial Learning for Breast pCR Prediction](http://arxiv.org/abs/2607.00798v1)
  来源：arXiv | 日期：2026-07-01 | 相关度：8.9 | 新颖度：7.26
  匹配主题：foundation_model_agent
  中文摘要：Neoadjuvant chemotherapy (NAC) response prediction is clinically important for treatment stratification in breast cancer. However, robust pre-treatment pathological complete response (pCR) prediction remains challenging ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Towards Developing a Multimodal Chat Assistant for University Stakeholders: RAG-based Approach](http://arxiv.org/abs/2607.01115v1)
  来源：arXiv | 日期：2026-07-01 | 相关度：7.9 | 新颖度：7.82
  匹配主题：foundation_model_agent
  中文摘要：University stakeholders often face difficulties in accessing timely and reliable information, especially in developing countries, where there are very few intelligent support systems. Existing rule-based chatbots are una...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MolSafeEval: A Benchmark for Uncovering Safety Risks in AI-Generated Molecules](http://arxiv.org/abs/2607.00464v1)
  来源：arXiv | 日期：2026-07-01 | 相关度：7.55 | 新颖度：7.07
  匹配主题：foundation_model_agent
  中文摘要：Current molecular generation benchmarks emphasize task complexity, molecule novelty, and property alignment; they largely overlook a critical concern: the potential safety risks of AI-generated molecules. In practice, ma...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [M2Note: Continual Evolution of Vision Language Models via Mistake Notebook Learning](http://arxiv.org/abs/2607.00685v1)
  来源：arXiv | 日期：2026-07-01 | 相关度：7.5 | 新颖度：6.98
  匹配主题：foundation_model_agent
  中文摘要：Vision Language Models (VLMs) have demonstrated remarkable capabilities in multimodal reasoning tasks, yet they still suffer from recurring failures, such as skipping key visual checks, misapplying domain rules, and hall...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [RareDxR1: Autonomous Medical Reasoning for Rare Disease Diagnosis Beyond Human Annotation](http://arxiv.org/abs/2607.00147v1)
  来源：arXiv | 日期：2026-06-30 | 相关度：7.55 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：Rare disease differential diagnosis is a critical yet arduous clinical task, requiring physicians to identify precise phenotypes from complex, unstructured patient symptoms and execute intricate reasoning within a vast s...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Integrating Semantic Retrieval, LLM-based Refinement, and Structured Expert Curation for Scalable AOP Gene Mapping](https://www.biorxiv.org/content/10.64898/2026.06.25.734475v1)
  来源：bioRxiv | 日期：2026-06-30 | 相关度：7.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Toxicogenomics can support regulatory toxicology, but its use is limited by the difficulty of translating molecular responses into mechanistic, decision-relevant interpretations. Adverse Outcome Pathways (AOPs) provide a...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Artificial intelligence for child health: current capabilities and the next frontier.](https://pubmed.ncbi.nlm.nih.gov/42386397/)
  来源：PubMed | 日期：2026-07-01 | 相关度：8.5 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence (AI) is reshaping paediatric healthcare, offering new capabilities across diagnosis, monitoring and treatment personalisation. Modern AI systems integrate multimodal data, including imaging, genom...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 可追踪

### Foundation Model / Agent

- [GeoPep: A Geometry-Aware Masked Language Model for Protein-Peptide Binding Site Prediction.](https://pubmed.ncbi.nlm.nih.gov/42367058/)
  来源：PubMed | 日期：2026-06-29 | 相关度：10.0 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Multimodal approaches that integrate protein structure and sequence have achieved remarkable success in protein-protein interface prediction. However, extending these methods to protein-peptide interactions remains chall...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Clinical-Grade Somatic Variant Interpretation Performance via a Rule-Constrained Large Language Model Framework (Oncology Logic-Informed Variant Evaluator).](https://pubmed.ncbi.nlm.nih.gov/42031331/)
  来源：PubMed | 日期：2026-07-01 | 相关度：10.0 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent, application_monitoring
  中文摘要：Interpretation of somatic variants in clinical oncology requires integration of gene-specific biology, tumor context, and multiple evidence sources. Although large language models (LLMs) can assist variant interpretation...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [How Post-Training Shapes Biological Reasoning Models](http://arxiv.org/abs/2606.16517v2)
  来源：arXiv | 日期：2026-06-15 | 相关度：7.8 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Scientific reasoning models for biology combine language models with foundation models trained on multimodal biological data, including DNA, RNA, and proteins. These models are built through post-training, yet how each s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AI as a signal assessor - Can a Large Language Model perform causality assessment on a case series?](https://www.medrxiv.org/content/10.64898/2026.06.26.26356656v1)
  来源：medRxiv | 日期：2026-06-29 | 相关度：7.55 | 新颖度：1.2
  匹配主题：foundation_model_agent
  中文摘要：BackgroundLarge Language Models (LLMs) are increasingly explored for pharmacovigilance tasks, including information extraction, case documentation, and single-case causality assessment. However, their ability to support ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PHO-Agents: A Large Language Model Powered Multi-Agent System for Predicting Health Outcomes](https://www.medrxiv.org/content/10.64898/2026.06.19.26355815v1)
  来源：medRxiv | 日期：2026-06-29 | 相关度：7.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：ObjectivePredicting health outcomes from electronic health records (EHRs) is challenging because traditional models rely on structured data and often ignore external medical knowledge. We propose an approach that integra...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RASR: Retrieval-Augmented Semantic Reasoning for Fake News Video Detection](http://arxiv.org/abs/2604.06687v2)
  来源：arXiv | 日期：2026-04-08 | 相关度：7.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Multimodal fake news video detection is a crucial research direction for maintaining the credibility of online information. Existing studies primarily verify content authenticity by constructing multimodal feature fusion...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ManimAgent: Self-Evolving Multimodal Agents for Visual Education](http://arxiv.org/abs/2606.30296v2)
  来源：arXiv | 日期：2026-06-29 | 相关度：6.8 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Multi-round reflection lets agents built on large language models recover from failures within a single task, but each task remains an isolated episode: lessons learned across many reflection rounds on one task are disca...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Large-Language-Model Supported Personalized Driving Framework for Lane Change in Highway Scenarios](http://arxiv.org/abs/2606.31483v2)
  来源：arXiv | 日期：2026-06-30 | 相关度：6.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Personalized driving can improve the user acceptance of automated driving systems. However, existing methods still provide limited support for translating natural-language driving preferences, especially when such prefer...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [CORTEX: Token-Level Hallucination Detection in RAG via Comparative Internal Representations](http://arxiv.org/abs/2606.31033v1)
  来源：arXiv | 日期：2026-06-30 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：In this paper, we propose CORTEX, a token-level hallucination detection method for Retrieval-Augmented Generation (RAG). In long-form RAG outputs, hallucinations often arise in localized spans rather than throughout an e...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Cross-LLM AI platform meta-research: Non-inferiority of bovine milk-based fortifiers to human milk-based fortifiers](https://www.medrxiv.org/content/10.64898/2026.06.24.26356426v1)
  来源：medRxiv | 日期：2026-06-29 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Necrotizing enterocolitis (NEC), frequently resulting in sepsis, is among the leading causes of morbidity and mortality of pre-term newborns. However, diagnostic and therapeutic strategies for NEC and sepsis are still li...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OHCA-EXTRACT: Evaluating the Accuracy of a Large Language Model Pipeline for Out-of-Hospital Cardiac Arrest Case Identification and Utstein Variable Extraction](https://www.medrxiv.org/content/10.64898/2026.06.29.26356890v1)
  来源：medRxiv | 日期：2026-07-01 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Background: Manual identification and abstraction of out-of-hospital cardiac arrest (OHCA) cases and Utstein template variables from electronic health records is resource-intensive and limits scalable measurement for obs...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond Document Grounding: Span-Level Hallucination Detection over Code, Tool Output, and Documents](http://arxiv.org/abs/2607.00895v1)
  来源：arXiv | 日期：2026-07-01 | 相关度：5.45 | 新颖度：7.82
  匹配主题：foundation_model_agent
  中文摘要：Hallucination detection for retrieval-augmented generation (RAG) is usually evaluated on natural-language document evidence. However, grounded generation systems increasingly rely on structured inputs: source code, devel...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AGE: Adaptive-masking for Graph Embedding in Graph Retrieval-Augmented Generation](http://arxiv.org/abs/2607.00052v1)
  来源：arXiv | 日期：2026-06-30 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：GraphRAG is an extension of retrieval-augmented generation (RAG) that supports large language models (LLMs) by referring to graph-structured data as external knowledge. While this technique ideally captures intricate rel...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The Illusion of Agentic Complexity in README.md Generation: Evaluating Single-Agent vs. Multi-Agent RAG Systems](http://arxiv.org/abs/2606.30524v2)
  来源：arXiv | 日期：2026-06-29 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) are increasingly utilized to automate several software engineering tasks, including code completion, code summarization, testing, and the generation of repository-level documentation. While M...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [When RAG Meets Query Planning: Logical Query Trees for Resolving Exploratory Reasoning Problems](http://arxiv.org/abs/2607.00508v1)
  来源：arXiv | 日期：2026-07-01 | 相关度：4.75 | 新颖度：6.02
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) effectively grounds large language models (LLMs) in external knowledge but struggles with \textbf{exploratory reasoning problems (ERPs)} that are the complex queries involving high un...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Precision Grounding: augmenting large language models with evidence-based databases for trustworthy genetic variant summarization.](https://pubmed.ncbi.nlm.nih.gov/41950627/)
  来源：PubMed | 日期：2026-07-01 | 相关度：9.1 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：To propose a novel method that augments LLMs with evidence-based, variant-specific information to improve summarization accuracy and support clinical decision making. We proposed Precision Grounding which uses a query to...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Advances in rapid microbiological testing for animal diseases: A review.](https://pubmed.ncbi.nlm.nih.gov/42217635/)
  来源：PubMed | 日期：2026-07-01 | 相关度：8.6 | 新颖度：1.25
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：Animal pathogenic microorganisms destabilize livestock economies and jeopardize human health through zoonotic transmission and foodborne illness. Traditional culture-based detection methods, while standardized, are time-...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [EpiCity: An AI-Enabled Epidemic-Aware Smart City Health Intelligence Framework for Sustainable Urban Planning](https://www.medrxiv.org/content/10.64898/2026.06.29.26356899v1)
  来源：medRxiv | 日期：2026-07-01 | 相关度：6.2 | 新颖度：5.5
  匹配主题：foundation_model_agent, application_monitoring
  中文摘要：Urban centres across the world remain structurally unprepared for epidemic events, lacking the real-time intelligence infrastructure needed to anticipate outbreaks, model population-level spread, and evaluate competing h...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Engineering phage endolysins and receptor-binding proteins for foodborne pathogen control and detection: A review and AI-driven framework.](https://pubmed.ncbi.nlm.nih.gov/42001688/)
  来源：PubMed | 日期：2026-07-02 | 相关度：2.65 | 新颖度：8.4
  匹配主题：sequencing_bioinformatics
  中文摘要：Antimicrobial resistance exacerbates food safety risks, highlighting the need for novel, matrix-tolerant control and detection tools. Phage-derived endolysins and receptor-binding proteins (RBPs) offer high specificity, ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Generative Artificial Intelligence and Large Language Models in Clinical Oncology.](https://pubmed.ncbi.nlm.nih.gov/42358410/)
  来源：PubMed | 日期：2026-07-01 | 相关度：8.5 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Cancer remains a major global health challenge, and the increasing availability of multimodal biomedical data has created unprecedented opportunities for precision oncology. Recent advances in generative artificial intel...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial intelligence (AI)-assisted diagnosis of skin diseases: From image classification to dermatology-specific multimodal clinical reasoning.](https://pubmed.ncbi.nlm.nih.gov/42368306/)
  来源：PubMed | 日期：2026-06-30 | 相关度：7.8 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence (AI) in dermatology has moved beyond the early paradigm of single-image classification. Dermatological diagnosis is achieved based on morphology, distribution, symptoms, tactile findings, temporal...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial intelligence in clinical oncology: Multimodal integration and translational development.](https://pubmed.ncbi.nlm.nih.gov/41962624/)
  来源：PubMed | 日期：2026-07-01 | 相关度：7.8 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence (AI) is rapidly reshaping clinical oncology, as cancer care increasingly relies on integrating heterogeneous data streams spanning radiology, digital pathology, genomics, and longitudinal electron...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [InfoFlow KV: Information-Flow-Aware KV Recomputation for Long Context](http://arxiv.org/abs/2603.05353v2)
  来源：arXiv | 日期：2026-03-05 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) for long-context question answering is bottlenecked by inference-time prefilling over large retrieved contexts. A common strategy is to precompute key-value (KV) caches for individual...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Infoxmed2.0-27B: Instruction Tuning, Preference Alignment, and GRPO-Based Reward Model Training for Medical LLMs](https://www.medrxiv.org/content/10.64898/2026.06.25.26356522v1)
  来源：medRxiv | 日期：2026-06-30 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Abstract-Large language models (LLMs) [1], [2] have demon strated remarkable capabilities across general domains, yet their application in specialized medical contexts demands rigorous domain adaptation [3], [4]. We pres...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Protein contacts are already in the attention: a single-forward-pass alternative to the Categorical Jacobian](http://arxiv.org/abs/2606.21876v2)
  来源：arXiv | 日期：2026-06-20 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：The Categorical Jacobian of Zhang et al. (2024) reads protein contacts from a language model by perturbing every residue with every alternative amino acid, about $19L$ forward passes. We show the signal it reconstructs i...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Field-Deployable Risk Stratification of Pathogens via an AI-Integrated Nanozyme Sensor.](https://pubmed.ncbi.nlm.nih.gov/42301193/)
  来源：PubMed | 日期：2026-06-30 | 相关度：5.5 | 新颖度：0.5
  匹配主题：pathogenomics, foundation_model_agent, application_monitoring
  中文摘要：Pathogen surveillance in complex environmental matrices requires analytical methods that are sensitive, robust, and suitable for field deployment. Here, we report a geometry-engineered trimetallic PdPtRu nanozyme-enabled...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SAGE: A Search-AuGmented Evaluation of Large Language Models on Free-Form QA](http://arxiv.org/abs/2504.07385v3)
  来源：arXiv | 日期：2025-04-10 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：As Large Language Models (LLMs) become increasingly used for question-answering (QA), relying on static, pre-annotated references for evaluation poses significant challenges in cost, scalability, and completeness. Meanwh...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ThunderAgent: A Simple, Fast and Program-Aware Agentic Inference System](http://arxiv.org/abs/2602.13692v3)
  来源：arXiv | 日期：2026-02-14 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models(LLMs) are now used to power complex multi-turn agentic workflows. Existing systems run agentic inference by loosely assembling isolated components: an LLM inference engine (e.g., vLLM) and a tool or...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BayesEvolve: Explicit Belief States for Autonomous Scientific Discovery](http://arxiv.org/abs/2606.30335v1)
  来源：arXiv | 日期：2026-06-29 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Autonomous scientific discovery systems increasingly use large language models (LLMs) to propose new hypotheses, but many such systems condition primarily on experimental memory: archives of high-scoring candidates or he...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [An APOC1+ inflammatory CAF-like state drives a senescent, treatment-resistant niche in rheumatoid arthritis](https://www.biorxiv.org/content/10.64898/2026.04.17.718831v5)
  来源：bioRxiv | 日期：2026-06-29 | 相关度：3.05 | 新颖度：0.25
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：Objectives: Rheumatoid arthritis (RA) synovitis frequently persists despite cytokine-targeted therapies, suggesting the existence of pathogenic stromal programs that sustain chronic inflammation independently of canonica...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Machine Learning Predicts Hepatocellular Carcinoma Risk from Routine Clinical Data: A Large Population-Based Multicentric Study.](https://pubmed.ncbi.nlm.nih.gov/41881847/)
  来源：PubMed | 日期：2026-07-01 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：肝细胞癌（HCC）是一种高致死性肿瘤，其风险分层对预后至关重要但仍具挑战。本研究开发了一个基于常规临床数据的可解释机器学习框架 PRE-Screen-HCC。研究利用了来自两个大规模队列（UK Biobank 用于模型开发，All of Us 研究计划用于外部测试）的 900,000 多名受试者和 983 例 HCC 病例的前瞻性多模态数据。研究评估了人口统计学、生活方式、健康记录、血液指标、基因组学和代谢组学等数据模态的个体与累积贡献...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Human-Agent Collaborative Paper-to-Page Crafting](http://arxiv.org/abs/2510.19600v2)
  来源：arXiv | 日期：2025-10-22 | 相关度：2.1 | 新颖度：1.75
  匹配主题：未命中具体主题
  中文摘要：In the quest for scientific progress, communicating research is as vital as the discovery itself. Yet, researchers are often sidetracked by the manual, repetitive chore of building project webpages to make their dense pa...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The Calibration Turn in AI-Assisted Research: A Conceptual and Methodological Framework for Evidence-Licensed Claims](http://arxiv.org/abs/2606.31273v1)
  来源：arXiv | 日期：2026-06-30 | 相关度：2.1 | 新颖度：1.75
  匹配主题：未命中具体主题
  中文摘要：AI-assisted research has entered a stage in which the central question is not only whether systems can generate hypotheses, run experiments, or produce manuscripts, but whether their scientific claims are calibrated to t...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Accelerometry-Derived Digital Biomarkers for Cardiometabolic Risk: A Population-Representative Tabular Benchmark with Uncertainty Quantification](http://arxiv.org/abs/2606.30702v1)
  来源：arXiv | 日期：2026-06-29 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Structured tabular data dominates clinical medicine, yet existing benchmarks fail to reflect real-world properties like complex survey sampling, demographic oversampling, and subgroup fairness. We introduce the NHANES Ac...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [GeneBench-Pro: Evaluating Multistage Statistical Reasoning\\in Genomics, Quantitative Biology, and Translational Biomedicine](https://www.biorxiv.org/content/10.64898/2026.06.29.735386v1)
  来源：bioRxiv | 日期：2026-06-30 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：We introduce GeneBench-Pro, an expanded and improved version of GeneBench that comprises harder problems across a wider breadth of domains. GeneBench-Pro is a benchmark for AI agents performing realistic multi-stage scie...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Continuous Knowledge Metabolism: Generating Scientific Hypotheses from Evolving Literature](http://arxiv.org/abs/2604.12243v2)
  来源：arXiv | 日期：2026-04-14 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Identifying promising research directions in fast-moving subareas is one of the most cognitively expensive tasks in modern AI research. Existing LLM-driven scientific discovery systems are typically limited to one-shot p...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [KidnapRAG: A Black-Box Attack for Hijacking Reasoning in Agentic Retrieval-Augmented Generation Systems](http://arxiv.org/abs/2607.00422v1)
  来源：arXiv | 日期：2026-07-01 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) systems are vulnerable to poisoning attacks that inject malicious documents into the retrieval process to manipulate model outputs. Recent Agentic RAG systems are more robust to such ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Minos: A Multi-Agent Collaborative Framework for Provenance-Based Backward Tracking](http://arxiv.org/abs/2607.00440v1)
  来源：arXiv | 日期：2026-07-01 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Sophisticated cyber attacks, particularly Advanced Persistent Threats (APTs), require effective post-intrusion forensic analysis. Provenance-based backward tracking reconstructs attack scenarios by tracing causality from...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Diagnosing and Mitigating Compounding Failures in Agentic Persuasion via Taxonomic Strategy Retrieval](http://arxiv.org/abs/2606.24976v2)
  来源：arXiv | 日期：2026-06-23 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Foundation-model agents in multi-step, open-ended environments frequently suffer from compounding errors, where early mistakes contaminate long-horizon trajectories. While Multi-Agent Debate (MAD) succeeds in determinist...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [RARE: Redundancy-Aware Retrieval Evaluation Framework for High-Similarity Corpora](http://arxiv.org/abs/2604.19047v2)
  来源：arXiv | 日期：2026-04-21 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Existing QA benchmarks typically assume distinct documents with minimal overlap, yet real-world retrieval-augmented generation (RAG) systems operate on corpora such as financial reports, legal codes, and patents, where i...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DDIAgents: Mechanism-Conditioned Context Flow for Drug-Drug Interaction Prediction](http://arxiv.org/abs/2606.31085v1)
  来源：arXiv | 日期：2026-06-30 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Drug-drug interaction (DDI) prediction is essential for medication safety, yet it requires reasoning over heterogeneous biomedical evidence whose relevance changes across interaction mechanisms. We propose DDIAgents, a m...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Accelerating scientific discovery with Co-Scientist](http://arxiv.org/abs/2502.18864v2)
  来源：arXiv | 日期：2025-02-26 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Scientific discovery is driven by scientists generating novel hypotheses for complex problems that undergo rigorous experimental validation. To augment this process, we introduce Co-Scientist, a multi-agent AI system bui...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Knowledge Graphs as the Missing Data Layer for LLM-Based Industrial Asset Operations](http://arxiv.org/abs/2605.26874v3)
  来源：arXiv | 日期：2026-05-26 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：LLM-based agents for industrial asset operations show limited accuracy when reasoning over flat document stores. AssetOpsBench (KDD 2026) establishes that GPT-4 agents achieve 65% on 139 industrial maintenance scenarios,...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Structure-Regularized Interpretable TCR-Epitope Prediction](http://arxiv.org/abs/2606.30902v1)
  来源：arXiv | 日期：2026-06-29 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：T cell receptor (TCR)-epitope binding prediction is essential for understanding adaptive immunity and developing immunotherapies. Existing sequence- and structure-based models often generalize poorly to unseen epitopes a...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Pep2Mol: 3D Molecule Generation Targeting Protein-Protein Interfaces with Diffusion Models](https://www.biorxiv.org/content/10.64898/2026.06.28.734975v1)
  来源：bioRxiv | 日期：2026-06-29 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Protein-protein interactions (PPIs) are central to biological processes. Designing small molecules that modulate dysregulated PPIs holds strong promise for targeting undruggable proteins. However, existing structure-base...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Dual-Confidence Contrastive Decoding for Retrieval-Augmented Generation](http://arxiv.org/abs/2607.00570v1)
  来源：arXiv | 日期：2026-07-01 | 相关度：0.7 | 新颖度：6.22
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) increasingly requires models to answer questions from multiple retrieved documents, where only some sources are relevant and the retrieved bundle may contain stale, noisy, or conflict...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators](http://arxiv.org/abs/2606.26294v2)
  来源：arXiv | 日期：2026-06-24 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Self-improving agents are state-of-the-art (SOTA) on agentic coding benchmarks and have recently been extended to general domains. However, their search methods generally assume a stationary evaluation criterion: a fixed...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [A transformer-based language model reveals developmental constraint and network complexity during zebrafish embryogenesis.](https://pubmed.ncbi.nlm.nih.gov/42376282/)
  来源：PubMed | 日期：2026-07-01 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Understanding how regulatory complexity and constraint shape organismal development remains a central challenge in biology. The developmental hourglass framework posits that mid-embryogenesis-the phylotypic stage-is a pe...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Rank-aware agglomeration of foundation models for immunohistochemistry image cell counting.](https://pubmed.ncbi.nlm.nih.gov/42140101/)
  来源：PubMed | 日期：2026-07-01 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Accurate cell counting in immunohistochemistry (IHC) images is critical for quantifying protein expression and aiding cancer diagnosis. However, the task remains challenging due to the chromogen overlap, variable biomark...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SysVCoder: An LLM-Driven Framework for Systematic Generation of System-Level Design](http://arxiv.org/abs/2504.20653v3)
  来源：arXiv | 日期：2025-04-29 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in large language models (LLMs) have demonstrated strong potential in generating hardware designs using hardware description languages (HDLs) such as Verilog. However, existing LLM-based frameworks strugg...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Rethinking On-policy Optimization for Query Augmentation](http://arxiv.org/abs/2510.17139v3)
  来源：arXiv | 日期：2025-10-20 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in large language models (LLMs) have led to a surge of interest in query augmentation for information retrieval (IR). Two main approaches have emerged. The first prompts LLMs to generate answers or pseudo...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Regime-Aware Peer Specialization for Robust RAG under Heterogeneous Knowledge Conflicts](http://arxiv.org/abs/2606.30518v1)
  来源：arXiv | 日期：2026-06-29 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) improves language models by grounding generation in external context. However, it can be fragile when the retrieved context conflicts with the model's parametric knowledge. Such confl...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GUIDE: Resolving Domain Bias in GUI Agents through Real-Time Web Video Retrieval and Plug-and-Play Annotation](http://arxiv.org/abs/2603.26266v3)
  来源：arXiv | 日期：2026-03-27 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Large vision-language models have endowed GUI agents with strong general capabilities for interface understanding and interaction. However, due to insufficient exposure to domain-specific software operation data during t...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [OpenGerminal: an open-source implementation of the Germinal antibody design pipeline](https://www.biorxiv.org/content/10.64898/2026.06.25.734527v1)
  来源：bioRxiv | 日期：2026-06-29 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Germinal is a recently described computational pipeline for de novo antibody design that combines AlphaFold-Multimer hallucination with antibody language model guidance to generate epitope-targeted antibodies. Germinal i...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Agentic RAG-VLM: Affordance-Aware Retrieval-Augmented Generation with Self-Reflective Planning for Robotic Grasping](http://arxiv.org/abs/2606.31200v1)
  来源：arXiv | 日期：2026-06-30 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Generalizable robotic grasping in cluttered environments is essential for deploying manipulators in unstructured human spaces, yet existing VLM-based methods rely on visual similarity for object matching, neglecting phys...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AdaTrans: Automated C to Rust Transformation via Error-Adaptive Repair](http://arxiv.org/abs/2606.31706v1)
  来源：arXiv | 日期：2026-06-30 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：The automated transformation of C code to Rust is challenging due to Rust's strict ownership and borrowing semantics. While Large Language Models (LLMs) show promise, they often produce code that violates these rules or ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Data-Efficient Multimodal Alignment for Histopathology-based Molecular Prediction](http://arxiv.org/abs/2606.29949v1)
  来源：arXiv | 日期：2026-06-29 | 相关度：3.05 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：H&E-stained whole-slide images offer cohort-scale availability and rich spatial context but lack molecular specificity, whereas bulk RNA-seq provides transcriptome-wide resolution at high cost with limited archival avail...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Building artificial intelligence virtual tissue (AIVT) for tissue state representation, feature prediction, and dynamic simulation](http://arxiv.org/abs/2606.29883v1)
  来源：arXiv | 日期：2026-06-29 | 相关度：2.75 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Modeling tissue states and their transitions is essential for understanding tissue homeostasis in health and pathological remodeling in disease. However, conventional computational modeling approaches are inadequate to c...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Enhancing Title and Abstract Priority Screening Through SimEd AI Pipeline.](https://www.medrxiv.org/content/10.64898/2026.06.26.26356718v1)
  来源：medRxiv | 日期：2026-06-30 | 相关度：2.1 | 新颖度：1.75
  匹配主题：未命中具体主题
  中文摘要：The exhaustive identification of evidence is central to systematic reviews, but the screening of titles and abstracts remains particularly labor intensive. Priority screening, an active learning approach that ranks recor...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Agentic-Ideation: Sample Efficient Agentic Trajectories Synthesis for Scientific Ideation Agents](http://arxiv.org/abs/2606.31229v1)
  来源：arXiv | 日期：2026-06-30 | 相关度：2.1 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Ideation plays a pivotal role in scientific discovery. Recent LLM, especially AI Scientist systems, show promising potential for automated ideation. However, existing approaches predominantly rely on pre-defined agentic ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [BulkFormer: A large-scale foundation model for bulk transcriptomes.](https://pubmed.ncbi.nlm.nih.gov/42385705/)
  来源：PubMed | 日期：2026-07-01 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Foundation models are transforming transcriptome analysis, yet most RNA sequencing (RNA-seq) foundation models are pretrained on sparse single-cell RNA-seq data, which typically captures only ∼3,000 genes per cell. This ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Can Tabular In-Context Learners Generalize to Biomolecular Property Prediction?](http://arxiv.org/abs/2606.31126v1)
  来源：arXiv | 日期：2026-06-30 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Predicting biomolecular properties from limited labeled data is a central bottleneck in protein engineering and small-molecule design. As strong pretrained encoders now supply rich fixed-length representations, the diffi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Integrating stemness and epithelial-mesenchymal transition signatures with machine learning identifies RUNX1 as a therapeutic vulnerability in colorectal cancer.](https://pubmed.ncbi.nlm.nih.gov/42372471/)
  来源：PubMed | 日期：2026-06-29 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Colorectal cancer (CC) arises from a complex interplay between genetic and epigenetic alterations within the colorectal mucosa, resulting in unchecked cellular proliferation and tumor development. This complexity results...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Linkify: Learning from Interface-Augmented Assembly Graphs](http://arxiv.org/abs/2607.01205v1)
  来源：arXiv | 日期：2026-07-01 | 相关度：1.4 | 新颖度：8.11
  匹配主题：未命中具体主题
  中文摘要：We present Linkify, a framework for learning from interface-augmented assembly graphs to enable context-aware part retrieval in mechanical assemblies. While recent generative AI methods for CAD have focused largely on is...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Bayesian Uncertainty Propagation for Agentic RAG Pipelines: A Proof-of-Concept Study on Multi-Hop Question Answering](http://arxiv.org/abs/2607.00972v1)
  来源：arXiv | 日期：2026-07-01 | 相关度：0.7 | 新颖度：6.75
  匹配主题：未命中具体主题
  中文摘要：Trustworthy deployment of Agentic Retrieval-Augmented Generation (RAG) systems requires mechanisms for estimating when multi-stage reasoning pipelines may fail. This paper presents an uncertainty-aware Agentic Retrieval-...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Decoding viral evolution through integrative bioinformatics: From genomes to global health.](https://pubmed.ncbi.nlm.nih.gov/42035616/)
  来源：PubMed | 日期：2026-07-01 | 相关度：6.55 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Bioinformatics has transformed modern virology by linking genomic variation to epidemiology, protein structure, and public health action. This review integrates core analytical frameworks-sequence alignment and genome an...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Large language models for cancer registry abstraction: a real-world evaluation across models, variables, and cancer types](https://www.medrxiv.org/content/10.64898/2026.06.25.26356626v1)
  来源：medRxiv | 日期：2026-06-29 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Cancer registries enable cancer surveillance at the population level. These registries require significant human-time to read through many different parts of the electronic health record, including structured data and le...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Advancing AI for multi-omics and clinical data integration in basic and translational cancer research.](https://pubmed.ncbi.nlm.nih.gov/42014628/)
  来源：PubMed | 日期：2026-07-01 | 相关度：3.75 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：The extensive heterogeneity of cancer across biological scales necessitates a holistic approach beyond single-analyte methods. Integrating multi-omics data - from genomics to proteomics - with multimodal information, suc...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [The double threat: bacterial and fungal co-/superinfection in viral pneumonia.](https://pubmed.ncbi.nlm.nih.gov/41653012/)
  来源：PubMed | 日期：2026-07-01 | 相关度：3.05 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Respiratory viral pneumonias are a leading cause of severe respiratory failure and intensive care unit (ICU) admission worldwide. Although viral infection itself drives significant morbidity and mortality, secondary bact...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [A comprehensive survey of AI agents in healthcare.](https://pubmed.ncbi.nlm.nih.gov/42009269/)
  来源：PubMed | 日期：2026-07-01 | 相关度：2.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：This survey aims to systematically map the rapidly evolving landscape of AI agents in healthcare. It addresses the critical need to adapt general-purpose agentic frameworks characterized by autonomy, planning, and tool u...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Integrating multi-omics and artificial intelligence for personalized breast cancer management: A guide to clinicians.](https://pubmed.ncbi.nlm.nih.gov/41936855/)
  来源：PubMed | 日期：2026-07-01 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Breast cancer's (BC) diverse nature and global impact demand tailored clinical strategies. Conventional screening methods often fall short in early detection and individualized risk assessment. By merging multi-omics tec...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Secondary prevention of recurrent ischemic stroke: from guidelines to precision medicine.](https://pubmed.ncbi.nlm.nih.gov/42374519/)
  来源：PubMed | 日期：2026-06-29 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Recurrent ischemic stroke remains a major global health challenge, accounting for substantial disability and mortality despite advances in acute management. Secondary prevention has undergone a fundamental paradigm shift...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Esketamine multi-omic biomarker evaluation in major depressive disorder (EMBER-MDD): concept, objectives and methodologies of a non-clinical investigator-initiated study.](https://pubmed.ncbi.nlm.nih.gov/42377483/)
  来源：PubMed | 日期：2026-06-30 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Treatment resistance (TR) in major depressive disorder (MDD) affects a substantial minority of patients and is hard to recognize early, delaying intensified care. The Esketamine multi-omic biomarker evaluation in MDD (EM...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [What Survives Into Context: A Diagnostic for Budget-Constrained Multi-Hop RAG and When Submodular Evidence Packing Improves It](http://arxiv.org/abs/2607.00725v1)
  来源：arXiv | 日期：2026-07-01 | 相关度：0.7 | 新颖度：6.1
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) under a fixed reader-context budget forces a selection problem: of the evidence retrieved, only a fraction can be shown to the reader. We argue that document recall -- the standard re...
  为什么值得看：What Survives Into Context: A Diagnostic 与你的主题有弱匹配，暂时保留作低优先级跟踪。
