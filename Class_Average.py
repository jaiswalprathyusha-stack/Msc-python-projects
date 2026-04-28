
# MSc 1st Sem - Stats for ML Assignment
# Program to find class average and toppers

marks = [78, 85, 92, 67, 88, 95, 73]
total_students = len(marks)
class_average = sum(marks) / total_students

print("📊 Class Report")
print("Total Students:", total_students)
print("Class Average:", round(class_average, 2))

print("\n🌟 Students above average:")
for i, mark in enumerate(marks, start=1):
    if mark > class_average:
        print(f"Student {i}: {mark} marks")
