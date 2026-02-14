from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import json
from typing import Dict

class ValidationAgent:
    """Agent responsible for merging and validating data from multiple sources"""
    
    def __init__(self, api_key: str, model: str = "llama-3.3-70b-versatile"):
        self.llm = ChatGroq(
            api_key=api_key,
            model=model,
            temperature=0.1
        )
    
    def merge_and_validate(self, inspection_data: Dict, thermal_data: Dict) -> Dict:
        """Merge inspection and thermal data, detect conflicts and missing info"""
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert at merging and validating property inspection data.

Your task: Intelligently merge inspection and thermal data.

CRITICAL RULES:
1. Match observations by AREA/LOCATION
2. Combine related observations (e.g., "dampness" from inspection + "cold spot" from thermal)
3. DETECT CONFLICTS: If inspection and thermal data contradict, FLAG IT explicitly
4. IDENTIFY MISSING INFO: Note what information is incomplete
5. DO NOT resolve conflicts arbitrarily - present both values
6. Deduplicate similar observations
7. Mark combined observations with source="both"

Return JSON:
{{
    "observations": [
        {{
            "area": "location",
            "issue": "combined description",
            "severity": "Good/Moderate/Poor",
            "source": "inspection/thermal/both",
            "details": "merged context"
        }}
    ],
    "conflicts": ["description of any conflicts found"],
    "missing_info": ["list of missing required information"]
}}"""),
            ("human", """Merge these datasets:

INSPECTION DATA:
{inspection}

THERMAL DATA:
{thermal}

Merge intelligently, detect conflicts, identify missing information.""")
        ])
        
        chain = prompt | self.llm
        response = chain.invoke({
            "inspection": json.dumps(inspection_data, indent=2),
            "thermal": json.dumps(thermal_data, indent=2)
        })
        
        try:
            content = response.content
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0]
            elif "```" in content:
                content = content.split("```")[1].split("```")[0]
            
            data = json.loads(content.strip())
            return data
        except Exception as e:
            print(f"Error parsing validation: {e}")
            return {"error": str(e), "raw_response": response.content}
