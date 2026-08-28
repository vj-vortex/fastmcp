# 📋 FastMCP Learning Tasks & Roadmap

Use this checklist to track your learning progress through the modules. Each task has starter code in `exercise.py` and a reference in `solution.py`.

---

## 🎯 Task Checklist

### 🟢 Stage 1: The Basics (Tools, Signatures & Docstrings)
- [ ] **Task 1.1: Understand Automatic Tool Reflection**
  - Study [tutorials/01_basics/server.py](file:///c:/code/mcp/tutorials/01_basics/server.py) and [tutorials/01_basics/client.py](file:///c:/code/mcp/tutorials/01_basics/client.py).
  - Run the server and call the tools using the client script.
- [ ] **Task 1.2: Complete Exercise 1**
  - Open [tutorials/01_basics/exercise.py](file:///c:/code/mcp/tutorials/01_basics/exercise.py).
  - Implement a `calculator` tool with mathematical operations and docstrings.
  - Verify your solution with [tutorials/01_basics/solution.py](file:///c:/code/mcp/tutorials/01_basics/solution.py).

---

### 🟡 Stage 2: Complex Types & Pydantic Validation
- [ ] **Task 2.1: Model Complex Payloads**
  - Study [tutorials/02_complex_tools/server.py](file:///c:/code/mcp/tutorials/02_complex_tools/server.py).
  - Learn how Pydantic `BaseModel`, `Field`, `Literal`, and `Optional` provide JSON-schema constraints to LLMs.
- [ ] **Task 2.2: Complete Exercise 2**
  - Open [tutorials/02_complex_tools/exercise.py](file:///c:/code/mcp/tutorials/02_complex_tools/exercise.py).
  - Create a user registration and query tool using Pydantic models.
  - Verify with [tutorials/02_complex_tools/solution.py](file:///c:/code/mcp/tutorials/02_complex_tools/solution.py).

---

### 🔵 Stage 3: Resources & Dynamic Resource Templates
- [ ] **Task 3.1: Static & Dynamic Resources**
  - Study [tutorials/03_resources/server.py](file:///c:/code/mcp/tutorials/03_resources/server.py).
  - Understand how LLMs query read-only data via custom URIs (`system://status`, `docs://{topic}`).
- [ ] **Task 3.2: Complete Exercise 3**
  - Open [tutorials/03_resources/exercise.py](file:///c:/code/mcp/tutorials/03_resources/exercise.py).
  - Implement a database mock resource exposing tables at `db://tables/{table_name}`.
  - Verify with [tutorials/03_resources/solution.py](file:///c:/code/mcp/tutorials/03_resources/solution.py).

---

### 🟣 Stage 4: Dynamic Prompts & Workflows
- [ ] **Task 4.1: Prompt Templating**
  - Study [tutorials/04_prompts/server.py](file:///c:/code/mcp/tutorials/04_prompts/server.py).
  - Learn how to structure reusable agent prompts with `@mcp.prompt()`.
- [ ] **Task 4.2: Complete Exercise 4**
  - Open [tutorials/04_prompts/exercise.py](file:///c:/code/mcp/tutorials/04_prompts/exercise.py).
  - Build a structured PR Review prompt template with severity rating guidelines.
  - Verify with [tutorials/04_prompts/solution.py](file:///c:/code/mcp/tutorials/04_prompts/solution.py).

---

### 🟠 Stage 5: Context, Logging & Telemetry
- [ ] **Task 5.1: Injecting `Context`**
  - Study [tutorials/05_context_logging/server.py](file:///c:/code/mcp/tutorials/05_context_logging/server.py).
  - Learn how to send real-time logs (`ctx.info`, `ctx.warning`) and progress indicators (`ctx.report_progress`).
- [ ] **Task 5.2: Complete Exercise 5**
  - Open [tutorials/05_context_logging/exercise.py](file:///c:/code/mcp/tutorials/05_context_logging/exercise.py).
  - Implement a long-running batch job that sends stepped progress updates.
  - Verify with [tutorials/05_context_logging/solution.py](file:///c:/code/mcp/tutorials/05_context_logging/solution.py).

---

### 🔴 Stage 6: Production Transports & Tool Integration
- [ ] **Task 6.1: Stdio vs HTTP Transports**
  - Study [tutorials/06_production_transports/server.py](file:///c:/code/mcp/tutorials/06_production_transports/server.py).
  - Review [tutorials/06_production_transports/config_guide.md](file:///c:/code/mcp/tutorials/06_production_transports/config_guide.md).
- [ ] **Task 6.2: Connect to MCP Clients (Claude Desktop / Inspector)**
  - Test server with `npx @modelcontextprotocol/inspector`.
  - Connect your server configuration to your IDE or Claude Desktop.
