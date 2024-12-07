from flask import Blueprint, render_template, request
from models import User
from service import UserService
from form import LoginForm, UpdateForm

user_page = Blueprint('user', __name__, template_folder='templates')


service_user = UserService()

@user_page.route('/')
def index():
    form = LoginForm(request.form)
    if request.method == 'POST':
        model_user = User()
        model_user.name = form.username.data
        model_user.password = form.password.data
        service_user.create(model_user)
    return render_template('index.html', title='Sign In', form=form)