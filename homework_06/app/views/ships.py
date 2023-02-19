from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
    flash
)
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound, BadRequest

from models import db, Ship

from views.forms.ships import ShipForm

ships_app = Blueprint(
    "ships_app",
    __name__,
)


@ships_app.route("/", endpoint="list")
def ships_list():
    ships = Ship.query.all()
    return render_template(
        "ships/list.html",
        ships=ships,
    )


@ships_app.route("/<int:ship_id>/",
                 methods=["GET", "DELETE"],
                 endpoint="details")
def get_ships_id(ship_id: int):
    ship = Ship.query.get_or_404(
        ship_id,
        description=f"Ship #{ship_id} not found",
    )

    if request.method == 'GET':
        return render_template(
            "ships/details.html",
            ship=ship,
        )

    ship_name = ship.name
    db.session.delete(ship)
    db.session.commit()
    flash(f"Deleted ship {ship_name}!", "warning")
    url = url_for("ships_app.list")
    return {'status': 'Ok', 'url': url}


@ships_app.route(
    "/<int:ship_id>/update/",
    methods=["GET", "POST"],
    endpoint="update",
)
def update_ship(ship_id: int):
    ship = Ship.query.get_or_404(
        ship_id,
        description=f"Ship #{ship_id} not found!",
    )

    if request.method == "GET":
        form = ShipForm(name=ship.name, description=ship.description)
        return render_template("ships/add.html", form=form, ship=ship)

    form = ShipForm()
    if not form.validate_on_submit():
        return render_template("ships/add.html", form=form, ship=ship), 400

    ship.name = form.name.data
    ship.description = form.description.data

    db.session.commit()

    flash(f"Successfully updated ship {ship.name}!")
    url = url_for("ships_app.details", ship_id=ship.id)
    return redirect(url)


@ships_app.route(
    "/add/",
    methods=["GET", "POST"],
    endpoint="add",
)
def add_ship():
    form = ShipForm()

    if request.method == "GET":
        return render_template("ships/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("ships/add.html", form=form), 400

    ship_name = form.name.data
    ship_description = form.description.data
    ship = Ship(name=ship_name, description=ship_description)
    db.session.add(ship)
    try:
        db.session.commit()
    except IntegrityError:
        raise BadRequest(f"Could not create ship {ship_name!r},"
                         f" probably such ship already exists.")


    flash(f"Ship is successfully added {ship_name}!")
    url = url_for("ships_app.details", ship_id=ship.id)
    return redirect(url)

