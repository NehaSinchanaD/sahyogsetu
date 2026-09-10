from flask import Blueprint, render_template, request, redirect, url_for, flash

citizen_bp = Blueprint(
    "citizen",
    __name__,
    url_prefix="/citizen"
)


# Sample citizen data
issues = [
    {
        "id": 1,
        "title": "Garbage collection issue",
        "description": "Garbage has not been collected in the area.",
        "status": "Pending"
    },
    {
        "id": 2,
        "title": "Street light problem",
        "description": "Street lights are not working.",
        "status": "In Progress"
    }
]


@citizen_bp.route("/")
def dashboard():
    return render_template(
        "citizen/dashboard.html",
        issues=issues
    )


@citizen_bp.route("/issues")
def view_issues():
    return render_template(
        "citizen/issues.html",
        issues=issues
    )


@citizen_bp.route("/issues/report", methods=["POST"])
def report_issue():

    title = request.form.get("title")
    description = request.form.get("description")

    if title and description:
        issues.append({
            "id": len(issues) + 1,
            "title": title,
            "description": description,
            "status": "Pending"
        })

        flash("Issue reported successfully.", "success")

    else:
        flash("Please fill in all fields.", "error")

    return redirect(url_for("citizen.view_issues"))