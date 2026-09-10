from flask import Blueprint, render_template, request, redirect, url_for, flash

# University Module Blueprint
university_bp = Blueprint(
    "university",
    __name__,
    url_prefix="/university",
    template_folder="templates"
)


challenges = [
    {
        "id": 1,
        "title": "Smart Waste Management",
        "description": "Develop an intelligent system for efficient waste collection.",
        "status": "Assigned"
    },
    {
        "id": 2,
        "title": "AI-Based Traffic Management",
        "description": "Use AI to improve traffic monitoring and management.",
        "status": "Assigned"
    }
]

teams = []

milestones = []

projects = [
    {
        "id": 1,
        "name": "Smart Waste Management",
        "progress": 40,
        "status": "In Progress"
    },
    {
        "id": 2,
        "name": "AI Traffic System",
        "progress": 65,
        "status": "In Progress"
    }
]

reports = []

support_requests = []

@university_bp.route("/")
def dashboard():
    return render_template(
        "university/dashboard.html",
        challenges=challenges,
        teams=teams,
        projects=projects
    )



@university_bp.route("/challenges")
def assigned_challenges():
    return render_template(
        "university/assigned_challenges.html",
        challenges=challenges
    )

@university_bp.route("/challenge/<int:challenge_id>/accept", methods=["POST"])
def accept_challenge(challenge_id):

    for challenge in challenges:
        if challenge["id"] == challenge_id:
            challenge["status"] = "Accepted"
            flash("Challenge accepted successfully.", "success")
            break

    return redirect(url_for("university.assigned_challenges"))

@university_bp.route("/challenge/<int:challenge_id>/reject", methods=["POST"])
def reject_challenge(challenge_id):

    for challenge in challenges:
        if challenge["id"] == challenge_id:
            challenge["status"] = "Rejected"
            flash("Challenge rejected.", "warning")
            break

    return redirect(url_for("university.assigned_challenges"))


@university_bp.route("/teams")
def university_teams():
    return render_template(
        "university/teams.html",
        teams=teams
    )


@university_bp.route("/teams/create", methods=["POST"])
def create_team():

    team_name = request.form.get("team_name")
    students = request.form.get("students")
    faculty = request.form.get("faculty")

    if team_name:
        teams.append({
            "id": len(teams) + 1,
            "name": team_name,
            "students": students,
            "faculty": faculty
        })

        flash("Team created successfully.", "success")

    return redirect(url_for("university.university_teams"))


@university_bp.route("/milestones")
def university_milestones():
    return render_template(
        "university/milestones.html",
        milestones=milestones
    )


@university_bp.route("/milestones/add", methods=["POST"])
def add_milestone():

    title = request.form.get("title")
    deadline = request.form.get("deadline")

    if title:
        milestones.append({
            "id": len(milestones) + 1,
            "title": title,
            "deadline": deadline,
            "status": "Pending"
        })

        flash("Milestone added successfully.", "success")

    return redirect(url_for("university.university_milestones"))


@university_bp.route("/progress")
def project_progress():
    return render_template(
        "university/progress.html",
        projects=projects
    )


@university_bp.route("/progress/update/<int:project_id>", methods=["POST"])
def update_progress(project_id):

    progress = request.form.get("progress")

    for project in projects:
        if project["id"] == project_id:
            project["progress"] = int(progress)
            project["status"] = (
                "Completed" if int(progress) == 100
                else "In Progress"
            )
            break

    flash("Project progress updated.", "success")

    return redirect(url_for("university.project_progress"))


@university_bp.route("/reports")
def prototype_reports():
    return render_template(
        "university/reports.html",
        reports=reports
    )

@university_bp.route("/reports/upload", methods=["POST"])
def upload_report():

    report_name = request.form.get("report_name")

    if report_name:
        reports.append({
            "id": len(reports) + 1,
            "name": report_name,
            "status": "Uploaded"
        })

        flash("Prototype report uploaded successfully.", "success")

    return redirect(url_for("university.prototype_reports"))

@university_bp.route("/industry-support")
def industry_support():
    return render_template(
        "university/industry_support.html",
        support_requests=support_requests
    )
@university_bp.route("/industry-support/request", methods=["POST"])
def request_industry_support():

    requirement = request.form.get("requirement")

    if requirement:
        support_requests.append({
            "id": len(support_requests) + 1,
            "requirement": requirement,
            "status": "Pending"
        })

        flash("Industry support request submitted.", "success")

    return redirect(url_for("university.industry_support"))

