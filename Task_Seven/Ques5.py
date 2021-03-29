class Person:
    def __init__(self, initialAge):
        if initialAge<0:
            print("Age is not valid, setting it to zero.")
            self.age=0
        else:
            self.age=initialAge

    def yearPasses(self, initialAge):
        print("Increased age is:", self.age+initialAge)
    def amIOld(self):
        if self.age<13:
            print("You are young")
        elif self.age>=13 and self.age<=19:
            print("You are teenager")
        else:
            print("You are old")

t=int(input("Number of inputs:"))
for i in range(0,t):
    age=int(input("Enter age: "))
    oj=Person(age)
    oj.yearPasses(age)
    oj.amIOld()