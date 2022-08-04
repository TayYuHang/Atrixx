from pathlib import Path
import csv
import requests
my_api = '359XZEEVAMH3VA4A'
url= 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={my_api}'

response= requests.get(url)

import json
data=response.json()
print(json.dumps(data,indent=4))

close_data=data["Realtime Currency Exchange Rate"]
Exchange_Rate=(float(close_data['5. Exchange Rate']))
fp=Path.cwd()/"Atrixx"
file_path=Path.cwd()/"CSV Reports"/"cash-on-hand-usd.csv"
#print(fp.exists())
with file_path.open(mode = "r",encoding = "UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    empty_list=[]
    flag_list=[]
    for line in reader:
        empty_list.append(line)
    

prev_figure=float(empty_list[0][1])
day=empty_list
for value in empty_list:
    if float(value[1]) >= float(prev_figure):
        prev_figure=float(value[1])  
    else:
        difference=  float(prev_figure) - float(value[1])  
        def convertUSD_SGD(USD):        
            """
        -This function will convert USD to SGD by multiplying exchange rate and return the converted value
        - one parameter required USD (as integer or float)
        """
            return USD * Exchange_Rate
        SGD=(convertUSD_SGD(USD=difference))
        day=value[0]
        prev_figure=float(value[1])
        COH=(day,SGD)
        flag_list.append(COH)
        prev_figure=float(value[1])
print(flag_list)
        
