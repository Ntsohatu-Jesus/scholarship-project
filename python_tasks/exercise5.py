# excercise_5: Student report card. List,functions and looping principles applied
students = [("James",85),("Susan",70),("Peter",55),("Mike",40),("Mary",80)]
def grading(score):
    if score >= 80:
        print("Grade: A,Passed")
    elif score >= 70:
        print("Grade: B,Passed")
    elif score >= 60:
        print("Grade: B,Passed")
    elif score >= 50:
        print("Grade: B,Passed")
    else:
        print("Grade: F, Failed")
for i in students :
    name = i[0]
    score = i[1]
    grade = grading(score)
    print(f"Name: {name}")
    print("Score: ",score)
    print("Grade: ",grade)   