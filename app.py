from flask import Flask,render_template
# from flask_sqlalchemy import SQLAlchemy

#myapp
app=Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

if __name__ in "__main__":
    app.run(debug=True)