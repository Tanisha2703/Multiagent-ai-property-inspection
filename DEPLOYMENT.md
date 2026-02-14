# 🚀 Deployment Guide - Streamlit Cloud

## Prerequisites

- ✅ GitHub repository (already done!)
- ✅ Streamlit Cloud account (free at https://streamlit.io/cloud)
- ✅ Groq API key

---

## Step-by-Step Deployment

### 1. Sign Up for Streamlit Cloud

1. Go to https://streamlit.io/cloud
2. Click "Sign up" or "Get started"
3. Sign in with your GitHub account
4. Authorize Streamlit to access your repositories

### 2. Deploy Your App

1. Click "New app" button
2. Select your repository: `Tanisha2703/Multiagent-ai-property-inspection`
3. Set the branch: `main`
4. Set the main file path: `app.py`
5. Click "Deploy!"

### 3. Configure Secrets (IMPORTANT!)

Before the app works, you need to add your API key:

1. Go to your app's dashboard
2. Click on "⚙️ Settings" (or the three dots menu)
3. Select "Secrets"
4. Add your secret in TOML format:

```toml
GROQ_API_KEY = "gsk_your_actual_api_key_here"
```

5. Click "Save"
6. The app will automatically restart

### 4. Wait for Deployment

- First deployment takes 2-5 minutes
- Streamlit will install all dependencies
- You'll see build logs in real-time

### 5. Access Your App

Once deployed, you'll get a URL like:
```
https://your-app-name.streamlit.app
```

Share this URL with anyone!

---

## Troubleshooting

### Error: "Unable to deploy - not connected to GitHub"

**Solution:**
1. Make sure you've pushed your code to GitHub
2. Refresh the Streamlit Cloud page
3. Try disconnecting and reconnecting your GitHub account
4. Verify the repository exists: https://github.com/Tanisha2703/Multiagent-ai-property-inspection

### Error: "GROQ_API_KEY not found"

**Solution:**
1. Go to app Settings → Secrets
2. Add your API key in TOML format:
   ```toml
   GROQ_API_KEY = "gsk_your_key_here"
   ```
3. Save and wait for restart

### Error: "Module not found"

**Solution:**
- Check `requirements.txt` is in repository root
- Verify all dependencies are listed
- Check build logs for specific missing packages

### Error: "App is taking too long"

**Solution:**
- First deployment is slow (2-5 minutes)
- Subsequent updates are faster
- Check if there are any errors in logs

### Error: "PDF processing fails"

**Solution:**
- `packages.txt` file should be in repository root
- Contains system dependencies for PyMuPDF
- Streamlit will install these automatically

---

## Configuration Files

### Required Files (Already Created)

1. **app.py** - Main Streamlit application
2. **requirements.txt** - Python dependencies
3. **packages.txt** - System dependencies (for PyMuPDF)
4. **.streamlit/config.toml** - Streamlit configuration
5. **.streamlit/secrets.toml.example** - Example secrets file

### File Structure for Deployment

```
Multiagent-ai-property-inspection/
├── app.py                          # ✅ Main app
├── requirements.txt                # ✅ Dependencies
├── packages.txt                    # ✅ System packages
├── .streamlit/
│   ├── config.toml                # ✅ Config
│   └── secrets.toml.example       # ✅ Example
├── agents/                         # ✅ AI agents
├── models/                         # ✅ Data models
├── utils/                          # ✅ Utilities
└── ... (other files)
```

---

## Environment Variables

### Local Development (.env file)
```bash
GROQ_API_KEY=gsk_your_key_here
```

### Streamlit Cloud (Secrets)
```toml
GROQ_API_KEY = "gsk_your_key_here"
```

**Note:** The app automatically detects which environment it's running in!

---

## Updating Your Deployed App

### Method 1: Push to GitHub (Automatic)

```bash
# Make changes to your code
git add .
git commit -m "Update: description of changes"
git push origin main
```

Streamlit Cloud will automatically detect changes and redeploy!

### Method 2: Manual Redeploy

1. Go to your app on Streamlit Cloud
2. Click "⚙️ Settings"
3. Click "Reboot app"

---

## Resource Limits (Free Tier)

Streamlit Cloud free tier includes:
- ✅ 1 GB RAM
- ✅ 1 CPU core
- ✅ Unlimited apps (public)
- ✅ Automatic HTTPS
- ✅ Custom domain support

**Note:** This is sufficient for the DDR generation system!

---

## Security Best Practices

### ✅ DO:
- Store API keys in Streamlit Secrets
- Use `.gitignore` to exclude `.env` files
- Keep secrets in Streamlit Cloud dashboard
- Use HTTPS (automatic on Streamlit Cloud)

### ❌ DON'T:
- Commit API keys to GitHub
- Share your secrets.toml file
- Hardcode credentials in code
- Expose sensitive data in logs

---

## Monitoring Your App

### View Logs
1. Go to your app on Streamlit Cloud
2. Click "Manage app"
3. View real-time logs

### Check Usage
1. Go to Streamlit Cloud dashboard
2. View app analytics
3. Monitor resource usage

---

## Custom Domain (Optional)

### Add Custom Domain

1. Go to app Settings
2. Click "Custom domain"
3. Add your domain (e.g., `reports.yourdomain.com`)
4. Follow DNS configuration instructions
5. Wait for SSL certificate (automatic)

---

## Backup & Recovery

### Backup Your Code
- ✅ Code is on GitHub (automatic backup)
- ✅ Secrets are in Streamlit Cloud
- ✅ Download secrets from dashboard if needed

### Recovery
1. Code: Clone from GitHub
2. Secrets: Re-add in Streamlit Cloud
3. Redeploy: Push to GitHub or manual redeploy

---

## Cost Optimization

### Free Tier Tips
- ✅ Use Groq free tier (30 req/min)
- ✅ Optimize code for efficiency
- ✅ Cache results when possible
- ✅ Monitor usage regularly

### If You Need More
- Upgrade Streamlit Cloud plan
- Upgrade Groq API plan
- Deploy on your own server

---

## Alternative Deployment Options

### 1. Heroku
```bash
# Create Procfile
echo "web: streamlit run app.py" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
```

### 2. Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

### 3. AWS/GCP/Azure
- Use container services
- Deploy as web app
- Configure environment variables

---

## Support

### Streamlit Cloud Issues
- Documentation: https://docs.streamlit.io/streamlit-community-cloud
- Community: https://discuss.streamlit.io
- Status: https://status.streamlit.io

### App-Specific Issues
- GitHub Issues: https://github.com/Tanisha2703/Multiagent-ai-property-inspection/issues
- Check logs in Streamlit Cloud dashboard
- Review error messages carefully

---

## Quick Checklist

Before deploying:
- [ ] Code pushed to GitHub
- [ ] `app.py` in repository root
- [ ] `requirements.txt` present
- [ ] `packages.txt` present
- [ ] `.streamlit/config.toml` present
- [ ] Groq API key ready
- [ ] Streamlit Cloud account created

During deployment:
- [ ] Repository connected
- [ ] Branch set to `main`
- [ ] Main file set to `app.py`
- [ ] Secrets configured
- [ ] Build completed successfully

After deployment:
- [ ] App loads without errors
- [ ] Can upload PDFs
- [ ] Report generation works
- [ ] Download works
- [ ] Share URL with others

---

## 🎉 You're Ready!

Your app is now deployed and accessible worldwide!

**Your App URL**: https://your-app-name.streamlit.app

Share it with anyone who needs to generate property inspection reports! 🚀
