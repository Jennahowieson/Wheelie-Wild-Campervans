from flask import Flask, render_template, request, redirect
from repositories import van_repository
from repositories import customer_repository
from flask import Blueprint
from models.customer import Customer
from models.van import Van

customers_blueprint = Blueprint("customer", __name__)

@customers_blueprint.route("/customers")
def customers():
    customers = customer_repository.select_all()
    return render_template ("customers/index.html", customers = customers)

@customers_blueprint.route("/customers/<id>")
def customer(id):
    customer = customer_repository.select(id)
    rental_options = customer.give_rental_options()
    return render_template("customers/single_customer.html", customer = customer, rental_options =rental_options)

@customers_blueprint.route("/customers/<id>/delete", methods=["POST"])
def delete_customer(id):
    customer_repository.delete(id)
    return redirect("/customers")

@customers_blueprint.route("/customers/<id>/edit_customer")
def edit_customer(id):
    customer = customer_repository.select(id)
    return render_template ("customers/edit_customer.html", customer = customer)

@customers_blueprint.route("/customers/<id>/edit_customer", methods=["POST"])
def update_van(id):
    # license, budget, friends
    customer_name = request.form["customer_name"]
    license = request.form["license"]
    budget = request.form['budget']
    friends = request.form["friends"]
    customer = Customer(customer_name, license, budget, friends, id)
    customer_repository.update(customer)
    id = id
    return render_template("customers/single_customer.html", customer = customer)

@customers_blueprint.route("/customers/new")
def new_customer_page():
    customers = customer_repository.select_all()
    return render_template ("customers/new.html", customers = customers)


@customers_blueprint.route("/customers/new", methods=["POST"])
def new_customer():
    customer_name = request.form["customer_name"]
    license = request.form["license"]
    budget = request.form['budget']
    friends = request.form["friends"]
    new_customer = Customer(customer_name, license, budget, friends, id)
    customer_repository.save(new_customer)
    return redirect ("/customers")