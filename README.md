# Employment_Data_Analyzer with Pandas 

## Introduction

This Python Pandas project, created by Daniel Tsechmaister, involves analyzing a dataset named "employment.csv." The dataset contains transaction data for 1000 employees from different departments. The dataset includes the following columns:

- Gender: Binary variable (Male/Female)
- Salary: Continuous variable (float)
- Bonus %: Continuous variable (float)
- Team: Categorical variable (11 categories)

In this project, you are required to implement various functions to perform data analysis on this dataset.


# Project Structure

The project includes six functions, each with its own set of functions to implement.
The functions include input and output handling, and we can validate your implementations using the provided tests.


 #Functions

Omit Zeros (omit_zeros)
Implement the function omit_zeros. This function takes a list of column names (colnames) and replaces NaN values in those columns with zeros. It also removes rows where zeros appear in any of the specified columns.

Calculate Total (calc_total)
Implement the function calc_total. This function takes the names of two columns (col1 and col2) and the name of a new column (newcol). It calculates a new column newcol in the DataFrame, which represents the total salary (Salary + Bonus %) for each employee.


Select Group (select_group)
Implement the function select_group. This function takes the name of a categorical column (group_col) and a category (group). It returns rows where the specified category appears in the given categorical column.


Summarize by Group (summ_by_group)
Implement the function summ_by_group. This function takes a DataFrame (d), a list of categorical column names (group_cols), a list of numeric column names (val_col), and a list of aggregation functions (funcs). It returns a summary table that aggregates the values in val_col per category from group_cols using the provided aggregation functions.


Concatenate DataFrames (concat_dfs)
Implement the function concat_dfs. This function concatenates two DataFrames (dfs) along the column axis while keeping the specified column names (col1 and col2). It also calculates a new column (newcol) representing the difference between the values in col1 and col2.


Merge Sort (merge_sort)
Implement the recursive function merge_sort. This function sorts a DataFrame L based on the values in the specified column col using the merge sort algorithm. It also includes the auxiliary function merge to merge two sorted DataFrames.


```bash
git clone <Python_pandas2>
