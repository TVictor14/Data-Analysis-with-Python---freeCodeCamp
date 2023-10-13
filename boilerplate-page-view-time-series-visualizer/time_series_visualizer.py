import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
df.set_index('date',inplace=True)

# Clean data
df = df.sort_values(by='value', ascending=True)
cut = round(df.size*0.025)
df = df.drop(df.index[:cut]).drop(df.index[-cut:])
df = df.sort_values(by='date', ascending=True)

def draw_line_plot():

    # Draw line plot
    fig, ax = plt.subplots(figsize=(18,6))
    plt.plot(df.index, df['value'], 'r')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():

    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar = df_bar.reset_index()
    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.month_name()
    df_bar = df_bar.drop(['date'],axis = 1)
    df_bar = df_bar.groupby(['year','month'],as_index=False).mean()

    #Draw bar plot
    labels=[
            'January','February','March','April',
            'May','June','July','August',
            'September','October','November','December'
            ] 

    fig, ax = plt.subplots(figsize=(10, 10))

    sns.barplot(
                data=df_bar, 
                x='year', y='value',hue='month',
                hue_order = labels,
                palette=sns.color_palette('tab10')
               )
    plt.ylabel('Average Page Views')
    plt.xlabel('Years')
    plt.legend(title = 'Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():

    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2,figsize=(20,10))

    sns.boxplot(
      data=df_box, x='year', y='value',
      hue='year',legend=False, ax=ax[0],
      palette=sns.color_palette(),
      flierprops={'marker': 'd'}
    )

    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_ylabel('Page Views')
    ax[0].set_xlabel('Year')

    sns.boxplot(
                data=df_box, x='month', y='value',
                hue='month',legend=False,
                ax=ax[1],order =['Jan', 'Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
                ,palette=sns.color_palette(),
               flierprops={'marker': 'd', 'markersize':'12','fillstyle': 'full'}
               )


    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_ylabel('Page Views')
    ax[1].set_xlabel('Month')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
