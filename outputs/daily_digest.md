# 每日论文监控日报 (2026-09-09)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 14 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：429 Client Error: Unknown Error
- PubMed：成功，命中 31 篇
- bioRxiv：成功，命中 13 篇
- medRxiv：成功，命中 10 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [From code to natural language: MErlin - a multiomics toolkit for bacterial epigenomics delivered as Claude agent skill.](https://www.biorxiv.org/content/10.64898/2026.09.02.748773v1)
  来源：bioRxiv | 日期：2026-09-06 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Interpreting a bacterial methylome is a multi-omics problem. It requires integrating modified-base calls with genome annotation, motif inventories, methyltransferase genotypes, transcript abundance, replichore position a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Large language model-driven knowledge graph learning for herb-macromolecule interaction prediction and functional analysis.](https://pubmed.ncbi.nlm.nih.gov/42705563/)
  来源：PubMed | 日期：2026-09-07 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：The rapid accumulation of biological macromolecule data has created an urgent need for computational methods capable of characterizing the functional roles of macromolecular targets in complex therapeutic systems. Tradit...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Auditing Large Language Model-Generated Digital Standardized Patients for Demographic Bias: A Simulation Study with HIV Pre-Exposure Prophylaxis Screening as a Tracer Condition](https://www.medrxiv.org/content/10.64898/2026.09.01.26361928v1)
  来源：medRxiv | 日期：2026-09-07 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are entering clinical training as digital standardized patients (DSPs), simulated patient encounters the model scripts and portrays. Demographic associations learned from corpus co-occurrence...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Comparative Study in Surgical AI: Potential and Limitations of Data, Compute, and Scaling](https://www.medrxiv.org/content/10.64898/2026.03.26.26349455v5)
  来源：medRxiv | 日期：2026-09-07 | 相关度：6.8 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Recent Artificial Intelligence (AI) models have matched or exceeded human experts in several benchmarks of biomedical task performance, but multi-modal benchmarks involving surgery in particular are often missing from pr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A user-friendly, no-code, application for HIPAA-compliant automated analysis of tabular data at scale](https://www.medrxiv.org/content/10.64898/2026.09.06.26362377v1)
  来源：medRxiv | 日期：2026-09-08 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Background: Clinical research often requires reviewing large volumes of unstructured electronic medical record (EMR) data, a time-consuming task demanding skilled personnel. Large language models (LLMs) like ChatGPT can ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Using large language models to facilitate literature review and data extraction for infectious disease models: COVID-19 as a test case](https://www.medrxiv.org/content/10.64898/2026.09.06.26362399v1)
  来源：medRxiv | 日期：2026-09-08 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Infectious disease transmission models are governed by parameters informed by systematic review of epidemiological literature. Large language models (LLMs) could facilitate this, but the reliability of the results to inf...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [OmniSyn unifies target-aware molecular generation and optimization within a synthesis-native LLM framework across the human proteome](https://www.biorxiv.org/content/10.64898/2026.09.02.748775v1)
  来源：bioRxiv | 日期：2026-09-06 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Designing target-specific bioactive molecules with actionable synthesis routes for the human proteome holds enormous potential for expanding therapeutic discovery, but remains a challenge. Existing target-aware generativ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Reasoning Before Disposition: A Model-Agnostic Cannot-Miss Discipline for Quiet Emergencies and the Case for Deterministic Enforcement](https://www.medrxiv.org/content/10.64898/2026.09.02.26362074v1)
  来源：medRxiv | 日期：2026-09-08 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models now match clinicians on medical-knowledge benchmarks. Whether they can safely triage a patient message is a separate question, and the highest-consequence failure in triage is the emergency that nev...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [UKB-KG: Knowledge Graph for Integrating and Enhancing Biomedical Insights from the UK Biobank](https://www.medrxiv.org/content/10.64898/2026.09.02.26361902v1)
  来源：medRxiv | 日期：2026-09-07 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：The UK Biobank (UKB) is a cornerstone of modern biomedical research, providing unparalleled data to advance the understanding, prediction, and treatment of diseases. Its contributions span genetics, genomics, disease pre...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Coarse composition suffices: tabular in-context learning for multi-activity antimicrobial peptide profiling](https://www.biorxiv.org/content/10.64898/2026.08.27.747591v2)
  来源：bioRxiv | 日期：2026-09-06 | 相关度：4.7 | 新颖度：1.5
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Antimicrobial peptides (AMPs) often act against multiple pathogen classes, making multi-label activity prediction a more realistic screening target than binary antimicrobial classification. The ESCAPE benchmark formalize...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [PromptBio: An Agentic Platform for End-to-End Computational Biomedical Research](https://www.biorxiv.org/content/10.64898/2026.09.02.748774v1)
  来源：bioRxiv | 日期：2026-09-06 | 相关度：2.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Modern biomedical research increasingly depends on complex computational analyses, yet translating a scientific question into a reliable workflow still requires substantial technical expertise and manual coordination. Pr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [AtlasFold: Protein structure prediction with metagenomic-scale language models](https://www.biorxiv.org/content/10.64898/2026.09.04.749352v1)
  来源：bioRxiv | 日期：2026-09-07 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Protein language models (PLMs) trained on evolutionary sequences learn representations that encode protein structure, enabling direct structure prediction without multiple-sequence alignments (MSAs). Here we present the ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ProMaya: a hierarchical universal Deep Learning framework for accurate and interpretable Protein-Protein interaction identification](https://www.biorxiv.org/content/10.64898/2026.04.03.716278v2)
  来源：bioRxiv | 日期：2026-09-08 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Protein-protein interactions (PPIs) are molecular lego which define the physical states of cells. Accurately identifying PPIs remains challenging due to the interplay of several factors ranging from electrostatic to mole...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Machine learning-enabled wastewater-based surveillance for emerging pathogen detection and monitoring: current applications, challenges, and future prospects.](https://pubmed.ncbi.nlm.nih.gov/42704107/)
  来源：PubMed | 日期：2026-09-07 | 相关度：5.0 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Abstract Wastewater-based surveillance (WBS) has become an important public-health tool for tracking community-level circulation of emerging and re-emerging pathogens, but wastewater measurements are not directly interpr...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
