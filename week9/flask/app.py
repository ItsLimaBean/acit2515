from flask import Flask, render_template

from models.school import School

app = Flask(__name__)

@app.route("/")
def home():
    school = School("bcit.json")
    return render_template("list.html", school=school)

if __name__ == "__main__":
    app.run(debug=True)
