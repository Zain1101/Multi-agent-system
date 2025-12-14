class ResearchAgent:
    def __init__(self):
        self.knowledge_base = self._initialize_knowledge_base()
        self.research_count = 0
    def _initialize_knowledge_base(self):
        return {
            "optimization techniques": {
                "items": [
                    {"name": "Gradient Descent", "type": "iterative", "complexity": "O(n)", "use_case": "Basic optimization"},
                    {"name": "Adam", "type": "adaptive", "complexity": "O(n)", "use_case": "Deep learning, fast convergence"},
                    {"name": "RMSProp", "type": "adaptive", "complexity": "O(n)", "use_case": "RNNs, non-stationary problems"},
                    {"name": "Adagrad", "type": "adaptive", "complexity": "O(n)", "use_case": "Sparse data, decreasing learning rate"},
                    {"name": "Nadam", "type": "hybrid", "complexity": "O(n)", "use_case": "Adam with Nesterov momentum"}
                ],
                "description": "Methods for minimizing loss functions in machine learning"
            },
            "neural networks": {
                "items": [
                    {"name": "CNN", "architecture": "Convolutional", "best_for": "Image processing", "strength": "Local feature extraction"},
                    {"name": "RNN", "architecture": "Recurrent", "best_for": "Sequences", "strength": "Temporal dependencies"},
                    {"name": "LSTM", "architecture": "Recurrent", "best_for": "Long sequences", "strength": "Vanishing gradient solution"},
                    {"name": "GRU", "architecture": "Recurrent", "best_for": "Long sequences", "strength": "Simplified LSTM"},
                    {"name": "Transformer", "architecture": "Attention-based", "best_for": "NLP, sequences", "strength": "Parallelizable, self-attention"},
                    {"name": "DNN", "architecture": "Fully-connected", "best_for": "General tasks", "strength": "Versatile"}
                ],
                "description": "Different neural network architectures for various tasks"
            },
            "reinforcement learning": {
                "items": [
                    {"name": "Q-Learning", "type": "Value-based", "model_free": True, "exploration": "epsilon-greedy"},
                    {"name": "Policy Gradient", "type": "Policy-based", "model_free": True, "gradient_based": True},
                    {"name": "Actor-Critic", "type": "Hybrid", "components": ["Actor", "Critic"], "advantage": "Reduced variance"},
                    {"name": "DQN", "type": "Deep Q-Learning", "innovation": "Deep neural networks", "stability": "Experience replay"},
                    {"name": "PPO", "type": "Policy-based", "algorithm": "Trust region", "stability": "Clipped objective"}
                ],
                "description": "Methods for learning through interaction with environment"
            },
            "machine learning models": {
                "items": [
                    {"name": "Linear Regression", "type": "regression", "complexity": "Low", "interpretability": "High"},
                    {"name": "Logistic Regression", "type": "classification", "probabilistic": True, "use_case": "Binary/multiclass"},
                    {"name": "SVM", "type": "classification", "kernel_trick": True, "high_dimensions": True},
                    {"name": "Decision Trees", "type": "tree-based", "interpretability": "High", "risk": "Overfitting"},
                    {"name": "Random Forest", "type": "ensemble", "robustness": "High", "parallel_friendly": True},
                    {"name": "K-Means", "type": "clustering", "unsupervised": True, "complexity": "O(nkt)"}
                ],
                "description": "Fundamental machine learning algorithms and models"
            },
            "transformers": {
                "items": [
                    {"name": "BERT", "task": "Encoder", "training": "Masked Language Model", "applications": ["Classification", "NER", "QA"]},
                    {"name": "GPT", "task": "Decoder", "training": "Causal Language Model", "applications": ["Text generation", "Summarization"]},
                    {"name": "T5", "task": "Encoder-Decoder", "training": "Text-to-Text", "applications": ["All NLP tasks"]},
                    {"name": "RoBERTa", "task": "Encoder", "improvement_over": "BERT", "training": "Optimized MLM"},
                    {"name": "ELECTRA", "task": "Encoder", "training": "Discriminative", "efficiency": "Pre-training efficient"}
                ],
                "description": "State-of-the-art transformer models for NLP"
            }
        }

    def research(self, topic: str) -> dict:
        self.research_count += 1
        topic_lower = topic.lower()
        result_items = []
        matched_topic = None
        keyword_to_category = {
            "adam": "optimization techniques",
            "sgd": "optimization techniques",
            "gradient": "optimization techniques",
            "descent": "optimization techniques",
            "optimizer": "optimization techniques",
            "optimization": "optimization techniques",  
            "rmsprop": "optimization techniques",
            "adagrad": "optimization techniques",
            "nadam": "optimization techniques",
            "neural": "neural networks",
            "network": "neural networks",
            "cnn": "neural networks",
            "rnn": "neural networks",
            "lstm": "neural networks",
            "gru": "neural networks",
            "transformer": "neural networks",
            "dnn": "neural networks",
            "convolutional": "neural networks",
            "recurrent": "neural networks",
            "reinforcement": "reinforcement learning",
            "q-learning": "reinforcement learning",
            "policy": "reinforcement learning",
            "actor": "reinforcement learning",
            "critic": "reinforcement learning",
            "dqn": "reinforcement learning",
            "ppo": "reinforcement learning",
            "regression": "machine learning models",
            "classification": "machine learning models",
            "svm": "machine learning models",
            "decision": "machine learning models",
            "tree": "machine learning models",
            "forest": "machine learning models",
            "k-means": "machine learning models",
            "clustering": "machine learning models",
            "bert": "transformers",
            "gpt": "transformers",
            "t5": "transformers",
            "roberta": "transformers",
            "electra": "transformers",
            "attention": "transformers",
            "deep": "neural networks",
            "learning": "reinforcement learning"
        }
        
        #try exact category matching
        for key, content in self.knowledge_base.items():
            if key in topic_lower:
                result_items = content["items"]
                matched_topic = key
                return {
                    "result": result_items,
                    "topic": topic,
                    "matched_category": matched_topic,
                    "research_id": self.research_count,
                    "completeness": "high",
                    "items_found": len(result_items)
                }
        #try keyword-based matching for more specific queries
        best_match_score = 0
        best_match_category = None
        specific_item = None
        
        for keyword, category in keyword_to_category.items():
            if keyword in topic_lower:
                score = len(keyword)  #Longer keywords= more specific
                if score > best_match_score:
                    best_match_score = score
                    best_match_category = category
                    specific_item = keyword
        
        # If found a matching category via keywords
        if best_match_category and best_match_category in self.knowledge_base:
            content = self.knowledge_base[best_match_category]
            all_items = content["items"]
            
            # filter to a specific item
            if specific_item and best_match_score >= 3: 
                filtered = [item for item in all_items 
                           if isinstance(item, dict) and specific_item.lower() in item.get("name", "").lower()]
                if filtered:
                    result_items = filtered
                else:
                    result_items = all_items 
            else:
                result_items = all_items
            
            matched_topic = best_match_category
            return {
                "result": result_items,
                "topic": topic,
                "matched_category": matched_topic,
                "research_id": self.research_count,
                "completeness": "high",
                "items_found": len(result_items),
                "query_type": "specific" if len(result_items) < 6 else "category"
            }
        return {
            "result": ["No specific match found. Try queries like: 'What is CNN?', 'Compare Adam and SGD', 'Explain Transformers', 'What is LSTM?'"],
            "topic": topic,
            "matched_category": None,
            "research_id": self.research_count,
            "completeness": "low",
            "items_found": 0,
            "query_type": "none"
        }
