# 🏗️ Multi-Agent AI Property Inspection Report

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Groq](https://img.shields.io/badge/LLM-Groq-green.svg)](https://groq.com)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-red.svg)](https://streamlit.io)

> **Multi-Agent AI System for Automated Property Diagnostic Report Generation**

Transform property inspection and thermal imaging data into professional diagnostic reports in seconds using advanced AI and multi-agent architecture powered by Llama 3.3 70B.

[🚀 Quick Start](#-quick-start) • [� Documentation](#-documentation) • [🌐 Web Interface](#-web-interface) • [🏗️ Architecture](#-architecture) • [🤝 Contributing](#-contributing)

---

## 📋 Overview

An intelligent multi-agent AI system that automatically converts technical property inspection data into professional, client-ready DDR (Detailed Diagnostic Report) documents. Built with open-source LLMs and designed for accuracy, reliability, and transparency.

### ✨ Key Features

- 🤖 **Multi-Agent Architecture**: 5 specialized AI agents working in pipeline
- � **PDF Processing**: Automatic extraction from inspection and thermal reports
- 🔍 **Intelligent Merging**: Area-based correlation of multiple data sources
- ⚠️ **Conflict Detection**: Explicit handling of contradictions and missing data
- ✅ **Quality Validation**: Automated checks for accuracy and completeness
- 🌐 **Web Interface**: User-friendly browser-based interface with drag-and-drop
- 💰 **Cost-Effective**: Uses free Groq API (Llama 3.3 70B)
- 📊 **Audit Trail**: Complete intermediate data for transparency

### 🎯 Problem Solved

**Challenge**: Converting raw technical inspection data into structured, client-friendly reports is time-consuming and error-prone.

**Solution**: Automated multi-agent system that:
- Extracts data accurately from multiple sources
- Merges information intelligently
- Handles missing/conflicting data transparently
- Generates professional reports in seconds
- Validates output quality automatically

---

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have:
- **Python 3.8 or higher** ([Download here](https://www.python.org/downloads/))
- **Internet connection** (for API calls)
- **Free Groq API key** ([Get one here](https://console.groq.com))

### Installation

Follow these steps to set up the system:

#### Step 1: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/yourusername/multiagent-ai-property-inspection-report.git

# Navigate to project directory
cd multiagent-ai-property-inspection-report
```

#### Step 2: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
```

**Linux/Mac:**
```bash
python3 -m venv venv
```

#### Step 3: Activate Virtual Environment

**Windows (Command Prompt):**
```bash
venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
.\venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

You should see `(venv)` at the start of your command prompt.

#### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all required packages including:
- LangChain (agent framework)
- Groq API client
- PyMuPDF (PDF processing)
- Streamlit (web interface)
- Pydantic (data validation)

#### Step 5: Get Your Free API Key

1. Visit [Groq Console](https://console.groq.com)
2. Sign up for a free account (no credit card required)
3. Navigate to "API Keys" section
4. Click "Create API Key"
5. Copy your API key (starts with `gsk_`)

#### Step 6: Configure API Key

**Option A: Interactive Setup (Recommended)**
```bash
python setup_env.py
```
Paste your API key when prompted.

**Option B: Manual Setup**
```bash
# Windows
copy .env.example .env

# Linux/Mac
cp .env.example .env
```

Then edit `.env` file and add your key:
```
GROQ_API_KEY=gsk_your_actual_api_key_here
```

⚠️ **Important**: Never commit the `.env` file to Git! It's already in `.gitignore`.

#### Step 7: Verify Installation

```bash
python verify_setup.py
```

You should see all checks pass:
```
✅ Running in virtual environment
✅ All packages installed
✅ .env file exists
✅ GROQ_API_KEY is configured
✅ All input PDFs present
✅ Output directory exists
```

---

## 🎮 Usage

### Option 1: Web Interface (Recommended)

The easiest way to use the system is through the web interface:

**Windows:**
```bash
run_web_interface.bat
```

**Linux/Mac:**
```bash
chmod +x run_web_interface.sh
./run_web_interface.sh
```

Your browser will automatically open at `http://localhost:8501`

**Using the Web Interface:**
1. 📤 Upload your inspection report PDF
2. 📤 Upload your thermal imaging PDF
3. 🚀 Click "Generate DDR Report"
4. ⏳ Wait ~30 seconds for processing
5. � Download your generated report!

See [WEB_INTERFACE.md](WEB_INTERFACE.md) for detailed guide.

### Option 2: Command Line Interface

For advanced users or automation:

```bash
# Activate virtual environment (if not already)
# Windows: .\venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# Run with default sample files
python main.py

# View generated report
# Windows: type output\generated_ddr.md
# Linux/Mac: cat output/generated_ddr.md
```

**Process Custom Files:**
```python
from main import DDRGenerationSystem
import os

# Initialize system
api_key = os.getenv("GROQ_API_KEY")
system = DDRGenerationSystem(api_key)

# Process your files
result = system.process_reports(
    inspection_pdf="path/to/your/inspection.pdf",
    thermal_pdf="path/to/your/thermal.pdf",
    output_path="output/your_report.md"
)

print(f"Report generated: {result['report'][:100]}...")
```

---

## � System Architecture

### Multi-Agent Pipeline

```
Input PDFs → Agent 1&2 (Extract) → Agent 3 (Merge) → Agent 4 (Generate) → Agent 5 (Validate) → DDR Report
```

### Agent Responsibilities

| Agent | Role | Input | Output | Temperature |
|-------|------|-------|--------|-------------|
| **Agent 1** | Inspection Extraction | Sample Report.pdf | inspection_data.json | 0.1 (factual) |
| **Agent 2** | Thermal Extraction | Thermal Images.pdf | thermal_data.json | 0.1 (factual) |
| **Agent 3** | Merge & Validate | Both JSON files | merged_data.json | 0.1 (precise) |
| **Agent 4** | DDR Generation | Merged data | generated_ddr.md | 0.3 (balanced) |
| **Agent 5** | Quality Check | Generated report | quality_check.json | 0.1 (strict) |

### Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **LLM** | Llama 3.3 70B | AI reasoning and generation |
| **API** | Groq (FREE) | Fast LLM inference |
| **Framework** | LangChain | Agent orchestration |
| **PDF** | PyMuPDF | Text extraction |
| **Web UI** | Streamlit | Browser interface |
| **Validation** | Pydantic | Data models |
| **Language** | Python 3.8+ | Implementation |

See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed system design.

---

## 📁 Project Structure

```
multiagent-ai-property-inspection-report/
├── agents/                      # AI Agents
│   ├── extraction_agent.py     # Extract from PDFs
│   ├── validation_agent.py     # Merge & validate
│   ├── generation_agent.py     # Generate DDR
│   └── quality_agent.py        # Quality check
├── models/
│   └── schemas.py              # Data structures
├── utils/
│   └── pdf_parser.py           # PDF utilities
├── output/                     # Generated files
│   ├── generated_ddr.md        # ⭐ Final report
│   ├── inspection_data.json    # Extracted data
│   ├── thermal_data.json       # Extracted data
│   ├── merged_data.json        # Merged data
│   └── quality_check.json      # Validation
├── app.py                      # Web interface
├── main.py                     # CLI interface
├── requirements.txt            # Dependencies
├── .env.example               # Config template
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

---

## 📋 Output Format

The system generates a complete DDR with these sections:

1. **Property Issue Summary** - High-level overview of main problems
2. **Area-wise Observations** - Organized by location (bedroom, bathroom, etc.)
3. **Probable Root Cause** - Analysis of why issues occurred
4. **Severity Assessment** - Overall severity with evidence-based reasoning
5. **Recommended Actions** - Specific, actionable repair steps
6. **Additional Notes** - Important context and warnings
7. **Missing Information** - Explicit "Not Available" items

**Example Output:**
```markdown
# Detailed Diagnostic Report for Property XYZ

## Property Issue Summary
Multiple moisture intrusion points detected across the property...

## Area-wise Observations
### Master Bedroom
- Dampness at skirting level (Severity: Poor)
- Thermal signature confirms moisture (3°C below ambient)

### Common Bathroom
- Gaps in tile joints (Severity: Moderate)
- Plumbing issues detected

## Recommended Actions
1. Immediate: Seal cracks in external walls
2. Short-term: Repair tile joints in bathrooms
3. Long-term: Apply waterproof coating
```

---

## ✅ Evaluation Criteria Coverage

| Criteria | Implementation | Evidence |
|----------|---------------|----------|
| **Accuracy** | Source attribution, low temp (0.1) | inspection_data.json |
| **Logical Merging** | Area-based matching | merged_data.json |
| **Missing/Conflict** | Explicit tracking | conflicts & missing_info arrays |
| **Clarity** | Client-friendly prompts | Clarity score 8/10 |
| **System Thinking** | Multi-agent modular design | 5 separate agents |

---

## 💰 Cost & Performance

### Using Groq Free Tier
- **Cost per report**: $0 (FREE!)
- **Processing time**: ~30 seconds
- **Token usage**: ~13K tokens
- **Rate limit**: 30 requests/minute
- **Daily limit**: 14,400 requests/day

### Scalability
- Can process 1,800+ reports/hour (free tier)
- Upgrade to paid tier for higher limits
- Or switch to other LLM providers (GPT-4, Claude)

---

## 🔧 Configuration

### Environment Variables

Create `.env` file:
```bash
GROQ_API_KEY=gsk_your_api_key_here
```

### Model Selection

Change model in agent files (`agents/*.py`):
```python
def __init__(self, api_key: str, model: str = "llama-3.3-70b-versatile"):
    # Options: llama-3.3-70b-versatile, mixtral-8x7b-32768, etc.
```

### Temperature Settings

Adjust creativity/factuality:
```python
# In agents/extraction_agent.py
temperature=0.1  # Low = more factual (extraction)

# In agents/generation_agent.py
temperature=0.3  # Medium = balanced (generation)
```

---

## 🧪 Testing

### Verify Setup
```bash
python verify_setup.py
```

### Test with Sample Files
```bash
python main.py
```

### Check Output Quality
```bash
cat output/quality_check.json
```

---

## 📚 Documentation

- **[SETUP.md](SETUP.md)** - Detailed setup instructions with troubleshooting
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - System design and architecture details
- **[WEB_INTERFACE.md](WEB_INTERFACE.md)** - Web interface user guide
- **[MODEL_INFO.md](MODEL_INFO.md)** - LLM model specifications and usage
- **[QUICKSTART.md](QUICKSTART.md)** - Quick start guide
- **[GITHUB_CHECKLIST.md](GITHUB_CHECKLIST.md)** - Safe GitHub upload guide

---

## 🐛 Troubleshooting

### Common Issues

**"GROQ_API_KEY not found"**
```bash
# Run interactive setup
python setup_env.py
```

**"Module not found"**
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

**"Rate limit exceeded"**
```bash
# Wait 1 minute or upgrade to paid tier
```

**Virtual environment not activated**
```bash
# Windows: .\venv\Scripts\activate
# Linux/Mac: source venv/bin/activate
```

See [SETUP.md](SETUP.md) for comprehensive troubleshooting guide.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/multiagent-ai-property-inspection-report.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run tests
python verify_setup.py
python main.py
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Groq** for free LLM API access
- **Meta AI** for Llama 3.3 70B model
- **LangChain** for agent framework
- **Streamlit** for web interface framework
- **PyMuPDF** for PDF processing capabilities

---

## 📞 Support

For issues or questions:

1. Check [SETUP.md](SETUP.md) for setup help
2. Review [ARCHITECTURE.md](ARCHITECTURE.md) for system details
3. Run `python verify_setup.py` for diagnostics
4. Open an issue on GitHub

---

## 🎯 Project Status

- ✅ **Status**: Production Ready
- ✅ **Version**: 1.0.0
- ✅ **Last Updated**: February 2026
- ✅ **Tested**: Successfully processed sample reports
- ✅ **Quality**: 8/10 clarity score

---

## 🌟 Star History

If you find this project useful, please consider giving it a star ⭐

---

<div align="center">

**Built with ❤️ using AI and Open Source**

[Report Bug](https://github.com/yourusername/multiagent-ai-property-inspection-report/issues) • 
[Request Feature](https://github.com/yourusername/multiagent-ai-property-inspection-report/issues) • 
[Documentation](https://github.com/yourusername/multiagent-ai-property-inspection-report/wiki)

</div>
