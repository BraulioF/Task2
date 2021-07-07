""" views models"""
from flask import Flask, jsonify, request
from models import *
from models import odoo

""" import librery"""
import datetime
import time
import config as cg
import logging

#Global varial
HOST = cg.server['host']

#Declare app
app = Flask(__name__)


#Views parnter list
@app.route("/partner", methods=["GET"])
def search_read():
    parnters = rs_partner.ResPartnerList.res_partner()
    return jsonify(parnters)

#Views parnter list
@app.route("/partner/create", methods=["POST"])
#Enviar a la ruta a traves de postman un json con el name el phone y el email
def partner_create():
    #capturo json
    #y lo mando a su resource
    return jsonify(parnters)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)