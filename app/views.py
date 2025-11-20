from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import ContactForm
import logging

@app.route("/")
def resume():
    return render_template("resume.html", title="Моє Резюме")

logging.basicConfig(filename="contact.log", level=logging.INFO)

@app.route("/contacts", methods=["GET", "POST"])
def contacts():
    form = ContactForm()
    if form.validate_on_submit():
        logging.info(
            f"Contact form submitted: {form.name.data} ({form.email.data}) - {form.subject.data}"
        )
        flash(f"Message from {form.name.data} <{form.email.data}> sent successfully!", "success")
        return redirect(url_for("contacts"))
    elif form.is_submitted():
        flash("Form contains errors. Please fix them.", "danger")

    return render_template("contacts.html", form=form)
