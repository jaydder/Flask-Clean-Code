import os
from flask import render_template, request, blueprints
from models import User
from service import UserService
from form import LoginForm, UpdateForm

blueprint = blueprints.Blueprint('home', __name__)

service_user = UserService()

@blueprint.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm(request.form)
    if request.method == 'POST':
        model_user = User()
        model_user.name = form.username.data
        model_user.password = form.password.data
        service_user.create(model_user)
    return render_template('index.html', title='Sign In', form=form)

@blueprint.route('/list_all', methods=['GET', 'POST'])
def list_all() -> str:
    if request.method == 'POST':
        user_delete = request.form['delete']
        service_user.delete(user_delete)
    users = service_user.list_all()
    return render_template('list_all.html', users=users)

@blueprint.route('/update', methods=['GET', 'POST'])
def update() -> str:
    form = UpdateForm(request.form)
    if request.method == 'POST':
        model_user = User()
        model_user.name = form.new_username.data
        model_user.password = form.new_password.data
        service_user.update(form.old_username.data ,model_user)
    return render_template('update.html',  form=form)

