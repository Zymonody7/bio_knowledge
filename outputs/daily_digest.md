# 每日论文监控日报 (2026-04-30)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 14 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：429 Client Error: Unknown Error
- PubMed：成功，命中 49 篇
- bioRxiv：成功，命中 15 篇
- medRxiv：成功，命中 9 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### 产品应用 / 监测落地

- [Artificial Intelligence, LLM-based generation of synthetic patients with Parkinson's Disease: towards a digital twin paradigm for in silico studies](https://www.medrxiv.org/content/10.64898/2026.04.28.26351471v1)
  来源：medRxiv | 日期：2026-04-29 | 相关度：7.55 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Heterogeneity in sporadic Parkinson's Disease (PD) is a critical problem that drives variable rates of progression and treatment response and complicates clinical trials. Access to large PD datasets that may help in clus...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 可追踪

### Foundation Model / Agent

- [A Multi-modal LLM-Knowledge Fusion Framework for Predicting Single-cell Genetic Perturbation Effects](https://www.biorxiv.org/content/10.64898/2026.04.24.720560v1)
  来源：bioRxiv | 日期：2026-04-28 | 相关度：7.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：理解细胞对基因扰动的反应是药物发现的基础，但实验方法在覆盖范围和成本上的局限阻碍了对细胞行为的全面绘制。为此，研究者开发了“虚拟细胞”计算模型，通过学习细胞状态与功能的关系来预测扰动后果。然而，现有方法在处理复杂基因相互作用、生物可解释性以及对未知基因的泛化能力方面存在不足。本研究提出 scPert，这是一个基于 Transformer 架构的多模态框架，整合了大语言模型（LLM）嵌入与结构化生物知识，用于预测单细胞转录组对基因扰动的响...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [From simulation to pedagogy: structured AI standardized patients for clinical communication training validated through multi-model and randomized evaluation](https://www.medrxiv.org/content/10.64898/2026.04.26.26351793v1)
  来源：medRxiv | 日期：2026-04-28 | 相关度：7.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：标准化病人（SPs）是临床沟通培训的核心，但受限于高昂成本、可扩展性及对专业演员的依赖。本研究开发了由大语言模型（LLM）驱动的AI标准化病人（AI-SPs），其核心是采用三层信息架构，根据学习者的技能水平动态调节病情的披露程度。验证过程分为三个阶段：第一阶段通过对5个前沿LLM生成的350次模拟咨询进行专家盲评，结果显示学习者的技能水平对表现差异的影响（eta^2 = 0.31）显著高于模型选择（eta^2 = 0.06），证明教学质...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Comparative Study in Surgical AI: Datasets, Foundation Models, and Barriers to Med-AGI](https://www.medrxiv.org/content/10.64898/2026.03.26.26349455v3)
  来源：medRxiv | 日期：2026-04-28 | 相关度：6.8 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：本研究探讨了通用人工智能（AI）在外科图像分析任务中的表现。尽管AI在多项生物医学基准上已超越人类，但在外科领域仍面临多模态整合与专业数据标注的挑战。研究以2026年最先进的AI方法为基础，针对神经外科手术器械检测进行了案例研究。实验结果显示：(1) 评估19个开源视觉语言模型（VLM）的零样本性能，仅一个模型略微超过13.4%的基准线；(2) 使用LoRA微调Gemma 3 27B模型生成JSON预测，准确率提升至47.63%；(3)...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Risk Based Prediction of Novel AMR Variants Using Protein Language Models](https://www.biorxiv.org/content/10.1101/2025.09.12.672331v2)
  来源：bioRxiv | 日期：2026-04-27 | 相关度：9.65 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：抗生素耐药性（AMR）是全球健康的重大威胁，监测系统亟需检测已知及新兴的耐药标志物。本研究开发了 AMRscope，这是一种基于 ESM2 蛋白质语言模型（PLM）嵌入向量的预测模型，专门用于评估单位点突变导致耐药的可能性。该工具应用于多种细菌的抗生素相互作用蛋白，涵盖了世卫组织（WHO）重点病原体，如耐利福平结核分枝杆菌和耐碳青霉烯铜绿假单胞菌。实验结果显示，在随机划分的数据集上，模型达到了 0.88 的准确率、0.87 的 F1 分...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Protein Function Prediction with Pretrained ProtT5 Embeddings and Gradient Boosting](https://www.biorxiv.org/content/10.64898/2026.04.27.721184v1)
  来源：bioRxiv | 日期：2026-04-28 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：蛋白质功能预测因基因本体（GO）注释的极端稀疏性和长尾分布，一直是计算生物学的核心挑战。蛋白质语言模型的发展使得从氨基酸序列中提取固定长度的稠密表征成为可能，为理化性质等人工特征提供了可扩展的替代方案。本研究在 CAFA-6 竞赛设置下，评估了利用 ProtT5-XL 提取的 Transformer 嵌入向量结合经典及现代多标签分类器进行 GO 预测的效果。研究通过对 Transformer 隐藏状态进行均值池化生成固定长度嵌入，并将其...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Design of Safe and Efficient Adenine Base Editors via Protein Language Model Screening for Osteoarthritis Treatment.](https://pubmed.ncbi.nlm.nih.gov/42052652/)
  来源：PubMed | 日期：2026-04-29 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：碱基编辑器（Base editors）可实现精确的基因组修饰，是纠正单核苷酸变异引起疾病的潜力疗法。虽然现有的高效腺嘌呤碱基编辑器（ABEs，如 ABE8e）在 A-to-G 转换方面效率极高，但其持续的高脱靶效应阻碍了临床转化。本研究利用人工智能辅助设计，开发了一种名为 RDLot-ABE 的安全变体。与 ABE8e 相比，RDLot-ABE 具有更窄（4 nt）的编辑窗口，且 DNA 脱靶编辑活性显著降低。此外，利用 RDLot-A...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Metastasis Extraction from NSCLC Clinical Notes: A Retrospective Comparative Evaluation of Large Language Model-Based Classification](https://www.medrxiv.org/content/10.64898/2026.04.27.26351872v1)
  来源：medRxiv | 日期：2026-04-29 | 相关度：7.15 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：识别非小细胞肺癌（NSCLC）的转移状态对疾病预后和治疗决策至关重要，但临床登记系统中的结构化数据往往不完整。本研究评估了三种大语言模型（LLM）在提取转移信息方面的表现。研究涵盖两个独立任务：全转移识别和脑/中枢神经系统（CNS）转移识别。实验基于两个队列：队列1包含579名患者的24,887份临床记录，以登记数据为标准；队列2包含22名患者的644份影像报告，以人工双重标注为标准。方法上，研究微调了GatorTron-base编码器...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [MedSDoH: A Rule-Based System for Extracting Social Determinants of Health from Multi-site EHRs Based on the OHNLP Framework](https://www.medrxiv.org/content/10.64898/2026.04.27.26351699v1)
  来源：medRxiv | 日期：2026-04-29 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：健康社会决定因素（SDoH）对患者护理和人群健康至关重要，但相关信息常嵌入在非结构化临床文本（如社会工作者笔记）中，限制了其在临床决策中的应用。虽然 Transformer 模型是目前的主流，但其计算需求和透明度问题阻碍了大规模多中心临床实施。本研究开发了基于 OHNLP 框架的 MedSDoH 系统，利用文献资源、标准化定义和专家规则集构建。在开发过程中，利用大语言模型（LLM）辅助生成规则和扩展词库。MedSDoH 包含涵盖 22 ...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Silent numerical failures in large language model-generated pharmacokinetic simulation code: a benchmark against target-controlled infusion validation criteria using the Marsh propofol model](https://www.medrxiv.org/content/10.64898/2026.04.27.26351582v1)
  来源：medRxiv | 日期：2026-04-28 | 相关度：6.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Background. Large language models (LLMs) are increasingly used by clinicians to generate executable code for pharmacokinetic (PK) simulation. Whether such code meets the accuracy standards of target-controlled infusion s...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Polymer-Agent: Large Language Model Agent for Polymer Design.](https://pubmed.ncbi.nlm.nih.gov/42048526/)
  来源：PubMed | 日期：2026-04-28 | 相关度：6.15 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：按需聚合物发现对于从生物医学应用到增强材料的各个行业都至关重要。传统的聚合物实验涉及漫长的试错过程，消耗大量资源。虽然机器学习在性能预测和潜空间搜索方面加速了科学发现，但受限于基础设施，实验室研究人员往往难以直接调用代码和模型来提取特定结构与性能。本文提出了 Polymer-Agent，这是一个集成在终端中的闭环聚合物结构-性能预测框架，用于早期聚合物发现。该框架利用大语言模型（LLM）的推理能力，为用户提供性能预测、性能导向的聚合物结...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [All Models are Wrong, Some are Annotated: Automating Metadata in Biomedical Repositories](https://www.biorxiv.org/content/10.64898/2026.04.23.720371v1)
  来源：bioRxiv | 日期：2026-04-27 | 相关度：4.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：高质量元数据对科学发现至关重要，但生物医学数据库中普遍存在标注稀疏问题。本研究评估了大语言模型（LLMs）从神经科学数据库 ModelDB 的源代码中推断离子通道和受体亚型元数据的能力。研究人员从 ModelDB 提取了 5,133 个模型文件，其中 1,100 个经过人工标注（253 个用于测试）。实验对比了 GPT-5.2 和 GPT-mini 在零样本及启发式增强提示下的表现，并以特征工程驱动的 XGBoost 模型作为基线。结果...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Designing DNA With Tunable Regulatory Activity Using Discrete Diffusion](https://www.biorxiv.org/content/10.1101/2024.05.23.595630v3)
  来源：bioRxiv | 日期：2026-04-27 | 相关度：5.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：设计具有可调和背景特异性活性的调控 DNA 是生物技术和医学的核心目标。本研究提出了 DNA 离散扩散模型（D3），这是一种通过迭代核苷酸替换过程生成调控 DNA 的生成模型。在计算基准测试中，D3 在生成调控序列方面优于匹配的扩散基准模型，其生成的序列在目标活性、活性分布和序列组成上更接近天然序列。在 K562 细胞的 lentiMPRA 实验中，D3 设计的序列保留了可测量的调控活性，并比基准模型更有效地重现了基因组调控序列的活性分...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Subarachnoid hemorrhage: epidemiology, risk factors, pathogenesis, and clinical therapies.](https://pubmed.ncbi.nlm.nih.gov/42043672/)
  来源：PubMed | 日期：2026-04-27 | 相关度：5.0 | 新颖度：0.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：蛛网膜下腔出血（SAH）是一种致死率极高的脑血管急症，常导致严重的长期神经功能缺损。研究表明，SAH的发病率在不同地区和人群间存在显著差异，这由不可干预因素（如年龄、性别、遗传易感性）与可干预因素（如高血压、吸烟、代谢紊乱）共同决定。血管生物学与基因组学进展揭示，细胞外基质不稳定、内皮功能障碍及特定人群的遗传变异在动脉瘤形成和破裂中起关键作用。破裂后，SAH触发双相损伤级联反应：早期脑损伤（EBI）发生于数小时内，表现为颅内压升高、血脑...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
