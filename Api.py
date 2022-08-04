import requests 
#set api key as my_api 
my_api = '359XZEEVAMH3VA4A' 
#my_api='VSAFQ7CP9MDL4PCL' 
#set url with api key as url  
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
print(Exchange_Rate)

