# 每日论文监控日报 (2026-04-08)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 6 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：429 Client Error: Too Many Requests
- PubMed：成功，命中 23 篇
- bioRxiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='api.biorxiv.org', port=443): Read timed out. (read timeout=60)
- medRxiv：成功，命中 7 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [Tokenizing loops of antibodies.](https://pubmed.ncbi.nlm.nih.gov/41936024/)
  来源：PubMed | 日期：2026-12-31 | 相关度：9.15 | 新颖度：5.0
  匹配主题：foundation_model_agent
  中文摘要：抗体的互补决定区（CDR）是与抗原相互作用的关键环状结构，对新型生物药物设计至关重要。现有表征方法覆盖范围有限，且难以整合进蛋白质基础模型。本研究提出 Igloo（免疫球蛋白环标记器），这是一种编码主链二面角和序列的多模态抗体环标记器。Igloo 采用对比学习目标训练，将具有相似主链二面角的环在潜在空间中映射得更近。相比现有蛋白质编码方法，Igloo 能更高效地从结构数据库中检索匹配的环结构，在识别相似 H3 环方面优于现有方法 6.1...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [Digital Registrar: A Schema-First Framework for Multi-Cancer Privacy-Preserving Pathology Abstraction via Local LLMs](https://www.medrxiv.org/content/10.1101/2025.10.21.25338475v8)
  来源：medRxiv | 日期：2026-04-05 | 相关度：8.9 | 新颖度：1.7
  匹配主题：foundation_model_agent
  中文摘要：手术病理报告包含精细的癌症诊断数据，但其自由文本格式阻碍了自动化登记和二次分析。本研究开发了“Digital Registrar”框架，其核心是基于美国病理学家协会（CAP）标准的临床本体，通过严格类型的分层架构和 DSPy 签名实现。该系统涵盖 10 种主要癌症类型，涉及 193 个登记字段，包括淋巴结组和手术切缘等复杂变量。研究利用 DSPy 框架构建了与模型无关的提取流水线，并在单块 48GB GPU 上测试了本地部署的可行性。实...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 产品应用 / 监测落地

- [Leveraging Open-Source Large Language Models to Identify Undiagnosed Patients with Rare Genetic Aortopathies](https://www.medrxiv.org/content/10.1101/2025.09.05.25333227v2)
  来源：medRxiv | 日期：2026-04-07 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：罕见遗传性主动脉病常因表型异质性导致漏诊，延误诊断可能引发致命心脏后果。虽然基因检测可实现早期干预，但目前高度依赖初级保健医生对症状的识别与转诊。由于临床记录包含丰富的叙述性细节，本研究开发了一种基于开源大语言模型（LLM）的基因检测推荐流程，利用检索增强生成（RAG）技术结合精选的遗传性主动脉病语料库，从非结构化文本中识别潜在患者。该流程在宾夕法尼亚大学生物样本库（Penn Medicine BioBank）的 500 名个体（250...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Using Relative Risk Rankings to Understand Information Differences in Multimodal Prediction Models](https://www.medrxiv.org/content/10.1101/2025.10.30.25339162v2)
  来源：medRxiv | 日期：2026-04-07 | 相关度：7.1 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：多模态临床预测模型常将原始影像替换为专家撰写的文本摘要以简化流程，但这种替代是否保留了预后信息尚不明确。本研究利用视觉语言模型（VLM），对比了胸部X光片（CXR）及其配对放射报告在预测出院后30天死亡率中的效用。研究基于MIMIC-IV/MIMIC-CXR数据集（n=1,360），以出院记录为全局临床背景，分别加入CXR或放射报告进行增强。结果显示，“出院记录+CXR”模型性能最优（AUROC=0.864），优于“仅出院记录”（AUR...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### 产品应用 / 监测落地

- [Cognitive AI-Assisted Primary Care Health Delivery: A Pilot Study in Bangladesh](https://www.medrxiv.org/content/10.64898/2026.04.03.26349253v1)
  来源：medRxiv | 日期：2026-04-05 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：全球医生短缺严重威胁基层医疗服务，而现有医疗AI多侧重于风险评分，未能有效缩短诊疗时间。2025年1月的研究指出，大语言模型（LLM）在缺乏信息时无法主动提问以收集病史并更新鉴别诊断，缺乏可靠医学推理所需的元认知能力。本研究报告了2025年在孟加拉国开展的ClinicalAssist试点部署，该系统旨在复制临床工作流的每一个步骤。在涉及239名唯一患者、277次就诊和287次诊断机会的测试中，该系统实现了94.7%的总体诊断准确率，其中...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Reproducibility and Robustness of Large Language Models for Mobility Functional Status Extraction](https://www.medrxiv.org/content/10.64898/2026.04.03.26350117v1)
  来源：medRxiv | 日期：2026-04-05 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：临床叙述性文本包含关键患者信息，但由于语言变异和记录习惯，提取仍具挑战。大语言模型（LLMs）在临床信息提取（IE）中表现出色，但其在临床部署中至关重要的可重复性（重复运行的稳定性）和鲁棒性（提示词微小变化下的稳定性）尚未得到一致量化。本研究评估了三种代表性开源 LLM：稠密通用模型 Llama 3.3、混合专家（MoE）通用模型 Llama 4 以及领域微调医学模型 MedGemma。研究聚焦于基于国际功能、残疾和健康分类（ICF）框...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
