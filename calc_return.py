"""
Calc return
===========

For a given stock, the return is connected to its close price p by

         p(t) - p(t-1)
ret(t) = -------------
             p(t-1)

The close price for Apple stock for all business days in 2008 is loaded for you
from the data file `aapl_2008_close_values.csv`.

1. Use these values to compute the corresponding daily return for every
business day of that year (except the first one).

2. Plot these returns, converted to percentages, over the course of the year.
On the same plot, draw a red line at 0.

Note: a for loop is neither necessary nor recommended for this calculation

Bonus
~~~~~
3. There is some blank space in the plot made in question 2 because by default,
matplotlib displays plots with a range along the x axis that is larger than the
highest x coordinate. Use IPython to learn about matplotlib's `plt.xlim` function
and make the limits of your plot tighter.
"""
from __future__ import print_function
from numpy import arange, loadtxt, zeros
import numpy as np
import matplotlib.pyplot as plt

prices = loadtxt('D:\\simon\\Documents\\VisualCode\\venus\\Exercise\\aapl_2008_close_values.csv', usecols=[1], delimiter=",")
'''
1. Use these values to compute the corresponding daily return for every
business day of that year (except the first one).
'''

def first_exercise(array_prices):
    return np.array([(array_prices[index] - array_prices[index-1]) / array_prices[index - 1]
            for index in np.arange(1,len(array_prices))])

def second_exercise(array_prices):
    fig, p_prices = plt.subplots()
    time_prices = np.arange(len(array_prices))
    #a = list(map(lambda x: x * 100, array_prices))
    #point_prices = np.array(a)
    point_prices = array_prices * 100

    p_prices.plot(time_prices, point_prices)

    p_prices.set(xlabel='Year 2018', ylabel='Prices in %',
                title='Percentages')

    p_prices.set(xticks = [])
    p_prices.grid()

    plt.show()

#to finish
def third_exercise(array_prices, padding=1):
    plt.xlim(- padding, len(array_prices) + padding)
    plt.show()

if __name__ == "__main__":
    print("Prices for AAPL stock in 2008:")
    print(prices)
    print('\nFirst exercise')
    returns = first_exercise(prices) 
    print(returns)
    print('\nSecond exercise')
    second_exercise(returns)
    print('\nthird_exercise')
    third_exercise(returns)
