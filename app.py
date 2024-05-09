from flask import Flask, Blueprint, render_template
from blueprints.home import home
from blueprints.customers import customers
from blueprints.staff import staff
from blueprints.local_manager import local_manager
from blueprints.national_manager import national_manager
from blueprints.admin import admin

app = Flask(__name__)
app.secret_key = "the first secret key for schwifty"


app.config["ALLOWED_EXTENSIONS"] = {
    "png",
    "jpg",
    "jpeg",
    "gif",
}  # Allowed upload file extensions

home = Blueprint("home", __name__, template_folder="templates")


def create_app():
    app = Flask(__name__)
    app.register_blueprint(home)
    app.register_blueprint(customers)
    app.register_blueprint(staff)
    app.register_blueprint(local_manager)
    app.register_blueprint(national_manager)
    app.register_blueprint(admin)
    return app


@home.route("/")
def home():
    return render_template("home.html")
