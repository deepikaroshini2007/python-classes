class Employee:
    def __init__(self,n):
        self.name=  []
        self.empid=[]
        self.basic=[]
        self.gross=[]
    def input_details(self,n):
        for i in range(n):
           name=input("Enter Employee Name:")
           self.name.append(name)
           empid=int(input("Enter Employee ID:"))
           self.empid.append(empid)
           basic=int(input("Enter Basic salary Details:"))
           self.basic.append(basic)
    def calculate_salary(self,n):
            for i in self.basic:

                da=0.10*i
                hra=0.20*i
                gross=i+da+hra
                self.gross.append(gross)
    def display(self):
        for i in range(n):
            print(f"-------EMPLOYEE {i+1}-------")
            print("employee name:",self.name[i])
            print("employee id:",self.empid[i])
            print("Salary:",self.gross[i])

n=int(input("enter no of employee:"))
emp=Employee(n)
emp.input_details(n)
emp.calculate_salary(n)
emp.display()

