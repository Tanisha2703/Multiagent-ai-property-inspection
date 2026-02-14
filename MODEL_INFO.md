# 🤖 Model Information

## Overview

This system uses **Llama 3.3 70B** via the **Groq API** for all AI operations.

---

## Primary Model

### Llama 3.3 70B Versatile

**Official Name:** `llama-3.3-70b-versatile`  
**Provider:** Groq  
**Developer:** Meta AI  
**Release:** December 2024

### Specifications

| Attribute | Value |
|-----------|-------|
| **Parameters** | 70 billion |
| **Architecture** | Transformer (decoder-only) |
| **Context Window** | 8,192 tokens (~6,000 words) |
| **Training Data Cutoff** | December 2023 |
| **Languages** | Multilingual (English optimized) |
| **License** | Llama 3 Community License |

### Capabilities

✅ **Strengths:**
- Strong reasoning and logic
- Excellent instruction following
- Good at structured output (JSON)
- Multilingual support
- Fast inference via Groq

⚠️ **Limitations:**
- Knowledge cutoff: December 2023
- May occasionally produce incorrect information
- Requires clear, specific prompts
- Context window limited to 8K tokens

---

## Why This Model?

### 1. Cost-Effective
- **Free tier available**: 30 requests/minute
- **No credit card required**
- **Sufficient for testing and demos**
- **Paid tier is affordable** if needed

### 2. Performance
- **Fast inference**: 1-2 seconds per request via Groq
- **High quality**: 70B parameters provide strong reasoning
- **Reliable**: Consistent structured output

### 3. Accessibility
- **Easy API access**: Simple REST API
- **Good documentation**: Clear examples
- **Active community**: Support available

### 4. Open Source
- **Transparent**: Model architecture is public
- **No vendor lock-in**: Can switch providers
- **Community-driven**: Continuous improvements

---

## Model Usage in System

### Agent 1: Inspection Extraction
- **Model:** `llama-3.3-70b-versatile`
- **Temperature:** 0.1 (low = factual)
- **Purpose:** Extract structured data from inspection report
- **Input:** Raw PDF text
- **Output:** JSON with observations

### Agent 2: Thermal Extraction
- **Model:** `llama-3.3-70b-versatile`
- **Temperature:** 0.1 (low = factual)
- **Purpose:** Extract thermal readings and findings
- **Input:** Raw PDF text
- **Output:** JSON with thermal data

### Agent 3: Validation & Merging
- **Model:** `llama-3.3-70b-versatile`
- **Temperature:** 0.1 (low = precise)
- **Purpose:** Merge data, detect conflicts, identify missing info
- **Input:** Both JSON files
- **Output:** Merged JSON with conflicts/missing_info

### Agent 4: DDR Generation
- **Model:** `llama-3.3-70b-versatile`
- **Temperature:** 0.3 (medium = balanced)
- **Purpose:** Generate client-friendly DDR report
- **Input:** Merged JSON
- **Output:** Markdown report

### Agent 5: Quality Check
- **Model:** `llama-3.3-70b-versatile`
- **Temperature:** 0.1 (low = strict)
- **Purpose:** Validate report quality
- **Input:** Generated report + source data
- **Output:** Quality validation JSON

---

## Temperature Settings Explained

### What is Temperature?

Temperature controls the randomness/creativity of the model's output:
- **0.0**: Deterministic (always same output)
- **0.1**: Very factual, minimal creativity
- **0.5**: Balanced
- **1.0**: Creative, varied
- **2.0**: Very random

### Our Settings

| Agent | Temperature | Reason |
|-------|-------------|--------|
| Extraction (1&2) | 0.1 | Need factual, accurate extraction |
| Validation (3) | 0.1 | Need precise conflict detection |
| Generation (4) | 0.3 | Need some creativity for natural language |
| Quality (5) | 0.1 | Need strict, consistent validation |

---

## API Provider: Groq

### What is Groq?

Groq is an AI infrastructure company that provides ultra-fast LLM inference through custom hardware (LPU - Language Processing Unit).

### Why Groq?

1. **Speed**: 10-100x faster than traditional GPU inference
2. **Free Tier**: Generous limits for testing
3. **Reliability**: High uptime and availability
4. **Easy Integration**: Simple REST API

### Groq API Details

**Endpoint:** `https://api.groq.com/openai/v1/chat/completions`  
**Authentication:** API key in header  
**Rate Limits (Free Tier):**
- 30 requests per minute
- 14,400 requests per day
- Sufficient for ~1,800 reports/hour

**Pricing (if upgrading):**
- Pay-as-you-go available
- Competitive rates
- No minimum commitment

---

## Alternative Models

If you want to use different models, here are options:

### Other Groq Models

1. **Mixtral 8x7B** (`mixtral-8x7b-32768`)
   - Faster, smaller
   - Good for testing
   - 32K context window

2. **Gemma 2 9B** (`gemma2-9b-it`)
   - Very fast
   - Smaller model
   - Good for simple tasks

### Other Providers

1. **OpenAI GPT-4**
   - Higher quality
   - More expensive (~$0.03/1K tokens)
   - Requires OpenAI API key

2. **Anthropic Claude 3**
   - Excellent reasoning
   - Good alternative
   - Requires Anthropic API key

3. **Local Models**
   - Llama 3.1 8B (run locally)
   - Free but slower
   - Requires GPU

---

## Switching Models

### Change Groq Model

Edit agent files (`agents/*.py`):

```python
def __init__(self, api_key: str, model: str = "llama-3.3-70b-versatile"):
    # Change to:
    # model: str = "mixtral-8x7b-32768"
    # or
    # model: str = "gemma2-9b-it"
```

### Switch to OpenAI

1. Install OpenAI package:
```bash
pip install openai langchain-openai
```

2. Update imports:
```python
from langchain_openai import ChatOpenAI
```

3. Update initialization:
```python
self.llm = ChatOpenAI(
    api_key=api_key,
    model="gpt-4",
    temperature=0.1
)
```

### Switch to Anthropic Claude

1. Install Anthropic package:
```bash
pip install anthropic langchain-anthropic
```

2. Update imports:
```python
from langchain_anthropic import ChatAnthropic
```

3. Update initialization:
```python
self.llm = ChatAnthropic(
    api_key=api_key,
    model="claude-3-opus-20240229",
    temperature=0.1
)
```

---

## Model Performance

### Benchmarks (Our System)

| Metric | Value |
|--------|-------|
| **Processing Time** | ~30 seconds per report |
| **Token Usage** | ~13K tokens per report |
| **Cost (Free Tier)** | $0 |
| **Accuracy** | High (8/10 quality score) |
| **Hallucination Rate** | Low (validation passed) |

### Token Breakdown

| Step | Tokens |
|------|--------|
| Extraction (Agent 1&2) | ~4,000 |
| Validation (Agent 3) | ~3,000 |
| Generation (Agent 4) | ~4,000 |
| Quality Check (Agent 5) | ~2,000 |
| **Total** | **~13,000** |

---

## Model Limitations

### Known Issues

1. **Knowledge Cutoff**: December 2023
   - Won't know about events after this date
   - May have outdated information

2. **Context Window**: 8,192 tokens
   - Very large PDFs may need chunking
   - Current system handles typical reports fine

3. **Occasional Errors**:
   - May misinterpret complex tables
   - May miss subtle details
   - Quality check catches most issues

4. **Language**: Optimized for English
   - Works with other languages
   - English gives best results

### Mitigation Strategies

✅ **Low Temperature**: Reduces hallucinations  
✅ **Explicit Prompts**: Clear instructions improve accuracy  
✅ **Validation Agent**: Catches errors automatically  
✅ **Source Attribution**: Tracks where facts come from  
✅ **Intermediate Files**: Allows manual verification  

---

## Model Updates

### Staying Current

Groq regularly updates available models. Check:
- **Groq Console**: https://console.groq.com/docs/models
- **Deprecation Notices**: https://console.groq.com/docs/deprecations

### If Model is Deprecated

1. Check Groq docs for replacement model
2. Update model name in agent files
3. Test with sample data
4. Adjust temperature if needed

---

## Responsible AI Use

### Best Practices

✅ **Verify Output**: Always review generated reports  
✅ **Human Oversight**: Don't blindly trust AI  
✅ **Cite Sources**: Mention AI was used  
✅ **Protect Privacy**: Don't send sensitive data  
✅ **Stay Updated**: Monitor model changes  

### Ethical Considerations

- AI is a tool, not a replacement for human expertise
- Always verify critical information
- Be transparent about AI usage
- Respect data privacy and security
- Follow applicable regulations

---

## Support & Resources

### Groq Resources
- **Documentation**: https://console.groq.com/docs
- **API Reference**: https://console.groq.com/docs/api-reference
- **Models**: https://console.groq.com/docs/models
- **Support**: https://console.groq.com/support

### Llama 3 Resources
- **Model Card**: https://ai.meta.com/llama/
- **Research Paper**: https://arxiv.org/abs/2407.21783
- **GitHub**: https://github.com/meta-llama/llama3

### LangChain Resources
- **Documentation**: https://python.langchain.com/
- **Groq Integration**: https://python.langchain.com/docs/integrations/chat/groq

---

**Model Version:** Llama 3.3 70B Versatile  
**Last Updated:** February 14, 2026  
**Status:** Active and Supported ✅
