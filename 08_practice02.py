name = input("Enter your name: ")
marks = input("Enter your marks: ")
phone = input("Enter you phone Number: ")

template = "The name of the student is {}, his marks are {} and phone Number is {}."
output = template.format(name,marks,phone)

print(output)