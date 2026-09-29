from student import Student

UNITS = ["Programming", "Databases", "Networking"]


def read_mark(unit):
    """Keep asking until a valid mark between 0 and 100 is entered."""
    while True:
        try:
            mark = float(input(f"  Enter {unit} mark (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("  Mark must be between 0 and 100.")
        except ValueError:
            print("  Please enter a number.")


def capture_student():
    name = input("Enter student name: ").strip()
    reg_no = input("Enter registration number: ").strip()
    marks = [read_mark(unit) for unit in UNITS]
    return Student(name, reg_no, marks)


def print_report(students):
    print("\n" + "=" * 68)
    print(f"{'Name':<16}{'Reg No':<14}{'Total':>7}{'Average':>10}   Result")
    print("-" * 68)
    for s in students:
        print(f"{s.name:<16}{s.reg_no:<14}{s.calculate_total():>7.1f}"
              f"{s.calculate_average():>10.1f}   {s.classify_result()}")
    print("=" * 68)


def main():
    students = []
    count = int(input("How many students? "))
    for i in range(1, count + 1):
        print(f"\nStudent {i}")
        students.append(capture_student())

    print_report(students)

    best = max(students, key=lambda s: s.calculate_average())
    print(f"Top student: {best.name} with {best.calculate_average():.1f}%")


if __name__ == "__main__":
    main()