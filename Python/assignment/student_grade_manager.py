"""Student Grade Manager

Question:
Create a Python program that manages student grades for a class.
The program should allow adding students with their scores, displaying the students,
calculating each student's grade, and showing class statistics.

Description:
- Add multiple students by name and score.
- Convert scores into letter grades.
- Show all student records with grade details.
- Show class average, highest score, and lowest score.
- Allow users to remove a student or update an existing score.
"""

from typing import Dict, List

GRADE_MAP = [
    (90, "A"),
    (80, "B"),
    (70, "C"),
    (60, "D"),
    (0, "F"),
]


def get_grade(score: float) -> str:
    for threshold, grade in GRADE_MAP:
        if score >= threshold:
            return grade
    return "F"


def add_student(records: Dict[str, float], name: str, score: float) -> None:
    records[name] = score


def remove_student(records: Dict[str, float], name: str) -> bool:
    return records.pop(name, None) is not None


def update_score(records: Dict[str, float], name: str, score: float) -> bool:
    if name in records:
        records[name] = score
        return True
    return False


def get_statistics(records: Dict[str, float]) -> Dict[str, float]:
    if not records:
        return {"average": 0.0, "highest": 0.0, "lowest": 0.0}

    scores = list(records.values())
    return {
        "average": sum(scores) / len(scores),
        "highest": max(scores),
        "lowest": min(scores),
    }


def display_students(records: Dict[str, float]) -> None:
    if not records:
        print("No students available.")
        return

    print("Student Grades")
    print("--------------")
    for name, score in records.items():
        print(f"{name}: {score} -> {get_grade(score)}")


def main() -> None:
    records: Dict[str, float] = {}

    while True:
        print("\nStudent Grade Manager")
        print("1. Add student")
        print("2. Update score")
        print("3. Remove student")
        print("4. Show all students")
        print("5. Show stats")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Student name: ").strip()
            score = float(input("Score (0-100): ").strip())
            add_student(records, name, score)
            print(f"Added {name} with score {score}.")

        elif choice == "2":
            name = input("Student name to update: ").strip()
            score = float(input("New score (0-100): ").strip())
            if update_score(records, name, score):
                print(f"Updated {name} to score {score}.")
            else:
                print("Student not found.")

        elif choice == "3":
            name = input("Student name to remove: ").strip()
            if remove_student(records, name):
                print(f"Removed {name}.")
            else:
                print("Student not found.")

        elif choice == "4":
            display_students(records)

        elif choice == "5":
            stats = get_statistics(records)
            print("Class statistics")
            print("---------------")
            print(f"Average: {stats['average']:.2f}")
            print(f"Highest: {stats['highest']:.2f}")
            print(f"Lowest: {stats['lowest']:.2f}")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()
