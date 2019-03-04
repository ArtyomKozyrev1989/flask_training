from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/form')
def form_page():
    return render_template('form.html')


@app.route('/form/result')
def form_result():
    name = request.args.get('name')
    surname = request.args.get('surname')
    return render_template('result.html', name=name, surname=surname)


if __name__ == '__main__':
    app.run(debug=True)