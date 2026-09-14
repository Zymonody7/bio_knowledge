# 每日论文监控日报 (2026-09-14)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 7 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：429 Client Error: Too Many Requests
- PubMed：成功，命中 30 篇
- bioRxiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='api.biorxiv.org', port=443): Read timed out. (read timeout=60)
- medRxiv：成功，命中 8 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [Benchmarking methods integrating GWAS and single-cell transcriptomic data for mapping trait-cell type associations](https://www.medrxiv.org/content/10.1101/2025.05.24.25328275v3)
  来源：medRxiv | 日期：2026-09-12 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Genome-wide association studies (GWAS) have discovered numerous trait-associated variants, but their biological context remains unclear. Integrating GWAS summary statistics with single-cell RNA-sequencing (scRNA-seq) dat...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Adolescent engagement and sentiment toward reproductive-health videos on Chinese social media: a cross-sectional content analysis](https://www.medrxiv.org/content/10.1101/2025.06.18.25329831v2)
  来源：medRxiv | 日期：2026-09-13 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Background Adolescent reproductive health information is increasingly sought on social-media platforms, yet the scope, credibility, and emotional reception of such content remain unclear in China. This study examined how...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 低优先级

### 数据集 / Benchmark

- [BeitAI-pHLA: Multiallele Peptide-HLA Class I Binding Prediction Using Protein Language Model and Multi-Instance Learning.](https://pubmed.ncbi.nlm.nih.gov/42729647/)
  来源：PubMed | 日期：2026-01-01 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Human leukocyte antigen (HLA) molecules participate in cellular immune responses by binding to peptide fragments derived from antigens. Exploring this process is crucial to understanding the mechanisms and underlying fac...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Accuracy Overstates Evidence Grounding and Abstention Reliability in Mammography Vision-Language Models](https://www.medrxiv.org/content/10.64898/2026.09.10.26361944v1)
  来源：medRxiv | 日期：2026-09-11 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Answer accuracy alone cannot determine whether a Vision-Language Model (VLM) relies on clinically relevant mammographic evidence or recognizes when that evidence is unavailable. We introduce an evidence-grounded selectiv...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Context Matters in LLM-Assisted Qualitative Data Analysis: Workflow Development and Multidimensional Evaluation in Health Research](https://www.medrxiv.org/content/10.64898/2026.09.07.26362410v1)
  来源：medRxiv | 日期：2026-09-11 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly used for qualitative analysis, but strong language performance does not guarantee strong interpretation when meaning depends on method and context. We developed a context-spe...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Generative model of patient health states and pan-cancer risk stratification](https://www.medrxiv.org/content/10.64898/2026.09.09.26362676v1)
  来源：medRxiv | 日期：2026-09-11 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：While large language models are powerful generators of new text, forecasting disease progression from longitudinal health histories remains a challenging problem. We introduce GenEHR, an autoregressive generative model t...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Evaluation of AI-assisted summarisation of tertiary clinical genomics reports: results of the QNOMX-VHIR-CPSP-001 Phase 1 study](https://www.medrxiv.org/content/10.64898/2026.09.10.26362656v1)
  来源：medRxiv | 日期：2026-09-11 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Background. Comprehensive genomic reports in oncology contain complex molecular information that must be translated into concise summaries for treating clinicians. Manual summarisation is time-intensive, and robust evide...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
