# Complete Deployment Guide - Step by Step

## Phase 1: GitHub Setup

### Step 1: Create GitHub Repository

1. Go to [github.com](https://github.com)
2. Sign in to your account (create one if needed)
3. Click **+** (top right) → **New repository**
4. Fill in:
   - **Repository name**: `revised-ai` (or your choice)
   - **Description**: "AI-powered study assistant"
   - **Public** (select this)
   - Check: **Add a README file**
   - Check: **Add .gitignore** → select Python
5. Click **Create repository**

### Step 2: Push Your Code to GitHub

Open PowerShell in your project folder (N:\projects\Revised AI):

```powershell
# Initialize git (one time)
git init

# Configure git with your details
git config user.name "Your Name"
git config user.email "your.email@gmail.com"

# Add all files
git add .

# Commit
git commit -m "Initial project commit"

# Rename branch to main (if not already)
git branch -M main

# Add remote (replace USERNAME with your GitHub username)
git remote add origin https://github.com/USERNAME/revised-ai.git

# Push to GitHub
git push -u origin main
```

**Warning**: Do NOT commit `.env` file! It should be in `.gitignore` (already done).

**Check if successful**: Go to [github.com/USERNAME/revised-ai](https://github.com/USERNAME/revised-ai) - you should see your code there.

---

## Phase 2: Deploy Backend API on Render

### Step 1: Create Render Account

1. Go to [render.com](https://render.com)
2. Click **Sign up**
3. Use your GitHub account (select **Continue with GitHub**)
4. Authorize Render to access your GitHub

### Step 2: Deploy Backend Service

1. In Render dashboard, click **+** → **New Web Service**
2. Select **Connect a Repository**
3. Find `revised-ai` in the list and click **Connect**
4. If repo doesn't appear:
   - Click **Configure account**
   - Grant access to your GitHub repo
   - Try again

### Step 3: Configure Service Settings

Fill in these fields exactly:

| Field | Value |
|-------|-------|
| **Name** | `revised-ai-api` |
| **Environment** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn -w 4 -b 0.0.0.0:$PORT wsgi:app` |
| **Instance Type** | `Free` |

### Step 4: Add Environment Variables

In the same form, scroll down to **Environment**:

Click **Add Environment Variable** twice:

**Variable 1:**
```
SAMBANOVA_API_KEY
[your_actual_api_key_here]
```

**Variable 2:**
```
CACHE_EXPIRATION
3600
```

### Step 5: Deploy

Click **Create Web Service**

**Wait 2-3 minutes for deployment**

✅ **Success indicators:**
- Status shows "Live"
- You see a URL like: `https://revised-ai-api-xxx.onrender.com`

**Save this URL** - you'll need it for the frontend!

---

## Phase 3: Deploy Frontend on Streamlit Cloud

### Step 1: Create Streamlit Account

1. Go to [cloud.streamlit.app](https://cloud.streamlit.app)
2. Click **Sign up** or **Sign in with GitHub**
3. Authorize with your GitHub account

### Step 2: Deploy App

1. Click **Create app**
2. Fill in:
   - **Repository**: `USERNAME/revised-ai`
   - **Branch**: `main`
   - **Main file path**: `frontend/app.py`
3. Click **Deploy**

**Wait 1-2 minutes** for deployment to complete

### Step 3: Add Backend URL to Streamlit

Once deployed, you'll see your app at a URL like: `https://revised-ai-xxxx.streamlit.app`

1. Click **⚙️ Settings** (top right)
2. Click **Secrets**
3. Paste this (replace URL with your Render backend URL):

```
BACKEND_URL="https://revised-ai-api-xxx.onrender.com"
```

**Get your Render URL** from Phase 2, Step 5

4. Save

**App will auto-refresh** with the new settings

---

## Phase 4: Test Everything

### Test Backend

1. Go to your Render URL: `https://revised-ai-api-xxx.onrender.com/`
2. You should see a JSON error (that's okay - it means server is running)

### Test Frontend

1. Go to your Streamlit URL: `https://revised-ai-xxxx.streamlit.app`
2. Select "Explain" tab
3. Type a topic: **"photosynthesis"**
4. Click **Submit**
5. Wait for response (may take 10-15 seconds first time)

✅ **If it works**: You see an explanation from the AI

❌ **If it fails**: Check troubleshooting section below

---

## Troubleshooting

### "Connection refused" or Backend not responding

**Solution:**
1. Check Render dashboard - is service running? (status should say "Live")
2. Visit backend URL directly in browser
3. Check if `SAMBANOVA_API_KEY` is set in Render (⚙️ Settings → Environment)

### "Rate limit exceeded" error

**This is normal** - SambaNova free tier has limits. Solutions:
- Wait a few minutes between requests
- Upgrade your SambaNova plan
- Use caching (already implemented)

### Frontend can't connect to backend

**Solution:**
1. Check the `BACKEND_URL` in Streamlit Secrets (⚙️ Settings → Secrets)
2. Make sure it exactly matches your Render URL (no trailing slash)
3. Click **Rerun** in Streamlit or refresh the page

### App shows "Error: connection timeout"

**Solution:**
1. Backend might be starting up (free tier takes 30+ seconds first request)
2. Wait 1 minute
3. Try again

---

## Important Links

| Service | URL |
|---------|-----|
| Your GitHub | `https://github.com/USERNAME/revised-ai` |
| Render Dashboard | `https://dashboard.render.com` |
| Streamlit Cloud | `https://share.streamlit.io` |
| Live Backend | `https://revised-ai-api-xxx.onrender.com` |
| Live Frontend | `https://revised-ai-xxxx.streamlit.app` |

---

## Useful Commands

### Update code after changes

```powershell
# After making changes, run:
git add .
git commit -m "Your change description"
git push origin main
```

**Both Render and Streamlit auto-deploy** when you push to GitHub!

### View logs

**Streamlit**: Click **Manage app** → **Logs**
**Render**: Click service → **Logs** tab

---

## Cost Summary

| Service | Free Tier | Cost |
|---------|-----------|------|
| Render Backend | Yes (auto-sleeps) | $0/month |
| Streamlit Frontend | Yes (unlimited) | $0/month |
| GitHub | Free public repos | $0/month |
| SambaNova API | Limited free tier | $0-20/month |
| **Total** | | **$0-20/month** |

---

## Next Steps After Deployment

1. ✅ Share your live app with others
2. Add custom domain (optional, both support it)
3. Monitor logs for errors
4. Update `.env` if API quotas change
