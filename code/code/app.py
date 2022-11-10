
from flask import Flask, render_template,request
import pickle
import numpy as np
#from sklearn.ensemble.forest import RandomForestClassifier

app= Flask(__name__)


svc_model = pickle.load(open('svc_trained_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/predict', methods=['POST'])
def predict():
   
   
   inputs = []
   inputs.append(request.form['age'])
   inputs.append(request.form['gender'])    
   inputs.append(request.form['slope'])
   inputs.append(request.form['fbs'])
   
   age = request.form['age']
   gender = request.form['gender'] 
   slope = request.form['slope']
   fbs = request.form['fbs']
   

   
   
   final_inputs = [np.array(inputs)]
   prediction = svc_model.predict(final_inputs)
    #unseen_feature_vectors = request.form.values()
   
   if prediction[0] == 1:
        categorical_array = "Detected"
   if prediction[0] == 0:
        categorical_array = "Not Detected"
    
   result= categorical_array
   if age=="1":
       age = 1
   if age=="2":
       age = 2
   if age=="3":
       age = 3
   if age=="4":
       age = 4       
   if gender=="1":
       gender = 1
   if gender=="2":
       gender = 2
   if gender=="3":
       gender==3        
   if slope=="0":
       slope = 0
   if slope=="1":
       slope = 1
   if slope=="2":
       slope = 2
   if fbs=="0":
       fbs = 0    
   if fbs=="1":
       fbs = 1
   if fbs=="2":
       fbs = 2
   if fbs=="3":
       fbs = 3
       
   return render_template('Home.html', prediction_text1=result, age = age, gender=gender, slope=slope, fbs=fbs)



if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)