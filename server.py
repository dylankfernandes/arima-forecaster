from flask import Flask, render_template, url_for, jsonify
import pickle
import json
import pandas

app = Flask(__name__)

def get_model():
  filename='analysis/forecaster'
  file = open(filename, 'rb')
  model = pickle.load(file)
  file.close()
  return model

def get_dataframe():
  filename='analysis/data'
  file = open(filename, 'rb')
  dataframe = pickle.load(file)
  file.close()
  return dataframe
  
model = get_model()
dataframe = get_dataframe()

@app.route('/')
def main():
  response = {
    "data": get_data()
  }
  return render_template('index.html', response=response)

@app.route('/api/data/')
def get_data():
  return dataframe.to_json(orient='records')

@app.route('/api/predict/')
def make_prediction():
  return model

@app.route('/api/data/<amount>')
def get_data_by_amount(amount):
  return dataframe

@app.route('/api/predict/<amount>')
def make_prediction_by_amount(amount):
  return model  

if __name__ == '__main__':
  app.run(debug=True)