# ProjectContinuum Structure Backup Reference
Generated: 2025-07-25

## Project Root Location
`C:\Users\carls\OneDrive\Desktop\ProjectContinuum`

## Directory Structure

### Root Level Files
- `ContinuumOS Homepage.html` - Main homepage
- `ContinuumOS_Daily_Checklist.html` - Daily task checklist
- `ContinuumOS_Project_Dashboard.html` - Project overview dashboard
- `ContinuumOS_Prototype_Weekend_Guide.html` - Weekend development guide
- `ContinuumOS_Skills_Assessment.html` - Team skills assessment
- `ContinuumOS_Tech_Roadmap.html` - Technical roadmap
- `ContinuumOS_Tools_Setup.html` - Tools setup guide
- `Project Continuum notes.txt` - Extensive project notes and vision
- `context drop.txt` - Legacy stack architecture description

### Subdirectories

#### 1. ContinuumOS demo/
Frontend demo files:
- `ContinuumOS.html` - Main demo interface
- `README.txt` - Demo documentation
- `ancestors.json` - Sample ancestor data (Grandpa Joe, Grandma Mary)
- `conversations.json` - Pre-loaded conversation samples
- `dashboard.html` - User dashboard
- `memories.json` - Sample memory data

#### 2. work steps and needs/
Planning and documentation:
- Various HTML files with implementation steps
- Workflow documentation

### Audio Files
- `ContinuumOS 60-second Investor Pitch 191124 2055.mp3`
- `Living History 60-second pitch 191124 2124.mp3`

## Project Type
- **Frontend**: HTML/CSS with inline JavaScript
- **Backend**: Not yet implemented (planned for API integration)
- **Current State**: Static demo ready for deployment

## Technology Stack (Planned)
- **Frontend**: HTML, CSS, JavaScript (currently), Next.js (planned)
- **Backend**: Node.js/Python (planned)
- **AI/ML**: OpenAI GPT-4, ElevenLabs (voice), Pinecone (vector DB)
- **Database**: Neo4j (graph), PostgreSQL
- **Deployment**: Vercel, GitHub

## Key Files for Development

### Frontend Entry Points
- Main Demo: `/ContinuumOS demo/ContinuumOS.html`
- Dashboard: `/ContinuumOS demo/dashboard.html`
- Homepage: `/ContinuumOS Homepage.html`

### Data Files
- Ancestors: `/ContinuumOS demo/ancestors.json`
- Conversations: `/ContinuumOS demo/conversations.json`
- Memories: `/ContinuumOS demo/memories.json`

### Documentation
- Project Vision: `/Project Continuum notes.txt`
- Architecture: `/context drop.txt`
- Demo Guide: `/ContinuumOS demo/README.txt`

## Current Development Phase
Phase 3: Deployment (out of 5 phases)
- Phase 1: Planning ✓
- Phase 2: Demo Creation ✓
- Phase 3: Deployment ← CURRENT
- Phase 4: API Integration
- Phase 5: Beta Launch

## Quick Reference Commands
When you need to access the project after restart:
```bash
# Navigate to project
cd /mnt/c/Users/carls/OneDrive/Desktop/ProjectContinuum

# List all files
ls -la

# View demo files
ls -la "ContinuumOS demo/"

# Read main demo file
cat "ContinuumOS demo/ContinuumOS.html"
```

## Important Notes
- No package.json yet (not a Node project currently)
- No .git directory yet (needs GitHub repo creation)
- All JavaScript is inline in HTML files
- Demo uses localStorage for data persistence
- Sample data pre-loaded for Grandpa Joe and Grandma Mary

This backup reference should help you quickly locate all project files after system restart.