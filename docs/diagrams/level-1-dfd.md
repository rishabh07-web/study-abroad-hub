
# Level 1 Data Flow Diagram

## Description

The Level 1 DFD represents the internal processes of Study Abroad Hub and illustrates how data flows between the student, system processes, and data stores.

## Diagram

```mermaid
flowchart TB
    S[Student]
    A[Administrator]

    P1((1.0 Browse Programs))
    P2((2.0 Search and Filter))
    P3((3.0 Check Eligibility))
    P4((4.0 Manage Shortlist))
    P5((5.0 Compare Programs))

    D1[(D1: Program Database)]
    D2[(D2: Shortlist Data)]

    A -->|University and program data| D1

    S -->|Browse request| P1
    D1 -->|Available program records| P1
    P1 -->|Program information| S

    S -->|Keywords and filter criteria| P2
    D1 -->|Program records| P2
    P2 -->|Matching programs| S

    S -->|Academic details and program ID| P3
    D1 -->|Admission requirements| P3
    P3 -->|Eligibility result| S

    S -->|Add or remove program| P4
    D2 <-->|Shortlist records| P4
    P4 -->|Updated shortlist| S

    S -->|Selected program IDs| P5
    D1 -->|Selected program details| P5
    P5 -->|Comparison results| S
```

## Explanation of Components

### External Entities
- Student: Uses the application to explore and evaluate programs.
- Administrator: Provides university and program information.

### Processes
- 1.0 Browse Programs: Displays available programs.
- 2.0 Search and Filter: Finds programs based on user criteria.
- 3.0 Check Eligibility: Evaluates academic information against program requirements.
- 4.0 Manage Shortlist: Adds or removes selected programs.
- 5.0 Compare Programs: Displays selected programs side by side.

### Data Stores
- D1: Program Database stores university and program information.
- D2: Shortlist Data stores shortlisted program selections.

### Purpose

This diagram shows how the major functions of Study Abroad Hub interact and exchange information.
