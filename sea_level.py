import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    file = "sea_level_data.csv"
    df = pd.read_csv(file, dtype=str)

    # Create scatter plot
    df["Year"] = df["Year"].astype(float)
    df["CSIRO Adjusted Sea Level"] = df["CSIRO Adjusted Sea Level"].astype(float)
    a = df["Year"]
    b = df["CSIRO Adjusted Sea Level"]
    fig, ax = plt.subplots()
    plt.scatter(a, b)

    # Create first line of best fit
    line1 = linregress(a, b)
    x_predict = pd.Series(i for i in range(1880, 2050))
    y_predict = line1.slope*x_predict + line1.intercept
    plt.plot(x_predict, y_predict, "r")
    # Create second line of best fit
    # use conditional .loc for filtering the correct data in the whole dataframe
    new_df = df.loc[df["Year"] >= 2000]
    print(new_df)
    new_year = new_df["Year"]
    print(new_year)
    new_csiro = new_df["CSIRO Adjusted Sea Level"]
    print(new_csiro)
    line2 = linregress(new_year, new_csiro)
    x_pred = pd.Series(i for i in range(2000, 2050))
    y_pred = line2.slope*x_pred + line2.intercept
    plt.plot(x_pred, y_pred, "green")

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    # return plt.gca()
print(draw_plot())