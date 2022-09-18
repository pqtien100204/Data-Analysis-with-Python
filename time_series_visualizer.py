import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from datetime import datetime
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
data_file = "time_series_data.csv"
df = pd.read_csv(data_file, dtype=str)
# transfer the data- split  the date into year-month-day column
list_of_splitted_date = list()
for index, item in df.loc[:, "date"].items():
    dat = item.split("-")
    if dat[0] == "2016":
        if dat[1] == "05" and dat[2] == "09":
            list_of_splitted_date.append([int(dat[0]), int(dat[1])])
        elif dat[1] != "05" and dat[2] ==  "01":
            list_of_splitted_date.append([int(dat[0]), int(dat[1])])
    elif dat[0] in ["2017", '2018', '2019'] and dat[2] == "01":
        list_of_splitted_date.append([int(dat[0]), int(dat[1])])

date_ele_list = {}

date_ele_list["Year"] = list(list_of_splitted_date[iii][0] for iii in range(0, len(list_of_splitted_date)))
date_ele_list["Month"] = list(list_of_splitted_date[iii][1] for iii in range(0, len(list_of_splitted_date)))
# date_ele_list["Day"] =list(list_of_splitted_date[iii][2] for iii in range(0, len(list_of_splitted_date)))
list_of_value_for_month = list()
for indexung, valung in df.loc[:, "value"].items():
    ola = df.at[indexung, "date"].split("-")
    if ola[0] == "2016":
        if ola[1] == "05" and ola[2] == "09":
            list_of_value_for_month.append(int(valung))
        elif ola[2] ==  "01":
            list_of_value_for_month.append(int(valung))
    elif ola[0] in ["2017", '2018', '2019'] and ola[2] == "01":
        list_of_value_for_month.append(int(valung))

datafr = pd.DataFrame({'year': date_ele_list["Year"], 'month': date_ele_list["Month"], "value": list_of_value_for_month})
# create a copy to extract date and month out of the date category
# dataframee = pd.DataFrame()
# dataframee["date_copy"] = df["date"]
# df.set_index("date", inplace=True)

# Clean data
# df = df[
#     (df["value"] >= df["value"].quantile(0.025)) &
#     (df["value"] <= df["value"].quantile(0.975))
# ]

# Get the Year and Month 
# extracting month and year from the date column
# dataframee["date_copy"] = pd.to_datetime(dataframee["date_copy"])
# dataframee["date_copy"] = dataframee["date_copy"].dt.to_period('M')
# dataframee["date_copy"] = dataframee["date_copy"].dt.strftime('%Y-%m')

# set a DISTINCT list of date 
# m_y = set(dataframee["date_copy"])
# dist_y_m = list(m_y)

# arrange by ASC order
# dist_y_m.sort(key = lambda date: datetime.strptime(date, '%Y-%m'))
# dtlist = range(2, len(list(dist_y_m)), 6)
# datetime_data = list()
# for i in dtlist:
#     datetime_data.append(dist_y_m[i])

# Get the Viewing values
# value = list(df["value"])
# value_data = list()
# for valuu in df.index:
#     value = valuu.split("-")
#     for valuee in datetime_data:
#         valuing = valuee.split("-")
#         if (value[0] == valuing[0]) and (value[1] == valuing[1]) and (value[2] == '01'):
#             value_data.append(df.at[valuu, "value"])
# value_data = sorted(value_data)

# although the freecodecamp project require me to use matplotlib but my laptop does not let me doing that sooooo i use seaborn
def draw_line_plot():
        # plt.subplots() is a function that returns a tuple containing a figure and axes object(s)
        # The fig object to be used as a container for all the subplots.
        # ax: 1 obj in the axes.Axes obj if there is 1 plot. a set of obj in the axes.Axes obj if there is many plots
    fig, ax = plt.subplots(figsize=(10,5)) 
    # ax.plot(datetime_data, value_data, "r", linewidth=1)  # Plot y versus x as lines and/or markers.

    # sth = datafr.pivot_table(values="value", index=["year", "month"], aggfunc='mean')
    views_wide = datafr.pivot("year", "month", "value")
    ax = sns.lineplot(data=views_wide)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    fig.savefig("nehe.png")
print(draw_line_plot())

def draw_bar_plot():
    # Draw bar plot
    sns.barplot(data=datafr, y='value', x='year', hue='month')
    # datafr.pivot('year','month','value').plot.bar()
    plt.savefig("bar_plot2.png")

def draw_box_plot():
    # Prepare data for box plots (this part is done!). I will again start from scratch, using the {df}
    df['date'] = pd.to_datetime(df['date'])
    df_box = df.copy()
    # df_box.reset_index(inplace=True)

    # strftime() is for formatting *{date objects}* which contains datetime values into readable strings.
    df_box["year"] = [d.year for d in df_box.date]
    df_box["month"] = [d.strftime('%m') for d in df_box.date]
    # df_box["month_number"] = df_box["date"].dt.month
    df_box = df_box.sort_values("month")  # sort so that the month chart starts with January instead of May in 2016
    df_box["value"] = df_box["value"].astype(int)
    df_box["month"] = df_box["month"].astype(int)
    # use normal loop to split a string value(show datetime)
    # df_box['year'] = [int(valui.split('-')[0]) for valui in df_box['date']]
    # df_box['month'] = [int(valui.split('-')[1]) for valui in df_box['date']]
    print(df_box)
    print(df_box.dtypes)
    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10,5))  # because we generate 2 chart for year and month => use axes(this is a set, not an obj) and columns == 2
    axes[1] = sns.boxplot(x="month", y="value", data=df_box, ax = axes[1])
    axes[0] = sns.boxplot(x="year", y="value", data=df_box, ax = axes[0])

    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Years")
    axes[0].set_ylabel("Page Views")

    axes[1].set_title(" Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Months")
    axes[1].set_ylabel("Page Views")
    
    fig.savefig("box_plot_month3.png")
