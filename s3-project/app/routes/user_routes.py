from flask import request,Blueprint,render_template
import numpy as np
import pickle
from xgboost import XGBClassifier
import os

dir = os.path.join(os.getcwd(),'xgb_model.pickle')
bp = Blueprint('answer',__name__, static_url_path='/answer')

@bp.route('/')
def main_get(val=None):
    return render_template('index.html', val=val)

@bp.route('/calculate', methods=['POST','GET'])
def index(val=None):
    if request.method == 'POST':
        pass
    elif request.method =='GET':
        v1 = request.args.get("danceability")
        v2 = request.args.get("energe")
        v3 = request.args.get("key")
        v4 = request.args.get("loudness")
        v5 = request.args.get("mode")
        v6 = request.args.get("speechiness")
        v7 = request.args.get("acousticness")
        v8 = request.args.get("instrumentalness")
        v9 = request.args.get("liveness")
        v10 = request.args.get("valence")
        v11 = request.args.get("tempo")
        v12 = request.args.get("duration_ms")
        v13 = request.args.get("time_signature")
        data = np.array([[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13]])
        genre_list = ['pop', 'rap', 'rock', 'edm', 'trap', 'electropop', 'r&b', 'latin', 'hip hop']

        with open (dir, 'rb') as f:
            model = pickle.load(f)
            pred = model.predict(data)
            return render_template('index.html',val=genre_list[pred[0]])
