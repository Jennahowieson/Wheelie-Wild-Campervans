from flask import Flask, render_template, request, redirect
from repositories import van_repository
from repositories import customer_repository
from flask import Blueprint
from models.customer import Customer
from models.van import Van

vans_blueprint = Blueprint("van", __name__)

@vans_blueprint.route("/vans")
def vans():
    vans = van_repository.select_all()
    return render_template ("vans/index.html", vans= vans)

