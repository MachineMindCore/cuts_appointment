from flask import render_template, url_for, request

def home():
    template_vars = { 
        "title": "Barber",
        "state": "inicio"
    }
    return render_template("public/index.html", **template_vars)

def salon():
    template_vars = { 
        "title": "Barber - Salon",
        "state": "salon"
    }
    return render_template("public/salon.html", **template_vars)


