class Person:
    
    def __init__(self, cf:str, name:str, surname:str, age:int):
    
        self.cf=cf
        self.name=name
        self.surname=surname
        self.age=age
        
class Student(Person):
    
    def __init__(self, cf:str, name:str, surname:str, age:int):
    
        super().__init__(cf, name, surname, age)
        self.group=None
        
    def set_group(self, group):
        if isinstance(group, Group):
            self.group=group
        
class Lecturer(Person):
    
    def __init__(self, cf:str, name:str, surname:str, age:int):
    
        super().__init__(cf, name, surname, age)
        
class Group:
    
    def __init__(self, name:str, limit:int):
        
        self.name=name
        self.limit=limit
        self.students:list[Student]=[]
        self.lecturers:list[Lecturer]=[]
    
    def get_name(self):
        return self.name
    def get_limit(self):
        return self.name
    def get_students(self):
        return self.students
    def get_limit_lecturers(self):
        if len(self.students)<=10:
            return 1
        else:
            return len(self.students + 9)//10
    
    def add_student(self, student:Student):
        if len(self.students)<self.limit:
            self.students.append(student)
    
    def add_lecturer(self, lecturer:Lecturer):
        if len(self.students)<=10 and len(self.lecturers)==0:
            self.lecturers.append(lecturer)
        elif len(self.students)>10 and len(self.lecturers)<len(self.students + 9)//10:
            self.lecturers.append(lecturer)
        