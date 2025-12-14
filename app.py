import streamlit as st
from agents.coordinator import Coordinator
from datetime import datetime
import json

coordinator = Coordinator()

st.set_page_config(page_title="Multi-Agent Chatbot", layout="wide")
st.title("🧠 Multi-Agent Research & Analysis Assistant")

# Sidebar with system info
with st.sidebar:
    st.header("System Info")
    st.write(f"Query History: {len(coordinator.query_history)}")
    if st.checkbox("Show Advanced Metrics"):
        st.write(f"Research Count: {coordinator.research_agent.research_count}")
        st.write(f"Analysis Count: {coordinator.analysis_agent.analysis_count}")

if "log" not in st.session_state:
    st.session_state.log = []

# Query input
col1, col2 = st.columns([4, 1])
with col1:
    query = st.text_input("Enter your query:", placeholder="e.g., 'What is the difference between RNN and CNN?'")
with col2:
    submit = st.button("🔍 Search", use_container_width=True)

if submit and query:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.log.append({"timestamp": timestamp, "query": query, "response": "Processing..."})
    st.rerun()

# Display results
if st.session_state.log:
    for i, entry in enumerate(st.session_state.log):
        # Process response if still in processing state
        if entry.get("response") == "Processing...":
            res = coordinator.handle_query(entry['query'])
            entry["response"] = res
        
        with st.container():
            # Query header
            st.markdown(f"### 🔹 [{entry['timestamp']}] User Query")
            st.info(entry['query'])
            
            # Response handling
            response = entry["response"]
            
            # Show confidence and source
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Confidence", f"{response.get('confidence', 0):.1%}")
            with col2:
                st.metric("Source", response.get('source', 'Unknown').upper())
            with col3:
                if 'execution_trace' in response:
                    st.metric("Steps", len(response['execution_trace']))
            
            # Display execution trace
            if response.get("execution_trace"):
                with st.expander("📋 Execution Trace"):
                    for trace in response['execution_trace']:
                        st.write(f"✓ {trace}")
            
            # Display responses
            if response.get("from_memory"):
                st.success("✨ Result from Memory Cache")
                st.markdown(f"**Response:** {response['response']}")
            else:
                resp = response.get("response", {})
                
                # Research results
                if "research" in resp:
                    with st.expander("🔬 Research Results", expanded=True):
                        research = resp["research"]
                        st.write(f"**Topic:** {research.get('topic')}")
                        st.write(f"**Category:** {research.get('matched_category', 'General')}")
                        st.write(f"**Completeness:** {research.get('completeness', 'N/A').upper()}")
                        
                        if isinstance(research.get("result"), list):
                            st.write("**Findings:**")
                            for item in research["result"]:
                                if isinstance(item, dict):
                                    st.write(f"- **{item.get('name', 'Item')}**")
                                    for key, value in item.items():
                                        if key != "name":
                                            st.write(f"  - {key}: {value}")
                                else:
                                    st.write(f"- {item}")
                
                # Analysis results
                if "analysis" in resp:
                    with st.expander("📊 Analysis Results", expanded=True):
                        analysis = resp["analysis"]
                        if analysis.get("status") == "success":
                            st.success(f"Analysis Complete (ID: {analysis.get('analysis_id')})")
                            st.write(analysis["summary"])
                            st.write(f"**Confidence:** {analysis.get('confidence', 0):.1%}")
                            st.write(f"**Items Analyzed:** {analysis.get('items_analyzed', 0)}")
                        else:
                            st.warning(analysis.get("summary", "Analysis failed"))
            
            st.divider()

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🗑️ Clear History"):
        st.session_state.log = []
        coordinator.query_history = []
        st.rerun()
with col2:
    if st.button("📥 Export Results"):
        export_data = json.dumps(st.session_state.log, indent=2)
        st.download_button("Download JSON", export_data, "results.json", "application/json")
with col3:
    st.write(f"Total Queries: {len(st.session_state.log)}")
