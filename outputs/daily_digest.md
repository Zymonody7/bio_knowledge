# 每日论文监控日报 (2026-10-01)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 29 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：429 Client Error: Too Many Requests
- PubMed：成功，命中 192 篇
- bioRxiv：成功，命中 14 篇
- medRxiv：成功，命中 8 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [Automatic prompt engineering using multimodal large language models for the analysis of biological research images.](https://pubmed.ncbi.nlm.nih.gov/42431798/)
  来源：PubMed | 日期：2026-10-01 | 相关度：8.9 | 新颖度：4.31
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are being applied across diverse fields due to their capability to derive various insights from complex data. In biotechnology, where complex multimodal data including images is rapidly expan...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Effect of large language model on diagnostic accuracy and clinical completeness among nephrology fellows managing transplant infection.](https://pubmed.ncbi.nlm.nih.gov/41888321/)
  来源：PubMed | 日期：2026-10-01 | 相关度：7.55 | 新颖度：8.81
  匹配主题：foundation_model_agent
  中文摘要：Infections are the predominant etiologies of post-transplant mortality in India, yet a structured infectious disease curriculum for nephrology fellows is limited. We evaluated whether large language model (LLM)-augmented...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Application of multimodal large language models for HER2/CEN17 FISH signal detection.](https://pubmed.ncbi.nlm.nih.gov/42248130/)
  来源：PubMed | 日期：2026-10-01 | 相关度：7.1 | 新颖度：8.06
  匹配主题：foundation_model_agent
  中文摘要：Fluorescence in situ hybridisation (FISH) is a reference technique for HER2 gene amplification assessment, yet manual signal counting is labour-intensive and subject to inter-observer variability. This study evaluates th...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [LncPNdeep: A long non-coding RNA classifier based on large language model with peptide and nucleotide embedding.](https://pubmed.ncbi.nlm.nih.gov/42621896/)
  来源：PubMed | 日期：2026-10-01 | 相关度：6.45 | 新颖度：9.31
  匹配主题：foundation_model_agent
  中文摘要：Accurate classification of long non-coding RNAs (lncRNAs) is essential for transcriptome annotation and understanding gene regulation. Existing computational methods predominantly rely on nucleotide sequence features, fr...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [A ReAct Agentic AI System for Natural Language Querying and Statistical Analysis of The Cancer Genome Atlas Clinical Data](https://www.medrxiv.org/content/10.64898/2026.07.15.26358188v2)
  来源：medRxiv | 日期：2026-09-28 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：The Cancer Genome Atlas (TCGA) holds clinical data for over 11,000 patients across 33 cancer types, but access is hard because of complex file structures, heterogeneous formats, and the need for programming. We present a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Large language model-based bibliometric evaluation of population descriptors in human genetics](https://www.biorxiv.org/content/10.64898/2026.09.24.754051v1)
  来源：bioRxiv | 日期：2026-09-28 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：As the use of population descriptors such as race, ethnicity, and ancestry have become increasingly common in modern genetics research, there have been growing calls to critically examine their use. Most notably, in 2023...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AI agents in drug discovery: A review of evolution, applications, and future directions.](https://pubmed.ncbi.nlm.nih.gov/42475855/)
  来源：PubMed | 日期：2026-10-01 | 相关度：3.1 | 新颖度：9.06
  匹配主题：未命中具体主题
  中文摘要：Artificial intelligence (AI) agents represent a paradigm shift in pharmaceutical research, moving the field from narrow drug-protein affinity modeling toward systems-biology-level evaluation in which autonomous, multi-do...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [A locally deployable agentic framework for clinical data deidentification](https://www.medrxiv.org/content/10.64898/2026.05.28.26353952v3)
  来源：medRxiv | 日期：2026-09-29 | 相关度：7.1 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Multimodal clinical data contain identifiers across diverse formats. We developed the Multimodal Anonymizer, a locally deployable framework combining multimodal language models, specialist networks, deterministic transfo...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [RNASeek: A Cross-Phyla Generative Foundation Model for Multipurpose RNA Modeling and Reinforcement Learning-Based Design](https://www.biorxiv.org/content/10.64898/2026.09.24.754173v1)
  来源：bioRxiv | 日期：2026-09-28 | 相关度：7.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：RNA plays central roles in regulating information flow and provides a versatile substrate for engineering biological functions. While large language models (LLMs) have transformed natural language processing and protein ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Genome-wide-scale prediction of compound-protein interactions using foundation and language models based on three-dimensional structures of compounds and proteins.](https://pubmed.ncbi.nlm.nih.gov/42803464/)
  来源：PubMed | 日期：2026-09-28 | 相关度：6.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：The identification of compound-protein interactions (CPIs) is crucial in the early stages of drug discovery. However, machine-learning (ML)-based methods based on one- and two-dimensional representations cannot capture i...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [BindRNAgen: Protein-binding RNA Sequence Generation Using Latent Diffusion Models.](https://pubmed.ncbi.nlm.nih.gov/42409279/)
  来源：PubMed | 日期：2026-10-01 | 相关度：5.75 | 新颖度：4.06
  匹配主题：foundation_model_agent
  中文摘要：RNA-binding proteins (RBPs) are pivotal regulators of gene expression, and their dysregulation is implicated in a wide range of human diseases. Designing synthetic RNA molecules to modulate RBP activity represents a prom...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [AI-Empowered Viral Metagenomics for Clinical Diagnosis: Advances, Bottlenecks, and Translational Pathways.](https://pubmed.ncbi.nlm.nih.gov/42809384/)
  来源：PubMed | 日期：2026-09-29 | 相关度：10.0 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Viral metagenomics, leveraging high-throughput sequencing technologies, provides comprehensive, hypothesis-free characterization of viral communities in clinical specimens, establishing itself as a pivotal tool for clini...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Reproducibility of AI-generated antibiotic recommendations in standardised clinical scenarios: A proof-of-concept experimental study.](https://pubmed.ncbi.nlm.nih.gov/42285312/)
  来源：PubMed | 日期：2026-10-01 | 相关度：8.65 | 新颖度：3.56
  匹配主题：foundation_model_agent, application_monitoring
  中文摘要：Artificial intelligence (AI) tools are increasingly used to support antimicrobial prescribing, but most published literature focuses on accuracy rather than reproducibility across identical inputs. Reproducibility is a k...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Assessing spoken discourse in aphasia using multimodal artificial intelligence](https://www.medrxiv.org/content/10.64898/2026.09.27.26364108v1)
  来源：medRxiv | 日期：2026-09-28 | 相关度：7.8 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Discourse analysis can reliably predict real-world communicative success, yet is rarely implemented clinically, due to challenges in manually generating stimulus-specific main concept inventories (MCIs) and scoring patie...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial Intelligence for Colorectal Surgeons-Part II: Research Applications, Challenges in Adoption, and Practical Resources.](https://pubmed.ncbi.nlm.nih.gov/42117468/)
  来源：PubMed | 日期：2026-10-01 | 相关度：7.1 | 新颖度：3.56
  匹配主题：foundation_model_agent
  中文摘要：This is part II of a 2-part series examining artificial intelligence in colorectal surgery. Part I established foundational concepts and clinical applications. Implementation, however, requires understanding research met...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Recent advances in CRISPR-based detection of foodborne pathogens: Mechanistic foundations, technological advances, and biosensing integration.](https://pubmed.ncbi.nlm.nih.gov/42215224/)
  来源：PubMed | 日期：2026-10-01 | 相关度：2.7 | 新颖度：8.06
  匹配主题：pathogenomics
  中文摘要：CRISPR-based biosensing has emerged as a rapid, sensitive, and field-deployable platform for foodborne pathogen detection, thereby effectively addressing the intrinsic limitations of conventional detection methodologies....
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Comparative Evaluation of a System One Model and a General-Purpose Large Language Model on the Korean Physical Therapist Licensing Examination](https://www.medrxiv.org/content/10.64898/2026.09.26.26364067v1)
  来源：medRxiv | 日期：2026-09-28 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Background: System One Model is designed for structured decision-making and can provide probabilistic outputs, but their performance in domain-specific physical therapy tasks has not been established. Objective: To evalu...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Vision-language encoding models reveal an image-computable food-quality dimension in human occipitotemporal cortex](https://www.biorxiv.org/content/10.64898/2026.08.25.747006v2)
  来源：bioRxiv | 日期：2026-09-28 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Perceived calorie content contributes to neural representational structure in human ventral visual cortex, yet it remains unclear whether this reflects an abstract nutritional signal or whether perceived calorie is large...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Biologically grounded cell profiling across microscopy modalities](https://www.biorxiv.org/content/10.64898/2026.09.23.753678v1)
  来源：bioRxiv | 日期：2026-09-28 | 相关度：3.1 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Microscopy-based cell profiling has broad applications in biological discovery, disease characterization, and phenotypic drug screening. Modern microscopy continues to push the limits of resolution, speed, depth and thro...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Peptide molecular lock-engineered nanobodies enable an oriented dual-modal immunoassay for reliable detection of Cronobacter sakazakii.](https://pubmed.ncbi.nlm.nih.gov/42447597/)
  来源：PubMed | 日期：2026-10-01 | 相关度：0.7 | 新颖度：8.06
  匹配主题：未命中具体主题
  中文摘要：Conventional nanobody ELISAs for trace Cronobacter sakazakii in powdered infant formula suffer from random orientation and low signal output. We developed an oriented dual-modal immunoassay that combines site-specific bi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Human-in-the-loop machine learning with community engagement reduces title, abstract and full-text screening workload in knowledge synthesis.](https://pubmed.ncbi.nlm.nih.gov/42805514/)
  来源：PubMed | 日期：2026-09-28 | 相关度：2.45 | 新颖度：0.25
  匹配主题：application_monitoring
  中文摘要：Manual screening of titles, abstracts, and full texts for large-volume knowledge synthesis requires significant time investment. Machine-assisted tools offer solutions for facilitating screening. Most applications to dat...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Accelerating cancer research and personalized medicine by tie-up with AI empowered genomics and proteomics.](https://pubmed.ncbi.nlm.nih.gov/42322793/)
  来源：PubMed | 日期：2026-10-01 | 相关度：2.4 | 新颖度：3.81
  匹配主题：未命中具体主题
  中文摘要：Artificial intelligence (AI) driven novel technique in genomics and proteomics have revolutionized cancer research with comprehensive analysis of complex molecular datasets. However, multiple challenges linked to data he...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Toward Precision Cardiac Rehabilitation: Current Limitations and Future Opportunities of Omics and Artificial Intelligence.](https://pubmed.ncbi.nlm.nih.gov/42295671/)
  来源：PubMed | 日期：2026-10-01 | 相关度：2.4 | 新颖度：3.31
  匹配主题：未命中具体主题
  中文摘要：Cardiovascular disease involves complex molecular, cellular, and physiological derangements that present challenges for traditional diagnostic and therapeutic approaches. Precision medicine is an evolving field that seek...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AMP-distillation: A knowledge distillation framework for accurate and efficient antimicrobial peptide prediction.](https://pubmed.ncbi.nlm.nih.gov/42155201/)
  来源：PubMed | 日期：2026-10-01 | 相关度：1.7 | 新颖度：8.56
  匹配主题：未命中具体主题
  中文摘要：Antimicrobial peptides (AMPs) are pivotal component of the innate immune system, showing broad activity to bacteria, fungi, viruses, and parasites. Despite their therapeutic potential, accurate identification and predict...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Multi-omics-guided dynamic precision medicine in leukemia: An AML-centered framework integrating genotype, cellular state, bone marrow pathology, and the immune ecosystem.](https://pubmed.ncbi.nlm.nih.gov/42456531/)
  来源：PubMed | 日期：2026-10-01 | 相关度：1.7 | 新颖度：8.06
  匹配主题：未命中具体主题
  中文摘要：Leukemia comprises a group of hematologic malignancies characterized by pronounced molecular heterogeneity, cellular-state plasticity, and highly variable clinical outcomes. With the rapid development of high-throughput ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Reclaiming Anatomy as Method: From Morphological Reasoning to Clinical Relevance.](https://pubmed.ncbi.nlm.nih.gov/41460831/)
  来源：PubMed | 日期：2026-10-01 | 相关度：1.7 | 新颖度：8.06
  匹配主题：未命中具体主题
  中文摘要：In recent decades, molecular biology and omics technologies have profoundly reshaped biomedical research, with genomics, proteomics, and other high-throughput approaches dominating scientific agendas and funding prioriti...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Transforming one health antimicrobial resistance surveillance in resource-limited countries (RLCs): From point-of-care diagnostics to AI-driven decision support.](https://pubmed.ncbi.nlm.nih.gov/42810525/)
  来源：PubMed | 日期：2026-09-29 | 相关度：5.95 | 新颖度：0.25
  匹配主题：pathogenomics, application_monitoring
  中文摘要：Antimicrobial resistance (AMR) is an emerging global problem, particularly for, resource-limited countries (RLCs) with limited capacity to diagnose diseases, inadequate surveillance systems, insufficient antimicrobial st...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Decoding cancer with artificial intelligence: Transforming research, diagnosis, and therapy with future insights.](https://pubmed.ncbi.nlm.nih.gov/42685611/)
  来源：PubMed | 日期：2026-10-01 | 相关度：3.75 | 新颖度：3.81
  匹配主题：foundation_model_agent
  中文摘要：Cancer remains one of the leading global health burdens, with increasing complexity in genomic, imaging, and clinical datasets presenting significant challenges for effective management. Artificial intelligence (AI) has ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Esketamine multi-omic biomarker evaluation in major depressive disorder (EMBER-MDD): concept, objectives and methodologies of a non-clinical investigator-initiated study.](https://pubmed.ncbi.nlm.nih.gov/42377483/)
  来源：PubMed | 日期：2026-10-01 | 相关度：1.7 | 新颖度：3.06
  匹配主题：未命中具体主题
  中文摘要：Treatment resistance (TR) in major depressive disorder (MDD) affects a substantial minority of patients and is hard to recognize early, delaying intensified care. The Esketamine multi-omic biomarker evaluation in MDD (EM...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
