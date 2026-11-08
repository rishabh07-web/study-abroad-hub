
from flask import Flask, render_template
from database import get_universities, get_programs_with_university

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
    programs = get_programs_with_university()

    return render_template(
        "programs.html",
        programs=programs
    )


if __name__ == "__main__":
    app.run(debug=True)
