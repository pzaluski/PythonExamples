#!/usr/local/bin/python3
students=[]
class Student():

    

    def __init__(self, name, id=332):
        self.name = name
        self.id = id
        student={"name":name,"id":id}
        students.append(self)

    def do_capitalization(self):
        return self.name.capitalize()
    
    def __str__(self):
            return "Student {0} ID: {1}".format(self.name, self.id)

mark = Student("Mark")
print(mark)

""" Dupa bisu """


