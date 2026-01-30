from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/entry_form", methods=["POST","GET"])
def entry_form():
    subjects = ["subject1", "subject2", "subject3"]

    if request.method == "POST":
        title = request.form.get("title")
        subject = request.form.get("subject")
        concepts_learned = request.form.get("concepts_learned")
        reference_notes = request.form.get("reference_notes")
        key_takeaways = request.form.get("key_takeaways")
        date = request.form.get("date")
        return f"Form submitted successfully! Entry Name: {title}, Subject: {subject}"

    return render_template("entry_form.html", subjects=subjects)

# def submit():
if __name__ == "__main__":
    app.run(debug=True, port=3000)