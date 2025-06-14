# 🧬 LangGraph Medical Research Agent

**AI-powered medical research reports using LangGraph framework with DeepSeek R1**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![LangGraph](https://img.shields.io/badge/Framework-LangGraph-green.svg)](https://langchain-ai.github.io/langgraph/)

Generate comprehensive medical research reports with professional formatting, authoritative sources, and AI-powered analysis.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Ollama with DeepSeek R1 8B model
- NVIDIA GPU (recommended for acceleration)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/langgraph-medical-research-agent.git
cd langgraph-medical-research-agent
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Setup Ollama and DeepSeek R1**
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Start Ollama server
ollama serve

# Pull DeepSeek R1 model (in another terminal)
ollama pull deepseek-r1:8b
```

4. **Setup LangGraph Deep Researcher**
```bash
git clone https://github.com/langchain-ai/local-deep-researcher.git
```

### Usage

#### Method 1: Easy Runner (Recommended)
```bash
# Edit run_research.py and change the topic
python run_research.py
```

#### Method 2: Command Line
```bash
python research_agent.py "aspirin cardiovascular benefits"
python research_agent.py "CAR-T cell therapy advances 2024"
python research_agent.py "latest breast cancer treatments"
```

#### Method 3: Interactive Mode
```bash
python research_agent.py --interactive
```

#### Method 4: Docker
```bash
docker build -t medical-research-agent .
docker run -it medical-research-agent "your research topic"
```

## 📋 Example Topics

- `"aspirin cardiovascular benefits"`
- `"CAR-T cell therapy advances 2024"`
- `"latest breast cancer treatments"`
- `"immunotherapy combinations cancer"`
- `"precision medicine oncology 2024"`
- `"liquid biopsy cancer detection"`
- `"checkpoint inhibitors resistance mechanisms"`

## 📄 Output Format

The agent generates professional medical research reports with:

- 📋 **Executive Summary**
- 🚀 **Key Developments and Recent Advances**
- 📊 **Clinical Data and Trial Results** 
- ⚙️ **Treatment Mechanisms and Approaches**
- 👥 **Patient Eligibility and Selection Criteria**
- 🔮 **Future Implications and Recommendations**
- 📚 **Sources and References** (authoritative medical journals)
- 🔬 **Research Methodology**
- ⚕️ **Medical Disclaimer**

## 🏗️ Architecture

- **Framework**: LangGraph Deep Researcher
- **AI Model**: DeepSeek R1 8B (GPU-accelerated)
- **Search Engine**: DuckDuckGo with multiple research loops
- **Output**: Professional markdown reports with citations
- **Processing Time**: 2-3 minutes per comprehensive analysis

## 📁 Project Structure

```
langgraph-medical-research-agent/
├── research_agent.py          # Main research agent
├── run_research.py           # Easy runner script
├── requirements.txt          # Python dependencies
├── Dockerfile               # Docker containerization
├── docker-compose.yml       # Docker Compose setup
├── .gitignore              # Git ignore file
├── setup.py                # Package setup
├── LICENSE                 # MIT license
├── README.md               # This file
└── examples/               # Example outputs
    ├── aspirin_research.md
    └── immunotherapy_research.md
```

## 🛠️ Development

### Local Development
```bash
# Clone and setup
git clone https://github.com/yourusername/langgraph-medical-research-agent.git
cd langgraph-medical-research-agent
pip install -e .

# Run tests
python -m pytest tests/

# Format code
black .
```

### Environment Variables
```bash
export OLLAMA_BASE_URL="http://localhost:11434"
export LOCAL_LLM="deepseek-r1:8b"
export SEARCH_API="duckduckgo"
```

## 🐳 Docker Usage

### Build and Run
```bash
docker build -t medical-research-agent .
docker run -it medical-research-agent "cancer immunotherapy 2024"
```

### Docker Compose
```bash
docker-compose up
```

## 📊 Features

- ✅ **Professional Medical Reports** with structured sections
- ✅ **GPU Acceleration** with NVIDIA support
- ✅ **Authoritative Sources** from medical journals (PubMed, NEJM, etc.)
- ✅ **Real-time Web Search** with DuckDuckGo integration
- ✅ **Thinking Tag Removal** for clean output
- ✅ **Multiple Usage Methods** (CLI, interactive, Docker)
- ✅ **Comprehensive Citations** with URL references
- ✅ **Medical Disclaimer** for ethical compliance
- ✅ **Error Handling** with fallback mechanisms

## 🔧 Configuration

Edit `config.yml` to customize:

```yaml
model:
  provider: "ollama"
  name: "deepseek-r1:8b"
  base_url: "http://localhost:11434"

search:
  api: "duckduckgo"
  max_results: 10
  research_loops: 2

output:
  format: "markdown"
  include_sources: true
  strip_thinking_tokens: true
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Medical Disclaimer

This tool is for informational and research purposes only. It should not replace professional medical advice, diagnosis, or treatment. Always consult qualified healthcare professionals for medical decisions.

## 🙏 Acknowledgments

- [LangGraph](https://langchain-ai.github.io/langgraph/) for the research framework
- [DeepSeek](https://deepseek.com/) for the R1 reasoning model
- [Ollama](https://ollama.ai/) for local LLM serving
- Medical research community for open access publications

## 📞 Support

- 📖 [Documentation](https://github.com/yourusername/langgraph-medical-research-agent/wiki)
- 🐛 [Issues](https://github.com/yourusername/langgraph-medical-research-agent/issues)
- 💬 [Discussions](https://github.com/yourusername/langgraph-medical-research-agent/discussions)

---

⭐ **Star this repository if you find it useful!**