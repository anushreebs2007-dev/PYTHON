student_marks=int(input("enter the student_marks: "))
if student_marks >= 90:
   print("grade A")
elif student_marks >= 80 and student_marks < 90:
    print("grade B")
elif student_marks >= 70 and student_marks < 80:
    print("grade C")
elif student_marks >= 60 and student_marks < 70:
    print("grade D")
elif student_marks >= 50 and student_marks < 60:
    print("grade E") 
elif student_marks >= 0 and student_marks < 50:
    print("grade F") 
else:
    print("invalid marks")               
