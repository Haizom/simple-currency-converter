# loading the packages
import requests
import json

# Define the base URL
base_url = "https://api.exchangeratesapi.io/latest"

#The user inputs
date = input("Please enter the date (in the format 'yyyy-mm-dd' or 'latest'): ")
print("""Choose currency from ('CAD', 'HKD', 'ISK', 'PHP', 'DKK', 'HUF', 'CZK', 
'AUD', 'RON', 'SEK', 'IDR', 'INR', 'BRL', 'RUB', 'HRK', 'JPY', 'THB', 'CHF', 'SGD', 
'PLN', 'BGN', 'TRY', 'CNY', 'NOK', 'NZD', 'ZAR', 'USD', 'MXN', 'ILS', 'GBP', 'KRW', 'MYR')""")
base = input("Convert from (currency): ")
curr = input("Convert to (currency): ")
quan = float(input("How much {} do you want to convert: ".format(base)))

# Constructing the URL based on the user parameters and sending a request to the server
url = base_url + "/" + date + "?base=" + base + "&symbols=" + curr
response = requests.get(url)

print(response.ok)
# Displaying the error message, if something went wrong
if(response.ok is False):
    print("\nError ")

#Final results
else:
    data = response.json()
    data2 = json.loads(data)
    rate = data2['rates'][curr]
    
    result = quan*rate
    
    print("\n{0} {1} is equal to {2} {3}, based upon exchange rates on {4}".format(quan,base,result,curr,data['date']))



