# 每日论文监控日报 (2026-03-27)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 21 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：429 Client Error: Unknown Error
- PubMed：成功，命中 38 篇
- bioRxiv：成功，命中 33 篇
- medRxiv：成功，命中 17 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [[Construction and teaching practice of an AI- and OBE-integrated smart course Genetic Engineering].](https://pubmed.ncbi.nlm.nih.gov/41873092/)
  来源：PubMed | 日期：2026-03-25 | 相关度：7.55 | 新颖度：1.2
  匹配主题：foundation_model_agent
  中文摘要：Several critical challenges exist in the graduate course Genetic Engineering at Beijing Institute of Technology, including conceptual confusion in core topics such as CRISPR-Cas9, difficulties in transferring theoretical...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Human-supervised, large language model-based clinical decision support aligned to national newborn protocols in Kenya: a pragmatic, early-stage evaluation](https://www.medrxiv.org/content/10.64898/2026.03.22.26348994v1)
  来源：medRxiv | 日期：2026-03-25 | 相关度：7.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Introduction: Timely, protocol-adherent clinical decisions are crucial for reducing neonatal mortality in low-resource settings. Translating extensive national guidelines into bedside practice remains challenging. Object...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Structured retrieval closes the gap between low-cost and frontier clinical language models](https://www.medrxiv.org/content/10.64898/2026.03.22.26349018v1)
  来源：medRxiv | 日期：2026-03-24 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Most clinical large language model (LLM) benchmarks rely on clean, concise vignettes that do not reflect the noisy, long-form documentation typical of real clinical records. How LLM performance degrades under realistic c...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OmicClaw: executable and reproducible natural-language multi-omics analysis over the unified OmicVerse ecosystem.](https://www.biorxiv.org/content/10.64898/2026.03.13.711464v2)
  来源：bioRxiv | 日期：2026-03-25 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Advances in bulk, single-cell and spatial omics have transformed biological discovery, yet analysis remains fragmented across packages with incompatible interfaces, heterogeneous dependencies and limited workflow reprodu...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A statistical framework for evaluating the repeatability and reproducibility of large language models](https://www.medrxiv.org/content/10.1101/2025.08.06.25333170v3)
  来源：medRxiv | 日期：2026-03-25 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Objective. Systematic evaluation of variability in large language model (LLM)-generated outputs is critical for assessing their reliability. We developed a regulatory-informed statistical framework to quantify LLM repeat...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Nonlinear trajectories of language network development](https://www.biorxiv.org/content/10.64898/2026.03.25.714106v1)
  来源：bioRxiv | 日期：2026-03-25 | 相关度：6.1 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：人类大脑如何组织复杂认知功能，特别是局域化与分布式架构之争，目前仍无定论。本研究通过多模态神经影像和行为测量，揭示了语言网络经历的一种非线性发育重组过程，从而调和了上述观点。研究确定了一个三阶段发育轨迹：早期局域化、青少年时期以连通性下降（connectivity dip）为特征的瞬时分布式状态，以及成年期向精细局域化的回归。这种青少年时期的连通性下降具有行为学意义，并有助于构建整合性网络架构。功能连通性与脑-行为关系的趋同转变表明，青...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Quantitative prediction of nonsense-mediated mRNA decay across human genes by genomic language model and large-scale mutational scanning](https://www.biorxiv.org/content/10.64898/2026.03.24.714003v1)
  来源：bioRxiv | 日期：2026-03-26 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：The molecular consequences of protein truncating variants depend strongly on whether their transcripts are eliminated by nonsense-mediated mRNA decay (NMD), yet NMD is still predicted largely from a small set of binary p...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Decoding Immunomodulatory Hydrogels for Arthritis: Comparative Insights from Predictive Machine Learning and Large Language Models](https://www.biorxiv.org/content/10.64898/2026.03.23.713755v1)
  来源：bioRxiv | 日期：2026-03-26 | 相关度：6.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：Hydrogels are increasingly recognized as promising therapeutics for arthritic joints, extending their traditional role as mechanical lubricants to modulators of joint immunity. However, the rational design of these mater...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Emergent Biological Realism in RL-Trained DNA Language Models](https://www.biorxiv.org/content/10.64898/2026.03.24.713963v1)
  来源：bioRxiv | 日期：2026-03-26 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：强化学习（RL）通过解锁非预期能力推动了大语言模型的广泛应用，但在生成式 DNA 模型中仍未得到充分探索。本研究以质粒生成为测试平台，探讨后训练技术是否能诱导 DNA 语言模型产生“涌现的生物学现实性”。质粒因其结构相对简单、功能约束明确且在生物技术中广泛应用而被选中。研究采用基于工程生物学约束的奖励函数，利用群体相对策略优化（GRPO）算法进行训练。结果显示，该模型的质量控制（QC）通过率从预训练基线的 5% 显著提升至 77%。值得...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Advances in Pathogen Detection by Nanosensors: Biorecognition Strategies, Signal Amplification, and Platform Engineering.](https://pubmed.ncbi.nlm.nih.gov/41808396/)
  来源：PubMed | 日期：2026-03-24 | 相关度：7.75 | 新颖度：0.5
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：The escalating global threat of infectious diseases, compounded by antimicrobial resistance (AMR), calls for improved diagnostic strategies. Conventional pathogen detection techniques─culture, enzyme-linked immunosorbent...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Fully Automated Abstraction of Longitudinal Breast Oncology Records with Off-The-Shelf Large Language Models](https://www.medrxiv.org/content/10.64898/2026.03.23.26349012v1)
  来源：medRxiv | 日期：2026-03-25 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：Background: Manual chart abstraction is a major bottleneck in clinical research. In oncology, important outcomes such as disease recurrence and the treatment history are often only documented in clinical notes, limiting ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Genomebook: Mendelian inheritance as a structured parameterisation layer for LLM agent populations](https://www.biorxiv.org/content/10.64898/2026.03.22.713494v1)
  来源：bioRxiv | 日期：2026-03-24 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：本研究引入了 Genomebook，这是一种为大语言模型（LLM）智能体设计的演化系统，旨在解决智能体通常作为克隆体部署且缺乏遗传变异机制的问题。该系统通过 60 个二倍体位点编码了 26 种行为特征，采用加性、显性和隐性遗传模型。研究以 20 个初始智能体为起点，每个智能体由人格配置文件（SOUL.md）和编译基因组（DNA.md）定义，通过孟德尔分离定律进行有性繁殖，并伴随 0.1% 的基础突变率。在 8 代演化（共 626 个智能...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Machine learning predicts hepatocellular carcinoma risk from routine clinical data: a large population-based multicentric study.](https://pubmed.ncbi.nlm.nih.gov/41881847/)
  来源：PubMed | 日期：2026-03-26 | 相关度：3.05 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：肝细胞癌（HCC）是一种致死率极高的肿瘤，其风险分层至关重要但仍具挑战。本研究开发了一个基于常规临床数据的可解释机器学习框架。研究利用了来自两个大规模队列（UK Biobank 用于模型开发，All of Us Research Program 用于外部测试）的 900,000 多名个体和 983 例 HCC 病例的前瞻性多模态数据。研究评估了包括人口统计学、生活方式、健康记录、血液、基因组学和代谢组学在内的多种数据模态的个体及累积贡献...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [EvoRMD: Integrating Biological Context and Evolutionary RNA Language Models for Interpretable Prediction of RNA Modifications](https://www.biorxiv.org/content/10.64898/2026.03.22.713386v1)
  来源：bioRxiv | 日期：2026-03-25 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：RNA修饰是转录后基因表达的关键调节因子，影响RNA的稳定性、定位、翻译和降解。确定特定核苷酸的修饰类型对于理解其调控作用至关重要。目前大多数计算方法将每种修饰视为独立的二分类任务，但这忽略了在特定生化条件下，一个位点通常仅存在一种修饰类型的生物学事实，且现有测序数据往往只标记一种修饰而将其他类型视为“未标记”而非“负样本”。为此，我们开发了EvoRMD，这是一个整合生物学背景且具有可解释性的统一预测模型。EvoRMD结合了大规模RNA...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Unveiling the biodiversity of large DNA viruses in intertidal mudflats via metagenomics.](https://pubmed.ncbi.nlm.nih.gov/41872229/)
  来源：PubMed | 日期：2026-03-24 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：大型 DNA 病毒 (LDVs) 因其巨大的基因组和广泛的代谢潜力而备受关注，但对复杂动态生境中该类群的了解仍有限。本研究利用多种采样和测序策略，从潮间带滩涂 5.3 TB 的宏基因组数据中恢复了 237 个 LDV 基因组。研究发现了一个系统发育独特的 Imitervirales 亚群，并揭示了其与多种真核生物的广泛关联。部分 LDV 种群在当地持久存在，并表现出由动态潮间带驱动的显著基因组变异。在生态模式上，巨型病毒表现出比大型噬菌...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Unlocking Enzyme Discovery: A High-Resolution Gene Cluster Database Powered by Phylogenetic Insights and Machine Learning.](https://pubmed.ncbi.nlm.nih.gov/41837859/)
  来源：PubMed | 日期：2026-03-25 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：高通量测序产生了大量注释不足的基因组库，阻碍了酶的发现。本研究提出了一套集成流程：(i) 构建高分辨率跨界系统发育数据库；(ii) 通过多位点系统发育挖掘候选基因；(iii) 利用进化规模的蛋白质语言模型（pLM）预测活性；(iv) 通过多级残基-原子接触重评分剔除假阳性。将该方法应用于 r-BOX 途径，发现了大量此前未记录的 FadB、BktB、Ter 和 YdiI 同源物。活性预测模型实现了 R² = 0.68，在高价值靶点上的均...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Visualize, Explore, and Select: A protein Language Model-based Approach Enabling Navigation of Protein Sequence Space for Enzyme Discovery and Mining](https://www.biorxiv.org/content/10.64898/2026.03.23.712833v1)
  来源：bioRxiv | 日期：2026-03-25 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：蛋白质序列数据库的快速扩张远超功能鉴定速度，限制了在大型、异质且注释稀疏的序列空间中高效发现酶。本文提出 SelectZyme，一个基于嵌入引导的酶序列空间结构化导航框架。该工作流整合了蛋白质语言模型（pLM）嵌入、降维、层次聚类、连通性重建和定量树状图分析，实现了无需依赖固定序列一致性阈值或预定义功能注释的探索。通过案例研究，证明即使在序列一致性处于“黄昏区”时，嵌入定义的邻域仍能保持折叠水平的一致性，且在完全无监督条件下可涌现出具有...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Spatial multi-omics of multiple myeloma uncovers niche-dependent pro-myeloma and immunosuppressive signaling in the bone marrow and extramedullary lesions](https://www.biorxiv.org/content/10.64898/2026.03.23.713195v1)
  来源：bioRxiv | 日期：2026-03-25 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：多发性骨髓瘤（MM）是一种受浆细胞与免疫微环境动态相互作用影响的恶性肿瘤。为在空间维度剖析细胞背景对 MM 及免疫细胞表达的影响，本研究开发了一个整合 10x Genomics Visium HD、Xenium 及临床注释单细胞 RNA 测序（scRNA-seq）数据的多模态框架。Visium HD 实现了 16μm 分辨率下的无偏全转录组空间发现，Xenium 提供单细胞水平的正交验证，scRNA-seq 则通过映射空间标签和利用高测...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Computational Design and Atomistic Validation of a High-Affinity VHH Nanobody Targeting the PI/RuvC Interface of Streptococcus pyogenes Cas9: A Bivalent Hub Strategy for CRISPR-Cas9 Enhancement](https://www.biorxiv.org/content/10.64898/2026.03.22.713495v1)
  来源：bioRxiv | 日期：2026-03-25 | 相关度：0.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：CRISPR-Cas9 系统在基因组工程中具有革命性意义，但其活性和特异性的精确调节仍面临挑战。本研究报告了一个全计算端到端流程，用于从头设计针对化脓性链球菌 Cas9（SpCas9；PDB: 4UN3）PI 与 RuvC-III 界面非催化表位的单域 VHH 纳米抗体（NbSpCas9-v1）。研究利用生成式扩散结合物设计框架 BoltzGen 生成纳米抗体序列，并使用 Boltz-2 与 SpCas9 进行共折叠，以评估结构置信度和...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Medical errors in large language models revealed using 1,000 synthetic clinical transcripts](https://www.medrxiv.org/content/10.64898/2026.03.23.26349082v1)
  来源：medRxiv | 日期：2026-03-25 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：当前大语言模型（LLM）的临床评估依赖于无法反映真实医疗复杂性的数据集。本研究开发了一种针对头痛患者的高通量模拟系统，生成了1000份医患对话转录文本，实现了对跨人口统计学和临床表型的临床推理失败的深度映射。结果显示，在拥有完整病史的情况下，GPT-5.2的诊断准确率达到97.5%（95% CI: 95.0-99.5）。然而，不完整的转录文本会触发危险建议：模型不仅未要求补充信息，反而阻止了必要的检查，例如在蛛网膜下腔出血病例中100%...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Fingerprinting Fluorescent In Situ Hybridization Enables Multiplexed Identification of Pathogenic Bacteria.](https://pubmed.ncbi.nlm.nih.gov/41810482/)
  来源：PubMed | 日期：2026-03-24 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：荧光原位杂交（FISH）是一种无需培养即可检测病原菌的高特异性技术，能同时提供病原菌丰度、形态和空间定位信息。然而，传统 FISH 灵敏度有限且多重检测能力不足，限制了其广泛应用。本研究提出了一种由 DNA 自组装驱动的指纹 FISH（FinFISH）策略，用于多重病原菌检测。以呼吸道病原体为模型，FinFISH 利用 FAM、Cy3 和 Cy5 三种荧光团进行组合标记，为每个物种生成独特的荧光指纹。该策略突破了荧光通道数量对检测通量的...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
