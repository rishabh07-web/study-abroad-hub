# Data Dictionary — Study Abroad Hub

## 1. Student Academic Input

| Attribute | Data Type | Description | Example |
|---|---|---|---|
| student_cgpa | Decimal | Student's CGPA | 8.2 |
| ielts_score | Decimal | Student's IELTS score | 7.0 |
| preferred_country | String | Country preferred by student | Germany |
| preferred_field | String | Preferred academic field | Computer Science |
| budget | Decimal | Maximum tuition budget | 25000 |

## 2. University

| Attribute | Data Type | Description | Example |
|---|---|---|---|
| university_id | Integer | Unique university identifier | 101 |
| university_name | String | Name of university | Example University |
| country | String | University country | Germany |
| city | String | University city | Berlin |
| website | String | Official university website | https://example.edu |

## 3. Program

| Attribute | Data Type | Description | Example |
|---|---|---|---|
| program_id | Integer | Unique program identifier | 201 |
| university_id | Integer | Associated university identifier | 101 |
| program_name | String | Name of the program | MSc Computer Science |
| degree | String | Degree type | Master's |
| field | String | Academic field | Computer Science |
| tuition_fee | Decimal | Tuition fee | 18000 |
| duration | String | Program duration | 2 years |
| minimum_cgpa | Decimal | Minimum required CGPA | 7.5 |
| minimum_ielts | Decimal | Minimum IELTS requirement | 6.5 |
| deadline | Date | Application deadline | 2027-01-15 |

## 4. Search Criteria

| Attribute | Data Type | Description | Example |
|---|---|---|---|
| keyword | String | Search keyword | Computer Science |
| country | String | Selected country filter | Germany |
| degree | String | Selected degree filter | Master's |
| field | String | Selected field filter | Computing |
| maximum_budget | Decimal | Maximum tuition budget | 25000 |

## 5. Eligibility Result

| Attribute | Data Type | Description | Example |
|---|---|---|---|
| program_id | Integer | Program being evaluated | 201 |
| cgpa_status | Boolean | Whether CGPA requirement is met | True |
| ielts_status | Boolean | Whether IELTS requirement is met | True |
| eligible | Boolean | Whether all defined checks pass | True |
| result_message | String | Explanation of result | Eligible |

## 6. Shortlist

| Attribute | Data Type | Description | Example |
|---|---|---|---|
| shortlist_id | Integer | Unique shortlist record identifier | 1 |
| program_id | Integer | Saved program identifier | 201 |

## 7. Comparison

| Attribute | Data Type | Description | Example |
|---|---|---|---|
| selected_program_ids | List of Integers | Programs selected for comparison | [201, 202] |
| comparison_fields | List of Strings | Attributes to compare | [tuition_fee, duration, country] |

## Notes

- University and program identifiers uniquely identify records.
- Each program belongs to a university.
- Eligibility results are calculated using predefined academic requirements.
- Shortlisting and comparison are features of the student interface.
- The initial system does not make official admission decisions.
- Program information should include its source where available.