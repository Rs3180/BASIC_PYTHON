class Employee:
      company = "Bharat Gas"
      salary = 5600
      salarybonus = 500
#       extra = 3000
      # totalSalary = 6100

      @property
      def totalSalary(self):
            return self.salary + self.salarybonus  #+ self.extra
      
      @totalSalary.setter
      def totalSalary(self, val):
            self.salarybonus = val - self.salary
e = Employee()
print(e.totalSalary)
print(e.salary)
e.totalSalary = 5800
print(e.salarybonus)