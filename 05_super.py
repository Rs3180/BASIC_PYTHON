class Person:
      country = "India"

      def __init__(self):
           print("Initializing Person....\n")

      def takeBreath(self):
           print("I am breathing...")

class Employee(Person):
      comapny = "Honda"

      def __init__(self):
           super().__init__()
           print("Initializing Employee...\n")

      def getSalary(self):
           print(f"Salary is {self.salary}")

      def takeBreath(self):
           super().takeBreath()
           print("I am an Employee so I am luckily breaking..")

class Programmer(Employee):
      comapny = "Fiverr"
      
      def __init__(self):
           super().__init__()
           print("Initializing Programmer...\n")

      def getSalary(self):
           print(f"No salary to programmers")

      def takeBreath(self):
           super().takeBreath()
           print("I am a Programmer so I am breathing..")

# p = Person()
# p.takeBreath()

# print(p.company)    #throws an error

# e = Employee()
# e.takeBreath()

# print(e.comapny)

pr = Programmer()
# pr.takeBreath()

# print(pr.comapny)
# print(pr.country )
