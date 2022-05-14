import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    gaussian_numbers = np.random.normal(size=1000)
    # plt.hist(gaussian_numbers, bins=35, range=(-1,1))
    # plt.hist(gaussian_numbers, bins=35, density=True)
    # plt.hist(gaussian_numbers, bins=35, cumulative=True)
    # plt.hist(gaussian_numbers, bins=35, cumulative=True, histtype='step')
    plt.hist(gaussian_numbers, bins=35, orientation='horizontal')
    
    plt.title("Histogram example", fontsize=20, fontweight=100, color='r')
    plt.show()