'''1. School Grading System:

     Create a function that takes a student's name and their scores in different subjects as input.
    The function calculates the average score and prints the student's name, average,
    and a message indicating whether the student passed the exam (average >= 60) or failed.
    Create a for loop to iterate over a list of students and scores, calling the function for each student.
'''

def average_score(students_name:str, *args:list[int]) -> int:

    print(students_name)
    
    average = 0

    for n in args:
        average += n
    
    print(average/len(args))

    if average >= 60:
        print(f"{students_name} passed")
    else:
        print(f"{students_name} failed")



list_students = ["Didi", "Nello"] 

scores = [1,2,3,4]

for s in list_students:
    average_score(s)
    for s in scores
