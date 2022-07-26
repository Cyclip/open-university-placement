import pandas as pd

from funcs import get_dataframe

DATASET_PATH = "datasets/income.xlsm"   # path to xlsm dataset


def main():
    # read from xlsm dataset
    df = get_dataframe("datasets/income.xlsm.pickle", sheet_name="IncomeBreakdown")


if __name__ == "__main__":
    main()