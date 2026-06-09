def title():
    print("----- MARKS ANALYZER -----")
title()

physics = int(input("Enter Physics marks: "))
chemistry = int(input("Enter Chemistry marks: "))
maths = int(input("Enter Maths marks: "))
english = int(input("Enter English marks: "))
pe = int(input("Enter PE marks: "))

marks = [physics, chemistry, maths, english, pe]

print("Physics:", marks[0])
print("Chemistry:", marks[1])
print("Maths:", marks[2])
print("English:", marks[3])
print("PE:", marks[4])

subjects = ["Physics", "Chemistry", "Maths", "English", "PE"]

total = marks[0] + marks[1] + marks[2] + marks[3] + marks[4]
print("Total Marks =", total)

percentage = (total / 500) * 100
print("Percentage =", percentage)

weakest_mark = min(marks)
position = marks.index(weakest_mark)
print("Weakest Subject =", subjects[position])
print("Marks =", weakest_mark) 

highest_mark = max(marks)
position2 = marks.index(highest_mark)
print("Best Subject =", subjects[position2])
print("Marks =", highest_mark)

if percentage >= 90:
    print("Grade = A+")
elif percentage >= 75:
    print("Grade = A")
elif percentage >= 60:
    print("Grade = B")
elif percentage >= 50:
    print("Grade = C")
else :
    print("Grade = F")

topper_percentage = 92
difference = topper_percentage - percentage
print("Topper Percentage =", topper_percentage)
print("Difference =", difference)

import matplotlib.pyplot as plt

plt.bar(subjects, marks)

plt.title("Marks Analyzer")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()