#!/usr/bin/env python3

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="langgraph-medical-research-agent",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="AI-powered medical research reports using LangGraph framework with DeepSeek R1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/langgraph-medical-research-agent",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "gpu": ["torch>=2.0.0", "nvidia-ml-py3>=7.352.0"],
        "dev": ["pytest>=7.0", "black>=22.0", "flake8>=4.0", "mypy>=1.0"],
    },
    entry_points={
        "console_scripts": [
            "medical-research=research_agent:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="medical research ai langraph deepseek ollama healthcare",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/langgraph-medical-research-agent/issues",
        "Source": "https://github.com/yourusername/langgraph-medical-research-agent",
        "Documentation": "https://github.com/yourusername/langgraph-medical-research-agent/wiki",
    },
)