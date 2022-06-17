from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from data_loader import DataLoader

app = Flask(__name__)
api = Api(app)
CORS(app)




parser = reqparse.RequestParser()
parser.add_argument('tracks', type=dict, required=True, action='append')
parser.add_argument('n', type=int, required=True)

root_parser = reqparse.RequestParser()
root_parser.add_argument('tracks', type=dict)



loader = DataLoader()
loader.load_model()


class Playlist(Resource):
    def get(self):
        return """You can use POST for track recommendation! Parameters are 'tracks' and 'n'"""

    def post(self):
        args = parser.parse_args()
        tracks_uri = loader.load_tracks_uri(args['tracks'][0])
        playlist = loader.load_audio_features(tracks=tracks_uri)
        similar_tracks = loader.load_similar_tracks(playlist, args['n'])
        names = [(my_track['name'], ", ".join([artist['name'] for artist in my_track['artists']])) for my_track in
                 similar_tracks]
        return names


api.add_resource(Playlist, '/')
if __name__ == '__main__':
    app.run()
