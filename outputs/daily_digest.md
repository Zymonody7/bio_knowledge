# 每日论文监控日报 (2026-10-02)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 31 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：429 Client Error: Unknown Error
- PubMed：成功，命中 200 篇
- bioRxiv：成功，命中 17 篇
- medRxiv：成功，命中 9 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### 数据集 / Benchmark

- [PathoBERT: A Hybrid Attention-Based Genomic Language Model for Read-Level Bacterial Pathogenicity Prediction](https://www.biorxiv.org/content/10.64898/2026.09.27.754806v1)
  来源：bioRxiv | 日期：2026-09-29 | 相关度：8.6 | 新颖度：5.75
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Motivation Although recent deep learning models have achieved promising results on read level classification tasks, their robustness to realistic sequencing conditions, sensitivity to read length, and ability to support ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [ELITE: E3 Ligase Inference for Tissue specific Elimination: A LLM Based E3 Ligase Prediction System for Precise Targeted Protein Degradation](https://www.biorxiv.org/content/10.1101/2025.11.05.686884v10)
  来源：bioRxiv | 日期：2026-09-29 | 相关度：10.0 | 新颖度：6.75
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Targeted protein degradation (TPD) has transformed modern drug discovery by harnessing the ubiquitin-proteasome system to eliminate disease-driving proteins previously deemed undruggable. However, current approaches pred...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [Automatic prompt engineering using multimodal large language models for the analysis of biological research images.](https://pubmed.ncbi.nlm.nih.gov/42431798/)
  来源：PubMed | 日期：2026-10-01 | 相关度：8.9 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are being applied across diverse fields due to their capability to derive various insights from complex data. In biotechnology, where complex multimodal data including images is rapidly expan...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Effect of large language model on diagnostic accuracy and clinical completeness among nephrology fellows managing transplant infection.](https://pubmed.ncbi.nlm.nih.gov/41888321/)
  来源：PubMed | 日期：2026-10-01 | 相关度：7.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Infections are the predominant etiologies of post-transplant mortality in India, yet a structured infectious disease curriculum for nephrology fellows is limited. We evaluated whether large language model (LLM)-augmented...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Biological rationales from language models enable leakage-resistant forecasts of target-indication success](https://www.biorxiv.org/content/10.64898/2026.09.24.754137v1)
  来源：bioRxiv | 日期：2026-09-29 | 相关度：7.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Identifying which target-indication (T-I) hypotheses can translate into clinical success remains a central challenge in drug discovery. We present PRIORITI (Prospective Rationale-Informed Outcome Reasoning for Integrated...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Application of multimodal large language models for HER2/CEN17 FISH signal detection.](https://pubmed.ncbi.nlm.nih.gov/42248130/)
  来源：PubMed | 日期：2026-10-01 | 相关度：7.1 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Fluorescence in situ hybridisation (FISH) is a reference technique for HER2 gene amplification assessment, yet manual signal counting is labour-intensive and subject to inter-observer variability. This study evaluates th...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [A locally deployable agentic framework for clinical data deidentification](https://www.medrxiv.org/content/10.64898/2026.05.28.26353952v3)
  来源：medRxiv | 日期：2026-09-29 | 相关度：7.1 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Multimodal clinical data contain identifiers across diverse formats. We developed the Multimodal Anonymizer, a locally deployable framework combining multimodal language models, specialist networks, deterministic transfo...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Comparative analysis of mitochondrial proteomes across the tree of life.](https://pubmed.ncbi.nlm.nih.gov/42822426/)
  来源：PubMed | 日期：2026-10-01 | 相关度：7.7 | 新颖度：5.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Mitochondria arose from the endosymbiosis of a bacterium with an archaea-related host cell about 2 billion years ago. To understand their origins and evolution, we compared experimentally defined mitoproteomes from the M...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AI-Based Comparison of UniProt annotations and Literature Across Human Kinases](https://www.biorxiv.org/content/10.64898/2026.09.23.753935v1)
  来源：bioRxiv | 日期：2026-09-29 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Curated protein records and their supporting publications organize biological evidence at different levels of detail. Here, we used AI to independently answer a set of biological questions using either UniProt records or...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [LncPNdeep: A long non-coding RNA classifier based on large language model with peptide and nucleotide embedding.](https://pubmed.ncbi.nlm.nih.gov/42621896/)
  来源：PubMed | 日期：2026-10-01 | 相关度：6.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Accurate classification of long non-coding RNAs (lncRNAs) is essential for transcriptome annotation and understanding gene regulation. Existing computational methods predominantly rely on nucleotide sequence features, fr...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A low-annotation-budget PubMedBERT classifier for chondrogenesis regulator discovery via active learning](https://www.biorxiv.org/content/10.64898/2026.09.24.754045v1)
  来源：bioRxiv | 日期：2026-09-29 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Motivation: Biomedical natural language processing (Bio-NLP) classification tasks are often limited by the cost of manual annotation, especially for specialised extraction problems where labelled corpora are scarce. Acti...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [AI-Empowered Viral Metagenomics for Clinical Diagnosis: Advances, Bottlenecks, and Translational Pathways.](https://pubmed.ncbi.nlm.nih.gov/42809384/)
  来源：PubMed | 日期：2026-09-29 | 相关度：10.0 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Viral metagenomics, leveraging high-throughput sequencing technologies, provides comprehensive, hypothesis-free characterization of viral communities in clinical specimens, establishing itself as a pivotal tool for clini...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Reproducibility of AI-generated antibiotic recommendations in standardised clinical scenarios: A proof-of-concept experimental study.](https://pubmed.ncbi.nlm.nih.gov/42285312/)
  来源：PubMed | 日期：2026-10-01 | 相关度：8.65 | 新颖度：0.75
  匹配主题：foundation_model_agent, application_monitoring
  中文摘要：Artificial intelligence (AI) tools are increasingly used to support antimicrobial prescribing, but most published literature focuses on accuracy rather than reproducibility across identical inputs. Reproducibility is a k...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial Intelligence for Colorectal Surgeons-Part II: Research Applications, Challenges in Adoption, and Practical Resources.](https://pubmed.ncbi.nlm.nih.gov/42117468/)
  来源：PubMed | 日期：2026-10-01 | 相关度：7.1 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：This is part II of a 2-part series examining artificial intelligence in colorectal surgery. Part I established foundational concepts and clinical applications. Implementation, however, requires understanding research met...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Machine learning-enabled wastewater-based surveillance for emerging pathogen detection and monitoring: current applications, challenges, and future prospects.](https://pubmed.ncbi.nlm.nih.gov/42704107/)
  来源：PubMed | 日期：2026-12-01 | 相关度：5.0 | 新颖度：4.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Wastewater-based surveillance (WBS) has become an important public-health tool for tracking community-level circulation of emerging and re-emerging pathogens, but wastewater measurements are not directly interpretable pu...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Title and abstract screening for systematic reviews with Jev, a System One model: comparison with generative large language models](https://www.medrxiv.org/content/10.64898/2026.09.25.26364021v1)
  来源：medRxiv | 日期：2026-10-01 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) screen titles and abstracts without review-specific training, but generating screening decisions as text takes processing time and incurs API charges. We evaluated Jev, a non-generative model...
  为什么值得看：medRxiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [AI agents in drug discovery: A review of evolution, applications, and future directions.](https://pubmed.ncbi.nlm.nih.gov/42475855/)
  来源：PubMed | 日期：2026-10-01 | 相关度：3.1 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Artificial intelligence (AI) agents represent a paradigm shift in pharmaceutical research, moving the field from narrow drug-protein affinity modeling toward systems-biology-level evaluation in which autonomous, multi-do...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Peptide molecular lock-engineered nanobodies enable an oriented dual-modal immunoassay for reliable detection of Cronobacter sakazakii.](https://pubmed.ncbi.nlm.nih.gov/42447597/)
  来源：PubMed | 日期：2026-10-01 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Conventional nanobody ELISAs for trace Cronobacter sakazakii in powdered infant formula suffer from random orientation and low signal output. We developed an oriented dual-modal immunoassay that combines site-specific bi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [BindRNAgen: Protein-binding RNA Sequence Generation Using Latent Diffusion Models.](https://pubmed.ncbi.nlm.nih.gov/42409279/)
  来源：PubMed | 日期：2026-10-01 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：RNA-binding proteins (RBPs) are pivotal regulators of gene expression, and their dysregulation is implicated in a wide range of human diseases. Designing synthetic RNA molecules to modulate RBP activity represents a prom...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Accelerating cancer research and personalized medicine by tie-up with AI empowered genomics and proteomics.](https://pubmed.ncbi.nlm.nih.gov/42322793/)
  来源：PubMed | 日期：2026-10-01 | 相关度：2.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Artificial intelligence (AI) driven novel technique in genomics and proteomics have revolutionized cancer research with comprehensive analysis of complex molecular datasets. However, multiple challenges linked to data he...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Toward Precision Cardiac Rehabilitation: Current Limitations and Future Opportunities of Omics and Artificial Intelligence.](https://pubmed.ncbi.nlm.nih.gov/42295671/)
  来源：PubMed | 日期：2026-10-01 | 相关度：2.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Cardiovascular disease involves complex molecular, cellular, and physiological derangements that present challenges for traditional diagnostic and therapeutic approaches. Precision medicine is an evolving field that seek...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SpatialTRACE predicts anatomical axes and regions in spatial transcriptomics and microscopy](https://www.biorxiv.org/content/10.64898/2026.09.23.753836v1)
  来源：bioRxiv | 日期：2026-09-29 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Spatial transcriptomics measures gene expression in tissue sections. However, interpretation requires anatomical maps that link gene expression and cellular composition to tissue structure. Annotating entire sections oft...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [An agentic AI environment to support biomedical research in collaborative academic environments](https://www.biorxiv.org/content/10.64898/2026.09.24.753565v1)
  来源：bioRxiv | 日期：2026-09-29 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Agentic artificial intelligence (AAI) is increasingly used by biomedical scientists, where it has substantially lowered the difficulty of integrating computational, statistical and data-science approaches into day-to-day...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AMP-distillation: A knowledge distillation framework for accurate and efficient antimicrobial peptide prediction.](https://pubmed.ncbi.nlm.nih.gov/42155201/)
  来源：PubMed | 日期：2026-10-01 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Antimicrobial peptides (AMPs) are pivotal component of the innate immune system, showing broad activity to bacteria, fungi, viruses, and parasites. Despite their therapeutic potential, accurate identification and predict...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Multi-omics-guided dynamic precision medicine in leukemia: An AML-centered framework integrating genotype, cellular state, bone marrow pathology, and the immune ecosystem.](https://pubmed.ncbi.nlm.nih.gov/42456531/)
  来源：PubMed | 日期：2026-10-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Leukemia comprises a group of hematologic malignancies characterized by pronounced molecular heterogeneity, cellular-state plasticity, and highly variable clinical outcomes. With the rapid development of high-throughput ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Reclaiming Anatomy as Method: From Morphological Reasoning to Clinical Relevance.](https://pubmed.ncbi.nlm.nih.gov/41460831/)
  来源：PubMed | 日期：2026-10-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：In recent decades, molecular biology and omics technologies have profoundly reshaped biomedical research, with genomics, proteomics, and other high-throughput approaches dominating scientific agendas and funding prioriti...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Transforming one health antimicrobial resistance surveillance in resource-limited countries (RLCs): From point-of-care diagnostics to AI-driven decision support.](https://pubmed.ncbi.nlm.nih.gov/42810525/)
  来源：PubMed | 日期：2026-09-29 | 相关度：5.95 | 新颖度：0.25
  匹配主题：pathogenomics, application_monitoring
  中文摘要：Antimicrobial resistance (AMR) is an emerging global problem, particularly for, resource-limited countries (RLCs) with limited capacity to diagnose diseases, inadequate surveillance systems, insufficient antimicrobial st...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Theranostic innovation in infectious lung diseases: integrating biotechnology and nanotechnology for precision medicine.](https://pubmed.ncbi.nlm.nih.gov/42549821/)
  来源：PubMed | 日期：2026-10-01 | 相关度：4.45 | 新颖度：0.25
  匹配主题：pathogenomics, application_monitoring
  中文摘要：Infectious lung diseases, such as pneumonia, tuberculosis, COVID-19, influenza, and emerging fungal infections, are major causes of illness and death worldwide. Traditional methods have serious limitations such as diagno...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Decoding cancer with artificial intelligence: Transforming research, diagnosis, and therapy with future insights.](https://pubmed.ncbi.nlm.nih.gov/42685611/)
  来源：PubMed | 日期：2026-10-01 | 相关度：3.75 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Cancer remains one of the leading global health burdens, with increasing complexity in genomic, imaging, and clinical datasets presenting significant challenges for effective management. Artificial intelligence (AI) has ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Recent advances in CRISPR-based detection of foodborne pathogens: Mechanistic foundations, technological advances, and biosensing integration.](https://pubmed.ncbi.nlm.nih.gov/42215224/)
  来源：PubMed | 日期：2026-10-01 | 相关度：2.7 | 新颖度：0.25
  匹配主题：pathogenomics
  中文摘要：CRISPR-based biosensing has emerged as a rapid, sensitive, and field-deployable platform for foodborne pathogen detection, thereby effectively addressing the intrinsic limitations of conventional detection methodologies....
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Esketamine multi-omic biomarker evaluation in major depressive disorder (EMBER-MDD): concept, objectives and methodologies of a non-clinical investigator-initiated study.](https://pubmed.ncbi.nlm.nih.gov/42377483/)
  来源：PubMed | 日期：2026-10-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Treatment resistance (TR) in major depressive disorder (MDD) affects a substantial minority of patients and is hard to recognize early, delaying intensified care. The Esketamine multi-omic biomarker evaluation in MDD (EM...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
