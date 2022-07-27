import pandas as pd

DATASET_PATH = "datasets/MercedesBensSales.xlsx"


def get_aggregates(df, column):
    # get sum and s.d of column
    sum = df[column].sum()
    sd = df[column].std()
    name = column.split(".")[-1] + " sales"

    # return as list
    return [name, sum, sd]


def main():
    # dataframe from dataset
    df = pd.read_excel(DATASET_PATH)

    # drop null values as they distort the sum/sd
    df.dropna(subset=['unit.cl', 'unit.sl'])

    # get sum and s.d of both SL/CL sales
    output = []
    output.append(get_aggregates(df, 'unit.cl'))
    output.append(get_aggregates(df, 'unit.sl'))

    output_df = pd.DataFrame(output, columns=["name", "sum", "sd"])
    print(output_df)
    output_df.to_html("output/e-mercedesBensAggregates.html")


if __name__ == "__main__":
    main()