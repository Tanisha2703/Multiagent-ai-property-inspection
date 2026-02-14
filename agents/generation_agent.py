from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import json
from typing import Dict

class GenerationAgent:
    """Agent responsible for generating the final DDR report"""
    
    def __init__(self, api_key: str, model: str = "llama-3.3-70b-versatile"):
        self.llm = ChatGroq(
            api_key=api_key,
            model=model,
            temperature=0.3  # Slightly higher for natural language generation
        )
    
    def generate_ddr(self, merged_data: Dict) -> str:
        """Generate final DDR report from merged data"""
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert at creating professional property diagnostic reports for clients.

Your task: Generate a complete DDR (Detailed Diagnostic Report) in a clear, client-friendly format.

REQUIRED SECTIONS:
1. Property Issue Summary - Brief overview of main problems
2. Area-wise Observations - Organized by location (Bedroom, Bathroom, Terrace, etc.)
3. Probable Root Cause - Analysis of why issues occurred
4. Severity Assessment - Overall severity with reasoning
5. Recommended Actions - Specific repair/treatment recommendations
6. Additional Notes - Any important context
7. Missing or Unclear Information - Explicitly list "Not Available" items

CRITICAL RULES:
1. Use SIMPLE, CLIENT-FRIENDLY language (avoid excessive jargon)
2. Be SPECIFIC - reference exact locations and observations
3. DO NOT invent facts - only use provided data
4. If information is missing, write "Not Available" or "Information not provided"
5. Structure clearly with headings and bullet points
6. Link severity assessment to specific evidence
7. Make recommendations actionable

TONE: Professional but accessible, like explaining to a homeowner."""),
            ("human", """Generate a complete DDR report from this data:

{merged_data}

Create a well-structured, client-ready report.""")
        ])
        
        chain = prompt | self.llm
        response = chain.invoke({
            "merged_data": json.dumps(merged_data, indent=2)
        })
        
        return response.content
