student = {
    "name": input("Enter student name: "),
    "class": input("Enter student class: "),
    "marks": int(input("Enter student marks: "))
}
if student["marks"] >= 40:
    student["result"] = "Pass"
else:
    student["result"] = "Fail"
print("\n--- Student Report ---")
print("Name:", student["name"])
print("Class:", student["class"])
print("Marks:", student["marks"])
print("Result:", student["result"])
