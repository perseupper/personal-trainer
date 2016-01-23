from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from sense_hat import SenseHat

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        sense = SenseHat()
        sense.show_message("Hello {}!".format(form.openid.data))
        #flash('Login requested for OpenID="{}", remember_me={}'.format(form.openid.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form)
