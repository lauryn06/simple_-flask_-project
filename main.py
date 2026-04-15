from flask import Flask,render_template
import pandas as pd
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/iris")
def iris():
    dataset=pd.read_json("iris.json")
    return render_template("iris.html", dataset=dataset)

@app.route("/titanic")
def titanic():          
    return render_template("titanic.html")

if __name__ == "__main__":
   app.run(debug=True)