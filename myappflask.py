from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)
app.config['SECRET_KEY'] ="helloworld"


class MyForm(FlaskForm):
    name = StringField("Give me your name:")
    surname = StringField("Give your surname")
    submit = SubmitField()


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


@app.route('/newform', methods=['GET', 'POST'])
def hello_new_form():
    name = False
    surname = False
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        form.name.data = ""
        form.surname.data = ""
    return render_template('newform.html', name=name, surname=name, form=form)


if __name__ == "__main__":
    app.run(debug=True)
