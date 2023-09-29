# Medical_Analysis_Project
The dataset and assignments come from web site : "freeCodeCamp.org"
## The dataset description :
File "medical_examination.csv" contains a data with medical examinations. Rows in the dataset represents patients and 
columns represents inforamtions from examined patients.

| Feature | Variable Type | Variable      | Value Type |
|:-------:|:------------:|:-------------:|:----------:|
| Age | Objective Feature | age | int (days) |
| Height | Objective Feature | height | int (cm) |
| Weight | Objective Feature | weight | float (kg) |
| Gender | Objective Feature | gender | categorical code |
| Systolic blood pressure | Examination Feature | ap_hi | int |
| Diastolic blood pressure | Examination Feature | ap_lo | int |
| Cholesterol | Examination Feature | cholesterol | 1: normal, 2: above normal, 3: well above normal |
| Glucose | Examination Feature | gluc | 1: normal, 2: above normal, 3: well above normal |
| Smoking | Subjective Feature | smoke | binary |
| Alcohol intake | Subjective Feature | alco | binary |
| Physical activity | Subjective Feature | active | binary |
| Presence or absence of cardiovascular disease | Target Variable | cardio | binary |

## Code :
A full code with comments is located in a file "medical_analysis.py".
Python with its libraries like numpy, matpotlib and others helped in making charts and calcuations
needed for this analysis and conclusions.

## Charts of analysis :
Bar plot to see differences between patients with and without cardiovascular disease:
- patients who have a cardiovascular disease have cholesterol and glucose levels above normal
- patients who have a cardiovascular disease are a little less physically active
   
![Figure_1_bar_plot](https://github.com/claudia13062013/Medical_analysis_/assets/97663507/cde8705d-3ca0-4fea-858e-b9de2f98adfa)


Heatmap correlation matrix to see positive or negative correlations between features:
- features : 'weight', 'ap-lo ', 'cholesterol', 'gluc' and 'BMI', 'age ' have low but maybe significant correlation with 'cardio'. 


![Figure_2_heatmap](https://github.com/claudia13062013/Medical_analysis_/assets/97663507/738b2310-c52f-4cc2-9ab7-0037eb50366d)

## Machine Learning Model:
Using conclusions from an analysis, a classifier model  predicts if patient has or hasn't a cardiovascular disease with 72% accuracy:
  Full code in file 'ML_model_classifier.py'
- doing another column that should help with a model training and then scaling features
  'BMI' column that uses columns 'weight' and 'height'
  #bmi[i] = df['weight'][i] / pow(df["height"][i] * 0.01, 2)
- checking if classes are equal and no need of over/under sampling
  
- Using Logistic regression and a feature selection with RFE
  
  Result:
  
  -seeing columns that can be dropped and overall infos about features
  
- Result of training and testing of a model
  
Accuracy of Logistic Regression test: 0.72
