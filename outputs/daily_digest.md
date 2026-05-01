# 每日论文监控日报 (2026-05-01)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 65 篇新论文。

## 抓取状态

- arXiv：成功，命中 47 篇
- PubMed：成功，命中 129 篇
- bioRxiv：成功，命中 16 篇
- medRxiv：成功，命中 15 篇

## 最值得看

### Foundation Model / Agent

- [DeepSeMS: revealing the hidden biosynthetic potential of the global ocean microbiome with a large language model.](https://pubmed.ncbi.nlm.nih.gov/42062603/)
  来源：PubMed | 日期：2026-04-30 | 相关度：8.15 | 新颖度：5.75
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：Microbial-derived secondary metabolites (SMs) hold great therapeutic potential but are predominantly discovered from cultured species, representing only a fraction of microbial biodiversity. Advances in metagenomics have...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Iterative Multimodal Retrieval-Augmented Generation for Medical Question Answering](http://arxiv.org/abs/2604.27724v1)
  来源：arXiv | 日期：2026-04-30 | 相关度：7.9 | 新颖度：7.56
  匹配主题：foundation_model_agent
  中文摘要：Medical retrieval-augmented generation (RAG) systems typically operate on text chunks extracted from biomedical literature, discarding the rich visual content (tables, figures, structured layouts) of original document pa...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Retrieval-Augmented Multimodal Model for Fake News Detection](http://arxiv.org/abs/2604.18112v2)
  来源：arXiv | 日期：2026-04-20 | 相关度：7.5 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：In recent years, multimodal multidomain fake news detection has garnered increasing attention. Nevertheless, this direction presents two significant challenges: (1) Failure to Capture Cross-Instance Narrative Consistency...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [Artificial Intelligence Agents in Mental Health: A Systematic Review and Meta Analysis](https://www.medrxiv.org/content/10.64898/2026.04.21.26351365v2)
  来源：medRxiv | 日期：2026-04-30 | 相关度：8.9 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：The rapid rise of large language models (LLMs) and foundation models has accelerated efforts to build artificial intelligence (AI) agents for mental health assessment, triage, psychotherapy support and clinical decision ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Multi-modal LLM-Knowledge Fusion Framework for Predicting Single-cell Genetic Perturbation Effects](https://www.biorxiv.org/content/10.64898/2026.04.24.720560v1)
  来源：bioRxiv | 日期：2026-04-28 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：理解细胞对基因扰动的反应是药物发现的基础，但实验方法在覆盖范围和成本上的局限阻碍了对细胞行为的全面绘制。为此，研究者开发了“虚拟细胞”计算模型，通过学习细胞状态与功能的关系来预测扰动后果。然而，现有方法在处理复杂基因相互作用、生物可解释性以及对未知基因的泛化能力方面存在不足。本研究提出 scPert，这是一个基于 Transformer 架构的多模态框架，整合了大语言模型（LLM）嵌入与结构化生物知识，用于预测单细胞转录组对基因扰动的响...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From simulation to pedagogy: structured AI standardized patients for clinical communication training validated through multi-model and randomized evaluation](https://www.medrxiv.org/content/10.64898/2026.04.26.26351793v1)
  来源：medRxiv | 日期：2026-04-28 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：标准化病人（SPs）是临床沟通培训的核心，但受限于高昂成本、可扩展性及对专业演员的依赖。本研究开发了由大语言模型（LLM）驱动的AI标准化病人（AI-SPs），其核心是采用三层信息架构，根据学习者的技能水平动态调节病情的披露程度。验证过程分为三个阶段：第一阶段通过对5个前沿LLM生成的350次模拟咨询进行专家盲评，结果显示学习者的技能水平对表现差异的影响（eta^2 = 0.31）显著高于模型选择（eta^2 = 0.06），证明教学质...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OptimusKG: Unifying biomedical knowledge in a modern multimodal graph](http://arxiv.org/abs/2604.27269v1)
  来源：arXiv | 日期：2026-04-29 | 相关度：7.1 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Biomedical knowledge graphs (KGs) are widely used in the life sciences, yet many are derived from unstructured documents and therefore lack schema-level constrains, whereas graphs assembled from structured resources are ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Mirage to Grounding: Towards Reliable Multimodal Circuit-to-Verilog Code Generation](http://arxiv.org/abs/2604.27969v1)
  来源：arXiv | 日期：2026-04-30 | 相关度：6.8 | 新颖度：7.18
  匹配主题：foundation_model_agent
  中文摘要：Multimodal large language models (MLLMs) are increasingly used to translate visual artifacts into code, from UI mockups into HTML to scientific plots into Python scripts. A circuit diagram can be viewed as a visual domai...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MEG-RAG: Quantifying Multi-modal Evidence Grounding for Evidence Selection in RAG](http://arxiv.org/abs/2604.24564v2)
  来源：arXiv | 日期：2026-04-27 | 相关度：6.8 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Multimodal Retrieval-Augmented Generation (MRAG) addresses key limitations of Multimodal Large Language Models (MLLMs), such as hallucination and outdated knowledge. However, current MRAG systems struggle to distinguish ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Comparative Study in Surgical AI: Datasets, Foundation Models, and Barriers to Med-AGI](https://www.medrxiv.org/content/10.64898/2026.03.26.26349455v3)
  来源：medRxiv | 日期：2026-04-28 | 相关度：6.8 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：本研究探讨了通用人工智能（AI）在外科图像分析任务中的表现。尽管AI在多项生物医学基准上已超越人类，但在外科领域仍面临多模态整合与专业数据标注的挑战。研究以2026年最先进的AI方法为基础，针对神经外科手术器械检测进行了案例研究。实验结果显示：(1) 评估19个开源视觉语言模型（VLM）的零样本性能，仅一个模型略微超过13.4%的基准线；(2) 使用LoRA微调Gemma 3 27B模型生成JSON预测，准确率提升至47.63%；(3)...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Position-Aware Drafting for Inference Acceleration in LLM-Based Generative List-Wise Recommendation](http://arxiv.org/abs/2604.27747v1)
  来源：arXiv | 日期：2026-04-30 | 相关度：6.55 | 新颖度：7.61
  匹配主题：foundation_model_agent
  中文摘要：Large language model (LLM)-based generative list-wise recommendation has advanced rapidly, but decoding remains sequential and thus latency-prone. To accelerate inference without changing the target distribution, specula...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Think it, Run it: Autonomous ML pipeline generation via self-healing multi-agent AI](http://arxiv.org/abs/2604.27096v1)
  来源：arXiv | 日期：2026-04-29 | 相关度：6.55 | 新颖度：6.7
  匹配主题：foundation_model_agent
  中文摘要：The purpose of our paper is to develop a unified multi-agent architecture that automates end-to-end machine learning (ML) pipeline generation from datasets and natural-language (NL) goals, improving efficiency, robustnes...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [End-to-end autonomous scientific discovery on a real optical platform](http://arxiv.org/abs/2604.27092v1)
  来源：arXiv | 日期：2026-04-29 | 相关度：6.55 | 新颖度：6.2
  匹配主题：foundation_model_agent
  中文摘要：Scientific research has long been human-led, driving new knowledge and transformative technologies through the continual revision of questions, methods and claims as evidence accumulates. Although large language model (L...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [FlashRT: Towards Computationally and Memory Efficient Red-Teaming for Prompt Injection and Knowledge Corruption](http://arxiv.org/abs/2604.28157v1)
  来源：arXiv | 日期：2026-04-30 | 相关度：5.45 | 新颖度：7.63
  匹配主题：foundation_model_agent
  中文摘要：Long-context large language models (LLMs)-for example, Gemini-3.1-Pro and Qwen-3.5-are widely used to empower many real-world applications, such as retrieval-augmented generation, autonomous agents, and AI assistants. Ho...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ProMax: Exploring the Potential of LLM-derived Profiles with Distribution Shaping for Recommender Systems](http://arxiv.org/abs/2604.26231v1)
  来源：arXiv | 日期：2026-04-29 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：The remarkable text understanding and generation capabilities of large language models (LLMs) have revitalized the field of general recommendation based on implicit user feedback. Rather than deploying LLMs directly as r...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Enhancing Linux Privilege Escalation Attack Capabilities of Local LLM Agents](http://arxiv.org/abs/2604.27143v1)
  来源：arXiv | 日期：2026-04-29 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Recent research has demonstrated the potential of Large Language Models (LLMs) for autonomous penetration testing, particularly when using cloud-based restricted-weight models. However, reliance on such models introduces...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Toward Autonomous SOC Operations: End-to-End LLM Framework for Threat Detection, Query Generation, and Resolution in Security Operations](http://arxiv.org/abs/2604.27321v1)
  来源：arXiv | 日期：2026-04-30 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Security Operations Centers (SOCs) face mounting operational challenges. These challenges come from increasing threat volumes, heterogeneous SIEM platforms, and time-consuming manual triage workflows. We present an end-t...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [LIT-RAGBench: Benchmarking Generator Capabilities of Large Language Models in Retrieval-Augmented Generation](http://arxiv.org/abs/2603.06198v2)
  来源：arXiv | 日期：2026-03-06 | 相关度：6.55 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) is a framework in which a Generator, such as a Large Language Model (LLM), produces answers by retrieving documents from an external collection using a Retriever. In practice, Generat...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [SecGoal: A Benchmark for Security Goal Extraction and Formalization from Protocol Documents](http://arxiv.org/abs/2604.27601v1)
  来源：arXiv | 日期：2026-04-30 | 相关度：4.75 | 新颖度：6.9
  匹配主题：foundation_model_agent
  中文摘要：Formal verification provides rigorous guarantees for cryptographic security, yet automating the extraction and formalization of security goals from natural language protocol documents remains a major bottleneck, compound...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [ChipLingo: A Systematic Training Framework for Large Language Models in EDA](http://arxiv.org/abs/2604.27415v1)
  来源：arXiv | 日期：2026-04-30 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：With the rapid advancement of semiconductor technology, Electronic Design Automation (EDA) has become an increasingly knowledge-intensive and document-driven engineering domain. Although large language models (LLMs) have...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Purifying Multimodal Retrieval: Fragment-Level Evidence Selection for RAG](http://arxiv.org/abs/2604.27600v1)
  来源：arXiv | 日期：2026-04-30 | 相关度：6.8 | 新颖度：6.65
  匹配主题：foundation_model_agent
  中文摘要：Multimodal Retrieval-Augmented Generation (MRAG) is widely adopted for Multimodal Large Language Models (MLLMs) with external evidence to reduce hallucinations. Despite its success, most existing MRAG frameworks treat re...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Cell type annotation for scATAC-seq via DNA large language model and graph domain adaptation.](https://pubmed.ncbi.nlm.nih.gov/42060707/)
  来源：PubMed | 日期：2026-04-01 | 相关度：6.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Single-cell ATAC-seq (scATAC-seq) enables the exploration of chromatin accessibility at single-cell resolution, offering critical insights into gene regulation. Accurate cell type annotation is a fundamental prerequisite...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RosettaSearch: Multi-Objective Inference-Time Search for Protein Sequence Design](http://arxiv.org/abs/2604.17175v2)
  来源：arXiv | 日期：2026-04-19 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：We introduce RosettaSearch, an inference-time multi-objective optimization approach for backbone conditioned protein sequence design. We use large language models (LLMs) as a generative optimizer within a search algorith...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Progressive Multi-Agent Reasoning for Biological Perturbation Prediction](http://arxiv.org/abs/2602.07408v2)
  来源：arXiv | 日期：2026-02-07 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Predicting gene regulation responses to biological perturbations requires reasoning about underlying biological causalities. While large language models (LLMs) show promise for such tasks, they are often overwhelmed by t...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Faithfulness-Aware Uncertainty Quantification for Fact-Checking the Output of Retrieval Augmented Generation](http://arxiv.org/abs/2505.21072v5)
  来源：arXiv | 日期：2025-05-27 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) enhanced with retrieval, an approach known as Retrieval-Augmented Generation (RAG), have achieved strong performance in open-domain question answering. However, RAG remains prone to hallucina...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Efficient Listwise Reranking with Compressed Document Representations](http://arxiv.org/abs/2604.26483v1)
  来源：arXiv | 日期：2026-04-29 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Reranking, the process of refining the output from a first-stage retriever, is often considered computationally expensive, especially when using Large Language Models (LLMs). A common approach to mitigate this cost invol...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A safety-centric perspective on innovation and risk in the use of artificial intelligence in genomics.](https://pubmed.ncbi.nlm.nih.gov/42062163/)
  来源：PubMed | 日期：2026-04-29 | 相关度：4.35 | 新颖度：6.0
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Adopting a safety-centric approach, this article explores how generative artificial intelligence (AI), and more specifically, foundation models for biological sequences, can exacerbate data quality issues, technical bias...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Artificial Intelligence, LLM-based generation of synthetic patients with Parkinson's Disease: towards a digital twin paradigm for in silico studies](https://www.medrxiv.org/content/10.64898/2026.04.28.26351471v1)
  来源：medRxiv | 日期：2026-04-29 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Heterogeneity in sporadic Parkinson's Disease (PD) is a critical problem that drives variable rates of progression and treatment response and complicates clinical trials. Access to large PD datasets that may help in clus...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Metastasis Extraction from NSCLC Clinical Notes: A Retrospective Comparative Evaluation of Large Language Model-Based Classification](https://www.medrxiv.org/content/10.64898/2026.04.27.26351872v1)
  来源：medRxiv | 日期：2026-04-29 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：识别非小细胞肺癌（NSCLC）的转移状态对疾病预后和治疗决策至关重要，但临床登记系统中的结构化数据往往不完整。本研究评估了三种大语言模型（LLM）在提取转移信息方面的表现。研究涵盖两个独立任务：全转移识别和脑/中枢神经系统（CNS）转移识别。实验基于两个队列：队列1包含579名患者的24,887份临床记录，以登记数据为标准；队列2包含22名患者的644份影像报告，以人工双重标注为标准。方法上，研究微调了GatorTron-base编码器...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Global strategies to fight carbapenem-resistant Acinetobacter baumannii (CRAB) infections.](https://pubmed.ncbi.nlm.nih.gov/41771383/)
  来源：PubMed | 日期：2026-05-01 | 相关度：5.75 | 新颖度：8.43
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent, application_monitoring
  中文摘要：Carbapenem-resistant Acinetobacter baumannii (CRAB) has emerged as a formidable healthcare-associated pathogen, particularly in intensive care units, where it causes severe infections associated with prolonged hospitaliz...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Laboratory innovations to diagnose invasive mould infections-what is relevant, what is not?](https://pubmed.ncbi.nlm.nih.gov/41173342/)
  来源：PubMed | 日期：2026-05-01 | 相关度：5.0 | 新颖度：8.43
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Invasive mould infections (IMI) carry high morbidity and mortality. Conventional diagnostics-histopathology, culture and microscopy-rely on invasive sampling and lack sensitivity, particularly during early phases of infe...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial intelligence-based gram stain classification: Accuracy and clinical utility in positive blood cultures.](https://pubmed.ncbi.nlm.nih.gov/41794133/)
  来源：PubMed | 日期：2026-05-01 | 相关度：2.45 | 新颖度：8.43
  匹配主题：application_monitoring
  中文摘要：With the rapid advancement of artificial intelligence (AI) technology, AI has been applied to the detection of pathogens that cause infectious diseases. This study evaluated the newly developed AI-based software, the BiT...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [PRAG: End-to-End Privacy-Preserving Retrieval-Augmented Generation](http://arxiv.org/abs/2604.26525v2)
  来源：arXiv | 日期：2026-04-29 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) is essential for enhancing Large Language Models (LLMs) with external knowledge, but its reliance on cloud environments exposes sensitive data to privacy risks. Existing privacy-prese...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Silent numerical failures in large language model-generated pharmacokinetic simulation code: a benchmark against target-controlled infusion validation criteria using the Marsh propofol model](https://www.medrxiv.org/content/10.64898/2026.04.27.26351582v1)
  来源：medRxiv | 日期：2026-04-28 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：BackgroundLarge language models (LLMs) are increasingly used by clinicians to generate executable code for pharmacokinetic (PK) simulation. Whether such code meets the accuracy standards of target-controlled infusion sys...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Polymer-Agent: Large Language Model Agent for Polymer Design.](https://pubmed.ncbi.nlm.nih.gov/42048526/)
  来源：PubMed | 日期：2026-04-28 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：按需聚合物发现对于从生物医学应用到增强材料的各个行业都至关重要。传统的聚合物实验涉及漫长的试错过程，消耗大量资源。虽然机器学习在性能预测和潜空间搜索方面加速了科学发现，但受限于基础设施，实验室研究人员往往难以直接调用代码和模型来提取特定结构与性能。本文提出了 Polymer-Agent，这是一个集成在终端中的闭环聚合物结构-性能预测框架，用于早期聚合物发现。该框架利用大语言模型（LLM）的推理能力，为用户提供性能预测、性能导向的聚合物结...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Evergreen: Efficient Claim Verification for Semantic Aggregates](http://arxiv.org/abs/2604.26180v1)
  来源：arXiv | 日期：2026-04-28 | 相关度：2.05 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：With recent semantic query processing engines, semantic aggregation has become a primitive operator, enabling the reduction of a relation into a natural language aggregate using an LLM. However, the resulting semantic ag...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SciHorizon-DataEVA: An Agentic System for AI-Readiness Evaluation of Heterogeneous Scientific Data](http://arxiv.org/abs/2604.26645v1)
  来源：arXiv | 日期：2026-04-29 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：AI-for-Science (AI4Science) is increasingly transforming scientific discovery by embedding machine learning models into prediction, simulation, and hypothesis generation workflows across domains. However, the effectivene...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Auto-ARGUE: LLM-Based Report Generation Evaluation](http://arxiv.org/abs/2509.26184v5)
  来源：arXiv | 日期：2025-09-30 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Generation of citation-backed reports is a primary use case for retrieval-augmented generation (RAG) systems. While open-source evaluation tools exist for various RAG tasks, tools designed for report generation are lacki...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [In Line with Context: Repository-Level Code Generation via Context Inlining](http://arxiv.org/abs/2601.00376v2)
  来源：arXiv | 日期：2026-01-01 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Repository-level code generation has attracted growing attention in recent years. Unlike function-level code generation, it requires the model to understand the entire repository, reasoning over complex dependencies acro...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Contextual Agentic Memory is a Memo, Not True Memory](http://arxiv.org/abs/2604.27707v1)
  来源：arXiv | 日期：2026-04-30 | 相关度：0.7 | 新颖度：6.75
  匹配主题：未命中具体主题
  中文摘要：Current agentic memory systems (vector stores, retrieval-augmented generation, scratchpads, and context-window management) do not implement memory: they implement lookup. We argue that treating lookup as memory is a cate...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A scoping review of uranium and other radioactive heavy metals in breast milk and their impact on early life health.](https://pubmed.ncbi.nlm.nih.gov/42062526/)
  来源：PubMed | 日期：2026-04-30 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Radioactive heavy metals, including uranium, strontium-90, caesium-137, radium, thorium, and plutonium, pose potential health risks to nursing infants through breast milk transfer. Understanding the extent of contaminati...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Machine Collective Intelligence for Explainable Scientific Discovery](http://arxiv.org/abs/2604.27297v1)
  来源：arXiv | 日期：2026-04-30 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Deriving governing equations from empirical observations is a longstanding challenge in science. Although artificial intelligence (AI) has demonstrated substantial capabilities in function approximation, the discovery of...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [OpenClassGen: A Large-Scale Corpus of Real-World Python Classes for LLM Research](http://arxiv.org/abs/2504.15564v3)
  来源：arXiv | 日期：2025-04-22 | 相关度：1.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：Existing class-level code generation datasets are either synthetic (ClassEval: 100 classes) or insufficient in scale for modern training needs (RealClassEval: 400 classes), hindering robust evaluation and empirical analy...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Don't Retrieve, Navigate: Distilling Enterprise Knowledge into Navigable Agent Skills for QA and RAG](http://arxiv.org/abs/2604.14572v2)
  来源：arXiv | 日期：2026-04-16 | 相关度：1.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) grounds LLM responses in external evidence but treats the model as a passive consumer of search results: it never sees how the corpus is organized or what it has not yet retrieved, li...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Faithfulness-QA: A Counterfactual Entity Substitution Dataset for Training Context-Faithful RAG Models](http://arxiv.org/abs/2604.25313v2)
  来源：arXiv | 日期：2026-04-28 | 相关度：0.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) models frequently produce answers grounded in parametric memory rather than the retrieved context, undermining the core promise of retrieval augmentation. A fundamental obstacle to fi...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [NuggetIndex: Governed Atomic Retrieval for Maintainable RAG](http://arxiv.org/abs/2604.27306v1)
  来源：arXiv | 日期：2026-04-30 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) systems are frequently evaluated via fact-based metrics, yet standard implementations retrieve passages or static propositions. This unit mismatch between evaluation and retrieval obj...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [AutoResearchBench: Benchmarking AI Agents on Complex Scientific Literature Discovery](http://arxiv.org/abs/2604.25256v1)
  来源：arXiv | 日期：2026-04-28 | 相关度：0.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Autonomous scientific research is significantly advanced thanks to the development of AI agents. One key step in this process is finding the right scientific literature, whether to explore existing knowledge for a resear...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Protein Function Prediction with Pretrained ProtT5 Embeddings and Gradient Boosting](https://www.biorxiv.org/content/10.64898/2026.04.27.721184v1)
  来源：bioRxiv | 日期：2026-04-28 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：蛋白质功能预测因基因本体（GO）注释的极端稀疏性和长尾分布，一直是计算生物学的核心挑战。蛋白质语言模型的发展使得从氨基酸序列中提取固定长度的稠密表征成为可能，为理化性质等人工特征提供了可扩展的替代方案。本研究在 CAFA-6 竞赛设置下，评估了利用 ProtT5-XL 提取的 Transformer 嵌入向量结合经典及现代多标签分类器进行 GO 预测的效果。研究通过对 Transformer 隐藏状态进行均值池化生成固定长度嵌入，并将其...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Design of Safe and Efficient Adenine Base Editors via Protein Language Model Screening for Osteoarthritis Treatment.](https://pubmed.ncbi.nlm.nih.gov/42052652/)
  来源：PubMed | 日期：2026-04-29 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：碱基编辑器（Base editors）可实现精确的基因组修饰，是纠正单核苷酸变异引起疾病的潜力疗法。虽然现有的高效腺嘌呤碱基编辑器（ABEs，如 ABE8e）在 A-to-G 转换方面效率极高，但其持续的高脱靶效应阻碍了临床转化。本研究利用人工智能辅助设计，开发了一种名为 RDLot-ABE 的安全变体。与 ABE8e 相比，RDLot-ABE 具有更窄（4 nt）的编辑窗口，且 DNA 脱靶编辑活性显著降低。此外，利用 RDLot-A...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Spatial Single-Cell Proteomics Reveals Molecular Trajectories Of Tangle-Bearing Neurons In Alzheimer's Disease](https://www.biorxiv.org/content/10.64898/2026.04.26.720932v1)
  来源：bioRxiv | 日期：2026-04-29 | 相关度：2.7 | 新颖度：5.25
  匹配主题：pathogenomics
  中文摘要：Neurofibrillary tangles composed of hyperphosphorylated tau are a defining pathological hallmark of Alzheimer's disease (AD); however, the pathways and mechanisms associated with the transition from physiological tau to ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AI-Enabled Imaging for Pathogen Detection Under Stress Conditions: A Systematic Review.](https://pubmed.ncbi.nlm.nih.gov/42021525/)
  来源：PubMed | 日期：2026-05-01 | 相关度：1.7 | 新颖度：8.93
  匹配主题：未命中具体主题
  中文摘要：Advances in pathogen detection that incorporate artificial intelligence (AI) may capture microbial signals under challenging environmental conditions that traditional methods miss. This systematic review evaluates the ap...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Biological multi-omics approaches to next-generation biomarkers in immune-related disorders and malignancies: An overview.](https://pubmed.ncbi.nlm.nih.gov/41324821/)
  来源：PubMed | 日期：2026-05-01 | 相关度：1.7 | 新颖度：8.93
  匹配主题：未命中具体主题
  中文摘要：Cancer and autoimmune diseases are major global health challenges characterized by molecular and clinical heterogeneity. Traditional single-analyte biomarkers often lack the sensitivity and specificity required for early...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Learning the All-Atom Equilibrium Distribution of Biomolecular Interactions at Scale](https://www.biorxiv.org/content/10.64898/2026.03.10.710952v2)
  来源：bioRxiv | 日期：2026-04-29 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：生物分子的功能由动态构象系综而非静态结构决定。尽管 AlphaFold 等模型革新了静态结构预测，但由于分子动力学（MD）计算成本高昂，准确捕捉全原子生物分子相互作用的平衡分布仍是重大挑战。本研究提出了 AnewSampling，这是一个可迁移的生成式基础框架，旨在实现全原子平衡分布的高保真采样，是首个在全原子水平上忠实再现 MD 的模型。该模型采用新型商空间（quotient-space）生成框架以确保数学一致性，并利用了包含超过 1...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Intern-Atlas: A Methodological Evolution Graph as Research Infrastructure for AI Scientists](http://arxiv.org/abs/2604.28158v1)
  来源：arXiv | 日期：2026-04-30 | 相关度：0.7 | 新颖度：7.39
  匹配主题：未命中具体主题
  中文摘要：现有的科研基础设施主要以文献为中心，仅提供论文间的引用链接，缺乏对方法论演进的显式表达，难以揭示研究方法如何产生、适配及迭代的结构化关系。随着 AI 科研智能体（AI Scientists）的兴起，这种局限性愈发显著，因为智能体难以从非结构化文本中可靠地重建方法演进拓扑。为此，我们推出了 Intern-Atlas，这是一个能够自动识别方法实体、推断方法谱系并捕捉创新驱动瓶颈的方法论演进图谱。该图谱基于 1,030,314 篇 AI 领域...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [NeocorRAG: Less Irrelevant Information, More Explicit Evidence, and More Effective Recall via Evidence Chains](http://arxiv.org/abs/2604.27852v1)
  来源：arXiv | 日期：2026-04-30 | 相关度：0.7 | 新颖度：7.2
  匹配主题：未命中具体主题
  中文摘要：Although precise recall is a core objective in Retrieval-Augmented Generation (RAG), a critical oversight persists in the field: improvements in retrieval performance do not consistently translate to commensurate gains i...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [YOSO: single-frame Gerchberg-Saxton phase retrieval with AI-based data augmentation for in-line holography](http://arxiv.org/abs/2604.27777v1)
  来源：arXiv | 日期：2026-04-30 | 相关度：0.7 | 新颖度：6.97
  匹配主题：未命中具体主题
  中文摘要：We present YOSO (You Only Shot Once), a single-frame phase retrieval framework for digital in-line holographic microscopy (DIHM) in which supervised deep learning is used to numerically generate an additional hologram co...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CubeGraph: Efficient Retrieval-Augmented Generation for Spatial and Temporal Data](http://arxiv.org/abs/2604.06616v2)
  来源：arXiv | 日期：2026-04-08 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Hybrid queries combining high-dimensional vector similarity search with spatio-temporal filters are increasingly critical for modern retrieval-augmented generation (RAG) systems. Existing systems typically handle these w...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models](http://arxiv.org/abs/2604.26649v1)
  来源：arXiv | 日期：2026-04-29 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：DeepSeek-R1 和 OpenAI o1 等大型推理模型（LRM）能生成数千 token 的长思维链，但其与检索增强生成（RAG）的集成存在根本性错位：传统 RAG 侧重于推理前的上下文提供，而 LRM 需要在多步推理过程中动态注入证据。本研究提出 ReaLM-Retrieve 框架，通过三大创新解决此问题：(1) 步级不确定性检测器，在推理步粒度而非 token 级别识别知识空缺；(2) 检索干预策略，学习外部证据收益最大化的时...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [MedSDoH: A Rule-Based System for Extracting Social Determinants of Health from Multi-site EHRs Based on the OHNLP Framework](https://www.medrxiv.org/content/10.64898/2026.04.27.26351699v1)
  来源：medRxiv | 日期：2026-04-29 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：健康社会决定因素（SDoH）对患者护理和人群健康至关重要，但相关信息常嵌入在非结构化临床文本（如社会工作者笔记）中，限制了其在临床决策中的应用。虽然 Transformer 模型是目前的主流，但其计算需求和透明度问题阻碍了大规模多中心临床实施。本研究开发了基于 OHNLP 框架的 MedSDoH 系统，利用文献资源、标准化定义和专家规则集构建。在开发过程中，利用大语言模型（LLM）辅助生成规则和扩展词库。MedSDoH 包含涵盖 22 ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [AI-powered insights in pediatric nephrology: current applications and future opportunities.](https://pubmed.ncbi.nlm.nih.gov/40957986/)
  来源：PubMed | 日期：2026-05-01 | 相关度：1.7 | 新颖度：8.93
  匹配主题：未命中具体主题
  中文摘要：Artificial intelligence (AI) is rapidly emerging as a transformative force in pediatric nephrology, enabling improvements in diagnostic accuracy, therapeutic precision, and operational workflows. By integrating diverse d...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Surface-enhanced Raman scattering (SERS) in antibiotic resistance detection: Advances, challenges, and future perspectives.](https://pubmed.ncbi.nlm.nih.gov/41519006/)
  来源：PubMed | 日期：2026-05-01 | 相关度：1.7 | 新颖度：8.43
  匹配主题：未命中具体主题
  中文摘要：Antimicrobial resistance (AMR) has emerged as one of the most critical global public health crises, causing an estimated 700,000 deaths annually according to the World Health Organization. Achieving early, rapid, and acc...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Quantitative Real-Time PCR Detection of Inactivated H5 Avian Influenza Virus in Raw Milk Samples by Miniaturized Instruments Designed for On-Site Testing](https://www.biorxiv.org/content/10.1101/2025.06.02.657307v3)
  来源：bioRxiv | 日期：2026-04-29 | 相关度：1.7 | 新颖度：5.25
  匹配主题：pathogenomics
  中文摘要：Highly pathogenic avian influenza virus (HPAIV) of H5 and H7 subtypes has emerged as one of the most important zoonotic pathogens in the 21st century with significant economic consequences. The recent outbreak of H5N1 av...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Toward precision chemotherapy in pancreatic ductal adenocarcinoma: molecular, transcriptomic and clinical determinants.](https://pubmed.ncbi.nlm.nih.gov/41846177/)
  来源：PubMed | 日期：2026-05-01 | 相关度：1.7 | 新颖度：3.43
  匹配主题：未命中具体主题
  中文摘要：胰腺导管腺癌（PDAC）是致死率极高的恶性肿瘤，化疗仍是各阶段系统治疗的核心。尽管改良型FOLFIRINOX及吉西他滨联合白蛋白结合型紫杉醇（AG或PAXG）等方案改善了部分患者预后，但疗效具有高度异质性且受毒性限制。本综述总结了从经验性化疗转向整合肿瘤生物学、分子生物学标志物及患者相关因素（如药物基因组学、合并症和毒性特征）的个体化方案的证据。目前，同源重组修复缺陷（HRD）、错配修复缺陷（MMRD）及罕见致癌融合等分子特征仅能为少数...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Using AI to Build AI: AIDO.Builder Enables Autonomous Machine Learning Model Building for Biomedicine](https://www.biorxiv.org/content/10.64898/2026.04.20.719735v2)
  来源：bioRxiv | 日期：2026-04-29 | 相关度：4.75 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Machine learning accelerates biomedical discovery, but creating effective predictive models requires specialized human expertise and demanding manual effort. Researchers must iteratively design pipelines, select architec...
  为什么值得看：bioRxiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [Decoupling Knowledge and Task Subspaces for Composable Parametric Retrieval Augmented Generation](http://arxiv.org/abs/2604.26768v1)
  来源：arXiv | 日期：2026-04-29 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Parametric Retrieval-Augmented Generation (PRAG) encodes external documents into lightweight parameter modules that can be retrieved and merged at inference time, offering a promising alternative to in-context retrieval ...
  为什么值得看：Decoupling Knowledge and Task Subspaces  与你的主题有弱匹配，暂时保留作低优先级跟踪。
