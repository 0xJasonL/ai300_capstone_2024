# Heicoder AI 300 Capstone Project
<b>Context:</b>
- This project was completed as part of a 2-man team capstone project for the Heicoders AI300 - Deploying Machine Learning Models to the Cloud.
- For this capstone, our goal is to train a ML model to predict which Telco Users are likely to churn.
- Once the model is ready, we are to develop a simple Flask webapp on AWS where hypothetical users can use to make their own predictions - through a user form or an API Post method.
- The evaluation metric for the models is AUC and we are encouraged to do our own hyperparameter tuning.

<b>Objective:</b>
- Extract dataset from a hosted cloud Database with SQL
- Select features to train an ML model to predict Telco User Churn and integrate it into a Flask Webapp
- Host the Flask Webapp on an AWS EC2 instance that can predict if user will churn via 2 endpoints, user form and Json via POST Method

<b>Dataset Used:</b>
- Provided by Heicoders. 

<b>My approach</b>
1. Data cleaning and imputing - replace missing values and dropping irrelevant rows (Newly joined users etc)
2. Explored XGboost & Catboost due to categorical features, with GridSearchCV optimizing for AUC.
3. Identified top 5 features with sufficient predictive power for easier UX
4. Developed a simple Flask Webapp accepting the top 5 features via 2 endpoints: i) User form input , ii) via POST API method
5. Containerize webapp with Docker and hosting on AWS EC2

<b>Model Selected</b>
- Model Chosen: CatBoost with best params from Gridsearch - {'learning_rate':0.15, 'max_depth':5} 
- Model AUC: 0.93
- Churn Threshold: 0.29
- Selected Features: `[tenure_months, contract_type, num_dependents, num_referrals, total_monthly_fee]`

<b>Repo Contents</b>
1. Research Notebook - XGBoost and Catboost
2. Dockerfile for Docker Configuration
3. Source code for Flask Webapp  

<b> Connect with me on Linkedin: [Jason Leung](https://www.linkedin.com/in/jasonleunghp/)<b>

