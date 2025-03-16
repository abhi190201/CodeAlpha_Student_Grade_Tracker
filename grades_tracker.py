import json

def load_data(filename="grades.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data, filename="grades.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def add_student(data, student_name):
    if student_name not in data:
        data[student_name] = {}
        print(f"✅ Student '{student_name}' added successfully.")
    else:
        print(f"⚠️ Student '{student_name}' already exists.")

def add_grade(data, student_name, subject, grade):
    if student_name in data:
        if subject not in data[student_name]:
            data[student_name][subject] = []
        data[student_name][subject].append(grade)
        print(f"✅ Successfully added grade {grade} for '{student_name}' in subject '{subject}'.")
    else:
        print(f"❌ Error: Student '{student_name}' not found. Please add the student first.")

def calculate_average(data, student_name):
    if student_name in data and data[student_name]:
        total_sum, count = 0, 0
        for subject, grades in data[student_name].items():
            total_sum += sum(grades)
            count += len(grades)
        if count > 0:
            return total_sum / count
    return None

def display_grades(data, student_name):
    if student_name in data:
        print(f"\n📘 Grades for {student_name}:\n----------------------------")
        for subject, grades in data[student_name].items():
            print(f"{subject}: {', '.join(map(str, grades))}")
    else:
        print(f"❌ Error: Student '{student_name}' not found.")

# Function to display all stored student data
def display_all_data(data):
    if data:
        print("\n📂 All Student Grades Data:\n==============================")
        for student, subjects in data.items():
            print(f"\n📌 Student: {student}")
            for subject, grades in subjects.items():
                print(f"   {subject}: {', '.join(map(str, grades))}")
    else:
        print("📭 No student data available.")

def main():
    data = load_data()
    while True:
        print("\n📚 Student Grades Tracker")
        print("===========================")
        print("1️⃣  Add Student")
        print("2️⃣  Add Grade")
        print("3️⃣  Calculate Average")
        print("4️⃣  Display Grades for a Student")
        print("5️⃣  Display All Stored Data")  # Added new menu option
        print("6️⃣  Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            student_name = input("Enter student name: ")
            add_student(data, student_name)
        elif choice == "2":
            student_name = input("Enter student name: ")
            subject = input("Enter subject: ")
            try:
                grade = float(input("Enter grade: "))
                add_grade(data, student_name, subject, grade)
            except ValueError:
                print("❌ Error: Invalid grade input. Please enter a numeric value.")
        elif choice == "3":
            student_name = input("Enter student name: ")
            avg = calculate_average(data, student_name)
            if avg is not None:
                print(f"🎯 Average grade for '{student_name}': {avg:.2f}")
            else:
                print("❌ No grades available for this student.")
        elif choice == "4":
            student_name = input("Enter student name: ")
            display_grades(data, student_name)
        elif choice == "5":
            display_all_data(data)  # Calls the new function
        elif choice == "6":
            save_data(data)
            print("💾 Data saved successfully. Exiting... 👋")
            break
        else:
            print("❌ Invalid choice, please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
5