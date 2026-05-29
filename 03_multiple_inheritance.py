class Employee:
      company = "Visa"
      eCode = 120

class Freelancer:
      company = "Fiverr"
      level = 5

      def upgradeLevel(self):
            self.level = self.level +1
            
class Programmer(Employee, Freelancer):
      name = "Raj"

p = Programmer()
p.upgradeLevel()
print(p.level)
print(p.company)
