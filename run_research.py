#!/usr/bin/env python3
"""
Easy Research Runner - Simple interface for LangGraph Research Agent

Just change the topic below and run this file!
"""

# 🔍 CHANGE YOUR RESEARCH TOPIC HERE:
RESEARCH_TOPIC = "stage 4 bone cancer latest treatment options"

# Import the research agent
from research_agent import langgraph_research_agent

def main():
    print("🚀 Starting Easy Research...")
    print(f"📋 Topic: {RESEARCH_TOPIC}")
    print("-" * 50)
    
    # Run the research
    report, filename = langgraph_research_agent(RESEARCH_TOPIC)
    
    if report and filename:
        print(f"\n🎉 Success! Your research report is ready:")
        print(f"📄 File: {filename}")
        print("\n💡 To research a different topic:")
        print("   1. Edit the RESEARCH_TOPIC variable at the top of this file")
        print("   2. Run this file again")
    else:
        print("\n❌ Research failed. Please check your setup.")

if __name__ == "__main__":
    main()