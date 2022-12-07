from flask import Flask, request, render_template, redirect
import time

app = Flask(__name__, static_folder="static")


@app.route("/")
def index():
    return render_template("form.html")


@app.route("/create_tks/", methods=['GET', 'POST'])
def create_tks():
    if request.method == 'POST':
        run_time()
        data = [v for v in request.form.values()]
        return render_template('modal.html',  ac=data[0], moderators=data[1:])
    else:
        return redirect("/")


def run_time():
    time.sleep(3)
    return True


if __name__ == '__main__':
    app.run(debug=True, port=8888)
