# KRR Multi-Agent System

A multi-agent system where different AI agents work together to answer questions, analyze information, and remember past conversations. Built for a university assignment on knowledge representation and reasoning.

## What Does It Do?

The system has four main agents that each do different things:

1. **Coordinator** - Listens to your question and decides which other agents should help answer it
2. **Research Agent** - Searches through a knowledge base to find relevant information
3. **Analysis Agent** - Compares and evaluates different items or ideas
4. **Memory Agent** - Remembers previous conversations and can find similar past questions

When you ask a question, the coordinator routes it to the right agent(s), they process it, and you get a response with a confidence score showing how sure the system is about the answer.

## How It Works

The system uses a simple but effective technique called character-frequency embeddings. Instead of using complex AI models, it converts text into vectors (26 numbers, one for each letter). When you ask a question, it converts that to a vector and compares it to vectors of stored memories to find similar past conversations.

## Installation & Running

### Local Setup

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open http://localhost:8501 in your browser.

### Using Docker

```bash
docker-compose up --build
```

The app runs on http://localhost:8501

## Project Files

```
agents/
  - coordinator.py         # Routes queries to right agents
  - research_agent.py      # Searches knowledge base
  - analysis_agent.py      # Compares items
  - memory_agent.py        # Stores and retrieves memories

app.py                      # Web interface
main.py                     # Main entry point
requirements.txt            # Python packages
Dockerfile                  # Container setup
docker-compose.yaml         # Docker configuration
```

## Testing

Run the test suite:

```bash
python tests/test_scenarios.py
```

This tests the system with 5 different types of queries to make sure everything works properly.

## Key Features

- **Multi-agent coordination** - Different agents work together
- **Memory system** - Remembers past conversations
- **Knowledge base** - Has facts about computers, math, philosophy, history, and general knowledge
- **Confidence scores** - Shows how confident the system is in each answer
- **Easy to understand** - Simple design, no complex external dependencies
- **Docker ready** - Easy to deploy and run anywhere

## How to Use

Type your question in the web interface. The system will:

1. Analyze your question
2. Send it to the right agent(s)
3. Get information from the knowledge base or memory
4. Return an answer with a confidence score

You can ask follow-up questions and the system remembers the conversation context.
