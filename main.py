from flask import Flask,render_template
import pandas as pd
import matplotlib.pyplot as plt
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/iris")
def iris():
    return render_template("iris.html")

@app.route("/iris_data")
def iris_data():
    dataset=pd.read_json("iris.json")
    return render_template("iris_data.html", dataset=dataset)
@app.route("/iris_pie")

def iris_pie():
   pieChart=pd.read_json("iris.json")
   counts = pieChart["species"].value_counts()
   plt.figure()
   plot_url = plt.pie(counts, labels=counts.index, autopct='%1.1f%%')
   plt.savefig( format='png')
   plt.close()
   return render_template("iris_pie.html", plot_url=plot_url)
 
@app.route("/iris_bar")
def iris_bar():
    return render_template("iris_bar.html")
@app.route("/titanic")
def titanic():          
    return render_template("titanic.html")

if __name__ == "__main__":
   app.run(debug=True)