from flask import render_template, request, redirect, url_for
from . import app
from . import models
from validator import validate

@app.route('/')
def index() :
    return render_template('index.html')

@app.route('/create/contact')
def create() :
    models.contact.create_table()
    return 'created'

@app.route('/contact', methods=['GET','POST'])
def contact() :
    if request.method == "POST" :
        nama = request.form["nama"]
        nohp = request.form["nohp"]
        request_data = {
            "nama": nama,
            "nohp": nohp,
        }

        rules = {
            "nama": "required",
            "nohp": "integer"
        }
        result, _, err = validate(request_data, rules, return_info=True)
        if result :
            models.contact.insert(nama, nohp)
            return redirect('/contact')
        else :
            return '<h1>403 Bad Request</h1>'
    
    contacts = models.contact.getContact()
    return render_template('contact/index.html', contacts=contacts, update=False, title="Halaman Contact")

@app.route('/contact/update/<int:id>', methods=['GET',"POST"])
def contact_update(id) :
    if request.method == "POST" :
        nama = request.form["nama"]
        nohp = request.form["nohp"]
        request_data = {
            "nama": nama,
            "nohp": nohp,
        }
        rules = {
            "nama": "required",
            "nohp": "integer"
        }
        result = validate(request_data, rules)
        if result :
            models.contact.update(id,nama,nohp)
            return redirect('/contact')
        else : 
            return '<h1>403 Bad Request</h1>'
    contact = models.contact.getContactId(id)
    return render_template('contact/index.html', update=True, contact=contact, title="Ubah Contact")

@app.route('/contact/delete/<int:id>', methods=['GET',"POST"])
def contact_delete(id) :
    models.contact.destroy(id)
    return redirect('/contact')