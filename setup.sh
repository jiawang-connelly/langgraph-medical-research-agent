#!/bin/bash

echo "🧬 Setting up LangGraph Medical Research Agent"
echo "=============================================="

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

echo "✅ Python 3 found"

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Python dependencies installed"
else
    echo "❌ Failed to install Python dependencies"
    exit 1
fi

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo "🔄 Installing Ollama..."
    curl -fsSL https://ollama.ai/install.sh | sh
    if [ $? -eq 0 ]; then
        echo "✅ Ollama installed"
    else
        echo "❌ Failed to install Ollama"
        exit 1
    fi
else
    echo "✅ Ollama already installed"
fi

# Start Ollama server
echo "🚀 Starting Ollama server..."
ollama serve &
OLLAMA_PID=$!
sleep 5

# Pull DeepSeek R1 model
echo "📥 Downloading DeepSeek R1 8B model (this may take a few minutes)..."
ollama pull deepseek-r1:8b

if [ $? -eq 0 ]; then
    echo "✅ DeepSeek R1 8B model downloaded"
else
    echo "❌ Failed to download DeepSeek R1 model"
    kill $OLLAMA_PID 2>/dev/null
    exit 1
fi

# Clone LangGraph Deep Researcher
if [ ! -d "local-deep-researcher" ]; then
    echo "📂 Cloning LangGraph Deep Researcher..."
    git clone https://github.com/langchain-ai/local-deep-researcher.git
    if [ $? -eq 0 ]; then
        echo "✅ LangGraph Deep Researcher cloned"
    else
        echo "❌ Failed to clone LangGraph Deep Researcher"
        kill $OLLAMA_PID 2>/dev/null
        exit 1
    fi
else
    echo "✅ LangGraph Deep Researcher already exists"
fi

# Create reports directory
mkdir -p reports

echo ""
echo "🎉 Setup complete!"
echo "✅ All dependencies installed"
echo "✅ Ollama server running (PID: $OLLAMA_PID)"
echo "✅ DeepSeek R1 8B model ready"
echo "✅ LangGraph Deep Researcher configured"
echo ""
echo "🚀 Ready to use! Try:"
echo "   python research_agent.py \"aspirin cardiovascular benefits\""
echo "   python run_research.py"
echo ""
echo "⚠️  Keep this terminal open to maintain Ollama server"