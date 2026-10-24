
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return "This is my Simple Quiz Application"

@app.route("/result", methods=["POST"])
def result():

    if not request.form.get("q1") or not request.form.get("q2") or not request.form.get("q3") or not request.form.get("q4") or not request.form.get("q5"):
        return "Please answer all 5 questions before submitting."

    score = 0

    if request.form.get("q1") == "Python":
        score = score + 1

    if request.form.get("q2") == "Hyper Text Markup Language":
        score = score + 1

    if request.form.get("q3") == "#":
        score = score + 1

    if request.form.get("q4") == "Web framework":
        score = score + 1

    if request.form.get("q5") == ".py":
        score = score + 1

    
    return render_template("result.html", score=score)

if __name__ == "__main__":
    app.run(debug=True)
