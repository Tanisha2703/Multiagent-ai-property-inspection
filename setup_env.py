"""Interactive script to create .env file"""
import os

def create_env_file():
    print("="*60)
    print("GROQ API KEY SETUP")
    print("="*60)
    print()
    print("To get your free API key:")
    print("1. Visit: https://console.groq.com")
    print("2. Sign up (free, no credit card)")
    print("3. Go to 'API Keys' section")
    print("4. Create new API key")
    print("5. Copy the key (starts with 'gsk_')")
    print()
    print("="*60)
    print()
    
    api_key = input("Paste your Groq API key here: ").strip()
    
    if not api_key:
        print("❌ No API key provided. Exiting.")
        return
    
    if not api_key.startswith('gsk_'):
        print("⚠️  Warning: API key should start with 'gsk_'")
        confirm = input("Continue anyway? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Cancelled.")
            return
    
    # Create .env file
    with open('.env', 'w') as f:
        f.write(f"# Groq API Configuration\n")
        f.write(f"GROQ_API_KEY={api_key}\n")
    
    print()
    print("="*60)
    print("✅ .env file created successfully!")
    print("="*60)
    print()
    print("Next steps:")
    print("1. Run: python verify_setup.py")
    print("2. Run: python main.py")
    print()

if __name__ == "__main__":
    if os.path.exists('.env'):
        print("⚠️  .env file already exists!")
        overwrite = input("Overwrite? (y/n): ").strip().lower()
        if overwrite != 'y':
            print("Cancelled.")
            exit()
    
    create_env_file()
