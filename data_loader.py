import spotipy
from spotipy.oauth2 import SpotifyOAuth
import yaml
import psycopg2
import pandas as pd
import os

CONFIG = yaml.safe_load(open('credentials.yml'))
DATABASE_URL = os.environ.get('DATABASE_URL')


class DataLoader:
    def __init__(self):
        self.con = psycopg2.connect(DATABASE_URL)

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CONFIG['SPOTIFY']['CLIENT_ID'],
                                                            client_secret=CONFIG['SPOTIFY']['CLIENT_SECRET'],
                                                            redirect_uri=CONFIG['SPOTIFY']['REDIRECT_URI'],
                                                            scope="user-library-read"))

        self.audio_cols = ["danceability", "energy", "key", "loudness", "mode", "speechiness", "acousticness",
                      "instrumentalness", "liveness", "valence", "tempo"]
        self.avg = [0.55, 0.58, 5.26, -9.66, 0.65, 0.09, 0.35, 0.22, 0.21, 0.48, 119.98, 38.1, 66.3]
        self.std = [0.18, 0.26, 3.55, 5.62, 0.48, 0.12, 0.35, 0.35, 0.19, 0.26, 29.92, 30.3, 53.7]

    def load_audio_features(self, tracks):
        audio_features = pd.DataFrame([x for x in self.sp.audio_features(tracks=tracks) if x is not None])[self.audio_cols]
        tracks = self.sp.tracks(tracks)
        audio_features['num_artists'] = len(
            [artist['name'] for track in tracks['tracks'] for artist in track['artists']])
        audio_features['num_tracks'] = len(tracks)
        audio_features[audio_features.columns] = audio_features.apply(
            lambda row: pd.Series([(row[i] - self.avg[i]) / self.std[i] for i in range(len(row))]), axis=1)
        playlist = audio_features.mean(axis=0)
        return playlist

