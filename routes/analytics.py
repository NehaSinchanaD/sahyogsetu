from flask import Blueprint, render_template

analytics_bp = Blueprint(
    "analytics",
    __name__,
    url_prefix="/analytics"
)


# Sample analytics data
analytics_data = {
    "total_challenges": 10,
    "accepted_challenges": 6,
    "completed_projects": 3,
    "active_projects": 7,
    "total_teams": 8,
    "industry_support_requests": 4
}


@analytics_bp.route("/")
def dashboard():
    return render_template(
        "analytics/dashboard.html",
        data=analytics_data
    )


@analytics_bp.route("/challenges")
def challenge_analytics():
    return render_template(
        "analytics/challenges.html",
        data=analytics_data
    )


@analytics_bp.route("/projects")
def project_analytics():
    return render_template(
        "analytics/projects.html",
        data=analytics_data
    )