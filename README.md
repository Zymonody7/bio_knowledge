# 每日论文监控系统

这是一个面向 pathogenomics / pathogen detection / foundation model 方向的每日论文监控项目。它每天抓取最近 24 小时新增论文，完成去重、打分、分组，并输出中文日报。

## 覆盖数据源

- arXiv
- PubMed
- bioRxiv
- medRxiv

优先使用公开 API，避免依赖脆弱网页爬虫。

## 输出文件

- `outputs/papers.csv`：结构化论文列表
- `outputs/daily_digest.md`：中文日报
- `outputs/knowledge_base.md`：可读知识库索引
- `data/state.json`：已见论文状态，避免重复推送
- `data/raw/*.json`：各数据源原始抓取结果
- `data/processed/knowledge_base.json`：累计沉淀的结构化知识库

## 字段设计

每篇论文输出以下核心字段：

- `title`
- `source`
- `date`
- `url`
- `abstract`
- `matched_topics`
- `relevance_score`
- `novelty_score`
- `why_it_matters`

`merge_rank.py` 额外补充 `category`，用于日报里的方法类、数据集类、foundation model 类、临床应用类分组。

## 安装

```bash
uv venv .venv
uv pip install --python .venv/bin/python -r requirements.txt
```

## 运行方式

按顺序执行：

```bash
env -u HTTP_PROXY -u HTTPS_PROXY -u ALL_PROXY -u http_proxy -u https_proxy -u all_proxy .venv/bin/python scripts/fetch_arxiv.py
env -u HTTP_PROXY -u HTTPS_PROXY -u ALL_PROXY -u http_proxy -u https_proxy -u all_proxy .venv/bin/python scripts/fetch_pubmed.py
.venv/bin/python scripts/merge_rank.py
.venv/bin/python scripts/summarize_digest.py
.venv/bin/python scripts/build_knowledge_base.py
```

也可以在自动化里按同样顺序每天运行。

## 检索主题

默认主题配置在 `config/topics.yaml`，已经包含以下方向的检索词：

- pathogenomics
- bioinformatics / sequencing platform for pathogen detection
- pathogen foundation model / LLM / Agent
- FAIR biomedical datasets / pretraining / post-training
- rapid pathogen identification / risk warning / monitoring platform

可以直接编辑 `config/topics.yaml` 扩展关键词和优先级。

源端抓取参数在 `config/sources.yaml`。其中 bioRxiv / medRxiv 默认限制分页深度，避免自动化因为近 24 小时 preprint 量过大而跑得过慢；如果你确认需要更全覆盖，可以提高 `max_pages`。

## 排序逻辑

- 对 pathogenomics、unknown pathogen discovery、pathogen foundation model、clinical metagenomics、metagenomics 等强相关主题给予更高相关度
- 通过 DOI、arXiv ID、PubMed ID 和标准化标题做去重
- 对新出现、更新时间近、带有 benchmark / dataset / foundation model / long-read / nanopore 信号的论文增加新颖度
- 中文日报按 `最值得看 / 可追踪 / 低优先级` 三档输出

## 知识库逻辑

- `build_knowledge_base.py` 会把当天 `outputs/papers.csv` 的论文累计合并到 `data/processed/knowledge_base.json`
- 同样使用 DOI、arXiv ID、PubMed ID 和标准化标题做知识库层去重
- 对重复出现的论文会保留更完整的摘要，并更新时间
- 同时生成 `outputs/knowledge_base.md`，方便你直接浏览和后续做 Git 同步

## 自动化建议

Codex App automation 可以绑定到这个 project，每次运行会在独立 worktree 中执行，适合每日定时跑下面这组命令：

```bash
env -u HTTP_PROXY -u HTTPS_PROXY -u ALL_PROXY -u http_proxy -u https_proxy -u all_proxy .venv/bin/python scripts/fetch_arxiv.py
env -u HTTP_PROXY -u HTTPS_PROXY -u ALL_PROXY -u http_proxy -u https_proxy -u all_proxy .venv/bin/python scripts/fetch_pubmed.py
.venv/bin/python scripts/merge_rank.py
.venv/bin/python scripts/summarize_digest.py
.venv/bin/python scripts/build_knowledge_base.py
```

如果你后续要把日报推送到飞书、邮件或 Slack，可以在 `summarize_digest.py` 后面再接一个通知脚本。
