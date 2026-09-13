# 每日论文监控日报 (2026-09-13)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 4 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：429 Client Error: Unknown Error
- PubMed：成功，命中 50 篇
- bioRxiv：失败，命中 0 篇，错误：504 Server Error: Gateway Timeout
- medRxiv：失败，命中 0 篇，错误：('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

今天这一档没有命中论文。

## 可追踪

### 数据集 / Benchmark

- [BeitAI-pHLA: Multiallele Peptide-HLA Class I Binding Prediction Using Protein Language Model and Multi-Instance Learning.](https://pubmed.ncbi.nlm.nih.gov/42729647/)
  来源：PubMed | 日期：2026-01-01 | 相关度：5.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Human leukocyte antigen (HLA) molecules participate in cellular immune responses by binding to peptide fragments derived from antigens. Exploring this process is crucial to understanding the mechanisms and underlying fac...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 产品应用 / 监测落地

- [Advancing One Health genomics in Africa: opportunities and challenges for outbreak and antimicrobial resistance control.](https://pubmed.ncbi.nlm.nih.gov/42262139/)
  来源：PubMed | 日期：2026-09-10 | 相关度：8.3 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：SUMMARYAfrica's ongoing struggles with emerging epidemics and antimicrobial resistance (AMR) underscore the urgency of integrating pathogen genomics and surveillance systems into the continent's One Health strategy, part...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Fine-Tuning Large Language Models for Structured Extraction of Infectious Disease-Related Information From Clinical Notes in Japanese Primary Care: Development and Internal Validation Study.](https://pubmed.ncbi.nlm.nih.gov/42721099/)
  来源：PubMed | 日期：2026-09-10 | 相关度：7.45 | 新颖度：0.5
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：The COVID-19 pandemic highlighted the importance of timely infectious disease surveillance. In Japan, conventional sentinel and claims-based systems incur reporting lags and capture limited clinical detail, whereas free-...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### 数据集 / Benchmark

- [Genomic language model for predicting enhancers and their allele-specific activity in the human genome.](https://pubmed.ncbi.nlm.nih.gov/42723633/)
  来源：PubMed | 日期：2026-09-10 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Predicting and deciphering the regulatory logic of enhancers remains a significant challenge due to their complex sequence features and the absence of consistent genetic or epigenetic signatures that distinguish them fro...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。
