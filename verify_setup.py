"""Verify that the setup is complete and ready to run"""
import sys
import os

def check_virtual_env():
    """Check if running in virtual environment"""
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )
    return in_venv

def check_packages():
    """Check if required packages are installed"""
    required = [
        'fitz',  # pymupdf
        'PIL',   # pillow
        'langchain',
        'langchain_groq',
        'pydantic',
        'dotenv'
    ]
    
    missing = []
    for package in required:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)
    
    return missing

def check_env_file():
    """Check if .env file exists"""
    return os.path.exists('.env')

def check_pdf_files():
    """Check if input PDF files exist"""
    files = ['Sample Report.pdf', 'Thermal Images.pdf']
    missing = [f for f in files if not os.path.exists(f)]
    return missing

def main():
    print("="*60)
    print("DDR GENERATION SYSTEM - SETUP VERIFICATION")
    print("="*60)
    print()
    
    all_good = True
    
    # Check 1: Virtual Environment
    print("1. Checking virtual environment...")
    if check_virtual_env():
        print("   ✅ Running in virtual environment")
    else:
        print("   ⚠️  Not in virtual environment")
        print("      Run: .\\venv\\Scripts\\activate")
        all_good = False
    print()
    
    # Check 2: Packages
    print("2. Checking required packages...")
    missing = check_packages()
    if not missing:
        print("   ✅ All packages installed")
    else:
        print(f"   ❌ Missing packages: {', '.join(missing)}")
        print("      Run: pip install -r requirements.txt")
        all_good = False
    print()
    
    # Check 3: .env file
    print("3. Checking .env configuration...")
    if check_env_file():
        print("   ✅ .env file exists")
        # Check if API key is set
        from dotenv import load_dotenv
        load_dotenv()
        api_key = os.getenv('GROQ_API_KEY')
        if api_key and api_key != 'your_groq_api_key_here':
            print("   ✅ GROQ_API_KEY is configured")
        else:
            print("   ⚠️  GROQ_API_KEY not set or using example value")
            print("      Get key from: https://console.groq.com")
            all_good = False
    else:
        print("   ❌ .env file not found")
        print("      Copy .env.example to .env and add your API key")
        all_good = False
    print()
    
    # Check 4: Input files
    print("4. Checking input PDF files...")
    missing_pdfs = check_pdf_files()
    if not missing_pdfs:
        print("   ✅ All input PDFs present")
    else:
        print(f"   ⚠️  Missing PDFs: {', '.join(missing_pdfs)}")
        print("      These files should be in the project root")
    print()
    
    # Check 5: Output directory
    print("5. Checking output directory...")
    if not os.path.exists('output'):
        os.makedirs('output')
        print("   ✅ Created output directory")
    else:
        print("   ✅ Output directory exists")
    print()
    
    # Final verdict
    print("="*60)
    if all_good:
        print("✅ SETUP COMPLETE - Ready to run!")
        print()
        print("Run the system with:")
        print("   python main.py")
    else:
        print("⚠️  SETUP INCOMPLETE - Please fix the issues above")
    print("="*60)

if __name__ == "__main__":
    main()
