# 每日论文监控日报 (2026-06-03)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 27 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：429 Client Error: Unknown Error
- PubMed：成功，命中 195 篇
- bioRxiv：成功，命中 14 篇
- medRxiv：成功，命中 15 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [Multi-Agent AI for Chest Radiography: A Sequential Segmentation and LLM-Driven Consultative Tool for Medical Training](https://www.medrxiv.org/content/10.64898/2026.05.29.26354432v1)
  来源：medRxiv | 日期：2026-06-01 | 相关度：8.9 | 新颖度：1.2
  匹配主题：foundation_model_agent
  中文摘要：Background: Traditional diagnostic models lack explainability, while multimodal language models prone to hallucination remain unsafe for medical education. An interactive, risk-free artificial intelligence framework is r...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agent Role Structure and Operating Characteristics in Large Language Model Clinical Classification: A Comparative Study of Specialist and Deliberative Multi-Agent Protocols](https://www.medrxiv.org/content/10.64898/2026.02.22.26346818v4)
  来源：medRxiv | 日期：2026-05-31 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly considered in clinical decision support, yet the architectural effects of role decomposition within multi-agent systems remain poorly isolated. Prior comparisons of single-ag...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SeGA-GNN: Semantically Gated Augmented Graph Neural Networks for Wearable-Based Emotion Detection](https://www.medrxiv.org/content/10.64898/2026.05.29.26354434v1)
  来源：medRxiv | 日期：2026-06-01 | 相关度：6.8 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Background: Wearable technologies enable scalable and continuous monitoring of emotional states through passive sensing of physiological and behavioral signals. However, conventional learning approaches often struggle to...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Med.ai ASK: an agentic system for biomedical question answering.](https://pubmed.ncbi.nlm.nih.gov/41911379/)
  来源：PubMed | 日期：2026-06-01 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Intelligent agent-driven research co-pilots, leveraging advances in generative AI, are transforming how scientists access biomedical knowledge. This paper presents Med.ai ASK, an agentic question-answering system designe...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Predicting host-pathogen interactions using a proteome-scale language model](https://www.biorxiv.org/content/10.64898/2026.05.29.728699v1)
  来源：bioRxiv | 日期：2026-05-31 | 相关度：8.4 | 新颖度：1.0
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：ProteomeLM is a proteome-scale language model trained on proteomes spanning the tree of life to reconstruct masked protein embeddings from proteome context within each species. Its attention coefficients capture protein-...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Species- and Topic-aware Representation Learning for Antimicrobial Peptide Discovery](https://www.biorxiv.org/content/10.64898/2026.05.28.728246v1)
  来源：bioRxiv | 日期：2026-06-01 | 相关度：6.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Antimicrobial resistance poses a major global health challenge, necessitating efficient strategies to discover potent antimicrobial peptides (AMPs). While recent generative models can produce many candidate sequences, ex...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [The AFRIDIARRHEA multimodal fusion framework for Estimating the Burden of Diarrheal Diseases Among Children Under Five in Kenya, Zimbabwe, and Somaliland](https://www.medrxiv.org/content/10.64898/2026.06.01.26354632v1)
  来源：medRxiv | 日期：2026-06-02 | 相关度：4.8 | 新颖度：6.25
  匹配主题：pathogenomics, foundation_model_agent, application_monitoring
  中文摘要：Background: Accurate estimation of childhood diarrheal disease burden in Africa remains challenging because of limited surveillance, incomplete mortality data, pathogen-attribution uncertainty, and complex environmental ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Advances and challenges in the application of metagenomic sequencing for the diagnosis and treatment of infectious diseases: from pathogen spectrum identification to personalized antimicrobial strategies.](https://pubmed.ncbi.nlm.nih.gov/41764831/)
  来源：PubMed | 日期：2026-06-01 | 相关度：7.25 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：Infectious diseases remain a major global public health concern, demanding rapid and accurate identification of pathogens. Although conventional diagnostic methods such as culture, PCR, and immunological assays are widel...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Relationship Extraction for Adverse Drug Events in Clinical Notes Using Large Language Models](https://www.medrxiv.org/content/10.64898/2026.05.28.26354362v1)
  来源：medRxiv | 日期：2026-06-01 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Background: Adverse drug events (ADEs) are a critical indicator of patient safety but are often documented only in free-text clinical notes. The potential of recent advances in natural language processing (NLP), particul...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Algorithmic Versus Expert Rankings of Large Language Models in Peritoneal Dialysis Prescription Review: A Trap-Embedded Synthetic Benchmark](https://www.medrxiv.org/content/10.64898/2026.05.28.26354383v1)
  来源：medRxiv | 日期：2026-06-01 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Background: Clinical LLM benchmarks rarely test whether algorithmic rankings agree with expert clinical judgment. We developed a trap-embedded peritoneal dialysis (PD) benchmark comparing multiple scoring constructs with...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Reproducible and shareable bioinformatics pipelines from natural-language prompts](https://www.biorxiv.org/content/10.64898/2026.05.28.719125v1)
  来源：bioRxiv | 日期：2026-06-01 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly used to generate bioinformatics pipelines and to carry out analyses from natural-language prompts. However, the resulting analyses are often difficult to reproduce across ses...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [An extensible laboratory information management system for data harmonization across research centers: The ICTS-Dashboard](https://www.medrxiv.org/content/10.64898/2026.05.31.26354439v1)
  来源：medRxiv | 日期：2026-06-02 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Background: Collaborative research programs increasingly require infrastructure capable of integrating heterogeneous participant, sample, and experimental data while meeting evolving research needs. Existing tools, inclu...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Evolutionary constraints improve protein large language model predictions for protein stability, binding regions and epistasis](https://www.biorxiv.org/content/10.64898/2026.05.22.726784v2)
  来源：bioRxiv | 日期：2026-06-01 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Our understanding of protein function and evolution is largely based on the relationship between amino acid sequence and overall fold, now effectively captured by computational models. Yet predicting how mutations--shape...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Transfer learning with pre-trained language models for protein expression level prediction in Escherichia coli .](https://pubmed.ncbi.nlm.nih.gov/41438772/)
  来源：PubMed | 日期：2026-06-01 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Accurately predicting recombinant protein expression in Escherichia coli remains a long-standing challenge due to the multifactorial nature of gene regulation and translation. Existing computational approaches typically ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Integrating protein and DNA embeddings for improving genome-wide transcription factor binding site prediction.](https://pubmed.ncbi.nlm.nih.gov/42099803/)
  来源：PubMed | 日期：2026-06-01 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Transcription factors (TFs) regulate gene expression by binding to specific DNA sites on genome, making accurate TF binding site prediction critical for understanding gene regulation and downstream phenotypes. Almost all...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Big data in multiple sclerosis.](https://pubmed.ncbi.nlm.nih.gov/41925198/)
  来源：PubMed | 日期：2026-06-01 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：This review summarizes recent key advancements in multiple sclerosis (MS) achieved through the utilization of big data from diverse sources and advanced analytical techniques. Real-world evidence (RWE) derived from MS bi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GeneKnow: AI-powered literature synthesis for gene-context analysis](https://www.biorxiv.org/content/10.64898/2026.05.28.728511v1)
  来源：bioRxiv | 日期：2026-06-01 | 相关度：2.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Interpreting gene function in specific biological contexts is essential for biomedical research, yet manual literature review is labor-intensive. We developed GeneKnow, a source-grounded framework that uses generative AI...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AI-Guided Structure-Aware Modeling and Thermal Proteomics Reveal Direct Demethylzeylasteral-ACLY Interaction](https://www.biorxiv.org/content/10.64898/2026.04.07.717093v2)
  来源：bioRxiv | 日期：2026-06-01 | 相关度：1.7 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：Identifying the direct molecular targets of bioactive natural products remains a central challenge in chemical biology. Here we present an integrated experimental-computational framework, that combines matrix-augmented t...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Field-ready portable rapid nucleic acid test for tuberculosis detection and drug-resistance profiling in resource-limited settings](https://www.medrxiv.org/content/10.64898/2026.05.29.26354438v1)
  来源：medRxiv | 日期：2026-06-01 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Tuberculosis (TB) remains one of the deadliest infectious diseases, with over a million deaths annually and a growing threat from multidrug-resistant strains (MDR-TB). A major bottleneck in controlling TB is the lack of ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Thermoregulation and associated disorders: 3PM-guided holistic approach bridging innovative and traditional Chinese medicine.](https://pubmed.ncbi.nlm.nih.gov/42179458/)
  来源：PubMed | 日期：2026-06-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Accurately performed thermoregulation is life-important for the human body. Therefore, a relatively narrow temperature range of 36.5-37 °C, which all our biochemical reactions are adapted to, is rigorously kept by the bo...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Artificial intelligence in combating challenges in antimicrobial resistance: a narrative review.](https://pubmed.ncbi.nlm.nih.gov/41859321/)
  来源：PubMed | 日期：2026-06-01 | 相关度：6.15 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：Antimicrobial resistance (AMR) is a major global health challenge that threatens the effective prevention and treatment of infections. It arises from increasing resistance rates, limited diagnostic capacity, inappropriat...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [From risk to resilience: A narrative review on strengthening veterinary clinical biosecurity to prevent healthcare-associated infections.](https://pubmed.ncbi.nlm.nih.gov/42025907/)
  来源：PubMed | 日期：2026-06-01 | 相关度：4.45 | 新颖度：0.25
  匹配主题：pathogenomics, application_monitoring
  中文摘要：Veterinary clinical biosecurity is key to preventing infectious diseases in animal clinics, particularly when there is high patient turnover, a mix of species, close contact among animals, or immunocompromised patients t...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [A Foundation Model for the Cancer Genome](https://www.biorxiv.org/content/10.64898/2026.05.27.728319v1)
  来源：bioRxiv | 日期：2026-06-01 | 相关度：4.35 | 新颖度：0.75
  匹配主题：sequencing_bioinformatics, application_monitoring
  中文摘要：Cancer is a disease of the genome, in which somatic mutations and copy-number alterations determine tumour identity, clinical behaviour, and response to therapy. Consortium-scale sequencing has profiled hundreds of thous...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Artificial Intelligence in Oncology: Clinical Applications, Challenges, and Opportunities.](https://pubmed.ncbi.nlm.nih.gov/42214043/)
  来源：PubMed | 日期：2026-06-01 | 相关度：3.75 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence (AI) is reshaping cancer research and clinical oncology by enabling large-scale analysis of complex biomedical data. Although early AI efforts focused on single-modality tasks such as imaging inte...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [A Three-Item Functional Screen for Multimodal Prognostic Triage in Mild Cognitive Impairment: Benchmarking Against Entorhinal Tau PET and Plasma p-tau217](https://www.medrxiv.org/content/10.64898/2026.06.01.26354584v1)
  来源：medRxiv | 日期：2026-06-02 | 相关度：3.05 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Importance: Broadening access to biomarker-informed risk stratification in mild cognitive impairment (MCI) has become even more critical to early assessment in Alzheimer disease given recent developments in regulatory ap...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Multimodal Ultrasound Integration Pathways and Paradigm Innovations in Precision Diagnosis and Treatment of Thyroid Cancer.](https://pubmed.ncbi.nlm.nih.gov/42230172/)
  来源：PubMed | 日期：2026-06-02 | 相关度：2.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Thyroid cancer, the fastest-growing endocrine malignancy, is shifting from morphological evaluation to molecular-functional imaging. This review systematically evaluates the translational value of multimodal ultrasound t...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Integrating multi-omics data and artificial intelligence for personalized medicine in glioblastoma.](https://pubmed.ncbi.nlm.nih.gov/41921727/)
  来源：PubMed | 日期：2026-06-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Glioblastoma (GBM) is one of the most lethal primary brain tumors and is characterized by profound molecular heterogeneity, rapid progression, and limited therapeutic responsiveness. Traditional diagnostic and treatment ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
