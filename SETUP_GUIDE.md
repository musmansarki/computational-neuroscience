# Complete Setup Guide for WBAI077-05
## Computational Methods in Neuroscience

Welcome! This guide will walk you through setting up your Python environment step by step.

---

## ✅ What We Just Set Up

Your environment is now ready! Here's what was installed:

### 📁 Folder Structure
```
cmn-practical/
├── cmn-env/              # Your Python virtual environment (don't edit this)
├── project1/             # For your first project
│   ├── data/            # Put raw data here
│   ├── notebooks/       # Jupyter notebooks for exploration
│   ├── scripts/         # Clean Python scripts
│   └── figures/         # Save your plots here
├── project2/             # For your second project
│   └── (same structure)
├── project3/             # For your third project
│   └── (same structure)
├── verify_setup.py       # Script to test your setup
├── requirements.txt      # List of installed packages
└── test_plot.png         # Test plot (proof it works!)
```

### 📦 Installed Packages
- **numpy** (2.4.2) - Arrays and numerical operations
- **scipy** (1.17.0) - Signal processing, statistics
- **pandas** (3.0.0) - Data tables and manipulation
- **matplotlib** (3.10.8) - Basic plotting
- **seaborn** (0.13.2) - Statistical visualizations
- **mne** (1.11.0) - EEG/MEG analysis
- **scikit-learn** (1.8.0) - Machine learning
- **statsmodels** (0.14.6) - Statistical modeling
- **jupyterlab** (4.5.3) - Interactive notebooks

---

## 🚀 How to Use This Setup

### Option 1: Using VS Code (Recommended for Beginners)

#### Step 1: Open VS Code
1. Download and install VS Code from https://code.visualstudio.com/
2. Open VS Code

#### Step 2: Open Your Project Folder
1. File → Open Folder
2. Navigate to and select `cmn-practical/`
3. Click "Open"

#### Step 3: Install Python Extension
1. Click the Extensions icon (four squares) on the left sidebar
2. Search for "Python"
3. Install the official Python extension by Microsoft

#### Step 4: Select Your Virtual Environment
1. Open any Python file (or create a new one: `test.py`)
2. Look at the bottom-right corner of VS Code
3. Click where it says the Python version
4. Select the option that includes `cmn-env` (should be `./cmn-env/bin/python`)
5. VS Code will now use your course environment!

#### Step 5: Create a Jupyter Notebook
1. Create a new file: `test_notebook.ipynb` in the `project1/notebooks/` folder
2. VS Code will ask to install Jupyter extension - click "Install"
3. Click "+ Code" to add a code cell
4. Type this test code:
```python
import numpy as np
import matplotlib.pyplot as plt

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot it
plt.figure(figsize=(10, 4))
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('My First Plot!')
plt.grid(True)
plt.show()
```
5. Click the ▶️ button to run the cell
6. You should see a sine wave plot!

### Option 2: Using Jupyter Lab (Browser-Based)

#### Step 1: Start Jupyter Lab
In your terminal:
```bash
cd cmn-practical
source cmn-env/bin/activate  # (or `. cmn-env/bin/activate`)
jupyter lab
```

#### Step 2: Navigate and Create
1. Your browser will open with Jupyter Lab
2. Navigate to `project1/notebooks/`
3. Click the "+" button to create a new notebook
4. Run the test code from above

---

## 📝 Quick Reference Commands

### Activate Your Environment
**Every time you start working, activate your environment first!**
```bash
cd cmn-practical
source cmn-env/bin/activate
# or use the short version:
. cmn-env/bin/activate
```

You'll know it's activated when you see `(cmn-env)` at the start of your terminal prompt.

### Verify Everything Still Works
```bash
python verify_setup.py
```

### Start Jupyter Lab
```bash
jupyter lab
```

### Deactivate When Done
```bash
deactivate
```

### Install Additional Packages (if needed)
```bash
# Make sure environment is activated first!
pip install package-name
```

---

## 🎓 Course-Specific Tips

### Before Each Work Session
1. Open terminal
2. `cd cmn-practical`
3. `. cmn-env/bin/activate`
4. Start working!

### File Organization Tips
- Keep raw data in `data/` folders - NEVER modify original files
- Use `notebooks/` for exploratory work and testing
- Put final, clean scripts in `scripts/`
- Save all plots to `figures/` with descriptive names
- Each project gets its own folder - keep them separate!

### When Starting a New Project
1. Go to the appropriate project folder (project1, project2, or project3)
2. Create a new notebook in `notebooks/`
3. Load your data from `data/`
4. Explore, analyze, visualize!
5. Save important plots to `figures/`

### Good Coding Habits (from the setup guide)
1. **Plot early, plot often** - Always visualize raw data first
2. **Check shapes** - After every transformation, print array shapes
3. **Use functions** - If you copy-paste code twice, make it a function
4. **Save intermediate results** - Don't re-run slow preprocessing
5. **Label everything** - Every plot needs axis labels and titles

---

## 🆘 Troubleshooting

### "Module not found" errors
**Solution:** Make sure your environment is activated!
```bash
. cmn-env/bin/activate
```

### VS Code not finding the right Python
**Solution:** 
1. Press Ctrl+Shift+P (or Cmd+Shift+P on Mac)
2. Type "Python: Select Interpreter"
3. Choose the one with `cmn-env` in the path

### Jupyter kernel issues
**Solution:**
```bash
. cmn-env/bin/activate
python -m ipykernel install --user --name cmn --display-name "CMN Course"
```
Then select "CMN Course" as your kernel in Jupyter.

### Packages won't install
**Solution:** Make sure you're in the activated environment and try:
```bash
pip install --upgrade pip
pip install package-name
```

### "Permission denied" errors
**Solution:** Never use `sudo` with pip in this environment. If you see permission errors, something is wrong with your activation.

---

## 📚 Learning Resources

### Python Basics
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) (free online)
- [NumPy Basics](https://numpy.org/doc/stable/user/absolute_beginners.html)

### Plotting
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)

### MNE (EEG/MEG)
- [MNE Tutorials](https://mne.tools/stable/auto_tutorials/index.html)
- Start with "Getting Started" if you're new to EEG data

### Machine Learning
- [Scikit-learn Tutorials](https://scikit-learn.org/stable/tutorial/index.html)

---

## ✨ You're All Set!

Your environment is ready for the course. Here's what to do next:

1. **Test your setup**: Run `python verify_setup.py` one more time
2. **Get familiar**: Open VS Code or Jupyter Lab and explore
3. **Wait for course start**: Your instructor will provide datasets when the course begins
4. **Join Brightspace**: All course materials will be posted there

**Questions?** 
- Email your instructor: l.vortmann@rug.nl
- Check the syllabus for work session times
- Ask during the first class!

Good luck with the course! 🚀🧠
