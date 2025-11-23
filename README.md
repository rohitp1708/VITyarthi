Student Grade Tracker (In-Memory System)
________________________________________
Overview of the Project
This is a simple, command-line Student Grade Tracker implemented in Python. It provides a basic solution for educators or students to manage academic records by allowing users to add/update scores for specific courses and immediately view a detailed report, including the calculated overall average score.
The data is stored in the global Python dictionary STUDENTS_DB (an in-memory system), meaning the data is not saved when the program is closed.
________________________________________
Features

Grade Management: Allows recording or updating a numerical score (0-100) for a student in any specified course.
On-Demand Records: Automatically creates a new student record if the Student ID is entered for the first time.
Performance Report: Displays a clear, formatted list of all grades for a specific student and calculates their overall average score.
Input Validation: Robustly checks user input to ensure scores are integers between 0 and 100.
Menu Interface: Simple, numbered menu for easy navigation of the application's functions.
________________________________________
Technologies/Tools Used
Category	Item	Notes
Language	Python 3.x	Standard Python (no external libraries required).
Data Structure	Dictionary (STUDENTS_DB)	Used for efficient in-memory storage of nested student/course data.
Interface	Command Line	Pure console-based application driven by input() and print().
________________________________________
Steps to Install & Run the Project
Prerequisites: Ensure you have Python 3 installed on your operating system.
Save the Code: Save the provided Python script into a file named grade_tracker.py.
Open Terminal: Navigate to the directory where you saved grade_tracker.py using your terminal or command prompt.
Execute the Script: Run the application using the following command:
python grade_tracker.py
________________________________________
Instructions for Testing
Test the core functionality by running the script and following these steps:
Step	Action	Expected Result
1. Add New Student	Select 1. Enter ID: S900. Course: History. Score: 70.	Confirms "New student S900 added." and the grade update.
2. Add Second Grade	Select 1. Enter ID: S900. Course: Science. Score: 90.	Confirms grade update.
3. View Report	Select 2. Enter ID: S900.	Displays History: 70, Science: 90, and an Average Score of 80.0.
4. Test Invalid Input	Select 1. When prompted for score, enter 101.	System displays "Score must be between 0 and 100." and prompts again.
5. Test Exit	Select 3.	System displays "Goodbye! Data is not saved..." and terminates.
________________________________________
  
