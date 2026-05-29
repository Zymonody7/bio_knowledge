# 每日论文监控日报 (2026-05-29)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 15 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：429 Client Error: Unknown Error
- PubMed：成功，命中 49 篇
- bioRxiv：成功，命中 17 篇
- medRxiv：成功，命中 12 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [Pathogen-specific antimicrobial activity prediction with biological large language model-based methods](https://www.biorxiv.org/content/10.64898/2026.05.23.727347v1)
  来源：bioRxiv | 日期：2026-05-26 | 相关度：8.4 | 新颖度：1.0
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Driven by the rise of antimicrobial resistance, antimicrobial peptides (AMPs) have emerged as promising therapeutics capable of targeting multidrug-resistant pathogens. Because identifying AMPs and their specific targets...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DISCERN: A Clinical Impact-aware Framework for Radiology Report Comparison](https://www.medrxiv.org/content/10.64898/2026.05.26.26353612v1)
  来源：medRxiv | 日期：2026-05-27 | 相关度：7.55 | 新颖度：1.7
  匹配主题：foundation_model_agent
  中文摘要：The surge in medical imaging has spurred the development of vision-language models (VLMs) to alleviate radiologist workloads. However, clinical deployment is hindered by the lack of meaningful evaluation frameworks. Curr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Association of a polygenic risk score with coronary atherosclerotic burden in clinical CT angiograms](https://www.medrxiv.org/content/10.64898/2026.05.26.26353801v1)
  来源：medRxiv | 日期：2026-05-27 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Background: Polygenic risk scores (PRS) for coronary artery disease (CAD) are associated with cardiovascular events, but the relationship between inherited risk and routinely reported coronary computed tomography angiogr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Grounding Language Models in Behavioral Science to Scale Physical Activity Interventions for Hispanic/Latinx Populations](https://www.medrxiv.org/content/10.64898/2026.05.26.26354165v1)
  来源：medRxiv | 日期：2026-05-28 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Objective: Hispanic/Latinx populations in the U.S. experience higher rates of chronic disease linked to physical inactivity, yet digital health interventions remain largely inaccessible to more than 16 million Hispanic/L...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ProteomeLM: A proteome-scale language model enables accurate and rapid prediction of protein-protein interactions and gene essentiality across taxa.](https://pubmed.ncbi.nlm.nih.gov/42160340/)
  来源：PubMed | 日期：2026-05-26 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Language models trained on biological sequences are advancing inference tasks from the scale of single proteins to that of genomic neighborhoods. Here, we introduce ProteomeLM, a transformer-based language model that uni...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [AI Decision Support for Challenging Teledermatology Cases: MedGemma Performance in the Dermatology ECHO Program](https://www.medrxiv.org/content/10.64898/2026.05.21.26353523v1)
  来源：medRxiv | 日期：2026-05-26 | 相关度：8.5 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Teledermatology expands access to dermatologic expertise in rural settings, yet diagnostic uncertainty persists in low-resource primary care. This retrospective study evaluated MedGemma-4B-IT, a compact multimodal vision...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [IID-KG: An ontology-aligned literature-derived knowledge graph for infectious and immune-mediated diseases](https://www.biorxiv.org/content/10.64898/2026.05.21.727015v1)
  来源：bioRxiv | 日期：2026-05-26 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Infectious and immune-mediated diseases (IIDs) represent a broad and rapidly expanding biomedical literature domain in which scalable evidence extraction, disease ontology refinement, and interpretable knowledge integrat...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Full-Body AI Agent: A Perspective on Multi-Scale Collaborative AI for Systemic Biology and Precision Medicine.](https://pubmed.ncbi.nlm.nih.gov/42189114/)
  来源：PubMed | 日期：2026-05-26 | 相关度：2.1 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Artificial intelligence (AI) is increasingly applied to biomedical research, but most current systems remain limited to specific tasks, data types, or biological scales. This makes it difficult to connect molecular alter...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Constrained protein Large Language Model illustrated in protein stability, function and epistasis](https://www.biorxiv.org/content/10.64898/2026.05.22.726784v1)
  来源：bioRxiv | 日期：2026-05-26 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Our understanding of protein function and evolution is largely based on the relationship between amino acid sequence and overall fold, now effectively captured by computational models. Yet predicting how mutations--shape...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [dbGIST: An LLM-Assisted Multi-Omics Resource for Target Exploration and Cross-Dataset Validation in Gastrointestinal Stromal Tumors](https://www.biorxiv.org/content/10.64898/2026.05.22.727292v1)
  来源：bioRxiv | 日期：2026-05-26 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Gastrointestinal stromal tumors (GISTs) are the most common mesenchymal neoplasms of the gastrointestinal tract, yet GIST-specific omics evidence remains scattered across small cohorts and is not represented as a dedicat...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Current understanding and future directions in severe asthma through artificial intelligence-integrated multi-omic approaches.](https://pubmed.ncbi.nlm.nih.gov/42203233/)
  来源：PubMed | 日期：2026-04-01 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Severe asthma remains a challenging, heterogeneous condition, despite significant advances in therapeutic strategies. A subset of patients continues to experience poor control, frequent exacerbations and a high burden of...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Frontier Large Language Models for Comprehensive Medication Review in CKD Patients with Polypharmacy: A Trap-Embedded Synthetic Benchmark](https://www.medrxiv.org/content/10.64898/2026.05.23.26353939v1)
  来源：medRxiv | 日期：2026-05-26 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：BackgroundPatients with CKD and polypharmacy face high rates of drug-related problems, yet comprehensive medication review remains time-intensive and inconsistently performed. Large language models (LLMs) may augment thi...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [The evolution of scientific knowledge in childhood asthma over time.](https://pubmed.ncbi.nlm.nih.gov/42203231/)
  来源：PubMed | 日期：2026-04-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Paediatric asthma management has undergone a significant transformation from rudimentary assessments in the early 20th century to sophisticated diagnostic and therapeutic approaches today. Early clinical observations lac...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [An intention-oriented multi-agent dialogue system for patient-centered decision-making.](https://pubmed.ncbi.nlm.nih.gov/42192358/)
  来源：PubMed | 日期：2026-05-26 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Conversational agents are increasingly used in healthcare, but most systems are designed for clinicians and insufficiently support patient-centered decision-making. Limited patient understanding of medical decisions may ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Integrative advances in biomarker-driven prostate cancer management from genomic discovery to precision oncology.](https://pubmed.ncbi.nlm.nih.gov/42189429/)
  来源：PubMed | 日期：2026-05-26 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Prostate cancer (PCa) is the second most common malignancy in men worldwide, with rising mortality linked to late-stage diagnoses. While current diagnostic strategies rely heavily on biomarker detection, their limitation...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
