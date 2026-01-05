from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/entry_form")
def entry_form():
    return render_template("entry_form.html")

if __name__ == "__main__":
    app.run(debug=True, port=3000)