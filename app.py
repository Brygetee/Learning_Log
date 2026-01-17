from calendar import month

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/entry_form")
def entry_form():
    subjects = ["subject1","subject2","subject3"]
    return render_template("entry_form.html", subjects=subjects)

if __name__ == "__main__":
    app.run(debug=True, port=3000
            )