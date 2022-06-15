from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import json
import psycopg2
import os



app = Flask(__name__)
api = Api(app)
CORS(app)

parser = reqparse.RequestParser()
parser.add_argument('tracks', type=list, location='form')
parser.add_argument('n', type=int, location='form')

DATABASE_URL = os.environ.get('DATABASE_URL')
con = psycopg2.connect(DATABASE_URL)




class Playlist(Resource):
    def get(self):
        return """You can use POST for track recommendation! For example """

    def post(self):
        args = parser.parse_args()
        tracks_uri = json.loads("".join(args['tracks']))
        cur = con.cursor()

        # similar_tracks = system.model.predict(tracks_uri=tracks_uri, n=args['n'])
        return tracks_uri.to_json()


api.add_resource(Playlist, '/')
if __name__ == '__main__':
    app.run()
