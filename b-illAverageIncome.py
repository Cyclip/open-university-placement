import pandas as pd
import matplotlib.pyplot as plt


from funcs import get_dataframe

# Difference between avg income of male and female from age 35 - 45 inclusive

DATASET_PATH = "datasets/income.xlsm"   # path to xlsm dataset


def calculate_average(df):
    return df['Income'].median()


def main():
    # read from dataset
    df = get_dataframe(DATASET_PATH, "datasets/income.xlsm.pickle", sheet_name="IncomeBreakdown")

    # filter out for only ill people
    ill_df = df.loc[df["Illness"] == "Yes"]

    # group by city
    grouped = ill_df.groupby("City")

    # get median income for each city
    medians = grouped["Income"].median()

    # format into dataframe
    # medians = medians.apply(lambda x: "${:,.2f}".format(x))
    median_df = pd.DataFrame({'City': medians.index, 'Income': medians.values})
    median_df.to_html("output/a-illAverageIncome.html")
    print(median_df)

    # plot into bar chart
    median_df.plot(kind="bar", x="City", y="Income", figsize=(10, 5))
    plt.xlabel("City")
    plt.ylabel("Average Income ($)")
    plt.title("Average income of ill people by city")
    
    # average income of ill people
    plt.axhline(y=ill_df["Income"].median(),linewidth=1, color='#d3d3d3AA', label="Average income of ill people")

    plt.show()


if __name__ == "__main__":
    main()