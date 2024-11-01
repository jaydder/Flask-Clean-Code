import os
from flask import Flask, render_template, request
from flask.helpers import url_for
from werkzeug.utils import redirect
from db import db
from models import User
from service import UserService
from form import LoginForm


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

app = Flask(__name__)
app.config.from_object(Config)

service_user = UserService()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm(request.form)
    if request.method == 'POST':
        model_user = User()
        model_user.name = form.username.data
        model_user.password = form.password.data
        service_user.create(model_user)
    return render_template('index.html', title='Sign In', form=form)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port, debug=True)
