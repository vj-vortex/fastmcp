<div align="center">

# ⚡ FastMCP: Zero to Hero Mastery

**A complete, progressive hands-on curriculum and project repository for mastering the Model Context Protocol (MCP) using Python & FastMCP 3.x.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastMCP](https://img.shields.io/badge/FastMCP-3.4%2B-green.svg?style=for-the-badge&logo=fastapi&logoColor=white)](https://github.com/jlowin/fastmcp)
[![MCP Protocol](https://img.shields.io/badge/MCP-Standard-orange.svg?style=for-the-badge&logo=anthropic&logoColor=white)](https://modelcontextprotocol.io/)
[![License](https://img.shields.io/badge/License-MIT-purple.svg?style=for-the-badge)](LICENSE)

<p align="center">
  <a href="#-overview">Overview</a> •
  <a href="#-why-fastmcp">Why FastMCP?</a> •
  <a href="#-repository-structure">Structure</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-curriculum--learning-roadmap">Curriculum</a> •
  <a href="#-interactive-debugger--inspector">MCP Inspector</a> •
  <a href="#-production-integrations">Integrations</a>
</p>

---

</div>

## 📖 Overview

The **Model Context Protocol (MCP)** is an open standard that allows Large Language Models (LLMs) and AI agents (Claude, Cursor, Antigravity, ChatGPT) to securely interface with local data, custom code execution, and external APIs.

**FastMCP** is the most intuitive, developer-friendly Python framework for building MCP servers. This repository serves as a **battle-tested, production-ready learning path** taking you from zero knowledge to architecting enterprise MCP servers.

---

## 💡 Why FastMCP?

```
┌────────────────────────────────────────────────────────┐
│                      AI Clients                        │
│         (Claude Desktop, Cursor, Antigravity)          │
└───────────────────────────┬────────────────────────────┘
                            │  JSON-RPC 2.0 (stdio / HTTP)
┌───────────────────────────▼────────────────────────────┐
│                      FastMCP                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │    Tools     │  │  Resources   │  │   Prompts    │  │
│  │ (@mcp.tool)  │  │(@mcp.resource│  │(@mcp.prompt) │  │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  │
│         │                 │                 │          │
│  ┌──────┴─────────────────┴─────────────────┴───────┐  │
│  │    Pydantic Type Validation & Context Logging    │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────┘
```

- 🧩 **Zero-Boilerplate Decorators**: Turn standard Python functions into discoverable AI tools with `@mcp.tool()`.
- 🛡️ **Pydantic Validation**: Auto-generate JSON Schemas with strict type safety.
- 📁 **Dynamic Resources**: Expose custom schema-driven data feeds (`db://`, `file://`, `api://`).
- 💬 **Reusable Prompt Templates**: Expose modular system and user prompt engineering flows.
- 📡 **Multi-Transport Support**: Run locally over `stdio` or as a distributed microservice over `http`/SSE.

---

## 📂 Repository Structure

Every tutorial module is standalone, featuring a server, client, hands-on exercise, and reference solution:

```bash
fastmcp/
├── README.md                          # Comprehensive project documentation
├── TASKS.md                           # Progress checklist and hands-on exercises
├── pyproject.toml                     # Python dependencies & build config
├── server.py                          # Root quickstart server
├── client.py                          # Root quickstart client
└── tutorials/
    ├── 01_basics/                     # Functions as tools, type hints, docstrings
    │   ├── server.py                  # Runnable server
    │   ├── client.py                  # Async client call example
    │   ├── exercise.py                # Hands-on challenge
    │   └── solution.py                # Reference solution
    ├── 02_complex_tools/              # Pydantic schemas, nested payloads, error handling
    ├── 03_resources/                  # Static URI endpoints & dynamic resource templates
    ├── 04_prompts/                    # Parameterized prompt templates for agent workflows
    ├── 05_context_logging/            # Live telemetry, progress indicators, client logging
    └── 06_production_transports/      # Stdio vs HTTP, Claude Desktop setup & MCP Inspector
```

---

## 🚀 Quick Start

### 1. Prerequisites
Ensure you have [uv](https://github.com/astral-sh/uv) or Python 3.10+ installed.

```bash
# Clone the repository
git clone https://github.com/vj-vortex/fastmcp.git
cd fastmcp

# Install dependencies with uv
uv sync
```

### 2. Run the Demo Server & Client

Open two terminal windows:

**Terminal 1 (Start Server):**
```bash
uv run python server.py
```

**Terminal 2 (Execute Client):**
```bash
uv run python client.py
```

Output:
```text
Result: Hello Ford
```

---

## 🧭 Curriculum & Learning Roadmap

Follow the interactive progress checklist in [TASKS.md](TASKS.md).

| Module | Topic | Core Concepts | Hands-on Exercise |
|---|---|---|---|
| **[01_basics](tutorials/01_basics/)** | FastMCP Fundamentals | `@mcp.tool()`, type hints, docstrings to schema | Build a mathematical calculator tool |
| **[02_complex_tools](tutorials/02_complex_tools/)** | Pydantic & Schema Validation | `BaseModel`, `Field(description=...)`, Enums | User registration & validation pipeline |
| **[03_resources](tutorials/03_resources/)** | MCP Resources & URIs | `@mcp.resource("schema://{param}")`, static data | Database mock table resource provider |
| **[04_prompts](tutorials/04_prompts/)** | Prompt Engineering | `@mcp.prompt()`, reusable LLM agent templates | PR code review prompt with strictness levels |
| **[05_context_logging](tutorials/05_context_logging/)** | Context & Telemetry | `Context`, `ctx.info()`, `ctx.report_progress()` | Long-running diagnostics & progress reporting |
| **[06_production_transports](tutorials/06_production_transports/)** | Production & Deployment | `stdio` vs `http`, Claude Desktop config | Deploy server to Claude Desktop & Inspector |

---

## 🛠️ FastMCP Syntax Cheat Sheet

### 1. Simple Tool
```python
from fastmcp import FastMCP

mcp = FastMCP("DemoServer")

@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b
```

### 2. Complex Pydantic Tool
```python
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(description="Item name")
    price: float = Field(gt=0, description="Price per unit")

@mcp.tool()
def calculate_tax(item: Item, tax_rate: float = 0.08) -> float:
    """Calculate total tax for an item."""
    return round(item.price * tax_rate, 2)
```

### 3. Dynamic Resource Template
```python
@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: str) -> str:
    """Return user profile JSON by user ID."""
    return f'{{"id": "{user_id}", "status": "active"}}'
```

### 4. Progress & Telemetry
```python
from fastmcp import Context

@mcp.tool()
async def process_batch(items: list[str], ctx: Context) -> str:
    await ctx.info(f"Processing {len(items)} items...")
    for idx, item in enumerate(items, start=1):
        await ctx.report_progress(progress=idx, total=len(items))
    return "Done"
```

---

## 🔍 Interactive Debugger (MCP Inspector)

You can test any FastMCP server visually in your browser with the official MCP Inspector:

```bash
npx @modelcontextprotocol/inspector uv run python tutorials/01_basics/server.py
```

---

## 🔌 Production Integrations

### Claude Desktop Setup
Add your server to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "my-fastmcp-server": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\code\\mcp",
        "run",
        "python",
        "tutorials/06_production_transports/server.py"
      ],
      "env": {
        "MCP_TRANSPORT": "stdio"
      }
    }
  }
}
```

---

## 🤝 Contributing & Community

Contributions, issues, and feature requests are welcome!
- Fork the repository
- Create your feature branch (`git checkout -b feature/awesome-feature`)
- Commit your changes (`git commit -m 'feat: add awesome feature'`)
- Push to the branch (`git push origin feature/awesome-feature`)
- Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
