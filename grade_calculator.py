# Student Grade Calculator

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

print("🎓 Welcome to Student Grade Calculator 🎓")
name = input("Enter student name: ")

# Take marks for 5 subjects
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

# Calculate total and average
total = sum(marks)
average = total / 5
grade = calculate_grade(average)

# Display results
print("\n------ Result ------")
print(f"Name: {name}")
print(f"Marks: {marks}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
print("--------------------")

# Save to file
with open("grades.txt", "a") as file:
    file.write(f"{name} - Marks: {marks}, Total: {total}, Average: {average:.2f}, Grade: {grade}\n")

print("✅ Record saved successfully in 'grades.txt'")
