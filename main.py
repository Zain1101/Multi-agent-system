from agents.coordinator import Coordinator
import sys
import io
import json

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    coordinator = Coordinator()
    queries = [
    "Research optimization techniques and analyze which is better",
    "Research neural networks and summarize",
    "What did we learn about optimization techniques earlier?"
]

    for q in queries:
        print(f"\nQuery: {q}")
        result = coordinator.handle_query(q)

        response = result["response"]
        print(f"Source: {result['source']}")
        print(f"Confidence: {result['confidence']:.0%}")
        
        if 'research' in response:
            research = response['research']
            print(f"\nResearch - Topic: {research['topic']}, Items: {research['items_found']}")
            for item in research['result'][:3]:
                if isinstance(item, dict):
                    print(f"  - {item.get('name', 'Unknown')}")
                else:
                    print(f"  - {item}")  
        if 'analysis' in response:
            analysis = response['analysis']
            print(f"\nAnalysis - Status: {analysis['status']}, Confidence: {analysis['confidence']:.0%}")
            summary = analysis['summary'].replace('█', '=').replace('░', '-')[:200]
            print(f"  {summary}...")

if __name__ == "__main__":
    main()
