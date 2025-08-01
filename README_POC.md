# ContinuumOS Legacy-Sphere - Proof of Concept

## 🎯 POC Goals
1. Chat with Ron Leavitt's 100-year family history using Ollama
2. Process 5 PDF heritage artifacts into a searchable legacy stack
3. Generate basic podcasts from conversations
4. Deploy frontend to Vercel while running backend locally

## 📋 Prerequisites

1. **Node.js 18+** - [Download](https://nodejs.org/)
2. **Python 3.10+** - [Download](https://python.org/)
3. **Ollama** - [Download](https://ollama.ai/)
   ```bash
   # After installing Ollama, pull required models:
   ollama pull llama3
   ollama pull nomic-embed-text
   ```
4. **FFmpeg** - For audio conversion (optional for podcasts)

## 🚀 Quick Start

### Step 1: Place Your PDFs
Copy your 5 PDF files to:
```
backend/data/ron_leavitt_legacy_stack/
```

### Step 2: Backend Setup (Terminal 1)
```bash
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Ingest PDFs into vector database (run once)
python ingest.py

# Start the FastAPI server
uvicorn server:app --reload --port 7860
```

Backend will be running at: http://localhost:7860

### Step 3: Frontend Setup (Terminal 2)
```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend will be running at: http://localhost:3000

## 🎨 Using the POC

1. **Open browser**: http://localhost:3000
2. **Ask questions** like:
   - "Tell me about the gas leak incident in 7th grade"
   - "What was Grandpa doing during World War II?"
   - "Describe the family road trip in 1964"
3. **Generate podcasts**: Click "Make Podcast" to create audio from any topic

## 🚢 Deploying to Vercel

### Frontend Deployment
1. Push code to GitHub
2. Connect GitHub repo to Vercel
3. Set environment variable in Vercel:
   ```
   BACKEND_URL=https://your-ngrok-url.ngrok.io
   ```

### Backend Exposure (for Vercel)
Since backend runs locally, use ngrok:
```bash
# Install ngrok
npm install -g ngrok

# Expose your local backend
ngrok http 7860
```

Copy the ngrok URL and update Vercel's BACKEND_URL environment variable.

## 📁 Project Structure
```
ProjectContinuum/
├── frontend/          # Next.js app (Vercel)
│   └── src/pages/    # UI components
├── backend/           # Python FastAPI (Local)
│   ├── ingest.py     # PDF processor
│   ├── server.py     # API endpoints
│   └── data/         # Your family PDFs
└── README_POC.md     # This file
```

## 🔧 Troubleshooting

**"Ollama not found"**
- Make sure Ollama is running: `ollama serve`
- Check models are installed: `ollama list`

**"No PDFs found"**
- Ensure PDFs are in: `backend/data/ron_leavitt_legacy_stack/`
- Re-run: `python ingest.py`

**"Connection refused"**
- Backend running? Check port 7860
- Frontend `.env.local` has correct BACKEND_URL?

## 🎉 Success Checklist
- [ ] Ollama running with llama3 model
- [ ] PDFs placed in correct folder
- [ ] Backend ingested PDFs successfully
- [ ] Frontend connects to backend
- [ ] Can ask questions and get responses
- [ ] Podcast generation works (optional)

## 📝 Notes
- This is a POC - not production ready
- Ollama must stay running for chat to work
- PDFs are processed once and cached locally
- Podcasts use basic TTS (not NotebookLM quality yet)

---
Built with ❤️ for preserving family memories