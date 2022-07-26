import pandas as pd

from funcs import get_dataframe

# Difference between avg income of male and female from age 35 - 45 inclusive

DATASET_PATH = "datasets/income.xlsm"   # path to xlsm dataset


def calculate_average(df):
    return df['Income'].median()


def main():
    # read from xlsm dataset
    df = get_dataframe(DATASET_PATH, "datasets/income.xlsm.pickle", sheet_name="IncomeBreakdown")

    # get records where ages are 35 - 45 inc.
    age_df = df.query('Age >= 35 & Age <= 45')
    
    # split into female/male dataframes
    male_df = age_df.loc[age_df["Gender"] == "Male"]
    female_df = age_df.loc[age_df["Gender"] == "Female"]

    # calculate average of each
    male_average = calculate_average(male_df)
    female_average = calculate_average(female_df)

    # get the difference
    difference = abs(male_average - female_average)
    
    print(f"Male average:   ${round(male_average, 2):,.2f}")
    print(f"Female average: ${round(female_average, 2):,.2f}")
    print(f"DIfference:     ${round(difference, 2):,.2f}")


if __name__ == "__main__":
    main()