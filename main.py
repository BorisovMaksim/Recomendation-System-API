from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from data_loader import DataLoader




app = Flask(__name__)
api = Api(app)
CORS(app)

parser = reqparse.RequestParser()
parser.add_argument('tracks',  type=list, location='form', required=True,  action='append')
parser.add_argument('n', type=int, location='form', required=True)
loader = DataLoader()




class Playlist(Resource):
    def get(self):
        return """You can use POST for track recommendation! For example """

    def post(self):
        args = parser.parse_args()
        tracks_uri = [''.join(track) for track in args['tracks']]
        playlist = loader.load_audio_features(tracks=tracks_uri)

        return playlist
        # similar_tracks = loader.load_similar_tracks(playlist, args['n'])
        # return similar_tracks



api.add_resource(Playlist, '/')
if __name__ == '__main__':
    app.run(debug=True)

