import requests     # Import the requests library
response = requests.get('https://restcountries.com/v3.1/all')
print(response)



response = requests.get('https://restcountries.com/v3.1/name/turkey')    # Send a GET request to the URL

if response.status_code == 200:
    data = response.json()
    print(data)
else:  
    print(f"Error: {response.status_code}")
    