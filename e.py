class Apple : 
    def __init__ (self, color, amount) :
        self.color = color
        self.amount = amount

    def cheese (self, n) :
        print('cheese: ' , n) 


Cheese = Apple('red', -1)
print(Cheese.cheese(1234567))
print(Cheese.color)