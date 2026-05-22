# 每日论文监控日报 (2026-05-22)

本日报聚焦 pathogenomics、clinical metagenomics、unknown pathogen discovery、pathogen foundation model、FAIR biomedical datasets、long-read pathogen identification 等方向。

今日共整理 18 篇新论文。

## 抓取状态

- arXiv：失败，命中 0 篇，错误：HTTPSConnectionPool(host='export.arxiv.org', port=443): Read timed out. (read timeout=60)
- PubMed：成功，命中 71 篇
- bioRxiv：成功，命中 12 篇
- medRxiv：成功，命中 16 篇

注：部分来源抓取失败时，后续整理结果可能包含缓存原始数据，不等同于这些来源当天没有新论文。

## 最值得看

### Foundation Model / Agent

- [Language-dependent diagnostic safety of medical AI systems: a cross-lingual benchmarking and prospective clinical study](https://www.medrxiv.org/content/10.64898/2026.05.19.26353490v1)
  来源：medRxiv | 日期：2026-05-21 | 相关度：8.5 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Background Patients worldwide receive healthcare in many languages, yet medical AI systems are validated almost exclusively in high-resource languages such as English and Chinese, exposing patients in other linguistic se...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [A comprehensive study on Salmonella enterica serovar Richmond in farmed fish Pangasianodon hypophthalmus: insights into zoonotic potential, virulence and antimicrobial resistance.](https://pubmed.ncbi.nlm.nih.gov/42165977/)
  来源：PubMed | 日期：2026-05-21 | 相关度：10.0 | 新颖度：5.75
  匹配主题：pathogenomics, sequencing_bioinformatics, foundation_model_agent
  中文摘要：Salmonella enterica serovar Richmond is an emerging pathogen from contaminated animal food, posing a risk of global foodborne outbreaks. Few reports have documented this species in live aquatic organisms. In this study, ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

## 可追踪

### Foundation Model / Agent

- [MyeGPT: an AI agent for Multiple Myeloma](https://www.medrxiv.org/content/10.64898/2026.05.14.26353252v1)
  来源：medRxiv | 日期：2026-05-20 | 相关度：7.55 | 新颖度：2.0
  匹配主题：foundation_model_agent
  中文摘要：Today, advancements in our understanding of cancer biology are increasingly attributed to large-scale clinical-molecular datasets. The case in point for multiple myeloma, the second-most prevalent haematological malignan...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [OmniGene-4: A Unified Bio-Language MoE Model with Router-Level Interpretability](https://www.biorxiv.org/content/10.64898/2026.05.12.724542v2)
  来源：bioRxiv | 日期：2026-05-19 | 相关度：6.45 | 新颖度：1.0
  匹配主题：foundation_model_agent
  中文摘要：We introduce OmniGene-4, a unified bio-language foundation model built on Gemma-4-26B-A4B (30 layers, 128 experts per layer, top-8 routing). We inject 28,028 biological tokens (DNA and protein BPE, Foldseek 3Di, DSSP lab...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 方法创新

- [MARRVEL-MCP: An agentic interface for Mendelian disease discovery via tool-augmented context engineering.](https://pubmed.ncbi.nlm.nih.gov/42167217/)
  来源：PubMed | 日期：2026-05-21 | 相关度：6.75 | 新颖度：5.25
  匹配主题：pathogenomics, foundation_model_agent
  中文摘要：Variant interpretation in rare diseases requires navigating multiple genomic databases, each with strict input formats, while synthesizing heterogeneous evidence. This process creates significant barriers for non-experts...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [A Potent CRISPR-Cas12l Double-Strand Break Gene Editor.](https://pubmed.ncbi.nlm.nih.gov/42163774/)
  来源：PubMed | 日期：2026-05-21 | 相关度：6.45 | 新颖度：5.5
  匹配主题：foundation_model_agent
  中文摘要：Recently, a new family of CRISPR-Cas12 endonucleases from an unexplored phylum of bacteria, Armatimonadota , was discovered. Named Cas12l, they are compact (800-900 aa), recognize a 5' C-rich protospacer adjacent motif, ...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ProtmRNA: Cross-Modal Knowledge Transfer from Proteins to Messenger RNA](https://www.biorxiv.org/content/10.64898/2026.05.19.726141v1)
  来源：bioRxiv | 日期：2026-05-19 | 相关度：5.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Motivation According to the central dogma of molecular biology, messenger RNA (mRNA) sequences are directly translated into amino acid sequences, positioning mRNA as the fundamental intermediary between genetic informati...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [ATACompass enables cross-species cell identity mapping for scATAC-seq without gene annotations.](https://pubmed.ncbi.nlm.nih.gov/42167226/)
  来源：PubMed | 日期：2026-05-21 | 相关度：5.75 | 新颖度：6.25
  匹配主题：foundation_model_agent
  中文摘要：Single-cell assay for transposase-accessible chromatin with sequencing (scATAC-seq) provides insights into transcriptional regulation, but there remain challenges in cell identity annotation due to data sparsity and limi...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [CancerOmicsStudio (CoS): A web server for integrative and interpretable analysis of multi-omics cancer data.](https://pubmed.ncbi.nlm.nih.gov/42162949/)
  来源：PubMed | 日期：2026-05-20 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：Large-scale omics resources, including The Cancer Genome Atlas, Genomics of Drug Sensitivity in Cancer, and the Cancer Dependency Map, have become essential for cancer research. However, these datasets are distributed ac...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [resLens: genomic language models to enhance antibiotic resistance gene detection.](https://pubmed.ncbi.nlm.nih.gov/42168341/)
  来源：PubMed | 日期：2026-05-21 | 相关度：5.75 | 新颖度：5.75
  匹配主题：foundation_model_agent
  中文摘要：The rise of antibiotic resistance necessitates advanced tools to detect and analyze antibiotic resistance genes (ARGs). We present resLens, a family of genomic language models that leverage latent genomic representations...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Benchmarking General-Purpose and Medical AI Large Language Models for Clinical Assessment and Management in Parkinson's Disease](https://www.medrxiv.org/content/10.64898/2026.05.13.26353021v1)
  来源：medRxiv | 日期：2026-05-20 | 相关度：7.15 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Background: The clinical applicability of large language models (LLMs) in Parkinson's disease (PD) management remains insufficiently characterized, particularly in generative responses to clinical vignette scenarios. Obj...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

## 低优先级

### Foundation Model / Agent

- [Drug or Pokemon? An analysis of the ability of large language models to discern fabricated medications](https://www.medrxiv.org/content/10.64898/2026.01.12.26343930v3)
  来源：medRxiv | 日期：2026-05-20 | 相关度：5.75 | 新颖度：1.25
  匹配主题：foundation_model_agent
  中文摘要：Background Large language models (LLMs) are increasingly used in medication-related tasks despite limited evidence supporting their accuracy and safety. LLMs are vulnerable to adversarial attacks and may confabulate in r...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

- [Accelerating scientific discovery with Co-Scientist.](https://pubmed.ncbi.nlm.nih.gov/42156544/)
  来源：PubMed | 日期：2026-05-19 | 相关度：1.4 | 新颖度：0.5
  匹配主题：未命中具体主题
  中文摘要：Scientific discovery is driven by scientists generating novel hypotheses for complex problems that undergo rigorous experimental validation. To augment this process, we introduce Co-Scientist, a multi-agent AI system bui...
  为什么值得看：这篇工作偏基础模型/Agent方向，可能影响病原检测任务的建模上限，值得关注其任务定义与评测设计。

### 数据集 / Benchmark

- [A pan-cancer regulatory atlas of 6,983 GWAS variants prioritizes recurrent regulatory annotations and candidate programs at cancer risk loci](https://www.medrxiv.org/content/10.64898/2026.05.16.26353369v1)
  来源：medRxiv | 日期：2026-05-20 | 相关度：1.7 | 新颖度：0.75
  匹配主题：未命中具体主题
  中文摘要：Genome-wide association studies have identified thousands of cancer risk variants in non-coding regions, yet their regulatory mechanisms remain largely uncharacterized. Here we present a regulatory annotation atlas of 6,...
  为什么值得看：这篇工作偏数据集或基准构建，适合判断是否能作为病原组学训练或评测资源。

### 方法创新

- [Interpretable fine-tuned large language models facilitate making genetic test decisions for rare diseases.](https://pubmed.ncbi.nlm.nih.gov/42156861/)
  来源：PubMed | 日期：2026-05-19 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Clinical decision making often relies on expert judgment guided by established guidelines, which can be challenging to standardize and abstract to implement. For example, selecting between gene panels and whole exome/gen...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

- [AI-genomics synergy for drug repurposing in breast cancer: an interpretability-driven framework.](https://pubmed.ncbi.nlm.nih.gov/42162002/)
  来源：PubMed | 日期：2026-05-20 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Breast cancer's genomic heterogeneity complicates drug discovery, making repurposing an attractive but challenging strategy. Advances in artificial intelligence now enable integration of multi-omics data to reveal drug-g...
  为什么值得看：这篇工作更像方法创新，可能直接关联 metagenomics、long-read 或 pathogen identification 流程优化。

### 产品应用 / 监测落地

- [Evaluating Sycophancy in Frontier Models Using Persona-Driven Challenge](https://www.medrxiv.org/content/10.64898/2026.05.17.26353406v1)
  来源：medRxiv | 日期：2026-05-20 | 相关度：5.75 | 新颖度：0.25
  匹配主题：foundation_model_agent
  中文摘要：Large language models (LLMs) are increasingly used for lay health queries, yet may abandon correct recommendations under pressure, a vulnerability termed sycophancy. We evaluated sycophancy across five frontier LLMs (Cla...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。

- [ASO Special Article: Proceedings of the Inaugural Joint US-India Cancer Dialogue: Accelerating Collaboration to Advance Cancer Prevention, Early Detection, Treatment, and Care.](https://pubmed.ncbi.nlm.nih.gov/42166060/)
  来源：PubMed | 日期：2026-05-21 | 相关度：1.7 | 新颖度：5.25
  匹配主题：未命中具体主题
  中文摘要：Cancer is a leading cause of death in both the USA and India. During Prime Minister Narendra Modi's State Visit to Washington, DC in June 2023, the two governments announced several cooperation commitments. One such comm...
  为什么值得看：这篇工作更接近临床/监测落地，适合评估其对快速识别、预警或治疗辅助的实际价值。
