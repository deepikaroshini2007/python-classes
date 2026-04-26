class ElectricityBill:
def __init__(self, unit):
self.unit = unit
self.amount = 0

def bill(self):
if self.unit &lt;= 100:
self.amount = 0

elif self.unit &lt;= 200:
self.amount = (self.unit - 100) * 1.5

elif self.unit &lt;= 300:
self.amount = (100 * 1.5) + (self.unit - 200) * 2.5

elif self.unit &lt;= 400:
self.amount = (100 * 1.5) + (100 * 2.5) + (self.unit - 300) * 4

else:
print(&quot;Unit above 400&quot;)

def display(self):
print(&quot;----- Electricity Bill -----&quot;)
print(&quot;Units Consumed:&quot;, self.unit)
print(&quot;Amount = &quot;, self.amount)
unit = int(input(&quot;Enter units: &quot;))
obj = ElectricityBill(unit)
obj.bill()
obj.display()
