# 每日论文监控日报 (2026-06-06)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 60 篇新论文。

## 抓取状态

- arXiv：成功，命中 49 篇
- PubMed：成功，命中 61 篇
- bioRxiv：成功，命中 21 篇
- medRxiv：成功，命中 17 篇

## 最值得看

### Foundation Model / Agent

- [Retrieval and competition: how a protein foundation model starts a protein](http://arxiv.org/abs/2605.16331v2)
  来源：arXiv | 日期：2026-05-05 | 相关度：8.0 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Protein language models are increasingly used to guide experimental and clinical decisions, yet it is often unclear whether a confident prediction reflects recognition of biological evidence or retrieval of a statistical...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Clinician-Centered Evaluation of Large Language Model-Generated Discharge Summaries for Longer Hospitalizations: Insights from Hospitalists and Primary Care Physicians](https://www.medrxiv.org/content/10.64898/2026.06.03.26354858v1)
  来源：medRxiv | 日期：2026-06-05 | 相关度：7.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Although large language models (LLMs) have shown promise for discharge summary generation, their value may be greater in longer hospitalizations, where increasing documentation volume and complexity increase both clinici...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Learning residue-level context for modeling protein-protein interactions](https://www.biorxiv.org/content/10.64898/2026.06.01.729118v1)
  来源：bioRxiv | 日期：2026-06-04 | 相关度：9.55 | 新颖度：5.25
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Protein language models (PLMs) enable prediction of protein properties by learning residue-level features from sequence, yet most PLM-based approaches to protein-protein interactions aggregate information across entire p...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [An Infectious Disease Spread Simulation Based on Large Language Model Decision Making](http://arxiv.org/abs/2606.06360v1)
  来源：arXiv | 日期：2026-06-04 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Modelling individual decision-making during infectious disease outbreaks is crucial for understanding behavioural dynamics and informing effective public health interventions. Prior work has shown that large language mod...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [SciDER: Scientific Data-centric End-to-end Researcher](http://arxiv.org/abs/2603.01421v3)
  来源：arXiv | 日期：2026-03-02 | 相关度：6.8 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：While large language models accelerate scientific discovery, existing agents face severe limitations in adaptability, domain generalization, and multimodal scalability, often struggling to autonomously process raw, domai...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [BRepCLIP: Contrastive Multimodal Pretraining on BRep Primitives for CAD Understanding](http://arxiv.org/abs/2606.05515v1)
  来源：arXiv | 日期：2026-06-03 | 相关度：6.8 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Learning representations of CAD models is a largely open problem. While 3D representation learning has flourished around point clouds and meshes, the native format of CAD - boundary representations BReps, which encodes e...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [LDARNet: DNA Adaptive Representation Network with Learnable Tokenization for Genomic Modeling](http://arxiv.org/abs/2606.04552v1)
  来源：arXiv | 日期：2026-06-03 | 相关度：6.55 | 新颖度：7.0
  匹配主题：foundation_model_agent
  中文摘要：Genomic foundation models increasingly adopt large language model architectures, yet almost universally rely on fixed tokenization schemes such as $k$-mers, BPE, or single nucleotides, which impose arbitrary sequence bou...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Toward Pre-Deployment Assurance for Enterprise AI Agents: Ontology-Grounded Simulation and Trust Certification](http://arxiv.org/abs/2606.04037v2)
  来源：arXiv | 日期：2026-06-02 | 相关度：6.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Pre-deployment verification of enterprise artificial intelligence (AI) agents remains a critical gap between large language model (LLM) capability benchmarking and production deployment. Post-deployment monitoring, human...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [QCFuse: Query-Aware Cache Fusion via Compressed View for Efficient RAG Serving](http://arxiv.org/abs/2606.05875v1)
  来源：arXiv | 日期：2026-06-04 | 相关度：6.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-augmented generation (RAG) improves large language model (LLM) answer quality by grounding generation in external evidence, but processing retrieved contexts makes the prefill stage a dominant serving cost. RAG...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery](http://arxiv.org/abs/2606.06473v1)
  来源：arXiv | 日期：2026-06-04 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Large language model (LLM) agents are increasingly applied to long-horizon tasks such as scientific discovery and machine learning engineering (MLE), where sustained self-evolution becomes a key capability. However, exis...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [HypRAG: Hyperbolic Dense Retrieval for Retrieval Augmented Generation](http://arxiv.org/abs/2602.07739v2)
  来源：arXiv | 日期：2026-02-08 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Embedding geometry plays a fundamental role in retrieval quality, yet dense retrievers for retrieval-augmented generation (RAG) remain largely confined to Euclidean space. However, natural language exhibits hierarchical ...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [MolE-RAG: Molecular Structure-Enhanced Retrieval-Augmented Generation for Chemistry](http://arxiv.org/abs/2606.05693v1)
  来源：arXiv | 日期：2026-06-04 | 相关度：6.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have shown promise for molecular property prediction, but their ability to reason over chemical structures remains limited, as molecular representations such as SMILES differ substantially fr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Autonomous heterogeneous catalyst discovery with a self-evolving multi-agent digital twin](http://arxiv.org/abs/2606.05050v1)
  来源：arXiv | 日期：2026-06-03 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Theoretical heterogeneous catalysis promises rapid catalyst discovery, yet computational and machine-learning predictions often deviate from experiment and stay confined to narrow material families, for want of a faithfu...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Agent-Orchestrated Adaptive RAG: A Comparative Study on Structured and Multi-Hop Retrieval](http://arxiv.org/abs/2606.05658v1)
  来源：arXiv | 日期：2026-06-04 | 相关度：4.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) enhances Large Language Models (LLMs) by grounding their responses in external knowledge, but conventional pipelines rely on static, single-step retrieval that limits performance on c...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Vision Hopfield Memory Networks](http://arxiv.org/abs/2603.25157v2)
  来源：arXiv | 日期：2026-03-26 | 相关度：3.45 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Recent vision and multimodal foundation backbones, such as Transformer families and state-space models like Mamba, have achieved remarkable progress, enabling unified modeling across images, text, and beyond. Despite the...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [Reducing Hallucinations in Complex Question Answering using Simple Graph-based Retrieval-Augmented Generation (long version)](http://arxiv.org/abs/2606.05901v1)
  来源：arXiv | 日期：2026-06-04 | 相关度：6.15 | 新颖度：6.75
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have fundamentally transformed the landscape of Natural Language Processing. Despite these advances, LLMs and LLM-based systems remain prone to a variety of failure modes. Retrieval-augmented...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Performance evaluation and benchmarking across 16 large language models on a comprehensive real-world emergency department triage data set](https://www.medrxiv.org/content/10.64898/2026.05.28.26353935v1)
  来源：medRxiv | 日期：2026-06-05 | 相关度：5.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Background Emergency department (ED) triage is a high-stakes clinical decision process that determines patient prioritization and resource allocation under time pressure. Large language models (LLMs) have recently been p...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [GLM-Prior: a genomic language model for transferable sequence-derived priors in gene regulatory network inference](https://www.biorxiv.org/content/10.1101/2025.06.29.662198v3)
  来源：bioRxiv | 日期：2026-06-03 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Gene regulatory network (GRN) inference depends on high-quality prior knowledge, yet curated priors are often incomplete or unavailable across species and cell types. We present GLM-Prior, a genomic language model fine-t...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Language Modeling Materializes a World Model of Protein Biology](https://www.biorxiv.org/content/10.64898/2026.06.03.729735v1)
  来源：bioRxiv | 日期：2026-06-04 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Proteins are fundamental to life. The full extent of their biology is beyond our ability to characterize with experimental approaches in the physical laboratory. Accurate digital representations could accelerate the disc...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Towards A Generative Protein Evolution Machine with DPLM-Evo](http://arxiv.org/abs/2605.00182v3)
  来源：arXiv | 日期：2026-04-30 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Proteins are shaped by gradual evolution under biophysical and functional constraints. Protein language models learn rich evolutionary constraints from large-scale sequences, and discrete diffusion-based protein language...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Overweight status drives early tumor microenvironment reprogramming in pancreatic ductal adenocarcinoma: a cell-type-resolved Bayesian hierarchical modeling and interactome analysis](https://www.biorxiv.org/content/10.64898/2026.05.14.721695v2)
  来源：bioRxiv | 日期：2026-06-03 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Obesity significantly increases the risk of pancreatic ductal adenocarcinoma, yet a comprehensive understanding of obesity-driven tumor microenvironment remodeling remains incomplete. We developed a cell-type-resolved tr...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CASS-RTL: Correctness-Aware Subspace Steering for RTL Generation with LLMs](http://arxiv.org/abs/2606.05680v1)
  来源：arXiv | 日期：2026-06-04 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Recent advances in large language models (LLMs) have enabled the automatic synthesis (generation) of register-transfer level (RTL) code from natural language instructions, offering a promising pathway to accelerate chip ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Self-Augmenting Retrieval for Diffusion Language Models](http://arxiv.org/abs/2606.06474v1)
  来源：arXiv | 日期：2026-06-04 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Discrete diffusion language models generate text by iteratively denoising an entire response in parallel. At each step, they predict tentative tokens for every masked position, committing the confident predictions to the...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Adaptive Minds: Empowering Agents with LoRA-as-Tools](http://arxiv.org/abs/2510.15416v2)
  来源：arXiv | 日期：2025-10-17 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：We investigate a framework in which LoRA adapters are treated as callable tools that a base language model can dynamically select and invoke. We hypothesize that, when adapters are trained to provide strong domain-specif...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [IA-RAG: Interval-Algebra-Driven Temporal Reasoning for Dynamic Knowledge Retrieval](http://arxiv.org/abs/2606.06044v1)
  来源：arXiv | 日期：2026-06-04 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) has shown strong effectiveness in grounding Large Language Models (LLMs) with external knowledge. However, existing RAG and Graph RAG frameworks largely treat knowledge as static or a...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [RAG Security and Privacy: Formalizing the Threat Model and Attack Surface](http://arxiv.org/abs/2509.20324v2)
  来源：arXiv | 日期：2025-09-24 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Retrieval-Augmented Generation (RAG) is an emerging approach in natural language processing that combines large language models (LLMs) with external document retrieval to produce more accurate and grounded responses. Whi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Revisiting Vul-RAG: Reproducibility and Replicability of RAG-based Vulnerability Detection with Open-Weight Models](http://arxiv.org/abs/2606.04739v1)
  来源：arXiv | 日期：2026-06-03 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) have shown strong potential for automated software vulnerability detection, particularly in retrieval-augmented generation (RAG) settings. However, for approaches relying on proprietary model...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Extracting Social Determinants of Health from Electronic Health Records: Development and Comparison of Rule-Based and Large Language Model Methods](https://www.medrxiv.org/content/10.1101/2025.11.15.25339520v3)
  来源：medRxiv | 日期：2026-06-04 | 相关度：7.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Background Social determinants of health (SDoH) are critical drivers of health outcomes but are often under-documented in structured electronic health record (EHR) data. Instead, SDoH are more commonly recorded in unstru...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Ten Headache Specialists versus Artificial Intelligence for Clinical Literature Summarization: A Critical Evaluation and Comparison](http://arxiv.org/abs/2606.05436v1)
  来源：arXiv | 日期：2026-06-03 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Summarizing the latest medical literature to guide clinical decision-making is essential for evidence-based medicine and high-quality patient care. Yet clinicians face increasing challenges due to limited time with patie...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Quantifying Cancer Clinical Trial Eligibility Using Artificial Intelligence-Based Matching](https://www.medrxiv.org/content/10.64898/2026.06.03.26354859v1)
  来源：medRxiv | 日期：2026-06-05 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：PURPOSE: To develop and validate an artificial intelligence-enabled platform that converts unstructured cancer trial eligibility criteria into structured queries and quantifies trial eligibility across advanced/metastati...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [To RAG, or Not to RAG? A Comparative Evaluation of Retrieval-Augmented Generation for ICD Coding of German Tumor Diagnoses](https://www.medrxiv.org/content/10.64898/2026.05.27.26353695v1)
  来源：medRxiv | 日期：2026-06-03 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Introduction Coding tumor diagnoses from free-text clinical documentation currently requires substantial manual effort. Promising approaches for automating this process include large language mod-els (LLMs), embedding mo...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Towards World Models in Biomedical Research](http://arxiv.org/abs/2606.05925v1)
  来源：arXiv | 日期：2026-06-04 | 相关度：5.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：A central goal of biomedicine is to understand, predict and ultimately control the dynamic mechanisms by which biological systems respond to perturbations, disease progression and therapeutic intervention. Although found...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [FIDES: Faithful Inference via Deep Evidence Signals for Retrieval-Memory Conflict in RAG](http://arxiv.org/abs/2606.05644v1)
  来源：arXiv | 日期：2026-06-04 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：When retrieved evidence contradicts parametric memory, language models frequently ignore context and default to memorized priors -- a failure that undermines the core purpose of retrieval augmentation. Contrastive decodi...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

- [When Should Memory Stay Silent: Measuring Memory-Use Boundaries in Memory-Augmented Conversational Agents](http://arxiv.org/abs/2606.06055v1)
  来源：arXiv | 日期：2026-06-04 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：Long-term memory enables language model agents to support personalized interactions, but it remains unclear when available memories warrant integration into responses. Existing memory evaluations emphasize retrieval accu...
  为什么值得看：arXiv 上的新论文与 foundation_model_agent 相关，可用于补充你当前的病原检测与模型监控视角。

## 低优先级

### Foundation Model / Agent

- [Agentic Authoring of OMOP Concept Sets from Natural Language](https://www.medrxiv.org/content/10.64898/2026.06.02.26354704v1)
  来源：medRxiv | 日期：2026-06-03 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Authoring OMOP concept sets from free-text descriptions remains a major bottleneck in scalable computable phenotyping for observational research. Existing tools support parts of this workflow but are designed primarily f...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Self-Reported Side Effects Among Reddit Users Taking Unapproved Retatrutide](https://www.medrxiv.org/content/10.64898/2026.05.28.26352819v1)
  来源：medRxiv | 日期：2026-06-03 | 相关度：5.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：Gray-market retatrutide use is increasing, but patient safety experiences remain poorly characterized. This cross-sectional analysis examined Reddit posts and comments from retatrutide-specific and broader peptide or wei...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Retrieval-Augmented Generation Must Move Beyond Factual Grounding to Represent Diverse Opinions](http://arxiv.org/abs/2604.12138v2)
  来源：arXiv | 日期：2026-04-13 | 相关度：2.1 | 新颖度：6.75
  匹配主题：未命中具体主题
  中文摘要：This position paper argues that Retrieval-Augmented Generation systems exhibit a systematic factual bias-optimizing for epistemic uncertainty reduction while ignoring the aleatoric uncertainty inherent in opinion-rich co...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Optimizing genomics-aware clinical agents in precision oncology.](https://pubmed.ncbi.nlm.nih.gov/42248877/)
  来源：PubMed | 日期：2026-06-05 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Agentic systems are proposed for clinical decision support, yet unrestricted tool access can undermine accountability and safety in precision oncology, where recommendations must be grounded in evolving guidelines, regul...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [ProfiliTable: Profiling-Driven Tabular Data Processing via Agentic Workflows](http://arxiv.org/abs/2605.12376v2)
  来源：arXiv | 日期：2026-05-12 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Table processing-including cleaning, transformation, augmentation, and matching-is a foundational yet error-prone stage in real-world data pipelines. While recent LLM-based approaches show promise for automating such tas...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Context-as-AI-Service: Surfacing Cross-File Dependency Chains for LLM-Generated Developer Documentation](http://arxiv.org/abs/2606.04397v2)
  来源：arXiv | 日期：2026-06-03 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：LLM agents increasingly write and maintain developer documentation, but usefulness and accuracy often rely on dependency chains that are not obvious to follow. Even with more files in context, the agent must still decide...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Beyond Vector Similarity: A Structural Analysis of Graph-Augmented Retrieval for Industrial Knowledge Graphs](http://arxiv.org/abs/2606.06003v1)
  来源：arXiv | 日期：2026-06-04 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：Retrieval-Augmented Generation (RAG) fails systematically on queries requiring structural reasoning over interconnected entities. We compare eight retrieval architectures for aerospace supply chain intelligence, progress...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Programming Biomolecular Interactions with All-Atom Generative Model](https://www.biorxiv.org/content/10.64898/2026.03.12.711044v3)
  来源：bioRxiv | 日期：2026-06-04 | 相关度：1.4 | 新颖度：1.0
  匹配主题：未命中具体主题
  中文摘要：Biomolecular interactions lie at the core of cellular life, spanning diverse molecular modalities from small molecules to nucleic acids and proteins. Nevertheless, design strategies remain separated despite shared physic...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [MeDiCNet: Integrating Multi-scale Dynamic Convolution and Enhanced Position-Aware Transformer for DNA Methylation Site Prediction.](https://pubmed.ncbi.nlm.nih.gov/42234354/)
  来源：PubMed | 日期：2026-06-03 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：DNA methylation is a covalent modification of cytosine and adenine bases that regulates gene expression and underlies diverse biological processes and diseases. Existing computational methods often rely on fixed-scale fe...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [CLFEC: A New Task for Unified Linguistic and Factual Error Correction in paragraph-level Chinese Professional Writing](http://arxiv.org/abs/2602.23845v2)
  来源：arXiv | 日期：2026-02-27 | 相关度：1.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：Chinese text correction has traditionally focused on spelling and grammar, while factual error correction is usually treated separately. However, in paragraph-level Chinese professional writing, linguistic (word/grammar/...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Towards Generalization of Block Attention via Automatic Segmentation and Block Distillation](http://arxiv.org/abs/2605.15913v4)
  来源：arXiv | 日期：2026-05-15 | 相关度：1.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：Block attention, which processes the input as separate blocks that cannot attend to one another, offers significant potential to improve KV cache reuse in long-context scenarios such as Retrieval-Augmented Generation (RA...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

- [Exposing Blindspots: Cultural Bias Evaluation in Generative Image Models](http://arxiv.org/abs/2510.20042v3)
  来源：arXiv | 日期：2025-10-22 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：Generative image models produce striking visuals yet often misrepresent culture. Prior work has examined cultural bias mainly in text-to-image (T2I) systems, leaving image-to-image (I2I) editors underexplored. We bridge ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [MARRVEL-MCP: An agentic interface for Mendelian disease discovery via tool-augmented context engineering.](https://pubmed.ncbi.nlm.nih.gov/42167217/)
  来源：PubMed | 日期：2026-06-04 | 相关度：6.75 | 新颖度：0.25
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：Variant interpretation in rare diseases requires navigating multiple genomic databases, each with strict input formats, while synthesizing heterogeneous evidence. This process creates significant barriers for non-experts...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Deep learning model for predicting mRNA half-life based on 3'UTR sequences.](https://pubmed.ncbi.nlm.nih.gov/41932116/)
  来源：PubMed | 日期：2026-06-04 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：mRNA stability, quantified by half-life, is central to gene expression homeostasis and post-transcriptional regulation. Predicting mRNA half-life from 3' untranslated region (3'UTR) sequences alone, however, remains chal...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [SciCore-Omics: a tri-modal foundation model unifying histology, spatial transcriptomics and language for spatial biology](https://www.biorxiv.org/content/10.64898/2026.05.30.728937v1)
  来源：bioRxiv | 日期：2026-06-03 | 相关度：5.75 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：Histomorphology and spatial transcriptomics capture complementary aspects of tissue biology, but their relationships remain difficult to extract, align, and interpret at scale. Existing foundation models typically connec...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MVFAN-Kcr: A Multi-View Feature Fusion and Attention-Based Network for Lysine Crotonylation Site Identification.](https://pubmed.ncbi.nlm.nih.gov/42234353/)
  来源：PubMed | 日期：2026-06-03 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Lysine crotonylation (Kcr), as an emerging post-translational modification, plays a crucial role in core life activities such as chromatin dynamics and gene expression. To address the current limitations of Kcr site dete...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [MAGI: Mechanistic Consequences of Genetic Variants via Genomic Foundation Models](https://www.biorxiv.org/content/10.64898/2026.05.31.729117v1)
  来源：bioRxiv | 日期：2026-06-03 | 相关度：5.55 | 新颖度：1.75
  匹配主题：pathogenomics, sequencing_bioinformatics
  中文摘要：Clinical variant interpretation requires mechanism-aware evidence to guide diagnosis and clarify the biological consequences of mutations. However, existing computational predictors and genomic foundation models largely ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [HEIST: A Graph Foundation Model for Spatial Transcriptomics and Proteomics Data](http://arxiv.org/abs/2506.11152v4)
  来源：arXiv | 日期：2025-06-11 | 相关度：2.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：Single-cell transcriptomics and proteomics have become a great source for data-driven insights into biology, enabling the use of advanced deep learning methods to understand cellular heterogeneity and gene expression at ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [R^3: Composed Video Retrieval via Reasoning-Guided Recalling and Re-ranking](http://arxiv.org/abs/2606.01113v2)
  来源：arXiv | 日期：2026-05-31 | 相关度：2.05 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：The CoVR-R challenge evaluates composed video retrieval, where a system must retrieve a target video from a large gallery given a reference video and a textual edit instruction. This setting is not a standard video-text ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Cross-scale spatially-aware generative modeling of transcriptomic programs underlying neurodegenerative brain organization](http://arxiv.org/abs/2606.05870v1)
  来源：arXiv | 日期：2026-06-04 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Neurodegenerative disorders such as Alzheimer's disease exhibit highly organized patterns of regional brain vulnerability, yet the biological mechanisms underlying this spatial selectivity remain incompletely understood....
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Seeing is making: AI visualisation and genomic prediction.](https://pubmed.ncbi.nlm.nih.gov/42242919/)
  来源：PubMed | 日期：2026-06-04 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：The integration of artificial intelligence (AI) into genomics is reshaping not only how biological data are analysed, but how genomic knowledge is produced and operationalised in clinical practice. Earlier computational ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A2RAG: Adaptive Agentic Graph Retrieval for Cost-Aware and Reliable Reasoning](http://arxiv.org/abs/2601.21162v2)
  来源：arXiv | 日期：2026-01-29 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Graph Retrieval-Augmented Generation (Graph-RAG) enhances multihop question answering by organizing corpora into knowledge graphs and routing evidence through relational structure. However, practical deployments face two...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [KESOZI Digital Twin: Physics-Informed Neural Network for Independent Estimation and Prediction of Childhood Diarrheal Disease Burden in Kenya, Somaliland, and Zimbabwe](https://www.medrxiv.org/content/10.64898/2026.06.03.26354823v1)
  来源：medRxiv | 日期：2026-06-04 | 相关度：5.8 | 新颖度：0.75
  匹配主题：pathogenomics, foundation_model_agent, application_monitoring
  中文摘要：Childhood diarrheal disease remains a leading cause of morbidity and mortality among children under five years in sub-Saharan Africa, particularly in settings affected by inadequate sanitation, climate variability, malnu...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Leveraging Digitization, Archiving and Artificial Intelligence to Re-examine Predictors of Sustained Mental Health Care Engagement in Ugandan First-Episode Psychosis Patients: A Study Protocol](https://www.medrxiv.org/content/10.64898/2026.06.02.26354672v1)
  来源：medRxiv | 日期：2026-06-03 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Background: We previously examined the burden and predictors of sustained mental health care engagement in Ugandan first episode psychosis patients by retrospective chart review methods. However, the extensive requiremen...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Tuberculosis in households with infectious cases in Kampala city: Harnessing health data science for new insights on an ancient disease with persistent, unresolved problems.](https://pubmed.ncbi.nlm.nih.gov/42241447/)
  来源：PubMed | 日期：2026-01-01 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：Tuberculosis (TB) is prevalent in Uganda and overlaps with a high rate of HIV/TB coinfection. While nearly all hospital-based TB cases in Kampala, the capital of Uganda, show clear TB symptoms, 30% or more of undiagnosed...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

### 其他

- [Toward decision-aware AI for LSST-scale time-domain astronomy](http://arxiv.org/abs/2606.05285v1)
  来源：arXiv | 日期：2026-06-03 | 相关度：0.7 | 新颖度：5.75
  匹配主题：未命中具体主题
  中文摘要：The Vera C. Rubin Observatory's Legacy Survey of Space and Time (LSST) will generate approximately (10^7) alerts per night, pushing time-domain astronomy beyond pipelines that treat discovery as a static labeling problem...
  为什么值得看：Toward decision-aware AI for LSST-scale  与你的主题有弱匹配，暂时保留作低优先级跟踪。
