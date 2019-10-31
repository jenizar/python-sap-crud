#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 13:06:19 2019
@author: john
"""
import requests
from markupsafe import Markup
import json
import urllib.request
from flask import Flask, jsonify, request, redirect, url_for, render_template
from flask import request
import os

app = Flask(__name__, template_folder="mytemplate")
cf_port = os.getenv("PORT")

@app.route("/", methods=['GET', 'POST'])
def homepage():
    html = urllib.request.urlopen("http://saprestdev.saprest.com:8000/sap/bc/bsp/sap/zres_app/z1.htm")
    #html = '{"PRODUK": [{"MANDT": "010", "PRODUCTID": "235-92-391", "NAME": "BODY SOAP", "CATEGORY": "TOILETORIES", "AVAILABLE": "63", "UNITPRICE": "1.33", "DATECHECKED": "20190902"}, {"MANDT": "010", "PRODUCTID": "239-38-932", "NAME": "SLEEP AID", "CATEGORY": "PHARMACY", "AVAILABLE": "33", "UNITPRICE": "1.38", "DATECHECKED": "20190907"}, {"MANDT": "010", "PRODUCTID": "294-33-483", "NAME": "Sun Flower Oil", "CATEGORY": "Kitchen", "AVAILABLE": "72", "UNITPRICE": "2.31", "DATECHECKED": "20190908"}, {"MANDT": "010", "PRODUCTID": "313-83-179", "NAME": "FEVER REDUCER", "CATEGORY": "PHARMACY", "AVAILABLE": "48", "UNITPRICE": "1.43", "DATECHECKED": "20190901"}, {"MANDT": "010", "PRODUCTID": "345-93-873", "NAME": "LOTION", "CATEGORY": "COSMETICS", "AVAILABLE": "21", "UNITPRICE": "1.47", "DATECHECKED": "20190903"}, {"MANDT": "010", "PRODUCTID": "382-48-394", "NAME": "DETERGENT", "CATEGORY": "TOILETORIES", "AVAILABLE": "73", "UNITPRICE": "1.73", "DATECHECKED": "20190905"}, {"MANDT": "010", "PRODUCTID": "387-39-293", "NAME": "WHEET POWDER", "CATEGORY": "KITCHEN", "AVAILABLE": "38", "UNITPRICE": "2.34", "DATECHECKED": "20190904"}, {"MANDT": "010", "PRODUCTID": "482-39-248", "NAME": "BUCKET", "CATEGORY": "HOME CARE", "AVAILABLE": "64", "UNITPRICE": "1.53", "DATECHECKED": "20190906"}]}'
    data = json.load(html)
    json_data = []
    #data = json.loads(html)
    #json_data = []
    for item in data["PRODUK"]:
        #print (item["NAME"])
        json_data.append(item)
    html.close    

    return render_template("menu.html", data = json_data)

@app.route('/addform')
def addform():

    return render_template("create.html")

@app.route('/addpost', methods = ['POST'])
def addpost():
    if request.method == 'POST':
        productid = request.form["productid"]
        name = request.form["name"]
        category = request.form["category"]
        available = request.form["available"]
        unitprice = request.form["unitprice"]
        datechecked = request.form["datechecked"]
        payload = {'c_productid': productid, 'c_name': name, 'c_category': category, 'c_available': available, 'c_unitprice': unitprice, 'c_datechecked': datechecked}
        print(payload)
        x = requests.post('http://saprestdev.saprest.com:8000/sap/bc/bsp/sap/zres_app/z1.htm', data = payload)
        print(x)
        return redirect(url_for('homepage'))
    return render_template("create.html")

@app.route('/readform', methods = ['POST', 'GET'])
def readform():
    if request.method == 'GET':
        productid = request.args.get("r_productid")
        name = request.args.get("r_name")
        category = request.args.get("r_cat")
        available = request.args.get("r_avail")
        unitprice = request.args.get("r_price")
        datechecked = request.args.get("r_date")
        #print (json.dumps({'productid': productid, 'name': name})
        #myjson = []
        myjson = json.dumps([{'PRODUCTID':productid, 'NAME':name, 'CATEGORY':category, 'AVAILABLE':available, 'UNITPRICE':unitprice, 'DATECHECKED':datechecked}])
        loaded_r = json.loads(myjson)
        #print (loaded_r)
    return render_template("read.html", data = loaded_r)

@app.route('/updateform', methods = ['POST', 'GET'])
def updateform():
    if request.method == 'GET':
        productid = request.args.get("u_productid")
        name = request.args.get("u_name")
        category = request.args.get("u_cat")
        available = request.args.get("u_avail")
        unitprice = request.args.get("u_price")
        datechecked = request.args.get("u_date")
        #print (json.dumps({'productid': productid, 'name': name})
        #myjson = []
        myjson = json.dumps([{'PRODUCTID':productid, 'NAME':name, 'CATEGORY':category, 'AVAILABLE':available, 'UNITPRICE':unitprice, 'DATECHECKED':datechecked}])
        loaded_r = json.loads(myjson)
        #return redirect(url_for('homepage'))
    return render_template("update.html", data = loaded_r)

@app.route('/updatepost', methods = ['POST'])
def updatepost():
    if request.method == 'POST':
        productid = request.form.get("productid")
        name = request.form.get("name")
        category = request.form.get("category")
        available = request.form.get("available")
        unitprice = request.form.get("unitprice")
        datechecked = request.form.get("datechecked")
        payload = {'u_productid': productid, 'u_name': name, 'u_category': category, 'u_available': available, 'u_unitprice': unitprice, 'u_datechecked': datechecked}
        print(payload)
        x = requests.post('http://saprestdev.saprest.com:8000/sap/bc/bsp/sap/zres_app/z1.htm', data = payload)
        return redirect(url_for('homepage'))
    return render_template("update.html")

@app.route('/deleteform', methods = ['POST', 'GET'])
def deleteform():
    if request.method == 'GET':
        productid = request.args.get("d_productid")
        name = request.args.get("d_name")
        category = request.args.get("d_cat")
        available = request.args.get("d_avail")
        unitprice = request.args.get("d_price")
        datechecked = request.args.get("d_date")
        #print (json.dumps({'productid': productid, 'name': name})
        #myjson = []
        myjson = json.dumps([{'PRODUCTID':productid, 'NAME':name, 'CATEGORY':category, 'AVAILABLE':available, 'UNITPRICE':unitprice, 'DATECHECKED':datechecked}])
        loaded_r = json.loads(myjson)
        #return redirect(url_for('homepage'))
    return render_template("delete.html", data = loaded_r)

@app.route('/deletepost', methods = ['POST'])
def deletepost():
    if request.method == 'POST':
        productid = request.form.get("productid")
        name = request.form.get("name")
        category = request.form.get("category")
        available = request.form.get("available")
        unitprice = request.form.get("unitprice")
        datechecked = request.form.get("datechecked")
        payload = {'d_productid': productid, 'd_name': name, 'd_category': category, 'd_available': available, 'd_unitprice': unitprice, 'd_datechecked': datechecked}
        print(payload)
        x = requests.post('http://saprestdev.saprest.com:8000/sap/bc/bsp/sap/zres_app/z1.htm', data = payload)
        return redirect(url_for('homepage'))
    return render_template("delete.html")

#if __name__ == '__main__':
#   app.run(debug = True)
if __name__ == '__main__':
   if cf_port is None:
       app.run(host='0.0.0.0', port=5000)
   else:
       app.run(host='0.0.0.0', port=int(cf_port))
