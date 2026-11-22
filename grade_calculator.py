
# Student Grade Calculator

def average(marks):
    return sum(marks) / len(marks)


def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    elif avg >= 35:
        return "E"
    else:
        return "F"


def is_pass(marks):
    return all(mark >= 35 for mark in marks)


# Feature added in Phase 4
def highest_mark(marks):
    return max(marks)


# Main Program
def main():
    print("===== STUDENT GRADE CALCULATOR =====")

    name = input("Enter student name: ")

    marks = []

    for i in range(1, 6):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)

    total = sum(marks)
    avg = average(marks)

    print("\n===== STUDENT RESULT =====")
    print("Student Name:", name)
    print("Total Marks:", total)
    print("Average Marks:", round(avg, 2))
    print("Grade:", grade(avg))
    print("Highest Marks:", highest_mark(marks))

    if is_pass(marks):
        print("Result: PASS")
    else:
        print("Result: FAIL")


# Execute only when the file is run directly
if __name__ == "__main__":
    main()
