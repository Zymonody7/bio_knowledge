# 每日论文监控日报 (2026-08-17)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 20 篇新论文。

## 抓取状态

- arXiv：成功，命中 15 篇
- PubMed：成功，命中 29 篇
- bioRxiv：失败，命中 0 篇，错误：Expecting value: line 1 column 1 (char 0)
- medRxiv：失败，命中 0 篇，错误：Expecting value: line 1 column 1 (char 0)

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [NEURON: A Neuro-symbolic System for Grounded Clinical Explainability](http://arxiv.org/abs/2605.01189v3)
  来源：arXiv | 日期：2026-05-02 | 相关度：7.55 | 新颖度：6.7
  匹配主题：foundation_model_agent
  中文摘要：Clinical AI adoption is hindered by the black-box/grey-box nature of high-performing models, which lack the ontological grounding and narrative transparency required for professional-level explainability. We present NEUR...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [Event-Grounded Question Answering over Long Audio via Structured Retrieval](http://arxiv.org/abs/2602.14612v6)
  来源：arXiv | 日期：2026-02-16 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Answering natural-language questions over multi-hour audio requires reliable event recognition, temporal grounding, and efficient retrieval. We present LA-RAG (Long Audio Retrieval-Augmented Generation), a structured fra...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Adaptive Stopping for Multi-Turn LLM Reasoning](http://arxiv.org/abs/2604.01413v3)
  来源：arXiv | 日期：2026-04-01 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) increasingly rely on multi-turn reasoning and interaction, such as adaptive retrieval-augmented generation (RAG) and ReAct-style agents, to answer difficult questions. These methods improve a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AtomBridge: Agentic VLA Inference Plugin for Long-Horizon Tasks in Scientific Experiments](http://arxiv.org/abs/2602.09430v2)
  来源：arXiv | 日期：2026-02-10 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Robotic laboratories play a critical role in autonomous scientific discovery by enabling scalable, continuous experimental execution. Recent vision-language-action (VLA) models offer a promising foundation for robotic la...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AutoSchema: Live Schema Grounding for Agentic Text-to-Sparql over Heterogeneous Knowledge Graphs](http://arxiv.org/abs/2608.14228v1)
  来源：arXiv | 日期：2026-08-14 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Life science knowledge graphs make large collections of structured data available through SPARQL, but each resource uses its own schema, identifiers, and links. TogoMCP helps language model agents query these resources b...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Fine-grained Claim-level RAG Benchmark for Law](http://arxiv.org/abs/2605.21071v4)
  来源：arXiv | 日期：2026-05-20 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：The rapid progress of large language models (LLMs) is shifting semantic search toward a question-answering paradigm, where users ask questions and LLMs generate responses. In high-stake domains such as law, retrieval-aug...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Aligning protein-generative models to experimental fitness with ProteinDPO.](https://pubmed.ncbi.nlm.nih.gov/42601461/)
  来源：PubMed | 日期：2026-08-14 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Biological generative models can predict biological functions without task-specific training data but often under-perform specialized models. This is due to a fundamental 'alignment gap', where the rules learned during u...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Multi-omics precision diagnosis of brucellosis: Advances in biomarker discovery and clinical application.](https://pubmed.ncbi.nlm.nih.gov/42128325/)
  来源：PubMed | 日期：2026-08-15 | 相关度：7.4 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics, application_monitoring
  中文摘要：Brucellosis, a neglected zoonosis caused by intracellular Brucella bacteria, remains a formidable global public health challenge, especially in developing regions. The notorious ability of Brucella to evade host immunity...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [CytoBERT: A Foundation Model for Cytometry Data](http://arxiv.org/abs/2608.14414v1)
  来源：arXiv | 日期：2026-08-14 | 相关度：2.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：Cytometry measures the complex characteristics of single cells (e.g., counts and protein expression of immune cells) and is widely used across immunological research and clinical settings. However, cytometry data is high...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ScienceFlow: A long-horizon agent for ML research, scientific discovery and beyond](http://arxiv.org/abs/2608.14354v1)
  来源：arXiv | 日期：2026-08-14 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Enabling LLM agents to sustain productive, stable, and goal-aligned research over extended horizons is a central challenge for autonomous machine learning and scientific discovery, as progress hinges on continuously mana...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [RL-Index: Reinforcement Learning for Retrieval Index Reasoning](http://arxiv.org/abs/2606.16316v2)
  来源：arXiv | 日期：2026-06-15 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Retrieving external knowledge is crucial for real-world tasks but remains difficult when queries and relevant knowledge are linked by implicit reasoning (e.g., shared theorems or coding logic). Existing methods rely main...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Model-agnostic Retrieval-Augmented Extended Forecasting for time series](http://arxiv.org/abs/2608.14054v1)
  来源：arXiv | 日期：2026-08-14 | 相关度：2.1 | 新颖度：7.25
  匹配主题：未命中具体主题
  中文摘要：Time series forecasting with pretrained foundation models has demonstrated strong zero-shot capabilities. However, achieving optimal performance on time series with short or negligible historical data in domain-specific ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Integrating stemness and epithelial-mesenchymal transition signatures with machine learning identifies RUNX1 as a therapeutic vulnerability in colorectal cancer.](https://pubmed.ncbi.nlm.nih.gov/42372471/)
  来源：PubMed | 日期：2026-08-15 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Colorectal cancer (CC) arises from a complex interplay between genetic and epigenetic alterations within the colorectal mucosa, resulting in unchecked cellular proliferation and tumor development. This complexity results...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Emerging and Re-Emerging Viral Infections in Poultry: Integrating Traditional and AI-Based Control Strategies.](https://pubmed.ncbi.nlm.nih.gov/42599520/)
  来源：PubMed | 日期：2026-08-14 | 相关度：5.45 | 新颖度：0.25
  匹配主题：pathogenomics, application_monitoring
  中文摘要：Poultry production remains significantly challenged by emerging and re-emerging avian viral diseases, which are influenced by host-pathogen interactions, viral evolution, and intensified farming systems. Viruses like avi...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Beyond Morphology: Reframing Lymph-Node Metastasis Prediction Through Clonal Ecology-Decades-Long Genomic Instability and Polyclonal-to-Monoclonal Transitions as the Missing Dimension in Cancer.](https://pubmed.ncbi.nlm.nih.gov/42598790/)
  来源：PubMed | 日期：2026-08-14 | 相关度：3.75 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Recent whole-genome, lineage-tracing, single-cell, and spatial studies have reshaped our understanding of tumor evolution, revealing that cancers can arise from polyclonal populations, undergo decades-long genomic instab...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Machine learning and AI for cancer research and care: a review of applications, limitations, and future directions.](https://pubmed.ncbi.nlm.nih.gov/42599390/)
  来源：PubMed | 日期：2026-08-14 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Machine learning (ML) is transforming cancer research and care by enabling analysis of complex, high-dimensional datasets spanning genomics, transcriptomics, proteomics, imaging, and clinical records. By improving risk s...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Bridging innovation and implementation in laboratory medicine: insights from a global survey on unmet needs and emerging technologies.](https://pubmed.ncbi.nlm.nih.gov/42119761/)
  来源：PubMed | 日期：2026-08-15 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Technological innovation in laboratory medicine is advancing rapidly, driven by artificial intelligence, next-generation sequencing, high-resolution mass spectrometry, novel biomarkers, and decentralized point-of-care te...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [The Past and Future of AI Scientists](http://arxiv.org/abs/2608.14407v1)
  来源：arXiv | 日期：2026-08-14 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：We present a survey of the past and future of AI Scientists: machines capable of automating science. AI Scientists can originate hypotheses, deduce their consequences, design and execute experiments, interpret their resu...
  为什么值得看：The Past and Future of AI Scientists 与你的主题有弱匹配，暂时保留作低优先级跟踪。

- [GEM: A Generative Embedding Model Bridging Reasoning and Retrieval](http://arxiv.org/abs/2608.13200v2)
  来源：arXiv | 日期：2026-08-13 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Modern LLMs excel at reasoning and instruction following, enabling users to express complex and diverse information needs. However, conventional retrievers largely rely on surface-level matching between queries and docum...
  为什么值得看：GEM: A Generative Embedding Model Bridgi 与你的主题有弱匹配，暂时保留作低优先级跟踪。

- [How Much Do Legal RAG Systems Still Hallucinate?](http://arxiv.org/abs/2608.14210v1)
  来源：arXiv | 日期：2026-08-14 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Hallucination is a major challenge for retrieval-augmented generation (RAG) systems in the legal domain, where ungrounded answers can lead to serious consequences. To better understand this problem, we conduct a fine-gra...
  为什么值得看：How Much Do Legal RAG Systems Still Hall 与你的主题有弱匹配，暂时保留作低优先级跟踪。
