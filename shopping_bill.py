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
        n = int(input("Enter no of products: "))
        for i in range(n):
            item = input("Enter item name: ")
            self.items.append(item)
            qty = int(input("Enter quantity: "))
            self.quantity.append(qty)
            price = int(input("Enter price: "))
            self.price.append(price)

    def subtotalcalc(self):
        for i in range(len(self.items)):
            sub = self.quantity[i] * self.price[i]
            self.subtotal.append(sub)
            self.total += sub

    def discount(self):
        if self.total > 3000:
            self.afterdiscount = self.total -(self.total*0.10)
        else:
            self.afterdiscount = self.total

    def gstcalc(self):
        self.gst = self.afterdiscount * 0.05
        self.finalamount=self.afterdiscount+self.gst

    def display(self):
        print("\n--- BILL ---")
        print("Item\tQty\tPrice\tSubtotal")

        for i in range(len(self.items)):
            print(self.items[i], "\t", self.quantity[i], "\t",
                  self.price[i], "\t", self.subtotal[i])

        print("Total:", self.total)
        print("After Discount:", self.afterdiscount)
        print("GST:", self.gst)
        print("Final Amount:", self.finalamount)

obj = Shopping()
obj.getinput()
obj.subtotalcalc()
obj.discount()
obj.gstcalc()
obj.display()
