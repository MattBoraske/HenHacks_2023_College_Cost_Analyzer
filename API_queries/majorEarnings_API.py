import requests
from API_queries.Dictionaries.schoolCodes import SchoolCodeDict
from API_queries.Dictionaries.CIPCodes import CIPCodeDict

api_key = 'PP7IoOsMzwaWH8g3z9fWzP3SqVTOPk8qr2ugcSu9'

def earningsQuery(schoolname, major):
    school_id = SchoolCodeDict.dct[schoolname]  # Replace with the specific school's ID
    cip_code = CIPCodeDict.dct[major]

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
        level_3_earnings = None
        for result in data['results']:
            for program in result['latest.programs.cip_4_digit']:
                if program['credential']['level'] == 3:
                    level_3_earnings = program['earnings']['1_yr']['overall_median_earnings']
        return level_3_earnings if level_3_earnings else 'No data available'
    else:
        error = f'Error: {response.status_code}'
        return error
