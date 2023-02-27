from os import getenv

from flask import Flask
from flask import flash
from flask import redirect
from flask import request
from flask import render_template
from werkzeug.exceptions import NotFound
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from sqlalchemy.exc import DatabaseError
from views.ships import ships_app


from models import db

app = Flask(
    __name__,
)
app.register_blueprint(ships_app, url_prefix="/ships")

CONFIG_OBJECT = getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_OBJECT}")

csft = CSRFProtect(app)

#CSRFProtect(app)
db.app = app
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)
#migrate = Migrate(app, db)


@app.cli.command("db-create-all")
def db_create_all():
    print(db.metadata.tables)
    #db.create_all()

def print_request():
    print("request:", request)
    print("headers", request.headers)


#@app.route("/", endpoint="index_page)
@app.get("/", endpoint="index_page")
def get_root():
    return render_template("index.html")


@app.route("/about/", endpoint="about_page")
def get_about_page():
    return render_template("about.html")


#@app.errorhandler(404)
#def handle_404(error):
#    if isinstance(error, NotFound) and error.description != NotFound.description:
#        return error
#    return f"<h1>eroror: {error}</h1>", 404


@app.errorhandler(DatabaseError)
def handle_database_error(error):
    flash("oops! no db connection!", "danger")
    return redirect("/")

#if __name__ == "__main__":
#    app.run(debug=True)


