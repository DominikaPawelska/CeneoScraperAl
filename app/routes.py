from models.product import Product
from app import app
from app.models.opinion import Opinion
from app.models.product import ProductForm
from flask import request, render_template, url_for
import requests
import json


@app.route('/')
@app.route('/index')
def index():
    opinion1 = Opinion()
    return str(opinion1)


@app.route('/extract')
def example():
    form = ProductForm()
    if form.validate():


@app.route('/product/<productId>')
def example(productId):
    pass


@app.route('/products/<var>')
def example(var):
    pass


@app.route('/author')
def example(var):
    pass
