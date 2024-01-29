import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from datetime import datetime


def make_plot_frequency_technologies(df: DataFrame) -> None:
    df["skills"] = df["skills"].replace({
        "machine learning": "ML",
        "Artificial Intelligence": "AI",
        " ШІ": "AI",
        "AI ": "AI",
        "ООП": "OOP"
    }, regex=True)
    skills_list = df["skills"].str.split(", ")

    technologies_count = pd.Series(
        np.concatenate(skills_list.iloc[:].values)
    ).value_counts()

    plt.figure(figsize=(30, 10))
    plt.bar(technologies_count.index, technologies_count)
    plt.xlabel("technology")
    plt.ylabel("Frequency")
    plt.title("Count of technologies in all vacancies")
    plt.xticks(rotation=45)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    plt.savefig("../data/plots/" f"frequency_technologies_{timestamp}.png")


def make_plot_frequency_technologies_with_exp(df: DataFrame) -> None:
    df["skills"] = df["skills"].replace({
        "machine learning": "ML",
        "Artificial Intelligence": "AI",
        "ШІ": "AI",
        "ООП": "OOP"
    }, regex=True)

    beginner_skills_list = df.loc[df["experience"] == "<1", "skills"].str.split(", ")
    beginner_technologies = pd.Series(
        np.concatenate(beginner_skills_list.iloc[:].values)
    ).value_counts()

    one_plus_exp_skills_list = df.loc[df["experience"] == "1…3", "skills"].str.split(", ")
    one_plus_exp_technologies = pd.Series(
        np.concatenate(one_plus_exp_skills_list.iloc[:].values)
    ).value_counts()

    three_plus_exp_skills_list = df.loc[df["experience"] == "3…5", "skills"].str.split(", ")
    three_plus_exp_technologies = pd.Series(
        np.concatenate(three_plus_exp_skills_list.iloc[:].values)
    ).value_counts()

    five_plus_exp_skills_list = df.loc[df["experience"] == "5+", "skills"].str.split(", ")
    five_plus_exp_technologies = pd.Series(
        np.concatenate(five_plus_exp_skills_list.iloc[:].values)
    ).value_counts()

    fig, axes = plt.subplots(2, 2, figsize=(30, 15))
    fig.suptitle("Count of technologies in all vacancies")

    axes[0, 0].bar(beginner_technologies.index, beginner_technologies)
    axes[0, 0].set_title("Beginner Experience")
    axes[0, 0].set_xlabel("Technology")
    axes[0, 0].set_ylabel("Frequency")
    axes[0, 0].tick_params(axis='x', rotation=45)

    axes[0, 1].bar(one_plus_exp_technologies.index, one_plus_exp_technologies)
    axes[0, 1].set_title("1-3 Years Experience")
    axes[0, 1].set_xlabel("Technology")
    axes[0, 1].set_ylabel("Frequency")
    axes[0, 1].tick_params(axis='x', rotation=45)

    axes[1, 0].bar(three_plus_exp_technologies.index, three_plus_exp_technologies)
    axes[1, 0].set_title("3-5 Years Experience")
    axes[1, 0].set_xlabel("Technology")
    axes[1, 0].set_ylabel("Frequency")
    axes[1, 0].tick_params(axis='x', rotation=45)

    axes[1, 1].bar(five_plus_exp_technologies.index, five_plus_exp_technologies)
    axes[1, 1].set_title("5+ Years Experience")
    axes[1, 1].set_xlabel("Technology")
    axes[1, 1].set_ylabel("Frequency")
    axes[1, 1].tick_params(axis='x', rotation=45)

    plt.tight_layout(rect=[0, 0, 1, 0.96])

    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    plt.savefig("../data/plots/" f"frequency_technologies_with_exp{timestamp}.png")


def make_plot_cities_in_vacancies(df: DataFrame) -> None:
    mask = (
            (df["location"].str.len() > 15)
            & (df["location"].str.contains("We're"))
    )
    df.loc[mask, "location"] = "unknown"

    locations = df["location"].str.split(", ")
    locations_count = (
        pd.Series(
            np.concatenate(locations.iloc[:].values)
        ).value_counts()
    )

    plt.figure(figsize=(30, 20))
    locations_count.plot(kind="bar", color="skyblue")
    plt.xlabel("Location")
    plt.ylabel("Vacancies in the location")
    plt.title("Vacancies by location")
    plt.xticks(rotation=45)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    plt.savefig("../data/plots/" f"cities_in_vacancies_{timestamp}.png")


def make_plot_vacancies_in_companies(df: DataFrame) -> None:
    vacancies_in_company = df["company"].value_counts().head(10)

    plt.pie(
        vacancies_in_company,
        labels=vacancies_in_company.index,
        autopct=lambda p: "{:.0f}".format(p * sum(vacancies_in_company) / 100),
    )

    plt.title("Top 10 vacancies by max counts")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    plt.savefig("../data/plots/" f"vacancies_in_companies_{timestamp}.png")


def make_plot_vacancies_by_exp(df: DataFrame) -> None:
    exps = ["less then year", "1-3 years", "more than 5 years", "3-5 years"]
    plt.figure(figsize=(8, 8))
    plt.pie(
        df["experience"].value_counts(),
        labels=exps[::-1],
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Vacancies by yars experiences")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    plt.savefig("../data/plots/" f"vacancies_by_experience_{timestamp}.png")
