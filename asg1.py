import json
import os

DATA_FILE = "student_records.json"

def load_records():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("\n[Error] Data file is corrupted. Initializing with empty records.")
        return []
    except Exception as e:
        print(f"\n[Error] An unexpected error occurred while reading the file: {e}")
        return []

def save_records(records):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(records, file, indent=4)
    except Exception as e:
        print(f"\n[Error] Failed to save records to file: {e}")

def add_record(records):
    print("\n--- Add New Student Record ---")
    
    while True:
        roll_no = input("Enter Roll Number (e.g., S101): ").strip()
        if not roll_no:
            print("Roll number cannot be empty.")
            continue
        if any(r['roll_no'] == roll_no for r in records):
            print("A student with this roll number already exists.")
            return
        break

    name = input("Enter Student Name: ").strip()
    if not name:
        print("Name cannot be empty. Record creation cancelled.")
        return

    while True:
        try:
            age = int(input("Enter Age: "))
            if age <= 0 or age > 120:
                print("Please enter a realistic age between 1 and 120.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer for age.")

    course = input("Enter Course/Grade: ").strip()

    while True:
        try:
            marks = float(input("Enter Marks (0 - 100): "))
            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number for marks.")

    new_student = {
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    records.append(new_student)
    save_records(records)
    print(f"\nSuccess: Record for {name} added successfully!")

def view_records(records):
    print("\n--- Student Records List ---")
    if not records:
        print("No records found.")
        return

    print(f"{'Roll No':<10} | {'Name':<20} | {'Age':<5} | {'Course':<15} | {'Marks':<5}")
    print("-" * 65)
    for r in records:
        print(f"{r['roll_no']:<10} | {r['name']:<20} | {r['age']:<5} | {r['course']:<15} | {r['marks']:<5}")

def search_record(records):
    print("\n--- Search Student Record ---")
    if not records:
        print("No records available to search.")
        return

    query = input("Enter Roll Number to search: ").strip()
    found = False
    for r in records:
        if r['roll_no'].lower() == query.lower():
            print("\nRecord Found:")
            print(f"  Roll Number : {r['roll_no']}")
            print(f"  Name        : {r['name']}")
            print(f"  Age         : {r['age']}")
            print(f"  Course      : {r['course']}")
            print(f"  Marks       : {r['marks']}")
            found = True
            break
    
    if not found:
        print(f"No student found with Roll Number '{query}'.")

def update_record(records):
    print("\n--- Update Student Record ---")
    if not records:
        print("No records available to update.")
        return

    roll_no = input("Enter Roll Number of the student to update: ").strip()
    student = None
    for r in records:
        if r['roll_no'].lower() == roll_no.lower():
            student = r
            break

    if not student:
        print(f"No student found with Roll Number '{roll_no}'.")
        return

    print(f"\nUpdating record for: {student['name']}. Leave blank to keep existing value.")

    new_name = input(f"Enter new Name [{student['name']}]: ").strip()
    if new_name:
        student['name'] = new_name

    new_age = input(f"Enter new Age [{student['age']}]: ").strip()
    if new_age:
        try:
            parsed_age = int(new_age)
            if 0 < parsed_age <= 120:
                student['age'] = parsed_age
            else:
                print("Invalid age range. Keeping previous age.")
        except ValueError:
            print("Invalid input for age. Keeping previous age.")

    new_course = input(f"Enter new Course [{student['course']}]: ").strip()
    if new_course:
        student['course'] = new_course

    new_marks = input(f"Enter new Marks [{student['marks']}]: ").strip()
    if new_marks:
        try:
            parsed_marks = float(new_marks)
            if 0 <= parsed_marks <= 100:
                student['marks'] = parsed_marks
            else:
                print("Invalid marks range. Keeping previous marks.")
        except ValueError:
            print("Invalid input for marks. Keeping previous marks.")

    save_records(records)
    print("\nSuccess: Record updated successfully!")

def delete_record(records):
    print("\n--- Delete Student Record ---")
    if not records:
        print("No records available to delete.")
        return

    roll_no = input("Enter Roll Number of the student to delete: ").strip()
    for i, r in enumerate(records):
        if r['roll_no'].lower() == roll_no.lower():
            confirm = input(f"Are you sure you want to delete {r['name']}? (y/n): ").strip().lower()
            if confirm == 'y':
                records.pop(i)
                save_records(records)
                print("\nSuccess: Record deleted successfully!")
            else:
                print("Deletion cancelled.")
            return

    print(f"No student found with Roll Number '{roll_no}'.")

def main():
    records = load_records()
    
    while True:
        print("\n========================================")
        print("    STUDENT RECORD MANAGEMENT SYSTEM    ")
        print("========================================")
        print("1. Add New Record")
        print("2. View All Records")
        print("3. Search Record")
        print("4. Update Record")
        print("5. Delete Record")
        print("6. Exit")
        print("----------------------------------------")

        try:
            choice = int(input("Enter your choice (1-6): "))
            
            if choice == 1:
                add_record(records)
            elif choice == 2:
                view_records(records)
            elif choice == 3:
                search_record(records)
            elif choice == 4:
                update_record(records)
            elif choice == 5:
                delete_record(records)
            elif choice == 6:
                print("\nExiting application. Goodbye!")
                break
            else:
                print("\n[Error] Invalid choice! Please enter a number between 1 and 6.")
        
        except ValueError:
            print("\n[Error] Invalid input! Please enter a numeric choice (1-6).")
        except Exception as e:
            print(f"\n[An unexpected error occurred: {e}]")

if __name__ == "__main__":
    main()
    
    

