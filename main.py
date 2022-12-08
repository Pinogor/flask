from flask import Flask, request, render_template, redirect
from flask.views import View
import time
import re
from json_test import data
import random
from flask_restful import Resource, Api

app = Flask(__name__, static_folder="static")
api = Api(app)


@app.route("/")
def index():
    return render_template("form.html")


@app.route("/create_tks/", methods=['GET', 'POST'])
def create_tks():
    if request.method == 'POST':
        data = [value for value in request.form.values()]
        for value in data[1:]:
            if re.search(r'@[a-z]{5}.[a-z]{4}.ru$', value):
                continue
            return render_template('modal_error.html', content=data)
        time.sleep(3)
        return render_template('modal.html', ac=data[0], moderators=data[1:])


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
