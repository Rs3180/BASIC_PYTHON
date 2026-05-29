class Employee:
    company = "Google"

    def getsalary(self, signature):
        print(f"salary for this employee working in {self.company} is {self.salary}\n {signature} ")

    @staticmethod
    def greet():
        print("Good Morning, sir")

    @staticmethod
    def time():
        print("The time is to long")

harry = Employee()  
harry.salary = 10000    
harry.getsalary("Thanks!") # Employee.getsalary(harry)
harry.greet() # Employee.greet()
harry.time()