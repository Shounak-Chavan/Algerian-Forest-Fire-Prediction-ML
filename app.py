from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

scalar = pickle.load(open('Models/scalar.pkl',"rb"))
model = pickle.load(open('Models/ridge.pkl',"rb"))

cor_features = {'DC', 'BUI'}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    data = {
        'Temperature': float(request.form['Temperature']),
        'RH': float(request.form['RH']),
        'Ws': float(request.form['Ws']),
        'Rain': float(request.form['Rain']),
        'FFMC': float(request.form['FFMC']),
        'DMC': float(request.form['DMC']),
        'ISI': float(request.form['ISI']),
        'Classes': int(request.form['Classes']),
        'Region': int(request.form['Region'])
    }

    df = pd.DataFrame([data])

    df_scaled = scalar.transform(df)

    pred = model.predict(df_scaled)[0]

    return render_template("index.html", result=round(pred, 2))


if __name__ == "__main__":
    app.run(debug=True)
