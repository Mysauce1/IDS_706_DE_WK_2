"""Import necessary packages/libraries"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


divorce = pd.read_csv("divorce_df.csv")  # Import the data


def explore_data_characteristics(data):
    """
    Explores the data's characteristics by:
    1. Displaying the first few rows of the dataset
    2. Displaying summary statistics for each variable
    3. Displaying the type of each variable
    """
    divorce_head = data.head()
    # divorce_variable_types =
    divorce_summ_stats = data.describe()
    total_rows = data.shape[0]
    print(
        "Divorce Head: ",
        divorce_head,
        "\n",
        "Divorce Summary Statistics: ",
        divorce_summ_stats,
    )
    print("Divorce Variable Types: ")
    data.info()
    return total_rows


def isnull(data, column=None):
    """
    Counts the number of missing values in each variable if a column is not specified.
    If a column is specified, then the number of missing values in that specific variable.
    """
    if column is None:
        missing_sum = data.isnull().sum()
        print("Sum of Missing Values Per Column: ", missing_sum)
        return missing_sum
    else:
        missing_sum = data[column].isnull().sum()
        print(f"Sum of Missing Values in {column}: {missing_sum}")
        return missing_sum


def age_and_marital_status_stats(data):
    """
    Shows the mean, standard deviation, minimum, and maximum age at marriage for married and divorced couples
    """
    summ_stats_grouped_by_divorce = data.groupby("divorced").agg(
        mean_age=("age_at_marriage", "mean"),
        sd_age=("age_at_marriage", "std"),
        min_age=("age_at_marriage", "min"),
        max_age=("age_at_marriage", "max"),
    )
    print("Summary Statistics Grouped By Divorce: ", summ_stats_grouped_by_divorce)
    return summ_stats_grouped_by_divorce


"""Calls the functions """
if divorce is not None:
    explore_data_characteristics(divorce)
    isnull(divorce)
    age_and_marital_status_stats(divorce)


"""Filter Exploration"""
print(
    divorce["marriage_type"].value_counts()
)  # Count the number of couples in each marriage type. 
    # This is to ensure that there is enough data in the 'Love' type to conduct our analysis.'''


love_divorce = divorce[
    divorce["marriage_type"] == "Love"
]  # Filters data to only include love marriages
love_divorce = love_divorce.drop(
    columns=["marriage_type"]
)  # Remove the marriage type variable since there's only one type included
love_divorce.head()  # Show the filtered dataset

married_30_plus = love_divorce[
    love_divorce["age_at_marriage"] >= 30
]  # Filter the data to only include couples who got married at age 30 or over

married_30_plus["divorced"].value_counts().plot(
    kind="bar"
)  # Create a bar chart that shows the frequency of couples 
 # who stay married or get a divorce given they got married at age 30 or after. 
 # This can help give us an idea of their proportions.
plt.xlabel("Marital Status")  # Add a label for the x axis
plt.ylabel("Frequency")  # Add a label for the y axis
plt.xticks(
    ticks=[0, 1], labels=["Divorced", "Married"], rotation=0
)  # Convert the encoded names to their corresponding label names. 
    # Note: Divorced = 1, Not Divorced (Married) = 0. 
    # These labels were rotated to be horizontal
plt.title(
    "Marital Status Frequencies for Couples who Married for Love at Age 30 or After"
)  # title the graph
plt.show()  # Show the graph


""" Encode the categorical data. The OrdinalEcoder encodes ordinal variables, while the OneHotEncoder encodes norminal variables"""
ordencoder = OrdinalEncoder(
    categories=[["No Formal Education", "High School", "Bachelor", "Master", "PhD"]]
)  # Establish the OrdinalEncoder with the appropriate category order for the education level
love_divorce["education_level_enc"] = ordencoder.fit_transform(
    love_divorce[["education_level"]]
)  # Encode the education level
love_divorce.head()  # Check if the data was encoded correctly

ohencoder = OneHotEncoder(sparse_output=False)  # Establish the OneHotEncoder
nom_cols = [
    "employment_status",
    "religious_compatibility",
    "conflict_resolution_style",
]  # Create a list of the nominal variables
love_divorce_enc = pd.DataFrame(
    ohencoder.fit_transform(love_divorce.loc[:, nom_cols]),
    columns=ohencoder.get_feature_names_out(nom_cols),
)  # Create a new dataframe with the encoded nominal variables

love_divorce_final = pd.concat(
    [
        love_divorce.drop(columns=nom_cols + ["education_level"]).reset_index(
            drop=True
        ),
        love_divorce_enc.reset_index(drop=True),
    ],
    axis=1,
)  # Create a new dataframe where the encoded categorical variables 
 # are included with the rest of the data and the unecoded categorical variables are removed
love_divorce_final.head()  # Show the prepared dataset

"""Perform logistic regression"""
X = love_divorce_final.drop(columns="divorced")  # Create feature set
y = love_divorce_final["divorced"]  # Create target set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)  # Split data into training and test sets. 
    # 70 % of the data will be in the training set, while 30 % will be in the test set
logreg = LogisticRegression()  # Establish the model
logreg.fit(X_train, y_train)  # Fit the model
y_pred = logreg.predict(X_test)  # Make marital status predictions
print(
    "Accuracy", accuracy_score(y_test, y_pred)
)  # Evaluate the model's performance based on its accuracy

coefs = pd.DataFrame(
    {"Features": X_train.columns, "Coefficients": np.exp(logreg.coef_[0])}
)  # Obtain the model coefficients. 
    # The exponent of the coefficients is used so the coefficients can be interpreted as odds.
print(coefs)  # Show the coefficients
