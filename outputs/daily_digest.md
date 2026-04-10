# 每日论文监控日报 (2026-04-10)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 6 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：429 Client Error: Too Many Requests
- PubMed：成功，命中 58 篇
- bioRxiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='api.biorxiv.org', port=443): Read timed out. (read timeout=60)
- medRxiv：成功，命中 3 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### 方法创新

- [Causal Prediction of TP53 Variant Pathogenicity Using a Perturbation-Informed Protein Language Model.](https://pubmed.ncbi.nlm.nih.gov/41955512/)
  来源：PubMed | 日期：2026-04-09 | 相关度：10.0 | 新颖度：5.75
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：准确预测变异的功能影响对于理解人类疾病（特别是 TP53 等癌症相关基因）至关重要。尽管高通量突变分析提升了变异效应预测（VEP）能力，但通用型模型在错义突变分类上仍存在局限。本研究开发了 CaVepP53，这是一种针对 TP53 特化的预测模型，通过扰动实验变异数据对蛋白质语言模型（PLM）进行微调。该模型通过计算野生型与突变体嵌入向量之间的欧几里得距离，并结合逻辑变换推导置信度评分，实现对突变致病性的量化分类。基准测试表明，CaVe...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [A survey on large language models in biology and chemistry.](https://pubmed.ncbi.nlm.nih.gov/41258076/)
  来源：PubMed | 日期：2026-04-08 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：人工智能正通过提供适应生物系统复杂性的可扩展计算框架重塑生物医学研究。其核心是生物/化学语言模型（包括大语言模型），这些模型将分子结构重新概念化为一种适用于先进计算技术的“语言”。本文批判性地审视了这些模型在生物学和化学中的作用，追踪了其从分子表示到分子生成与优化的演变。综述涵盖了生物大分子和有机小分子的关键表示策略，包括蛋白质和核苷酸序列、单细胞数据、基于字符串的化学格式、基于图的编码以及三维点云，并分析了其在AI应用中的优劣。讨论进...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 产品应用 / 监测落地

- [Leveraging Open-Source Large Language Models to Identify Undiagnosed Patients with Rare Genetic Aortopathies](https://www.medrxiv.org/content/10.1101/2025.09.05.25333227v2)
  来源：medRxiv | 日期：2026-04-07 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：罕见遗传性主动脉病由于表型异质性常被漏诊，延迟诊断可能导致致命的心脏后果。虽然基因检测可实现早期预防性干预，但其高度依赖初级保健医生对遗传症状的识别。本研究开发了一种基于开源大语言模型（LLM）的基因检测推荐流程，利用检索增强生成（RAG）技术结合精选的遗传性主动脉病语料库，从非结构化临床文本中提取相关知识以识别潜在受益患者。该流程在宾夕法尼亚大学生物样本库（Penn Medicine BioBank）的 500 名受试者（250 例病...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Using Relative Risk Rankings to Understand Information Differences in Multimodal Prediction Models](https://www.medrxiv.org/content/10.1101/2025.10.30.25339162v2)
  来源：medRxiv | 日期：2026-04-07 | 相关度：7.1 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：本研究探讨了在多模态临床预测模型中，使用专家撰写的摘要（如放射报告）替代原始模态数据（如医学影像）是否会损失预后信息。研究人员利用视觉语言模型（VLMs），针对出院后 30 天死亡率预测任务，对比了胸部 X 光片（CXRs）与其配对放射报告的预测效用。基于 MIMIC-IV/MIMIC-CXR 数据集的子集（n=1,360），研究以出院记录摘要为全局临床背景，分别加入 CXR 影像或放射报告进行增强。结果显示，“出院记录+CXR”模型性...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### 方法创新

- [spRefine denoises and imputes spatial transcriptomic data with a reference-free framework powered by genomic language model.](https://pubmed.ncbi.nlm.nih.gov/41633767/)
  来源：PubMed | 日期：2026-04-07 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：空间转录组数据分析常受限于高噪声水平和基因测量缺失，且其成本远高于传统单细胞数据。为解决这一挑战，研究者开发了 spRefine，这是一个利用基因组语言模型（Genomic Language Models, gLMs）对空间转录组数据进行联合去噪和插补的深度学习框架。该框架采用无参考（Reference-free）设计，实验结果表明，spRefine 在去噪和插补后能生成更稳健的细胞级和位点级表示，显著提升了数据整合效果。此外，spRe...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [CRISPR/Cas12a: A Comprehensive Review from Structural Foundations to Applications in Nucleic Acid Precision Detection.](https://pubmed.ncbi.nlm.nih.gov/41889087/)
  来源：PubMed | 日期：2026-04-08 | 相关度：3.05 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：CRISPR/Cas12a 技术凭借其独特的反向切割（trans-cleavage）活性，已从基因编辑工具演变为强大的分子检测工具。本文系统阐述了 Cas12a 的结构基础与分子机制，重点探讨了该技术如何将特定核酸识别转化为级联信号放大。其应用涵盖病原体诊断、物种鉴定、食品安全及中药材鉴别。通过与等温扩增及多模态检测平台集成，Cas12a 推动了分子诊断向便携化、可视化和定量化方向发展。文章进一步讨论了在灵敏度、定量准确性、crRNA ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
