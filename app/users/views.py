from flask import request, redirect, url_for, render_template, flash, session, make_response
from . import users_bp

@users_bp.route("/hi/<string:name>")
def greetings(name):
    name = name.upper()
    age = request.args.get("age", None, int)
    return render_template("users/hi.html", name=name, age=age)

@users_bp.route("/admin")
def admin():
    to_url = url_for("users.greetings", name="administrator", age=45)
    return redirect(to_url)

@users_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "user1" and password == "12345":
            session["username"] = username
            flash("Login successful!", "success")
            return redirect(url_for("users.profile"))
        else:
            flash("Wrong data! Try again!", "danger")
            return redirect(url_for("users.login"))

    return render_template("users/login.html")

@users_bp.route("/profile", methods=["GET", "POST"])
def profile():
    if "username" not in session:
        flash("You must log in first!", "warning")
        return redirect(url_for("users.login"))

    username = session["username"]
    cookies = request.cookies
    theme = request.cookies.get("theme", "light") 
    return render_template("users/profile.html", username=username, cookies=cookies, theme=theme)

@users_bp.route("/logout", methods=["POST"])
def logout():
    session.pop("username", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("users.login"))

@users_bp.route("/add_cookie", methods=["POST"])
def add_cookie():
    if "username" not in session:
        flash("You must log in first!", "warning")
        return redirect(url_for("users.login"))

    key = request.form.get("key")
    value = request.form.get("value")
    max_age = request.form.get("max_age", type=int)

    resp = make_response(redirect(url_for("users.profile")))
    resp.set_cookie(key, value, max_age=max_age)
    flash(f"Cookie '{key}' added!", "success")
    return resp

@users_bp.route("/delete_cookie", methods=["POST"])
def delete_cookie():
    if "username" not in session:
        flash("You must log in first!", "warning")
        return redirect(url_for("users.login"))

    key = request.form.get("delete_key")

    resp = make_response(redirect(url_for("users.profile")))
    resp.delete_cookie(key)
    flash(f"Cookie '{key}' deleted!", "info")
    return resp


@users_bp.route("/delete_all_cookies", methods=["POST"])
def delete_all_cookies():
    if "username" not in session:
        flash("You must log in first!", "warning")
        return redirect(url_for("users.login"))

    resp = make_response(redirect(url_for("users.profile")))
    for key in request.cookies.keys():
        resp.delete_cookie(key)
    flash("All cookies deleted!", "info")
    return resp

@users_bp.route("/set_theme/<string:theme>")
def set_theme(theme):
    if "username" not in session:
        flash("You must log in first!", "warning")
        return redirect(url_for("users.login"))

    resp = make_response(redirect(url_for("users.profile")))
    resp.set_cookie("theme", theme, max_age=60*60*24*30)  # зберігаємо на 30 днів
    flash(f"Theme set to {theme}!", "info")
    return resp
