# 🛠️ Setup Instructions - DDR Generation System

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation Steps](#installation-steps)
3. [API Key Setup](#api-key-setup)
4. [Verification](#verification)
5. [First Run](#first-run)
6. [Troubleshooting](#troubleshooting)
7. [Configuration](#configuration)

---

## Prerequisites

### Required
- **Python 3.8 or higher** ([Download](https://www.python.org/downloads/))
- **Internet connection** (for API calls)
- **Free Groq API key** ([Get one here](https://console.groq.com))

### Check Python Version
```bash
python --version
# Should show Python 3.8.0 or higher
```

---

## Installation Steps

### Step 1: Clone/Download Repository

**Option A: Using Git**
```bash
git clone <repository-url>
cd New_Task
```

**Option B: Download ZIP**
1. Download the repository as ZIP
2. Extract to a folder
3. Open terminal/command prompt in that folder

### Step 2: Create Virtual Environment

**Why?** Isolates project dependencies from your system Python.

**Windows:**
```bash
python -m venv venv
```

**Linux/Mac:**
```bash
python3 -m venv venv
```

### Step 3: Activate Virtual Environment

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

**Quick Activation (Windows):**
```bash
activate.bat
```

**Verify Activation:**
You should see `(venv)` at the start of your command prompt.

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

**Expected output:**
- Installing pymupdf, pillow, langchain, langchain-groq, pydantic, python-dotenv
- Should complete without errors

**If installation fails:**
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Try again
pip install -r requirements.txt
```

---

## API Key Setup

### Why Do You Need This?

The system uses Groq's API to access the Llama 3.3 70B language model. The API key authenticates your requests.

### Getting Your Free API Key

#### Step 1: Visit Groq Console
Go to: **https://console.groq.com**

#### Step 2: Sign Up
- Click "Sign Up" or "Get Started"
- Use email or Google account
- **No credit card required!**

#### Step 3: Create API Key
1. After login, go to "API Keys" section
2. Click "Create API Key"
3. Give it a name (e.g., "DDR System")
4. Copy the key (starts with `gsk_`)
5. **Save it somewhere safe!** (You won't see it again)

### Adding API Key to Project

**Option A: Interactive Setup (Recommended)**
```bash
# Make sure virtual environment is activated
python setup_env.py
```
- Paste your API key when prompted
- Script will create `.env` file automatically

**Option B: Manual Setup**
```bash
# 1. Copy the example file
copy .env.example .env          # Windows
cp .env.example .env            # Linux/Mac

# 2. Edit .env file
# Open .env in any text editor and replace:
GROQ_API_KEY=your_groq_api_key_here
# With your actual key:
GROQ_API_KEY=gsk_your_actual_key_here
```

### ⚠️ IMPORTANT: Keep Your API Key Safe!

**DO:**
- ✅ Keep `.env` file in your project folder
- ✅ Add `.env` to `.gitignore` (already done)
- ✅ Never share your API key publicly

**DON'T:**
- ❌ Commit `.env` to GitHub
- ❌ Share your API key in screenshots
- ❌ Post your key in forums/chat
- ❌ Hard-code the key in Python files

**If you accidentally expose your key:**
1. Go to https://console.groq.com
2. Delete the exposed key
3. Create a new one

---

## Verification

### Verify Complete Setup

```bash
# Make sure virtual environment is activated
python verify_setup.py
```

**Expected output:**
```
============================================================
DDR GENERATION SYSTEM - SETUP VERIFICATION
============================================================

1. Checking virtual environment...
   ✅ Running in virtual environment

2. Checking required packages...
   ✅ All packages installed

3. Checking .env configuration...
   ✅ .env file exists
   ✅ GROQ_API_KEY is configured

4. Checking input PDF files...
   ✅ All input PDFs present

5. Checking output directory...
   ✅ Output directory exists

============================================================
✅ SETUP COMPLETE - Ready to run!
============================================================
```

**If any checks fail, see [Troubleshooting](#troubleshooting) section.**

---

## First Run

### Run the System

```bash
# Make sure virtual environment is activated
python main.py
```

### What Happens

```
🚀 Initializing Multi-Agent DDR Generation System...
✅ All agents initialized

============================================================
STEP 1: EXTRACTING DATA FROM PDFs
============================================================
📄 Reading Sample Report.pdf...
📄 Reading Thermal Images.pdf...

============================================================
STEP 2: AGENT 1 & 2 - STRUCTURED EXTRACTION
============================================================
🤖 Agent 1: Extracting inspection data...
🤖 Agent 2: Extracting thermal data...

============================================================
STEP 3: AGENT 3 - MERGE & VALIDATE
============================================================
🤖 Agent 3: Merging and validating data...

============================================================
STEP 4: AGENT 4 - GENERATE DDR REPORT
============================================================
🤖 Agent 4: Generating DDR report...

============================================================
STEP 5: AGENT 5 - QUALITY VALIDATION
============================================================
🤖 Agent 5: Performing quality check...

============================================================
✨ PROCESS COMPLETE!
============================================================
```

### Check Output

**Windows:**
```bash
type output\generated_ddr.md
```

**Linux/Mac:**
```bash
cat output/generated_ddr.md
```

**Or open in text editor:**
- Navigate to `output/` folder
- Open `generated_ddr.md`

---

## Troubleshooting

### Issue: "python: command not found"

**Solution:**
```bash
# Try python3 instead
python3 --version
python3 -m venv venv
```

### Issue: "GROQ_API_KEY not found"

**Symptoms:**
```
❌ ERROR: GROQ_API_KEY not found!
```

**Solutions:**
1. Check `.env` file exists in project root
2. Open `.env` and verify key is present
3. Make sure no quotes around the key
4. Run `python setup_env.py` to recreate

**Correct format:**
```
GROQ_API_KEY=gsk_abc123xyz
```

**Incorrect formats:**
```
GROQ_API_KEY="gsk_abc123xyz"  ❌ (no quotes)
GROQ_API_KEY = gsk_abc123xyz  ❌ (no spaces)
```

### Issue: "Virtual environment not activated"

**Symptoms:**
- No `(venv)` in command prompt
- Packages not found

**Solution:**
```bash
# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# Verify - should see (venv) in prompt
```

### Issue: "Module not found" errors

**Solution:**
```bash
# Make sure venv is activated first!
pip install -r requirements.txt

# If still fails, upgrade pip
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Issue: "Rate limit exceeded"

**Symptoms:**
```
groq.RateLimitError: Rate limit exceeded
```

**Solution:**
- Groq free tier: 30 requests/minute
- Wait 1 minute and try again
- Or upgrade to paid tier at console.groq.com

### Issue: "Model decommissioned" error

**Solution:**
The code already uses `llama-3.3-70b-versatile` (current model).
If you see this error, the model name may have changed.

Check available models at: https://console.groq.com/docs/models

Update in agent files:
```python
# In agents/*.py
model: str = "llama-3.3-70b-versatile"  # Update this
```

### Issue: PDF files not found

**Symptoms:**
```
FileNotFoundError: Sample Report.pdf
```

**Solution:**
1. Make sure PDF files are in project root folder
2. Check file names match exactly:
   - `Sample Report.pdf`
   - `Thermal Images.pdf`

### Issue: Permission denied on Windows

**Solution:**
```bash
# Run PowerShell as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate venv
.\venv\Scripts\activate
```

---

## Configuration

### Change LLM Model

Edit agent files (`agents/*.py`):
```python
def __init__(self, api_key: str, model: str = "llama-3.3-70b-versatile"):
    # Available models:
    # - llama-3.3-70b-versatile (recommended)
    # - mixtral-8x7b-32768
    # - gemma2-9b-it
```

### Change Temperature (Creativity)

```python
# In agents/extraction_agent.py
temperature=0.1  # Low = more factual (extraction)

# In agents/generation_agent.py
temperature=0.3  # Medium = balanced (generation)
```

### Process Different PDFs

Edit `main.py`:
```python
result = system.process_reports(
    inspection_pdf="YOUR_INSPECTION.pdf",
    thermal_pdf="YOUR_THERMAL.pdf",
    output_path="output/your_report.md"
)
```

---

## Models Used

### Primary Model: Llama 3.3 70B Versatile

**Provider:** Groq  
**Model Name:** `llama-3.3-70b-versatile`  
**Purpose:** All 5 agents use this model

**Why This Model?**
- ✅ **Free tier available** (30 requests/min)
- ✅ **Fast inference** (~1-2 seconds per request)
- ✅ **Strong reasoning** (70B parameters)
- ✅ **Good at structured output** (JSON generation)
- ✅ **Open source** (Meta's Llama 3.3)

**Model Specifications:**
- **Parameters:** 70 billion
- **Context window:** 8,192 tokens
- **Training data:** Up to December 2023
- **Strengths:** Reasoning, instruction following, structured output
- **Temperature settings:**
  - Extraction agents: 0.1 (factual)
  - Validation agent: 0.1 (precise)
  - Generation agent: 0.3 (balanced)
  - Quality agent: 0.1 (strict)

**Alternative Models (if needed):**
- `mixtral-8x7b-32768` - Faster, smaller
- `gemma2-9b-it` - Very fast, good for testing
- GPT-4 (OpenAI) - More expensive but higher quality
- Claude 3 (Anthropic) - Good alternative

---

## Next Steps

After successful setup:

1. ✅ **Read the output**: Check `output/generated_ddr.md`
2. ✅ **Review architecture**: Read `ARCHITECTURE.md`
3. ✅ **Understand the system**: Read `EXPLANATION_FOR_YOU.md`
4. ✅ **Check results**: Review `RUN_RESULTS.md`
5. ✅ **Prepare for evaluation**: Read `CHECKLIST.md`

---

## Quick Reference

### Essential Commands

```bash
# Activate environment
.\venv\Scripts\activate          # Windows
source venv/bin/activate         # Linux/Mac

# Setup API key
python setup_env.py

# Verify setup
python verify_setup.py

# Run system
python main.py

# Deactivate environment
deactivate
```

### File Locations

- **API Key**: `.env` (never commit!)
- **Input PDFs**: Project root
- **Output**: `output/` folder
- **Logs**: Console output
- **Config**: `.env` file

### Getting Help

1. Run `python verify_setup.py` for diagnostics
2. Check this SETUP.md file
3. Review error messages carefully
4. Check Groq console for API status

---

## Security Checklist

Before sharing on GitHub:

- [ ] `.env` file is in `.gitignore`
- [ ] No API keys in code files
- [ ] No API keys in screenshots
- [ ] `.env.example` has placeholder only
- [ ] README mentions API key setup
- [ ] No sensitive data in output files

---

**Setup complete?** Run `python main.py` and check your first DDR report! 🚀
