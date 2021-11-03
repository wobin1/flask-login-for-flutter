from flask import Blueprint, request, json, jsonify
from .models import Student
from software import db

views = Blueprint('views', __name__)

@views.route('/register', methods=["GET", "POST"])
def register():
    d={}
    if request.method =="POST":
        data = json.loads(request.data,strict=False)
        mail = data["email"]
        password = data["password"]

        email = Student.query.filter_by(email=mail).first()

        if email is None:
            register = Student(email=mail, password=password)

            db.session.add(register)
            db.session.commit()
            d["status"] = 11
            return jsonify(d)
        else:
            # already exist
            d["status"] = 22
            return jsonify(d)


@views.route('/login', methods=["GET", "POST"])
def login():
    d = {}
    if request.method == "POST":
        data = json.loads(request.data,strict=False)
        mail = data["email"]
        password = data["password"]

        login = Student.query.filter_by(email=mail, password=password).first()

        if login is None:
            # acount not found
            d["status"] = 22
            return jsonify(d)
        else:
            # acount found
            d["status"] = 11
            return jsonify(d)
