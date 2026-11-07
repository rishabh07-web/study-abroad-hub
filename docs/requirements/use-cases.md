# Use Case Specifications

## Actor

**Student:** The primary user who explores and evaluates study-abroad programs.

## UC-01: Explore Programs

**Precondition:** The application is running.

**Main Flow:**
1. Student opens the application.
2. System displays available programs.
3. Student selects a program.
4. System displays the program details.

**Postcondition:** Program information is displayed.

## UC-02: Search and Filter Programs

**Precondition:** Program information is available.

**Main Flow:**
1. Student opens the program listing.
2. Student enters a search keyword or selects filters.
3. System processes the search criteria.
4. System displays matching programs.

**Alternative Flow:** If no programs match, the system displays a suitable no-results message.

**Postcondition:** Matching programs are displayed.

## UC-03: Check Eligibility

**Precondition:** The selected program has defined admission requirements.

**Main Flow:**
1. Student opens a program.
2. Student selects the eligibility checker.
3. System requests relevant academic information.
4. Student enters the required information.
5. System compares the inputs with program requirements.
6. System displays the result and unmet criteria, if any.

**Postcondition:** Eligibility results are displayed.

## UC-04: Shortlist a Program

**Precondition:** A program is available.

**Main Flow:**
1. Student selects a program.
2. Student clicks Add to Shortlist.
3. System adds the program to the shortlist.
4. System confirms the action.

**Postcondition:** The program appears in the shortlist.

## UC-05: Compare Programs

**Precondition:** At least two programs are available.

**Main Flow:**
1. Student selects programs for comparison.
2. Student opens the comparison view.
3. System retrieves the selected program details.
4. System displays their attributes side by side.

**Postcondition:** The student can compare the selected programs.