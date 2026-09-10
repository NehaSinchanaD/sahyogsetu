from flask import Blueprint, render_template, request, redirect, url_for, flash

industry_bp = Blueprint(
    "industry",
    __name__,
    url_prefix="/industry"
)


# -----------------------------
# Sample Industry Data
# -----------------------------

support_requests = [
    {
        "id": 1,
        "title": "AI Development Support",
        "description": "Industry mentor required for AI project.",
        "status": "Pending"
    },
    {
        "id": 2,
        "title": "Prototype Review",
        "description": "Technical review required for prototype.",
        "status": "In Progress"
    }
]

mentors = [
    {
        "id": 1,
        "name": "Industry Mentor",
        "expertise": "Artificial Intelligence"
    },
    {
        "id": 2,
        "name": "Technical Expert",
        "expertise": "Software Development"
    }
]


# -----------------------------
# Industry Dashboard
# -----------------------------

@industry_bp.route("/")
def dashboard():
    return render_template(
        "industry/dashboard.html",
        support_requests=support_requests,
        mentors=mentors
    )


# -----------------------------
# Support Requests
# -----------------------------

@industry_bp.route("/requests")
def requests_page():
    return render_template(
        "industry/requests.html",
        support_requests=support_requests
    )


# -----------------------------
# Accept Support Request
# -----------------------------

@industry_bp.route("/requests/<int:request_id>/accept", methods=["POST"])
def accept_request(request_id):

    for support_request in support_requests:
        if support_request["id"] == request_id:
            support_request["status"] = "Accepted"
            break

    flash("Support request accepted.", "success")

    return redirect(url_for("industry.requests_page"))


# -----------------------------
# Reject Support Request
# -----------------------------

@industry_bp.route("/requests/<int:request_id>/reject", methods=["POST"])
def reject_request(request_id):

    for support_request in support_requests:
        if support_request["id"] == request_id:
            support_request["status"] = "Rejected"
            break

    flash("Support request rejected.", "warning")

    return redirect(url_for("industry.requests_page"))


# -----------------------------
# Industry Mentors
# -----------------------------

@industry_bp.route("/mentors")
def mentors_page():
    return render_template(
        "industry/mentors.html",
        mentors=mentors
    )


# -----------------------------
# Add Mentor
# -----------------------------

@industry_bp.route("/mentors/add", methods=["POST"])
def add_mentor():

    name = request.form.get("name")
    expertise = request.form.get("expertise")

    if name and expertise:

        mentors.append({
            "id": len(mentors) + 1,
            "name": name,
            "expertise": expertise
        })

        flash("Industry mentor added successfully.", "success")

    return redirect(url_for("industry.mentors_page"))