class Student:
    school="VNUAPT Mat School"
    def __init__(self,name,marks,id):
        self.name=name
        self.marks=marks
        self.id=id
    def display(self) :
        sum=0
        for i in self.marks:
            sum+=i
        average=sum/len(self.marks)
        if average>=90:
            grade="o"
        elif average>=80 and average<90:
            grade="A+"
        elif average>=70 and average<80:
            grade="A"
        elif average>=60 and average<70:
            grade="B+"
        elif average>=55 and average<60:
            grade="B"
        elif average>=50 and average<55:
            grade="C"
        else:
            grade="F"
        print("\n--------Student Details--------")

        print("Name:",self.name)
        print("Marks:",self.marks)
        print("Id:",self.id)
        print("School:",Student.school)
        print("total:",sum)
        print("Average:",average)
        print("Grade:",grade)
n=int(input("Enter the number of students:"))
for i in range(n):
    name=input("Enter Student Name: ")
    id=int(input("Enter Student Id: "))
    subject=int(input("Enter no of subjects: "))
    mark=[]
    for i in range(subject):
          marks=int(input(f"Enter Student Mark {i+1}:"))
          mark.append(marks)
    s=Student(name,mark,id)
    s.display()


