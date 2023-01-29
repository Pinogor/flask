from flask import Flask, request, render_template, redirect, abort, jsonify, url_for
from flask.views import View
import os
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
import time
import re
from json_test import data
import random
from flask_restful import Resource, Api
from flask_bcrypt import Bcrypt

app = Flask(__name__, static_folder="static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = os.urandom(12).hex()
api = Api(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
    # return db.session.query(User).get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'{self.id}:{self.username}'


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form.get('login')).first()
        if user:
            if bcrypt.check_password_hash(user.password, request.form.get('password')):
                login_user(user)
                return redirect('/create_tks')
        else:
            return render_template('login.html', context='Невкрный логин или пароль!')
    return render_template('login.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/create_tks", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
@login_required
def create_tks():
    if request.method == 'POST':
        data = [value for value in request.form.values()]
        for value in data[1:]:
            if re.search(r'@[a-z]{5}.[a-z]{4}.ru$', value):
                continue
            return render_template('modal_error.html', content=data)
        time.sleep(3)
        return render_template('modal.html', ac=data[0], moderators=data[1:])
    if login_required:
        return render_template("form.html")


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login?next=' + request.path)


@app.route("/create_tks_api/", methods=['POST'])
def create_tks_api():
    if not request.data:
        abort(400)
    create_tks = {
        'ac': request.json['ac'],
        'moderators': request.json['moderators'],
    }
    print(request.data)
    print(request.json)
    print(request.values)
    print(request.args)
    return jsonify({'create_tks': create_tks}), 201


class TKS(Resource):
    """API"""

    def get(self, id):
        if id == 0:
            return random.choice(data), 200
        for value in data:
            if value['id'] == id:
                return value, 200
        return "Данных не найдено ", 404


api.add_resource(TKS, '/create_tks_api/<int:id>')

if __name__ == '__main__':
    app.run(debug=True, port=8888)

# curl -v http://127.0.0.1:5555/create_tks_api/  -H "Content-Type: application/json" -X POST --data '{"ac":"Example AC", "moderators":["XXX", "XXXXX", "XXXXX"]}'
