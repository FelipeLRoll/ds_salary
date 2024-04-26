
#class to determine the behavior of the flask app, as well as the skills neede to predict the DS Monthly Salary

from flask import Flask, render_template, request
import pickle
import numpy as np

with open('models/pipe.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

app = Flask(__name__)  # initializing Flask app

@app.route("/",methods=['GET'])
def hello():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict_result():
    if request.method == 'POST':
        skills = ['python', 'spark', 'aws', 'excel', 'sql', 'sas', 'keras', 'pytorch', 'scikit', 'tensor', 'hadoop', 'tableau', 'bi', 'flink', 'mongo', 'google_an']
        data = []

        for skill in skills:
            value = request.form.get(skill)
            if value == 'No':
                data.append(0)
            else:
                data.append(1)

        new_data = np.array([data])
        predicted_salary = loaded_model.predict(new_data)
        result_text = "Predicted Salary: {}".format(predicted_salary)

        return render_template('results.html', prediction_text=result_text)

@app.route("/result", methods=['GET'])
def show_result():
    return render_template('results.html')

app.run(debug=True)                # run on local system