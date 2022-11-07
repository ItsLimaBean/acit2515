import json
import requests

BASE_FILE = {"name": "BCIT", "students": [{"name": "Tim", "student_id": "A01234567", "grades": [0, 100]}]}
FLASK_URL = "http://127.0.0.1:5000"

def reset_json(filename):
    with open(filename, "w") as fp:
        json.dump(BASE_FILE, fp)
        
def get_url(url):
    return requests.get(FLASK_URL + url)
    
def check_homepage():
    r = get_url("/")
    assert r.status_code == 200
    assert "BCIT" in r.text
    assert "Tim" in r.text

def check_student_page():
    r = get_url("/student/A01234567")
    assert r.status_code == 200
    assert "Tim" in r.text
    assert "0" in r.text
    assert "100" in r.text

def check_add_student():
    r = requests.post(FLASK_URL + "/student/add", json={"name": "Bob", "student_id": "A01010101"})
    assert 200 <= r.status_code <= 204
    
    r = get_url("/")
    assert "Bob" in r.text
    
    r = get_url("/student/A01010101")
    assert r.status_code == 200
    assert "Bob" in r.text


def check_add_student_invalid():
    r = requests.post(FLASK_URL + "/student/add", json={"name": "", "student_id": ""})
    assert r.status_code == 400

    r = requests.post(FLASK_URL + "/student/add", json={"name": "Tim"})
    assert r.status_code == 400

    r = requests.post(FLASK_URL + "/student/add", json={"student_id": "A01010101"})
    assert r.status_code == 400

    r = requests.post(FLASK_URL + "/student/add", json={"name": "John", "student_id": "A33333333"})
    assert r.status_code == 200
    r = requests.post(FLASK_URL + "/student/add", json={"name": "John Wick", "student_id": "A33333333"})
    assert r.status_code == 409

def check_student_add_grade():
    r = requests.post(FLASK_URL + "/student/A01010101/grades/add", json={"grade": 67})
    r = requests.post(FLASK_URL + "/student/A01010101/grades/add", json={"grade": "99"})
    assert 200 <= r.status_code <= 204
    r = get_url("/student/A01010101")
    assert r.status_code == 200
    assert "67" in r.text
    assert "99" in r.text

def check_student_add_grade_invalid():
    r = requests.post(FLASK_URL + "/student/A9999999/grades/add", json={"grade": 67})
    assert r.status_code == 404

    r = requests.post(FLASK_URL + "/student/A01010101/grades/add", json={"grade": -100})
    assert r.status_code == 400

if __name__ == "__main__":
    reset_json("bcit.json")
    check_homepage()
    check_student_page()
    check_add_student()
    check_add_student_invalid()
    check_student_add_grade()
    check_student_add_grade_invalid()