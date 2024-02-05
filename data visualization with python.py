# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 15:16:32 2023

@author: busola
"""

# Load the dataset into a data frame using Python.
# Clean the data as needed.
# Plot a line chart to show the average temperature fluctuations in Tunisia and Cameroon. Interpret the results.
# Zoom in to only include data between 1980 and 2005, try to customize the axes labels.
# Create Histograms to show temperature distribution in Senegal between [1980,2000] and [2000,2023] (in the same figure). Describe the obtained results.
# Select the best chart to show the Average temperature per country.
# Make your own questions about the dataset and try to answer them using the appropriate visuals.
 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
# import seaborn as sns
from sklearn.impute import SimpleImputer
# from ydata_profiling import ProfileReport
# import plotly.express as px
# Load the dataset into a data frame using Python.
data = pd.read_csv("Africa_climate_change.csv")

descriptive = data.describe()
unique = data["COUNTRY"].unique()
taverage = data["TAVG"].unique()
# profile = ProfileReport(data, title = "visualization data")
# profile.to_file("visualization data.html")


data["DATE"] = pd.to_datetime(data['DATE'])

info = data.info()

#question 1
tunisia = data[data["COUNTRY"] == 'Tunisia']
cameroon= data[data["COUNTRY"] == "Cameroon"]

average_temp_tunisia = tunisia.groupby("DATE")["TAVG"].mean().reset_index()
average_temp_cameroon = cameroon.groupby("DATE")["TAVG"].mean().reset_index()

#using matplotlib
plt.figure(figsize = (15,10))
plt.plot(average_temp_tunisia["DATE"],average_temp_tunisia["TAVG"])
plt.plot(average_temp_cameroon["DATE"],average_temp_cameroon["TAVG"])
plt.xlabel("Date", fontsize = 12,labelpad = 20)
plt.ylabel("AVERAGE TAVG",fontsize = 12,labelpad = 20)
plt.show()
#using pandas
graph = data.plot(kind = "line",x = "DATE", y = "TAVG", title = "graph of country and average temp with time",color = "green", figsize = (15,10))
plt.show()
#using plotly
# graph_px = px.line(average_temp_tunisia["DATE"],average_temp_tunisia["TAVG"], markers = True,title = "graph of country and average temp with time")
# plt.show()
# graph_px.write_html("graph of country and average temp with time",auto_open = True)

#question 2
data_tunisia2 = data[(data["COUNTRY"] == "Tunisia") & (pd.to_datetime(data["DATE"]).dt.year <= 2005)]
data_cameroon2 = data[(data["COUNTRY"] == "Cameroon") & (pd.to_datetime(data["DATE"]).dt.year <= 2005)]

temp_tunisia_zoom = data_tunisia2.groupby("DATE")["TAVG"].mean().reset_index()
temp_cameroon_zoom = data_cameroon2.groupby("DATE")["TAVG"].mean().reset_index()

plt.figure(figsize = (20,15))
plt.plot(temp_tunisia_zoom["DATE"],temp_tunisia_zoom["TAVG"], markersize = 12)
plt.title("1980 to 2005")
plt.xlabel("date", labelpad = 20)
plt.ylabel("temperature average", labelpad = 20)
plt.show()

plt.figure(figsize = (200, 70))
plt.plot(temp_tunisia_zoom["DATE"], temp_tunisia_zoom["TAVG"])
plt.xlabel("Dates", labelpad = 20, fontsize = 150)
plt.ylabel("Average Temperature", labelpad = 20, fontsize = 150)
plt.title("Analyzing the average temperature fluctuations in Cameroon (1980 - 2005)", fontsize = 150, pad = 20)
plt.show()

#QUESTION 3
data_senegal_1980 = data[(data["COUNTRY"] == "Senegal") & (pd.to_datetime(data["DATE"]).dt.year <= 2000)]
senegal_temp_1980 = data_senegal_1980.groupby("DATE")[["TAVG","TMAX","TMIN"]].mean().reset_index()

data_senegal_2000 = data[(data["COUNTRY"] == "Senegal") & (pd.to_datetime(data["DATE"]).dt.year >= 2000)]
senegal_temp_2000 = data_senegal_2000.groupby("DATE")[["TAVG","TMIN","TMAX"]].mean().reset_index()

plt.figure(figsize = (40,30))
plt.subplot(231)
plt.title("temperature distribution in Senegal between [1980,2000]")
plt.hist(x =senegal_temp_1980["TAVG"],bins = 10)
plt.xlabel("bins")
plt.ylabel("average_temperature")

plt.figure(figsize = (40,30))
plt.subplot(232)
plt.title("temperature distribution in Senegal between [1980,2000]")
plt.hist(x =senegal_temp_1980["TMAX"],bins = 10)
plt.xlabel("bins")
plt.ylabel("maximum_temperature")

plt.figure(figsize = (40,30))
plt.subplot(233)
plt.title("temperature distribution in Senegal between [1980,2000]")
plt.hist(x =senegal_temp_1980["TMIN"],bins = 10)
plt.xlabel("bins")
plt.ylabel("minimum_temperature")

plt.figure(figsize = (40,30))
plt.subplot(234)
plt.title("temperature distribution in Senegal between [2000,2023]")
plt.hist(x =senegal_temp_2000["TMIN"],bins = 10)
plt.xlabel("bins")
plt.ylabel("minimum_temperature")

plt.figure(figsize = (40,30))
plt.subplot(235)
plt.title("temperature distribution in Senegal between [2000,2023]")
plt.hist(x =senegal_temp_2000["TMAX"],bins = 10)
plt.xlabel("bins")
plt.ylabel("maximum_temperature")


plt.figure(figsize = (40,30))
plt.subplot(236)
plt.title("temperature distribution in Senegal between [2000,2023]")
plt.hist(x =senegal_temp_2000["TAVG"],bins = 10)
plt.xlabel("bins")
plt.ylabel("average_temperature")
data["TAVG"] = pd.to_numeric(data["TAVG"], errors='coerce')
#question 4
tunisia_chart = data[data["COUNTRY"] == "Tunisia"]
senegal_chart = data[data["COUNTRY"] == "Senegal"]
cameroon_chart = data[data["COUNTRY"] == "Cameroon"]

tunisia_chart_temp = tunisia_chart[["DATE","TAVG"]].groupby("DATE").mean().reset_index()
senegal_chart_temp = senegal_chart[["DATE","TAVG"]].groupby("DATE").mean().reset_index()
cameroon_chart_temp = cameroon_chart[["DATE","TAVG"]].groupby("DATE").mean().reset_index()

plt.figure(figsize = (15,10))
plt.plot(tunisia_chart_temp["DATE"], tunisia_chart_temp["TAVG"])
plt.plot(senegal_chart_temp["DATE"], senegal_chart_temp["TAVG"])
plt.plot(cameroon_chart_temp["DATE"],cameroon_chart_temp["TAVG"])
plt.show()



  













