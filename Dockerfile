# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl -fsSL https://ollama.ai/install.sh | sh

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Clone LangGraph Deep Researcher
RUN git clone https://github.com/langchain-ai/local-deep-researcher.git

# Copy application code
COPY . .

# Set Python path for local-deep-researcher
ENV PYTHONPATH="/app/local-deep-researcher/src:$PYTHONPATH"

# Set environment variables
ENV OLLAMA_BASE_URL="http://localhost:11434"
ENV LOCAL_LLM="deepseek-r1:8b"
ENV SEARCH_API="duckduckgo"

# Expose Ollama port
EXPOSE 11434

# Create startup script
RUN echo '#!/bin/bash\n\
# Start Ollama server in background\n\
ollama serve &\n\
sleep 5\n\
# Pull DeepSeek R1 model if not exists\n\
ollama list | grep -q "deepseek-r1:8b" || ollama pull deepseek-r1:8b\n\
# Run the research agent\n\
python research_agent.py "$@"' > /app/start.sh

RUN chmod +x /app/start.sh

# Default command
ENTRYPOINT ["/app/start.sh"]
CMD ["--help"]