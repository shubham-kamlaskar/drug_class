from flask import Flask,request,render_template
import numpy as np
import pickle

with open("lre.pkl","rb") as f:
    model = pickle.load(f)
 
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("drug.html")

@app.route("/drug" ,methods=["POST"])
def drug():
    if request.method == "POST" :
        age = eval(request.form['age'])
        sex = eval(request.form['sex'])
        bp = eval(request.form['bp'])
        cholesterol = eval(request.form['cholesterol'])
        Na_to_K = eval(request.form['Na_to_K'])

        try :
            pred = model.predict(np.array([[age,sex,bp,cholesterol,Na_to_K]]))
            if pred  == 0 :
                pred = 'DrugY'
            if pred == 1 :
                pred = 'DrugC'
            if pred == 2 :
                pred = 'DrugX'
            if pred == 3 :
                pred = 'DrugA'
            if pred == 4 :
                pred = 'DrugB'
        except Exception as e:
            pred =e

    return render_template("drug.html",drug=pred)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)