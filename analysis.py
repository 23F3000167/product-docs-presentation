# Interactive Data Analysis Notebook using Marimo
# Author: Data Scientist
# Email: 23f3000167@ds.study.iitm.ac.in

import marimo

__generated_with = "0.7.13"
app = marimo.App()

# Cell 1: Import libraries and load dataset
# Data flow: This provides the dataset used in later analysis
@app.cell
def __(pd):
    import seaborn as sns
    df = sns.load_dataset("tips")
    df.head()
    return df

# Cell 2: User control with slider widget
# Data flow: Slider value will control which variable to analyze
@app.cell
def __(mo):
    var_slider = mo.ui.slider(start=0, stop=1, step=1, label="Choose variable: 0 = total_bill, 1 = tip")
    var_slider
    return var_slider

# Cell 3: Dynamic variable selection based on slider
# Data flow: Uses slider value to select correct column from dataset
@app.cell
def __(df, var_slider):
    var_map = {0: "total_bill", 1: "tip"}
    chosen_var = var_map[var_slider.value]
    selected_data = df[chosen_var]
    (chosen_var, selected_data.describe())
    return chosen_var, selected_data

# Cell 4: Visualization depending on slider choice
# Data flow: selected_data from previous cell is plotted
@app.cell
def __(plt, selected_data, chosen_var):
    import matplotlib.pyplot as plt
    plt.hist(selected_data, bins=20, color="skyblue", edgecolor="black")
    plt.title(f"Distribution of {chosen_var}")
    plt.xlabel(chosen_var)
    plt.ylabel("Frequency")
    plt.show()

# Cell 5: Dynamic markdown output
# Data flow: Markdown text updates when slider is moved
@app.cell
def __(mo, chosen_var):
    mo.md(f"### Currently Analyzing: **{chosen_var}**")


if __name__ == "__main__":
    app.run()
