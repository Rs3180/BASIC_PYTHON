class Employee:
   company = "Google"
   salary = 100

harry = Employee()
rajni = Employee()

# Creating instance attribute salary for both the object
# harry.salary = 300 
# rajni.salary = 400
harry.salary = 44
print(rajni.salary)
print(harry.salary)

# Below line throwas an error as address is not present in instance/class
# print(rajni.address)