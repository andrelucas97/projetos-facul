from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px


app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
 
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True) #nao pode ser nulo e o nome será unico
    password = db.Column(db.String(80), nullable=False)

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Usuario"})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Senha"})
    submit = SubmitField('Cadastrar')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError('Nome de usuário já existe. Tente outro.')


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField('Login')


@app.route('/')
def home():
    return render_template('home.html')    

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): #se a submissao for valida
        user = User.query.filter_by(username=form.username.data).first() # vamos procurar o usuario
        if user: # se o usuario for verdadeiro
            if bcrypt.check_password_hash(user.password, form.password.data): # vamos procurar a senha, sendo esta verdadeira
                login_user(user) #vamos usar o login_user do flask para logar e 
                return redirect(url_for('dashboard')) # redirecionar para dash
    return render_template('login.html', form=form) # o renderizador será login e o formulario vai receber a variavel da classe form


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user() # deslogue o usuario
    return redirect(url_for('login'))


@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data) # gerando uma senha encriptada
        new_user = User(username=form.username.data, password=hashed_password) # objeto que vai receber um novo usuario
        db.session.add(new_user) # adicionando o usuário da sessão ao nosso banco de dados
        db.session.commit() # confirmar as mudancas
        return redirect(url_for('login')) # ao final, vamos redirecionar o usuario para a rota login

    return render_template('register.html', form=form)



@app.route('/streamlit')
def streamlit():
    st.set_page_config(page_title="My Streamlit App")
    st.write("Hello, world!")
    return render_template('streamlit.html')


if __name__ == "__main__":
    app.run(debug=True)
