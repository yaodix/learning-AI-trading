Preprocessing is a critical concept in any successful ML model. In this course, you will learn the basics of data engineering, data selection, and exploratory data analysis.

## Preparing for Data Analysis

### 1. An Overview of Machine Learning Pipelines

![1766237709009](image/Note/1766237709009.png)

Developing a question to answer is the first step in the machine learning pipeline.

#### Data Acquisition

api

#### Data preprocessing

same date format

* same col name
* ![1766240909540](image/Note/1766240909540.png)

#### Feature Engineering

What?

* create **new attributes** columns using exsiting columns

#### Model Development

* supervised leanring
* unsupervised learning
* RL

很多模型的使用都有一些假设前提，Assumptions outline the expected relationships within the data and the underlying model(假设勾勒数据和模型的预期关系))

difference between predictive and explanatory machine learning model?

* A predictive model focuses on accurately predicting future outcomes, while an explanatory model focuses on understanding the relationships between variables.

Baseline Model

* **Initial Step** : Assess algorithm potential prior to detailed optimization.
* **Utility** : Helps determine whether to refine the current model or consider alternatives.

#### Model Deployment and Monitoring

* **Benefits of API:** By wrapping the model's prediction code into a Python script and function, the deployment becomes clean and straightforward, enriching usability and monitoring.

## Addressing Common Pandas Data Issues

### Key Concepts:

* **Data Importation Challenges** : Sometimes when importing datasets into Pandas, numeric data might be read as strings because of characters like dollar signs or commas.
