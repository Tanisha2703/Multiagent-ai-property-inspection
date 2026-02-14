import os
from dotenv import load_dotenv
from utils.pdf_parser import PDFParser
from agents.extraction_agent import ExtractionAgent
from agents.validation_agent import ValidationAgent
from agents.generation_agent import GenerationAgent
from agents.quality_agent import QualityAgent
import json

class DDRGenerationSystem:
    """Multi-agent system for DDR report generation"""
    
    def __init__(self, api_key: str):
        print("🚀 Initializing Multi-Agent DDR Generation System...")
        self.pdf_parser = PDFParser()
        self.extraction_agent = ExtractionAgent(api_key)
        self.validation_agent = ValidationAgent(api_key)
        self.generation_agent = GenerationAgent(api_key)
        self.quality_agent = QualityAgent(api_key)
        print("✅ All agents initialized\n")
    
    def process_reports(self, inspection_pdf: str, thermal_pdf: str, output_path: str = "output/generated_ddr.md"):
        """Main pipeline to process reports and generate DDR"""
        
        print("="*60)
        print("STEP 1: EXTRACTING DATA FROM PDFs")
        print("="*60)
        
        # Extract text from PDFs
        print(f"📄 Reading {inspection_pdf}...")
        inspection_text = self.pdf_parser.extract_text(inspection_pdf)
        print(f"   Extracted {len(inspection_text)} characters")
        
        print(f"📄 Reading {thermal_pdf}...")
        thermal_text = self.pdf_parser.extract_text(thermal_pdf)
        print(f"   Extracted {len(thermal_text)} characters\n")
        
        # Agent 1 & 2: Extract structured data
        print("="*60)
        print("STEP 2: AGENT 1 & 2 - STRUCTURED EXTRACTION")
        print("="*60)
        
        print("🤖 Agent 1: Extracting inspection data...")
        inspection_data = self.extraction_agent.extract_inspection_data(inspection_text)
        print(f"   ✅ Extracted {len(inspection_data.get('observations', []))} observations")
        
        print("🤖 Agent 2: Extracting thermal data...")
        thermal_data = self.extraction_agent.extract_thermal_data(thermal_text)
        print(f"   ✅ Extracted {len(thermal_data.get('thermal_readings', []))} thermal readings\n")
        
        # Save intermediate data
        os.makedirs("output", exist_ok=True)
        with open("output/inspection_data.json", "w") as f:
            json.dump(inspection_data, f, indent=2)
        with open("output/thermal_data.json", "w") as f:
            json.dump(thermal_data, f, indent=2)
        print("💾 Saved intermediate data to output/\n")
        
        # Agent 3: Merge and validate
        print("="*60)
        print("STEP 3: AGENT 3 - MERGE & VALIDATE")
        print("="*60)
        
        print("🤖 Agent 3: Merging and validating data...")
        merged_data = self.validation_agent.merge_and_validate(inspection_data, thermal_data)
        print(f"   ✅ Merged {len(merged_data.get('observations', []))} observations")
        print(f"   ⚠️  Found {len(merged_data.get('conflicts', []))} conflicts")
        print(f"   ℹ️  Identified {len(merged_data.get('missing_info', []))} missing items\n")
        
        with open("output/merged_data.json", "w") as f:
            json.dump(merged_data, f, indent=2)
        
        # Agent 4: Generate DDR
        print("="*60)
        print("STEP 4: AGENT 4 - GENERATE DDR REPORT")
        print("="*60)
        
        print("🤖 Agent 4: Generating DDR report...")
        ddr_report = self.generation_agent.generate_ddr(merged_data)
        print(f"   ✅ Generated report ({len(ddr_report)} characters)\n")
        
        # Agent 5: Quality check
        print("="*60)
        print("STEP 5: AGENT 5 - QUALITY VALIDATION")
        print("="*60)
        
        print("🤖 Agent 5: Performing quality check...")
        quality_result = self.quality_agent.validate_report(ddr_report, merged_data)
        print(f"   ✅ Validation complete")
        print(f"   Valid: {quality_result.get('is_valid', 'Unknown')}")
        print(f"   Clarity Score: {quality_result.get('clarity_score', 'N/A')}/10\n")
        
        if quality_result.get('quality_issues'):
            print("   ⚠️  Quality Issues Found:")
            for issue in quality_result.get('quality_issues', []):
                print(f"      - {issue}")
        
        with open("output/quality_check.json", "w") as f:
            json.dump(quality_result, f, indent=2)
        
        # Save final report
        print("\n" + "="*60)
        print("SAVING FINAL REPORT")
        print("="*60)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(ddr_report)
        
        print(f"✅ Final DDR saved to: {output_path}")
        print(f"📊 Intermediate data saved to: output/")
        print("\n" + "="*60)
        print("✨ PROCESS COMPLETE!")
        print("="*60)
        
        return {
            "report": ddr_report,
            "quality": quality_result,
            "merged_data": merged_data
        }

def main():
    # Load environment variables
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        print("❌ ERROR: GROQ_API_KEY not found!")
        print("Please:")
        print("1. Get free API key from https://console.groq.com")
        print("2. Create .env file with: GROQ_API_KEY=your_key_here")
        return
    
    # Initialize system
    system = DDRGenerationSystem(api_key)
    
    # Process reports
    result = system.process_reports(
        inspection_pdf="Sample Report.pdf",
        thermal_pdf="Thermal Images.pdf",
        output_path="output/generated_ddr.md"
    )
    
    print("\n📋 Summary:")
    print(f"   - Report length: {len(result['report'])} characters")
    print(f"   - Quality valid: {result['quality'].get('is_valid', 'Unknown')}")
    print(f"   - Observations: {len(result['merged_data'].get('observations', []))}")

if __name__ == "__main__":
    main()
