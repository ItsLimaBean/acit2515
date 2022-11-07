import json
from flask import Flask, render_template, request, make_response

from models.school import School

app = Flask(__name__)

@app.route("/")
def home():
    school = School("bcit.json")

    return render_template("list.html", school=school)

@app.route("/student/<string:student_id>")
def student(student_id):
    school = School("bcit.json")
    return render_template("student.html", student=school.get_student(student_id))

@app.route("/student/add", methods=["POST"])
def add_student():
    school = School("bcit.json")
    try:
        parsed_json = request.json

        if not school.add_student(parsed_json["name"], parsed_json["student_id"]):
            return make_response("Student with that ID already exists.", 409)

        school.save()
        
        return make_response("Success", 200)
    except ValueError: 
        return make_response("Invalid Data", 400)
    except KeyError:
        return make_response("Invalid Data", 400)
    
    
@app.route("/student/<string:student_id>/grades/add", methods=["POST"])
def add_grade(student_id):
    school = School("bcit.json")
    try:
        parsed_json = request.json
        student = school.get_student(student_id)
        if student is None:
            return make_response("Not Found", 404)
        student.add_grade(parsed_json["grade"])

        school.save()
        
        return make_response("Success", 200)
    except ValueError: 
        return make_response("Invalid Data", 400)
    except KeyError:
        return make_response("Invalid Data", 400)


if __name__ == "__main__":
    app.run(debug=True)

