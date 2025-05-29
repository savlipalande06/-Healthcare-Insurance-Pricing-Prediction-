# -Healthcare-Insurance-Pricing-Prediction-
- Project Overview
Healthcare insurance pricing is a multifaceted process influenced by several demographic, behavioral, and medical factors. This study leverages machine learning techniques to build predictive models for estimating insurance premiums with greater fairness and accuracy.

- App Demo
A web application titled Healthcare Pricing Prediction App was built using Streamlit to provide real-time premium cost estimations based on user input.

- Objectives
Identify key factors influencing health insurance premiums.

Compare different machine learning algorithms for predictive accuracy.

Develop a user-friendly tool for personalized premium estimation.

- Dataset
Source: Public dataset from Kaggle

Size: 1,338 records

Features:

age

sex

bmi

children

smoker

region

charges (target)

- Data Analysis & Visualizations
Exploratory Data Analysis (EDA) on variables like age, BMI, and charges.

Correlation heatmaps to identify influential predictors.

Distribution plots and scatter plots for better understanding of variable impact.

Key insight: Smoking status, age, and BMI were the most influential factors.

- Methodology
Data Preprocessing: Handled missing data, encoded categorical variables, and normalized features.

Visualization: Used matplotlib and seaborn for insights.

Model Building:

Linear Regression

Decision Tree Regressor

Random Forest Regressor

XGBoost Regressor

Model Evaluation:

R² Score

Mean Absolute Error (MAE)

Mean Squared Error (MSE)

Hyperparameter Tuning: Implemented with GridSearchCV for optimized performance.

- Results
Model	MAE	MSE	R² Score
Linear Regression	High	High	0.78
Decision Tree	Moderate	Highest	0.73
Random Forest	Lowest	Lowest	0.86
XGBoost	Low	Low	0.85

- Random Forest provided the best overall performance.

- App Features
Built using Streamlit, the web application includes:

Age input

BMI input

Number of children

Gender selector

Smoking status selector

Region selector

"Predict Charges" button

- Outputs the predicted medical insurance charge based on the input.

- Key Insights
Smoking is the strongest predictor of high premiums.

BMI and age moderately influence charges.

Region, sex, and number of children have minimal impact.

Machine learning enhances fairness and precision in pricing compared to traditional actuarial models.

- Limitations
Small dataset size (1,338 records).

Limited feature set (no income, education, etc.).

Static snapshot data; lacks temporal analysis.

Focused only on U.S. health system data.

- Future Scope
Incorporate real-time data from wearable devices.

Include more diverse and larger datasets.

Add advanced features (e.g., income, chronic conditions).

Extend to other countries and policy types.

Use advanced models like Neural Networks and Deep Learning.

Analyze cost-effectiveness and policy impact.

- Authors
Savli Palande (A008)

Yashasvi Mahadik (A036)

Nidhi Joshi (A040)

Mentor: Prof. Dr. Yogesh Naik

🛑 This research is currently unpublished and under review. Unauthorized distribution or reuse is prohibited
