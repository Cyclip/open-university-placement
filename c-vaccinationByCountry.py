import pandas as pd
import datetime as dt

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
TO_DATE = "2021-03-02"


def to_days(date):
    """Convert a date into an excel date (days since 1899-12-30)

    Args:
        date (DateTime): Date to convert

    Returns:
        int: Days since 1899-12-30
    """
    return (date - dt.datetime(1899, 12, 30)).days


def to_date(days):
    """Convert days since 1899-12-30 to a date

    Args:
        days (int): Number of days since 1899-12-30 (excel date)

    Returns:
        DateTime: DateTime object for excel date
    """
    return dt.datetime(1899, 12, 30) + dt.timedelta(days=days)


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

    for i, country in enumerate(COUNTRIES):
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