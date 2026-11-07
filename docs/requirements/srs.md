# Software Requirements Specification (SRS)

## 1. Introduction

### 1.1 Purpose
This document specifies the functional and non-functional requirements of Study Abroad Hub, a web-based system designed to help students explore and evaluate study-abroad programs.

### 1.2 Scope
The system provides a centralized platform for exploring selected universities and their study programs. Students can search and filter programs, check their basic eligibility, shortlist programs, and compare different options.

### 1.3 Intended Users
- Students: Explore programs and evaluate their suitability.
- Administrator: Maintains university and program information in the system.

## 2. Overall Description

### 2.1 Product Perspective
Study Abroad Hub is a standalone web application consisting of a user interface, application logic, and a database.

### 2.2 Product Functions
- Display university and program information.
- Search and filter programs.
- Display program details.
- Check eligibility using predefined criteria.
- Shortlist preferred programs.
- Compare selected programs.

### 2.3 Operating Environment
- Operating System: Windows, Linux or macOS.
- Browser: Modern web browser.
- Backend: Python with Flask.
- Database: SQLite.
- Frontend: HTML, CSS and Bootstrap.

### 2.4 Constraints
- Limited development time.
- Use of free development tools.
- Controlled dataset of selected universities.
- Simple architecture suitable for a beginner-level project.

## 3. Functional Requirements

**FR-01: Display Universities**

The system shall display information about selected universities.

**FR-02: Display Programs**

The system shall display programs associated with universities.

**FR-03: Search Programs**

The system shall allow users to search for programs using keywords.

**FR-04: Filter Programs**

The system shall allow users to filter programs by country, field, degree and tuition budget.

**FR-05: View Program Details**

The system shall display details such as tuition fees, duration, academic requirements and application deadlines.

**FR-06: Check Eligibility**

The system shall compare student-provided academic information with the selected program's admission requirements.

**FR-07: Display Eligibility Results**

The system shall display whether the student meets the defined requirements and identify unmet criteria.

**FR-08: Shortlist Programs**

The system shall allow users to add programs to and remove programs from a shortlist.

**FR-09: Compare Programs**

The system shall allow users to compare selected programs using relevant attributes.

## 4. Non-Functional Requirements

**NFR-01: Usability**

The interface should be simple and understandable.

**NFR-02: Performance**

Search and filtering should respond within a reasonable time for the controlled dataset.

**NFR-03: Reliability**

The system should produce consistent results for identical inputs and program requirements.

**NFR-04: Maintainability**

The application should be divided into logical modules.

**NFR-05: Security**

The system should validate user inputs and protect application data.

**NFR-06: Data Accuracy**

Program information should be accompanied by its source where available.

**NFR-07: Portability**

The application should run on commonly used operating systems with Python installed.

## 5. Assumptions and Dependencies

- University and program information will be entered into a controlled database.
- Eligibility checking will use predefined rules and will not represent an official university admission decision.
- Users will have access to a modern web browser.
- The initial version will not depend on paid external services.

## 6. Future Enhancements

- AI-powered assistant using Retrieval-Augmented Generation.
- Additional universities and study programs.
- User accounts and persistent personal shortlists.
- Application status tracking.