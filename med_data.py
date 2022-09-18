import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Read data from the csv file
file = 'raw_med_data.csv'
df = pd.read_csv(file, dtype=str)

# Create a overweight column with the proper calculation
df["weight"] = df["weight"].astype(float)
for i, v in df.loc[:, "weight"].items():
    bmi = float(v) / float((float(df.at[i, 'height']) / 100) ** 2)
    if bmi > 25:
        df.at[i, "overweight"] = 1    # overweight
    else:
        df.at[i, "overweight"] = 0    # not overweight

# use list comprehension
# df["weight"] = df["weight"].astype(float)
# df["height"] = df["height"].astype(float)
# df["overweight"] = ((df["weight"]) / (df["height"] / 100 ** 2)).apply(lambda x:1 if x > 25 else 0)

# Normalize data by making 0 always good and 1 always bad. 
# If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
for ind, val in df.loc[:, "cholesterol"].items():
    if int(val) == 1:
        df.at[ind, "cholesterol"] = 0
    else:
        df.at[ind, "cholesterol"] = 1

for ind, val in df.loc[:, "gluc"].items():
    if int(val) == 1:
        df.at[ind, "gluc"] = 0
    else:
        df.at[ind, "gluc"] = 1

# use list comprehension
# df["cholesterol"] = df["cholesterol"].apply(lambda x:0 if x == 1 else 1)
# df["gluc"] = df["gluc"].apply(lambda x:0 if x == 1 else 1)

# apply() => Apply a function along an axis of the DataFrame.

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['active', 'alco', 'cholesterol', "gluc", "overweight", "smoke"])
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat["total"] = int()   # this is set for storing the counting result
    df_cat = df_cat.groupby(["cardio", "variable", "value"], as_index = False).count()  # groupby() group the value of columns of a DataFrame by using the specified column
    # df_cat = df.groupby("cardio").active.value_counts() this is groupby for Series not DataFrame 
    
    # Draw the catplot with 'sns.catplot()'
    # fig, ax = plt.subplots()
    fig = sns.catplot(x="variable", y="total", data=df_cat, hue="value", kind="bar",  col="cardio")

    # Save the plot into a file
    fig.savefig('med_cate.png')

# change the type of columns in df into int
df = df.astype("int")

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    # df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
    #             (df['height'] >= (df.height.quantile(0.025))) &
    #             (df['height'] <= (df.height.quantile(0.975))) &
    #             (df['weight'] >= (df.weight.quantile(0.025))) &
    #             (df['weight'] <= (df.weight.quantile(0.975)))]

    # df_heat = pd.DataFrame({"id": df["id"], "age": df["age"], "sex": df["sex"], "height": df["height"], "weight": df["weight"], "ap_hi": df["ap_hi"], "ap_lo": df["ap_lo"], "cholesterol": df["cholesterol"], "gluc": df["gluc"], "smoke": df["smoke"], "alco": df["alco"], "active": df["active"], "cardio": df["cardio"], "overweight": df["overweight"]})
    
    # Calculate the correlation matrix
    corr = df.corr(method="pearson") # Correlation between different variables

    # Generate a mask for the upper triangle
    # mask = np.triu(np.ones_like(corr))   # Return a copy of an array with the elements below the k-th diagonal zeroed.
    # Return an array of ones with the same shape and type as a given array. ( two_like(), three_like())
    
    mask = np.triu(corr)
    
    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12)) # just modifying the size of the plot we're drawing

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, mask=mask, square=True, annot=True, vmin=-0.1, vmax=2)

    # # Save the heatmap into a file
    fig.savefig("med_heat.png")

print(draw_heat_map())