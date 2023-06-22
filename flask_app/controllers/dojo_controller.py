
from flask_app import app
from flask import Flask, redirect, request, render_template, session



# import the class from friend.py
from flask_app.models.dojo import Dojo


@app.route('/')
def Home():
    all_dojos=Dojo.get_all()

    return render_template('index.html', all_dojos=all_dojos)

@app.route('/submit_dojo_form', methods=['POST'])
def Create_Dojo():

    Dojo.add_dojo(request.form)
    return redirect('/')

@app.route('/dojo/<int:id>')
def Show_Dojo_Ninjas(id):
    one_dojo=Dojo.get_one_dojo({'id': id})
    return render_template('one_dojo.html',one_dojo=one_dojo)



