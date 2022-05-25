import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def LmPlot(data1, data2):
    sns.set(style="darkgrid", palette="Set1")
    
    sns.lmplot(x="Year", y="Price", data=data1, hue="ProductName")
    plt.show()
    
    sns.lmplot(x="Year", y="Price", data=data2, hue="ProductName")
    plt.show()

def ViolinPlot(data):
    sns.set(style="whitegrid", palette="Set2")
    
    sns.violinplot(y="Price", data=data)
    plt.show()
    
    sns.violinplot(y = "Year", data=data)
    plt.show()

def CountPlot(data):
    sns.set(style="whitegrid")
    
    sns.countplot(x="Year", data=data)
    plt.show()
    
    sns.countplot(x="Year", hue="Place", data=data)
    plt.show()

def BoxPlot(data):
    sns.boxplot(x=data["Price"])
    plt.show()
    
    sns.boxplot(x=data["Year"], y=data["Price"])
    plt.show()

if __name__ == '__main__':
    df = pd.read_csv("09.DatavisualizationNo3\data\FoodPrice_in_Turkey.csv")
    df = df.dropna()
    # print(df.info())
    # print(df.describe())
    
    # Vẽ biểu đồ xu hướng
    rice_df = df[df["ProductId"] == 52]
    trans_df = df[(df["ProductName"] == "Transport (public) - Retail") | (df["ProductName"] == "Rice - Retail")]
    LmPlot(rice_df, trans_df)
    
    # Vẽ biểu đồ phân bố
    ViolinPlot(df)
    
    # Vẽ biểu đồ tần số
    CountPlot(df)
    
    # Vẽ biểu đồ box plot
    BoxPlot(df)