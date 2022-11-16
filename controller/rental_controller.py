from flask import Flask, render_template, request, redirect
from repositories import van_repository
from repositories import customer_repository
from repositories import rentals_repository
from flask import Blueprint
from models.rental import Rental
from models.van import Van
from models.customer import Customer

rentals_blueprint = Blueprint("rentals", __name__)

@rentals_blueprint.route("/rentals")
def rentals():
    rentals = rentals_repository.select_all()
    customers = customer_repository.select_all()
    vans = van_repository.select_all()
    booked = rentals_repository.current_rentals()
    available_rentals = rentals_repository.available_rentals()
    return render_template ("rentals/index.html", rentals = rentals, customers=customers, vans = vans, booked=booked, available_rentals=available_rentals)
    # return render_template ("rentals/index.html", rentals = rentals, customers = customers, vans=vans)

@rentals_blueprint.route("/rentals/<id>")
def rental(id):
    rental = rentals_repository.select(id)
    customer = customer_repository.select(id)
    van = van_repository.select(id)
    return render_template("rentals/single_rental.html", rental = rental, customer = customer, van = van)

@rentals_blueprint.route("/rentals/<id>/delete", methods=["POST"])
def delete_rental(id):
    rentals_repository.delete(id)
    return redirect("/rentals")


@rentals_blueprint.route("/rentals/new")
def new_rental():
    customers = customer_repository.select_all()
    vans = van_repository.select_all()
    return render_template("rentals/new.html", customers=customers, vans=vans)


@rentals_blueprint.route("/rentals/new", methods=["POST"])
def create_rental():
    customer_id = request.form["customer_id"]
    van_id = request.form["van_id"]
    start_date = request.form["start_date"]
    end_date = request.form ["end_date"]
    customer = customer_repository.select(customer_id)
    van = van_repository.select(van_id)
    new_rental = Rental(customer,van, start_date,end_date)
    rentals_repository.save(new_rental)
    return redirect("/rentals")

@rentals_blueprint.route("/rentals/<id>/edit_rental")
def edit_rental(id):
    rental = rentals_repository.select(id)
    vans = van_repository.select_all()
    customers = customer_repository.select_all()
    return render_template ("rentals/edit_rental.html", rental = rental, customers=customers, vans=vans)


@rentals_blueprint.route("/rentals/<id>/edit_rental", methods=["POST"])
def update_rental(id):
    customer_id = request.form["customer_id"]
    van_id = request.form["van_id"]
    start_date = request.form["start_date"]
    end_date = request.form ["end_date"]
    customer = customer_repository.select(customer_id)
    van = van_repository.select(van_id)
    rental = Rental(customer, van, start_date, end_date, id)
    rentals_repository.update(rental)
    return redirect("/rentals")
