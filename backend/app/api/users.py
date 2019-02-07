from flask import jsonify, request
from ..model import User
from . import api
from .. import db

@api.route('/users', methods=['POST'])
def users():
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    email = request.json.get('email')
    password = request.json.get('password')
    user = User(first_name=first_name,
                last_name=last_name,
                email=email,
                password=password)
    db.session.add(user)
    try:
        db.session.commit()
        return jsonify(user.to_json()), 201
    except Exception as e:
        print(e)
        return 'Bad request', 400
