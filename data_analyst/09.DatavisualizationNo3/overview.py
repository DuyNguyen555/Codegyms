import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == '__main__':
    sns.set_theme(style="darkgrid")
    x = [1, 2, 3, 4, 5] 
    y = [1, 5, 4, 7, 4]
    tips = sns.load_dataset("tips")
    print(type(tips))
    print(tips.head())
    
    sns.lineplot(x, y)
    plt.show()
    