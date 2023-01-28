from flask import (
    Blueprint, render_template, request, url_for,
    redirect
)
from werkzeug.exceptions import NotFound

from views.forms.ships import CreateProductForm

ships_app = Blueprint(
    "ships_app",
    __name__,
)


SHIPS = {
    1: "Bismarck",
    2: "Yamashiro",
    3: "California",
    4: "Kirishima",
    5: "South Dakota",
    6: "Resolution",
    7: "Renown",
    8: "Royal Oak",
    9: "Wisconsin",
   10: "Kongo",
   11: "Missouri",
   12: "Iowa",
}


@ships_app.route("/", endpoint="list")
def ships_list():
    return render_template(
        "ships/list.html",
        ships=SHIPS,
    )


@ships_app.route("/<int:ship_id>/", endpoint="details")
def get_ships_id(ship_id: int):
    ship_name = SHIPS.get(ship_id)
    if ship_name is None:
        raise NotFound(f"Ship #{ship_id} not found")
    return render_template(
        "ships/details.html",
        ship_id=ship_id,
        ship_name=ship_name,
    )


@ships_app.route("/add/",
                    methods=["GET", "POST"],
                    endpoint="add")
def add_product():
    form = CreateProductForm()

    if request.method == "GET":
        return render_template("ships/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("ships/add.html", form=form), 400

    ship_name = form.name.data
    ship_id = len(SHIPS) + 1
    SHIPS[ship_id] = ship_name

    url = url_for("products_app.details", ship_id=ship_id)
    return redirect(url)

