STUDENTS_DB = {}

def add_student_grade():
    "Module 1: Adds a grade for a specific student and course."
    print("\n--- Add/Update Grade ---")
    
    student_id = input("Enter Student ID: ")
    course = input("Enter Course Name (e.g., 'CS101'): ")
    
    # Input validation for the score
    while True:
        try:
            score = int(input("Enter Score (0-100): "))
            if score>=0 and score<=100:
                break
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # If the student ID isn't in the database, initialize their record
    if student_id not in STUDENTS_DB:
        STUDENTS_DB[student_id] = {}
        print("New student ",student_id ,"added.")

    # Add or update the grade
    STUDENTS_DB[student_id][course] = score
    print(f" Grade for {course} updated to {score} for Student {student_id}.")


def view_student_report():
    "Module 2: Displays all grades and the average score for a student."
    print("--- View Student Report ---")
    
    student_id = input("Enter Student ID: ")

    if student_id not in STUDENTS_DB:
        print(" Error: Student ID ",student_id," not found.")
        return

    grades = STUDENTS_DB[student_id]

    if not grades:
        print(f"Student {student_id} has no grades recorded yet.")
        return

    print(f"\nReport for Student ID: {student_id}")
    print("-" * 30)

    total_score = 0
    num_courses = 0

    # Display grades and calculate total
    for course, score in grades.items():
        print(f"{course:<10}: {score:3}")
        total_score += score
        num_courses += 1
    
    # Calculate and display the average
    average = total_score / num_courses
    print("-" * 30)
    print("Number of Courses: ",num_courses)
    print("Average Score    : ",average)


def display_menu():
    "Module 3: Displays the main menu and handles user choice."
    
    print("\n\n===== Student Grade Tracker =====")
    print("1. Add/Update Student Grade")
    print("2. View Student Report & Average")
    print("3. Exit")
    print("---------------------------------")
    
    choice = input("Enter your choice (1-3): ")
    return choice

# --- Main Program Loop ---

if __name__ == "__main__":
    while True:
        user_choice = display_menu()
        
        if user_choice == '1':
            add_student_grade()
        
        elif user_choice == '2':
            view_student_report()
            
        elif user_choice == '3':
            print("Goodbye! Data is not saved (in-memory system).")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
