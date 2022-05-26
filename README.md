# The Man in a Hole project or A Way Against Customer Churn Cycle

## Project objectives

  - Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation),
  findings, and key takeaways in a Jupyter Notebook report.
  - Create modules (acquire.py, prepare.py) that make your process repeateable.
  - Ask exploratory questions of your data that will help you understand more about the attributes and drivers of customers churning 
  by using charts and statistical tests.
  - Construct a model to predict customer churn using classification techniques.
  - Deliver a 5 minute target-audience-appropriate presentation consisting of a high-level notebook walkthrough 
  using your Jupyter Notebook from above.
  - Answer questions of my audience.
## Business Goals
  - Find drivers for customer churn at Telco.
  - Construct a ML classification model that accurately predicts customer churn.
  - Deliver a report that a non-data scientist can read through and understand what steps were taken, why and what the outcome was.
## Audience
  - CodeUp students and instructors
## Project Deliverables
  - A final report notebook
  - A final presentation
  - Modules to make my project reproducible:
    * An acquire.py file
    * A prepare.py file
    * Explanation for the env.py module
    * A Readme (.md) file
  - A Predictions (.csv) file
## Project Context
  - Dataset used came from Codeup database
  - The project is the first of the Modeling project
## Executive Summary - Conclusions & Next Steps
  - The goal of this project was to build a model that could predict whether a client would churn based on the previous data
  - Only classification models were used (Decision tree, Random Forest, K-Nearest Neighbor, Logistic Regression)
  - Findings:
    * The best model with the features used is the Decision Tree model.
    * Its accuray is 76%  compared to the baseline at 73%
    * Some features prevent churn and are worth examining
