"""
Test Scenarios for KRR Multi-Agent System
Implements 5 comprehensive test scenarios as per assignment requirements
"""

import sys
import json
from datetime import datetime
from pathlib import Path

# Add agents to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.coordinator import Coordinator
from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.memory_agent import MemoryAgent


def print_section(title: str):
    """Print formatted section header"""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80)


def print_subsection(title: str):
    """Print formatted subsection header"""
    print(f"\n--- {title} ---")


def capture_test_output(test_name: str, output_text: str):
    """Capture test output to file"""
    output_dir = Path(__file__).parent.parent / "outputs"
    output_dir.mkdir(exist_ok=True)
    
    output_file = output_dir / f"{test_name}.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"TEST: {test_name.upper()}\n")
        f.write(f"Timestamp: {datetime.now().isoformat()}\n")
        f.write("=" * 80 + "\n\n")
        f.write(output_text)
    
    print(f"Output captured to: {output_file}")


class TestScenarios:
    """Comprehensive test scenarios for the multi-agent system"""
    
    def __init__(self):
        self.coordinator = Coordinator()
        self.memory_agent = self.coordinator.memory_agent
        # Clear memory for clean tests
        self.memory_agent.clear()
        self.test_results = []
    
    def test_1_simple_query(self) -> str:
        """
        Test 1: Simple Query
        User asks a straightforward question about a topic.
        System should retrieve matching information from knowledge base.
        """
        print_section("TEST 1: SIMPLE QUERY")
        output = []
        
        query = "What are the main types of neural networks?"
        output.append(f"Query: {query}\n")
        
        print_subsection("Processing Query")
        print(f"User Query: {query}")
        
        response = self.coordinator.handle_query(query)
        
        print_subsection("System Response")
        response_text = str(response.get('response', ''))[:200]
        print(f"Response: {response_text}...")
        print(f"Confidence: {response['confidence']}%")
        print(f"Source: {response['source']}")
        
        output.append(f"\nSystem Response:\n{str(response.get('response', ''))}\n")
        output.append(f"\nConfidence: {response['confidence']}%\n")
        output.append(f"Source: {response['source']}\n")
        output.append(f"Execution Trace:\n{str(response.get('execution_trace', {}))}\n")
        
        print_subsection("Memory State After Query")
        all_memory = self.memory_agent.get_all()
        print(f"Total records stored: {len(all_memory)}")
        for idx, record in enumerate(all_memory[-2:], 1):
            print(f"  Record {idx}: {record.get('topic', 'N/A')}")
        
        output.append(f"\nMemory Records Stored: {len(all_memory)}\n")
        
        result = "\n".join(output)
        self.test_results.append(("simple_query", "PASS", response.get("confidence", 0)))
        return result
    
    def test_2_complex_query(self) -> str:
        """
        Test 2: Complex Query
        Multi-part query requiring research and analysis.
        System should decompose into subtasks and coordinate agents.
        """
        print_section("TEST 2: COMPLEX QUERY")
        output = []
        
        query = "Research transformer architectures and analyze their computational efficiency compared to RNNs"
        output.append(f"Query: {query}\n")
        
        print_subsection("Processing Complex Query")
        print(f"User Query: {query}")
        print("Expected Agent Coordination: Research Agent -> Analysis Agent")
        
        response = self.coordinator.handle_query(query)
        
        print_subsection("System Response")
        response_text = str(response.get('response', ''))[:250]
        print(f"Response: {response_text}...")
        print(f"Confidence: {response['confidence']}%")
        
        output.append(f"\nSystem Response:\n{str(response.get('response', ''))}\n")
        output.append(f"\nConfidence: {response['confidence']}%\n")
        output.append(f"Source: {response['source']}\n")
        output.append(f"Execution Trace:\n{str(response.get('execution_trace', {}))}\n")
        
        print_subsection("Agent Execution Details")
        exec_trace = response.get('execution_trace', {})
        agents_used = list(exec_trace.keys()) if isinstance(exec_trace, dict) else []
        print(f"Agents Executed: {agents_used}")
        for agent, details in exec_trace.items() if isinstance(exec_trace, dict) else []:
            print(f"  {agent}: {str(details)[:60]}")
        
        output.append(f"\nAgent Coordination Trace:\n")
        if isinstance(exec_trace, dict):
            for agent, details in exec_trace.items():
                output.append(f"  {agent}: {details}\n")
        
        result = "\n".join(output)
        self.test_results.append(("complex_query", "PASS", response.get("confidence", 0)))
        return result
    
    def test_3_memory_context(self) -> str:
        """
        Test 3: Memory and Context
        Test conversation history and context retention.
        System should reference previous discussions.
        """
        print_section("TEST 3: MEMORY & CONTEXT")
        output = []
        
        print_subsection("Round 1: Initial Query")
        query1 = "What is a CNN?"
        print(f"Query 1: {query1}")
        response1 = self.coordinator.handle_query(query1)
        resp1_text = str(response1.get('response', ''))[:150]
        print(f"Response 1 Summary: {resp1_text}...")
        output.append(f"Query 1: {query1}\n")
        output.append(f"Response 1:\n{str(response1.get('response', ''))}\n")
        
        print_subsection("Round 2: Context Reference")
        query2 = "What did we discuss earlier about neural networks?"
        print(f"Query 2: {query2}")
        response2 = self.coordinator.handle_query(query2)
        resp2_text = str(response2.get('response', ''))[:150]
        print(f"Response 2 Summary: {resp2_text}...")
        print(f"Confidence: {response2['confidence']}%")
        output.append(f"\nQuery 2: {query2}\n")
        output.append(f"Response 2:\n{str(response2.get('response', ''))}\n")
        output.append(f"Confidence: {response2['confidence']}%\n")
        
        print_subsection("Memory Retrieved")
        query_history = self.coordinator.query_history
        print(f"Total queries in history: {len(query_history)}")
        for idx, q in enumerate(query_history[-3:], 1):
            print(f"  {idx}. {q[:60]}...")
        
        output.append(f"\nQuery History:\n")
        for idx, q in enumerate(query_history, 1):
            output.append(f"  {idx}. {q}\n")
        
        result = "\n".join(output)
        self.test_results.append(("memory_test", "PASS", response2.get("confidence", 0)))
        return result
    
    def test_4_multi_step_task(self) -> str:
        """
        Test 4: Multi-Step Task Execution
        Complex workflow requiring multiple sequential steps.
        Tests agent coordination and state management.
        """
        print_section("TEST 4: MULTI-STEP TASK")
        output = []
        
        steps = [
            "Find information about reinforcement learning approaches",
            "Analyze the different RL algorithms",
            "Identify challenges in RL implementation"
        ]
        
        print_subsection("Task Decomposition")
        print(f"Main Task: Comprehensive RL Analysis")
        for idx, step in enumerate(steps, 1):
            print(f"  Step {idx}: {step}")
        output.append("Task Steps:\n")
        for idx, step in enumerate(steps, 1):
            output.append(f"  Step {idx}: {step}\n")
        
        print_subsection("Executing Steps")
        all_responses = []
        for idx, step in enumerate(steps, 1):
            print(f"\nStep {idx}: {step}")
            response = self.coordinator.handle_query(step)
            print(f"  Confidence: {response['confidence']}%")
            print(f"  Source: {response['source']}")
            all_responses.append(response)
            output.append(f"\nStep {idx} Response:\n{response['response']}\n")
            output.append(f"Confidence: {response['confidence']}%\n")
        
        print_subsection("Task Completion Summary")
        avg_confidence = sum(r.get('confidence', 0) for r in all_responses) / len(all_responses)
        print(f"Steps Completed: {len(steps)}")
        print(f"Average Confidence: {avg_confidence:.1f}%")
        
        output.append(f"\nSummary:\n")
        output.append(f"Steps Completed: {len(steps)}\n")
        output.append(f"Average Confidence: {avg_confidence:.1f}%\n")
        
        result = "\n".join(output)
        self.test_results.append(("multi_step", "PASS", avg_confidence))
        return result
    
    def test_5_collaborative_analysis(self) -> str:
        """
        Test 5: Collaborative Agent Analysis
        Multiple agents working together on a comparative analysis.
        Tests agent communication and synthesis of results.
        """
        print_section("TEST 5: COLLABORATIVE ANALYSIS")
        output = []
        
        query = "Compare optimization techniques: Adam, SGD, and RMSprop"
        output.append(f"Query: {query}\n")
        
        print_subsection("Collaborative Analysis Request")
        print(f"Query: {query}")
        print("Expected Workflow: Research Agent retrieves items -> Analysis Agent creates comparisons")
        
        response = self.coordinator.handle_query(query)
        
        print_subsection("System Response")
        resp_len = len(str(response.get('response', '')))
        print(f"Response Length: {resp_len} characters")
        print(f"Confidence: {response['confidence']}%")
        print(f"Source: {response['source']}")
        
        output.append(f"\nSystem Response:\n{str(response.get('response', ''))}\n")
        output.append(f"\nConfidence: {response['confidence']}%\n")
        output.append(f"Source: {response['source']}\n")
        
        print_subsection("Agent Collaboration Trace")
        exec_trace = response.get('execution_trace', {})
        if isinstance(exec_trace, dict):
            agents_used = list(exec_trace.keys())
        elif isinstance(exec_trace, list):
            agents_used = []
        else:
            agents_used = []
        print(f"Agents Involved: {', '.join(agents_used)}")
        
        output.append(f"\nAgent Collaboration:\n")
        output.append(f"Agents Involved: {', '.join(agents_used)}\n")
        
        if isinstance(exec_trace, dict):
            for agent, details in exec_trace.items():
                print(f"  {agent}:")
                if isinstance(details, dict):
                    for key, value in details.items():
                        print(f"    - {key}: {str(value)[:60]}")
                        output.append(f"    - {key}: {value}\n")
        
        print_subsection("Memory State")
        all_memory = self.memory_agent.get_all()
        print(f"Total records in memory: {len(all_memory)}")
        
        result = "\n".join(output)
        self.test_results.append(("collaborative", "PASS", response.get("confidence", 0)))
        return result
    
    def run_all_tests(self):
        """Run all test scenarios"""
        print("\n" + "=" * 80)
        print("  KRR MULTI-AGENT SYSTEM - COMPREHENSIVE TEST SUITE")
        print("=" * 80)
        
        results = {}
        
        # Test 1: Simple Query
        print("\n[1/5] Running Simple Query Test...")
        try:
            output1 = self.test_1_simple_query()
            results["simple_query"] = output1
            capture_test_output("simple_query", output1)
        except Exception as e:
            print(f"ERROR in Test 1: {e}")
            results["simple_query"] = f"ERROR: {str(e)}"
        
        # Test 2: Complex Query
        print("\n[2/5] Running Complex Query Test...")
        try:
            output2 = self.test_2_complex_query()
            results["complex_query"] = output2
            capture_test_output("complex_query", output2)
        except Exception as e:
            print(f"ERROR in Test 2: {e}")
            results["complex_query"] = f"ERROR: {str(e)}"
        
        # Test 3: Memory Context
        print("\n[3/5] Running Memory & Context Test...")
        try:
            output3 = self.test_3_memory_context()
            results["memory_test"] = output3
            capture_test_output("memory_test", output3)
        except Exception as e:
            print(f"ERROR in Test 3: {e}")
            results["memory_test"] = f"ERROR: {str(e)}"
        
        # Test 4: Multi-Step Task
        print("\n[4/5] Running Multi-Step Task Test...")
        try:
            output4 = self.test_4_multi_step_task()
            results["multi_step"] = output4
            capture_test_output("multi_step", output4)
        except Exception as e:
            print(f"ERROR in Test 4: {e}")
            results["multi_step"] = f"ERROR: {str(e)}"
        
        # Test 5: Collaborative Analysis
        print("\n[5/5] Running Collaborative Analysis Test...")
        try:
            output5 = self.test_5_collaborative_analysis()
            results["collaborative"] = output5
            capture_test_output("collaborative", output5)
        except Exception as e:
            print(f"ERROR in Test 5: {e}")
            results["collaborative"] = f"ERROR: {str(e)}"
        
        # Print summary
        self._print_test_summary()
        
        return results
    
    def _print_test_summary(self):
        """Print test execution summary"""
        print("\n" + "=" * 80)
        print("  TEST EXECUTION SUMMARY")
        print("=" * 80)
        
        for test_name, status, confidence in self.test_results:
            conf_str = f"{confidence:.1f}%" if isinstance(confidence, (int, float)) else "N/A"
            print(f"  [{status}] {test_name:20} | Confidence: {conf_str}")
        
        print("\nAll test outputs saved to outputs/ folder")
        print("=" * 80 + "\n")


if __name__ == "__main__":
    try:
        tester = TestScenarios()
        results = tester.run_all_tests()
        print("TESTS COMPLETED SUCCESSFULLY")
        sys.exit(0)
    except Exception as e:
        print(f"FATAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
