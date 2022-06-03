import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def ditribution_chart(data):
    """Biểu đồ phân bố"""
    sns.set(style='darkgrid', palette='Set1')
    # sns.violinplot(y='Price', data=data)
    
    data_len = data.groupby(by=['InvoiceNo'])['Quantity'].sum().reset_index()
    sns.violinplot(y='Quantity', data=data_len)
    plt.show()
    
def histogram(data):
    """Biểu đồ tần số"""
    sns.set(style='darkgrid', palette='magma')
    
    data_count = data.drop_duplicates(subset='InvoiceNo')
    sns.countplot(x='Country', data=data_count)
    plt.show()

def box(data):
    """Biểu đồ box plot"""
    sns.set(style='darkgrid', palette='Set2')
    
    # sns.boxplot(x=data['UnitPrice'])
    sns.boxplot(x=data['Quantity'])
    
    plt.show()

if __name__ == '__main__':
    df = pd.read_csv('09.DatavisualizationNo3\data\OnlineRetail.csv', encoding='ISO-8859-1')
    df.dropna(inplace=True)
    df['Price'] = df['Quantity'] * df['UnitPrice']

    # Visualization
    ditribution_chart(df)
    histogram(df)
    box(df)
