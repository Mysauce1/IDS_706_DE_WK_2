"""Import the unittest module and functions from the divorce module"""

import unittest
from divorce import (
    explore_data_characteristics,
    isnull,
    age_and_marital_status_stats,
    divorce,
)


class TestDivorceFunctions(unittest.TestCase):
    """This class contains unittests for
    the explore_data_characteristics, isnull,
    and age_and_marital_status_stats function
    from the divorce module. The following test are performed:
    1. test_totalrows: Checks if the dataset has the correct number of rows.
    2. test_missing_values: Checks if there are any missing values in a specific column.
    3. test_summ_stat_dtype: Checks if the mean age of both married and divorce couples are the correct data type (float).
    """

    def test_totalrows(self):
        total_rows = explore_data_characteristics(
            divorce
        )  # Obtain the total number of rows in the dataset using the explore_data_characteristics function
        self.assertEqual(
            total_rows, 5000
        )  # Check if the value obtained by the function is the correct value

    def test_missing_values(self):
        total_missing = isnull(
            divorce["divorced"]
        )  # Count the number of missing marital status' in the 'divorced' column using the isnull function
        self.assertEqual(
            total_missing, 0
        )  # Checks if there are no missing marital status'

    def test_summ_stat_dtype(self):
        summ_stats = age_and_marital_status_stats(
            divorce
        )  # Obtain summary statistics (mean, standard deviation, minimum, and maximum) of age at marriage based on marital status using the age_and_marital_status_stats
        for val in summ_stats[
            "mean_age"
        ]:  # Iterate through the mean value of each marital status
            self.assertIsInstance(val, float)  # Check if the mean value is a float


if (
    __name__ == "__main__"
):  # Establish a condition where the tests run if the module that is executed is the main program (meaning it's not running the test on an imported module)
    unittest.main()  # Run all the test if the condition has been satisfied
