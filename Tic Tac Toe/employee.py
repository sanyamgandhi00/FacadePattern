import json
 
class Employee():
    def __init__(self , name , designation ):
        self.name = name 
        self.designation = designation
        self.subordinate = [] 

    def addSubordinate(self ,emp ) :
        self.subordinate.append(emp)


    def printt(self) :
        jsondata = json.dumps(self , default = lambda o : o.__dict__ , indent  = 10)
        print(jsondata)



e = Employee("Sanyam" , "SDE1") 
e1 = Employee("Kirti" , "Manager") 

e1.addSubordinate(e) 

e1.printt()

