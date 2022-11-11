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
    return render_template("customers/single_customer.html", customer = customer)

@customers_blueprint.route("/customers/<id>/delete", methods=["POST"])
def delete_customer(id):
    customer_repository.delete(id)
    return redirect("/customers")