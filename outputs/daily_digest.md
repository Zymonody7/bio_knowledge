# 每日论文监控日报 (2026-10-17)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 14 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='export.arxiv.org', port=443): Read timed out. (read timeout=60)
- PubMed：成功，命中 41 篇
- bioRxiv：成功，命中 10 篇
- medRxiv：成功，命中 11 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [Multimodal Artificial Intelligence for Cause-of-Death Assignment From Verbal Autopsy Records: A National Benchmark Study in South Africa](https://www.medrxiv.org/content/10.64898/2026.10.15.26364476v1)
  来源：medRxiv | 日期：2026-10-16 | 相关度：7.9 | 新颖度：6.7
  匹配主题：foundation_model_agent
  中文摘要：BACKGROUND Timely cause-of-death (COD) information guides health policy, yet many deaths in low- and middle-income countries are not medically certified. In Africa, fewer than 10% of deaths are. Verbal autopsy (VA) yield...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [Performance evaluation and benchmarking across 16 large language model configurations on a large real-world emergency department triage data set](https://www.medrxiv.org/content/10.64898/2026.05.28.26353935v2)
  来源：medRxiv | 日期：2026-10-16 | 相关度：7.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Background Emergency department (ED) triage is a decision process that determines patient prioritization and resource allocation. Large language models (LLMs) have been proposed as decision-support tools for triage, yet ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Feasibility and Measurement Properties of a Large Language Model-Based Virtual Patient Laboratory for Clinical Reasoning Training in Physical Therapy Students: Single-Arm Pilot Study](https://www.medrxiv.org/content/10.64898/2026.10.13.26364741v1)
  来源：medRxiv | 日期：2026-10-14 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Background: Large language models (LLMs) configured as virtual patients may expand structured practice of clinical reasoning in health professions education. Before testing effectiveness, it must be established whether s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PatientPheX: A Full-Text Biomedical Corpus for Patient-Specific Phenotype Information Extraction](https://www.biorxiv.org/content/10.64898/2026.10.07.757319v1)
  来源：bioRxiv | 日期：2026-10-15 | 相关度：6.15 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Patient-specific phenotype information extraction identifiers and normalizes phenotype entities and links them with individual patients, supporting rare disease research and genotype-phenotype analysis. However, existing...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Closed-Set Annotation to In-Context Discovery: Biologically Grounded LLMs for Cellular Profiling](https://www.biorxiv.org/content/10.64898/2026.10.07.757352v1)
  来源：bioRxiv | 日期：2026-10-14 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Tumour heterogeneity reflects both cellular identity (lineage) and state (active transcriptional programs), yet computational methods generally analyse these axes separately. We introduce CellScribe, a generative framewo...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Protein novelty, sequence similarity, and negative sampling controls reveal benchmark specific discrimination in protein protein interactionprediction](https://www.biorxiv.org/content/10.64898/2026.10.06.757125v1)
  来源：bioRxiv | 日期：2026-10-14 | 相关度：5.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Protein protein interaction (PPI) predictors are often evaluated with random pair splits that permit proteins to recur across training and test sets, while constructed negative pairs can introduce a separate source of be...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 产品应用 / 监测落地

- [Quantifying Cancer Clinical Trial Eligibility Using Artificial Intelligence-Based Matching](https://www.medrxiv.org/content/10.64898/2026.06.03.26354859v2)
  来源：medRxiv | 日期：2026-10-15 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：PURPOSE: To develop and validate an artificial intelligence-enabled platform that combines efficient screening with explicit eligibility logic by converting unstructured cancer trial criteria into reusable structured que...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [BanglaDiaHallu: Hallucinations of large language models and the effect of guideline-grounded retrieval-augmented generation in Bangla diabetes question answering](https://www.medrxiv.org/content/10.64898/2026.10.14.26365587v1)
  来源：medRxiv | 日期：2026-10-16 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly consulted for health advice, but they can produce fluent statements that are false or unsupported, known as hallucinations, and this risk is poorly characterised in low-resou...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### 方法创新

- [Benchmark Self-Triage (BeST): Comparing Self-Triage Systems and Multiple Generations of OpenAI Models Against Preliminary Expert Consensus](https://www.medrxiv.org/content/10.64898/2026.10.12.26365287v1)
  来源：medRxiv | 日期：2026-10-14 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：As digital self-triage becomes more widely used, quality assurance requires evaluation of both emergency recognition and overall agreement with clinical judgement, including how these outcomes differ across generations o...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Decoding super-enhancer regulatory grammar and pathogenic gain-of-function variants directly from DNA sequence](https://www.biorxiv.org/content/10.64898/2026.10.11.756618v1)
  来源：bioRxiv | 日期：2026-10-14 | 相关度：2.7 | 新颖度：0.25
  匹配主题：pathogenomics
  中文摘要：Super-enhancers (SEs) drive cell-identity gene expression, yet their identification relies on epigenomic profiling (e.g., H3K27ac ChIP-seq), precluding discovery in unprofiled cellular states and leaving their underlying...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Chemical foundation models reveal molecular principles underlying glycobiology](https://www.biorxiv.org/content/10.64898/2026.10.13.758502v1)
  来源：bioRxiv | 日期：2026-10-14 | 相关度：1.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：Glycans encode biological specificity through branching, linkage and stereochemical diversity, and have traditionally been modelled using specialised computational representations distinct from those developed for genera...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Community-driven advances in computational mass spectrometry: The perspective of EuBIC-MS members.](https://pubmed.ncbi.nlm.nih.gov/42436009/)
  来源：PubMed | 日期：2026-10-15 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Advances in data acquisition, artificial intelligence, and integrative bioinformatics are driving the rapid evolution of computational mass spectrometry, and in turn, transforming modern proteomics, metabolomics, and lip...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A multimodal precision oncology platform integrating genomics,single-cell transcriptomics, and functional drug screening expandstherapeutic options in pediatric brain tumors](https://www.biorxiv.org/content/10.64898/2026.10.12.758619v1)
  来源：bioRxiv | 日期：2026-10-14 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Precision oncology for pediatric brain tumors mainly relies on clinically validated, targetable genomic alterations, which are often sparse, yield few matched therapies, and do not guide chemotherapy selection. We develo...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Multimodal profiling for prediction of primary resistance to anti-PD-(L)1 therapy in advanced non-small-cell lung cancer: the prospective PIONeeR biomarkers study](https://www.medrxiv.org/content/10.64898/2026.01.09.26343779v3)
  来源：medRxiv | 日期：2026-10-16 | 相关度：3.05 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Background Pretreatment prediction of primary resistance to anti-PD-(L)1 therapy in advanced non-small-cell lung cancer (NSCLC) remains an unmet clinical need. Existing biomarkers - including PD-L1 expression and tumour ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
