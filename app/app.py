
from flask import Flask, render_template, request
from database import get_universities, get_programs_with_university, search_programs

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



if __name__ == "__main__":
    app.run(debug=True)
