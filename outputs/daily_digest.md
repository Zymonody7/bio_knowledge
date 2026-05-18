# 每日论文监控日报 (2026-05-18)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 11 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：429 Client Error: Too Many Requests
- PubMed：成功，命中 34 篇
- bioRxiv：成功，命中 16 篇
- medRxiv：成功，命中 8 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

今天这一档没有命中论文。

## 可追踪

### Foundation Model / Agent

- [Bio-BLIP: A Multimodal Architecture for Transferable Reasoning in Genomic Variant Interpretation](https://www.biorxiv.org/content/10.64898/2026.05.12.724740v1)
  来源：bioRxiv | 日期：2026-05-15 | 相关度：8.9 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：生物学假设的开发需要整合 DNA 序列、基因背景、蛋白质功能和既往文献等异构证据。现有模型多采用文本化或嵌入投影方式，且往往局限于特定微调任务。本研究提出 Bio-BLIP，一种基于 Q-former 的多模态架构，利用生物嵌入和 LLM 在无需任务特定微调的情况下实现复杂推理。Bio-BLIP 通过主 Q-former 整合 DNA、基因、蛋白质和文本四种模态信息，将其转化为 LLM 主干的固定长度前缀。该模型在人类遗传变异注释任务上...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A Comparative Study in Surgical AI: Potential and Limitations of Data, Compute, and Scaling](https://www.medrxiv.org/content/10.64898/2026.03.26.26349455v4)
  来源：medRxiv | 日期：2026-05-17 | 相关度：6.8 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：本研究探讨了人工智能在外科图像分析领域的潜力与局限，特别是针对神经外科手术器械检测这一核心任务。研究人员评估了2023年至2026年初发布的19个开源视觉语言模型（VLM）的零样本性能，结果显示仅有一个模型略微超过13.4%的基准线。通过使用LoRA微调Gemma 3 27B模型生成结构化JSON预测，准确率提升至47.63%；而采用专用分类头的方法进一步将准确率提高到51.08%。实验发现，即使将可训练参数增加近三个数量级，验证集准确...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Simulating population compliance with pandemic interventions using large language models](https://www.medrxiv.org/content/10.64898/2026.05.12.26352942v1)
  来源：medRxiv | 日期：2026-05-15 | 相关度：6.55 | 新颖度：1.5
  匹配主题：foundation_model_agent
  中文摘要：有效的流行病应对需要准确模拟人群对非药物干预措施（NPIs）的依从性，但传统模型常将行为变化视为固定情景而非演化过程。本研究测试了基于大语言模型（LLM）的智能体是否能针对随时间变化的 NPIs 和疾病风险生成个体化行为反应。研究在波士顿、丹佛和圣安东尼奥三个美国城市实例化了具有人口统计学代表性的智能体，并将其置于 COVID-19 早期疫情演变和政策环境中，且未拟合观测到的移动数据。通过三种前沿 LLM 及其集成模型，智能体在餐厅、零...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [Prompt-Only Gene-Circuit Modeling with a Large Language Model Simulates the synNotch Spheroids.](https://pubmed.ncbi.nlm.nih.gov/41968604/)
  来源：PubMed | 日期：2026-05-15 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：形态发生源于基因调节回路将生化信号转化为空间组织的细胞命运，但构建这些过程的定量模拟具有极高的技术门槛。本研究提出了一种“仅限提示词”（prompt-only）的流程，利用大语言模型（LLM）直接从自然语言描述的生物学规范中自动生成 CompuCell3D (CC3D) 模拟代码。以经典的 synNotch 球体实验为基准，研究证明 LLM 生成的代码无需人工编程即可捕捉接触依赖性信号传导、钙粘蛋白介导的粘附及多细胞分选动力学的关键特征...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A phenotype-to-mechanism framework links phenome-wide comorbidity architecture to molecular mechanisms and therapeutic discovery in complex diseases](https://www.medrxiv.org/content/10.64898/2026.05.13.26353128v1)
  来源：medRxiv | 日期：2026-05-17 | 相关度：6.9 | 新颖度：5.25
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：复杂人类疾病具有显著的临床异质性，且往往缺乏足够的分子和组学数据，阻碍了治疗开发。本研究提出 PiMInfer，一种从表型到机制的推理框架。该框架利用广泛可得的真实世界临床数据进行深度表型表征，并结合生物医学知识图谱，将疾病的临床异质性解析为表型相关的分子模块，从而加速治疗靶点发现。研究者将 PiMInfer 应用于化脓性汗腺炎（HS），识别出一致的表型相关 HS 基因模块（PiHSM）和功能内型，并经多模态证据验证。通过 PiHSM ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Thoughts-as-Planning: Latent World Models for Chain-of-Thoughts Optimization via Reinforcement Planning](https://www.biorxiv.org/content/10.64898/2026.05.10.724161v1)
  来源：bioRxiv | 日期：2026-05-15 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：大语言模型（LLMs）在多样化 NLP 任务中的成功，使得推理链（CoT）优化成为对齐模型行为与任务目标的关键步骤。现有的推理链微调方法通常依赖黑盒启发式或无梯度搜索，缺乏解释性、泛化性和样本效率。本文提出“思维即规划”（Thoughts-as-Planning）框架，将推理链优化形式化为潜在语义空间上的序列决策过程。我们将 LLM 建模为部分可观测环境，并学习一个潜在世界模型，用于模拟推理链编辑对下游输出的影响。通过构建保持邻近性的嵌...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 低优先级

### 方法创新

- [Toward scalable early cancer detection: evaluating EHR-based predictive models against traditional screening criteria.](https://pubmed.ncbi.nlm.nih.gov/42141079/)
  来源：PubMed | 日期：2026-05-15 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：现有的癌症筛查指南仅覆盖少数癌症类型，且依赖年龄或吸烟史等单一风险因素。本研究利用包含大规模纵向患者信息的电子健康记录（EHR），系统评估了基于EHR的预测模型在识别8种主要癌症（乳腺癌、肺癌、结直肠癌、前列腺癌、卵巢癌、肝癌、胰腺癌和胃癌）高风险人群中的临床效用。研究利用“All of Us”研究项目中超过86.5万名参与者的EHR、基因组和调查数据，将EHR模型与基因突变、家族史等传统风险因素进行了对比。结果显示，即使是基准建模方法...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Privacy-preserving local language models accurately identify the presence and timing of self-harm in electronic mental health records](https://www.medrxiv.org/content/10.1101/2025.10.27.25338892v2)
  来源：medRxiv | 日期：2026-05-16 | 相关度：6.45 | 新颖度：0.5
  匹配主题：foundation_model_agent
  中文摘要：自残是自杀最强的风险因素，但在临床电子健康记录（EHR）的非结构化自由文本中往往记录不精确。本研究评估了在英国国家医疗服务体系（NHS）安全基础设施内本地运行的隐私保护语言模型，在识别自残及其发生时间方面的准确性。研究从牛津健康 NHS 基金会信托基金中抽取了 1,352 份精神障碍患者的临床记录，并针对自残的存在性及其近期性（90天内、超过90天或未知）进行了标注，构建金标准数据集。研究采用 270 亿参数的本地化 Gemma 3 模...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Evidence Behind the Automation of Clinical Trial Statistical Programming: A Scoping Review of Technology Adoption, Validation Frameworks, and AI/ML Integration (2020-2025)](https://www.medrxiv.org/content/10.64898/2025.12.24.25342988v2)
  来源：medRxiv | 日期：2026-05-15 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：本综述系统总结了2020年至2025年间临床试验统计编程从手动编码向元数据驱动自动化流程转型的证据，重点关注表格、列表和图形（TLF）的生成及验证框架。研究通过检索PubMed、arXiv及PharmaSUG等渠道的789篇文献，最终纳入262篇并采用GRADE方法评估证据质量。结果显示：pharmaverse生态系统（如rtables、admiral）使TLF开发时间缩短15-25%；基于风险的验证结合CI/CD流水线减少了30-50...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Clinical Safety of AI-Generated Antibiotic Prescribing Advice: Guideline Adherence and Misinformation Risk Among Large Language Models](https://www.medrxiv.org/content/10.64898/2026.05.13.26352828v1)
  来源：medRxiv | 日期：2026-05-15 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：背景：大语言模型（LLMs）在远程医疗中应用日益广泛，但其在抗生素处方建议方面的安全性，尤其是在面对患者误导信息时的表现仍不明确。方法：本横断面分析研究通过 1,000 个轻度感染的初级保健临床病例，评估了 5 个聊天机器人模型的 5,000 条回复。研究重点评估了指南依从性、过度开药情况、误导信息的影响以及安全行为，并采用世卫组织（WHO）AWaRe 框架对不当处方进行分类。结果：总体而言，76.2% 的回复符合临床指南，但有 6.6...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Osteoarthritis phenotypes: advancing precision medicine through clinical, structural, and molecular stratification.](https://pubmed.ncbi.nlm.nih.gov/42141125/)
  来源：PubMed | 日期：2026-05-15 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：骨关节炎（OA）目前被认为是由生物、生物力学、代谢、遗传和分子机制驱动的异质性综合征，这种变异性解释了疾病进展和治疗反应的差异。本综述通过检索2010-2026年间主要数据库和国际骨关节炎研究协会（OARSI）资源，重点探讨了临床、结构和分子表型分层在精准医疗中的应用。研究识别出多种OA表型：炎症型、代谢型、生物力学型、软骨-软骨下骨型、疼痛致敏型和衰老型。影像学表型（如炎症、半月板-软骨、软骨下骨、萎缩、肥大型）和分子内型（低周转、结...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
