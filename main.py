from flask import Flask, request, render_template, redirect
import time

app = Flask(__name__, static_folder="static")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create_tks/", methods=['GET', 'POST'])
def create_tks():
    if request.method == 'POST':
        name_ac = request.form.get('AC')
        email = request.form.get('moder')
        if name_ac == '' or email == '':
            return redirect('/')
        else:
            run_time()
            context = {'name_ac': name_ac,
                       'email': email}
        print(context)
        return redirect("/")
    else:
        return 'Error'


def run_time():
    time.sleep(3)
    return True


if __name__ == '__main__':
    app.run(debug=True, port=8888)
