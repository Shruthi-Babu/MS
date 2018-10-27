from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
#import Flask-MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password',
    [validators.DataRequired(),  validators.EqualTo('confirm', message='Passwords do not match')])
    confirm = PasswordField('Confirm Password')

@app.route('/register', methods=['GET' , 'POST'])
def register():
    form= RegisterForm(request.form)
    #if request.method == 'POST' and form.validate():
    return render_template('register.html', form=form)


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)


