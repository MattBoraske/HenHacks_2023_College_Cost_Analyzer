import requests

def get_tuition(name):
    api_key = "PP7IoOsMzwaWH8g3z9fWzP3SqVTOPk8qr2ugcSu9"
    response = requests.get("https://api.data.gov/ed/collegescorecard/v1/"+ api_key)
    data = response.json()

    print(data)
    
    for result in data["results"]:
        school_name = result["school.name"]
        school_id = result["id"]
        print(school_name, school_id)
