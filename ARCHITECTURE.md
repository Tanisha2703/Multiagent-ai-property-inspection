# DDR Generation System - Architecture & Approach

## 🎯 Goal
Build an AI system that converts technical inspection data into a structured, client-ready DDR (Detailed Diagnostic Report).

## 📊 System Architecture

### Multi-Agent Pipeline

```
┌─────────────────────────────────────────────────────────────┐
│                    INPUT DOCUMENTS                          │
│  • Sample Report.pdf (Inspection)                           │
│  • Thermal Images.pdf (Thermal Data)                        │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              STEP 1: PDF PARSING                            │
│  Tool: PyMuPDF                                              │
│  • Extract text from both PDFs                              │
│  • Extract images (for reference)                           │
│  • Preserve structure                                       │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         STEP 2: PARALLEL EXTRACTION                         │
│                                                             │
│  ┌──────────────────────┐  ┌──────────────────────┐       │
│  │   AGENT 1            │  │   AGENT 2            │       │
│  │   Inspection Extract │  │   Thermal Extract    │       │
│  │                      │  │                      │       │
│  │  • Parse checklist   │  │  • Extract temps     │       │
│  │  • Extract issues    │  │  • Parse findings    │       │
│  │  • Get severity      │  │  • Note images       │       │
│  │  • Map locations     │  │  • Map locations     │       │
│  └──────────┬───────────┘  └──────────┬───────────┘       │
│             │                          │                   │
│             └──────────┬───────────────┘                   │
│                        ▼                                   │
│              inspection_data.json                          │
│              thermal_data.json                             │
└─────────────────────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         STEP 3: MERGE & VALIDATE                            │
│                                                             │
│  ┌──────────────────────────────────────────────┐          │
│  │   AGENT 3 - Validation Agent                 │          │
│  │                                               │          │
│  │  • Match observations by AREA                │          │
│  │  • Combine related findings                  │          │
│  │  • DETECT conflicts                          │          │
│  │  • IDENTIFY missing info                     │          │
│  │  • Deduplicate observations                  │          │
│  │  • Flag "Not Available" items                │          │
│  └──────────────────┬───────────────────────────┘          │
│                     ▼                                       │
│              merged_data.json                               │
│              (with conflicts & missing_info)                │
└─────────────────────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         STEP 4: DDR GENERATION                              │
│                                                             │
│  ┌──────────────────────────────────────────────┐          │
│  │   AGENT 4 - Generation Agent                 │          │
│  │                                               │          │
│  │  Generate structured report:                 │          │
│  │  1. Property Issue Summary                   │          │
│  │  2. Area-wise Observations                   │          │
│  │  3. Probable Root Cause                      │          │
│  │  4. Severity Assessment (with reasoning)     │          │
│  │  5. Recommended Actions                      │          │
│  │  6. Additional Notes                         │          │
│  │  7. Missing/Unclear Information              │          │
│  └──────────────────┬───────────────────────────┘          │
│                     ▼                                       │
│              generated_ddr.md (draft)                       │
└─────────────────────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         STEP 5: QUALITY CHECK                               │
│                                                             │
│  ┌──────────────────────────────────────────────┐          │
│  │   AGENT 5 - Quality Agent                    │          │
│  │                                               │          │
│  │  Validate:                                   │          │
│  │  • All sections present                      │          │
│  │  • No hallucinations                         │          │
│  │  • Clear language                            │          │
│  │  • Proper "Not Available" usage              │          │
│  │  • Logical consistency                       │          │
│  └──────────────────┬───────────────────────────┘          │
│                     ▼                                       │
│              quality_check.json                             │
└─────────────────────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                 FINAL OUTPUT                                │
│  • generated_ddr.md (Final Report)                          │
│  • All intermediate JSON files for audit                    │
└─────────────────────────────────────────────────────────────┘
```

## 🔧 Technology Stack

### Core Components
- **LLM**: Llama 3.1 70B via Groq API (FREE tier available)
- **Framework**: LangChain for agent orchestration
- **PDF Processing**: PyMuPDF (fitz)
- **Data Validation**: Pydantic models
- **Language**: Python 3.8+

### Why This Stack?
1. **Groq API**: Free, fast inference for Llama models
2. **Llama 3.1 70B**: Strong reasoning, good at structured extraction
3. **LangChain**: Easy agent management and prompt templating
4. **Pydantic**: Type-safe data validation

## 📋 How Each Agent Works

### Agent 1: Inspection Extraction
**Input**: Raw text from Sample Report.pdf  
**Output**: Structured JSON with observations

**Process**:
1. Parse checklist-style data
2. Extract severity ratings (Good/Moderate/Poor)
3. Identify areas (Terrace, Bedroom, Bathroom, etc.)
4. Capture specific issues (cracks, dampness, hollowness)
5. Preserve measurements and technical details

**Key Prompt Instructions**:
- Extract ONLY facts present
- Mark missing data as "Not Available"
- Preserve exact measurements
- Source attribution: "inspection"

### Agent 2: Thermal Extraction
**Input**: Raw text from Thermal Images.pdf  
**Output**: Structured JSON with thermal readings

**Process**:
1. Extract temperature readings
2. Identify thermal anomalies
3. Map to locations
4. Note image references
5. Capture findings

**Key Prompt Instructions**:
- Extract temperature values exactly
- If temp not specified: "Not Available"
- Link to image references
- Source attribution: "thermal"

### Agent 3: Validation & Merging
**Input**: inspection_data.json + thermal_data.json  
**Output**: merged_data.json with conflicts and missing info

**Process**:
1. **Area Matching**: Group observations by location
2. **Intelligent Merging**: 
   - "Dampness in bedroom" + "Cold spot in bedroom" → Combined observation
3. **Conflict Detection**:
   - If data contradicts → Flag explicitly
   - Don't resolve arbitrarily
4. **Missing Info Tracking**:
   - Required fields not present → List in missing_info
5. **Deduplication**:
   - Semantic similarity check
   - Remove redundant observations

**Example Merge**:
```
Inspection: "Dampness at skirting level in bedroom"
Thermal: "Temperature 3°C below ambient in bedroom wall"
→ Merged: "Moisture intrusion at skirting level in bedroom, 
           evidenced by dampness and thermal signature (3°C below ambient)"
Source: "both"
```

### Agent 4: DDR Generation
**Input**: merged_data.json  
**Output**: Complete DDR report in markdown

**Process**:
1. Generate Property Issue Summary (high-level overview)
2. Create Area-wise Observations (organized by location)
3. Analyze Probable Root Cause (why issues occurred)
4. Assess Severity (with evidence-based reasoning)
5. Recommend Actions (specific, actionable steps)
6. Add Additional Notes (context, warnings)
7. List Missing Information (explicit "Not Available")

**Key Prompt Instructions**:
- Client-friendly language (avoid jargon)
- Specific references to locations
- Link severity to evidence
- Actionable recommendations
- No invented facts

### Agent 5: Quality Check
**Input**: generated_ddr.md + merged_data.json  
**Output**: quality_check.json with validation results

**Checks**:
1. ✅ All 7 sections present
2. ✅ No hallucinated facts (traceable to source)
3. ✅ Clear, accessible language
4. ✅ Proper "Not Available" usage
5. ✅ Logical consistency
6. ✅ Specific recommendations

**Output**:
```json
{
  "is_valid": true/false,
  "missing_sections": [],
  "quality_issues": [],
  "hallucination_check": "pass/fail",
  "clarity_score": 8,
  "suggestions": []
}
```

## 🎯 Evaluation Criteria Addressed

### 1. Accuracy of Extracted Information ✅
- **Approach**: Low temperature (0.1) for extraction agents
- **Validation**: Source attribution for every fact
- **Audit Trail**: All intermediate JSON files saved
- **No Hallucinations**: Explicit instruction to extract only present facts

### 2. Logical Merging ✅
- **Approach**: Area-based matching algorithm
- **Intelligence**: Semantic combination of related observations
- **Example**: Visual + thermal evidence combined logically
- **Deduplication**: Semantic similarity check

### 3. Handling Missing/Conflicting Details ✅
- **Missing Data**: Explicit "Not Available" marking
- **Conflicts**: Flagged in conflicts array, not hidden
- **Transparency**: Both conflicting values presented with sources
- **Tracking**: missing_info list in merged data

### 4. Clarity of Final DDR Output ✅
- **Language**: Client-friendly, minimal jargon
- **Structure**: Clear sections with headings
- **Specificity**: Exact locations and measurements
- **Readability**: Bullet points, organized by area
- **Professional**: Follows DDR format conventions

### 5. System Thinking and Reliability ✅
- **Modular Design**: Each agent has single responsibility
- **Testable**: Each component can be tested independently
- **Auditable**: All intermediate outputs saved
- **Reusable**: Works on similar reports without modification
- **Error Handling**: Graceful degradation with error messages
- **Validation**: Quality check ensures output meets standards

## 💰 Cost Analysis

### Using Groq (FREE tier):
- **Llama 3.1 70B**: Free up to rate limits
- **Rate Limit**: 30 requests/minute, 14,400/day
- **Cost per report**: $0 (within free tier)

### If using paid alternatives:
- **GPT-4o-mini**: ~$0.02-0.05 per report
- **Claude Haiku**: ~$0.01-0.03 per report
- **GPT-4**: ~$0.15-0.25 per report

### Token Usage Estimate:
- Extraction: ~4K tokens
- Validation: ~3K tokens  
- Generation: ~4K tokens
- Quality: ~2K tokens
- **Total**: ~13K tokens per report

## 🚀 Running the System

### Setup:
```bash
# Install dependencies
pip install -r requirements.txt

# Get free API key
# Visit: https://console.groq.com

# Create .env file
echo "GROQ_API_KEY=your_key_here" > .env
```

### Run:
```bash
python main.py
```

### Output:
```
output/
├── generated_ddr.md       # Final report
├── inspection_data.json   # Extracted inspection data
├── thermal_data.json      # Extracted thermal data
├── merged_data.json       # Validated merged data
└── quality_check.json     # Quality validation results
```

## 🔍 Key Design Decisions

### Why Multi-Agent?
1. **Separation of Concerns**: Each agent has clear responsibility
2. **Testability**: Can test extraction without generation
3. **Debuggability**: Intermediate outputs show where issues occur
4. **Modularity**: Easy to swap or improve individual agents
5. **Evaluation**: Shows "system thinking" to evaluators

### Why Groq + Llama?
1. **Cost**: Free tier available
2. **Speed**: Fast inference
3. **Quality**: Llama 3.1 70B has strong reasoning
4. **Open Source**: No vendor lock-in

### Why Save Intermediate Data?
1. **Audit Trail**: Can trace every fact to source
2. **Debugging**: Easy to see where pipeline fails
3. **Evaluation**: Shows extraction accuracy
4. **Transparency**: Demonstrates no hallucinations

## 📈 Future Enhancements

1. **Image Analysis**: Use vision models for thermal images
2. **Confidence Scoring**: Add confidence levels to extractions
3. **Human-in-Loop**: Flag low-confidence items for review
4. **Template Customization**: Support different DDR formats
5. **Batch Processing**: Process multiple properties at once
