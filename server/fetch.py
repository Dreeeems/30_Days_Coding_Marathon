import requests
import os
from dotenv import load_dotenv

print(os.getenv("API_KEY"))

API_KEY = os.getenv("API_KEY")


BASE_URL = 'https://api.themoviedb.org/3/search/multi'

def get_movie_details(movie_id):

    url = f'{BASE_URL}?query={movie_id}&api_key={API_KEY}&language=en-UK'
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Return the parsed JSON data as a Python dictionary
        return data
    else:
        print(f"Erreur lors de la requête : {response.status_code}")
        return None
