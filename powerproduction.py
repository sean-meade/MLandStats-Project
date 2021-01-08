import flask as fl
import csv
import numpy as np
import pandas as pd
from sklearn.neighbors import RadiusNeighborsRegressor
import requests

app = fl.Flask(__name__)

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/powerproduction", methods=["POST"])
def powerproduction():
    if fl.request.method == "POST":
        speed = {}
        speed = float(fl.request.form['speed'])
        # speed = requests.get(data['input_s'])
        # import csv data and convert to pandas dataframe
        df = pd.read_csv("powerproduction.csv")

        # remove all zeros
        df = df[df.power != 0]

        # put rows in order of speed
        df = df.sort_values('speed')

        # set each column to a numpy array for processing
        S = df['speed'].to_numpy()
        p = df['power'].to_numpy()

        neigh_radius = RadiusNeighborsRegressor(radius=1.7, weights='distance', p = 2)
        neigh_radius.fit(S.reshape(-1, 1), p)

        p_pred = neigh_radius.predict([[speed]])

        return {'value': p_pred[0]}

if __name__ == "__main__":
    app.run(debug=True)