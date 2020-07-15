from flask import render_template, flash, redirect, url_for, request
from app import app
import yaml
import os

@app.route('/')
@app.route('/index')
def index():
    with open("app/data/exchanges.yaml", 'r') as stream:
        data = yaml.safe_load(stream)
    return render_template('index.html', list=data['exchanges'])


@app.route('/merchants')
def merchants():
    with open("app/data/merchants.yaml", 'r') as stream:
        data = yaml.safe_load(stream)
    return render_template('merchants.html', list=data['merchants'])

@app.route('/services')
def services():
    with open("app/data/services.yaml", 'r') as stream:
        data = yaml.safe_load(stream)
    return render_template('services.html', list=data['services'])

@app.route('/donate')
def donate():
    with open("app/data/donations.yaml", 'r') as stream:
        data = yaml.safe_load(stream)
    return render_template('donate.html', addr=data)