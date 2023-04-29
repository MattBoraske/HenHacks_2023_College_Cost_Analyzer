import requests

api_key = 'PP7IoOsMzwaWH8g3z9fWzP3SqVTOPk8qr2ugcSu9'
school_id = '243744'  # Replace with the specific school's ID
cip_code = '1107'

base_url = 'https://api.data.gov/ed/collegescorecard/v1/schools'
params = {
    'api_key': api_key,
    'id': school_id,
    'fields': 'school.name,programs.cip_4_digit.earnings.1_yr.overall_median_earnings,programs.cip_4_digit.earnings.highest.3_yr.overall_median_earnings',  # Replace the year (2017) with the desired year
    'latest.programs.cip_4_digit.code': cip_code
}

response = requests.get(base_url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Error: {response.status_code}')
