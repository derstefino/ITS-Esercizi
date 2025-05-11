'''1. School Grading System:

     Create a function that takes a student's name and their scores in different subjects as input.
    The function calculates the average score and prints the student's name, average,
    and a message indicating whether the student passed the exam (average >= 60) or failed.
    Create a for loop to iterate over a list of students and scores, calling the function for each student.
'''

def average_score(student_name:str, scores:list[int]) -> None:

    print(student_name)

    average = sum(scores)/len(scores)

    if average >= 60:
        print(f"average: {average}")
        print("passed\n")
    else:
        print(f"average: {average}")
        print("failed\n")




students_list:list = [("stefano",[60, 70, 80]),("goku",[40,60,100]),("ash",[30,20,90])]

for student in students_list:
    average_score(student[0], student[1])

