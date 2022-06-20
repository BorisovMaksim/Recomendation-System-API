# Recomendation-System-API
- API recommends tracks using Recomendation-System
- Designed using Flask
- Deployed on Heroku
- Available on RapidAPI

## Endpoint
- Recommendation:  `POST /`


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

```bash 
curl --request POST \
	--url https://spotify-tracks.p.rapidapi.com/ \
	--header 'X-RapidAPI-Host: spotify-tracks.p.rapidapi.com' \
	--header 'X-RapidAPI-Key: 4c2876fa83msh992a4395cef11a4p1436d7jsnc121d7cf6bda' \
	--header 'content-type: application/json' \
	--data '{
    "tracks": {
        "Ed sheeran": "photograph",
        "Queen": "The Show Must Go On",
        "Frank Sinatra": "Strangers in the night"
    },
    "n": 3
}'
```
