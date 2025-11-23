
Project Statement: In-Memory Student Grade Tracker
1. Problem Statement
The challenge addressed by this project is the need for a simple, immediate, and calculation-focused digital tool to manage student performance. While complex systems use databases, this project focuses on providing quick, reliable grade storage and average calculation within a single application session.
The project specifically solves the problem of how to efficiently store and retrieve nested data (students have many courses, each with a grade) and perform basic mathematical analysis (the average score) using core Python data structures.
________________________________________
2. Scope and Goals
The primary goal is to create a functional command-line utility for tracking grades in a temporary, in-memory environment.
In Scope (Achieved)
Student Data Storage: Managing student records by a unique ID using a dictionary key.
Grade Management: Allowing the addition, updating, and retrieval of grades (scores 0-100) per course.
Calculation: Calculating the overall average score for a specific student's recorded courses.
Data Integrity: Implementing input validation to ensure scores are integers between 0 and 100.
User Interaction: Providing a clear, menu-driven interface.

Out of Scope (Current Limitations)
Data Persistence: Data is not saved to any file and is lost upon program exit.
Security: No user authentication or encryption is implemented.
Advanced Reporting: Generating class averages, ranking students, or printing reports across the entire database.
Data Type Management: Assumes all grades are unweighted and numerical.
________________________________________
3. Design Rationale
A. Data Structure
Global Dictionary (STUDENTS_DB): A dictionary was chosen as the most suitable structure for the database. Using Student IDs as primary keys allows for fast, direct lookup of any student's record without iteration.
Nested Dictionary: The value associated with each Student ID is another dictionary where course names are the keys and the scores are the values. This nested design perfectly maps the one-to-many relationship (one student has many courses).
B. Modularity (Functions)
The code is broken down into three main functions to ensure high readability and separation of concerns:
add_student_grade(): Focuses solely on data input, validation, and write/update operations.
view_student_report(): Focuses solely on data retrieval, calculation, and formatted display.
display_menu(): Focuses on user interface and directing the flow of the application.
C. Input Validation
The add_student_grade function uses a while True loop and a try-except ValueError block to robustly handle input. This ensures the program does not crash on non-numeric input and forces the user to provide a score that adheres to the business rule of being between 0 and 100.

