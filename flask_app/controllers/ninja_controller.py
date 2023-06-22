from flask_app import app

from flask import Flask, redirect, request,  render_template, session

# import the class from friend.py
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/ninja_form')
def show_form():
    all_dojos= Dojo.get_all()
    return render_template('ninja_form.html', all_dojos=all_dojos)

@app.route('/submit_ninja_form', methods=['POST'])
def submit_ninja_form():

    data={
        'dojo_id': request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }

    Ninja.add_ninja(data)

    return redirect('/')

@app.route('/edit/<int:ninja_id>')
def show_edit_ninja(ninja_id):

    one_ninja = Ninja.get_one({'ninja_id': ninja_id})

    return render_template('edit_form.html', one_ninja=one_ninja)

@app.route('/edit_ninja', methods=['POST'])
def edit_ninja():

    print(request.form)

    Ninja.update_ninja(request.form)

    return redirect('/')

@app.route('/delete/<int:game_id>')
def destroy(game_id):
    Ninja.destroy_one(game_id)

    return redirect ('/')