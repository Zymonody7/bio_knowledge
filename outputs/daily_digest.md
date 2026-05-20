# 每日论文监控日报 (2026-05-20)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 14 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='export.arxiv.org', port=443): Read timed out. (read timeout=60)
- PubMed：成功，命中 47 篇
- bioRxiv：成功，命中 12 篇
- medRxiv：成功，命中 8 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [A tri-modal contrastive learning framework for protein representation learning.](https://pubmed.ncbi.nlm.nih.gov/41990738/)
  来源：PubMed | 日期：2026-05-18 | 相关度：9.15 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Protein foundation models, particularly protein language models, have shown strong success in learning meaningful protein representations using transformer architectures pretrained on large-scale datasets through self-su...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Advancing Knotted Protein Design with ESM3: Guided Generation and Topological Insights](https://www.biorxiv.org/content/10.64898/2026.05.07.723606v1)
  来源：bioRxiv | 日期：2026-05-18 | 相关度：8.9 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Multimodal protein language models have transformed protein design, yet their capacity to capture complex topological features remains poorly understood. We use knotted proteins, rare structures in which the backbone for...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Sparse autoencoders reveal interpretable cell-type programs in single-cell foundation model representations.](https://pubmed.ncbi.nlm.nih.gov/42155660/)
  来源：PubMed | 日期：2026-05-18 | 相关度：7.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Single-cell foundation models such as scGPT learn rich representations of cellular identity, yet the biological programs encoded in their internal activations remain opaque. We investigate whether sparse autoencoders (SA...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Comparative Study in Surgical AI: Potential and Limitations of Data, Compute, and Scaling](https://www.medrxiv.org/content/10.64898/2026.03.26.26349455v4)
  来源：medRxiv | 日期：2026-05-17 | 相关度：6.8 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：本研究探讨了人工智能在外科图像分析领域的潜力与局限，特别是针对神经外科手术器械检测这一核心任务。研究人员评估了2023年至2026年初发布的19个开源视觉语言模型（VLM）的零样本性能，结果显示仅有一个模型略微超过13.4%的基准线。通过使用LoRA微调Gemma 3 27B模型生成结构化JSON预测，准确率提升至47.63%；而采用专用分类头的方法进一步将准确率提高到51.08%。实验发现，即使将可训练参数增加近三个数量级，验证集准确...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [A phenotype-to-mechanism framework links phenome-wide comorbidity architecture to molecular mechanisms and therapeutic discovery in complex diseases](https://www.medrxiv.org/content/10.64898/2026.05.13.26353128v1)
  来源：medRxiv | 日期：2026-05-17 | 相关度：6.9 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Complex human diseases exhibit substantial clinical heterogeneity driven by poorly understood molecular mechanisms, while many also lack sufficient molecular and omics data for mechanistic investigation, hindering therap...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [DamageFormer: a damage-aware multimodal deep learning framework for DNA lesion identification from nanopore sequencing](https://www.biorxiv.org/content/10.64898/2026.05.14.725245v1)
  来源：bioRxiv | 日期：2026-05-18 | 相关度：6.8 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：Background: DNA lesions arise from endogenous metabolism and environmental exposure and are the major drivers of mutagenesis, aging, and cancer development. However, mapping DNA damage at nucleotide resolution remains a ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Interpretable fine-tuned large language models facilitate making genetic test decisions for rare diseases.](https://pubmed.ncbi.nlm.nih.gov/42156861/)
  来源：PubMed | 日期：2026-05-19 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Clinical decision making often relies on expert judgment guided by established guidelines, which can be challenging to standardize and abstract to implement. For example, selecting between gene panels and whole exome/gen...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### Foundation Model / Agent

- [Evaluating open LLMs for agentic analysis orchestration in a typical biomedical lab](https://www.biorxiv.org/content/10.64898/2026.05.13.724985v1)
  来源：bioRxiv | 日期：2026-05-18 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Agentic tools - software environments where a large language model plans, calls external tools, executes code, and iterates with minimal human intervention - will run a substantial share of routine biomedical data analys...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TogoMCP: Natural Language Querying of Life-Science Knowledge Graphs via Schema-Guided LLMs and the Model Context Protocol](https://www.biorxiv.org/content/10.64898/2026.03.19.713030v2)
  来源：bioRxiv | 日期：2026-05-17 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Querying the RDF Portal knowledge graph maintained by DBCLS, which aggregates approximately 60 life-science databases, requires proficiency in both SPARQL and database-specific RDF schemas, placing this resource beyond t...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Accelerating scientific discovery with Co-Scientist.](https://pubmed.ncbi.nlm.nih.gov/42156544/)
  来源：PubMed | 日期：2026-05-19 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Scientific discovery is driven by scientists generating novel hypotheses for complex problems that undergo rigorous experimental validation. To augment this process, we introduce Co-Scientist, a multi-agent AI system bui...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Unraveling Atherosclerosis through Multi-omics: Systematic Insights into the Unique Applications and Clinical Perspectives.](https://pubmed.ncbi.nlm.nih.gov/42149276/)
  来源：PubMed | 日期：2026-05-18 | 相关度：6.6 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Atherosclerosis (AS) is a progressive disease of the arterial wall characterized by metabolic dysregulation, inflammatory activation, and genetic susceptibility. Given the complex interactions across molecular layers, th...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Sequence-based Drug-Target Binding Site Pre-training Enables Cryptic Pocket Detection and Improves Binding Affinity and Kinetics Prediction](https://www.biorxiv.org/content/10.1101/2025.01.14.633076v3)
  来源：bioRxiv | 日期：2026-05-18 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Predicting protein-ligand binding characteristics, such as affinity and kinetics, is critical for accelerating drug discovery. However, many existing computational methods face key limitations, including insufficient int...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Cosine Similarity Conflates Clinically Distinct Cancer Variants: A Case for Typed-Graph Retrieval in Precision Oncology Decision Support](https://www.biorxiv.org/content/10.64898/2026.05.05.723102v2)
  来源：bioRxiv | 日期：2026-05-17 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）正日益应用于肿瘤临床决策支持，其核心是将患者NGS报告中的体细胞变异匹配至证据分级的治疗方案。然而，RAG系统常用的基于向量余弦相似度的检索架构更侧重语言接近性而非实体身份。本研究评估了9对具有不同FDA批准疗法指示的癌症变异（如EGFR L858R与T790M，KRAS G12C与G12D），涵盖BRAF、EGFR、KRAS等关键基因。实验发现，在PubMedBERT和MedCPT等生物医学编码器下，100%的临...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Circulating Tumor DNA and Precision Biomarkers in Colorectal Cancer: Implications for Diagnosis, Monitoring, and Management of Advanced Disease.](https://pubmed.ncbi.nlm.nih.gov/42150752/)
  来源：PubMed | 日期：2026-05-18 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Colorectal cancer (CRC) remains one of the leading causes of cancer-related mortality worldwide, with outcomes critically dependent on timely diagnosis, accurate risk stratification, and individualized treatment. Traditi...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
