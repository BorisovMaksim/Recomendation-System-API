# recomendation-system-api
API for music recommendation system


## Basic Usage
```python 
import requests
tracks = {
    "tracks": {'Ed sheeran': 'photograph', "Queen": "The Show Must Go On", "Vivaldi" : "The Four Seasons",
              "Taylor Swift" : "Shake It Off"},
    'n': 10
}
request = requests.post(url="https://spotify-tracks-api.herokuapp.com/", json=tracks)
recommendation = eval(request.text)
----------------------------------------------------------------------------------------------------------
[['What About Us - 2nd Adventure Radio Edit',
  'The Saturdays, Oliver Millington'],
 ['Hopeless Wanderer', 'Mumford & Sons'],
 ["Don't Judge Me - Dave Audé Radio Mix",
  'Chris Brown, Dave Audé, Christian Dwiggins'],
 ['Cups - Movie Version', 'Anna Kendrick'],
 ["We Can't Stop", 'Miley Cyrus'],
 ['Love in This Club', 'Usher, Jeezy'],
 ['Girlfriend', 'Icona Pop'],
 ["I Don't Care", 'Carina Dahl'],
 ['Wherever You Are', 'Sam Tsui'],
 ["Livin' It Up (feat. Nicki Minaj)", 'Ciara, Nicki Minaj']]
```
