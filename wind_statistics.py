"""
Wind Statistics
----------------

Topics: Using array methods over different axes, fancy indexing.

1. The data in 'wind.data' has the following format::

        61  1  1 15.04 14.96 13.17  9.29 13.96  9.87 13.67 10.25 10.83 12.58 18.50 15.04
        61  1  2 14.71 16.88 10.83  6.50 12.62  7.67 11.50 10.04  9.79  9.67 17.54 13.83
        61  1  3 18.50 16.88 12.33 10.13 11.17  6.17 11.25  8.04  8.50  7.67 12.75 12.71

   The first three columns are year, month and day.  The
   remaining 12 columns are average windspeeds in knots at 12
   locations in Ireland on that day.

   Use the 'loadtxt' function from numpy to read the data into
   an array.

2. Calculate the min, max and mean windspeeds and standard deviation of the
   windspeeds over all the locations and all the times (a single set of numbers
   for the entire dataset).

3. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds at each location over all the days (a different set of numbers
   for each location)

4. Calculate the min, max and mean windspeed and standard deviations of the
   windspeeds across all the locations at each day (a different set of numbers
   for each day)

5. Find the location which has the greatest windspeed on each day (an integer
   column number for each day).

6. Find the year, month and day on which the greatest windspeed was recorded.

7. Find the average windspeed in January for each location.

You should be able to perform all of these operations without using a for
loop or other looping construct.

Bonus
~~~~~

1. Calculate the mean windspeed for each month in the dataset.  Treat
   January 1961 and January 1962 as *different* months. (hint: first find a
   way to create an identifier unique for each month. The second step might
   require a for loop.)

2. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds across all locations for each week (assume that the first week
   starts on January 1 1961) for the first 52 weeks. This can be done without
   any for loop.

Bonus Bonus
~~~~~~~~~~~

Calculate the mean windspeed for each month without using a for loop.
(Hint: look at `searchsorted` and `add.reduceat`.)

Notes
~~~~~

These data were analyzed in detail in the following article:

   Haslett, J. and Raftery, A. E. (1989). Space-time Modelling with
   Long-memory Dependence: Assessing Ireland's Wind Power Resource
   (with Discussion). Applied Statistics 38, 1-50.


See :ref:`wind-statistics-solution`.
"""

import numpy as np 
from numpy import loadtxt

'''
1. The data in 'wind.data' has the following format::

        61  1  1 15.04 14.96 13.17  9.29 13.96  9.87 13.67 10.25 10.83 12.58 18.50 15.04
        61  1  2 14.71 16.88 10.83  6.50 12.62  7.67 11.50 10.04  9.79  9.67 17.54 13.83
        61  1  3 18.50 16.88 12.33 10.13 11.17  6.17 11.25  8.04  8.50  7.67 12.75 12.71

   The first three columns are year, month and day.  The
   remaining 12 columns are average windspeeds in knots at 12
   locations in Ireland on that day.

   Use the 'loadtxt' function from numpy to read the data into
   an array.
'''
array_data_wind = np.array(loadtxt(
   'D:\\simon\\Documents\\VisualCode\\venus\\ExerciseWind\\wind.data'))
#print(array_data_wind)
'''
2. Calculate the min, max and mean windspeeds and standard deviation of the
   windspeeds over all the locations and all the times (a single set of numbers
   for the entire dataset).
'''
def exe2(list):
   array_data_only_wind = list[:, 3:]

   min_wind = array_data_only_wind.min()
   max_wind = array_data_only_wind.max()
   mean_wind = array_data_only_wind.mean()

   array_std = np.std(array_data_only_wind) 
   return min_wind, max_wind, mean_wind, array_std

'''
3. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds at each location over all the days (a different set of numbers
   for each location)
'''

def exe3(list):
   array_data_only_wind = list[:, 3:]

   min_wind = array_data_only_wind.min(axis=0)
   max_wind = array_data_only_wind.max(axis=0)
   mean_wind = array_data_only_wind.mean(axis=0)
   array_std = np.std(array_data_only_wind, 0) 
   
   return min_wind, max_wind, mean_wind, array_std

'''
4. Calculate the min, max and mean windspeed and standard deviations of the
   windspeeds across all the locations at each day (a different set of numbers
   for each day)
'''
def exe4(list):
   array_data_only_wind = list[:, 3:]

   min_wind = array_data_only_wind.min(axis=1)
   max_wind = array_data_only_wind.max(axis=1)
   mean_wind = array_data_only_wind.mean(axis=1)
   array_std = np.std(array_data_only_wind, 1) 

   return min_wind, max_wind, mean_wind, array_std

'''
5. Find the location which has the greatest windspeed on each day (an integer
   column number for each day).
'''
def exe5(list):
   array_data_only_wind = list[:, 3:]

   return np.argmax(array_data_only_wind, 1)

'''
6. Find the year, month and day on which the greatest windspeed was recorded.
'''
def exe6(list):
   array_data_only_wind = list[:, 3:]
   array_data_only_times = list[:,:3]

   find_gratest_wind = array_data_only_wind.argmax()
   y = find_gratest_wind // array_data_only_wind.shape[1]  
   
   return array_data_only_times[y]

'''
7. Find the average windspeed in January for each location.
'''
def exe7(list):
   array_data_only_wind = list[:, 3:]
   array_data_only_times = list[:,1]

   find_gratest_january = np.argwhere(array_data_only_times == 1) 

   array_wind_only_january = array_data_only_wind[find_gratest_january]

   array_wind_average = np.average(array_wind_only_january, 0) 
   print(array_wind_average)
   return None

print(exe7(array_data_wind))