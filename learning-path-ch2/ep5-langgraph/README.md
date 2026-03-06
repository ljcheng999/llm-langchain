# 🎯 LangGraph Basics: Build Stateful AI Workflows Progressively

## Master the Fundamentals of Graph-Based AI - From Imports to Research Agent

Welcome to Master LangGraph Basics! Learn to build AI applications step by step, starting from basic imports and progressing to a complete research assistant with multiple tools.

## 🎯 Lab Objective

**Your Mission:** Master LangGraph fundamentals through 7 progressive tasks, building from simple imports to a complete research agent with calculator and web search capabilities.

## 📚 What is LangGraph?

LangGraph is a framework for building **stateful, multi-step AI workflows** using graphs. Unlike simple LLM chains, LangGraph gives you explicit control over how data flows through your application, enabling complex decision-making, loops, and conditional routing.

## 🏗️ What You'll Build

A progressive series of graphs that demonstrates:
1. **Basic Imports** - Foundation setup with StateGraph, END, TypedDict
2. **Node Functions** - State transformation basics without graphs
3. **Connected Edges** - Your first complete graph
4. **Multi-step Flows** - Document processing workflow
5. **Conditional Routing** - Dynamic decision-making
6. **Calculator Tool** - First LLM integration
7. **Research Agent** - Complete assistant with calculator + web search

## 📋 Lab Structure (7 Progressive Tasks)

### Task 1: Understanding Imports 📦
**File:** `task_1_understanding_imports.py` (44 lines)

**Concept:** Master the essential imports needed for LangGraph

**What You'll Do:**
- Import StateGraph and END from langgraph.graph
- Import TypedDict from typing
- Define your first State class with messages list
- Understand the building blocks WITHOUT execution

**Key Learning:** StateGraph creates workflows, END marks completion, State holds data

---

### Task 2: Creating Nodes ⚙️
**File:** `task_2_creating_nodes.py` (61 lines)

**Concept:** Learn that nodes are functions that transform state

**What You'll Do:**
- Create greet_node that generates a greeting
- Create enhance_node that adds decorations
- Test nodes manually WITHOUT a graph
- See how nodes return partial state updates

**Key Learning:** Nodes are functions that take state and return PARTIAL updates

---

### Task 3: Connecting Edges 🔗
**File:** `task_3_connecting_edges.py` (70 lines)

**Concept:** Build your first complete graph with edges

**What You'll Do:**
- Create your first StateGraph
- Add nodes using add_node
- Connect nodes with add_edge
- Set entry point and compile
- Run your first workflow!

**Key Learning:** StateGraph + add_node + add_edge = Complete workflow!

---

### Task 4: Complete Flow 🎯
**File:** `task_4_complete_flow.py` (86 lines)

**Concept:** Multi-step document processing workflow

**What You'll Do:**
- Build a 3-step workflow: outline → draft → review
- See state accumulation across multiple nodes
- Each node builds on previous results
- Complete multi-step processing

**Key Learning:** Multi-node workflows process data in stages with state accumulation

---

### Task 5: Conditional Routing 🔀
**File:** `task_5_conditional_routing.py` (115 lines)

**Concept:** Dynamic path selection based on state

**What You'll Do:**
- Analyze query length to determine routing
- Create router function that returns node names
- Route to quick_response or detailed_response
- Master add_conditional_edges

**Key Learning:** Router examines state → Returns node name → Graph routes dynamically

---

### Task 6: Calculator Tool 🧮
**File:** `task_6_calculator_tool.py` (124 lines)

**Concept:** First LLM integration as a calculator

**What You'll Do:**
- Classify queries as math or non-math
- Route to calculator_node for math queries
- Use LLM to solve calculations
- Handle non-math queries gracefully

**Key Learning:** Tools are just nodes with specific functions, LLM can act as calculator

---

### Task 7: Research Agent 🔬
**File:** `task_7_research_agent.py` (146 lines)

**Concept:** Complete assistant with multiple tools

**What You'll Do:**
- Initialize DuckDuckGo search
- Classify queries as math or search
- Route to calculator for math
- Route to web search for information
- Build a complete research assistant!

**Key Learning:** Smart routing between multiple tools based on query type

---

## 🔑 Key Concepts

### Progressive Learning Path
```
Task 1: Imports        → Foundation setup
       ↓
Task 2: Nodes          → State transformation
       ↓
Task 3: Edges          → Connect nodes
       ↓
Task 4: Complete Flow  → Multi-step workflow
       ↓
Task 5: Routing        → Dynamic decisions
       ↓
Task 6: Calculator     → LLM integration
       ↓
Task 7: Research Agent → Multiple tools
```

### Why This Progressive Approach?
- **Start Simple:** Begin with imports, not complex examples
- **Build Understanding:** Each task adds ONE new concept
- **No LLM Until Ready:** Tasks 1-5 use simple strings
- **Gradual Complexity:** From 44 to 146 lines progressively
- **Real Achievement:** End with a working research agent!

## 🚦 Getting Started

### 1. Environment Setup
```bash
# Activate virtual environment
uv venv --python 3.13.11

# Install dependencies
uv add langgraph langchain langchain-openai ddgs
```

### 2. Required Packages
- `langgraph` - Stateful graph framework
- `langchain` - Core LLM abstractions
- `langchain-openai` - OpenAI integration
- `ddgs(duckduckgo-search)` - Free web search (no API key needed!)

### 3. Environment Variables
Pre-configured in the container:
- `OPENAI_API_KEY` - Authentication
- `OPENAI_MODEL` - Default model (gpt-4.1-mini)

## 📂 File Structure

```
llm-eps/learning-path/ep5-langgraph/
├── task_1_understanding_imports.py
├── task_2_creating_nodes.py
├── task_3_connecting_edges.py
├── task_4_complete_flow.py
├── task_5_conditional_routing.py
├── task_6_calculator_tool.py
├── task_7_research_agent.py
├── README.md                       # this file
```

## 🏃 Running the Lab

Execute tasks in sequential order:

```bash
# Task 1: Understanding Imports
python3 ep5-langgraph/task_1_understanding_imports.py

# Task 2: Creating Nodes
python3 ep5-langgraph/task_2_creating_nodes.py

# Task 3: Connecting Edges
python3 ep5-langgraph/task_3_connecting_edges.py

# Task 4: Complete Flow
python3 ep5-langgraph/task_4_complete_flow.py

# Task 5: Conditional Routing
python3 ep5-langgraph/task_5_conditional_routing.py

# Task 6: Calculator Tool
python3 ep5-langgraph/task_6_calculator_tool.py

# Task 7: Research Agent
python3 ep5-langgraph/task_7_research_agent.py
```


## 🎯 Expected Outcomes

By completing this lab, you'll understand:

1. **Foundation Setup**
   - Essential imports for LangGraph
   - State definition with TypedDict
   - Building blocks before execution

2. **Nodes as State Transformers**
   - Functions that take state and return partial updates
   - No side effects - pure state transformations
   - Testing nodes without graphs

3. **Graphs as Orchestrators**
   - StateGraph manages node execution order
   - Fixed edges for linear flow
   - Entry points and compilation

4. **Multi-Step Workflows**
   - State accumulation across nodes
   - Each node building on previous results
   - Complex document processing

5. **Conditional Routing**
   - Router functions examine state
   - Dynamic path selection
   - Mapping router outputs to nodes

6. **Tool Integration**
   - LLM as a calculator
   - Query classification
   - Smart tool routing

7. **Complete Research Agent**
   - Multiple tool integration
   - Web search capabilities
   - Intelligent query routing

## 🆘 Troubleshooting

### Common Issues:

**Import Error:**
```bash
# Solution: Reinstall packages
uv add langgraph langchain langchain-openai ddgs
```

**State Type Error:**
```python
# Problem: Missing field in State
class State(TypedDict):
    field1: str
    # field2: str  # ← Forgot to add this!

# Solution: Add all required fields
```

**Routing Error:**
```python
# Problem: Router output doesn't match node names
# Solution: Ensure router returns exact node names
```

**ddgs (DuckDuckGo) Rate Limit:**
```python
# DuckDuckGo may rate-limit requests
# Solution: Wait 10 seconds and retry
```

## 🏆 Challenge Extensions

Once you complete all 7 tasks, try these extensions:

1. **Add More Tools**
   - Weather API for weather queries
   - News API for current events
   - Database lookup for structured data

2. **Improve Classification**
   - Use LLM to classify queries (more accurate)
   - Add confidence scores to routing
   - Handle edge cases gracefully

3. **Add Validation**
   - Grade search results for relevance
   - Loop back if results are poor
   - Implement fallback strategies

## 📖 Your Learning Journey

```
START → Imports → Nodes → Edges → Flows → Routing → Calculator → Research Agent → COMPLETE!
  ↓        ↓        ↓       ↓       ↓        ↓          ↓            ↓
Learn   Create   Connect  Multi   Dynamic   LLM      Multiple    You're a
Basics  Functions Graph    Step   Decisions  Tool     Tools      LangGraph Pro!
```

## 🎉 What You've Achieved

By completing this lab, you've mastered:

✅ **LangGraph imports and setup**
✅ **Node creation and state transformation**
✅ **Graph construction with edges**
✅ **Multi-step workflows**
✅ **Conditional routing**
✅ **LLM tool integration**
✅ **Complete research agent with multiple tools**

**Key Achievement:** You've progressed from basic imports to building a complete AI research assistant! 🚀

## 🔥 Next Steps

**Advanced LangGraph Patterns:**
- 🧠 Memory systems for conversation history
- 👤 Human-in-the-Loop workflows
- 🔄 Self-improvement loops with validation
- 🤖 Multi-agent collaboration
- 🚀 Production deployment patterns

## 📚 Additional Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangGraph Tutorials](https://github.com/langchain-ai/langgraph/tree/main/examples)
- [LangChain Documentation](https://python.langchain.com/docs/)

---

**Happy Progressive Learning!** 🕸️

*Remember: Start simple, build understanding, achieve mastery!*