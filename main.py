import json


DATA_FILE = "results.json"


def load_results():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_results(results):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)


def read_mark(prompt):
    while True:
        try:
            mark = float(input(prompt))
            if 0 <= mark <= 100:
                return mark
            print("Mark must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def add_student(results):
    name = input("Student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    subjects = {}
    print("Enter subject marks (leave the subject name empty when finished).")
    while True:
        subject = input("Subject: ").strip()
        if not subject:
            break
        subjects[subject] = read_mark(f"Mark for {subject}: ")

    if not subjects:
        print("No subjects entered.")
        return

    average = sum(subjects.values()) / len(subjects)
    results[name] = {
        "subjects": subjects,
        "average": round(average, 2),
        "status": "Pass" if average >= 50 else "Fail",
    }
    save_results(results)
    print(f"{name}'s result was saved.")


def view_results(results):
    if not results:
        print("No results found.")
        return

    print("\nSTUDENT RESULTS")
    print("-" * 40)
    for name, result in results.items():
        print(f"{name}: Average = {result['average']:.2f}% | {result['status']}")
        for subject, mark in result["subjects"].items():
            print(f"  {subject}: {mark}")


def search_student(results):
    name = input("Enter student name: ").strip()
    result = results.get(name)
    if not result:
        print("Student not found.")
        return

    print(f"\nResult for {name}")
    for subject, mark in result["subjects"].items():
        print(f"{subject}: {mark}")
    print(f"Average: {result['average']:.2f}%")
    print(f"Status: {result['status']}")


def delete_student(results):
    name = input("Enter student name to delete: ").strip()
    if name not in results:
        print("Student not found.")
        return

    del results[name]
    save_results(results)
    print(f"{name} was deleted.")


def main():
    results = load_results()

    while True:
        print("\nRESULTS MANAGEMENT SYSTEM")
        print("1. Add student result")
        print("2. View all results")
        print("3. Search for a student")
        print("4. Delete a student")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_student(results)
        elif choice == "2":
            view_results(results)
        elif choice == "3":
            search_student(results)
        elif choice == "4":
            delete_student(results)
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
