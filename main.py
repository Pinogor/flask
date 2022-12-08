from flask import Flask, request, render_template, redirect
import time
import re

app = Flask(__name__, static_folder="static")


@app.route("/")
def index():
    return render_template("form.html")


@app.route("/create_tks/", methods=['GET', 'POST'])
def create_tks():
    error_input = []
    if request.method == 'POST':
        data = [value for value in request.form.values()]
        for value in data[1:]:
            if re.search(r'@[a-z]{5}.sbrf.ru', value):
                continue
            else:
                error_input.append(value)
            return render_template('modal_error.html', content=error_input)
        time.sleep(3)
        return render_template('modal.html', ac=data[0], moderators=data[1:])



if __name__ == '__main__':
    app.run(debug=True, port=8888)
