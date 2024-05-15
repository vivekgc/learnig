class Computer:
    attr1 = "Computer"
    attr2="Laptop"
    def fun(self):
        print("I'm a ",self.attr1)
        print("I'm a ", self.attr2)

Victus = Computer()
print(Victus.attr2)
Victus.fun()