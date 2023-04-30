import requests
from API_queries.schoolCodes import SchoolCodeDict

api_key = 'PP7IoOsMzwaWH8g3z9fWzP3SqVTOPk8qr2ugcSu9'

def earningsQuery(schoolname):
    school_id = SchoolCodeDict.dct[schoolname]  # Replace with the specific school's ID
    cip_code = '1107'

    base_url = 'https://api.data.gov/ed/collegescorecard/v1/schools'

    params = {
    'api_key': api_key,
    'id': school_id,
    'fields': 'school.name,programs.cip_4_digit.earnings.1_yr.overall_median_earnings,programs.cip_4_digit.credential.level',  # Replace the year (2017) with the desired year
    'latest.programs.cip_4_digit.code': cip_code
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        earnings = data['results'][0]['latest.programs.cip_4_digit'][1]['earnings']['1_yr']['overall_median_earnings']
        return earnings
    else:
        error = f'Error: {response.status_code}'
        return error
