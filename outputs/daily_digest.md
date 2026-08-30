# 每日论文监控日报 (2026-08-30)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 17 篇新论文。

## 抓取状态

- arXiv：成功，命中 12 篇
- PubMed：成功，命中 35 篇
- bioRxiv：成功，命中 12 篇
- medRxiv：成功，命中 6 篇

## 最值得看

### 方法创新

- [Expert-Guided Visual Correction for Characterizing Diagnostic Performance and Error Patterns of Multimodal Large Language Models Using Periodontal In-Service Examination Images](https://www.medrxiv.org/content/10.64898/2026.08.21.26360755v1)
  来源：medRxiv | 日期：2026-08-27 | 相关度：7.8 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Multimodal large language models (MLLMs) are increasingly applied to image-based clinical reasoning, yet their diagnostic reliability in periodontal image interpretation, and the underlying source of their errors, remain...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

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

- [A complementary learning system for continual episodic memory in large language models](https://www.biorxiv.org/content/10.64898/2026.08.24.746712v1)
  来源：bioRxiv | 日期：2026-08-27 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Humans retain memories of individual experiences for a lifetime, an ability attributed to a complementary learning system in which a fast process encodes episodes and a slow process integrates them into semantic knowledg...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Intent Drift in LLM-Assisted Brain Computer Interface Communication: An In-Silico Benchmark Under Simulated Decoder Corruption](https://www.medrxiv.org/content/10.64898/2026.08.20.26360939v1)
  来源：medRxiv | 日期：2026-08-27 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Background Large language models are increasingly proposed to post-edit decoded text in communication brain-computer interfaces and augmentative communication. A fluent model can substitute a different intent than attemp...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [TaHL-PTM: Post-Translational Modification Prediction in Proteins via Target-Hooked Discriminative Fine-Tuning of Decoder-only Protein Language Models](https://www.biorxiv.org/content/10.64898/2026.08.24.746791v1)
  来源：bioRxiv | 日期：2026-08-27 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Post-translational modifications (PTMs) regulate protein function, making accurate residue-level PTM prediction essential for understanding cellular mechanisms and disease pathways. While decoder-only protein language mo...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [TRACE: A FINE-TUNED BIOMEDICAL LANGUAGE MODEL FOR DIRECTIONALLY INFORMED DRUG REPURPOSING FROM TRANSCRIPTOME-WIDE ASSOCIATION STUDIES](https://www.medrxiv.org/content/10.64898/2026.08.25.26361263v1)
  来源：medRxiv | 日期：2026-08-28 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Transcriptome-wide association studies (TWAS) can identify genes where genetically predicted gene expression is associated with disease risk, but translating those signals into therapeutic opportunities remains time-cons...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Anniemap: Vector Search for Viral Short Read Alignment](https://www.biorxiv.org/content/10.64898/2026.08.26.747390v1)
  来源：bioRxiv | 日期：2026-08-28 | 相关度：5.6 | 新颖度：5.25
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Background: The process of aligning sequencing reads to a reference genome is a foundational step in genomic analysis, underpinning tasks from variant detection to pathogen surveillance. In viral genomics, however, this ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Reservoir: A Large-Scale Simulated Dataset for Training and Evaluating Epidemiological Models](http://arxiv.org/abs/2608.27408v1)
  来源：arXiv | 日期：2026-08-27 | 相关度：9.65 | 新颖度：0.75
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Large-scale, standardized datasets have driven many advances in AI-based scientific modeling, from protein structure prediction to natural language processing. Infectious disease epidemiology is increasingly adopting AI ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

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

### 方法创新

- [SymbolLKG: Towards Verifiable Logical Reasoning via Logical Knowledge Graph and Symbolic Solvers](http://arxiv.org/abs/2608.26836v1)
  来源：arXiv | 日期：2026-08-27 | 相关度：4.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Large Language Models (LLMs) have demonstrated remarkable proficiency in natural language understanding, yet they struggle with strict multi-step reasoning, frequently suffering from hallucinations and inconsistency. Exi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Data-centric feedback loops for next-generation immunotherapy development.](https://pubmed.ncbi.nlm.nih.gov/42665646/)
  来源：PubMed | 日期：2026-08-28 | 相关度：3.05 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Despite explosive growth in biomedical data generation, driven largely by genomics, and in computational capabilities, the probability that a candidate entering phase I ultimately reaches approval has remained stubbornly...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Beyond Execution: Auditing Experimental Fidelity in LLM-Driven Scientific Research](http://arxiv.org/abs/2608.26753v1)
  来源：arXiv | 日期：2026-08-27 | 相关度：2.1 | 新颖度：1.25
  匹配主题：未命中具体主题
  中文摘要：LLM agents used for scientific experimentation must do more than generate executable code: they must implement the reference method faithfully, design experiments that test the paper's claims, and provide evidence suppor...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Traumatic Brain Injury: Multi-Omics Insights into Brain Aging, Neurodegeneration, and Precision Therapeutics.](https://pubmed.ncbi.nlm.nih.gov/42660464/)
  来源：PubMed | 日期：2026-08-27 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Traumatic brain injury (TBI) is a major cause of mortality and persistent neurological disability and is increasingly recognized as a potential contributor to accelerated brain aging and long-term neurodegenerative proce...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
