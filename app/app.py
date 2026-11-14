
from flask import Flask, render_template, request, redirect, url_for, flash
from database import (
    get_universities,
    get_programs_with_university,
    search_programs,
    get_program_by_id,
    get_programs_for_comparison,
    save_program,
    get_saved_programs,
    remove_saved_program,
    get_dashboard_stats,
    add_application,
    get_applications,
    update_application,
    delete_application
)

app = Flask(__name__)

import os

app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-only-change-me")


@app.route("/")
def home():
    universities = get_universities()
    programs = get_programs_with_university()

    return render_template(
        "index.html",
        universities=universities,
        programs=programs
    )



@app.route("/programs")
def programs_page():
    search = request.args.get("search", "")
    country = request.args.get("country", "")
    degree = request.args.get("degree", "")

    programs = search_programs(search, country, degree)

    return render_template(
        "programs.html",
        programs=programs,
        search=search,
        country=country,
        degree=degree
    )


@app.route("/eligibility", methods=["GET", "POST"])
def eligibility_page():

    programs = get_programs_with_university()

    if request.method == "POST":

        program_id = request.form.get("program_id", type=int)
        cgpa = request.form.get("cgpa", type=float)
        ielts = request.form.get("ielts", type=float)

        if program_id is None or cgpa is None or ielts is None:
            return "Please enter valid values.", 400

        if not (0 <= cgpa <= 10 and 0 <= ielts <= 9):
            return "Scores are outside the allowed range.", 400

        selected_program = get_program_by_id(program_id)

        if selected_program is None:
            return "Selected program does not exist.", 404

        cgpa_eligible = cgpa >= selected_program["min_cgpa"]
        ielts_eligible = ielts >= selected_program["min_ielts"]

        if cgpa_eligible and ielts_eligible:
            result = "You meet the minimum eligibility requirements!"
        else:
            result = "You do not meet all the minimum eligibility requirements."

        return render_template(
            "eligibility_result.html",
            program=selected_program,
            cgpa=cgpa,
            ielts=ielts,
            cgpa_eligible=cgpa_eligible,
            ielts_eligible=ielts_eligible,
            result=result
        )

    return render_template(
        "eligibility.html",
        programs=programs
    )


@app.route("/compare", methods=["GET", "POST"])
def compare_page():

    programs = get_programs_for_comparison()

    if request.method == "POST":

        program1_id = request.form.get("program1", type=int)
        program2_id = request.form.get("program2", type=int)

        if program1_id is None or program2_id is None:
            return "Please select two valid programs.", 400

        if program1_id == program2_id:
            return "Please select two different programs.", 400

        program1 = get_program_by_id(program1_id)
        program2 = get_program_by_id(program2_id)

        if program1 is None or program2 is None:
            return "Selected program does not exist.", 404

        return render_template(
            "compare_result.html",
            program1=program1,
            program2=program2
        )

    return render_template(
        "compare.html",
        programs=programs
    )


@app.route("/save-program/<int:program_id>", methods=["POST"])
def save_program_route(program_id):

    program = get_program_by_id(program_id)

    if program is None:
        return "Program does not exist.", 404

    save_program(program_id)

    return redirect(url_for("programs_page"))



@app.route("/saved-programs")
def saved_programs_page():

    programs = get_saved_programs()

    return render_template(
        "saved_programs.html",
        programs=programs
    )


@app.route("/remove-saved-program/<int:program_id>", methods=["POST"])
def remove_saved_program_route(program_id):

    remove_saved_program(program_id)

    return redirect(url_for("saved_programs_page"))



@app.route("/dashboard")
def dashboard_page():

    stats = get_dashboard_stats()

    return render_template(
        "dashboard.html",
        stats=stats
    )



@app.route("/applications", methods=["GET", "POST"])
def applications_page():

    programs = get_programs_for_comparison()

    if request.method == "POST":

        program_id = request.form.get("program_id", type=int)
        status = request.form.get("status", "")
        deadline = request.form.get("deadline", "")
        notes = request.form.get("notes", "").strip()

        valid_statuses = [
            "Not Applied",
            "Applied",
            "Under Review",
            "Accepted",
            "Rejected"
        ]

        if program_id is None or get_program_by_id(program_id) is None:
            return "Please select a valid program.", 400

        if status not in valid_statuses:
            return "Invalid application status.", 400

        from datetime import date

        if deadline:
            try:
                parsed_deadline = date.fromisoformat(deadline)
                if parsed_deadline.isoformat() != deadline:
                    return "Invalid deadline format.", 400
            except ValueError:
                return "Invalid deadline date.", 400

        existing = get_applications()

        if any(a["program_id"] == program_id for a in existing):
            flash("This program is already being tracked!", "error")
            return redirect(url_for("applications_page"))

        add_application(program_id, status, deadline or None, notes)

        return redirect(url_for("applications_page"))

    applications = get_applications()

    return render_template(
        "applications.html",
        programs=programs,
        applications=applications
    )



@app.route("/applications/edit/<int:application_id>", methods=["GET", "POST"])
def edit_application_page(application_id):

    applications = get_applications()

    application = next(
        (a for a in applications
         if a["application_id"] == application_id),
        None
    )

    if application is None:
        return "Application not found.", 404

    if request.method == "POST":

        status = request.form.get("status", "")
        deadline = request.form.get("deadline", "")
        notes = request.form.get("notes", "").strip()

        valid_statuses = [
            "Not Applied",
            "Applied",
            "Under Review",
            "Accepted",
            "Rejected"
        ]

        if status not in valid_statuses:
            flash("Invalid application status.", "error")
            return redirect(
                url_for("edit_application_page", application_id=application_id)
            )

        from datetime import date

        if deadline:
            try:
                parsed_deadline = date.fromisoformat(deadline)
                if parsed_deadline.isoformat() != deadline:
                    raise ValueError
            except ValueError:
                flash("Invalid deadline date.", "error")
                return redirect(
                    url_for("edit_application_page", application_id=application_id)
                )

        update_application(
            application_id,
            status,
            deadline or None,
            notes
        )

        flash("Application updated successfully!", "success")

        return redirect(url_for("applications_page"))

    return render_template(
        "edit_application.html",
        application=application
    )



@app.route("/applications/delete/<int:application_id>", methods=["POST"])
def delete_application_route(application_id):

    applications = get_applications()

    application = next(
        (a for a in applications
         if a["application_id"] == application_id),
        None
    )

    if application is None:
        flash("Application not found.", "error")
        return redirect(url_for("applications_page"))

    delete_application(application_id)

    flash("Application deleted successfully!", "success")

    return redirect(url_for("applications_page"))



if __name__ == "__main__":
    app.run(debug=True)
