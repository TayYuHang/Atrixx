from pathlib import Path 
import csv 
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
try: 
    # create a new fp and extend it to 'Atrixx' 
    fp=Path.cwd()/"Try folder" 
    #create a new file_path and extend it to overheads.csv 
    file_path=Path.cwd()/"Try folder"/"profit-and-loss-usd.csv" 
    #opening file_path to read data in csv file 
    with file_path.open(mode = "r",encoding = "UTF-8", newline="") as file: 
    #using csv reader to read data in csv file 
        reader = csv.reader(file) 
    #Ignore the first row of the data in the CSV file 
        next(reader) 
    #create an empty list and naming it empty_list 
        empty_list=[] 
    #create an empty list and naming it flag_list 
        flag_list=[] 
        for line in reader: 
    #Append the rest of the values in the CSV file into the empty list created    
            empty_list.append(line) 
         
    #make net profit value as float and set it as prev_figure 
    prev_figure=float(empty_list[0][4]) 
    #set day as empty_list 
    day=empty_list 
    #creating for loop and name values in empty_list as value 
    for value in empty_list: 
        if float(value[4]) >= float(prev_figure): 
    #if the value is bigger or equals to the prev value the current value would replace the prev_value  
            prev_figure=float(value[4])   
        else: 
    #if the value is smaller than the prev value, it would minus the prev_figure from current value 
            difference=  float(prev_figure) - float(value[4])   
            def convertUSD_SGD(USD):         
                """ 
            -This function will convert USD to SGD by multiplying exchange rate and return the converted value 
            - one parameter required USD (as integer or float) 
            """ 
                return USD * Exchange_Rate 
    #name value converted from USD to SGD as SGD 
            SGD=(convertUSD_SGD(USD=difference)) 
    #set the day value as day 
            day=value[0] 
    #make the current net profit value as float and set as new prev_figure 
            prev_figure=float(value[4]) 
    #set day and cash on hand value as Net_profit 
            Net_profit=(day,SGD) 
    #append Net_profit into flag_list 
            flag_list.append(Net_profit) 
    print(flag_list) 
except Exception as e: 
        print(f'An error has occurred.\nReason:{e}')