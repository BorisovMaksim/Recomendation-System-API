# recomendation-system-api
API for music recommendation system


## Basic Usage
```python 
import requests


tracks = {
    "tracks": {'Ed sheeran': 'photograph', "Queen": "The Show Must Go On", 
    "Vivaldi" : "The Four Seasons", "Taylor Swift" : "Shake It Off"},
    'n': 10
}
request = requests.post(url="https://spotify-tracks-api.herokuapp.com/", json=tracks)
recommendation = eval(request.text)
```
