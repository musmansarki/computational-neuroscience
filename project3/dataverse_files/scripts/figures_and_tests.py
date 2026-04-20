'''
Reproduce Figures 3-5, and statistical tests in the manuscript.
'''

import argparse 
import os, sys
import glob
import numpy as np
import pandas as pd
from scipy import stats
import statistics as stat
import cv2
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Figure: Total viewing times, number of fixations, and number of saccades for fake and true content during section 1.
ax = sns.violinplot(x = total_view_times["version"], y = total_view_times["viewingTimeSec"])
plt.ylabel('Total view time (s)')
plt.figure(num=None, figsize=(6, 4), dpi=160, facecolor='w', edgecolor='k')
fig_total_dur = ax.get_figure()
fig_total_dur.savefig("figure_03_a.svg")
plt.show()

plt.figure(num=None, figsize=(6, 4), dpi=160, facecolor='w', edgecolor='k')
plt.ylabel('Number of fixations')
plt.ylim([-20, 300])
ax = sns.violinplot(x = fixation_counts["version"], y = fixation_counts["fixationCount"])
plt.savefig("figure_03_b.svg")
plt.show()

plt.ylabel('Number of saccades')
plt.figure(num=None, figsize=(6, 4), dpi=160, facecolor='w', edgecolor='k')
plt.ylim([-20, 300])
sns.violinplot(x = saccade_counts["version"], y = saccade_counts["saccadeCount"])
plt.savefig("figure_03_c.svg")
plt.show()


# Figure: The Distribution of rated believability of items (5-item Likert scale, higher values represents more believable).
df = pd.read_csv('%s/data/features.csv'%root_folder)
plt.figure(num=None, figsize=(6, 4), dpi=160, facecolor='w', edgecolor='k')
ax = sns.countplot(data=df[df['believability']>-1], hue="version", x="believability")
plt.xlabel('rated believability of news')
plt.savefig("figure_04.svg")
plt.show()


# Figure: The distribution of perceived believability of news. Except for small amount of discarded data due to eye tracker issues, 
# the number of samples per stimulus is balanced in true and fake groups (N_true = 715, N_fake=734).
df_true = df[ (df['believability']>-1) & (df['version']=='true')].reset_index(drop=True)
plt.figure(num=None, figsize=(20, 3), dpi=160, facecolor='w', edgecolor='k')
ax = sns.boxplot(x="question",y="believability", data=df_true)
plt.savefig("figure_05_a.svg")
plt.show()

df_fake = df[ (df['believability']>-1) & (df['version']=='fake')].reset_index(drop=True)
plt.figure(num=None, figsize=(20, 3), dpi=160, facecolor='w', edgecolor='k')
ax = sns.boxplot(y="believability", x="question", data=df_fake)
plt.savefig("figure_05_b.svg")
plt.show()


# Statistical Analysis (mean/stdev of distributions, normality tests, and significance tests)
# Fetch the relevant data (Total view times, fixation counts, and saccades counts)
true_total_time = total_view_times[total_view_times["version"] != "fake"]["viewingTimeSec"]
fake_total_time = total_view_times[total_view_times["version"] == "fake"]["viewingTimeSec"]

true_fix_counts = fixation_counts[fixation_counts["version"] != "fake"]["fixationCount"]
fake_fix_counts = fixation_counts[fixation_counts["version"] == "fake"]["fixationCount"]

true_sacc_counts = saccade_counts[saccade_counts["version"] != "fake"]["saccadeCount"]
fake_sacc_counts = saccade_counts[saccade_counts["version"] == "fake"]["saccadeCount"]

input_data_dict = {
    "total_view_time" : [true_total_time, fake_total_time],
    "fixation_counts" : [true_fix_counts, fake_fix_counts],
    "saccade_counts" : [true_sacc_counts, fake_sacc_counts]
}

# Mean and std of analyzed features
print("Total view time of true content | Mean: ", stat.mean(true_total_time), " SD: ", stat.stdev(true_total_time))
print("Total view time of fake content | Mean: ", stat.mean(fake_total_time), " SD: ", stat.stdev(fake_total_time))

print("Number of fixations in true content | Mean: ", stat.mean(true_fix_counts), " SD: ", stat.stdev(true_fix_counts))
print("Number of fixations in fake content | Mean: ", stat.mean(fake_fix_counts), " SD: ", stat.stdev(fake_fix_counts))

print("Number of saccades in true content | Mean: ", stat.mean(true_sacc_counts), " SD: ", stat.stdev(true_sacc_counts))
print("Number of saccades in fake content | Mean: ", stat.mean(fake_sacc_counts), " SD: ", stat.stdev(fake_sacc_counts))
print('')

# Check normality with Shapiro-Wilk
print("Check for normality: ")
for key in input_data_dict:
    for val in input_data_dict[key]:
        print(key, '->', stats.shapiro(val))
print('')

# Check homogeneity of variance with Levene
print("Check for homogeneity of variance: ")
for key in input_data_dict:
    arr = input_data_dict[key]
    print(key, '->', stats.levene(arr[0], arr[1]))
print('')

# Statistical Tests
# Wilcoxon rank sum and Mann Whitney
print("Check statistical differences: ")
for key in input_data_dict:
    arr = input_data_dict[key]
    print(key, '->', stats.ranksums(arr[0], arr[1]))
    print(key, '->', stats.mannwhitneyu(arr[0], arr[1]))
print('')