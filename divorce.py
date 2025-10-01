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


def make_love_divorce(divorce):
    """Creates a dataframe that only includes couples who married in love marriages.
    A love marriage is a marriage that was not arranged and does not classify as any other type of marriage.
    """
    # Filters data to only include love marriages
    love_divorce = divorce[divorce["marriage_type"] == "Love"]
    # Remove the marriage type variable since there's only one type included
    love_divorce = love_divorce.drop(columns=["marriage_type"])

    love_divorce.head()
    return love_divorce


def make_married_30_plus(love_divorce):
    """Filter the data to only include couples who got married at age 30 or over"""
    married_30_plus = love_divorce[love_divorce["age_at_marriage"] >= 30]
    return married_30_plus
