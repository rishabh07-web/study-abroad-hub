
# Database Design — Study Abroad Hub

## Database

SQLite relational database.

## Tables

### 1. University

| Column | Data Type | Constraint |
|---|---|---|
| university_id | INTEGER | Primary Key |
| university_name | TEXT | NOT NULL |
| country | TEXT | NOT NULL |
| city | TEXT | NOT NULL |
| website | TEXT | Optional |

### 2. Program

| Column | Data Type | Constraint |
|---|---|---|
| program_id | INTEGER | Primary Key |
| university_id | INTEGER | Foreign Key |
| program_name | TEXT | NOT NULL |
| degree | TEXT | NOT NULL |
| field | TEXT | NOT NULL |
| tuition_fee | REAL | NOT NULL |
| duration | TEXT | NOT NULL |
| minimum_cgpa | REAL | NOT NULL |
| minimum_ielts | REAL | NOT NULL |
| deadline | TEXT | Optional |
| source_url | TEXT | Optional |

### 3. Shortlist

| Column | Data Type | Constraint |
|---|---|---|
| shortlist_id | INTEGER | Primary Key |
| session_key | TEXT | UNIQUE, NOT NULL |

### 4. Shortlist Item

| Column | Data Type | Constraint |
|---|---|---|
| item_id | INTEGER | Primary Key |
| shortlist_id | INTEGER | Foreign Key |
| program_id | INTEGER | Foreign Key |

## Database Rules

1. Every university must have a unique university ID.
2. Every program must have a unique program ID.
3. Every program must belong to an existing university.
4. A shortlist must have a unique browser session key.
5. A program cannot appear more than once in the same shortlist.
6. Deleting a shortlist should delete its associated shortlist items.

## Design Approach

The database follows a relational model. Primary keys uniquely identify records, while foreign keys establish relationships between tables.
