class Employee:
def __init__(self,n):
self.name= []
self.empid=[]
self.basic=[]
self.gross=[]

def input_details(self,n):
for i in range(n):
name=input(&quot;Enter Employee Name:&quot;)
self.name.append(name)
empid=int(input(&quot;Enter Employee ID:&quot;))
self.empid.append(empid)
basic=int(input(&quot;Enter Basic salary Details:&quot;))
self.basic.append(basic)
def calculate_salary(self,n):
for i in self.basic:

da=0.10*i
hra=0.20*i
gross=i+da+hra
self.gross.append(gross)
def display(self):
for i in range(n):
print(f&quot;-------EMPLOYEE {i+1}-------&quot;)
print(&quot;employee name:&quot;,self.name[i])
print(&quot;employee id:&quot;,self.empid[i])
print(&quot;Salary:&quot;,self.gross[i])

n=int(input(&quot;enter no of employee:&quot;))
emp=Employee(n)
emp.input_details(n)
emp.calculate_salary(n)
emp.display()
