import csv
from dataclasses import dataclass, fields, astuple
import time
import asyncio

from selenium import webdriver
from selenium.webdriver.common.by import By

from data.config import technologies_in_vacancy

BASE_URL = "https://jobs.dou.ua/vacancies/?category=Python"


async def click_all_more_btn(driver: webdriver) -> None:
    while True:
        button_click = driver.find_elements(
            By.CLASS_NAME,
            "more-btn > a"
        )

        if len(button_click) != 0:
            if driver.find_element(
                    By.CSS_SELECTOR, ".more-btn > a"
            ).get_attribute("style"):
                break
            button_click[0].click()
            time.sleep(0.5)
        else:
            break


@dataclass
class Vacancy:
    title: str
    company: str
    description: str
    location: str
    experience: str
    skills: str


VACANCY_FIELDS = [field.name for field in fields(Vacancy)]


async def parse_single_vacancy(vacancy: webdriver, exp: str) -> Vacancy:
    description = vacancy.find_element(By.CLASS_NAME, "vacancy-section").text
    location = vacancy.find_elements(By.CLASS_NAME, "bi-geo-alt-fill")
    skills = ", ".join(technologies_in_vacancy(description))

    if location:
        location = location[0].text
    else:
        location = None

    return Vacancy(
        title=vacancy.find_element(By.CLASS_NAME, "g-h2").text,
        company=vacancy.find_element(By.CSS_SELECTOR, ".l-n > a").text,
        description=description,
        location=location,
        experience=exp.replace("< 1", "<1").split()[0],
        skills=skills,
    )


async def get_vacancies(driver: webdriver) -> [Vacancy]:
    all_vacancies = []
    exp = driver.find_element(By.CLASS_NAME, "selected").text

    await click_all_more_btn(driver)

    vacancy_links = driver.find_elements(By.CSS_SELECTOR, ".title > a")

    for link in vacancy_links:
        link.click()

        vacancy_detail = await parse_single_vacancy(driver, exp)
        all_vacancies.append(vacancy_detail)

        driver.back()

    driver.get(BASE_URL)
    return all_vacancies


def write_to_csv(output_csv_path: str, vacancies: [Vacancy]) -> None:
    with open(output_csv_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(VACANCY_FIELDS)
        writer.writerows([astuple(vacancy) for vacancy in vacancies])


async def get_all_vacancies() -> None:

    driver = webdriver.Chrome()
    driver.get(BASE_URL)

    driver.find_elements(By.CSS_SELECTOR, ".b-region-filter > ul:first-of-type > li")[1].click()
    beginner = await get_vacancies(driver)

    driver.find_elements(By.CSS_SELECTOR, ".b-region-filter > ul:first-of-type > li")[2].click()
    before_three_years = await get_vacancies(driver)

    driver.find_elements(By.CSS_SELECTOR, ".b-region-filter > ul:first-of-type > li")[3].click()
    before_five_years = await get_vacancies(driver)

    driver.find_elements(By.CSS_SELECTOR, ".b-region-filter > ul:first-of-type > li")[4].click()
    five_plus_years = await get_vacancies(driver)

    all_vacancies = beginner + before_three_years + before_five_years + five_plus_years
    write_to_csv("../data/vacancies.csv", all_vacancies)

    driver.close()
