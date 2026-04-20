# Setup Complete! ✅

## WBAI077-05 - Computational Methods in Neuroscience
### Environment Setup Summary

**Date:** February 3, 2026  
**Student:** [Your Name]  
**Status:** ✅ READY FOR COURSE

---

## What Was Set Up

### ✅ Python Environment
- **Python Version:** 3.12.3
- **Environment Name:** cmn-env
- **Location:** `/home/claude/cmn-practical/cmn-env/`
- **Status:** ✅ Activated and tested

### ✅ Installed Packages
All course-required packages are installed and working:

| Package | Version | Purpose |
|---------|---------|---------|
| numpy | 2.4.2 | Arrays & numerical operations |
| scipy | 1.17.0 | Signal processing, statistics |
| pandas | 3.0.0 | Data tables |
| matplotlib | 3.10.8 | Plotting |
| seaborn | 0.13.2 | Statistical visualizations |
| mne | 1.11.0 | EEG/MEG analysis |
| scikit-learn | 1.8.0 | Machine learning |
| statsmodels | 0.14.6 | Statistical modeling |
| jupyterlab | 4.5.3 | Interactive notebooks |

### ✅ Project Structure
```
cmn-practical/
├── SETUP_GUIDE.md          ← Full detailed setup guide
├── QUICK_START.md          ← Quick reference cheat sheet
├── verify_setup.py         ← Test script (run anytime!)
├── requirements.txt        ← Package list for reproducibility
├── test_plot.png          ← Proof that plotting works
│
├── project1/              ← Project 1 workspace
│   ├── README.md
│   ├── data/             ← Put data here
│   ├── notebooks/        ← Work here!
│   │   └── project_template.ipynb
│   ├── scripts/          ← Final scripts
│   └── figures/          ← Save plots here
│
├── project2/              ← Project 2 workspace
│   └── (same structure)
│
└── project3/              ← Project 3 workspace
    └── (same structure)
```

---

## ✅ Verification Test Results
```
============================================================
WBAI077-05 Environment Verification
============================================================
✓ numpy v2.4.2
✓ scipy.signal imported successfully
✓ pandas v3.0.0
✓ matplotlib.pyplot imported successfully
✓ seaborn v0.13.2
✓ mne v1.11.0
✓ sklearn v1.8.0
✓ statsmodels.api imported successfully
------------------------------------------------------------
✓ Generated test signal
✓ Created and saved test plot to test_plot.png
------------------------------------------------------------
✓✓✓ ALL TESTS PASSED ✓✓✓
Your environment is ready for the course!
============================================================
```

---

## 📚 Quick Start Instructions

### Every Time You Work
```bash
# 1. Open terminal
# 2. Navigate to project folder
cd cmn-practical

# 3. Activate environment (IMPORTANT!)
. cmn-env/bin/activate

# 4. Start working!
# Option A: Jupyter Lab
jupyter lab

# Option B: VS Code
code .
```

### Verify Everything Still Works
```bash
python verify_setup.py
```

---

## 📖 Documentation Files

1. **SETUP_GUIDE.md** - Complete guide with VS Code setup, troubleshooting, and learning resources
2. **QUICK_START.md** - Cheat sheet for daily use
3. **Python Setup Guide.pdf** - Original course setup guide
4. **Course Syllabus.pdf** - Full course information

---

## 🎯 Next Steps

### Before Course Starts
- [ ] Familiarize yourself with Jupyter Lab or VS Code
- [ ] Read through the SETUP_GUIDE.md
- [ ] Test creating a simple notebook
- [ ] Bookmark the QUICK_START.md for easy reference

### First Day of Course (Feb 3, 2026)
- [ ] Attend course introduction (9:00-11:00)
- [ ] Receive Project 1 dataset and instructions
- [ ] Form groups or commit to solo work
- [ ] Decide on research question

### Before First Work Session
- [ ] Review dataset documentation
- [ ] Load data and do initial exploration
- [ ] Identify any potential issues early

---

## 🆘 Troubleshooting

### If something stops working:
1. Check environment is activated: `. cmn-env/bin/activate`
2. Run verification: `python verify_setup.py`
3. Check SETUP_GUIDE.md troubleshooting section
4. Email instructor: l.vortmann@rug.nl

### Common Issues:
- **Module not found** → Environment not activated
- **Jupyter won't start** → Run: `pip install jupyterlab`
- **VS Code can't find packages** → Select correct interpreter
- **Permission errors** → Never use `sudo` in this environment

---

## 📞 Course Information

- **Instructor:** Assist. Prof. dr. L. Vortmann (Lisa-Marie)
- **Email:** l.vortmann@rug.nl
- **Office:** BB 5161.0302
- **Course Code:** WBAI077-05
- **Credits:** 5 ECTS
- **Duration:** 8 weeks (Feb-Mar 2026)
- **Schedule:** Tuesdays & Thursdays, 09:00–11:00

---

## ✨ You're All Set!

Your Python environment is fully configured and ready for the course. All necessary packages are installed, the project structure is organized, and documentation is available.

**Remember:**
- Always activate your environment before working
- Use the QUICK_START.md as your daily reference
- Don't hesitate to ask for help during work sessions
- Start each project with the provided template

**Good luck with your course!** 🚀🧠

---

*Setup completed on: February 3, 2026*  
*Verified by: verify_setup.py (ALL TESTS PASSED)*
