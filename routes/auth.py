from flask import Blueprint, render_template, request, redirect, url_for, flash

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")
        role = request.form.get("role")

        # Basic validation
        if not email or not password or not role:
            flash("Please fill in all fields.", "error")
            return render_template("login.html")

        # Demo role-based login
        if role == "university":
            return redirect(url_for("university.dashboard"))

        elif role == "student":
            return redirect("/student/")

        elif role == "industry":
            return redirect("/industry/")

        elif role == "citizen":
            return redirect("/citizen/")

        flash("Invalid role selected.", "error")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    flash("You have been logged out.", "success")
    return redirect(url_for("auth.login"))