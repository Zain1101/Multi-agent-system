# Test Queries for Video Demonstration

Use these queries in order to show the different capabilities of the system. Each query is designed to demonstrate a specific feature.

## Section 1: Simple Knowledge Base Questions

These show the system retrieving information from its knowledge base.

### Query 1
**What is artificial intelligence?**

Expected: The system retrieves the AI definition from the knowledge base and returns it with a confidence score.

### Query 2
**Tell me about Python programming**

Expected: The system finds information about Python in the knowledge base and provides details about the programming language.

### Query 3
**What is machine learning?**

Expected: The system returns information about machine learning from its computer science knowledge base.

## Section 2: Comparative Analysis

These queries trigger the analysis agent to compare multiple items.

### Query 4
**Compare Python and Java**

Expected: The system analyzes both programming languages across multiple dimensions (speed, learning curve, community, use cases, etc.) and provides a detailed comparison.

### Query 5
**What are the differences between supervised and unsupervised learning?**

Expected: The system compares these two types of machine learning approaches with detailed analysis.

## Section 3: Multi-Step Tasks

These queries require the system to break down complex questions into steps.

### Query 6
**How do I learn programming? Start with learning the basics, then move to advanced concepts**

Expected: The system breaks this into steps, provides information for each step, and synthesizes a complete learning pathway.

### Query 7
**Explain how data science differs from machine learning and their relationship**

Expected: The system handles multiple related questions and explains how they connect.

## Section 4: Memory and Context

After asking several questions, follow up with these to show the memory system working.

### Query 8 (Follow-up after Queries 1-3)
**Can you compare what we discussed about AI with what I asked about Python?**

Expected: The system retrieves its memory of previous questions and synthesizes a comparison.

### Query 9 (Follow-up after Query 4)
**You compared Python and Java earlier. Which one is better for beginners?**

Expected: The system recalls the earlier comparison from memory and provides follow-up analysis.

## Section 5: Domain-Specific Queries

These show the breadth of knowledge across different domains.

### Query 10
**Tell me about Plato**

Expected: The system returns information from its philosophy/history knowledge base.

### Query 11
**What is calculus?**

Expected: The system provides mathematical knowledge from its mathematics domain.

### Query 12
**What is renewable energy?**

Expected: The system returns general knowledge information.

## Section 6: Complex Reasoning

These queries require coordination between multiple agents.

### Query 13
**Compare classical and modern philosophy in terms of their approach to knowledge**

Expected: The system analyzes two philosophical approaches and compares them across multiple dimensions.

### Query 14
**What are the key differences between Python, Java, and C++ for beginners?**

Expected: The system performs multi-item comparison across three programming languages.

## Section 7: Edge Cases and Broader Topics

### Query 15
**Tell me everything you know about computers**

Expected: The system provides a broad overview from multiple areas of its knowledge base.

### Query 16
**How does machine learning relate to philosophy?**

Expected: The system tries to find connections between concepts across different domains.

## Video Demonstration Flow

**Part 1: Introduction (2-3 minutes)**
- Show the interface
- Explain what multi-agent systems are
- Use Query 1, 2, 3 to show basic functionality

**Part 2: Agent Specialization (3-4 minutes)**
- Use Query 4, 5 to show the analysis agent comparing items
- Explain how the coordinator routes queries

**Part 3: Memory System (2-3 minutes)**
- Ask Queries 1-3 in sequence
- Then ask Query 8 to show memory working
- Explain how the system remembers conversations

**Part 4: Complex Scenarios (3-4 minutes)**
- Use Query 13, 14 to show complex analysis
- Show how confidence scores work
- Explain the execution trace

**Part 5: Summary**
- Show the test results file
- Explain the architecture briefly
- Discuss real-world applications

## Tips for Video Recording

1. Start with fresh state (empty memory) for first demonstration
2. Speak out loud what you're typing so viewers understand
3. Point out the confidence scores in responses
4. Show the execution trace to demonstrate agent routing
5. For comparison queries, pause to let viewers read the analysis
6. Explain what each agent is doing as responses appear
7. Show memory growth as you ask more questions
8. Demonstrate how follow-up questions reference earlier conversations

## Expected System Behavior

- Simple queries: 20-30% confidence (basic knowledge retrieval)
- Comparative queries: 50-70% confidence (more analysis involved)
- Memory-based queries: 60-90% confidence (exact matches from memory)
- Complex reasoning: 30-50% confidence (requires more inference)

The confidence scores reflect how directly the system can answer based on what's in its knowledge base or memory.
