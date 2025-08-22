import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def display_truc(
    life_expectancy: pd.DataFrame,
    income_per_person: pd.DataFrame,
    year: str,
):
    """
    Display a scatter plot of life expectancy against
    income per person for a given year.
    """
    year_life_expectancy = life_expectancy[year]
    year_income_per_person = income_per_person[year]

    try:
        plt.scatter(year_income_per_person, year_life_expectancy)
        plt.xscale('log')
        plt.xticks(ticks=(300, 1000, 10000), labels=('300', '1k', '10k'))
        plt.xlabel('Gross dosmetic product')
        plt.ylabel('Life expectancy')
        plt.title(year)
        plt.show()
    except KeyboardInterrupt:
        print("Image display interrupted by user.")


def main():
    life_expectancy = load("life_expectancy_years.csv")
    income_per_person = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )
    if life_expectancy is not None and income_per_person is not None:
        display_truc(life_expectancy, income_per_person, "1900")


if __name__ == "__main__":
    main()
