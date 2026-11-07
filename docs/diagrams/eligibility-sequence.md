
# Eligibility Checking — Sequence Diagram

## Description

This sequence diagram illustrates the interaction between the student, web interface, Flask application, SQLite database, and eligibility checking module when a student checks eligibility for a selected study program.

## Diagram

```mermaid
sequenceDiagram
    actor Student
    participant UI as Web Interface
    participant Backend as Flask Application
    participant DB as SQLite Database
    participant Engine as Eligibility Checker

    Student->>UI: Open selected program
    UI->>Backend: Request program details
    Backend->>DB: Fetch program by ID
    DB-->>Backend: Return program details
    Backend-->>UI: Display program information
    UI-->>Student: Show program requirements

    Student->>UI: Enter CGPA and IELTS score
    Student->>UI: Submit eligibility form

    UI->>Backend: Send eligibility request
    Backend->>Backend: Validate input data

    alt Input is valid
        Backend->>DB: Fetch admission requirements
        DB-->>Backend: Return minimum CGPA and IELTS
        Backend->>Engine: Compare student data with requirements
        Engine->>Engine: Calculate eligibility
        Engine-->>Backend: Return eligibility result
        Backend-->>UI: Send result and explanations
        UI-->>Student: Display eligibility status
    else Input is invalid
        Backend-->>UI: Return validation errors
        UI-->>Student: Display error messages
    end
```

## Explanation

1. The student opens a selected study program.
2. The web interface requests program information from Flask.
3. Flask retrieves the program details from SQLite.
4. The student enters academic information such as CGPA and IELTS score.
5. The backend validates the submitted information.
6. The backend retrieves the admission requirements.
7. The eligibility checker compares the student's details with the requirements.
8. The system returns the eligibility result and displays it to the student.
9. If the input is invalid, the system displays validation errors.

## Purpose

The diagram describes the sequence of interactions required to perform eligibility checking in Study Abroad Hub.
