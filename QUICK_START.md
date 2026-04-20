# Quick Start Cheat Sheet - WBAI077-05
## For Complete Beginners

---

## 🎯 Most Important Commands

### Start Working (Do this EVERY time!)
```bash
cd cmn-practical
. cmn-env/bin/activate
```
You'll see `(cmn-env)` at the start of your prompt when it's working!

### Stop Working
```bash
deactivate
```

### Start Jupyter Lab
```bash
# Make sure environment is activated first!
jupyter lab
```
Your browser will open automatically.

---

## 📝 VS Code Quick Setup

1. **Open VS Code** → File → Open Folder → Select `cmn-practical`
2. **Install Python extension** (do this once)
3. **Select interpreter:** 
   - Click bottom-right where it shows Python version
   - Choose the one with `cmn-env` in the path
4. **Create a notebook:** New File → `my_notebook.ipynb`
5. **Run code:** Click the ▶️ button next to each cell

---

## 🧪 Test Everything Works
```bash
cd cmn-practical
. cmn-env/bin/activate
python verify_setup.py
```
Should say "ALL TESTS PASSED ✓✓✓"

---

## 📁 Where Things Go

```
cmn-practical/
├── project1/          ← Your first project
│   ├── data/         ← Put data files here
│   ├── notebooks/    ← Work here! (Jupyter notebooks)
│   ├── scripts/      ← Final clean Python scripts
│   └── figures/      ← Save plots here
├── project2/          ← Your second project
└── project3/          ← Your third project
```

**Golden Rule:** Always work in the correct project folder!

---

## 💡 Common Mistakes (and Fixes)

### ❌ "ModuleNotFoundError: No module named 'numpy'"
**Fix:** You forgot to activate your environment!
```bash
. cmn-env/bin/activate
```

### ❌ VS Code can't find Python packages
**Fix:** Wrong interpreter selected
- Ctrl+Shift+P → "Python: Select Interpreter"
- Choose the one with `cmn-env`

### ❌ Jupyter won't start
**Fix:** Environment not activated or not installed
```bash
. cmn-env/bin/activate
pip install jupyterlab
```

### ❌ Can't save/find files
**Fix:** Check where you are!
```bash
pwd                    # Shows current directory
cd cmn-practical       # Go to project folder
cd project1/notebooks  # Go to notebooks folder
```

---

## 🎓 Workflow for Each Project

### Step 1: Setup (First time for each project)
```bash
cd cmn-practical
. cmn-env/bin/activate
cd project1  # or project2, project3
```

### Step 2: Get Data
- Put data files in the `data/` folder
- NEVER modify original data files!

### Step 3: Start Exploring
```bash
# Option A: VS Code
code .  # Opens VS Code in current folder

# Option B: Jupyter Lab
jupyter lab
```

### Step 4: Create Your Notebook
- Use the template: `project_template.ipynb`
- Or create new: `analysis.ipynb`

### Step 5: Work!
1. Load data
2. Explore (plot everything!)
3. Preprocess
4. Analyze
5. Create figures
6. Save results

### Step 6: Clean Up
- Save important figures to `figures/`
- Export final code if needed
- Update the project README.md

---

## 🔍 Essential Python Snippets

### Load Data
```python
import pandas as pd
data = pd.read_csv('../data/myfile.csv')
```

### Plot Something
```python
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('My Plot')
plt.savefig('../figures/my_plot.png', dpi=150)
plt.show()
```

### Check Array Shape
```python
print(data.shape)  # Always do this!
```

### Basic Statistics
```python
print(data.describe())
```

---

## 📞 Getting Help

### During Work Sessions
- Instructor is available in office: BB 5161.0302
- Email: l.vortmann@rug.nl

### Online Resources
- **SETUP_GUIDE.md** - Full detailed guide
- **Python Setup Guide.pdf** - Official course guide
- **Course Syllabus.pdf** - All course info
- Brightspace - Course materials and assignments

### Debugging
1. Read the error message carefully
2. Check if environment is activated
3. Check your file paths
4. Google the error (seriously!)
5. Ask a classmate
6. Ask instructor during work sessions

---

## ✅ Pre-Flight Checklist (Before Each Session)

- [ ] Environment activated? (see `(cmn-env)` in terminal)
- [ ] In the right folder? (`pwd` to check)
- [ ] Can import packages? (`import numpy as np`)
- [ ] Know which project I'm working on?
- [ ] Have my data ready?
- [ ] Know my research question?

---

## 🚀 You're Ready!

**Remember:**
1. Always activate the environment first
2. Work in the correct project folder
3. Save your work frequently
4. Plot your data early and often
5. Ask for help when stuck

Good luck! 🧠💻
