from flask import Flask,render_template
app=Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/iris")
def iris():
    return render_template("iris.html") 

@app.route("/titanic")
def titanic():          
    return render_template("titanic.html")

if __name__ == "__main__":
    app.run(debug=True)