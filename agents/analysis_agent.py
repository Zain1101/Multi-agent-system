class AnalysisAgent:
    def __init__(self):
        self.analysis_count = 0
        self.comparison_metrics = {
            "neural_networks": {
                "CNN": {"speed": 8, "accuracy": 9, "interpretability": 5, "complexity": 7, "use_cases": "Images, Vision"},
                "RNN": {"speed": 6, "accuracy": 7, "interpretability": 4, "complexity": 7, "use_cases": "Sequences, Time-series"},
                "LSTM": {"speed": 5, "accuracy": 9, "interpretability": 3, "complexity": 9, "use_cases": "Long sequences"},
                "GRU": {"speed": 6, "accuracy": 8, "interpretability": 4, "complexity": 7, "use_cases": "Sequences, faster"},
                "Transformer": {"speed": 9, "accuracy": 10, "interpretability": 6, "complexity": 9, "use_cases": "NLP, parallel processing"},
                "DNN": {"speed": 7, "accuracy": 7, "interpretability": 5, "complexity": 6, "use_cases": "General purpose"}
            },
            "optimization": {
                "Gradient Descent": {"convergence": 4, "speed": 3, "stability": 8, "memory": 9, "best_for": "Simple convex problems"},
                "Adam": {"convergence": 9, "speed": 8, "stability": 9, "memory": 6, "best_for": "Deep learning (industry standard)"},
                "RMSProp": {"convergence": 8, "speed": 7, "stability": 7, "memory": 7, "best_for": "RNNs, non-stationary"},
                "Adagrad": {"convergence": 7, "speed": 6, "stability": 6, "memory": 4, "best_for": "Sparse data"},
                "Nadam": {"convergence": 9, "speed": 8, "stability": 8, "memory": 6, "best_for": "Adam with momentum"}
            }
        }

    def analyze(self, data) -> dict:
        self.analysis_count += 1
        
        if not data:
            return {
                "status": "fail",
                "summary": "No data available for analysis. Try a comparison query like 'Compare Adam vs SGD'",
                "confidence": 0.3,
                "analysis_id": self.analysis_count
            }

        summary_lines = []
        comparison_data = {}

        # Detect and compare neural network types
        nn_types = ["CNN", "RNN", "LSTM", "GRU", "Transformer", "DNN"]
        matching_nn = [item for item in data if isinstance(item, dict) and item.get("name") in nn_types 
                       or isinstance(item, str) and item in nn_types]
        
        if matching_nn or any(nn in str(data) for nn in nn_types):
            summary_lines.append("[NEURAL NETWORK COMPARISON]\n")
            comparison_data = self._compare_neural_networks(data)
            summary_lines.append(self._format_comparison(comparison_data))

        # Detect and compare optimization techniques
        opt_types = ["Gradient Descent", "Adam", "RMSProp", "Adagrad", "Nadam"]
        matching_opt = [item for item in data if isinstance(item, dict) and item.get("name") in opt_types 
                        or isinstance(item, str) and item in opt_types]
        
        if matching_opt or any(opt in str(data) for opt in opt_types):
            summary_lines.append("[OPTIMIZATION TECHNIQUE COMPARISON]\n")
            comparison_data = self._compare_optimizers(data)
            summary_lines.append(self._format_comparison(comparison_data))

        # Generic summary if no specific matches
        if not summary_lines:
            summary_lines.append("[INFORMATION SUMMARY]\n")
            if isinstance(data, list) and len(data) > 0:
                summary_lines.append(f"Found {len(data)} items:\n")
                for item in data:
                    if isinstance(item, dict):
                        name = item.get("name", "Item")
                        summary_lines.append(f"\n{name}:")
                        for key, value in item.items():
                            if key != "name":
                                summary_lines.append(f"  - {key.replace('_', ' ').title()}: {value}")
                    else:
                        summary_lines.append(f"- {item}")

        summary = "\n".join(summary_lines)
        return {
            "status": "success",
            "summary": summary,
            "confidence": 0.92 if comparison_data else 0.70,
            "analysis_id": self.analysis_count,
            "items_analyzed": len(data) if isinstance(data, list) else 1,
            "analysis_type": "comparative" if comparison_data else "descriptive"
        }

    def _compare_neural_networks(self, data) -> dict:
        nn_to_compare = {}
        metrics = self.comparison_metrics["neural_networks"]
        
        for item in data:
            name = item.get("name") if isinstance(item, dict) else item
            if name in metrics:
                nn_to_compare[name] = metrics[name]
        
        return nn_to_compare if nn_to_compare else metrics

    def _compare_optimizers(self, data) -> dict:
        opt_to_compare = {}
        metrics = self.comparison_metrics["optimization"]
        
        for item in data:
            name = item.get("name") if isinstance(item, dict) else item
            if name in metrics:
                opt_to_compare[name] = metrics[name]
        
        return opt_to_compare if opt_to_compare else metrics

    def _format_comparison(self, comparison_data: dict) -> str:
        if not comparison_data:
            return ""
        lines = []
        for item_name, metrics in comparison_data.items():
            lines.append(f"\n**{item_name}**")
            if isinstance(metrics, dict):
                for metric, value in metrics.items():
                    if metric not in ["best_for", "use_cases"]:
                        if isinstance(value, (int, float)):
                            bar = "█" * value + "░" * (10 - value)
                            lines.append(f"  {metric.capitalize()}: {bar} ({value}/10)")
                    else:
                        lines.append(f"  {metric.capitalize()}: {value}")
        
        return "\n".join(lines)
