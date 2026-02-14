"""
Streamlit Web Interface for DDR Generation System
Upload inspection and thermal PDFs, generate DDR report
"""

import streamlit as st
import os
from dotenv import load_dotenv
from main import DDRGenerationSystem
import tempfile
import time

# Page configuration
st.set_page_config(
    page_title="DDR Report Generator",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
    }
    .info-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        color: #0c5460;
    }
    .warning-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        color: #856404;
    }
</style>
""", unsafe_allow_html=True)

def initialize_system():
    """Initialize the DDR generation system"""
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key or api_key == "your_groq_api_key_here":
        return None, "API key not configured"
    
    try:
        system = DDRGenerationSystem(api_key)
        return system, None
    except Exception as e:
        return None, str(e)

def main():
    # Header
    st.markdown('<h1 class="main-header">📋 DDR Report Generator</h1>', unsafe_allow_html=True)
    st.markdown("### Multi-Agent AI System for Property Diagnostic Reports")
    
    # Sidebar
    with st.sidebar:
        st.header("ℹ️ About")
        st.markdown("""
        This system uses AI to automatically generate Detailed Diagnostic Reports (DDR) 
        from property inspection and thermal imaging data.
        
        **How it works:**
        1. Upload inspection report PDF
        2. Upload thermal images PDF
        3. Click "Generate DDR Report"
        4. Download your report!
        
        **Technology:**
        - 🤖 Llama 3.3 70B (via Groq)
        - 🔄 Multi-agent pipeline
        - ✅ Quality validation
        """)
        
        st.divider()
        
        st.header("📊 System Status")
        
        # Check system status
        system, error = initialize_system()
        if system:
            st.success("✅ System Ready")
            st.info("🤖 Model: Llama 3.3 70B")
        else:
            st.error(f"❌ System Error: {error}")
            st.warning("⚠️ Please configure API key in .env file")
    
    # Main content
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📄 Upload Inspection Report")
        inspection_file = st.file_uploader(
            "Choose inspection PDF file",
            type=['pdf'],
            key="inspection",
            help="Upload the property inspection report PDF"
        )
        
        if inspection_file:
            st.success(f"✅ Uploaded: {inspection_file.name}")
            st.info(f"📊 Size: {inspection_file.size / 1024:.2f} KB")
    
    with col2:
        st.subheader("🌡️ Upload Thermal Report")
        thermal_file = st.file_uploader(
            "Choose thermal PDF file",
            type=['pdf'],
            key="thermal",
            help="Upload the thermal imaging report PDF"
        )
        
        if thermal_file:
            st.success(f"✅ Uploaded: {thermal_file.name}")
            st.info(f"📊 Size: {thermal_file.size / 1024:.2f} KB")
    
    st.divider()
    
    # Generate button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        generate_button = st.button(
            "🚀 Generate DDR Report",
            type="primary",
            use_container_width=True,
            disabled=not (inspection_file and thermal_file)
        )
    
    # Process files
    if generate_button:
        if not inspection_file or not thermal_file:
            st.error("❌ Please upload both PDF files")
            return
        
        # Check system
        system, error = initialize_system()
        if not system:
            st.error(f"❌ System Error: {error}")
            st.info("💡 Make sure you have configured your Groq API key in the .env file")
            return
        
        # Create progress bar
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            # Save uploaded files temporarily
            with tempfile.TemporaryDirectory() as temp_dir:
                # Save inspection file
                inspection_path = os.path.join(temp_dir, "inspection.pdf")
                with open(inspection_path, "wb") as f:
                    f.write(inspection_file.getbuffer())
                
                # Save thermal file
                thermal_path = os.path.join(temp_dir, "thermal.pdf")
                with open(thermal_path, "wb") as f:
                    f.write(thermal_file.getbuffer())
                
                # Output path
                output_path = os.path.join(temp_dir, "generated_ddr.md")
                
                # Process with progress updates
                status_text.text("📄 Step 1/5: Reading PDF files...")
                progress_bar.progress(20)
                time.sleep(0.5)
                
                status_text.text("🤖 Step 2/5: Extracting data with AI agents...")
                progress_bar.progress(40)
                
                status_text.text("🔄 Step 3/5: Merging and validating data...")
                progress_bar.progress(60)
                
                status_text.text("📝 Step 4/5: Generating DDR report...")
                progress_bar.progress(80)
                
                # Actually process the reports
                result = system.process_reports(
                    inspection_pdf=inspection_path,
                    thermal_pdf=thermal_path,
                    output_path=output_path
                )
                
                status_text.text("✅ Step 5/5: Quality validation...")
                progress_bar.progress(100)
                
                # Read generated report
                with open(output_path, 'r', encoding='utf-8') as f:
                    generated_report = f.read()
                
                # Clear progress
                progress_bar.empty()
                status_text.empty()
                
                # Success message
                st.success("✅ DDR Report Generated Successfully!")
                
                # Display results
                st.divider()
                
                # Metrics
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("📊 Observations", len(result['merged_data'].get('observations', [])))
                with col2:
                    st.metric("⚠️ Conflicts", len(result['merged_data'].get('conflicts', [])))
                with col3:
                    st.metric("ℹ️ Missing Info", len(result['merged_data'].get('missing_info', [])))
                with col4:
                    quality_valid = result['quality'].get('is_valid', False)
                    st.metric("✅ Quality", "Valid" if quality_valid else "Issues")
                
                st.divider()
                
                # Tabs for different views
                tab1, tab2, tab3 = st.tabs(["📄 Generated Report", "📊 Quality Check", "🔍 Merged Data"])
                
                with tab1:
                    st.subheader("Generated DDR Report")
                    st.markdown(generated_report)
                    
                    # Download button
                    st.download_button(
                        label="⬇️ Download DDR Report",
                        data=generated_report,
                        file_name="generated_ddr.md",
                        mime="text/markdown",
                        use_container_width=True
                    )
                
                with tab2:
                    st.subheader("Quality Validation Results")
                    
                    quality = result['quality']
                    
                    if quality.get('is_valid'):
                        st.success("✅ Report passed quality validation")
                    else:
                        st.warning("⚠️ Report has quality issues")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Clarity Score", f"{quality.get('clarity_score', 'N/A')}/10")
                    with col2:
                        hallucination = quality.get('hallucination_check', 'unknown')
                        st.metric("Hallucination Check", hallucination.upper())
                    
                    if quality.get('quality_issues'):
                        st.warning("**Quality Issues:**")
                        for issue in quality['quality_issues']:
                            st.write(f"- {issue}")
                    
                    if quality.get('suggestions'):
                        st.info("**Suggestions for Improvement:**")
                        for suggestion in quality['suggestions']:
                            st.write(f"- {suggestion}")
                
                with tab3:
                    st.subheader("Merged Data Analysis")
                    
                    merged = result['merged_data']
                    
                    st.write(f"**Total Observations:** {len(merged.get('observations', []))}")
                    
                    if merged.get('conflicts'):
                        st.warning("**Conflicts Detected:**")
                        for conflict in merged['conflicts']:
                            st.write(f"- {conflict}")
                    else:
                        st.success("✅ No conflicts detected")
                    
                    if merged.get('missing_info'):
                        st.info("**Missing Information:**")
                        for missing in merged['missing_info']:
                            st.write(f"- {missing}")
                    else:
                        st.success("✅ No missing information")
                    
                    with st.expander("View All Observations"):
                        for i, obs in enumerate(merged.get('observations', []), 1):
                            st.write(f"**{i}. {obs.get('area', 'Unknown')}**")
                            st.write(f"   - Issue: {obs.get('issue', 'N/A')}")
                            st.write(f"   - Severity: {obs.get('severity', 'N/A')}")
                            st.write(f"   - Source: {obs.get('source', 'N/A')}")
                            st.divider()
        
        except Exception as e:
            progress_bar.empty()
            status_text.empty()
            st.error(f"❌ Error generating report: {str(e)}")
            st.exception(e)
    
    # Footer
    st.divider()
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 2rem;'>
        <p>🤖 Powered by Llama 3.3 70B via Groq API</p>
        <p>Multi-Agent AI System for Automated Property Diagnostics</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
