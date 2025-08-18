from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def display_life_expectancy(country: str, df: pd.DataFrame):
    """
    Display the life expectancy data.
    """
    if country not in df["country"].values:
        print(f"Country '{country}' not found in the dataset.")
        return
    if df.shape[1] < 2 or df.shape[0] < 1:
        print("DataFrame does not have enough data to plot.")
        return
    country_df = df[df["country"] == country]
    years = country_df.columns[1:]
    life_expectancy = country_df.values[0][1:]

    plt.plot(years, life_expectancy)
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.title('France Life Expectancy Projections')
    plt.xticks(years[::40])
    plt.show()


def main():
    """
    Main function to load the dataset and display life expectancy for given country.
    """
    df = load('life_expectancy_years.csv')
    if df is not None:
        display_life_expectancy("France", df)


if __name__ == "__main__":
    main()
