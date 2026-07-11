class ElectricityBill:
    def __init__(self, unit):
        self.unit = unit
        self.amount = 0

    def bill(self):
        if self.unit <= 100:
            self.amount = 0

        elif self.unit <= 200:
            self.amount = (self.unit - 100) * 1.5

        elif self.unit <= 300:
            self.amount = (100 * 1.5) + (self.unit - 200) * 2.5

        elif self.unit <= 400:
            self.amount = (100 * 1.5) + (100 * 2.5) + (self.unit - 300) * 4

        else:
            print("Unit above 400")

    def display(self):
        print("----- Electricity Bill -----")
        print("Units Consumed:", self.unit)
        print("Amount = ", self.amount)
unit = int(input("Enter units: "))
obj = ElectricityBill(unit)
obj.bill()
obj.display()
