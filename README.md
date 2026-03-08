# 每日论文监控系统

这是一个面向 pathogenomics / pathogen detection / foundation model 方向的每日论文监控项目。它每天抓取最近 24 小时新增论文，完成去重、打分、分组，并输出中文日报。

现在也支持把累计知识库向量化，并通过 embedding + RAG 做检索。

同时提供一个静态前端，可以在 GitHub Pages 上在线浏览论文、过滤和提问。
前端源码现在放在 `frontend/src/`，再通过构建脚本生成到 `site/` 和 `docs/`。

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
- `outputs/knowledge_base_stats.md`：知识库统计与索引概览
- `data/state.json`：已见论文状态，避免重复推送
- `data/raw/*.json`：各数据源原始抓取结果
- `data/processed/knowledge_base.json`：累计沉淀的结构化知识库
- `data/processed/kb_embeddings.json`：向量化后的知识库索引
- `site/`：静态前端与站点数据
- `docs/`：为 branch-based GitHub Pages 兼容准备的镜像目录
- `frontend/src/`：前端源码目录

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
.venv/bin/python scripts/fetch_arxiv.py
.venv/bin/python scripts/fetch_pubmed.py
.venv/bin/python scripts/merge_rank.py
.venv/bin/python scripts/summarize_digest.py
.venv/bin/python scripts/build_knowledge_base.py
.venv/bin/python scripts/build_embeddings.py
.venv/bin/python scripts/build_site_bundle.py
.venv/bin/python scripts/build_frontend.py
```

也可以直接运行统一入口：

```bash
.venv/bin/python scripts/run_pipeline.py
```

如果你本地要走代理，直接在运行前设置环境变量即可，抓取脚本和统一入口都会自动继承：

```bash
export PROXY_URL=http://127.0.0.1:7897
export NO_PROXY=127.0.0.1,localhost

.venv/bin/python scripts/run_pipeline.py
```

如果你不想改全局环境变量，也可以只给当前命令挂代理：

```bash
PROXY_URL=http://127.0.0.1:7897 NO_PROXY=127.0.0.1,localhost .venv/bin/python scripts/run_pipeline.py
```

`PROXY_URL` 优先级高于系统里的 `HTTP_PROXY` / `HTTPS_PROXY` / `ALL_PROXY`。如果未设置 `PROXY_URL`，脚本会继续继承当前 shell 的代理环境。

抓取阶段现在按来源独立容错：

- `arXiv` 失败不会影响 `PubMed / bioRxiv / medRxiv`
- `PubMed` 失败不会阻断 `bioRxiv / medRxiv`
- `scripts/run_pipeline.py` 默认会继续完成后续离线步骤
- 如果你希望抓取失败时整个流程返回非零退出码，可以加 `--strict-fetch`

## 关于本地代理和 automation

如果你在本机终端里运行，下面这条通常可以抓全 4 个来源：

```bash
PROXY_URL=http://127.0.0.1:7897 NO_PROXY=127.0.0.1,localhost .venv/bin/python scripts/run_pipeline.py
```

但如果你把流程放进受限沙箱环境，`127.0.0.1:7897` 这种本机回环代理可能会被直接拦截。这时会出现：

- 代理本身是通的
- 终端里 `curl -x http://127.0.0.1:7897 ...` 可以成功
- automation 里却报 `Operation not permitted`

这不是脚本逻辑问题，而是运行环境不允许访问本机回环代理。要真正稳定抓全来源，建议优先使用下面两种方式之一：

- 直接在本机终端、`launchd`、`cron` 里跑 `scripts/run_pipeline.py`
- 使用能访问外网的 `self-hosted runner`

如果必须在受限 automation 里跑，就不要依赖本机 `127.0.0.1` 代理；需要改用运行环境本身可访问的远程代理，或者使用不经代理也能直连外网的网络环境。

## GitHub Actions 运行

如果你改为使用 GitHub Actions，每天抓取建议直接使用：

- [.github/workflows/update-knowledge-base.yml](/Users/mondyzy/projects/bgi/paper-monitor/.github/workflows/update-knowledge-base.yml)
- [.github/workflows/deploy-pages.yml](/Users/mondyzy/projects/bgi/paper-monitor/.github/workflows/deploy-pages.yml)

`update-knowledge-base.yml` 现在会直接调用：

```bash
.venv/bin/python scripts/run_pipeline.py
```

并支持通过 GitHub `Secrets / Variables` 覆盖 RAG 与站点默认 LLM 配置。

推荐配置：

- Secret：`BLTCY_API_KEY`
- Variable：`RAG_CHAT_BASE_URL=https://api.bltcy.ai/v1`
- Variable：`RAG_CHAT_MODEL=<你要用的 Gemini 模型名>`
- Variable：`SITE_LLM_BASE_URL=https://api.bltcy.ai/v1`
- Variable：`SITE_LLM_MODEL=<你要在前端默认展示的 Gemini 模型名>`

可选：

- `RAG_CHAT_PROVIDER=openai_compatible`
- `RAG_EMBEDDING_PROVIDER=local`
- `RAG_EMBEDDING_BASE_URL=<如果你后面要接远程 embedding>`
- `RAG_EMBEDDING_MODEL=<远程 embedding 模型名>`

说明：

- GitHub Actions 的 Secret 只会在工作流运行时注入，不会写进仓库
- 静态前端不能安全持有 API key，所以网页里只会预填 `Base URL / Model`
- 如果你要在网页里直接调用外部模型，仍然需要在浏览器本地填写 key

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
- 结构化知识库包含 `meta / summary / indexes / papers` 四层，便于后续扩字段和脚本调用
- 同时生成 `outputs/knowledge_base.md` 和 `outputs/knowledge_base_stats.md`，方便你直接浏览和后续做 Git 同步
- `build_embeddings.py` 会按 `content_hash` 复用已有向量，避免每次全量重建
- `manage_kb.py` 可直接查看统计、最近论文和单篇详情

示例：

```bash
.venv/bin/python scripts/manage_kb.py stats
.venv/bin/python scripts/manage_kb.py recent --limit 20 --sort importance
.venv/bin/python scripts/manage_kb.py show "doi:10.64898/2026.03.06.710164"
```

## 向量检索 / RAG

- `scripts/build_embeddings.py` 会把知识库转成向量索引，默认输出到 `data/processed/kb_embeddings.json`
- `scripts/search_kb.py "<query>"` 会做向量召回，返回最相关论文
- `scripts/search_kb.py "<query>" --rag` 会在召回结果上调用外部 LLM 生成中文回答
- 配置文件在 `config/rag.yaml`

默认配置下：

- `embedding.provider=local`，使用本地哈希 embedding，零额外依赖，可直接跑
- 如果你想外接模型，把 `embedding.provider` 改成 `openai_compatible`，并设置 `OPENAI_API_KEY`
- `chat.provider` 默认就是 OpenAI-compatible，可接 OpenAI、OpenRouter、OneAPI、vLLM、LM Studio 等兼容接口

示例：

```bash
.venv/bin/python scripts/build_embeddings.py
.venv/bin/python scripts/search_kb.py "bioinformatics agent for pathogen detection"
.venv/bin/python scripts/search_kb.py "recent LLM papers for genomics benchmark design" --rag
```

## 前端

- `site/index.html` 是静态站点入口
- `scripts/build_site_bundle.py` 会把知识库和摘要打包成 `site/data/site_bundle.json`
- `scripts/build_frontend.py` 会把 `frontend/src/` 编译/复制到 `site/` 和 `docs/`
- 页面支持：
  - 左侧分类导航、筛选和论文列表
  - 左侧按 `source / topic / year` 的导航树
  - 右侧查看论文详情、原文入口和详细 AI 解读
  - 本地收藏与研究备注
  - 查看每日摘要
  - 基于本地向量索引和关键词召回进行提问
  - 前端 Markdown 渲染，便于阅读结构化回答
  - 可选接入 OpenAI-compatible LLM 做在线 RAG；API Key 只保存在浏览器本地

本地预览可以直接用任意静态文件服务，例如：

```bash
python -m http.server 8000
```

然后打开 `http://localhost:8000/site/`

## 自动化建议

Codex App automation 可以绑定到这个 project，每次运行会在独立 worktree 中执行。现在更推荐直接跑统一入口：

```bash
PROXY_URL=http://127.0.0.1:7897 NO_PROXY=127.0.0.1,localhost .venv/bin/python scripts/run_pipeline.py
```

GitHub Actions 已经预留了两条工作流：

- `.github/workflows/update-knowledge-base.yml`：每天自动更新数据并提交回仓库
- `.github/workflows/deploy-pages.yml`：在 `main` 分支推送后自动部署前端到 GitHub Pages

如果你后续要把日报推送到飞书、邮件或 Slack，可以在 `summarize_digest.py` 后面再接一个通知脚本。
