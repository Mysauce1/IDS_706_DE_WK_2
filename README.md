# IDS_706_DE_WK2

# Project Overview
This project explores factors that impact the odds of a married couple getting a divorce. We will focus on love marriages, as opposed to arranged marriages and marriages that occurred for other reasons.

# Included Files
## divorce.py
Contains the analysis for the project.


# Data Overview
The dataset used for this project is the Divorce Prediction dataset from Kaggle. This dataset contains simulated data of 5000 couples with 21 predictors of divorce, as well as a target variable of whether the couples got a divorce or not. 
Source: https://www.kaggle.com/datasets/vanpatangan/divorce-prediction



# Analysis Overview
The following steps were conducted to perform the analysis:
- Import the necessary packages/libraries
- Import the dataset
- Explore the data, including a subset of the whole dataset, the variable types, and summary statistics
- Check for missing values
- Explore summary statistics of age at marriage based on the marital status
- Check if there are enough love couples to conduct the analysis
- Filter the dataset based on love couples
- Explore the frequency of love couples in each marital status.  
- Encode the categorical variables
- Perform logistic regression
- Interpret the regression coefficients

# Results

## Exploratory Analysis
- Based on the summary of the data types, there appears to be 13 integers, 4 floats (decimal numbers), and 5 objects.

- Based of the summary statistics regarding age at marriage for married and divorced couples, 27 seems to be the average age that people among both marital status get married. This seems like a reasonable age considering most people finish school and are a few years into their careers by the time they are 27. With more stability in their lives, many people feel more comfortable getting married. Both status have a standard deviation of almost 5 years, and the minimal age is 18. The main difference between the marital status is the max age. The oldest age at marriage for a divorced couple is 45, while the oldest for a couple that is still married is 43.


## Missing Values
- The dataset did not contain any missing values. This is not surprising, considering this is simulated data.

## Love Marriages (Before Logistic Regression)
- Based on the the results from the count of marriage types, love marriages make up the majority of the data with 3513 couples out of 5000. This is good, because we can filter the dataset without fear of losing too much data.

<img width="1335" height="773" alt="Screenshot 2025-09-10 232833" src="https://github.com/user-attachments/assets/db812d43-5ffa-49f7-b1d0-84ff6c3cd7cf" />

- Based on the results from the bar graph with the marital status frequencies for couples who married at age 30 or after, there appears to be more couples who have gotten a divorce (around 700 for divorce vs around 500 for married).

## Love Marriages (After Logistic Regression)
- Based on the accuracy score, the model did not perform well on the data with a score of 59% accuracy. This poor score could be due to lack of scaling (one variable had a high scale than the others, which probably skewed the results, the inclusion of irrelavant variables (feature selection was not performed prior to running the model), or lack of parameter tuning (the default parameters of model were used)). Due to these findings, we should be wary of the validity of the coefficients.

- For the interpeation of the coefficients, it is important to note that odds >1 represent increased odds of divorce, odds <1 represent decreased odds of divorce, and odds = 1 represent even odds. If we take a look at religious compatibility, we see that couples who have similar religious beliefs have the slightest increase in odds (1.01) of getting a divorce, couples with differing religious beliefs experience no change in odds (1.00), and couples who are not religious have the slightest decrease in odds (0.98) of getting a divorce. Assume these results are valid, we may be seeing the slight increase in odds among couples with similar beliefs because religion is a very important part of a religious person's life, and with the expectation that both individuals in the couple have similar beliefs, if a disagreement arises, this could lead to high tension in the relationship. We also see that for employment status, couples that include a homemaker have slightly increased odds (1.02) of getting a divorce, while couples with full-time and part-time workers have slightly decreased odds (0.99 for both). While there isn't a defined setting for this dataset, financial stability could play a role in these findings. 
