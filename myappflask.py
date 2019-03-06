from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class MyForm(FlaskForm):
    name_field = StringField("Give your name:")
    surname_field = StringField("Give your surname:")
    submit_button = SubmitField("WTF_BUTTONO")


app = Flask(__name__)
app.config['SECRET_KEY'] = '12345udp'


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/form/result')
def form_result():
    name = request.args.get('name')
    surname = request.args.get('surname')
    return render_template('result.html', name=name, surname=surname)


@app.route('/newform', methods=['GET', 'POST'])
def new_wtf_form():
    name = False
    surname = False
    form = MyForm()
    if form.validate_on_submit():
        name = form.name_field.data
        surname = form.surname_field.data
        form.name_field.data = ""
        form.surname_field.data = ""
    return render_template('newform.html', form=form, name=name, surname=surname)


if __name__ == '__main__':
    app.run(debug=True)
