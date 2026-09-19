# 每日论文监控日报 (2026-09-19)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 19 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：429 Client Error: Unknown Error
- PubMed：成功，命中 47 篇
- bioRxiv：成功，命中 12 篇
- medRxiv：成功，命中 11 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [Role of foundation models in data-driven tissue diagnostics.](https://pubmed.ncbi.nlm.nih.gov/42759410/)
  来源：PubMed | 日期：2026-09-18 | 相关度：7.8 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence (AI)-based tissue diagnostics is entering a new phase driven by pathology foundation models: large-scale encoders and multimodal systems pretrained with self-supervised and vision-language objecti...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [Genolator enables protein function interpretation using a multimodal large language model fusing genomic and structural interpretation with natural language interaction.](https://pubmed.ncbi.nlm.nih.gov/42750043/)
  来源：PubMed | 日期：2026-09-16 | 相关度：8.9 | 新颖度：1.2
  匹配主题：foundation_model_agent
  中文摘要：Decoding the genetic code to unveil its genome functionality is a monumental task which would greatly advance the understanding of disease mechanisms and development of targeted treatments. Although large language models...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Large Language Model-derived Symptom Clusters and Patient Outcomes in Colorectal Cancer from MIMIC-IV Clinical Notes](https://www.medrxiv.org/content/10.64898/2026.09.15.26363148v1)
  来源：medRxiv | 日期：2026-09-16 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Background: Prior research on symptom clusters (SCs) in colorectal cancer (CRC) has relied primarily on patient-reported outcome surveys, which capture symptom experience at discrete assessment points rather than the con...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Psychological factors contribute more to chronic low back pain than spine pathology: An LLM-based analysis of radiology reports](https://www.medrxiv.org/content/10.64898/2026.09.16.26363055v1)
  来源：medRxiv | 日期：2026-09-17 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Background Context Chronic low back pain (cLBP) is the leading global cause of disability, yet the anatomical, psychological, and socioeconomic determinants of cLBP are typically studied in isolation, with limited large-...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AI agents at the brain-computer interface: separating inference from control](https://www.medrxiv.org/content/10.64898/2026.09.13.26362955v1)
  来源：medRxiv | 日期：2026-09-17 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：In medicine, AI agents are moving from generating text to executing actions, making uncertainty from upstream decoders a control problem. We studied this at the brain-computer interface using 1,065 episodes from 47 peopl...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [scACORN: Context-engineered agent orchestration of specialized small language models for single-cell transcriptomic interpretation](https://www.biorxiv.org/content/10.64898/2026.09.10.750801v1)
  来源：bioRxiv | 日期：2026-09-16 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Single-cell atlases now exceed 66 million cells, but turning a ranked expression profile and a free-form biological question into a reliable, evidence-grounded answer remains unsolved. Scaling a single model does not res...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Reimagining research papers as interactive and reliable AI agents.](https://pubmed.ncbi.nlm.nih.gov/42749808/)
  来源：PubMed | 日期：2026-09-16 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Here we introduce Paper2Agent, an automated framework that converts research papers into artificial intelligence (AI) agents. Paper2Agent transforms research output from passive artefacts into active systems that acceler...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [HyLnc: a hybrid deep learning and feature-based approach for long non-coding RNA prediction.](https://pubmed.ncbi.nlm.nih.gov/42716909/)
  来源：PubMed | 日期：2026-12-31 | 相关度：5.75 | 新颖度：4.75
  匹配主题：foundation_model_agent
  中文摘要：Long non-coding RNAs (lncRNAs) play important roles in gene regulation, development and disease, yet accurate identification of lncRNAs from transcriptomic data remains a major computational challenge. Existing methods o...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 其他

- [A Turing-Style Test for In-Silico Antibodies: How Sampling Mode Makes WGAN-GP Beat VAE in the Wet Lab](https://www.biorxiv.org/content/10.64898/2026.09.11.750936v1)
  来源：bioRxiv | 日期：2026-09-16 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Recently, it has become feasible to generate antibodies in silico using AI-based approaches such as deep learning, natural language processing, and diffusion models. This opens the door to computational antibody design a...
  为什么值得看：bioRxiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Do Large Language Models Use the Clinical Vignette? A Question Ablation Study on the Orthopaedic In-Training Examination](https://www.medrxiv.org/content/10.64898/2026.09.15.26363139v1)
  来源：medRxiv | 日期：2026-09-16 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Background: Large language models (LLMs) have demonstrated strong performance on standardized medical examinations, with recent studies reporting performance approaching or exceeding that of senior medical residents. How...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Corpus-wide causality: Algorithm design & application for aggregating gene-disease causal evidence](https://www.biorxiv.org/content/10.64898/2026.05.08.723796v2)
  来源：bioRxiv | 日期：2026-09-16 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Identifying causal relationships and distinguishing them from associations is a central scientific endeavor with many applications; knowing causal links between genes and diseases, for instance, can focus drug discovery ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Unlocking Sensitive Data with SPHERE in the Age of AI](https://www.biorxiv.org/content/10.64898/2026.09.01.748580v2)
  来源：bioRxiv | 日期：2026-09-17 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Sensitive human data underpin discoveries across medicine, biology and the social sciences, yet privacy regulation often prevents sharing them with collaborators or artificial intelligence (AI) systems. We introduce SPHE...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Distinguishing Social Isolation, Social Support, and Contextual False Positives in Clinical Notes Using Fine-Tuned Language Models: Multisite Validation Study](https://www.medrxiv.org/content/10.64898/2026.07.05.26357334v3)
  来源：medRxiv | 日期：2026-09-16 | 相关度：6.5 | 新颖度：0.25
  匹配主题：foundation_model_agent, application_monitoring
  中文摘要：Background: Social isolation and social support are clinically important but inconsistently represented in structured electronic health record data. Their identification from clinical narratives is complicated by nuanced...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Population-Scale Precision Safety in Oncology Reveals Clinical and Genetic Determinants of Systemic Therapy Toxicity](https://www.medrxiv.org/content/10.64898/2026.09.16.26363259v1)
  来源：medRxiv | 日期：2026-09-17 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Treatment toxicity constrains the use of effective cancer therapies, but its clinical and genetic determinants remain poorly defined. We developed a large language model-based approach to produce MSK-Tox, a pan-cancer re...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Extracting Symptoms of Psychotic Disorders from Clinical Notes using Natural Language Processing.](https://www.medrxiv.org/content/10.64898/2026.09.16.26363090v1)
  来源：medRxiv | 日期：2026-09-17 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) are proposed as tools for high-throughput, deep phenotyping of psychiatric disorders. Applied to electronic health records, LLMs could in principle extract patient symptoms, outcome trajector...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Climate change impact on disease emergence and antimicrobial resistance: A perspective on transmission and detection.](https://pubmed.ncbi.nlm.nih.gov/42699333/)
  来源：PubMed | 日期：2026-09-18 | 相关度：3.7 | 新颖度：0.25
  匹配主题：pathogenomics
  中文摘要：Climate change is increasingly disrupting environmental and ecological systems, creating conditions that facilitate the emergence, transmission, and persistence of infectious diseases and the spread of antimicrobial resi...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [An injection-molded focal filter-integrated AI platform for cost-effective and highly sensitive molecular point-of-care testing.](https://pubmed.ncbi.nlm.nih.gov/42610358/)
  来源：PubMed | 日期：2026-09-16 | 相关度：2.7 | 新颖度：0.25
  匹配主题：pathogenomics
  中文摘要：The growing global demand for precise and accessible diagnostics underscores the need for decentralized, laboratory-grade molecular testing solutions. Current platforms are hindered by the high cost and fragility of glas...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Genomic foundation model-derived disruption profiling links somatic mutations to cancer biology and clinical outcomes](https://www.medrxiv.org/content/10.64898/2026.09.15.26363174v1)
  来源：medRxiv | 日期：2026-09-16 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Cancer genomics has concentrated on individual mutations, overlooking whether somatic mutations can accumulate to produce partial, gene-level disruption with biological and clinical consequences. Sequence-to-function mod...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Interaction Profiles as a Universal Language for Generative Molecular Design with ShEPhERD-2](https://www.biorxiv.org/content/10.64898/2026.09.10.750648v2)
  来源：bioRxiv | 日期：2026-09-16 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Three-dimensional intermolecular interactions govern molecular recognition and are fundamental to the pharmacological activity of small-molecule drugs. We propose that an interaction profile, comprising shape, electrosta...
  为什么值得看：bioRxiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。
