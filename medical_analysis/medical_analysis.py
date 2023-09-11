import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stat

# getting the data and showing some basic info about every feature:
data = pd.read_csv("medical_examination.csv")
pd.set_option('display.max_columns', None)
print(data.head())
print(data.count())
print(data.shape)
print(data.columns)

# making charts : where we show counts of different outcomes for the cholesterol, gluc, alco,
# active, and smoke variables for patients with cardio=1 and cardio=0 in different panels:
columns_needed = data[['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio']]
index_col = ['cholesterol', 'gluc', 'smoke', 'alco', 'active']
data_cardio_0 = columns_needed.loc[columns_needed['cardio'] == 0]
data_cardio_1 = columns_needed.loc[columns_needed['cardio'] == 1]

# counting outcomes for bad and good outcomes for 2 different class of feature 'cardio' :
chol_good_cardio_1 = data_cardio_1[data_cardio_1['cholesterol'] == 1].shape[0]
chol_bad_cardio_1 = data_cardio_1[data_cardio_1['cholesterol'] == 2].shape[0] + data_cardio_1[data_cardio_1['cholesterol'] == 3].shape[0]
chol_bad_cardio_0 = data_cardio_0[data_cardio_0['cholesterol'] == 2].shape[0] + data_cardio_0[data_cardio_0['cholesterol'] == 3].shape[0]
chol_good_cardio_0 = data_cardio_0[data_cardio_0['cholesterol'] == 1].shape[0]

gl_good_cardio_1 = data_cardio_1[data_cardio_1['gluc'] == 1].shape[0]
gl_bad_cardio_1 = data_cardio_1[data_cardio_1['gluc'] == 2].shape[0] + data_cardio_1[data_cardio_1['gluc'] == 3].shape[0]
gl_good_cardio_0 = data_cardio_0[data_cardio_0['gluc'] == 1].shape[0]
gl_bad_cardio_0 = data_cardio_0[data_cardio_0['gluc'] == 2].shape[0] + data_cardio_0[data_cardio_0['gluc'] == 3].shape[0]

sm_good_cardio_1 = data_cardio_1[data_cardio_1['smoke'] == 0].shape[0]
sm_bad_cardio_1 = data_cardio_1[data_cardio_1['smoke'] == 1].shape[0]
sm_good_cardio_0 = data_cardio_0[data_cardio_0['smoke'] == 0].shape[0]
sm_bad_cardio_0 = data_cardio_0[data_cardio_0['smoke'] == 1].shape[0]

al_good_cardio_1 = data_cardio_1[data_cardio_1['alco'] == 0].shape[0]
al_bad_cardio_1 = data_cardio_1[data_cardio_1['alco'] == 1].shape[0]
al_good_cardio_0 = data_cardio_0[data_cardio_0['alco'] == 0].shape[0]
al_bad_cardio_0 = data_cardio_0[data_cardio_0['alco'] == 1].shape[0]

act_good_cardio_1 = data_cardio_1[data_cardio_1['active'] == 1].shape[0]
act_bad_cardio_1 = data_cardio_1[data_cardio_1['active'] == 0].shape[0]
act_good_cardio_0 = data_cardio_0[data_cardio_0['active'] == 1].shape[0]
act_bad_cardio_0 = data_cardio_0[data_cardio_0['active'] == 0].shape[0]

# sorting counts into lists to make bar charts:
good_cardio_1 = [chol_good_cardio_1, gl_good_cardio_1, sm_good_cardio_1, al_good_cardio_1, act_good_cardio_1]
bad_cardio_1 = [chol_bad_cardio_1, gl_bad_cardio_1, sm_bad_cardio_1, al_bad_cardio_1, act_bad_cardio_1]
good_cardio_0 = [chol_good_cardio_0, gl_good_cardio_0, sm_good_cardio_0, al_good_cardio_0, act_good_cardio_0]
bad_cardio_0 = [chol_bad_cardio_0, gl_bad_cardio_0, sm_bad_cardio_0, al_bad_cardio_0, act_bad_cardio_0]

# bar charts:
bar_width = 0.25
bar1 = np.arange(len(good_cardio_0))
bar2 = [x + bar_width for x in bar1]

plt.subplot(2, 1, 1)
plt.bar(bar1, good_cardio_0, color='green', width=bar_width, edgecolor='grey', label='normal outcomes')
plt.bar(bar2, bad_cardio_0, color='red', width=bar_width, edgecolor='grey', label='above normal outcomes')

plt.title('outcomes if cardiovascular disease is absent', fontweight='bold', fontsize=10)
plt.ylabel('amount', fontweight='bold', fontsize=15)
plt.xticks([r + bar_width for r in range(len(good_cardio_0))], index_col)
plt.legend()

plt.subplot(2, 1, 2)
plt.bar(bar1, good_cardio_1, color='green', width=bar_width, edgecolor='grey', label='normal outcomes')
plt.bar(bar2, bad_cardio_1, color='red', width=bar_width, edgecolor='grey', label='above normal outcomes')

plt.xlabel('outcomes if cardiovascular disease is present', fontweight='bold', fontsize=10)
plt.ylabel('amount', fontweight='bold', fontsize=15)
plt.xticks([r + bar_width for r in range(len(good_cardio_0))], index_col)

plt.legend()
plt.show()

# calculating (making new feature) BMI for an every patient and classing as an overweight '1' or not overweight '0':
bmi = pd.Series([], dtype='float64')
print(len(data))
for i in range(len(data)):
    bmi[i] = 0
for i in range(len(data)):
    bmi[i] = data['weight'][i] / pow(data["height"][i] * 0.01, 2)

data.insert(13, 'BMI', bmi)
print(data.head(10))

overweight = np.zeros(70000)
for i in range(len(data)):
    if data['BMI'][i] > 25:
        overweight[i] = int(1)
    else:
        overweight[i] = int(0)

data.insert(14, 'overweight', overweight)

# Normalizing the data by making 0 always good and 1 always bad - the value of cholesterol or glucose:

data["cholesterol"] = np.where(data["cholesterol"] == 1, 0, 1)
data["gluc"] = np.where(data["gluc"] == 1, 0, 1)

# Cleaning the data to make correlations. Filtering out the following patient segments that represent incorrect data:
# diastolic pressure is higher than systolic
# height is less than the 2.5th percentile
# height is more than the 97.5th percentile
# weight is less than the 2.5th percentile
# weight is more than the 97.5th percentile
data_heatmap = data.loc[(data["ap_lo"] <= data["ap_hi"]) & (data["height"] >= data["height"].quantile(0.025)) & (data["height"] <= data["height"].quantile(0.975)) & (data["weight"] >= data["weight"].quantile(0.025)) & (data["weight"] <= data["weight"].quantile(0.975))]
corr = data_heatmap.corr()

# Creating a correlation matrix with the filtered data. (heatmap):
plt.subplots(figsize=(12, 9))
sns.heatmap(corr, vmax=0.8, fmt='.1f', annot=True)

plt.show()

# correlations and p-value for some features:
# - 'ap-lo' and 'cardio' corr. and p-value:
ap_lo_cardio_corr = stat.pointbiserialr(data_heatmap['cardio'], data_heatmap['ap_lo'])
print(ap_lo_cardio_corr)
# - 'weight' and 'cardio' corr. and p-value:
weight_cardio_corr = stat.pointbiserialr(data_heatmap['cardio'], data_heatmap['weight'])
print(weight_cardio_corr)
# - 'cholesterol' and 'gluc' corr. and p-value:
plt.plot(data_heatmap['cholesterol'], data_heatmap['gluc'])
plt.title('chol and gluc')
plt.show()

# CONCLUSIONS:
# Patients who have cardiovascular disease also have above normal or well above normal level of cholesterol and glucose
# Patients who have cardiovascular disease have a less percentage of people who are physically active
# Looking on a correlation matrix, features : 'weight', 'ap-lo ', 'cholesterol', 'gluc' and 'BMI' have
# low correlation with 'cardio'.
