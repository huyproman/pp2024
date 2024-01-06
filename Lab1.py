def input_number_students():
    return int(input("Number of students in class: "))

def input_student_info():
    student_id = input("Student ID: ")
    student_name = input("Student name: ")
    student_dob = input("Student date of birth: ")
    return (student_id, student_name, student_dob)

def input_number_of_courses():
    return int(input("Number of courses: "))

def input_course_information():
    course_id = input("Course ID: ")
    course_name = input("Course name: ")
    return course_id, course_name

def input_student_marks(students, courses):
    course_id = input("CourseID to input marks for: ")
    if course_id not in courses:
        print("Invalid course ID.")
        return
    marks = {}
    for student_id in students:
        mark = float(input(f"Enter the mark for student {student_id} in course {course_id}: "))
        marks[student_id] = mark
        
    courses[course_id]["marks"] = marks
    print("Marks saved.")
    
def list_courses(courses):
    print("Courses: ")
    for course_id, course in courses.items():
        print(f"Course ID: {course_id}, Course Name: {course['name']}")
        
def list_students(students):
    print("Students:")
    for student in students:
        print(f"Student ID: {student[0]}, Student Name: {student[1]}, DoB: {student[2]}")
        
def show_student_marks(students, courses):
    course_id = input("Enter the course ID to show marks for: ")
    if course_id not in courses:
        print("Invalid course ID.")
        return

    print(f"Marks for Course ID: {course_id}, Course Name: {courses[course_id]['name']}")
    for student_id, mark in courses[course_id]["marks"].items():
        student = next((s for s in students if s[0] == student_id), None)
        if student:
            print(f"Student ID: {student_id}, Student Name: {student[1]}, Mark: {mark}")
        else:
            print(f"Student ID: {student_id}, Mark: {mark}")

def main():
    students = []
    courses = {}

    num_students = input_number_students()
    for _ in range(num_students):
        student_info = input_student_info()
        students.append(student_info)

    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        course_info = input_course_information()
        courses[course_info[0]] = {"name": course_info[1], "marks": {}}

    while True:
        print("\n--- Student Mark Management System ---")
        print("1. Input student marks for a course")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a course")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            input_student_marks(students, courses)
        elif choice == "2":
            list_courses(courses)
        elif choice == "3":
            list_students(students)
        elif choice == "4":

            show_student_marks(students,courses)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()