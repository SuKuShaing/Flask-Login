from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required

from config import config  # Importa el diccionario de configuraciones

# Models
from models.ModelUser import ModelUser

# Entities
from models.entities.User import User


app = Flask(__name__)

db = MySQL(app)  # Inicializa la conexión a la base de datos
login_manager_app = LoginManager(
    app
)  # le pasamos la aplicación al manejador de sesiones


# login_user busca los datos datos del usuario aquí
@login_manager_app.user_loader # método que hay que crear para obtener todos los datos de un usuario que creado un sesión
def load_user(id):
    return ModelUser.get_by_id(db, id) # se le pasan la variable de conexión y un identificador


@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # print(request.form['username'])
        # print(request.form['password'])
        user = User(0, request.form["username"], request.form["password"])
        logged_user = ModelUser.login(db, user)  # usuario loggeado
        if logged_user != None:
            if logged_user.password:
                login_user(
                    logged_user
                )  # Una vez ingresa, se almacena al usuario loggeado
                return redirect(url_for("home"))
            else:
                flash("Invalid Password ...")
                return render_template("auth/login.html")
        else:
            flash("User not found...")
            return render_template("auth/login.html")
    else:
        return render_template("auth/login.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/home")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.config.from_object(config["development"])
    app.run()
