import requests 
#set api key as my_api 
my_api = '359XZEEVAMH3VA4A' 
#set website link with my_api as url 
url= 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={my_api}' 
#set url response from url as response 
response= requests.get(url) 
 
import json 
# use .json to retrieve data and stored as JSON object from the API and name it as data 
data=response.json() 
#converting values from API into string format 
json.dumps(data,indent=4) 
#extract values of Realtime Currency Exchange Rate from data and naming it close data 
close_data=data["Realtime Currency Exchange Rate"] 
#Extracting Exchange Rate values from close_data and converting it into float and name it Exchange_Rate 
Exchange_Rate=(float(close_data['5. Exchange Rate'])) 
 
 
 
import re 
from pathlib import Path 
import csv 
try: 
    #create a new file_path and extend it to overheads.csv 
    file_path = Path.cwd()/"CSV Reports"/"overheads.csv" 
 
    #creating an empty list and naming it empty_list 
    empty_list=[] 
    #opening file_path to read data in csv file 
    with file_path.open(mode = "r",encoding = "UTF-8", newline="") as file: 
    #using csv reader to read data in csv file 
        reader = csv.reader(file) 
    #Ignore the first row of the data in the CSV file 
        next(reader) 
        for line in reader: 
    #Append the rest of the values in the CSV file into the empty list created         
            empty_list.append(line) 
 
 
 
    #set value as 0 
    value = 0 
    #set empty_list as overhead values 
    overhead = empty_list 
    #Creating a for loop and naming previous values as prev_value 
    for prev_value in empty_list: 
        if float(prev_value[1]) > value: 
    #if the value is bigger or equals to the prev value the current value would replace the prev_value  
            value = float(prev_value[1]) 
    #set overhead as the day in prev_value 
            overhead = prev_value[0] 
 
    def convertUSD_SGD(USD):  
             
            """ 
            -This function will convert USD to SGD by multiplying exchange rate and return the converted value 
            - one parameter required USD  
            """ 
            return USD * Exchange_Rate 
         
    #name value converted from USD to SGD as SGD 
    SGD=(convertUSD_SGD(USD=value)) 
    #set value as variable Overhead 
    Overhead=(f"[HIGHEST OVERHEADS] {overhead}: SGD{SGD}") 
    print(Overhead) 
except Exception as e: 
        print(f'An error has occurred.\nReason:{e}')