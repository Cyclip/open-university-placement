import pandas as pd
import datetime as dt

from date_conversion import to_date, to_days

# from 20th January 2021 to 3rd February 2021
# 20/1/2021 to 3/2/2021

DATASET_PATH = "datasets/VaccinationByCountry.xlsx"
COUNTRIES = [
    "United Kingdom",
    "Norway",
    "United States",
    "China",
    "Australia",
]
FROM_DATE = "2021-01-20"
TO_DATE = "2021-02-03"


def get_closest(df, col, val):
    """Get the row in the dataframe that is closest to the value

    Args:
        df (DataFrame): DataFrame to search
        col (string): Column to search
        val (any): Value to search for (or closest value to)

    Returns:
        DataFrame: Row closest to the value
    """
    index = df[col].sub(val).abs().idxmin()
    return df.loc[index]


def main():
    # read into dict of dataframes
    df = pd.read_excel(DATASET_PATH, sheet_name=None)

    # get first (and only) sheet
    df = df["Sheet1"]

    # dates are stored weirdly, add converted dates
    df['real_date'] = pd.TimedeltaIndex(df['date'], unit='d') + dt.datetime(1899, 12, 30)

    # for each country, identify the total amount of vaccinations
    total_vaccinations = []

    for country in COUNTRIES:
        country_df = df[df["country"] == country]

        # get from and to date
        from_row = get_closest(country_df, "date", to_days(dt.datetime.strptime(FROM_DATE, "%Y-%m-%d")))
        to_row = get_closest(country_df, "date", to_days(dt.datetime.strptime(TO_DATE, "%Y-%m-%d")))

        # get total vaccinations
        difference = int(to_row["total_vaccinations"]) - int(from_row["total_vaccinations"])

        # map country to total vaccinations
        total_vaccinations.append([country, difference])
    
    # convert to dataframe
    total_vaccinations_df = pd.DataFrame(total_vaccinations, columns=["country", "total_vaccinations"])
    
    print(total_vaccinations_df)
    total_vaccinations_df.to_html("output/c-vaccinationByCountry.html")


if __name__ == "__main__":
    main()