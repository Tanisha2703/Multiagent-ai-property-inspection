from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from typing import Dict

class QualityAgent:
    """Agent responsible for quality checking the generated report"""
    
    def __init__(self, api_key: str, model: str = "llama-3.3-70b-versatile"):
        self.llm = ChatGroq(
            api_key=api_key,
            model=model,
            temperature=0.1
        )
    
    def validate_report(self, report: str, source_data: Dict) -> Dict:
        """Validate the generated report for quality and accuracy"""
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a quality assurance expert for property diagnostic reports.

Your task: Validate the DDR report for completeness and accuracy.

CHECK FOR:
1. All required sections present (Summary, Observations, Root Cause, Severity, Recommendations, Notes, Missing Info)
2. No hallucinated facts (everything traceable to source data)
3. Clear, client-friendly language
4. Proper handling of missing information ("Not Available" used appropriately)
5. Logical consistency
6. Specific, actionable recommendations

Return JSON:
{{
    "is_valid": true/false,
    "missing_sections": ["list any missing required sections"],
    "quality_issues": ["list any problems found"],
    "hallucination_check": "pass/fail - are there invented facts?",
    "clarity_score": "1-10",
    "suggestions": ["improvements to make"]
}}"""),
            ("human", """Validate this report:

REPORT:
{report}

SOURCE DATA:
{source_data}

Perform thorough quality check.""")
        ])
        
        chain = prompt | self.llm
        response = chain.invoke({
            "report": report,
            "source_data": str(source_data)
        })
        
        try:
            content = response.content
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0]
            elif "```" in content:
                content = content.split("```")[1].split("```")[0]
            
            import json
            data = json.loads(content.strip())
            return data
        except Exception as e:
            print(f"Error parsing quality check: {e}")
            return {"error": str(e), "raw_response": response.content}
