import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt
import math
import codecademylib3


## Read in Data
flight = pd.read_csv("flight.csv")
print(flight.head())

## Task 1
#Drawing a box plot for coach ticket prices to investigate the spread of the values
sns.boxplot(flight["coach_price"])
plt.title("Coach Ticket Prices")
plt.show()
plt.clf()
#Calculating mean and median values of coach ticket prices
coach_mean = np.mean(flight.coach_price)
coach_median = np.median(flight.coach_price)
print("The mean and median coach prices are {} and {} dollars respectively.".format(coach_mean, coach_median))
## Task 2
#Visualizing the coach ticket prices for only flights that are 8 hours long
flight_8hrs = flight[flight.hours == 8]
print(flight_8hrs.head())
sns.boxplot(flight_8hrs.coach_price)
plt.show()
plt.clf()
#Calculating mean and median values for coach prices of values that are 8 hours long
coach8_mean = np.mean(flight_8hrs.coach_price)
coach8_median = np.median(flight_8hrs.coach_price)
print("The mean and median coach prices for flights that are 8 hours long are {} and {} dollars respectively.".format(coach8_mean, coach8_median))
## Task 3
#Visualizing the distribution of flight delay times using a histogram
#plt.hist(flight.delay)
#plt.title("Distribution of Flight Delay Times")
#The data is highly skewed so subsetting the data to only include 10 minutes delays
plt.hist(flight.delay[flight.delay <= 10])
plt.title("Distribution of Flight Delay Times Less Than 10 Minutes")
plt.show()
plt.clf()
## Task 4
#Creating a visualization to observe the relationship between coach and first-class prices using a scatter plot
#sns.scatterplot(data = flight, x = "coach_price", y = "firstclass_price")
#The data points in the plot are crowded together with some overlappings so drawing a LOWESS smoother over a sample (10%) of the data in order to be able to see the association
perc = 0.1
flight_sub = flight.sample(n = int(flight.shape[0]*perc))
sns.lmplot(data = flight_sub, x = "coach_price", y = "firstclass_price", line_kws = {"color": "black"},lowess = True)
plt.title("Coach Prices Vs. First Class Prices")
plt.show()
plt.clf()
## Task 5
#Finding out if there is a relationship between coach price and any of the inflight features using histograms
sns.histplot(data = flight, x = "coach_price", hue = "inflight_meal")
plt.title("Distribution of Coach Price With Respect to Inflight Meal")
plt.show()
plt.clf()
sns.histplot(data = flight, x = "coach_price", hue = "inflight_entertainment")
plt.title("Distribution of Coach Price With Respect to Inflight Entertainment")
plt.show()
plt.clf()
sns.histplot(data = flight, x = "coach_price", hue = "inflight_wifi")
plt.title("Distribution of Coach Price With Respect to Inflight Wifi")
plt.show()
plt.clf()
## Task 6
#Finding the association between the number of passengers and the length of flights
#sns.scatterplot(data = flight, x = "passengers", y = "hours")
#Adding a jitter to help spread the points out as there are too many points in the same place
sns.lmplot(data = flight, x = "passengers", y = "hours", x_jitter = 0.15, y_jitter = 0.15, fit_reg = False)
plt.title("Number of Passengers Vs. Flight Hours")
plt.show()
plt.clf()
#Visualizing the relationship between coach and first-class prices compared to weekdays
sns.lmplot(data = flight, x = "coach_price", y = "firstclass_price", hue = "day_of_week")
plt.title("Coach Prices Vs. First Class Prices for Each Day")
plt.show()
plt.clf()
## Task 8
#Visualizing how coach prices differ for redeyes and non-redeyes on each day of the week
sns.barplot(data = flight, x = "redeye", y = "coach_price", hue= "day_of_week")
plt.title("Coach Prices for Redeyes on Each Day of the Week")
plt.show()