# -*- coding: utf-8 -*-
"""server.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n5OVdKlgjknsmu5axYh6eFBi_yKb0o_n
"""

#install flask and ngrok
#!apt-get update
#!pip install flask
#!pip install flask-ngrok

import pandas as pd
import numpy as np
import json
import pickle
from flask import Flask, jsonify, request
#from flask_ngrok import run_with_ngrok

app = Flask(__name__)
#run_with_ngrok(app)

#load model
model = pickle.load(open('model.pkl','rb'))
labels ={
  0: "setosa",
  1: "versicolor",
  2: "virginica"
}
@app.route('/')
def welcome():
  return 'welcome'

@app.route('/api',methods=['POST'])
def predict():
  #get data from POST request
  data = request.get_json(force=True)
  data = np.array(data['feature'].split(','),dtype=float)
  data = data.reshape(1,-1)
  predict = model.predict(data)
  return str(labels[predict[0]])
  #return str((predict[0]))

if __name__ == '__main__':
  #app.debug=True
  app.run()

