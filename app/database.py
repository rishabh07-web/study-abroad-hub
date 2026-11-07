import sqlite3
import os

# Get the project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the database location
DATABASE_PATH = os.path.join(BASE_DIR, "data", "study_abroad.db")


def create_connection():
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")

    return connection

def create_tables():

    connection = create_connection()

    connection.executescript("""

        CREATE TABLE IF NOT EXISTS UNIVERSITY (

            university_id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            country TEXT NOT NULL,

            city TEXT NOT NULL,

            website TEXT UNIQUE,

            description TEXT

        );


        CREATE TABLE IF NOT EXISTS PROGRAM (

            program_id INTEGER PRIMARY KEY AUTOINCREMENT,

            university_id INTEGER NOT NULL,

            name TEXT NOT NULL,

            degree TEXT NOT NULL,

            field TEXT NOT NULL,

            tuition REAL CHECK (tuition >= 0),

            duration TEXT NOT NULL,

            min_cgpa REAL CHECK (min_cgpa >= 0 AND min_cgpa <= 10),

            min_ielts REAL CHECK (min_ielts >= 0 AND min_ielts <= 9),

            deadline TEXT,

            source_url TEXT,

            FOREIGN KEY (university_id)

            REFERENCES UNIVERSITY(university_id)

            ON DELETE CASCADE,

            UNIQUE (university_id, name, degree)

        );

    """)

    connection.close()

    print("Database tables created successfully!")


def insert_sample_data():

    connection = create_connection()

    universities = [
        ("University of Toronto", "Canada", "Toronto",
         "https://www.utoronto.ca", "A research university in Canada."),

        ("University of Manchester", "United Kingdom", "Manchester",
         "https://www.manchester.ac.uk", "A research university in the UK.")
    ]

    for university in universities:

        connection.execute("""
            INSERT OR IGNORE INTO UNIVERSITY
            (name, country, city, website, description)
            VALUES (?, ?, ?, ?, ?)
        """, university)

    connection.commit()
    connection.close()

    print("University records inserted successfully!")


def insert_sample_programs():

    connection = create_connection()

    programs = [
        (
            "University of Toronto",
            "Computer Science",
            "Bachelor's",
            "Computer Science",
            45000,
            "4 years",
            7.0,
            6.5
        ),
        (
            "University of Toronto",
            "Data Science",
            "Master's",
            "Data Science",
            50000,
            "2 years",
            7.5,
            7.0
        ),
        (
            "University of Manchester",
            "Artificial Intelligence",
            "Master's",
            "Artificial Intelligence",
            35000,
            "1 year",
            7.0,
            6.5
        )
    ]

    for program in programs:

        university = connection.execute(
            "SELECT university_id FROM UNIVERSITY WHERE name = ?",
            (program[0],)
        ).fetchone()

        if university is None:
            continue

        connection.execute("""
            INSERT OR IGNORE INTO PROGRAM
            (
                university_id,
                name,
                degree,
                field,
                tuition,
                duration,
                min_cgpa,
                min_ielts
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (university["university_id"], *program[1:]))

    connection.commit()
    connection.close()

    print("Programme records inserted successfully!")


def get_universities():

    connection = create_connection()

    universities = connection.execute(
        "SELECT * FROM UNIVERSITY"
    ).fetchall()

    connection.close()

    return universities

if __name__ == "__main__":

    create_tables()
    insert_sample_data()
    insert_sample_programs()