class Shopping:
def __init__(self):
self.items = []
self.quantity = []
self.price = []
self.subtotal = []
self.total = 0
self.afterdiscount = 0
self.gst = 0
self.finalamount = 0

def getinput(self):
n = int(input(&quot;Enter no of products: &quot;))
for i in range(n):
item = input(&quot;Enter item name: &quot;)
self.items.append(item)
qty = int(input(&quot;Enter quantity: &quot;))
self.quantity.append(qty)
price = int(input(&quot;Enter price: &quot;))
self.price.append(price)

def subtotalcalc(self):
for i in range(len(self.items)):
sub = self.quantity[i] * self.price[i]
self.subtotal.append(sub)
self.total += sub

def discount(self):
if self.total &gt; 3000:
self.afterdiscount = self.total -(self.total*0.10)

else:
self.afterdiscount = self.total

def gstcalc(self):
self.gst = self.afterdiscount * 0.05
self.finalamount=self.afterdiscount+self.gst

def display(self):
print(&quot;\n--- BILL ---&quot;)
print(&quot;Item\tQty\tPrice\tSubtotal&quot;)

for i in range(len(self.items)):
print(self.items[i], &quot;\t&quot;, self.quantity[i], &quot;\t&quot;,
self.price[i], &quot;\t&quot;, self.subtotal[i])

print(&quot;Total:&quot;, self.total)
print(&quot;After Discount:&quot;, self.afterdiscount)
print(&quot;GST:&quot;, self.gst)
print(&quot;Final Amount:&quot;, self.finalamount)

obj = Shopping()
obj.getinput()
obj.subtotalcalc()
obj.discount()
obj.gstcalc()
obj.display()
