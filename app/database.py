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

if __name__ == "__main__":
    create_tables()
    insert_sample_data()