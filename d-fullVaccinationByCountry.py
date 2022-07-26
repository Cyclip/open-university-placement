import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

from date_conversion import to_date, to_days, get_closest_index

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

# read only
population_df = pd.read_csv(POPULATION_DATASET_PATH, skiprows=4)

def date_range(start, end):
    """Generate an iterator over the dates between start and end dates"""
    for n in range(int(end - start).days):
        yield start + dt.timedelta(n)


def gen_days():
    return {
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
        10: None,
        11: None,
        12: None,
        13: None,
        14: None,
        15: None,
    }



def plot(df):
    for i, country in df.iterrows():
        plt.plot(
            df.columns[2:],
            country[2:],
            label=country["country"],
        )
    plt.show()



def main():
    # read into dict of dataframes
    df = pd.read_excel(VACCINATION_DATASET_PATH, sheet_name=None)

    # get first (and only) sheet
    df = df["Sheet1"]

    # dates are stored weirdly, add converted dates
    df['real_date'] = pd.TimedeltaIndex(df['date'], unit='d') + dt.datetime(1899, 12, 30)

    # for each country, identify the total amount of vaccinations
    # country       population      proportion
    people_fully_vaccinated = []

    for country in COUNTRIES:
        country_df = df.loc[df["iso_code"] == country]
        print("\n\nCountry: " + country)

        # get from and to date
        from_row_index = get_closest_index(country_df, "date", to_days(dt.datetime.strptime(FROM_DATE, "%Y-%m-%d")))
        to_row_index = get_closest_index(country_df, "date", to_days(dt.datetime.strptime(TO_DATE, "%Y-%m-%d")))
        print(from_row_index, to_row_index)

        # get total amount of vaccinations for each day per hundred
        days = gen_days()
        for index in range(from_row_index, to_row_index + 1):
            newIndex = index - from_row_index + 5
            vaccinations = country_df.loc[index]["people_fully_vaccinated_per_hundred"]
            
            if pd.isna(vaccinations):
                days[newIndex] = None
            else:
                days[newIndex] = vaccinations
        
        # to list
        days = list(days.values())

        final = [country,]
        final += days

        people_fully_vaccinated.append(final)

    # convert to dataframe
    people_fully_vaccinated_df = pd.DataFrame(
        people_fully_vaccinated, 
        columns=[
            "country",
            dt.datetime.strptime("5/03/2021", "%d/%m/%Y"),
            dt.datetime.strptime("6/03/2021", "%d/%m/%Y"),
            dt.datetime.strptime("7/03/2021", "%d/%m/%Y"),
            dt.datetime.strptime("8/03/2021", "%d/%m/%Y"),
            dt.datetime.strptime("9/03/2021", "%d/%m/%Y"),
            dt.datetime.strptime("10/03/2021", "%d/%m/%Y"),
            dt.datetime.strptime("11/03/2021", "%d/%m/%Y"),
            dt.datetime.strptime("12/03/2021", "%d/%m/%Y"),
            dt.datetime.strptime("13/03/2021", "%d/%m/%Y"),
            dt.datetime.strptime("14/03/2021", "%d/%m/%Y"),
            dt.datetime.strptime("15/03/2021", "%d/%m/%Y"),
        
        ]
    )
    
    print(people_fully_vaccinated_df)
    people_fully_vaccinated_df.to_html("output/d-vaccinationByCountry.html")

    plot(people_fully_vaccinated_df)


if __name__ == "__main__":
    main()