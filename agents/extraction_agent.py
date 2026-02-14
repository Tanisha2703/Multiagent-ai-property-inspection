from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from models.schemas import InspectionData, ThermalData, Observation, ThermalReading
import json
from typing import Dict

class ExtractionAgent:
    """Agent responsible for extracting structured data from reports"""
    
    def __init__(self, api_key: str, model: str = "llama-3.3-70b-versatile"):
        self.llm = ChatGroq(
            api_key=api_key,
            model=model,
            temperature=0.1  # Low temperature for accuracy
        )
    
    def extract_inspection_data(self, inspection_text: str) -> Dict:
        """Extract structured data from inspection report"""
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert at extracting structured information from property inspection reports.
            
Your task: Extract ALL observations, issues, and conditions from the inspection report.

CRITICAL RULES:
1. Extract ONLY facts present in the document - DO NOT invent information
2. For each observation, identify: area, issue description, severity (Good/Moderate/Poor)
3. If information is missing, mark as "Not Available"
4. Preserve exact measurements and technical terms
5. Note the source as "inspection"

Return a JSON object with this structure:
{{
    "property_info": {{"address": "...", "flat_no": "..."}},
    "observations": [
        {{
            "area": "area name",
            "issue": "description",
            "severity": "Good/Moderate/Poor",
            "source": "inspection",
            "details": "additional context"
        }}
    ],
    "structural_conditions": {{"overall_assessment": "..."}}
}}"""),
            ("human", "Extract data from this inspection report:\n\n{text}")
        ])
        
        chain = prompt | self.llm
        response = chain.invoke({"text": inspection_text})
        
        # Parse JSON response
        try:
            # Extract JSON from response
            content = response.content
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0]
            elif "```" in content:
                content = content.split("```")[1].split("```")[0]
            
            data = json.loads(content.strip())
            return data
        except Exception as e:
            print(f"Error parsing extraction: {e}")
            return {"error": str(e), "raw_response": response.content}
    
    def extract_thermal_data(self, thermal_text: str) -> Dict:
        """Extract structured data from thermal report"""
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert at extracting thermal imaging data from reports.

Your task: Extract ALL thermal readings and observations.

CRITICAL RULES:
1. Extract ONLY facts present in the document - DO NOT invent information
2. For each thermal observation: area, temperature (if mentioned), finding
3. Note image references if mentioned
4. If temperature not specified, mark as "Not Available"
5. Preserve exact temperature values

Return a JSON object:
{{
    "thermal_readings": [
        {{
            "area": "location",
            "temperature": "value or Not Available",
            "finding": "observation",
            "image_reference": "image number or null"
        }}
    ]
}}"""),
            ("human", "Extract thermal data from this report:\n\n{text}")
        ])
        
        chain = prompt | self.llm
        response = chain.invoke({"text": thermal_text})
        
        try:
            content = response.content
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0]
            elif "```" in content:
                content = content.split("```")[1].split("```")[0]
            
            data = json.loads(content.strip())
            return data
        except Exception as e:
            print(f"Error parsing thermal extraction: {e}")
            return {"error": str(e), "raw_response": response.content}
