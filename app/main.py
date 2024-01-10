import asyncio

import pandas as pd
from data.parse import get_all_vacancies

import app.analisys as mp


def main():
    asyncio.run(get_all_vacancies())

    df = pd.read_csv("../data/vacancies.csv", index_col=0)

    mp.make_plot_frequency_technologies(df)
    mp.make_plot_frequency_technologies_with_exp(df)
    mp.make_plot_cities_in_vacancies(df)
    mp.make_plot_vacancies_in_companies(df)
    mp.make_plot_vacancies_by_exp(df)


if __name__ == '__main__':
    main()
