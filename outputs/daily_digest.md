# 每日论文监控日报 (2026-11-20)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 56 篇新论文。

## 抓取状态

- arXiv：成功，命中 46 篇
- PubMed：成功，命中 44 篇
- bioRxiv：成功，命中 15 篇
- medRxiv：成功，命中 10 篇

## 最值得看

### Foundation Model / Agent

- [Natural Language Processing: An Applied Research Practicum From Classical Text Processing to Multimodal and Agentic Systems](http://arxiv.org/abs/2605.03799v4)
  来源：arXiv | 日期：2026-05-05 | 相关度：7.9 | 新颖度：6.2
  匹配主题：foundation_model_agent
  中文摘要：This preprint presents a systematic, research-oriented guide to modern natural language processing, covering the full NLP pipeline from tokenisation, text normalisation, vector representations, and classical machine lear...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [A Neurosymbolic Multimodal Framework for 30-Day Diabetic Readmission Prediction: Integrating Structured EHR Data, Dense Clinical Embeddings, and Knowledge-Grounded Symbolic Extraction](http://arxiv.org/abs/2611.25236v1)
  来源：arXiv | 日期：2026-11-18 | 相关度：7.8 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Unplanned 30-day readmissions among patients with diabetes mellitus impose a substantial clinical and economic burden, yet most predictive models use only structured electronic health record (EHR) data and ignore free-te...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

## 可追踪

### Foundation Model / Agent

- [GenNA: Conditional generation of nucleotide sequences guided by natural language annotations.](https://pubmed.ncbi.nlm.nih.gov/43050525/)
  来源：PubMed | 日期：2026-11-20 | 相关度：8.5 | 新颖度：3.84
  匹配主题：foundation_model_agent
  中文摘要：Deciphering the mapping between biomolecular sequences and complex biological functions is a central challenge in genomics. While existing generative nucleotide models capture sequence distributions, they lack explicit a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LUNA-FM: a subword foundation model for long non-coding RNAs for functional inference.](https://pubmed.ncbi.nlm.nih.gov/43023405/)
  来源：PubMed | 日期：2026-12-01 | 相关度：7.55 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：RNA foundation models (FMs) have shown promise for RNA identification and functional annotation. However, many use single-nucleotide tokenization, which produces long input sequences and can increase computational costs ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DEO: Training-Free Direct Embedding Optimization for Negation-Aware Retrieval](http://arxiv.org/abs/2603.09185v2)
  来源：arXiv | 日期：2026-03-10 | 相关度：7.5 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) have enabled diverse retrieval methods. However, existing retrieval methods often fail to accurately retrieve results for negation ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Prospective prediction of clinical trial outcomes from public evidence](https://www.medrxiv.org/content/10.64898/2026.11.17.26368242v1)
  来源：medRxiv | 日期：2026-11-19 | 相关度：7.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Predicting clinical trial outcomes requires interpreting biological and clinical evidence in the context of a specific intervention, population and study design. Here we test whether a general-purpose large language mode...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Incorporating argumentation frameworks for LLM decision-making: Task-specific design and evaluation](http://arxiv.org/abs/2611.25361v1)
  来源：arXiv | 日期：2026-11-19 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Argumentation frameworks (AFs) provide explicit, formal mechanisms for representing and resolving conflicts and thus have been incorporated into large language model (LLM) decision-making. The benefits vary and depend on...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Hybrid RAG Framework for Deceptive Review Detection: Integrating RoBERTa-LoRA, FAISS-Based Retrieval, and LLM Reasoning](http://arxiv.org/abs/2611.24049v1)
  来源：arXiv | 日期：2026-11-18 | 相关度：6.55 | 新颖度：1.2
  匹配主题：foundation_model_agent
  中文摘要：The growth of deceptive online opinions poses a critical risk of misinformation and fraud. This paper proposes a Retrieval-Augmented Generation (RAG) system to automatically distinguish spam reviews. The architecture int...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agentic MLIR-to-QIR Translation with Dual-Backend Testing: A Hybrid Deterministic and LLM Approach](http://arxiv.org/abs/2611.25106v1)
  来源：arXiv | 日期：2026-11-18 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Quantum frameworks each define their own Multi-Level Intermediate Representation (MLIR) dialect, so porting a circuit to a Quantum Intermediate Representation (QIR) runtime needs a hand-written pass per dialect. Our tran...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [statLens enables accurate and interpretable statistical intelligence](https://www.biorxiv.org/content/10.64898/2026.11.16.767003v1)
  来源：bioRxiv | 日期：2026-11-17 | 相关度：5.45 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Diverse existing approaches and analyses of large-scale biomedical omics datasets along with the complexity of the corresponding statistical analytical workflows pose challenges to the direct application of large languag...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LLM4Rail: An LLM-Augmented Personalized Railway Services Platform](http://arxiv.org/abs/2507.23377v2)
  来源：arXiv | 日期：2025-07-31 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have significantly reshaped different walks of business. To meet the increasing demands for individualized railway service, we develop LLM4Rail - a novel LLM-augmented personalized railway se...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SPARK: Adaptive Parametric Knowledge Participation for Faithful Retrieval-Augmented Generation](http://arxiv.org/abs/2606.27786v3)
  来源：arXiv | 日期：2026-06-26 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) enhances the faithfulness of large language models (LLMs) by incorporating external knowledge into the generation process. However, conflicts between retrieved context and parametric ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AutoRAGBench: A Benchmark for LLM Agents Automating RAG System Development](http://arxiv.org/abs/2611.25582v1)
  来源：arXiv | 日期：2026-11-19 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) is a well-established paradigm for augmenting large language models (LLMs) with information retrieved from external corpora. However, developing effective RAG systems requires substan...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Industrial Product Documentation to Automated Digital Product Passport Generation: An Experimental Study of Large Language Models](http://arxiv.org/abs/2611.24998v1)
  来源：arXiv | 日期：2026-11-18 | 相关度：5.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Manufacturing companies that are planning to sell certain products in the European Union (EU) will be required to provide mandatory digital product passports (DPPs). The use of DPPs is to provide standardized product inf...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A General Harness for Protein Foundation Model Fitness Prediction](http://arxiv.org/abs/2609.34654v2)
  来源：arXiv | 日期：2026-09-28 | 相关度：3.95 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Accurate fitness prediction is central to protein engineering and understanding sequence-function relationships. With advances in deep learning, protein foundation models (PFMs) have become widely used for this task. Rec...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [MINA: Do frozen DNA encoders beat sequence composition? A homology-aware linear-probe benchmark](https://www.biorxiv.org/content/10.64898/2026.05.25.727711v4)
  来源：bioRxiv | 日期：2026-11-17 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：冻结的 DNA 编码器常被用作特征提取器，但微调过程往往掩盖了其固定嵌入向量中已包含的线性可访问信息。本研究引入了 MINA（核苷酸架构模型询问），这是一个轻量级基准测试，旨在评估冻结的 DNA 嵌入是否能恢复：(i) 五类蛋白质家族标签，以及 (ii) 每个基因的 1,536 维 GenePT 自然语言嵌入。实验对比了编码序列（CDS）和转录起始位点（TSS）背景，采用同源性感知划分，并与翻译后的组成成分及蛋白质语言模型基准进行比较。...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Rate-distortion Assessment for Hierarchical Content Summarization](http://arxiv.org/abs/2611.25151v1)
  来源：arXiv | 日期：2026-11-18 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Powerful generative models including large language and vision models have demonstrated success across a wide range of content generation, editing and manipulation tasks via end-to-end prompt-based generation. However, c...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Deciphering the Biological Function of Tandem Mass Spectra Using a Dual-Modal Metabolite Language Model](https://www.biorxiv.org/content/10.64898/2026.11.16.766993v1)
  来源：bioRxiv | 日期：2026-11-17 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Liquid chromatography-tandem mass spectrometry untargeted metabolomics captures thousands of metabolic peaks from biological samples. Conventional identification-dependent metabolomics workflows require confident structu...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [DeepQuest: From Knowledge Gaps to Scientific Discovery in Alzheimer's Disease](http://arxiv.org/abs/2611.26343v1)
  来源：arXiv | 日期：2026-11-19 | 相关度：5.75 | 新颖度：6.56
  匹配主题：foundation_model_agent
  中文摘要：Automating experiments does not necessarily advance scientific understanding. Research agents must identify meaningful knowledge gaps, determine what available data can resolve, and assess whether their findings advance ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SMSTPred: Protein Language Model Embeddings Predict SAM-Methyltransferase Substrate Specificity and Reveal Metabolite Methyltransferasome Enrichment in Plants and Actinomycetota](https://www.biorxiv.org/content/10.64898/2026.11.13.766537v1)
  来源：bioRxiv | 日期：2026-11-17 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：S-adenosyl-methionine (SAM)-dependent methyltransferases (MTases) are one of the largest and most ancient enzyme superfamilies in biology, transferring a methyl group from SAM to substrates as different as DNA, RNA, prot...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [S-PLM-TM enables fast and accurate sequence-based search for remote homologs](https://www.biorxiv.org/content/10.64898/2026.11.16.767046v1)
  来源：bioRxiv | 日期：2026-11-17 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Protein structures and functions can remain conserved after extensive sequence divergence, but detecting these distant relationships across large databases remains challenging. Here we present S-PLM-TM, a sequence-only r...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ALIoTh: Orchestrating Multi-Agent LLMs for Autonomous IoT Penetration Testing](http://arxiv.org/abs/2611.25809v1)
  来源：arXiv | 日期：2026-11-19 | 相关度：5.45 | 新颖度：5.68
  匹配主题：foundation_model_agent
  中文摘要：Penetration testing in Internet of Things (IoT) environments, especially those composed of various different devices, e.g., smart plugs, smart cameras, and smart doors, presents great challenges across the phases of info...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [LSP-RAG: Latent Scoring Perspectives for Knowledge Graph Retrieval-Augmented Generation](http://arxiv.org/abs/2611.25229v1)
  来源：arXiv | 日期：2026-11-18 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have demonstrated strong capabilities in open-domain question answering, but often struggle with factual accuracy and multi-hop reasoning due to the incompleteness of the training corpora. A ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Virtual spatial transcriptomics links kidney histopathology to disease-associated molecular programs](https://www.medrxiv.org/content/10.64898/2026.11.17.26368273v1)
  来源：medRxiv | 日期：2026-11-19 | 相关度：3.75 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Introduction: Spatial transcriptomics can resolve compartment-specific molecular programs in kidney disease, but its cost and technical requirements limit its use in clinical diagnostics and in large biopsy archives. Pre...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 其他

- [Fine-tuned encoders, generative large language models and typed decisions for classifying findings in chest CT reports: paired English-Japanese internal testing and external testing on naturally written Japanese reports](https://www.medrxiv.org/content/10.64898/2026.11.18.26368388v1)
  来源：medRxiv | 日期：2026-11-19 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Purpose: To compare fine-tuned encoders, generative large language models (LLMs) and typed decisions (per-finding yes/no questions answered with a probability) for classifying 18 findings in chest CT reports, and to iden...
  为什么值得看：medRxiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Evaluation of System One Models on Biomedical Texts](https://www.medrxiv.org/content/10.64898/2026.11.15.26368126v1)
  来源：medRxiv | 日期：2026-11-17 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Objective To compare the performance and cost of System One models (SOMs) with general-purpose large language models (LLMs) on biomedical tasks and evaluate confidence-based routing. Materials and Methods We evaluated th...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [The Effectiveness and Durability of Pretraining Data Filtering in Protein Language Models](http://arxiv.org/abs/2610.26651v2)
  来源：arXiv | 日期：2026-10-19 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Pretraining filtering is one of the most common safeguards for open-weight language models. Here we study its effectiveness, durability and scalability using the ESM-2 family of protein language models. We find that filt...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HYPER: Hypothesis-Guided Planning for Evidence-Seeking Retrieval](http://arxiv.org/abs/2603.19008v2)
  来源：arXiv | 日期：2026-03-19 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) improves Large Language Models (LLMs) by grounding generation in external, non-parametric knowledge. However, when a task requires choosing among competing possibilities, such as a di...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Human-Agentic AI Collaboration Workflow for Trend Analysis of ChatGPT Applications in Healthcare](https://www.medrxiv.org/content/10.64898/2026.11.14.26368120v1)
  来源：medRxiv | 日期：2026-11-17 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：BackgroundWith the rapid advancement of artificial intelligence (AI), large language models (LLMs) such as ChatGPT have demonstrated strong potential to transform healthcare research and practice. However, LLMs are proba...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Glyph: An Interpretability Engine for AI-Driven Scientific Discovery from Clinical Data](http://arxiv.org/abs/2611.08922v2)
  来源：arXiv | 日期：2026-11-06 | 相关度：4.45 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Automated scientific discovery has the potential to advance understanding of disease mechanisms and accelerate identification of early disease markers. Manual data annotation is infeasible at population scale, motivating...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [KnowledgeClaw: Towards Agentic Knowledge Engineering via Omnimodal Hypergraphs](http://arxiv.org/abs/2611.24294v1)
  来源：arXiv | 日期：2026-11-18 | 相关度：3.45 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Knowledge engineering (KE) turns raw files into a reasoning-ready knowledge base, a task now within reach of LLM agents. KE has progressed from chunk and graph retrieval-augmented generation (RAG) to memory agents, agent...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [AI Companions for Young Adult Caregivers: Practical Advice, Emotional Depth, and the Limits of Metric Evaluation](http://arxiv.org/abs/2611.23147v1)
  来源：arXiv | 日期：2026-11-17 | 相关度：2.5 | 新颖度：1.5
  匹配主题：未命中具体主题
  中文摘要：Young adult caregivers (YACs) are individuals aged 18 to 25 currently taking care of a family member, partner, or friend facing chronic illness. AI companions designed specifically for YACs remain underexplored in prior ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [In-Context Optimization for Retrieval-Augmented Generation: A Gradient-Descent Perspective](http://arxiv.org/abs/2605.26356v2)
  来源：arXiv | 日期：2026-05-25 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：In-context learning has recently been linked to implicit gradient descent in linear self-attention models, suggesting that context can induce a forward-pass update. Retrieval-augmented generation (RAG) also relies on con...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Toward Agentic Retrieval-Augmented Generation for Enterprise Retail Workflows over Heterogeneous Data Sources](http://arxiv.org/abs/2610.25096v3)
  来源：arXiv | 日期：2026-10-18 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Enterprise retail workflows require agents to chain evidence across heterogeneous sources, from structured product and order records to unstructured inquiries and reviews, yet existing agentic RAG benchmarks rarely captu...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Capability Framework for Evaluating Agentic AI Platforms in Regulated Enterprises](http://arxiv.org/abs/2611.24039v1)
  来源：arXiv | 日期：2026-11-18 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Agentic AI platforms-systems in which LLM agents plan, invoke tools, retain memory and coordinate to change the state of enterprise systems-are being procured faster than they can be measured. Public agent benchmarks sco...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MemeLogos: Knowledge-Driven Retrieval-Augmented Reasoning for Harmful Meme Detection](http://arxiv.org/abs/2610.15463v3)
  来源：arXiv | 日期：2026-10-11 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：With the rapid proliferation of social media, harmful memes have become a growing threat to online ecosystems. Their harmfulness is often implicitly conveyed through complex interactions among visual, textual, and contex...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Ethical Risks of Medical AI Agents and a Governance Framework: A Systematic Review of Current Applications and Policy Responses.](https://pubmed.ncbi.nlm.nih.gov/43048115/)
  来源：PubMed | 日期：2026-11-17 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：This systematic review identified ethical risks associated with medical AI agents and developed a governance framework adapted to China's healthcare context. PubMed, Web of Science, China National Knowledge Infrastructur...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MINTEval: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems](http://arxiv.org/abs/2605.18565v3)
  来源：arXiv | 日期：2026-05-18 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Real-world agents operate over long and evolving horizons, where information is repeatedly updated and may interfere across memories, requiring accurate recall and aggregated reasoning over multiple pieces of information...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Steering Automated Scientific Discovery via Audited Epistemic Exploration](http://arxiv.org/abs/2611.25214v1)
  来源：arXiv | 日期：2026-11-18 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Scientific discovery requires revisiting the hypotheses in light of new evidence and identifying promising directions beyond those already explored. However, research agents often make claims that are not supported by th...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [DS2Agent: Holistic Device Agents for Accelerated Embedded Board-Level Design](http://arxiv.org/abs/2611.25774v1)
  来源：arXiv | 日期：2026-11-19 | 相关度：0.7 | 新颖度：5.37
  匹配主题：未命中具体主题
  中文摘要：Embedded board-level development demands extensive expertise, from component selection and device characteristics to interface configuration, driver writing, and system composition. Recently, LLM-based agents have shown ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [AI-readiness criteria for biomedical data in functional genomics and clinical medicine](https://www.biorxiv.org/content/10.1101/2024.10.23.619844v7)
  来源：bioRxiv | 日期：2026-11-17 | 相关度：1.7 | 新颖度：6.25
  匹配主题：未命中具体主题
  中文摘要：生物医学研究正迅速转向人工智能（AI）驱动模式，但生物医学数据的复杂性要求在“模型前”阶段（涵盖数据获取、转换和伦理治理）实施稳健的可操作标准，以确保AI的伦理性和可解释性（XAI）。研究指出，单纯遵循FAIR原则（可发现、可访问、可互操作、可重用）已不足以满足AI建模需求。为此，NIH Bridge2AI标准工作组定义了生物医学数据“AI就绪”（AI-readiness）的标准与实践，涵盖七个核心维度：FAIR性、溯源性、特征化、伦理...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Democratizing Cross-Project Knowledge for Transforming Water Governance and Climate Resilience: an Agentic AI Ecosystem](http://arxiv.org/abs/2611.26398v1)
  来源：arXiv | 日期：2026-11-19 | 相关度：0.7 | 新颖度：7.15
  匹配主题：未命中具体主题
  中文摘要：EU-funded projects produce extensive evidence in the form of deliverables, reports, and case studies. However, this knowledge is typically scattered across projects and document structures, making it difficult to locate ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [StringQFT: A Multiuse Textbook Resource for AI-Assisted Theoretical Physics](http://arxiv.org/abs/2611.23225v1)
  来源：arXiv | 日期：2026-11-17 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：We present StringQFT as a textbook collection for string constructions of quantum field theory and as infrastructure for AI-assisted theoretical physics. The collection comprises 18 volumes, 190 chapters and 3,795 pages,...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Evidence-Based Credit Assignment for Search-Augmented Language Models](http://arxiv.org/abs/2611.23824v1)
  来源：arXiv | 日期：2026-11-18 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Reinforcement learning from terminal answer rewards enables search-augmented language models to interleave reasoning and retrieval without step-level annotations, yet outcome supervision assigns identical credit to every...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Auditing the adversarial robustness of genomic foundation models with SafeGenes.](https://pubmed.ncbi.nlm.nih.gov/43044595/)
  来源：PubMed | 日期：2026-11-17 | 相关度：4.65 | 新颖度：1.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Genomic foundation models (GFMs) such as evolutionary scale modeling (ESM) are increasingly applied to variant effect prediction in clinical genomics, yet their adversarial robustness remains underexplored. We present Sa...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [An Explainable and Scalable Hierarchical Tensor Framework for Integrating Multi-Omics and Digital Pathomics](http://arxiv.org/abs/2611.25584v1)
  来源：arXiv | 日期：2026-11-19 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Background: Precision oncology requires integration of heterogeneous molecular and pathology data, yet many fusion models offer limited biologically grounded interpretability and struggle with missing modalities. Methods...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RagHarnessDebugger: Jev-Guided Agentic RAG in Contract Inference Repair Auditing](http://arxiv.org/abs/2611.22991v1)
  来源：arXiv | 日期：2026-11-17 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Agentic systems using retrieval-augmented generation (RAG) must repair their own answers by gathering more evidence, testing alternative policies and deciding if, when, and what repairs are needed. Yet how do we know if ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RAVEN: A Self-RAG Based Agent for Threat Classification and Response](http://arxiv.org/abs/2611.25832v1)
  来源：arXiv | 日期：2026-11-19 | 相关度：0.7 | 新颖度：5.47
  匹配主题：未命中具体主题
  中文摘要：Security event analysis in large enterprises can be overwhelming, as each alert typically requires manual in- spection by human operators. This process is time-consuming and prone to inconsistencies, especially in high-v...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Agentic AI versus pediatric emergency physicians for differential diagnosis of acutely ill and injured children](https://www.medrxiv.org/content/10.64898/2026.11.16.26367440v1)
  来源：medRxiv | 日期：2026-11-18 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Background Misdiagnosis and delayed diagnosis of children in pediatric emergency departments lead to complications, and are particularly problematic in settings with limited pediatric expertise. Large language models (LL...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Applications of computer vision in mosquito-borne diseases: A systematic review.](https://pubmed.ncbi.nlm.nih.gov/43056402/)
  来源：PubMed | 日期：2026-11-19 | 相关度：3.65 | 新颖度：5.75
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Mosquito-borne diseases (MBDs) remain a major global health challenge. Vector surveillance, pathogen detection, and clinical diagnosis are central to control efforts but are limited by labor-intensive workflows and short...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Genetic variants of transthyretin amyloidosis with cardiomyopathy associated with low sensitivity to bone scintigraphy: a systematic review.](https://pubmed.ncbi.nlm.nih.gov/43055171/)
  来源：PubMed | 日期：2026-11-19 | 相关度：3.05 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Transthyretin cardiac amyloidosis (ATTR-CA) is characterized by amyloid deposition and frequently leads to a progressive cardiomyopathy with poor prognosis. Bone scintigraphy with 99m Tc-labeled tracers is the cornerston...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [A Biologically Interpretable Single-Cell Pathology Foundation Model for Molecular Decoding of H&E Images](https://www.biorxiv.org/content/10.64898/2026.11.14.766416v1)
  来源：bioRxiv | 日期：2026-11-17 | 相关度：1.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：The microscopic structure of human tissues encodes molecular information that is not directly accessible by visual inspection. Current pathology foundation models improve histological interpretation but operate at multic...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [TCC-RAG: Temporal Causal Chain-Guided RAG for Temporal Knowledge Graph Question Answering](http://arxiv.org/abs/2610.38366v2)
  来源：arXiv | 日期：2026-10-28 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in large language models (LLMs) have spurred growing interest in temporal knowledge graph question answering (TKGQA). Most existing methods rely on semantic retrieval augmented generation (RAG), which suf...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [When Detection Does Not Guarantee Resistance: Reasoning and Poisoned Context in RAG](http://arxiv.org/abs/2608.17153v5)
  来源：arXiv | 日期：2026-08-17 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) exposes large language models to knowledge-poisoning attacks, where misinformation injected into retrieved documents can influence model outputs. Prior work has shown that models may ...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [Quantifying the Intrusiveness of Retrofitting Retrieval-Augmented Generation onto Legacy Software Systems](http://arxiv.org/abs/2611.23931v1)
  来源：arXiv | 日期：2026-11-18 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Enterprises increasingly add retrieval-augmented generation (RAG) to existing REST and monolithic systems, usually by writing an ad hoc HTTP call into a handler, and have no way to quantify how intrusive that choice is. ...
  为什么值得看：Quantifying the Intrusiveness of Retrofi 与你的主题有弱匹配，暂时保留作低优先级跟踪。

- [When Is Additional Retrieval Worthwhile? A Cost-Aware Study of Evidence Gain and Answer Reliability in RAG](http://arxiv.org/abs/2610.37358v2)
  来源：arXiv | 日期：2026-10-27 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Retrieval-augmented generation (RAG) can benefit from more sophisticated retrieval, but extra retrieval may be unnecessary for many questions and gains in evidence retrieval may not translate into faithful or correct ans...
  为什么值得看：When Is Additional Retrieval Worthwhile? 与你的主题有弱匹配，暂时保留作低优先级跟踪。
