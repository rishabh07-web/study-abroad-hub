
from flask import Flask, render_template, request
from database import get_universities, get_programs_with_university, search_programs, get_program_by_id

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True)
