# Quick Deployment Checklist

## ☑️ Pre-Deployment (Do Once)

### GitHub Setup
- [ ] Create GitHub account if needed
- [ ] Create new repository named `revised-ai`
- [ ] Have your GitHub username ready

### API Keys Ready
- [ ] Have your SambaNova API key copied
- [ ] Have GitHub username ready
- [ ] Have Render account (deploy with GitHub)
- [ ] Have Streamlit account (deploy with GitHub)

---

## 📤 Step 1: Push to GitHub (5 minutes)

Run in PowerShell in your project folder:

```powershell
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/revised-ai.git
git push -u origin main
```

**✓ Test**: Visit `https://github.com/YOUR_USERNAME/revised-ai` - see your code?

---

## 🔧 Step 2: Deploy Backend on Render (5 minutes)

1. Go to [render.com](https://render.com) → Sign up with GitHub
2. Click **+** → **New Web Service**
3. Connect your `revised-ai` repository
4. Settings:
   - Name: `revised-ai-api`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn -w 4 -b 0.0.0.0:$PORT wsgi:app`
5. **Environment Variables** (click Add):
   - `SAMBANOVA_API_KEY` = your key
   - `CACHE_EXPIRATION` = `3600`
6. Click **Create Web Service**
7. Wait 2-3 minutes for "Live" status

**✓ Test**: Visit your backend URL - should show JSON error (that's okay!)

**⭐ COPY YOUR BACKEND URL**: `https://revised-ai-api-xxx.onrender.com`

---

## 🎨 Step 3: Deploy Frontend on Streamlit (3 minutes)

1. Go to [cloud.streamlit.app](https://cloud.streamlit.app) → Sign in with GitHub
2. Click **Create app**
3. Settings:
   - Repository: `YOUR_USERNAME/revised-ai`
   - Branch: `main`
   - Main file path: `frontend/app.py`
4. Click **Deploy**
5. Wait 1-2 minutes

**After deployment:**
1. Click **⚙️** (settings) → **Secrets**
2. Add this line (paste your Render URL):
   ```
   BACKEND_URL="https://revised-ai-api-xxx.onrender.com"
   ```
3. Save

**✓ Test**: Go to app URL → Select "Explain" → Type "photosynthesis" → Click Submit

---

## ✅ Final Checks

- [ ] Backend is "Live" on Render dashboard
- [ ] Frontend deployed on Streamlit Cloud
- [ ] `BACKEND_URL` secret added to Streamlit
- [ ] Can submit a topic in the app
- [ ] Get an explanation back

**🎉 You're live!** Share your Streamlit app URL with others!

---

## 📝 Update Your Code Later

After making changes locally:

```powershell
git add .
git commit -m "Fixed bug" 
git push origin main
```

**Auto-deploys in 1-2 minutes!** No manual redeploy needed.

---

## 🆘 Common Issues

| Problem | Solution |
|---------|----------|
| "Connection refused" | Wait 30 seconds, backend might be starting |
| "Rate limit" | Wait 5 minutes, SambaNova has free limits |
| "Can't find repo" | Make sure repo is public on GitHub |
| Backend not responding | Check Render dashboard status |
| Frontend shows error | Check `BACKEND_URL` in Streamlit Secrets |
| App says "Coming Soon" doesn't work | That's normal - it's a placeholder! |

---

## 🔗 Your Final Links

```
GitHub:    https://github.com/YOUR_USERNAME/revised-ai
Backend:   https://revised-ai-api-you_number.onrender.com
Frontend:  https://revised-ai-you_number.streamlit.app
```

Save these for later! 🎉
