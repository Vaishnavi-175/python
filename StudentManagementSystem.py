names = []
grade = []

def add():
        name = input("Enter name of Student: ")
        names.append(name)
        marks = float(input("Enter marks of Student: "))
        grade.append(marks)
        
    
def updateGrade():
        update = input("Enter Student name: ")
        
        for i in range(0, len(names)):
            if(update == names[i]):
                n = i
                
        newMark = float(input("Enter New marks of student: "))
        grade[n] = newMark
        

def RemoveStudent():
    name = input("Enter name of Student: ")
    
    for i in range(0, len(names)):
            if(name == names[i]):
                n = i
                
    names.pop(n)
    grade.pop(n)
    

def topLowScorer():
    
    top = max(grade)
    low = min(grade)
    
    for i in range(0, len(grade)):
        if(top == grade[i]):
            print("Topper: ", names[i], ":", grade[i])
            
        if(low == grade[i]):
            print("Lowest Mark Obtained: ", names[i], ":", grade[i])

def display():
    print("Student List ")
    for i in range(0, len(grade)):
        print(names[i], ":", grade[i])

def Exit():
    print("Exit...")
    exit()
    
    
switch = {
    1 : add,
    2 : updateGrade,
    3 : RemoveStudent,
    4 : topLowScorer,
    5 : display,
    6 : Exit
}      
        
print("----Student Grade Management System----")

print("1. Add Student")
print("2. Update Student Mark")
print("3. Remove Student")
print("4.Topper & Lowest marks Obtained Student")
print("5. Display All Students")
print("6. Exit...")
choice = None
while choice != 6:
    choice = int(input("Enter Your Choice: "))
    func = switch.get(choice)
    if func:
        func()
    else:
        print("Enter Valid Chioice")