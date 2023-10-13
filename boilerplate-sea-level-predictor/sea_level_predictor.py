import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():

    # Read data from file
    df = pd.read_csv('epa-sea-level.csv',na_values=None)
    #print(df.dtypes())
    # Create scatter plot

    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y, color='black')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x,y)

    x_ext1 = pd.Series(range(1880,2051))
    plt.plot(x_ext1, slope * x_ext1 + intercept, color='blue')

    # Create second line of best fit

    x_interval = df[df['Year'] >= 2000]['Year']
    y_interval = df[(df['Year'] >= 2000)]['CSIRO Adjusted Sea Level']
    
    slope, intercept, r_value, p_value, std_err = linregress(x_interval,y_interval)
    x_ext2 = pd.Series(range(2000,2051))
  
    plt.plot(x_ext2, slope * x_ext2 + intercept, color='red')

    #fig = plt.show()

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()