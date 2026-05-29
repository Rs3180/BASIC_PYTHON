class calculator:
      def __init__(self, num):
            self.number = num

      def square(self):
            print(f"The vale of {self.number} square is {self.number **2}")
      
      def squareRoot(self):
            print(f"The vale of {self.number} square is {self.number **0.5}")
      
      def cube(self):
            print(f"The vale of {self.number} square is {self.number **3}")
   
      @staticmethod
      def greet():
            print("***********Hello ther welcome to the best calculator of the world************")

a = calculator(4)
a.greet()
a.square()
a.squareRoot()
a.cube()
