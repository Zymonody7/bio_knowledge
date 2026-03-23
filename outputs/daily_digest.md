# 每日论文监控日报 (2026-03-23)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 19 篇新论文。

## 抓取状态

- arXiv：成功，命中 9 篇
- PubMed：成功，命中 14 篇
- bioRxiv：成功，命中 14 篇
- medRxiv：成功，命中 8 篇

## 最值得看

### Foundation Model / Agent

- [HViLM: A Foundation Model for Viral Genomics Enables Multi-Task Prediction of Pathogenicity, Transmissibility, and Host Tropism](https://www.biorxiv.org/content/10.64898/2026.03.18.712700v1)
  来源：bioRxiv | 日期：2026-03-20 | 相关度：10.0 | 新颖度：2.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Motivation: The emergence of novel viral pathogens poses critical threats to global health, yet current computational approaches for viral risk assessment are predominantly virus-specific and require extensive retraining...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [BioReason-Pro: Advancing Protein Function Prediction with Multimodal Biological Reasoning](https://www.biorxiv.org/content/10.64898/2026.03.19.712954v1)
  来源：bioRxiv | 日期：2026-03-20 | 相关度：8.9 | 新颖度：1.2
  匹配主题：foundation_model_agent
  中文摘要：Protein function annotation is fundamental to understanding biological mechanisms, designing therapeutics, and advancing biomedical research. Current computational methods either rely on shallow sequence similarity or tr...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From Protocol to Analysis Plan: Development and Validation of a Large Language Model Pipeline for Statistical Analysis Plan Generation using Artificial Intelligence (SAPAI)](https://www.medrxiv.org/content/10.64898/2026.03.19.26348626v2)
  来源：medRxiv | 日期：2026-03-20 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Background: Statistical Analysis Plans (SAPs) are essential for trial transparency and credibility but are resource-intensive to produce. While Large Language Models (LLMs) have shown promise in drafting protocols, their...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Understanding and Optimizing Multi-Stage AI Inference Pipelines](http://arxiv.org/abs/2504.09775v5)
  来源：arXiv | 日期：2025-04-14 | 相关度：6.55 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：大语言模型（LLM）的演进推动了对复杂推理流水线和硬件平台的需求。现代 LLM 服务已超越传统的预填充-解码（prefill-decode）流程，整合了检索增强生成（RAG）、键值（KV）缓存检索、动态模型路由和多步推理等阶段。这些阶段计算需求各异，需要集成 GPU、ASIC、CPU 及以内存为中心的分布式系统。然而，现有模拟器缺乏对这些异构多引擎工作流建模的保真度，限制了架构决策。为此，本文推出了 MIST，一种异构多阶段 LLM 推...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [CliPepPI: Scalable prediction of domain-peptide specificityusing contrastive learning](https://www.biorxiv.org/content/10.64898/2026.03.18.712595v1)
  来源：bioRxiv | 日期：2026-03-20 | 相关度：7.65 | 新颖度：1.25
  匹配主题：sequencing_bioinformatics, foundation_model_agent
  中文摘要：Domain-peptide interactions mediate a significant fraction of cellular protein networks, yet accurately predicting their specificity remains challenging. Peptide motifs typically have short, fuzzy sequence profiles, and ...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Designing mRNA coding sequence via multimodal reverse translation language modeling with Pro2RNA](https://www.biorxiv.org/content/10.64898/2026.03.18.712790v1)
  来源：bioRxiv | 日期：2026-03-20 | 相关度：8.5 | 新颖度：1.75
  匹配主题：foundation_model_agent
  中文摘要：mRNA coding sequence design is a critical component in the development of mRNA vaccines, nucleic acid therapeutics, and heterologous gene expression systems. While large language models have recently been successfully ap...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Coupling codon and protein constraints decouples drivers of variant pathogenicity](https://www.biorxiv.org/content/10.1101/2025.03.12.642937v3)
  来源：bioRxiv | 日期：2026-03-20 | 相关度：7.7 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Predicting the functional impact of genetic variants remains a fundamental challenge in genomics. Existing models focus on protein-intrinsic defects yet overlook regulatory constraints embedded within coding sequences. H...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Revisiting Gene Ontology Knowledge Discovery with Hierarchical Feature Selection and Virtual Study Group of AI Agents](http://arxiv.org/abs/2603.20132v1)
  来源：arXiv | 日期：2026-03-20 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：大语言模型在多项挑战性任务中取得了巨大成功，而新兴的智能体（Agentic AI）技术进一步提升了其能力。本研究提出了一种新型的基于智能体AI的知识发现导向型“虚拟学习小组”（Virtual Study Group），旨在通过层次化特征选择方法筛选出与衰老高度相关的基因本体（GO）术语，并从中提取有意义的衰老相关生物学知识。研究团队针对四种不同模式生物的衰老相关GO术语，考察了该智能体AI框架的性能，并通过查阅现有研究文献验证了其生物学...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [NAACL: Noise-AwAre Verbal Confidence Calibration for Robust LLMs in RAG Systems](http://arxiv.org/abs/2601.11004v2)
  来源：arXiv | 日期：2026-01-16 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：准确评估模型置信度对于在关键事实领域部署大语言模型（LLMs）至关重要。虽然检索增强生成（RAG）被广泛用于提高生成内容的可靠性，但 RAG 环境下的置信度校准仍缺乏深入研究。本研究通过四个基准测试发现，由于检索到的上下文存在噪声，LLMs 表现出较差的校准性能；具体而言，矛盾或无关的证据往往会夸大模型的虚假确定性，导致严重的过度自信。为此，研究者提出了 NAACL 规则（噪声感知置信度校准规则），为解决噪声下的过度自信提供原则性基础。...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [From Concept to Clinic: Real World Evidence for Autonomous AI Deployment in Primary Care Telemedicine](https://www.medrxiv.org/content/10.64898/2026.03.18.26348749v1)
  来源：medRxiv | 日期：2026-03-20 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：Systems powered by large language models are widely used for health information and advice, yet robust evidence for their safety and effectiveness in real-world clinical care remains lacking. Most existing studies evalua...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [TempPerturb-Eval: On the Joint Effects of Internal Temperature and External Perturbations in RAG Robustness](http://arxiv.org/abs/2512.01183v2)
  来源：arXiv | 日期：2025-12-01 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：检索增强生成（RAG）系统的评估通常独立考察检索质量和生成参数（如温度），忽略了二者的相互作用。本研究系统调查了文本扰动（模拟噪声检索）与不同大语言模型（LLM）运行温度设置之间的交互影响。我们提出了一个全面的 RAG 扰动-温度分析框架，在不同温度设置下对检索到的文档进行三种不同类型的扰动。通过在 HotpotQA 数据集上对开源和闭源 LLM 进行的大量实验，研究证明性能下降遵循特定模式：高温度设置会持续放大模型对扰动的脆弱性，而某...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Leveraging Residual Graph Convolutional Networks with Cross-Attention Mechanisms for High-Accuracy Protein Function Prediction.](https://pubmed.ncbi.nlm.nih.gov/41861353/)
  来源：PubMed | 日期：2026-03-20 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：蛋白质功能的精确确定对于阐明细胞过程和病理机制至关重要，有助于推动靶向药物设计。尽管湿实验方法仍是功能鉴定的金标准，但其周期长、成本高且劳动强度大，难以满足大规模蛋白质序列的注释需求。本研究提出了 RCHGO，这是一种新型深度学习框架，旨在利用配备交叉注意力机制的残差图卷积网络（RGCNs），直接从蛋白质序列推断基因本体（GO）注释。在 1,493 个非冗余蛋白质上的全面基准测试结果显示，RCHGO 的性能优于 16 种现有的先进方法。...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [X-Cell: Scaling Causal Perturbation Prediction Across Diverse Cellular Contexts via Diffusion Language Models](https://www.biorxiv.org/content/10.64898/2026.03.18.712807v1)
  来源：bioRxiv | 日期：2026-03-20 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：预测基因扰动如何重塑不同细胞背景下的基因表达，是构建通用细胞基础模型的关键。本研究推出了 X-Atlas/Pisces，这是目前规模最大的全基因组 CRISPRi Perturb-seq 数据集，包含 16 个生物学背景下的 2560 万个单细胞转录组，涵盖 iPSC、Jurkat T 细胞及多种分化谱系。基于此资源，研究者开发了 X-Cell 扩散语言模型，该模型通过交叉注意力机制整合自然语言、蛋白质语言模型、相互作用网络、遗传依赖图...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Bacteriophage host prediction using a genome language model](https://www.biorxiv.org/content/10.64898/2026.03.19.712863v1)
  来源：bioRxiv | 日期：2026-03-20 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：从基因组序列预测噬菌体宿主具有挑战性，因为宿主范围受受体结合蛋白、抗防御系统等快速演化的基因组因素影响，且现有预测信号（如同源性、CRISPR间隔序列、核苷酸组成）分布稀疏。本研究将宿主预测视为无监督检索问题，利用预训练基因组语言模型 Evo2-7B 生成噬菌体与候选细菌宿主的全基因组嵌入向量，通过余弦相似度进行排序。在 Virus-Host 数据库的革兰氏阴性测试集评估显示，Evo2 在检索多个潜在宿主方面表现强劲，55.4% 的噬菌...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Adapting a Pre-trained Single-Cell Foundation Model to Spatial Gene Expression Generation from Histology Images](http://arxiv.org/abs/2603.19766v1)
  来源：arXiv | 日期：2026-03-20 | 相关度：2.4 | 新颖度：6.5
  匹配主题：未命中具体主题
  中文摘要：空间转录组学（ST）能够实现位点级的原位表达谱分析，但其高昂的成本和有限的通量促使研究者探索直接从H&E染色的组织学图像预测基因表达。现有的生成模型（如基于评分或流的模型）虽能估计基因表达的条件分布，但往往忽略了基因间的依赖关系，削弱了生物学一致性。单细胞基础模型（sc-FMs）通过在大规模细胞群体上的预训练，捕捉到了组织学图像无法揭示的关键基因关系。为此，本研究提出了 HINGE（组织学条件生成）框架，将预训练的 sc-FM 改造为条...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A convolutional attention model classifies copy number variants from whole exome sequencing.](https://pubmed.ncbi.nlm.nih.gov/41862604/)
  来源：PubMed | 日期：2026-03-20 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：拷贝数变异（CNV）是遗传病和癌症的重要生物标志物，但现有的全外显子组（WES）CNV检测工具多依赖于读取深度启发式算法，难以捕获基因组上下文且跨平台泛化性差。本研究提出一种带注意力机制的双输入卷积神经网络（CNN-Att），可同时处理归一化读取深度、基因组坐标和染色体标识。模型在ECOLE标记的千人基因组计划数据上预训练，并经7个专家标注样本微调。测试集结果显示，该方法宏F1达0.83，宏PR-AUC达0.93。在HiSeq 4000...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CoverageBench: Evaluating Information Coverage across Tasks and Domains](http://arxiv.org/abs/2603.20034v1)
  来源：arXiv | 日期：2026-03-20 | 相关度：1.4 | 新颖度：6.0
  匹配主题：未命中具体主题
  中文摘要：本研究旨在衡量即时检索算法的“信息覆盖率”，即搜索结果涵盖可用相关信息的程度。信息覆盖率是检索系统的核心指标，尤其是在检索增强生成（RAG）系统中。传统的即时检索指标（如精确率、召回率、RBP、nDCG 和 MAP）通常根据检索到的相关文档数量来奖励系统。然而，由于这些测试集中的相关性是针对单个文档定义的，未考虑文档间可能包含重复信息的情况，因此高召回率虽能保证覆盖率，但并非必要条件。虽然 Web 搜索中的多样性排序集合包含部分覆盖率概...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [LLM-Enhanced Semantic Data Integration of Electronic Component Qualifications in the Aerospace Domain](http://arxiv.org/abs/2603.20094v1)
  来源：arXiv | 日期：2026-03-20 | 相关度：1.4 | 新颖度：5.5
  匹配主题：未命中具体主题
  中文摘要：大型制造企业因部门间的数据孤岛面临信息检索挑战，导致数据库间存在不一致性。本文分享了在卫星电路板设计中集成与检索电子元件鉴定数据的实践经验。由于数据孤岛的存在，设计人员无法实时确定单个元件的鉴定状态，而这一过程在生产前发布组装图的规划阶段至关重要，有助于优化新鉴定流程并避免重复劳动。为解决此问题，我们提出了一种流水线方案，利用虚拟知识图谱（VKG）提供异构数据源的统一视图，并结合大语言模型（LLM）增强检索能力并减少数据清洗的人工投入。...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Embodied Science: Closing the Discovery Loop with Agentic Embodied AI](http://arxiv.org/abs/2603.19782v1)
  来源：arXiv | 日期：2026-03-20 | 相关度：0.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：人工智能在预测科学属性方面已展现出卓越能力，但科学发现本质上是由实验周期驱动的物理性、长周期过程。目前的计算方法大多与这一现实脱节，将发现过程简化为孤立的特定任务预测，而非与物理世界的持续交互。本文提出了“具身科学”（Embodied Science）范式，将科学发现重构为智能体推理与物理执行紧密耦合的闭环。我们提出了统一的“感知-语言-行动-发现”（PLAD）框架，使具身智能体能够感知实验环境、基于科学知识进行推理、执行物理干预并内化...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。
