# 🌐 Web Interface Guide

## Overview

The DDR Generation System now includes a user-friendly web interface built with Streamlit. Upload your PDF files through your browser and download the generated DDR report!

## Features

✨ **Easy to Use**
- Drag-and-drop file upload
- Real-time progress tracking
- Instant download of generated reports

📊 **Comprehensive Results**
- View generated DDR report
- Check quality validation
- Review merged data analysis
- See conflicts and missing information

🎨 **Clean Interface**
- Modern, responsive design
- Clear status indicators
- Organized tabs for different views

## Quick Start

### Option 1: Using Run Script (Easiest)

**Windows:**
```bash
run_web_interface.bat
```

**Linux/Mac:**
```bash
chmod +x run_web_interface.sh
./run_web_interface.sh
```

### Option 2: Manual Start

```bash
# Activate virtual environment
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Run Streamlit app
streamlit run app.py
```

### Access the Interface

The web interface will automatically open in your browser at:
```
http://localhost:8501
```

If it doesn't open automatically, copy the URL from the terminal.

## How to Use

### Step 1: Upload Files

1. **Upload Inspection Report**
   - Click "Browse files" in the left column
   - Select your inspection PDF
   - Wait for upload confirmation

2. **Upload Thermal Report**
   - Click "Browse files" in the right column
   - Select your thermal PDF
   - Wait for upload confirmation

### Step 2: Generate Report

1. Click the **"🚀 Generate DDR Report"** button
2. Watch the progress bar:
   - Step 1: Reading PDF files
   - Step 2: Extracting data with AI
   - Step 3: Merging and validating
   - Step 4: Generating DDR
   - Step 5: Quality validation

### Step 3: Review Results

The interface shows three tabs:

#### 📄 Generated Report Tab
- View the complete DDR report
- Formatted in markdown
- Click **"⬇️ Download DDR Report"** to save

#### 📊 Quality Check Tab
- Validation status (Pass/Fail)
- Clarity score (out of 10)
- Hallucination check result
- Quality issues (if any)
- Suggestions for improvement

#### 🔍 Merged Data Tab
- Total observations count
- Detected conflicts
- Missing information
- Expandable list of all observations

### Step 4: Download Report

Click the **"⬇️ Download DDR Report"** button to save the generated report as a markdown file.

## Interface Layout

```
┌─────────────────────────────────────────────────────────┐
│                 DDR Report Generator                    │
│         Multi-Agent AI System for Property              │
│              Diagnostic Reports                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────────┐  ┌──────────────────┐           │
│  │ Upload Inspection│  │ Upload Thermal   │           │
│  │     Report       │  │     Report       │           │
│  └──────────────────┘  └──────────────────┘           │
│                                                         │
│         ┌──────────────────────────┐                   │
│         │ 🚀 Generate DDR Report   │                   │
│         └──────────────────────────┘                   │
│                                                         │
│  ┌─────────────────────────────────────────────────┐  │
│  │ Results:                                        │  │
│  │ [Generated Report] [Quality Check] [Merged Data]│  │
│  └─────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

## Sidebar Information

The sidebar shows:

### About Section
- How the system works
- Technology used
- Step-by-step process

### System Status
- ✅ System Ready (green)
- ❌ System Error (red)
- Current model information

## Metrics Display

After generation, you'll see:

| Metric | Description |
|--------|-------------|
| 📊 Observations | Number of issues extracted |
| ⚠️ Conflicts | Contradictions detected |
| ℹ️ Missing Info | Incomplete data items |
| ✅ Quality | Validation status |

## Troubleshooting

### Issue: "System Error: API key not configured"

**Solution:**
1. Make sure `.env` file exists
2. Check `GROQ_API_KEY` is set correctly
3. Restart the web interface

### Issue: "Connection refused" or "Cannot connect"

**Solution:**
```bash
# Stop any running instances
# Press Ctrl+C in terminal

# Restart the interface
streamlit run app.py
```

### Issue: Upload fails or hangs

**Solution:**
- Check PDF file is not corrupted
- Ensure file size is reasonable (<50MB)
- Try refreshing the page
- Check internet connection (for API calls)

### Issue: Generation takes too long

**Possible causes:**
- Large PDF files (processing takes longer)
- Slow internet connection
- Groq API rate limits

**Solution:**
- Wait patiently (usually 30-60 seconds)
- Check Groq API status
- Try again after a minute

### Issue: Page won't load

**Solution:**
```bash
# Clear Streamlit cache
streamlit cache clear

# Restart
streamlit run app.py
```

## Configuration

### Change Port

Default port is 8501. To change:

```bash
streamlit run app.py --server.port 8080
```

### Run on Network

To access from other devices on your network:

```bash
streamlit run app.py --server.address 0.0.0.0
```

Then access via: `http://your-ip-address:8501`

### Disable Auto-Open Browser

```bash
streamlit run app.py --server.headless true
```

## Advanced Usage

### Custom Configuration

Create `.streamlit/config.toml`:

```toml
[server]
port = 8501
headless = false
enableCORS = false

[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"
```

### Environment Variables

The web interface uses the same `.env` file:

```bash
GROQ_API_KEY=your_key_here
```

## Security Notes

### Local Use Only (Default)

By default, the interface only accepts connections from localhost (your computer).

### Network Access

If you enable network access (`--server.address 0.0.0.0`):
- ⚠️ Anyone on your network can access it
- ⚠️ Don't expose to public internet
- ⚠️ Use firewall rules if needed

### File Upload Security

- Files are processed in temporary directories
- Files are deleted after processing
- No files are permanently stored
- API key is never exposed to browser

## Performance Tips

### For Faster Processing

1. **Optimize PDFs**
   - Compress large PDFs before upload
   - Remove unnecessary pages
   - Use text-based PDFs (not scanned images)

2. **Network**
   - Use stable internet connection
   - Close other bandwidth-heavy applications

3. **System Resources**
   - Close unnecessary browser tabs
   - Ensure sufficient RAM available

## Comparison: CLI vs Web Interface

| Feature | CLI (`main.py`) | Web Interface (`app.py`) |
|---------|-----------------|--------------------------|
| **Ease of Use** | Technical users | Everyone |
| **File Upload** | Manual file placement | Drag-and-drop |
| **Progress** | Terminal output | Visual progress bar |
| **Results** | Files in output/ | In-browser view + download |
| **Batch Processing** | Easy to script | One at a time |
| **Automation** | Yes | No |
| **Remote Access** | SSH required | Browser-based |

## Use Cases

### Web Interface is Best For:
- ✅ Non-technical users
- ✅ Quick one-off reports
- ✅ Visual review of results
- ✅ Demonstrations
- ✅ Client presentations

### CLI is Best For:
- ✅ Batch processing
- ✅ Automation/scripting
- ✅ Integration with other tools
- ✅ Server deployments
- ✅ Advanced users

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl + R` | Rerun the app |
| `Ctrl + C` | Stop the server (in terminal) |
| `F5` | Refresh page |

## Browser Compatibility

Tested and working on:
- ✅ Chrome/Edge (Recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Opera

## Stopping the Interface

### Method 1: Terminal
Press `Ctrl + C` in the terminal where Streamlit is running

### Method 2: Close Terminal
Simply close the terminal window

### Method 3: Kill Process
```bash
# Find process
netstat -ano | findstr :8501  # Windows
lsof -i :8501                 # Linux/Mac

# Kill process
taskkill /PID <pid> /F        # Windows
kill -9 <pid>                 # Linux/Mac
```

## Deployment (Optional)

### Streamlit Cloud (Free)

1. Push code to GitHub
2. Go to https://streamlit.io/cloud
3. Connect your repository
4. Deploy!

**Note:** Add secrets in Streamlit Cloud dashboard:
- `GROQ_API_KEY` = your API key

### Docker (Advanced)

Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

Build and run:
```bash
docker build -t ddr-generator .
docker run -p 8501:8501 ddr-generator
```

## FAQ

**Q: Can I process multiple reports at once?**
A: The web interface processes one report at a time. Use the CLI for batch processing.

**Q: Where are my files stored?**
A: Files are processed in temporary directories and deleted immediately after.

**Q: Can I customize the interface?**
A: Yes! Edit `app.py` to modify the interface. Streamlit is very customizable.

**Q: Does it work offline?**
A: No, it requires internet connection for Groq API calls.

**Q: Can I use it on mobile?**
A: Yes! The interface is responsive and works on mobile browsers.

**Q: How do I update the interface?**
A: Pull latest code and restart: `git pull && streamlit run app.py`

## Support

For issues with the web interface:
1. Check this documentation
2. Review error messages in browser
3. Check terminal output for details
4. Verify API key is configured
5. Try the CLI version (`python main.py`) to isolate issues

---

**Ready to use the web interface?** Run `run_web_interface.bat` (Windows) or `./run_web_interface.sh` (Linux/Mac)! 🚀
