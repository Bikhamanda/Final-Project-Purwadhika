from flask import Flask, abort, jsonify, render_template,url_for, request,send_from_directory,redirect
import numpy as np 
import pandas as pd 
import json
import requests 
import joblib
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "GET":
        return render_template('main.html')
    else:
        dicyx = {0:'Get ready for your journey, Not Delay', 1:"We're so sorry for the inconvenience, but we predict you're plane will be Delay"}
        data = request.form
        hasil = model.predict([[
            data['day_sd'],data['month_sd'], 
            data['hour_sd'],data['day_sa'],
            data['month_sa'], data['hour_sa'],
            data['distance'], data['air_time'],
            data['sd']
            ]])
        return render_template('main.html', data=dicyx[hasil[0]])

# @app.route('/res', methods=['GET', 'POST'])
# def res():
#     if request.method == "POST":
#         day_sd = int(request.form['day_sd'])
#         month_sd = int(request.form['month_sd'])
#         hour_sd = int(request.form['hour_sd'])
#         day_sa = int(request.form['day_sa'])
#         month_sa = int(request.form['month_sa'])
#         hour_sa = int(request.form['hour_sa'])
#         distance = int(request.form['distance'])
#         air_time = int(request.form['air_time'])
#         sd = int(request.form['sd'])

#         flight = [
#             day_sd,
#             month_sd,
#             hour_sd,
#             day_sa,
#             month_sa,
#             hour_sa,
#             distance,
#             air_time,
#             sd
#         ]
#         classpredict = model([flight])[0]
#         results = ''
#         if str(classpredict) == '0':
#             results = 'Get ready for your jorney, Not Delay'
#         else:
#             results = "We're so sorry but we predict you're plane will be late, Delay"
#     else:
#         return render_template('main.html')

if __name__ == '__main__':
    df = pd.read_csv('sample_Flights_Delay_clean.csv')
    model = joblib.load('flight_rfc_model.sav')
    app.run(debug = True)