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
