import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def normalize(population: pd.Series) -> pd.Series:
    """
    Normalize population data to numeric values.
    Handles 'k', 'M', and 'B' suffixes for thousands, millions, and billions.
    """
    normalized_population = []
    for data in population:
        if data.endswith('k'):
            normalized_population.append(float(data[:-1]) * 1000)
        elif data.endswith('M'):
            normalized_population.append(float(data[:-1]) * 1000000)
        elif data.endswith('B'):
            normalized_population.append(float(data[:-1]) * 1000000000)
        else:
            normalized_population.append(float(data))
    return pd.Series(normalized_population)


def display_populations(country1: str, country2: str, df: pd.DataFrame):
    """
    Display the population data for two countries.
    """
    if country1 not in df["country"].values:
        print(f"Country '{country1}' not found in the dataset.")
        return
    if country2 not in df["country"].values:
        print(f"Country '{country2}' not found in the dataset.")
        return

    country1_df = df[df["country"] == country1]
    country1_years = country1_df.columns[1:-50]
    population1 = normalize(country1_df.values[0][1:-50])

    country2_df = df[df["country"] == country2]
    country2_years = country2_df.columns[1:-50]
    population2 = normalize(country2_df.values[0][1:-50])

    plt.plot(country2_years, population2, color='blue')
    plt.plot(country1_years, population1, color='green')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population Projections')
    plt.yticks([20000000, 40000000, 60000000], ["20M", "40M", "60M"])
    plt.xticks(country1_years[::40])
    plt.legend([country2, country1], loc='lower right')
    plt.show()


def main():
    df = load("population_total.csv")
    if df is not None:
        display_populations("France", "Belgium", df)


if __name__ == "__main__":
    main()
