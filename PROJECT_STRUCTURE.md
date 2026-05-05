# Project Structure

## Overview

**nanoAgent — Understanding Agents from Scratch**

A minimalist open-source educational project that builds a complete AI Agent system layer by layer, starting from 103 lines of core code. It progressively introduces **memory, planning, tool extensions, multi-agent collaboration, context compression, and safety** — all essential features of a production-grade Agent.

Core principle: **Agent = LLM + Tools + Loop**.

---

## Core Modules (01–07)

### 01-essence — Agent Fundamentals
- **agent-essence.md** — In-depth原理讲解 (17KB)
- **agent-essence.py** — 103-line minimalist Agent implementation
- **Topics**: Tool Schema, Tool Implementation (execute_bash/read_file/write_file), Agent core loop (ReAct: Think → Act → Observe)
- **Key concepts**: Function Calling, Agent Loop, Tool Schema

### 02-memory — Memory & Planning
- **agent-memory.md** — Memory and planning mechanisms (15KB)
- **agent-memory.py** — 206-line Agent with memory
- **Topics**: Persistent Memory, Task decomposition and planning
- **New capability**: Agent retains conversation history and can plan before executing complex tasks

### 03-skills-mcp — Rules, Skills & MCP Protocol
- **agent-skills-mcp.md** — Behavioral rules and MCP (23KB, largest doc)
- **agent-skills-mcp.py** — 282-line extended Agent
- **Topics**: Behavioral Rules, Reusable Skills, MCP (Model Context Protocol) tool loading
- **New capability**: Custom behavioral constraints, skill reuse, third-party tools via MCP

### 04-subagent — Sub-Agents
- **agent-subagent.md** — SubAgent mechanism (17KB)
- **agent-subagent.py** — 192-line SubAgent implementation
- **Topics**: One-off SubAgents, Task delegation
- **New capability**: Main Agent spawns sub-agents for parallel subtask execution

### 05-teams — Multi-Agent Team Collaboration
- **agent-teams.md** — Multi-Agent collaboration (14KB)
- **agent-teams.py** — 270-line team Agent
- **Topics**: Persistent Agents, Role-based identity, Team communication
- **New capability**: From ad-hoc workers to structured teams with role assignment and collaboration

### 06-compact — Context Compression
- **agent-compact.md** — Context compression strategy (13KB)
- **agent-compact.py** — 169-line compression Agent
- **Topics**: Automatic summarization to prevent context window overflow
- **New capability**: When conversation history grows too long, auto-summarizes old messages to save tokens

### 07-safety — Safety & Permission Control
- **agent-safe.md** — Safety mechanisms (14KB)
- **agent-safe.py** — 219-line safety-aware Agent
- **Topics**: Command blacklist, Human-in-the-loop confirmation, Output truncation
- **New capability**: Three-layer defense against dangerous operations (e.g. `rm -rf /`)

---

## Extended Modules

### bonus — Feature Collection
Standalone feature modules:
- **agent-command.py** — Command mode
- **agent-observable.py** — Observability / event system
- **agent-preset.py** — Preset configurations
- **agent-stream.py** — Streaming output
- 8 companion Markdown docs covering: Agent creation patterns, command mode, evaluation, filesystem, observability, streaming, token management, and tool selection

### full — Full-Featured Integration
- **agent-full.py** — 507-line integration of all 7 capabilities
- **agent-full.md** — Integration guide
- **nanoAgent-bonus-harness.md** — Testing harness (16KB)

### real-mcp — Real MCP Implementation
- **nanoagent-bonus-mcp-real.md** — MCP protocol实战 (14KB)
- **nano_mcp_http_agent.py** — MCP HTTP Agent (2KB)
- **nano_mcp_http_server.py** — MCP HTTP Server (2KB)
- **Topics**: True MCP communication over HTTP

### llm-from-scratch — Understanding LLMs from Scratch
12 Markdown docs + 12 Python scripts covering LLM internals:
- **Docs**: 01-next-token-prediction → 02-token → 03-embedding → 04-attention → 05-transformer → 06-training → 07-inference
- **Code**: tokenizer_demo.py, embedding.py, attention.py, multi_head.py, transformer_anatomy.py, train_tiny.py, inference.py, generate.py, etc.
- **Topics**: Next-token prediction, tokenization, embeddings, attention, Transformer architecture, training and inference

### nano-skill — Skill System Deep Dive
5-doc series (~76KB) covering the Agent skill system:
- **skill-01**: What is a Skill
- **skill-02**: Anatomy of a Skill
- **skill-03**: Your First Skill Implementation
- **skill-04**: Skill Creator
- **skill-05**: Skill Composition

### tech-sharing — Technical Sharing
- **tech-sharing.md** — ~27KB technical sharing document

### tests — Test Suite
- **test_agent.py** — Agent core tests (11KB)
- **test_compact.py** — Compression feature tests (4KB)
- **test_subagent.py** — SubAgent tests (4KB)

---

## Key Statistics

| Category | Count |
|----------|-------|
| Core series modules | 7 |
| Python files | 20+ |
| Markdown docs | 30+ |
| Core code lines (7 modules) | 103 → 206 → 282 → 192 → 270 → 169 → 219 |
| Full integration | 507 lines |
| Test files | 3 |

---

## Learning Path

```
Recommended sequence:
01-essence → 02-memory → 03-skills-mcp → 04-subagent → 05-teams → 06-compact → 07-safety

Jump in by topic:
- Agent fundamentals → 01-essence
- Adding memory → 02-memory
- MCP / custom tools → 03-skills-mcp
- Parallel tasks → 04-subagent
- Multi-agent collaboration → 05-teams
- Context window overflow → 06-compact
- Security concerns → 07-safety
- Full-featured version → full/
- LLM internals → llm-from-scratch/
```

---

*Generated: $(date)*
