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

@vans_blueprint.route("/vans/<id>")
def van(id):
    van = van_repository.select(id)
    return render_template("vans/single_van.html", van=van)

@vans_blueprint.route("/vans/<id>/delete", methods=["POST"])
def delete_van(id):
    van_repository.delete(id)
    return redirect("/vans")

@vans_blueprint.route("/vans/<id>/edit_van")
def edit_van(id):
    van = van_repository.select(id)
    return render_template ("vans/edit_van.html", van = van)

@vans_blueprint.route("/vans/<id>/edit_van", methods=["POST"])
def update_van(id):
    van_name = request.form["van_name"]
    reg_plate = request.form["reg_plate"]
    year = request.form["year"]
    capacity = request.form["capacity"]
    type = request.form["type"]
    van = Van(van_name, reg_plate, year, capacity,type, id)
    van_repository.update(van)
    return render_template("vans/single_van.html", van=van)

@vans_blueprint.route("/vans/new")
def new_van_page():
    vans = van_repository.select_all()
    return render_template ("vans/new.html", vans = vans)

@vans_blueprint.route("/vans/new", methods=["POST"])
def new_van():
    van_name = request.form["van_name"]
    reg_plate = request.form["reg_plate"]
    year = request.form["year"]
    capacity = request.form["capacity"]
    type = request.form["type"]
    new_van = Van(van_name, reg_plate, year, capacity,type) 
    van_repository.save(new_van)
    return redirect ("/vans")

