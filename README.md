# Analysis job technologies

## Description:
Program for parsing public information about vacancies for Python developer from site `Dou.ua`, save into csv file
and analyse this information and creation graphics
1. `What technologies are used in vacancies and how murch`
2. `The same technologies but divided into categories of experience`
3. `Locations for which vacancies are offered`
4. `How murch vacancies for every categories of experience`
5. `Top 10 companies by the largest number of vacancies`

## How to look like diagrams

![frequency_technologies_2024-01-10_180634.png](data%2Fplots%2Ffrequency_technologies_2024-01-10_180634.png)
![frequency_technologies_with_exp2024-01-10_172437.png](data%2Fplots%2Ffrequency_technologies_with_exp2024-01-10_172437.png)
![cities_in_vacancies_2024-01-10_172438.png](data%2Fplots%2Fcities_in_vacancies_2024-01-10_172438.png)
![vacancies_by_experience_2024-01-10_172439.png](data%2Fplots%2Fvacancies_by_experience_2024-01-10_172439.png)


## How to use
1. Open terminal and clone the repo (`git clone https://github.com/prochigor/analysis-job-technologies.git`)
2. Open the project with your IDE
3. Activate venv on the project
   - Open terminal and write: 
     - On Windows: (`python -m venv venv`) and (`venv\Scripts\activate`)
     - On Mac: (`python3 -m venv venv`) and (`source venv/bin/activate`)
4. Install requirements
  Write in terminal (`pip install -r requirements.txt`)
5. Open file `main.py` in folder `app` and run the project
6. Wait for program is working
7. You are welcome, in folder `data` file `vacancies.csv` with data and folder `plots` with all graphics
