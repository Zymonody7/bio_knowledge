# 每日论文监控日报 (2026-08-29)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 36 篇新论文。

## 抓取状态

- arXiv：成功，命中 46 篇
- PubMed：成功，命中 42 篇
- bioRxiv：失败，命中 0 篇，错误：503 Server Error: Service Unavailable
- medRxiv：失败，命中 0 篇，错误：503 Server Error: Service Unavailable

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [MLLMCLIP: Feature-Level Distillation of MLLM for Robust Vision-Language Representations](http://arxiv.org/abs/2608.25575v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：7.9 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Pretrained vision-language models such as CLIP excel at zero-shot recognition but often fail at compositionality, particularly attribute-object and relational structures. Recent studies mitigate this issue by augmenting ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Recurrence Meets Transformers for Universal Multimodal Retrieval](http://arxiv.org/abs/2509.08897v3)
  来源：arXiv | 日期：2025-09-10 | 相关度：7.5 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：With the rapid advancement of multimodal retrieval and its application in LLMs and multimodal LLMs, increasingly complex retrieval tasks have emerged. Existing methods predominantly rely on task-specific fine-tuning of v...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LLM-Specific Utility for Retrieval-Augmented Generation](http://arxiv.org/abs/2510.11358v4)
  来源：arXiv | 日期：2025-10-13 | 相关度：6.55 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) is typically optimized for topical relevance, yet its success ultimately depends on whether retrieved passages are useful for a large language model (LLM) to generate correct and comp...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Layered Security Framework Against Prompt Injection in RAG-Based Chatbots](http://arxiv.org/abs/2606.19660v2)
  来源：arXiv | 日期：2026-06-17 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Prompt injection is ranked as the most critical vulnerability in large language model (LLM) deployments by the OWASP Top 10 for LLM Applications, yet existing defenses operate at isolated pipeline stages and remain incom...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ProgRouter: Online Progress-Guided Orchestration for Multi-Agent LLM Workflows under Quality-Cost Tradeoffs](http://arxiv.org/abs/2608.25992v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Multi-agent large language model (LLM) workflows have emerged as a powerful paradigm for solving complex, open-ended tasks through collaborative reasoning among specialized LLM agents, but they incur substantial operatin...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Retrieval-Augmented Agentic Rubric Generation for Reliable Medical Response Evaluation](http://arxiv.org/abs/2601.15161v3)
  来源：arXiv | 日期：2026-01-21 | 相关度：6.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) are increasingly used for clinical decision support, where hallucinations and unsafe suggestions may pose direct risks to patient safety. These risks are hard to assess: subtle clinical error...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HypoForge: A Self-Improving Multi-Agent Framework for Automated Hypothesis Generation and Testing via Scientific Skill Learning](http://arxiv.org/abs/2608.25770v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：6.15 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have enabled AI scientist systems to automate scientific discovery, yet existing approaches most rely on static prompting or fixed workflows and fail to accumulate experience for continual im...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Computational Characterization of Pathogenic LMNA Missense Variants: Structural Instability, Altered Binding, and Conformational Dynamics.](https://pubmed.ncbi.nlm.nih.gov/42657169/)
  来源：PubMed | 日期：2026-01-01 | 相关度：10.0 | 新颖度：0.25
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Mutations in the LMNA gene underlie a broad spectrum of laminopathies, including muscular dystrophies, cardiomyopathies, and premature aging syndromes; however, the molecular mechanisms by which missense variants disrupt...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Unlocking Multimodal Protein Language Models at Inference Time](http://arxiv.org/abs/2608.25855v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：7.1 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Multimodal protein language models (pLMs) learn joint protein sequence-structure distributions, and their generation performance should also depend critically on inference-time sampling strategies. Yet prior work has foc...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Multi-Granularity Context-Enhanced RAG over Multimodal Knowledge Graphs](http://arxiv.org/abs/2608.25986v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：6.8 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) is widely used to mitigate hallucination issues in large language models (LLMs) and multimodal large language models (MLLMs). In particular, knowledge graph (KG)-based RAG leverages s...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Reservoir: A Large-Scale Simulated Dataset for Training and Evaluating Epidemiological Models](http://arxiv.org/abs/2608.27408v1)
  来源：arXiv | 日期：2026-08-27 | 相关度：9.65 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Large-scale, standardized datasets have driven many advances in AI-based scientific modeling, from protein structure prediction to natural language processing. Infectious disease epidemiology is increasingly adopting AI ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [The Performance of Large Language Models in Extracting Intestinal Symptoms From Electronic Health Records: Retrospective Observational Study.](https://pubmed.ncbi.nlm.nih.gov/42647073/)
  来源：PubMed | 日期：2026-08-26 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Unstructured electronic health records (EHRs) hinder the monitoring of intestinal infections. Large language models (LLMs) enable automated symptom extraction. However, their clinical validation is limited by a lack of s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ProRetrieval: Learning to Orchestrate Hybrid Search via Executable Program Synthesis](http://arxiv.org/abs/2608.27017v1)
  来源：arXiv | 日期：2026-08-27 | 相关度：5.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Real-world retrieval often composes structured constraints with semantic intents over text and images through arbitrary Boolean logic. Existing hybrid pipelines such as reciprocal rank fusion or self-querying retrievers ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Unleashing the Power of LLMs in Dense Retrieval with Query Likelihood Modeling](http://arxiv.org/abs/2504.05216v5)
  来源：arXiv | 日期：2025-04-07 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Dense retrieval is a crucial task in Information Retrieval (IR), serving as the basis for downstream tasks such as re-ranking and augmenting generation. Recently, large language models (LLMs) have demonstrated impressive...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TAU-Agent: An Agentic Retrieval-Augmented Framework for Traffic Anomaly Understanding](http://arxiv.org/abs/2608.25935v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Traffic Anomaly Understanding (TAU) requires models and systems to detect, reason about, and explain anomalous events in transportation videos. To address this challenge, we propose TAU-Agent, an agentic retrieval-augmen...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Harnessing the Collective Intelligence of AI Agents in the Wild for New Discoveries](http://arxiv.org/abs/2606.10402v2)
  来源：arXiv | 日期：2026-06-09 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Scientific discovery is often a collective process: researchers share partial results, inspect failed attempts, and build on each other's ideas over long time horizons. Recent AI systems have shown that language-model-ba...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Learning the ARTS of Search for Automated Discovery](http://arxiv.org/abs/2606.21891v2)
  来源：arXiv | 日期：2026-06-20 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Scientific discovery can be formulated as an iterative search process over the space of hypotheses and experiments. Contemporary methods navigate this space using heuristics such as MCTS. These algorithms conflate the me...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Graph Engineering in the Era of LLM Agents: From Individual Intelligence to System Intelligence](http://arxiv.org/abs/2608.21156v2)
  来源：arXiv | 日期：2026-08-21 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：LLMs have evolved from language generators to autonomous agents capable of complex, long-horizon tasks. This evolution has produced paradigms including Prompt Engineering to elicit model capabilities, Context Engineering...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [How AI Experiences Art: Emergent Aesthetic Structure in a Self-Supervised Multimodal Embedding Space](http://arxiv.org/abs/2608.27121v1)
  来源：arXiv | 日期：2026-08-27 | 相关度：3.45 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Aesthetics are an important part of the symbolism of artistic works. Although subjective, humans categorize art based on the emotion evoked regardless of modality. What remains under-explored is how AI models form their ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Accelerating Scientific Research with Gemini in the Real-World](http://arxiv.org/abs/2608.26701v1)
  来源：arXiv | 日期：2026-08-27 | 相关度：2.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：We present an extension and comprehensive real-world validation of Co-Scientist, a Gemini-based multi-agent system designed to accelerate end-to-end scientific research across hypothesis generation, experimentation, and ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution](http://arxiv.org/abs/2606.25721v2)
  来源：arXiv | 日期：2026-06-24 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate model outputs through malicious retrieved documents. Existing detection methods typically rely on auxiliary classifi...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LivingRAG: Augmenting Graph RAG with Experience](http://arxiv.org/abs/2608.25960v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Graph-based RAG improves multi-hop question answering by organizing evidence as a knowledge graph. However, most existing RAG systems process each query in isolation and discard useful reasoning from the LLM's response a...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [TriShieldRAG: 3 Rings, One Blind Spot in Layered Defenses for Retrieval-Augmented Generation](http://arxiv.org/abs/2607.23838v2)
  来源：arXiv | 日期：2026-07-26 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) grounds LLM answers in query-time retrieved documents, so reliability depends on what the retriever returns. PoisonedRAG (Zou et al., USENIX Security'25) showed five crafted documents...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [SustainableQA: A Comprehensive Question Answering Dataset for Corporate Sustainability and EU Taxonomy Reporting](http://arxiv.org/abs/2508.03000v3)
  来源：arXiv | 日期：2025-08-05 | 相关度：5.45 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：The growing demand for corporate sustainability transparency, particularly under new regulations like the EU Taxonomy, necessitates precise data extraction from large, unstructured corporate reports, a task for which Lar...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Retrieved But Not Reliable: A Survey on Attacks, and Defenses in Retrieval-Augmented Generation](http://arxiv.org/abs/2608.24977v2)
  来源：arXiv | 日期：2026-08-25 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) enhances large language models by grounding outputs in external knowledge, improving factuality and reducing hallucinations. At the same time, the retrieval-augmented pipeline introdu...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [When RAG Fails to Equalize: Geo-bias in Factual Question Answering over Public Companies](http://arxiv.org/abs/2608.25717v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) is widely assumed to mitigate factual errors in large language models (LLMs), but it remains unclear whether retrieval uniformly compensates for missing knowledge. We study this quest...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [PlanSightRAG: A Visual-First Multimodal RAG for Automating Question Answering and Compliance Checking for Civil Standard Plans](http://arxiv.org/abs/2608.26091v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Civil infrastructure compliance checking has long relied on engineers manually reading legacy 2D plans; however, OCR-based automation strips away the geometry and layout essential for interpreting these plans. We present...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Pointing the Way, Hiding the Destination: Practical Private Dense Retrieval at Scale](http://arxiv.org/abs/2608.25735v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Hosted retrieval-augmented generation (RAG) and semantic search allow users to query valuable provider-held corpora, raising two competing demands: to hide each query and chosen result, yet reveal only the documents that...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Interpreting Latent Protein Language Model Features with Geometric Annotations](http://arxiv.org/abs/2608.26419v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Protein language models (pLMs) encode information about protein sequences which enable downstream tasks such as structure prediction, but their internal representations are not well understood. Sparse autoencoders (SAEs)...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Interpreting Protein Language Model Embeddings via Orthogonal Projection for Protein Fitness Prediction](http://arxiv.org/abs/2608.25548v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Recently, there has been a growing adoption of protein language models (PLMs) in biomedical science. Their embeddings provide a rich numerical representation of protein sequences which achieve state-of-the-art performanc...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SymbolLKG: Towards Verifiable Logical Reasoning via Logical Knowledge Graph and Symbolic Solvers](http://arxiv.org/abs/2608.26836v1)
  来源：arXiv | 日期：2026-08-27 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have demonstrated remarkable proficiency in natural language understanding, yet they struggle with strict multi-step reasoning, frequently suffering from hallucinations and inconsistency. Exi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Beyond Execution: Auditing Experimental Fidelity in LLM-Driven Scientific Research](http://arxiv.org/abs/2608.26753v1)
  来源：arXiv | 日期：2026-08-27 | 相关度：2.1 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：LLM agents used for scientific experimentation must do more than generate executable code: they must implement the reference method faithfully, design experiments that test the paper's claims, and provide evidence suppor...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Why RAGs Hallucinate: Penalty-Aware Evaluation of Retrieval-Augmented Generation Systems with Knowledge-Gap Canaries](http://arxiv.org/abs/2608.26385v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Volume-based accuracy rewards retrieval-augmented generation (RAG) systems for guessing: a system that answers everything outscores one that declines when its knowledge base cannot support an answer. Building on the conf...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [hoBIT: A Profile-Aware Retrieval-Augmented Chatbot for University Academic Advising](http://arxiv.org/abs/2608.26604v1)
  来源：arXiv | 日期：2026-08-27 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：In university academic advising, identical questions can require different answers depending on a student's department, admission cohort, and degree program, causing profile-blind retrievers to surface plausible but inap...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Traumatic Brain Injury: Multi-Omics Insights into Brain Aging, Neurodegeneration, and Precision Therapeutics.](https://pubmed.ncbi.nlm.nih.gov/42660464/)
  来源：PubMed | 日期：2026-08-27 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Traumatic brain injury (TBI) is a major cause of mortality and persistent neurological disability and is increasingly recognized as a potential contributor to accelerated brain aging and long-term neurodegenerative proce...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Assessing the Downstream Utility of Evidence-Aware Retrieval in RAG](http://arxiv.org/abs/2608.26379v1)
  来源：arXiv | 日期：2026-08-26 | 相关度：0.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Retrieval evaluation for retrieval-augmented generation (RAG) is increasingly designed around whether retrieved passages contain evidence that can support generation, rather than topical relevance alone. We study whether...
  为什么值得看：Assessing the Downstream Utility of Evid 与你的主题有弱匹配，暂时保留作低优先级跟踪。
