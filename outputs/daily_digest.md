# 每日论文监控日报 (2026-04-06)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 20 篇新论文。

## 抓取状态

- arXiv：成功，命中 7 篇
- PubMed：成功，命中 18 篇
- bioRxiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='api.biorxiv.org', port=443): Read timed out. (read timeout=60)
- medRxiv：成功，命中 12 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [Tokenizing loops of antibodies.](https://pubmed.ncbi.nlm.nih.gov/41936024/)
  来源：PubMed | 日期：2026-12-31 | 相关度：9.15 | 新颖度：10.0
  匹配主题：foundation_model_agent
  中文摘要：The complementarity-determining regions (CDRs) of antibodies are loop structures that are key to their interactions with antigens and are of high importance to the design of novel biologics. Existing approaches for chara...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Digital Registrar: A Schema-First Framework for Multi-Cancer Privacy-Preserving Pathology Abstraction via Local LLMs](https://www.medrxiv.org/content/10.1101/2025.10.21.25338475v8)
  来源：medRxiv | 日期：2026-04-05 | 相关度：8.9 | 新颖度：6.7
  匹配主题：foundation_model_agent
  中文摘要：Background/Objectives: Surgical pathology reports contain the most granular diagnostic data for cancer, yet their predominant free-text format creates a "translational gap" that hinders automated registry entry and secon...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

## 可追踪

### Foundation Model / Agent

- [Citation Hallucination Determines Success: An Empirical Comparison of Six Medical AI Research Systems](https://www.medrxiv.org/content/10.64898/2026.04.02.26350091v1)
  来源：medRxiv | 日期：2026-04-04 | 相关度：7.55 | 新颖度：1.7
  匹配主题：foundation_model_agent
  中文摘要：Large language model (LLM) systems can now generate complete research manuscripts, yet their reliability in clinical medicine - where citation accuracy and reporting standards carry direct consequences - has not been sys...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Med-ICE: Enhancing Factual Accuracy in Medical AI through Autonomous Multi-Agent Consensus](https://www.medrxiv.org/content/10.64898/2026.04.02.26350080v1)
  来源：medRxiv | 日期：2026-04-04 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：The integration of Large Language Models into high-stakes clinical workflows is critically hampered by their lack of verifiable reliability and tendency to generate hallucinations. This paper introduces Med-ICE, an auton...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Multi-Task Learning and Soft-Label Supervision for Psychosocial Burden Profiling in Cancer Peer-Support Text](https://www.medrxiv.org/content/10.64898/2026.04.03.26350034v1)
  来源：medRxiv | 日期：2026-04-04 | 相关度：6.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Objective: Online cancer peer-support text contains signals of psychosocial burden beyond emotional tone, including treatment burden, financial strain, uncertainty, and unmet support needs. We evaluated 2 modeling extens...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [A neural-symbolic AI agent system for biomedical concept mapping.](https://pubmed.ncbi.nlm.nih.gov/41935204/)
  来源：PubMed | 日期：2026-04-04 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：生物医学概念映射旨在将自由文本描述链接到术语库和本体中的标准概念。现有方法主要分为两类：基于规则的系统虽具可解释性，但在处理歧义和扩展性方面存在困难；基于学习的方法利用上下文信号，但因训练数据有限，在长尾概念上表现不佳且缺乏解释性。为解决这些局限，我们提出了医疗概念映射（MCM），这是一种新型 Agent 工作流，利用语言模型在概念链接前将歧义提及重述为明确、标准的描述。这种重构显著提升了稀有概念和缩写概念的映射准确率。在 MedMen...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Quick on the Uptake: Eliciting Implicit Intents from Human Demonstrations for Personalized Mobile-Use Agents](http://arxiv.org/abs/2508.08645v2)
  来源：arXiv | 日期：2025-08-12 | 相关度：6.1 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：随着多模态大语言模型的进步，通过模拟人类与图形用户界面交互的移动端 Agent 实现任务自动化已成为可能。然而，现有方法主要关注人类的显式意图流（如操作步骤序列），忽视了隐式意图流（如个人偏好），导致难以构建个性化的移动端 Agent。本研究首先构建了 MobileIAR 数据集，包含人类意图对齐动作与基准动作，用于评估 Agent 与人类的意图对齐率（IAR）。随后，提出了基于意图流识别的 IFRAgent 框架。该框架通过分析显式意...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [ADSeeker: A Knowledge-Grounded Reasoning Framework for Industry Anomaly Detection and Reasoning](http://arxiv.org/abs/2508.03088v2)
  来源：arXiv | 日期：2025-08-05 | 相关度：6.8 | 新颖度：6.5
  匹配主题：foundation_model_agent
  中文摘要：Automatic vision inspection holds significant importance in industry inspection. While multimodal large language models (MLLMs) exhibit strong language understanding capabilities and hold promise for this task, their per...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [MZSGO: multimodal zero-shot protein function annotation via evolutionary signals and textual semantics.](https://pubmed.ncbi.nlm.nih.gov/41934619/)
  来源：PubMed | 日期：2026-04-03 | 相关度：7.1 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Although deep learning has significantly advanced the field of protein function prediction, current approaches are limited by their reliance on a narrow set of modalities. Specifically, they primarily rely on sequence pa...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Querying Structured Data Through Natural Language Using Language Models](http://arxiv.org/abs/2604.03057v1)
  来源：arXiv | 日期：2026-04-03 | 相关度：6.15 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：本文介绍了一种开源方法，允许用户通过自然语言查询结构化非文本数据集。针对检索增强生成（RAG）在处理数值和高度结构化信息时的局限性，本研究训练大语言模型（LLM）生成可执行查询。为实现这一目标，研究者引入了一套原则性的合成训练数据生成流水线，产生涵盖用户意图与底层数据集语义的多样化问答对。研究采用 QLoRA（4位量化）技术对紧凑型模型 DeepSeek R1 Distill 8B 进行微调，使其能在商用硬件上部署。通过对西班牙 Dur...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Adaptive Guidance for Retrieval-Augmented Masked Diffusion Models](http://arxiv.org/abs/2603.17677v2)
  来源：arXiv | 日期：2026-03-18 | 相关度：5.45 | 新颖度：6.0
  匹配主题：foundation_model_agent
  中文摘要：检索增强生成（RAG）通过引入外部知识提升语言模型的事实准确性。然而，当检索到的上下文存在噪声、不可靠或与模型参数化知识不一致时，会产生检索-先验冲突，导致生成质量下降。虽然该问题在自回归语言模型中已有研究，但在基于扩散的语言模型中仍未得到充分探索，其迭代去噪过程为整合检索上下文带来了独特挑战。本研究提出了 ARAM（自适应检索增强掩码扩散），这是一种针对 RAG 场景下掩码扩散模型（MDMs）的免训练自适应引导框架。ARAM 根据检索...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [LogicPoison: Logical Attacks on Graph Retrieval-Augmented Generation](http://arxiv.org/abs/2604.02954v1)
  来源：arXiv | 日期：2026-04-03 | 相关度：4.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：基于图的检索增强生成（GraphRAG）通过将大语言模型（LLM）的响应锚定在结构化知识图谱上，显著增强了其推理能力。尽管 GraphRAG 利用社区检测和关系过滤技术对传统的文本投毒和提示词注入攻击具有一定的内在抵抗力，但本研究发现其安全性本质上依赖于底层图谱的拓扑完整性。通过在不改变表面文本语义的情况下隐蔽地破坏逻辑连接，可以瓦解这种安全性。为此，我们提出了 LogicPoison 攻击框架，该框架针对逻辑推理而非注入虚假内容。具体...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [Beyond the Parameters: A Technical Survey of Contextual Enrichment in Large Language Models: From In-Context Prompting to Causal Retrieval-Augmented Generation](http://arxiv.org/abs/2604.03174v1)
  来源：arXiv | 日期：2026-04-03 | 相关度：4.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：大语言模型（LLMs）虽然在参数中编码了海量知识，但仍受限于静态知识、有限的上下文窗口以及弱结构化的因果推理能力。本综述沿“推理时提供的结构化上下文程度”这一核心轴线，对增强策略进行了统一阐述。研究涵盖了上下文学习（ICL）与提示工程、检索增强生成（RAG）、图检索增强生成（GraphRAG）以及因果检索增强生成（CausalRAG）。除了概念性对比，本文还提出了一套透明的文献筛选协议、声明审计框架以及结构化的跨论文证据合成方法，旨在区...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Extracting Social Determinants of Health from Electronic Health Records: Development and Comparison of Rule-Based and Large Language Model Methods](https://www.medrxiv.org/content/10.1101/2025.11.15.25339520v2)
  来源：medRxiv | 日期：2026-04-04 | 相关度：7.55 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：Background Social determinants of health (SDoH) are critical drivers of health outcomes but are often under-documented in structured electronic health record (EHR) data. Instead, SDoH are more commonly recorded in unstru...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Enhancing Medical Knowledge in Large Language Models via Supervised Continued Pretraining on Clinical Notes](https://www.medrxiv.org/content/10.64898/2026.04.02.26350065v1)
  来源：medRxiv | 日期：2026-04-04 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：由于临床文本获取受限，大语言模型（LLMs）的专业医学知识储备有限。本研究旨在利用去隐私化的临床笔记对开源指令模型进行持续预训练，并评估其在真实临床决策任务中的表现。研究者利用西达赛奈医疗系统（Cedars-Sinai Health System）的50万份去隐私化临床笔记，对Qwen3-4B Instruct模型进行监督微调，使其能够根据患者陈述生成医学决策（MDM）段落。评估涵盖了诊断预测、院内心脏骤停提及检测以及通用和生物医学基准...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Cognitive AI-Assisted Primary Care Health Delivery: A Pilot Study in Bangladesh](https://www.medrxiv.org/content/10.64898/2026.04.03.26349253v1)
  来源：medRxiv | 日期：2026-04-05 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：全球范围内医生短缺问题持续存在，严重威胁基层医疗的可及性。现有医疗 AI 应用多侧重于生成概率估计的预测性风险评分工具，未能有效缩短医生的诊疗时间。2025 年的研究指出，大语言模型缺乏可靠医学推理所需的元认知能力，即在信息缺失时无法通过主动提问来收集病史并更新鉴别诊断。本研究报告了 2025 年在孟加拉国开展的 ClinicalAssist 系统试点部署，该系统旨在复制临床工作流的每一个步骤。在针对 239 名唯一患者、277 次就诊...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [Reproducibility and Robustness of Large Language Models for Mobility Functional Status Extraction](https://www.medrxiv.org/content/10.64898/2026.04.03.26350117v1)
  来源：medRxiv | 日期：2026-04-05 | 相关度：5.75 | 新颖度：5.25
  匹配主题：foundation_model_agent
  中文摘要：临床叙述性文本包含关键的患者信息，但由于语言变异和记录习惯的差异，可靠的信息提取（IE）仍具挑战。大语言模型（LLMs）在临床IE中表现出极高的准确性，但其在临床部署中核心的可重复性（重复运行的稳定性）和鲁棒性（提示词微小变化下的稳定性）尚未得到一致量化。本研究评估了三种代表性开源LLM：稠密通用模型Llama 3.3、混合专家（MoE）通用模型Llama 4以及领域微调医学模型MedGemma。研究聚焦于国际功能、残疾和健康分类（IC...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Evaluating Large Language Models for Assessment of Psychosis Risk](https://www.medrxiv.org/content/10.64898/2026.04.02.26349960v1)
  来源：medRxiv | 日期：2026-04-04 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：精神病预防依赖于对临床高风险（CHR-P）个体的早期检测，但目前受限于临床评估需要专家对叙述性访谈进行解读，导致其难以大规模推广。本研究评估了大语言模型（LLMs）能否从访谈文本中提取临床信息以支持风险评估。研究人员利用来自373名参与者（其中77.7%为CHR-P）的678份PSYCHS访谈转录本，对11个开源LLM进行了评估。模型任务包括推断CHR-P状态，并估算15个症状领域的严重程度和频率。结果显示，大型模型表现最强，其中Lla...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Single-cell and spatial profiling in cancer biology and clinical oncology.](https://pubmed.ncbi.nlm.nih.gov/41933186/)
  来源：PubMed | 日期：2026-04-03 | 相关度：1.7 | 新颖度：0.25
  匹配主题：未命中具体主题
  中文摘要：多种单细胞和空间基因组学工具已彻底改变了研究者解析癌症等复杂疾病的能力。通过对复杂多模态数据的分析，研究者能够深入洞察肿瘤生态系统中的基因组学特征、细胞状态及相互作用，从而剖析显著的生物学机制，并深化对药物反应、耐药性及靶点发现的理解。然而，这些方法在实现其全部临床潜力之前仍面临多重挑战。本文探讨了单细胞与空间技术在临床应用中的机遇、障碍及潜在解决方案，涵盖了样本获取与保存方法、针对异质人群的分析手段及分析工具，并为在临床环境中稳健、可...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 产品应用 / 监测落地

- [Vision-language framework for multi-sequence brain magnetic resonance imaging](https://www.medrxiv.org/content/10.64898/2026.03.30.26349106v1)
  来源：medRxiv | 日期：2026-04-04 | 相关度：5.75 | 新颖度：0.75
  匹配主题：foundation_model_agent
  中文摘要：结构化磁共振成像（MRI）是诊断神经系统疾病的关键，但多序列脑部MRI的自动解读受限于跨序列推理和成像协议变异性的挑战。本研究提出了ReMIND，一个专为综合多序列和多体积脑部MRI分析定制的视觉-语言建模框架。ReMIND在超过73,000次去标识化患者就诊数据上进行训练，涵盖了来自不同临床和研究队列的850,000多个MRI序列及其配对的放射学报告。该框架结合了针对100万个临床基础问答（QA）对的大规模指令微调，以及用于放射学报告...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
