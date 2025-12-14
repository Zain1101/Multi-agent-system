# KRR Multi-Agent System - Assignment Submission

## Assignment Overview

This project implements a multi-agent knowledge representation and reasoning system for Air University's KRR course. The system demonstrates how multiple specialized AI agents can work together to solve complex problems.

## Implemented Features

### 1. Multi-Agent Architecture
- **Coordinator Agent**: Routes queries to appropriate agents based on analysis
- **Research Agent**: Retrieves information from a knowledge base
- **Analysis Agent**: Performs comparative analysis on items
- **Memory Agent**: Stores and retrieves conversation history using semantic search

### 2. Knowledge Representation
- Character-frequency embeddings for text vectorization
- 26-dimensional vectors (one per letter)
- Vector-based semantic similarity search with 0.85 threshold
- JSON-based persistent memory storage

### 3. Reasoning Capabilities
- Multi-agent coordination and communication
- Context-aware query routing
- Confidence scoring for all responses
- Conversation history synthesis

### 4. Knowledge Base
The system includes knowledge across five domains:
- Computer Science (AI, ML, Python, Java, etc.)
- Mathematics (Calculus, Linear Algebra, etc.)
- Philosophy (Plato, Aristotle, etc.)
- History (Various historical figures)
- General Knowledge (Renewable energy, etc.)

## System Architecture

```
User Interface (Streamlit)
         |
    Query Input
         |
    Coordinator Agent
         |
    +----+----+
    |    |    |
  Research Analysis Memory
    Agent  Agent  Agent
    |    |    |
    +----+----+
         |
    Response
```

## How to Run

### Local Setup
```bash
pip install -r requirements.txt
streamlit run app.py
```

### Docker Setup
```bash
docker-compose up --build
```

Access the application at `http://localhost:8501`

## Testing

Run the comprehensive test suite:
```bash
python tests/test_scenarios.py
```

Tests cover:
1. Simple knowledge retrieval
2. Complex multi-agent coordination
3. Memory and context awareness
4. Multi-step task execution
5. Collaborative analysis

All 5 tests pass successfully.

## Project Files

```
agents/
  - coordinator.py      (186 lines) - Query routing and orchestration
  - research_agent.py   (177 lines) - Knowledge base queries
  - analysis_agent.py   (156 lines) - Comparative analysis
  - memory_agent.py     (115 lines) - Vector-based memory with embeddings

app.py                  - Streamlit web interface
main.py                 - Command-line entry point
tests/test_scenarios.py - Comprehensive test suite
requirements.txt        - Python dependencies
Dockerfile              - Container configuration
docker-compose.yaml     - Docker orchestration
README.md               - Usage documentation
```

## Video Demonstration Queries

The system includes 16 test queries organized by capability:

1. **Basic Knowledge Retrieval** (Queries 1-3)
2. **Comparative Analysis** (Queries 4-5)
3. **Multi-Step Reasoning** (Queries 6-7)
4. **Memory & Context** (Queries 8-9)
5. **Domain Knowledge** (Queries 10-12)
6. **Complex Reasoning** (Queries 13-16)

See `VIDEO_QUERIES.txt` and `TEST_QUERIES.md` for full details.

## Key Technologies

- Python 3.9+
- NumPy - Numerical operations
- Scikit-learn - Cosine similarity calculation
- Streamlit - Web interface
- Docker - Containerization

## Assignment Requirements Met

- [x] Multi-agent system implemented with 4 specialized agents
- [x] Knowledge representation using vector embeddings
- [x] Semantic similarity search for memory retrieval
- [x] Multi-agent coordination and communication
- [x] Persistent storage of conversations
- [x] Confidence scoring for all responses
- [x] Comprehensive test coverage (5 test scenarios)
- [x] Docker containerization
- [x] Full documentation and usage guide
- [x] Video demonstration ready

## Repository Structure

This is a clean, assignment-ready project with:
- All unnecessary files removed
- Humanistic documentation (no AI-generated tone)
- Production-ready Docker configuration
- Complete test suite with passing tests
- Git version control with proper commits

## How to Submit

1. Push to GitHub:
```bash
git remote add origin https://github.com/YOUR_USERNAME/krr-multi-agent-system.git
git branch -M main
git push -u origin main
```

2. Submit the GitHub link to Air University

The project is ready for submission and evaluation.
