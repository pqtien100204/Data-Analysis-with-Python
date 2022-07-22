import pandas as pd
import csv

def calculate_demographic_data(print_data=False):
    # Read data from file with csv module

    # with open('demographic_analyser.csv', 'r') as filee: # "r" mode: reading mode => it have just taken to the file, not read it
    #     dff = csv.reader(filee, delimiter=",")
    #     next(dff)  # skipping header
    #     listt = []
    #     for index, content in enumerate(dff):    enumerate() create a list by adding serial number aside every value in a DataFrame,...
    #         if content[8]  not in listt:
    #             listt.append(content[8])
    #     print(listt)


    # Read data from file as Pandas DataFrame
    file = 'demographic_analyser.csv'
    df = pd.read_csv(file, dtype=str)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_list = {}
    # print(df.loc[:, "race"])   # !!!!testing!!!!
    for index, value in df.loc[:, "race"].items(): # Access a group of rows and columns by label with formula (row_of_value_to_access, (opt)the_fied,column_to_take_vlue_from)
        if value not in race_list.keys():
            race_list[value] = 1
        elif value in race_list.keys():
            race_list[value] += 1
    race_count = race_list.values()

    # What is the average age of men?
    age_of_men = []
    for index, value in df.loc[:, "sex"].items():
        if value == "Male":
            age_of_men.append(int(df.at[index, "age"]))    # Similar to loc, in that both provide label-based lookups. Use at if you only need to get or set a single value in a DataFrame or Series.
    average_age_men = round(int(sum(age_of_men)) / int(len(age_of_men)), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bach_de = []
    for index, value in df.loc[:, "education"].items():
        if value == "Bachelors":
            bach_de.append(value)
    # print(df['education'].size)   # return number of row for a speciic column
    # print(df.size)    # return number of rows * number of columns
    percentage_bachelors = round((len(bach_de) / df['education'].size) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = {}
    lower_education = {}
    for index, value in df.loc[:, "education"].items():
        if value in ["Bachelors", "Masters", "Doctorate"]:
            higher_education[index] = value
        else:
            lower_education[index] =  value

    # percentage with salary >50K
    list_h_r = []
    list_l_r = []
    for educated_id, educated_peo in higher_education.items():
        if df.at[educated_id, 'salary'] == ">50K":
            list_h_r.append(df.at[educated_id, 'salary'])
    for educated_id, educated_peo in lower_education.items():
        if df.at[educated_id, 'salary'] == ">50K":
            list_l_r.append(df.at[educated_id, 'salary'])

    higher_education_rich = round((len(list_h_r) / len(higher_education)) * 100, 1)
    lower_education_rich =  round((len(list_l_r) / len(lower_education)) * 100, 1)
    
    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min = (24 * 7)
    for vall in df.loc[:, 'hours-per-week']:
        if int(vall) < int(min):
            min = vall
    min_work_hours = min

    amount_of_min_worker = list(df.loc[:, 'hours-per-week']).count(min_work_hours)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers_but_rich = []
    for ind, val in df.loc[:, 'hours-per-week'].items():
        if val == min_work_hours:
            if df.at[ind, 'salary'] == '>50K':
                min_workers_but_rich.append(df.at[ind, 'salary'])

    rich_percentage = int((len(min_workers_but_rich) / amount_of_min_worker) * 100)

    # What country has the highest percentage of people that earn >50K?
    country_with_its_highest_earning = {}
    for indd, vaal in df.iloc[:, 13].items():
        if (vaal not in country_with_its_highest_earning) and (df.iloc[indd, 14] == ">50K"):
            country_with_its_highest_earning[vaal] = 1
        elif (vaal in country_with_its_highest_earning) and (df.iloc[indd, 14] == ">50K"):
            country_with_its_highest_earning[vaal] += 1
    print(country_with_its_highest_earning)
    
    # country_in_name = list(country_with_its_highest_earning.keys())
    # country_in_figure = list(country_with_its_highest_earning.values())
    # richest_country_in_figure = max(country_in_figure)
    # the_position = country_in_figure.index(richest_country_in_figure)

    total_country_both_high_and_low_earning = {}
    for iiii, people_in_evr_coun in df.iloc[:, 13].items():
        if (people_in_evr_coun in list(country_with_its_highest_earning.keys())) and (people_in_evr_coun not in total_country_both_high_and_low_earning.keys()):
            total_country_both_high_and_low_earning[people_in_evr_coun] = 1
        else:
            total_country_both_high_and_low_earning[people_in_evr_coun] += 1      
    print(total_country_both_high_and_low_earning)      

    result_with_country_and_percent = {}
    for indexing, valueing in country_with_its_highest_earning.items():
        for indesing, valueyng in total_country_both_high_and_low_earning.items():
            if indexing == indesing:
                result_with_country_and_percent[indexing] = (valueing / valueyng) * 100
  
    country_in_name = list(result_with_country_and_percent.keys())
    country_in_figure = list(result_with_country_and_percent.values())
    richest_country_in_figure = max(country_in_figure)
    the_position = country_in_figure.index(richest_country_in_figure)
    highest_earning_country = country_in_name[the_position]

    highest_earning_country_percentage = round(country_in_figure[the_position], 1)

    # Identify the most popular occupation for those who earn >50K in India.
    jobs_for_rich = {}
    for number, people in df.iloc[:, 13].items():
        if people == "India" and df.at[number, 'salary'] == ">50K":
            if df.at[number, 'occupation'] not in jobs_for_rich.keys():
                jobs_for_rich[df.at[number, 'occupation']] = 1
            elif df.at[number, 'occupation'] in jobs_for_rich.keys():
                jobs_for_rich[df.at[number, 'occupation']] += 1

    jobs_in_name = list(jobs_for_rich.keys())
    jobs_in_figure = list(jobs_for_rich.values())
    most_popular_jobs_values = max(jobs_in_figure)
    position = jobs_in_figure.index(most_popular_jobs_values)
    top_IN_occupation = jobs_in_name[position]

    # DO NOT MODIFY BELOW THIS LINE

    # if print_data:
    #     print("Number of each race:\n", race_count) 
    #     print("Average age of men:", average_age_men)
    #     print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    #     print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
    #     print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
    #     print(f"Min work time: {min_work_hours} hours/week")
    #     print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
    #     print("Country with highest percentage of rich:", highest_earning_country)
    #     print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
    #     print("Top occupations in India:", top_IN_occupation)

    # return {
    #     'race_count': race_count,
    #     'average_age_men': average_age_men,
    #     'percentage_bachelors': percentage_bachelors,
    #     'higher_education_rich': higher_education_rich,
    #     'lower_education_rich': lower_education_rich,
    #     'min_work_hours': min_work_hours,
    #     'rich_percentage': rich_percentage,
    #     'highest_earning_country': highest_earning_country,
    #     'highest_earning_country_percentage':
    #     highest_earning_country_percentage,
    #     'top_IN_occupation': top_IN_occupation
    # }


calculate_demographic_data()
