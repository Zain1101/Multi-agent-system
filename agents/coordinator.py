from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.memory_agent import MemoryAgent
import re
from typing import Dict, List, Tuple

class Coordinator:
    def __init__(self):
        self.research_agent = ResearchAgent()
        self.analysis_agent = AnalysisAgent()
        self.memory_agent = MemoryAgent()
        self.query_history = []
        
        # Extended stop words and domain keywords
        self.stop_words = set([
            "research", "analyze", "compare", "find", "what", "did", "we", "about",
            "earlier", "summarize", "is", "the", "a", "an", "and", "or", "but",
            "in", "on", "at", "to", "for", "of", "with", "by", "from"
        ])
        
        self.analysis_keywords = {
            "compare": 0.9, "difference": 0.9, "vs": 0.9, "versus": 0.9,
            "better": 0.8, "worse": 0.8, "effectiveness": 0.85, "efficiency": 0.85,
            "pros": 0.8, "cons": 0.8, "advantages": 0.9, "disadvantages": 0.9,
            "summarize": 0.7, "summary": 0.7, "overview": 0.75
        }
        
        self.research_keywords = {
            "research": 0.8, "find": 0.7, "learn": 0.6, "about": 0.5,
            "what": 0.4, "how": 0.6, "explain": 0.7, "describe": 0.6,
            "tell": 0.5, "information": 0.8,
            # Add specific technical terms
            "adam": 0.9, "sgd": 0.9, "optimizer": 0.9,
            "neural": 0.8, "network": 0.7, "cnn": 0.9, "rnn": 0.9, "lstm": 0.9,
            "transformer": 0.9, "bert": 0.9, "gpt": 0.9,
            "reinforcement": 0.8, "q-learning": 0.9,
            "optimization": 0.9, "algorithm": 0.7
        }

    def handle_query(self, query: str) -> Dict:
        """Advanced query handling with confidence scoring and multi-step reasoning"""
        self.query_history.append(query)
        
        # Check if query references earlier conversation
        context_keywords = ["earlier", "before", "previously", "we", "we discussed", "we talked", "what did", "remember", "previous"]
        uses_context = any(keyword in query.lower() for keyword in context_keywords)
        
        # If asking about previous context, synthesize from memory
        if uses_context and len(self.query_history) > 1:
            # Return summary of previous queries
            previous_results = []
            for prev_query in self.query_history[:-1]:  # Exclude current query
                prev_result = self.memory_agent.retrieve(prev_query)
                if prev_result:
                    previous_results.append(prev_result)
            
            if previous_results:
                return {
                    "from_memory": True,
                    "response": {
                        "context": "Based on our earlier conversations",
                        "previous_topics": self.query_history[:-1],
                        "summary": previous_results
                    },
                    "confidence": 0.75,
                    "source": "context"
                }
        
        # Step 1: Check memory first with relevance scoring
        memory_response, confidence = self._retrieve_from_memory_advanced(query)
        # Only use memory if confidence is very high (0.85+)
        if memory_response and confidence > 0.85:
            return {
                "from_memory": True,
                "response": memory_response,
                "confidence": confidence,
                "source": "memory"
            }

        # Step 2: Intelligent task planning
        steps, step_confidence = self.plan_tasks_advanced(query)
        if not steps:
            steps = ["research"]  # Default to research
        
        final_result = {}
        last_output = None
        execution_trace = []

        # Step 3: Execute planned steps with context
        for step in steps:
            if step == "research":
                topic = self._extract_topic_advanced(query, last_output)
                research_result = self.research_agent.research(topic)
                final_result["research"] = research_result
                last_output = research_result.get("result", [])
                execution_trace.append(f"Research on '{topic}' completed")

            elif step == "analysis":
                analysis_result = self.analysis_agent.analyze(last_output)
                final_result["analysis"] = analysis_result
                execution_trace.append("Analysis completed")

        # Step 4: Store in memory with rich metadata
        self.memory_agent.store(query, final_result)
        
        return {
            "from_memory": False,
            "response": final_result,
            "confidence": step_confidence,
            "execution_trace": execution_trace,
            "source": "execution"
        }

    def plan_tasks_advanced(self, query: str) -> Tuple[List[str], float]:
        """Advanced task planning with confidence scoring"""
        steps = []
        scores = {"research": 0.0, "analysis": 0.0}
        q = query.lower()
        
        # Score research relevance
        for keyword, score in self.research_keywords.items():
            if keyword in q:
                scores["research"] += score
        
        # Score analysis relevance
        for keyword, score in self.analysis_keywords.items():
            if keyword in q:
                scores["analysis"] += score
        
        # Normalize scores
        max_score = max(scores.values()) if scores.values() else 1
        confidence = (max_score / 10.0) if max_score > 0 else 0.5
        
        # For comparison queries, always do research first, then analysis
        if scores["analysis"] > 0.5:  # Comparison query detected
            steps.append("research")
            steps.append("analysis")
        # Otherwise add research if any relevance detected
        elif scores["research"] > 0.1:
            steps.append("research")
        else:
            # Default to research
            steps.append("research")
            confidence = 0.4
        
        return steps, min(confidence, 1.0)

    def _retrieve_from_memory_advanced(self, query: str) -> Tuple[Dict, float]:
        """Advanced memory retrieval with confidence scoring"""
        memory_response = self.memory_agent.retrieve(query)
        if memory_response:
            # Calculate similarity confidence
            confidence = 0.85  # High confidence for memory hits
            return memory_response, confidence
        return None, 0.0

    def _extract_topic_advanced(self, query: str, last_output=None) -> str:
        """Advanced topic extraction with better NLP and semantic understanding"""
        if last_output:
            return last_output[0] if last_output else "general"
        
        # Remove common punctuation and extra whitespace
        cleaned = re.sub(r'[?!.,;:\'"()]', '', query.lower())
        words = cleaned.split()
        
        # Keywords to prefer as topics
        technical_terms = [
            "adam", "sgd", "gradient", "optimizer", "cnn", "rnn", "lstm", "transformer",
            "neural", "network", "reinforcement", "learning", "deep", "bert", "gpt",
            "classification", "regression", "clustering", "optimization", "algorithm"
        ]
        
        # First check for technical terms
        for word in words:
            if word in technical_terms:
                return word
        
        # Then filter common stop words
        topic_words = [w for w in words if w not in self.stop_words and len(w) > 2]
        
        if topic_words:
            # Return the longest meaningful word
            return max(topic_words, key=len)
        
        return "general"
