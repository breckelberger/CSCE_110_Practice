#File: q3.py
#Author: Breck Echelberger
#Date: 9/11/2024
#Section: 502
#E-mail: breckechelberger@tamu.edu
#Description: Write a Python program (called q3.py) that asks the user to input today’s temperature and tomor-
#row’s temperature forecasts in Fahrenheit. Then, find the difference between the temperatures
#and the percentage change in the forecast compared to today. The percentage must be rounded
#to the nearest integer. Please pay close attention to the examples

today_temp = float(input("Enter todays temperature in fahrenheit: "))
tomorrow_temp = float(input("Enter tomorrows temperature in fahrenheit: "))

temp_dif = tomorrow_temp - today_temp
perc = round((temp_dif / today_temp) * 100, 0)

if temp_dif > 0:
    print("The temp will rise by", temp_dif,"degrees and the temperature change is ", perc,"%.")

else:
    print("The temp will drop by", temp_dif,"degrees and the temperature change is ", perc,"%.")
