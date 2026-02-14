# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Get Free API Key
1. Visit https://console.groq.com
2. Sign up (free)
3. Go to API Keys section
4. Create new API key
5. Copy the key

### Step 3: Configure
```bash
# Copy example env file
copy .env.example .env

# Edit .env and add your key
# GROQ_API_KEY=gsk_your_key_here
```

### Step 4: Run
```bash
python main.py
```

### Step 5: Check Output
```bash
# View generated report
type output\generated_ddr.md

# View intermediate data
type output\merged_data.json
```

## 📁 Project Structure
```
├── main.py                    # Run this!
├── agents/
│   ├── extraction_agent.py    # Extract from PDFs
│   ├── validation_agent.py    # Merge & validate
│   ├── generation_agent.py    # Generate DDR
│   └── quality_agent.py       # Quality check
├── models/
│   └── schemas.py             # Data structures
├── utils/
│   └── pdf_parser.py          # PDF utilities
├── output/                    # Generated files
│   ├── generated_ddr.md       # Final report ⭐
│   ├── inspection_data.json
│   ├── thermal_data.json
│   ├── merged_data.json
│   └── quality_check.json
├── Sample Report.pdf          # Input
├── Thermal Images.pdf         # Input
└── Main DDR.pdf               # Reference format
```

## 🎯 What Happens When You Run

```
🚀 Initializing Multi-Agent DDR Generation System...
✅ All agents initialized

============================================================
STEP 1: EXTRACTING DATA FROM PDFs
============================================================
📄 Reading Sample Report.pdf...
   Extracted 45000 characters
📄 Reading Thermal Images.pdf...
   Extracted 12000 characters

============================================================
STEP 2: AGENT 1 & 2 - STRUCTURED EXTRACTION
============================================================
🤖 Agent 1: Extracting inspection data...
   ✅ Extracted 25 observations
🤖 Agent 2: Extracting thermal data...
   ✅ Extracted 8 thermal readings

============================================================
STEP 3: AGENT 3 - MERGE & VALIDATE
============================================================
🤖 Agent 3: Merging and validating data...
   ✅ Merged 28 observations
   ⚠️  Found 2 conflicts
   ℹ️  Identified 5 missing items

============================================================
STEP 4: AGENT 4 - GENERATE DDR REPORT
============================================================
🤖 Agent 4: Generating DDR report...
   ✅ Generated report (8500 characters)

============================================================
STEP 5: AGENT 5 - QUALITY VALIDATION
============================================================
🤖 Agent 5: Performing quality check...
   ✅ Validation complete
   Valid: True
   Clarity Score: 8/10

============================================================
SAVING FINAL REPORT
============================================================
✅ Final DDR saved to: output/generated_ddr.md
📊 Intermediate data saved to: output/

============================================================
✨ PROCESS COMPLETE!
============================================================
```

## 🔍 Understanding the Output

### generated_ddr.md
The final client-ready report with:
- Property Issue Summary
- Area-wise Observations
- Root Cause Analysis
- Severity Assessment
- Recommendations
- Missing Information

### inspection_data.json
Raw extracted data from inspection report:
```json
{
  "property_info": {...},
  "observations": [
    {
      "area": "Master Bedroom",
      "issue": "Dampness at skirting level",
      "severity": "Moderate",
      "source": "inspection"
    }
  ]
}
```

### thermal_data.json
Raw extracted thermal readings:
```json
{
  "thermal_readings": [
    {
      "area": "Bedroom Wall",
      "temperature": "3°C below ambient",
      "finding": "Cold spot indicating moisture"
    }
  ]
}
```

### merged_data.json
Validated combined data:
```json
{
  "observations": [...],
  "conflicts": ["Conflict description if any"],
  "missing_info": ["List of missing data"]
}
```

### quality_check.json
Validation results:
```json
{
  "is_valid": true,
  "clarity_score": 8,
  "quality_issues": [],
  "suggestions": []
}
```

## 🛠️ Troubleshooting

### "GROQ_API_KEY not found"
- Make sure .env file exists
- Check the key is correct
- No quotes needed around the key

### "Rate limit exceeded"
- Groq free tier has limits
- Wait a minute and try again
- Or upgrade to paid tier

### "Error parsing extraction"
- Check PDF files are in root directory
- Ensure PDFs are readable (not corrupted)
- Check internet connection (API calls)

### "Module not found"
```bash
pip install -r requirements.txt
```

## 📊 Testing with Your Own Files

Replace the input files:
```python
# In main.py, change these lines:
result = system.process_reports(
    inspection_pdf="YOUR_INSPECTION.pdf",
    thermal_pdf="YOUR_THERMAL.pdf",
    output_path="output/your_ddr.md"
)
```

## 💡 Tips

1. **Check intermediate files** if output looks wrong
2. **Review quality_check.json** for issues
3. **Adjust temperature** in agents for more/less creativity
4. **Save API calls** by reusing extracted JSON files

## 🎓 Next Steps

1. Read ARCHITECTURE.md for detailed explanation
2. Examine the generated output files
3. Compare with Main DDR.pdf reference
4. Customize prompts in agents/ for your needs
5. Add more validation rules in quality_agent.py
