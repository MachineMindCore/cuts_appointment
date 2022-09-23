from flask import render_template, url_for, request

def home():
    return render_template("public/index.html", title = "Barber")

def salon():
    return render_template("public/salon.html", title = "Barber - Salon")

