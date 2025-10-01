[![Divorce Project for IDS706](https://github.com/Mysauce1/IDS_706_DE_WK_2/actions/workflows/main.yml/badge.svg)](https://github.com/Mysauce1/IDS_706_DE_WK_2/actions/workflows/main.yml)
# IDS_706_DE_WK2

# Project Overview
This project explores factors that impact the odds of a married couple getting a divorce. We will focus on love marriages, as opposed to arranged marriages and marriages that occurred for other reasons.

# Required Files
## divorce.py
Contains the functions for the analysis.


## divorce_analysis.ipynb
Contains the analysis for the project.


## test_divorce.py
Contains test cases to ensure the functions defined for the analysis work properly. There are 3 test cases:
1. test_totalrow: Checks if the expected number of rows are present in the dataset.
2. test_missing_values: Checks if a specific column is free of missing values.
3. test_summ_stat_dtype: Checks if the mean age at marriage for both marital status are float data types.

## requirements.txt
Contains dependancies that will be used to perform the analysis, as well as make and run the test cases.

## Makefile
Runs and formats the test cases.

# Setup Instructions

The following instructions are most effective if Visual Studio Code is used as the IDE.

## Check for the required files
These are the files included in the "Required Files" section, and can be found within the repository.

## Ensure dev container is set up
You should see a folder for the dev container in the repository.

If the dev container is not present and you are working in Visual Studio Code, complete the following steps:

1. Click ctrl/command+shift+P
2. Search and select Dev Containers: Add Development Container Configuration Files...
3. Select Create a new configuration...
4. Select Python 3
5. Select 3.11
- I normally choose bookworm, but bullseye probably works just as well
6. Select any other dependencies (optional)
- The container will be built after this step
7. Click ctrl/command+shift+P
8. Search and select Dev Containers: Rebuild Container
- This will rebuild the container

## Install dependencies from the requirements.txt file
In the terminal, run:
```
make install
```

## Run the tests
In the terminal, run:
```
make test
```
This will show you the results of the tests.

## Format divorce.py and test_divorce.py
In the terminal, run:
'''
make format
'''
This gives consistent formatting among divorce.py and test_divorce.py based on the Black formatter.

## Lint divorce.py
In the terminal, run:
'''
make lint
'''
This checks divorce.py for any errors.

## Clean up the environment
In the terminal, run:
```
make clean
```
Note: I took out the linting step because I could not figure out how to shorten the lines.

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
- Based on the summary of the data types, there appears to be 13 integers, 4 floats (decimal numbers), and 5 objects. 7 of the 13 integer variables are encoded binary variables.

- Based of the summary statistics regarding age at marriage for married and divorced couples, 27 seems to be the average age that people among both marital status get married. This seems like a reasonable age considering most people finish school and are a few years into their careers by the time they are 27. With more stability in their lives, many people feel more comfortable getting married. Both status have a standard deviation of almost 5 years, and the minimal age is 18. The main difference between the marital status is the max age. The oldest age at marriage for a divorced couple is 45, while the oldest for a couple that is still married is 43.


## Missing Values
- The dataset did not contain any missing values. This is not surprising, considering this is simulated data.

## Love Marriages (Before Logistic Regression)
- Based on the the results from the count of marriage types, love marriages make up the majority of the data with 3513 couples out of 5000. This is good, because we can filter the dataset without fear of losing too much data.

<img width="800" height="600" alt="married_30_plus" src="https://github.com/user-attachments/assets/236b9cd3-1227-4f49-9fea-7f7494b2ff92" />


- Based on the results from the bar graph with the marital status frequencies for couples who married at age 30 or after, 
710 couples (~58% of the the couples) got divorced, while 514 couples (~42% of the couples) stayed married. Even though a majority of the couples got divorced, the proportions for married and divorced couples isn't too far away from being evenly split. This could be because getting married later in life allows individuals to mature and develop an understand of what they need/want in a partner, which can increase their chance of finding an ideal partner. Exploration into how marrying at a younger age, such as 18, impacts the sustainability of a marriage would be an ideal next step to dive deeper into this topic.

## Love Marriages (After Logistic Regression)
- Based on the accuracy score, the model did not perform well on the data with a score of 59% accuracy. This poor score could be due to lack of scaling (one variable had a high scale than the others, which probably skewed the results, the inclusion of irrelavant variables (feature selection was not performed prior to running the model), or lack of parameter tuning (the default parameters of model were used)). Due to these findings, we should be wary of the validity of the coefficients.

- For the interpeation of the coefficients, it is important to note that odds >1 represent increased odds of divorce, odds <1 represent decreased odds of divorce, and odds = 1 represent even odds. If we take a look at religious compatibility, we see that couples who have similar religious beliefs have the slightest increase in odds (1.01) of getting a divorce, couples with differing religious beliefs experience no change in odds (1.00), and couples who are not religious have the slightest decrease in odds (0.98) of getting a divorce. Assume these results are valid, we may be seeing the slight increase in odds among couples with similar beliefs because religion is a very important part of a religious person's life, and with the expectation that both individuals in the couple have similar beliefs, if a disagreement arises, this could lead to high tension in the relationship. We also see that for employment status, couples that include a homemaker have slightly increased odds (1.02) of getting a divorce, while couples with full-time and part-time workers have slightly decreased odds (0.99 for both). While there isn't a defined setting for this dataset, financial stability could play a role in these findings.


# Continuous Integration
<img width="2059" height="1529" alt="Screenshot 2025-09-30 224950" src="https://github.com/user-attachments/assets/dada2eee-e760-408c-ae54-31f293856281" />

# Refactoring
<img width="2732" height="1543" alt="Screenshot 2025-09-30 223600" src="https://github.com/user-attachments/assets/ffcd49ac-f28b-4ecd-b5ad-f9963df3bb4b" />

<img width="1389" height="636" alt="Screenshot 2025-09-30 224903" src="https://github.com/user-attachments/assets/9e964cc9-d5e4-4259-baba-b0b0d208f014" />


