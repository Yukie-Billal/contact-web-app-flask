from flask import render_template, request, redirect, url_for
from . import app
from . import models


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
        models.contact.insert(request.form["nama"], request.form["nohp"])
        return redirect('/contact')
    
    contacts = models.contact.getContact()
    return render_template('contact/index.html', contacts=contacts, update=False, title="Halaman Contact")

@app.route('/contact/update/<int:id>', methods=['GET',"POST"])
def contact_update(id) :
    if request.method == "POST" :
        form = request.form
        nama = form["nama"]
        nohp = form["nohp"]
        models.contact.update(id,nama,nohp)
        return redirect('/contact')
    
    contact = models.contact.getContactId(id)
    return render_template('contact/index.html', update=True, contact=contact, title="Ubah Contact")

@app.route('/contact/delete/<int:id>', methods=['GET',"POST"])
def contact_delete(id) :
    models.contact.destroy(id)
    return redirect('/contact')