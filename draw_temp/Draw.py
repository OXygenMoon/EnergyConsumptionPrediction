import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
if __name__ == '__main__':
    data_url = 'energydata_complete.csv'
    data_csv = pd.read_csv(data_url)
    _appliances = data_csv['Appliances']
    # print(_appliances)
    size = len(_appliances)
    x = range(0, size)
    plt.plot(x[:1000], _appliances[:1000])
    plt.show()