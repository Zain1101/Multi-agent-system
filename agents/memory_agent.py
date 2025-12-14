import json
import os
from datetime import datetime
from typing import Dict, List, Any, Optional
import numpy as np
from numpy.linalg import norm


def embed(text):
    vec = np.zeros(26)
    text = text.lower()
    for c in text:
        if 'a' <= c <= 'z':
            vec[ord(c)-ord('a')] += 1
    return vec

class MemoryAgent:
    """
    Manages structured memory with vector search capabilities.
    - Stores records with metadata (topic, keywords, timestamp, source, confidence)
    - Uses character-frequency embeddings and cosine similarity
    - Persistent JSON storage with threshold-based retrieval
    """
    
    def __init__(self, store_path: str = "memory/memory_store.json"):
        self.file = store_path
        if not os.path.exists("memory"):
            os.makedirs("memory")
        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump([], f)

    def _load(self) -> List[Dict[str, Any]]:
        with open(self.file, "r") as f:
            try:
                data = json.load(f)
            except:
                data = []
        return data

    def _save(self, data: List[Dict[str, Any]]):
        with open(self.file, "w") as f:
            json.dump(data, f, indent=2)

    def store(self, topic: str, record: Dict[str, Any]) -> str:
        # Store a memory record with embedding and metadata
        vec = embed(topic)
        memory = self._load()
        record_id = f"mem_{len(memory) + 1}"
        
        entry = {
            "id": record_id,
            "topic": topic,
            "vector": vec.tolist(),
            "record": record,
            "timestamp": datetime.now().isoformat(),
            "confidence": record.get("confidence", 0.8),
            "source_agent": record.get("source_agent", "unknown"),
            "keywords": record.get("keywords", [])
        }
        memory.append(entry)
        self._save(memory)
        return record_id

    def retrieve(self, topic: str, threshold: float = 0.85) -> Optional[Dict[str, Any]]:
        # Retrieve a memory record by topic using cosine similarity
        vec = embed(topic)
        memory = self._load()
        
        if not memory:
            return None
            
        best_score = 0
        best_match = None
        
        for entry in memory:
            mem_vec = np.array(entry["vector"])
            score = np.dot(vec, mem_vec) / (norm(vec) * norm(mem_vec) + 1e-6)
            if score > best_score:
                best_score = score
                best_match = entry["record"]
        if best_score >= threshold:
            return best_match
        return None
    
    def search_by_keywords(self, keywords: List[str]) -> List[Dict[str, Any]]:
        memory = self._load()
        results = []
        for entry in memory:
            entry_keywords = entry.get("keywords", [])
            if any(kw in entry_keywords for kw in keywords):
                results.append(entry["record"])
        return results
    
    def get_all(self) -> List[Dict[str, Any]]:
        memory = self._load()
        return [entry["record"] for entry in memory]
    
    def clear(self):
        self._save([])
