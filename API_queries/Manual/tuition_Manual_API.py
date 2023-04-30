import requests
from Dictionaries.schoolCodes import SchoolCodeDict

api_key = 'PP7IoOsMzwaWH8g3z9fWzP3SqVTOPk8qr2ugcSu9'
schoolname = 'University of Delaware'
residency = 'in_state'

school_id = SchoolCodeDict.dct[schoolname]  # Replace with the specific school's ID

base_url = 'https://api.data.gov/ed/collegescorecard/v1/schools'

params = {
'api_key': api_key,
'id': school_id,
'fields': 'latest.cost.tuition.in_state,latest.cost.tuition.out_of_state'
}

response = requests.get(base_url, params=params)

if response.status_code == 200:
    data = response.json()
    tuition = None
    if residency == 'In-State':
        #get in-state tuition data from JSON
        tuition = data['results'][0]['latest.cost.tuition.in_state']
    else:
        #get out-of-state tuition data from JSON
        tuition = data['results'][0]['latest.cost.tuition.out_of_state']
    if tuition:
        print(f"Tuition: {tuition}")
    else:
        print('No tuition data available')
else:
    error = f'Error: {response.status_code}'
    print(error)
