import requests
import json

api_key = 'PP7IoOsMzwaWH8g3z9fWzP3SqVTOPk8qr2ugcSu9'
#school_id = '243744'  # Replace with the specific school's ID
#cip_code = '1107'

base_url = 'https://api.data.gov/ed/collegescorecard/v1/schools'
params = {
    'api_key': api_key,
    'fields': 'programs.cip_4_digit.title,programs.cip_4_digit.code',  # Replace the year (2017) with the desired year
}

response = requests.get(base_url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Error: {response.status_code}')