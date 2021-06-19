
from flask import Flask, render_template,request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
model = pickle.load(open('./Model/Bfsknn.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        age = request.form['Age']
        age = int(age)
        agevalue = 0

        if age >= 0 and age <= 17:
            age_value = 1
        elif age >= 18 and age <= 25:
            age_value = 2
        elif age >= 26 and age <= 35:
            age_value = 3
        elif age >= 36 and age <= 45:
            age_value = 4
        elif age >= 46 and age <= 50:
            age_value = 5
        elif age >= 51 and age <= 55:
            age_value = 6
        elif age >= 56:
            age_value = 7

        occupationvalue = request.form['Oc']
        gendervalue = request.form['Gender']
        martialstatus = request.form['MS']
        stayincityvalue = request.form['city']
        procat1value = request.form['pc1']
        procat2value = request.form['pc2']

    features = [agevalue,gendervalue,martialstatus,stayincityvalue,procat2value,procat1value,occupationvalue]

    int_features = [int(x) for x in features]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    return render_template('index.html', prediction_text=' The Purchase amount is  : {}$'.format(round(prediction[0])))

if __name__ == '__main__':
    app.run(debug=True)

