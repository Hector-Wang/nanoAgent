# Project Structure

## Overview

**nanoAgent — 从零理解 Agent**

极简开源教学项目，从 103 行核心代码出发，逐步构建涵盖**记忆、规划、工具扩展、多智能体协作、上下文压缩、安全防护**等全部关键特性的完整 AI Agent 系统。

核心理念：**Agent = LLM + 工具 + 循环**。

---

## Core Modules (01–07)

### 01-essence — Agent 本质
- **agent-essence.md** — 原理详解 (17KB)
- **agent-essence.py** — 103 行极简实现
- **核心内容**：Tool Schema、工具实现（execute_bash/read_file/write_file）、Agent 核心循环（ReAct：思考→行动→观察）
- **关键概念**：Function Calling、Agent Loop、Tool Schema

### 02-memory — 记忆与规划
- **agent-memory.md** — 记忆与规划机制 (15KB)
- **agent-memory.py** — 206 行带记忆实现
- **核心内容**：持久记忆、任务分解规划
- **新增能力**：Agent 能记住历史对话，面对复杂任务能先规划再执行

### 03-skills-mcp — 规则、技能与 MCP 协议
- **agent-skills-mcp.md** — 行为规则与 MCP (23KB，最大文档)
- **agent-skills-mcp.py** — 282 行扩展实现
- **核心内容**：行为规则、可复用技能、MCP (Model Context Protocol) 工具加载
- **新增能力**：自定义行为约束、复用已有技能、通过 MCP 扩展第三方工具

### 04-subagent — 子智能体
- **agent-subagent.md** — SubAgent 机制 (17KB)
- **agent-subagent.py** — 192 行子智能体实现
- **核心内容**：一次性子智能体、任务委派机制
- **新增能力**：主 Agent 创建子 Agent 并行处理子任务

### 05-teams — 多智能体团队协作
- **agent-teams.md** — 多 Agent 协作 (14KB)
- **agent-teams.py** — 270 行团队实现
- **核心内容**：持久 Agent、角色身份管理、团队通信
- **新增能力**：从临时工到正式团队，支持角色分配与协作

### 06-compact — 上下文压缩
- **agent-compact.md** — 上下文压缩策略 (13KB)
- **agent-compact.py** — 169 行压缩实现（含 bug 修复）
- **核心内容**：自动摘要压缩，防止 Context 窗口爆满
- **新增能力**：对话历史过长时自动摘要，节省 Token

### 07-safety — 安全与权限控制
- **agent-safe.md** — 安全防护机制 (14KB)
- **agent-safe.py** — 219 行安全实现
- **核心内容**：命令黑名单、人工确认、输出截断
- **新增能力**：三道安全防线，防止执行危险操作（如 `rm -rf /`）

---

## Extended Modules

### bonus — 功能合集
独立功能模块：
- **agent-command.py** — 命令模式
- **agent-observable.py** — 可观察性/事件系统
- **agent-preset.py** — 预设配置
- **agent-stream.py** — 流式输出
- 配套 8 篇 Markdown，涵盖：Agent 创建模式、命令模式、评估机制、文件系统、可观察性、流式处理、Token 管理、工具选择

### full — 完整集成版
- **agent-full.py** — 507 行，集成全部七篇能力
- **agent-full.md** — 集成说明
- **nanoAgent-bonus-harness.md** — 测试框架 (16KB)

### real-mcp — 真实 MCP 实现
- **nanoagent-bonus-mcp-real.md** — MCP 协议实战 (14KB)
- **nano_mcp_http_agent.py** — MCP HTTP Agent (2KB)
- **nano_mcp_http_server.py** — MCP HTTP Server (2KB)
- 通过 HTTP 实现真正的 MCP 通信

### llm-from-scratch — 从零理解 LLM
12 篇文档 + 12 个脚本，系统讲解 LLM 底层原理：
- **文档系列**：01-next-token-prediction → 02-token → 03-embedding → 04-attention → 05-transformer → 06-training → 07-inference
- **代码示例**：tokenizer_demo.py、embedding.py、attention.py、multi_head.py、transformer_anatomy.py、train_tiny.py、inference.py、generate.py 等
- **核心内容**：下一个词预测、Token 化、嵌入、注意力机制、Transformer 架构、训练与推理全流程

### nano-skill — 技能系统详解
5 篇系列文档（约 76KB），深入讲解 Agent 技能系统：
- **skill-01**：什么是 Skill
- **skill-02**：Skill 的解剖结构
- **skill-03**：第一个 Skill 实现
- **skill-04**：Skill Creator（技能创造者）
- **skill-05**：技能组合（Composition）

### tech-sharing — 技术分享
- **tech-sharing.md** — 约 27KB 技术分享文档

### tests — 测试套件
- **test_agent.py** — Agent 核心测试 (11KB)
- **test_compact.py** — 压缩功能测试 (4KB)
- **test_subagent.py** — 子智能体测试 (4KB)

---

## Key Statistics

| 类别 | 数量 |
|------|------|
| 核心系列篇章 | 7 篇 |
| Python 代码文件 | 20+ |
| Markdown 文档 | 30+ |
| 核心代码行数（7 个模块） | 103 → 206 → 282 → 192 → 270 → 169 → 219 |
| 完整版代码 | 507 行 |
| 测试文件 | 3 个 |

---

## Learning Path

```
推荐顺序：
01-essence → 02-memory → 03-skills-mcp → 04-subagent → 05-teams → 06-compact → 07-safety

按需跳入：
- 想懂 Agent 原理 → 01-essence
- 想加记忆 → 02-memory
- 想接 MCP/自定义工具 → 03-skills-mcp
- 想做并行任务 → 04-subagent
- 想做多 Agent 协作 → 05-teams
- 担心 Context 爆满 → 06-compact
- 担心安全隐患 → 07-safety
- 想要完整版 → full/
- 想学 LLM 底层原理 → llm-from-scratch/
```

---

*Generated: $(date)*
