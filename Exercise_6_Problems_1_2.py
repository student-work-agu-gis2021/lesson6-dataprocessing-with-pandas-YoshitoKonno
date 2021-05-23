#!/usr/bin/env python
# coding: utf-8

# # Exercise 6: Weather data calculation
# 
# ### Part 1 
# 
# You should start by reading the data file.
# 
# - Read the data file into variable the variable `data`
#     - Skip the second row
#     - Convert the no-data values (`-9999`) into `NaN`

import pandas as pd
import numpy as np

data = None

# YOUR CODE HERE 1

# Read the data file. skip the second row and convert the no-data values into NaN.
data=pd.read_csv('data/1091402.txt',skiprows=[1],delim_whitespace=True,na_values=-9999)

# ### Part 2 
# 
# In this section, you will calculate simple statistics based on the input data:
# 
# - Calculate how many no-data (NaN) values there are in the `TAVG` column
#     - Assign your answer to a variable called `tavg_nodata_count`.

tavg_nodata_count = None

#YOUR CODE HERE 2

#variable 'a' means all columns of 'TAVG'
#tavg_nodata_count means count of nodata of 'TAVG'. 
a=data['TAVG']
tavg_nodata_count=a.isnull().sum()

#for i in range(tavg.length()):
 #if tavg[i]==-9999:
  # tavg_nodata_count=tavg_nodata_count+1


 

#CAUTION!!! DON'T EDIT THIS PART START
# Print out the solution:
print('Number of no-data values in column "TAVG":',tavg_nodata_count)
#CAUTION!!! DON'T EDIT THIS PART END


# - Calculate how many no-data (NaN) values there are for the `TMIN` column
#     - Assign your answer into a variable called `tmin_nodata_count`

tmin_nodata_count = None

#YOUR CODE HERE 3

#variable 'b' means all columns of 'TMIN'
#tmin_nodata_count means count of nodata of 'TMIN'.

b=data['TMIN']
tmin_nodata_count=b.isnull().sum()

#CAUTION!!! DON'T EDIT THIS PART START
# Print out the solution:
print('Number of no-data values in column "TMIN":', tmin_nodata_count)
#CAUTION!!! DON'T EDIT THIS PART END


# - Calculate the total number of days covered by this data file
#     - Assign your answer into a variable called day_count

day_count = None 
#YOUR CODE HERE 4
#variable 'c' means all columns of 'DATE'
#day_count means count of date 

c=data['DATE']
day_count=c.count()
#CAUTION!!! DON'T EDIT THIS PART START
# Print out the solution:
print("Number of days:", day_count)
#CAUTION!!! DON'T EDIT THIS PART END

# - Find the date of the oldest (first) observation
#     - Assign your answer into a variable called `first_obs`


first_obs = None
 
# YOUR CODE HERE 5

#first_obs means first columns of 'DATE'
first_obs = data['DATE'][0]

#CAUTION!!! DON'T EDIT THIS PART START
# Print out the solution:
print('Date of the first observation:',first_obs)
#CAUTION!!! DON'T EDIT THIS PART END

# - Find the date of the most recent (last) observation
#     - Assign your answer into a variable called `last_obs`

last_obs = None

# YOUR CODE HERE 6

#last_obs means last columns of 'DATE'
last_obs = data['DATE'][len(data['DATE'])-1]

#CAUTION!!! DON'T EDIT THIS PART START
# Print out the solution:
print('Date of the last observation:', last_obs)
#CAUTION!!! DON'T EDIT THIS PART END


# - Find the average temperature for the whole data file (all observtions) from column `TAVG`
#     - Assign your answer into a variable called `avg_temp`

avg_temp = None

# YOUR CODE HERE 7


sum_temp=0#sum_temp mean total of tempature but it doesn't include nodata
for i in range(len(data['TAVG'])-1):
  #if "data['TAVG'][i]" is not nodata, we add "data['TAVG'][i]" to sum_temp
  if(np.isnan(data['TAVG'][i])==False):
   sum_temp+=data['TAVG'][i]
#avg_temp means average tempature for the whole data file from column 'TAVG'  
avg_temp=sum_temp/(len(data['TAVG'])-tavg_nodata_count)

#CAUTION!!! DON'T EDIT THIS PART START
# Print out the solution:
print('Average temperature (F) for the whole dataset:', round(avg_temp, 2))
#CAUTION!!! DON'T EDIT THIS PART END


# - Find the average `TMAX` temperature over the Summer of 1969 (months May, June, July, and August of the year 1969)
#     - Assign your answer into a variable called `avg_temp_1969`

avg_temp_1969 = None

# YOUR CODE HERE 8

sum_temp_1969=0##sum_temp mean total of tempature in 1969 5/1~8/31 but it doesn't include nodata
sum_temp_1969_count=0#total of data in 1969 5/1~8/31
for i in range(len(data['TMAX'])-1):
  if(np.isnan(data['TMAX'][i])==False)and(data['DATE'][i]>=19690501)and(data['DATE'][i]<=19690831):
    sum_temp_1969+=data['TMAX'][i]
    sum_temp_1969_count+=1
#avg_temp_1969 means average tempature for the 1969 5/1~8/31 from column 'TAVG'
avg_temp_1969=sum_temp_1969/sum_temp_1969_count

#CAUTION!!! DON'T EDIT THIS PART START
# This test print should print a number
print('Average temperature (F) for the Summer of 69:', round(avg_temp_1969, 2))
#CAUTION!!! DON'T EDIT THIS PART END


# ## Problem 2 - Calculating monthly average temperatures (*3 points*)
# 

monthly_data = None

# YOUR CODE HERE 9

month=[]#month[i] means month of data['DATE'][i]
celsius_temp=[]#celsius_temp[i] means tempature of data['TAVG'] #convert Fahrenheit to Celsius 
total_temp=0#we use this variable to caluculate total of tempature each month  
day_count=0# we use this variable to count "day"
month_ave=[]#month_ave means data of all "total_temp/day_count"

for i in range(len(data['DATE'])-1):
  month.append(int(data['DATE'][i]%10000/100))
  celsius_temp.append((data['TAVG'][i]-32.0)/1.8)



for i in range(len(data['DATE'])-1):
  if(i==0):#in case, i=0
    total_temp+=celsius_temp[i]
    day_count+=1
  else:#in case, i≠0
    if(month[i-1]!=month[i]):
      month_ave.append(total_temp/day_count)
      total_temp=celsius_temp[i]
      day_count=1 #initialization of day_count
    else:
      total_temp+=celsius_temp[i]
      day_count+=1
month_ave.append(total_temp/day_count)
monthly_data=pd.DataFrame({'temp_celsius':month_ave})
      


   


#CAUTION!!! DON'T EDIT THIS PART START
# This test print should print the length of variable monthly_data
print(len(monthly_data))

# This test print should print the column names of monthly_data
print(monthly_data.columns.values)

# This test print should print the mean of temp_celsius
print(round(monthly_data['temp_celsius'].mean(),2))

# This test print should print the median of temp_celsius
print(round(monthly_data['temp_celsius'].median(), 2))
#CAUTION!!! DON'T EDIT THIS PART END

def func1():
    return tavg_nodata_count
def func2():
    return tmin_nodata_count
def func3():
    return day_count
def func4():
    return first_obs
def func5():
    return last_obs
def func6():
    return round(avg_temp,2)
def func7():
    return round(avg_temp_1969,2)
def func8():
    return len(monthly_data)
def func9():
    return monthly_data.columns.values
def func10():
    return round(monthly_data['temp_celsius'].mean(),2)
def func11():
    return round(monthly_data['temp_celsius'].median(),2)