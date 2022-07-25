import pandas as pd
import datetime as dt

from date_conversion import to_date, to_days, get_closest

# Proportion of fully vaccinated from 5th to 15th March 2021

VACCINATION_DATASET_PATH = "datasets/VaccinationByCountry.xlsx"
POPULATION_DATASET_PATH = "datasets/API_SP.POP.TOTL_DS2_en_csv_v2_4335082.csv"
COUNTRIES = [
    "GBR",
    "ROU",
    "BGR",
    "BRA",
    "ARE",
]
FROM_DATE = "2021-03-05"
TO_DATE = "2021-03-15"


def get_country_population(countryCode, year):
    """Get popatulation of country from population dataset at a specific year

    Args:
        countryCode (string): ISO code of country
        year (int): year of population dataset

    Returns:
        int: Population of country
    """
    return int(
        population_df.loc[population_df["Country Code"] == countryCode][str(year)].item()
    )


def main():
    # read into dict of dataframes
    df = pd.read_excel(VACCINATION_DATASET_PATH, sheet_name=None)

    # get first (and only) sheet
    df = df["Sheet1"]

    # dates are stored weirdly, add converted dates
    df['real_date'] = pd.TimedeltaIndex(df['date'], unit='d') + dt.datetime(1899, 12, 30)

    # for each country, identify the total amount of vaccinations
    people_fully_vaccinated = []

    for country in COUNTRIES:
        country_df = df[df["iso_code"] == country]

        # get from and to date
        from_row = get_closest(country_df, "date", to_days(dt.datetime.strptime(FROM_DATE, "%Y-%m-%d")))
        to_row = get_closest(country_df, "date", to_days(dt.datetime.strptime(TO_DATE, "%Y-%m-%d")))

        # get total vaccinations
        difference = int(to_row["people_fully_vaccinated"]) - int(from_row["people_fully_vaccinated"])

        # map country to total vaccinations
        people_fully_vaccinated.append([country, difference])
    
    # convert to dataframe
    people_fully_vaccinated_df = pd.DataFrame(people_fully_vaccinated, columns=["country", "people_fully_vaccinated"])
    
    print(people_fully_vaccinated_df)
    people_fully_vaccinated_df.to_html("output/d-vaccinationByCountry.html")


if __name__ == "__main__":
    # read only
    population_df = pd.read_csv(POPULATION_DATASET_PATH, skiprows=4)
    
    main()