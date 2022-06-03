import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def distribution_word(data):
    sns.set(style='darkgrid', palette='Set1')
    sns.violinplot(y="GDP (millions of US$)", data=data)
    plt.show()

def distribution_asian(data):
    sns.set(style='darkgrid', palette='Set2')
    sns.violinplot(y=data[data['Continent']=="Asia"]["GDP (millions of US$)"], data=data)
    plt.show()

def Box(data):
    sns.set(style='darkgrid', palette='Set3')
    sns.boxplot(x='Continent' ,y='GDP (millions of US$)', data=data)
    plt.show()

if __name__ == '__main__':
    df = pd.read_csv('09.DatavisualizationNo3\data\GDPlist.csv', encoding='ISO-8859-1')
    
    # Visualization
    distribution_word(df)
    distribution_asian(df)
    Box(df)