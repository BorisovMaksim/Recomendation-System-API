import spotipy
from spotipy.oauth2 import SpotifyOAuth
import yaml
import pandas as pd
from sqlalchemy import create_engine
from annoy import AnnoyIndex

CONFIG = yaml.safe_load(open('credentials.yml'))


class DataLoader:
    def __init__(self):
        self.engine = create_engine(CONFIG['DATABASE']['URL'], echo=False)
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CONFIG['SPOTIFY']['CLIENT_ID'],
                                                            client_secret=CONFIG['SPOTIFY']['CLIENT_SECRET'],
                                                            redirect_uri=CONFIG['SPOTIFY']['REDIRECT_URI'],
                                                            scope="user-library-read"))

        self.audio_cols = ["duration_ms", "danceability", "energy", "key", "loudness", "mode", "speechiness",
                           "acousticness", "instrumentalness", "liveness", "valence", "tempo"]
        self.avg = [235131.93, 0.55, 0.58, 5.26, -9.66, 0.65, 0.09, 0.35, 0.22, 0.21, 0.48, 119.98, 38.1, 66.3]
        self.std = [39767.41, 0.18, 0.26, 3.55, 5.62, 0.48, 0.12, 0.35, 0.35, 0.19, 0.26, 29.92, 30.3, 53.7]
        self.model = AnnoyIndex(len(self.avg), metric='angular')
        self.model.load('model/annoy_full_data.ann')

    def load_audio_features(self, tracks):
        audio_features = pd.DataFrame([x for x in self.sp.audio_features(tracks=tracks) if x is not None])[
            self.audio_cols]
        tracks = self.sp.tracks(tracks)
        audio_features['num_artists'] = len(
            [artist['name'] for track in tracks['tracks'] for artist in track['artists']])
        audio_features['num_tracks'] = len(tracks)
        audio_features[audio_features.columns] = audio_features.apply(
            lambda row: pd.Series([(row[i] - self.avg[i]) / self.std[i] for i in range(len(row))]), axis=1)
        playlist = audio_features.mean(axis=0)
        return playlist

    def load_similar_tracks(self, playlist, n):
        similar_playlists = self.model.get_nns_by_vector(playlist, 100)
        con = self.engine.connect()
        similar_tracks = con.execute(f"SELECT tracks FROM playlist_heroku WHERE playlist_id IN"
                                     f"({','.join([str(x) for x in similar_playlists])})")
        return similar_tracks.fetchall()[0][0][:n]
