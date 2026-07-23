name=input("Enter your name: ")
physics_marks=int(input("Enter your Physics marks: "))
chemistry_marks=int(input("Enter your Chemistry marks: "))
maths_marks=int(input("Enter your Maths marks: "))

total_marks=physics_marks+chemistry_marks+maths_marks
percentage=(total_marks/300)*100
print("----------------------------------------\nStudent Report Card\n----------------------------------------")
print("Name:", name)
print("Physics :",physics_marks)
print("Chemistry :",chemistry_marks)
print("Maths :",maths_marks)
print("Total :",total_marks)
print("Percentage :",percentage)

if percentage>=90:
    print("Grade :A+")

elif percentage>=80 and percentage<90:
    print("Grade :A")

elif percentage>=70 and percentage<80:
    print("Grade :B")

elif percentage>60 and percentage<70:
    print("Grade :C")

elif percentage>=50 and percentage<60:
    print("Grade :D")

else:
    print("Grade :F")