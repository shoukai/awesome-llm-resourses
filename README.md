# awesome-llm-resourses

## 目录

- [RAG (检索增强生成)](#rag-检索增强生成)

## RAG (检索增强生成)

RAG (检索增强生成) 是一种结合信息检索与生成模型的技术，能够提供准确且富有上下文的回答。以下是 RAG 相关的优质资源：

### RAG 框架与系统

* [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) - 全能 AI 应用，适用于任何 LLM，具备完整的 RAG 和 AI Agent 能力
* [MaxKB](https://github.com/1Panel-dev/MaxKB) - 基于 LLM 大语言模型的知识库问答系统，开箱即用，支持快速嵌入到第三方业务系统
* [RAGFlow](https://github.com/infiniflow/ragflow) - 基于深度文档理解的开源 RAG 引擎
* [Dify](https://github.com/langgenius/dify) - 开源 LLM 应用开发平台，直观界面集成 AI 工作流、RAG 管道、代理能力和模型管理等
* [FastGPT](https://github.com/labring/FastGPT) - 基于 LLM 的知识平台，提供开箱即用的数据处理和模型调用能力，支持通过 Flow 可视化进行工作流编排
* [Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat) - 基于 Langchain 与 ChatGLM 等不同大语言模型的本地知识库问答
* [QAnything](https://github.com/netease-youdao/QAnything) - 基于任何内容的问答系统
* [Quivr](https://github.com/QuivrHQ/quivr) - 个人生产力助手，支持与文档（PDF、CSV 等）和应用程序聊天
* [RAG-GPT](https://github.com/open-kf/rag-gpt) - 利用 LLM 和 RAG 技术，从用户自定义知识库学习，提供上下文相关答案
* [Verba](https://github.com/weaviate/Verba) - 由 Weaviate 驱动的检索增强生成聊天机器人

### 专业 RAG 技术与实现

* [FlashRAG](https://github.com/RUC-NLPIR/FlashRAG) - 用于高效 RAG 研究的 Python 工具包
* [GraphRAG](https://github.com/microsoft/graphrag) - 微软开发的模块化图形化检索增强生成系统
* [LightRAG](https://github.com/SylphAI-Inc/LightRAG) - 帮助开发者构建和优化检索器-代理-生成器管道
* [GraphRAG-Ollama-UI](https://github.com/severian42/GraphRAG-Ollama-UI) - 使用 Gradio UI 和额外功能的 Ollama GraphRAG 实现
* [nano-GraphRAG](https://github.com/gusye1234/nano-graphrag) - 简单易用的 GraphRAG 实现
* [RAG Techniques](https://github.com/NirDiamant/RAG_Techniques) - 展示各种高级 RAG 系统技术的仓库
* [TurboRAG](https://github.com/MooreThreads/TurboRAG) - 通过预计算分块文本的 KV 缓存加速检索增强生成
* [LightRAG](https://github.com/HKUDS/LightRAG) - 简单快速的检索增强生成
* [AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG) - RAG AutoML 工具，自动为您的数据找到最佳 RAG 管道
* [KAG](https://github.com/OpenSPG/KAG) - 基于 OpenSPG 引擎的知识增强生成框架

### RAG 评估与优化工具

* [ragas](https://github.com/explodinggradients/ragas) - RAG 管道评估框架
* [Chonkie](https://github.com/bhavnicksm/chonkie) - 轻量级、高速的 RAG 文本分块库
* [RAGLite](https://github.com/superlinear-ai/raglite) - 基于 PostgreSQL 或 SQLite 的 Python RAG 工具包
* [CAG](https://github.com/hhhuang/CAG) - 通过预加载相关资源和缓存运行时参数利用现代 LLM 的扩展上下文窗口
* [MiniRAG](https://github.com/HKUDS/MiniRAG) - 通过异构图索引和轻量级拓扑增强检索，使小模型实现良好 RAG 性能的简单框架
* [XRAG](https://github.com/DocAILab/XRAG) - 用于评估高级 RAG 系统基础组件的基准测试框架

### 图形化 RAG 实现

* [Fast-GraphRAG](https://github.com/circlemind-ai/fast-graphrag) - 智能适应用例、数据和查询的 RAG
* [Tiny-GraphRAG](https://github.com/limafang/tiny-graphrag) - 轻量级图形化 RAG 实现
* [DB-GPT GraphRAG](https://github.com/eosphoros-ai/DB-GPT/tree/main/dbgpt/storage/knowledge_graph) - 集成基于三元组的知识图谱和文档结构图，同时利用社区和文档检索机制增强 RAG 能力

### RAG 用户界面与应用

* [kotaemon](https://github.com/Cinnamon/kotaemon) - 开源、干净且可定制的 RAG UI，用于与文档聊天
* [RAGapp](https://github.com/ragapp/ragapp) - 在任何企业中使用 Agentic RAG 的最简单方法
* [TEN](https://github.com/TEN-framework/ten_framework) - 下一代 AI 代理框架，全球首个真正实时多模态 AI 代理框架

### 向量数据库

RAG 系统的核心组件之一是向量数据库，用于存储和检索文本嵌入。以下是一些优秀的向量数据库：

* [Chroma](https://github.com/chroma-core/chroma) - 为 AI 应用程序设计的开源嵌入式数据库
* [Milvus](https://github.com/milvus-io/milvus) - 开源向量数据库，为下一代 AI 应用提供支持
* [Pinecone](https://www.pinecone.io/) - 专为向量搜索设计的托管向量数据库
* [pgvector](https://github.com/pgvector/pgvector) - PostgreSQL 的开源向量相似度搜索扩展
* [Qdrant](https://github.com/qdrant/qdrant) - 高性能、一致性和可扩展的向量相似度搜索数据库
* [Weaviate](https://github.com/semi-technologies/weaviate) - 开源向量搜索引擎，支持语义搜索
* [Epsilla](https://github.com/epsilla-cloud/vectordb) - 高性能向量数据库，针对生成式 AI 应用进行了优化
* [Lancedb](https://github.com/lancedb/lancedb) - 开源向量数据库，为 AI 应用提供可扩展的嵌入式解决方案
* [Marqo](https://github.com/marqo-ai/marqo) - 基于张量的云原生搜索和分析引擎
* [pgvecto.rs](https://github.com/tensorchord/pgvecto.rs) - 用 Rust 编写的 PostgreSQL 向量扩展，专注于性能
* [Vellum](https://www.vellum.ai/products/retrieval) - 提供高级检索和 RAG 功能的平台

## 参考来源

- [awesome-LLM-resourses](https://github.com/WangRongsheng/awesome-LLM-resourses)
- [Awesome-LLMOps](https://github.com/tensorchord/Awesome-LLMOps)