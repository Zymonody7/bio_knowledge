# 每日论文监控日报 (2026-09-21)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 12 篇新论文。

## 抓取状态

- arXiv：成功，命中 8 篇
- PubMed：成功，命中 27 篇
- bioRxiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='api.biorxiv.org', port=443): Read timed out. (read timeout=60)
- medRxiv：成功，命中 6 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [Role of foundation models in data-driven tissue diagnostics.](https://pubmed.ncbi.nlm.nih.gov/42759410/)
  来源：PubMed | 日期：2026-09-18 | 相关度：7.8 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence (AI)-based tissue diagnostics is entering a new phase driven by pathology foundation models: large-scale encoders and multimodal systems pretrained with self-supervised and vision-language objecti...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Large language model linguistic perplexity in childhood onset psychosis: unique features and developmental trends](https://www.medrxiv.org/content/10.64898/2026.09.17.26363314v1)
  来源：medRxiv | 日期：2026-09-20 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Objective: Child and early adolescent onset psychosis (COP) is associated with subtle changes in language linked to thought disorder, a key contributor to functional impairment. Large language models (LLM) can detect dev...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [An Interpretable Memory Decision Controller for LLM Agents Based on Three-Signal Complementarity: Decoupling Confidence and Consistency](http://arxiv.org/abs/2609.22043v1)
  来源：arXiv | 日期：2026-09-18 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Memory systems for large language models have focused predominantly on efficient retrieval, whereas the decision of whether retrieved memories should be trusted has received comparatively little attention. When the memor...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Knowledge-Graph Based Augmentation versus Retrieval Augmented Generation for Cultural-Related Question Answering](http://arxiv.org/abs/2609.18317v2)
  来源：arXiv | 日期：2026-09-16 | 相关度：6.55 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) suffer from a long-tail deficit: culturally specific facts, particularly those concerning underrepresented regions such as Latin America, appear too rarely in pretraining corpora to be reliab...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Micro-Collaborative Poisoning: A Distributed Attack on RAG Systems](http://arxiv.org/abs/2609.21573v1)
  来源：arXiv | 日期：2026-09-18 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) improves large language models by grounding outputs in external knowledge sources, but this dependency also creates a surface for poisoning attacks. This paper introduces Micro-Collab...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

## 低优先级

### Foundation Model / Agent

- [Artificial intelligence in onco-anaesthesia: Current applications, challenges, and future directions.](https://pubmed.ncbi.nlm.nih.gov/42625971/)
  来源：PubMed | 日期：2026-09-20 | 相关度：3.75 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Artificial intelligence (AI) is transforming onco-anaesthesia by shifting practice from reactive physiological management toward predictive and precision-based care. This review outlines current AI applications across th...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BEAT-Net: Injecting Biomimetic Spatio-Temporal Priors for Interpretable ECG Diagnosis](http://arxiv.org/abs/2601.07316v2)
  来源：arXiv | 日期：2026-01-12 | 相关度：2.4 | 新颖度：7.0
  匹配主题：未命中具体主题
  中文摘要：Automated electrocardiogram diagnosis using deep learning remains limited by signal-agnostic representations that treat multi-lead recordings as undifferentiated time-series or images, forcing models to rediscover physio...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Reducing Barriers to Academic Support: Evaluating a Course-Specific RAG System for Addressing Help-Seeking Disparities in Higher Education](http://arxiv.org/abs/2609.21600v1)
  来源：arXiv | 日期：2026-09-18 | 相关度：2.1 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Access to academic support is a key determinant of student success, yet students experience it unequally: some readily seek help from lecturers or tutors, while others hesitate due to anxiety, fear of judgement, uncertai...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [PersonalAI 2.0: Enhancing knowledge graph traversal/retrieval with planning mechanism for Personalized LLM Agents](http://arxiv.org/abs/2605.13481v3)
  来源：arXiv | 日期：2026-05-13 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：We introduce PersonalAI 2.0 (PAI-2), a novel framework designed to enhance LLM-based systems through integration of external knowledge graphs (KGs). The proposed approach addresses key limitations of existing Graph Retri...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Identifying cohorts at elevated risk of cancers using generative modeling of patient health states](https://www.medrxiv.org/content/10.64898/2026.09.09.26362676v2)
  来源：medRxiv | 日期：2026-09-19 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：While large language models are powerful generators of new text, forecasting disease progression from longitudinal health histories remains a challenging problem. We introduce GenEHR, an autoregressive generative model t...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Climate change impact on disease emergence and antimicrobial resistance: A perspective on transmission and detection.](https://pubmed.ncbi.nlm.nih.gov/42699333/)
  来源：PubMed | 日期：2026-09-18 | 相关度：3.7 | 新颖度：0.25
  匹配主题：pathogenomics
  中文摘要：Climate change is increasingly disrupting environmental and ecological systems, creating conditions that facilitate the emergence, transmission, and persistence of infectious diseases and the spread of antimicrobial resi...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [AutoRecLab: Describe the Experiment, Get the Code!](http://arxiv.org/abs/2609.21863v1)
  来源：arXiv | 日期：2026-09-18 | 相关度：2.05 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Empirical evaluation is central to recommender-systems (RecSys) research, but turning experimental designs into executable code remains a manual and error-prone task. We present AutoRecLab, a Python-based autonomous RecS...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。
