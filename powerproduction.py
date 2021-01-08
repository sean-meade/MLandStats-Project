import flask as fl
import csv
import numpy as np
import pandas as pd
from sklearn.neighbors import RadiusNeighborsRegressor

app = fl.Flask(__name__)

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/powerproduction")
def powerproduction():
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
    neigh_radius.fit(S, p)

    p_pred = neigh_radius.predict(3)

    return {'value': p_pred}

if __name__ == "__main__":
    app.run(debug=True)