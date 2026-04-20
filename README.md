# Computational Methods in Neuroscience
**Course:** WBAI077-05 — University of Groningen  
**Programme:** BSc Artificial Intelligence  

A collection of three data analysis projects applying machine learning and statistical methods to neurological and behavioural datasets. Each project investigates a distinct research question at the intersection of AI and neuroscience.

---

## Project 1: Sleep Stage Analysis from EEG Data

**Research Question:** How do age and sex influence N3 (deep) sleep duration, and is there a significant interaction between the two?

EEG recordings from 50 subjects were sourced from the PhysioNet Sleep-EDF dataset. N3 sleep percentages were extracted per subject and analysed using a two-way ANOVA to assess the independent and combined effects of age group and sex. Post-hoc t-tests were applied where significant interactions were found.

**Key Methods:** EEG feature extraction, sleep stage annotation parsing, two-way ANOVA, post-hoc t-testing  
**Tools:** Python, MNE, NumPy, Pandas, SciPy, Statsmodels, Seaborn

---

## Project 2: Visual Stimulus Decoding from fMRI Data

**Research Question:** Can brain activity in the ventral temporal cortex reliably distinguish between visual stimulus categories?

Using the Haxby et al. fMRI dataset, a Support Vector Machine (SVM) classifier was trained to decode visual stimulus categories (e.g. faces, objects, scenes) from fMRI BOLD signals. A Leave-One-Group-Out cross-validation scheme was used to evaluate generalisation across runs, and a confusion matrix was produced to assess category-level discriminability.

**Key Methods:** fMRI masking, BOLD signal extraction, SVM classification, cross-run validation, confusion matrix analysis  
**Tools:** Python, Nilearn, Scikit-learn, NumPy, Pandas, Matplotlib, Seaborn

---

## Project 3: Eye Movements and News Believability

**Research Question:** Do eye movement patterns predict how believable people find news stories?

Eye-tracking data from the FakeNewsPerception dataset (Sümer et al., 2021) was used to investigate whether fixation duration, pupil size, and regression patterns correlate with believability ratings. A Random Forest regression model was trained to predict believability scores from eye movement features, with feature importance analysis to identify the most predictive signals. A fallback classification task (fake vs. real news) was also performed using t-tests for feature comparison.

**Key Methods:** Eye-tracking feature extraction, correlation analysis, Random Forest regression, feature importance ranking, t-tests  
**Tools:** Python, NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn

---

## Repository Structure

```
├── project1/
│   ├── notebooks/         # EEG sleep stage analysis
│   └── figures/           # Output visualisations
├── project2/
│   ├── notebooks/         # fMRI visual decoding
│   └── figures/           # Confusion matrices and brain plots
├── project3/
│   ├── notebooks/         # Eye-tracking analysis
│   ├── dataverse_files/   # Raw dataset and scripts
│   └── figures/           # Output plots
└── requirements.txt
```

---

## Dependencies

Install required packages with:

```bash
pip install -r requirements.txt
```

Core libraries: `mne`, `nilearn`, `scikit-learn`, `numpy`, `pandas`, `matplotlib`, `seaborn`, `scipy`, `statsmodels`
