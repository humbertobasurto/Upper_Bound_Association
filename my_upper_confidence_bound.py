import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

#implementation
import math
N = 10000
d = 10
ads_selected = []
number_of_selections = [0] * d
sums_of_reward = [0] * d
total_reward = 0
for n in range(0, N):
    ad = 0
    max_upper_bound = 0
    for i in range(0, d):
        if (number_of_selections[i]> 0 ):
            average_reward = sums_of_reward[i] / number_of_selections[i]
            delta_i = math.sqrt(3/2 * math.log(n + 1)/number_of_selections[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    number_of_selections[ad] =  number_of_selections[ad] + 1
    reward = dataset.values[n, ad]
    sums_of_reward[ad] = sums_of_reward[ad] + reward
    total_reward = total_reward + reward
#plotting a histogram
plt.hist(ads_selected)
plt.title('histogram of ads selection')
plt.xlabel('ads')
plt.ylabel('number of times ad was selected')
plt.show()