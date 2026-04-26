class Student:
school=&quot;VNUAPT Mat School&quot;
def __init__(self,name,marks,id):
self.name=name
self.marks=marks
self.id=id
def display(self) :
sum=0
for i in self.marks:
sum+=i
average=sum/len(self.marks)
if average&gt;=90:
grade=&quot;o&quot;
elif average&gt;=80 and average&lt;90:
grade=&quot;A+&quot;
elif average&gt;=70 and average&lt;80:
grade=&quot;A&quot;
elif average&gt;=60 and average&lt;70:
grade=&quot;B+&quot;
elif average&gt;=55 and average&lt;60:
grade=&quot;B&quot;
elif average&gt;=50 and average&lt;55:
grade=&quot;C&quot;
else:
grade=&quot;F&quot;

print(&quot;\n--------Student Details--------&quot;)

print(&quot;Name:&quot;,self.name)
print(&quot;Marks:&quot;,self.marks)
print(&quot;Id:&quot;,self.id)
print(&quot;School:&quot;,Student.school)
print(&quot;total:&quot;,sum)
print(&quot;Average:&quot;,average)
print(&quot;Grade:&quot;,grade)
n=int(input(&quot;Enter the number of students:&quot;))
for i in range(n):
name=input(&quot;Enter Student Name: &quot;)
id=int(input(&quot;Enter Student Id: &quot;))
subject=int(input(&quot;Enter no of subjects: &quot;))
mark=[]
for i in range(subject):
marks=int(input(f&quot;Enter Student Mark {i+1}:&quot;))
mark.append(marks)
s=Student(name,mark,id)
s.display()
