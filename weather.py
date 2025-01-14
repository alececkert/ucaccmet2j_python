import json
import string
import csv

#loadig the json data
with open('precipitation.json') as file:
    contents= json.load(file)
    
#dictionaries and lists
results={}
total_monthly_precipitation=[]
monthly={}
#reading the csv 
with open('stations.csv', ) as file:
    stations= list(csv.DictReader(file))

#looping everything for all stations
for city in stations:    
    #giving each part of the csv file a variable 
    station_number=city['Station']
    state= city['State']
    city_name= city['Location']
    city_data=[]
    #selecting all the data for each station
    for measurements in contents:
        if measurements['station']==station_number:
            city_data.append(measurements)
        
    #precipitation per month
    for measurements in city_data:
        month=(int(measurements['date'].split('-')[1]))
        precipitation= int(measurements['value'])
        if month in monthly:
            monthly[month]+=precipitation
        else:
            monthly[month]=0
    #precipitation for the year
    total_yearly=sum(monthly.values())
    relative_monthly={}
    for month,precipitation in monthly.items():
        relative_monthly[month]=monthly[month]/total_yearly

    #relative_between_cities

    #my results in nested dictionary 
    results[city_name]= resrults_per_city= {
        'precipitation_month': monthly,
        'precipitation_yearly': total_yearly,
        'relative_monthly': relative_monthly
     }

#creating and saving results to json file
with open('results2.json', 'w') as file:
    json.dump(results, file, indent=4)
print (results)