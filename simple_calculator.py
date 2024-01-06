import math as M
print("-----------------Calculator------------")


def AreaOfCircle(): 
          # area = π * r^2
          radius = float(input("Enter a radius of Circle "))
          area_of_the_circle = M.pi * radius ** 2
          print(f"The Area of a Circle is: {area_of_the_circle}")


def CirumferenceOfCircle():
          # C=2πr -->perimeter of a circle
          radius = float(input("Enter radius of Circle: "))
          circumference_of_the_circle =2 * M.pi * radius
          print(f"The Circumference of a Circle  is: {circumference_of_the_circle}")


def AreaOfTriangle():
          # A = ½ (b × h)
          base = float(input("Enter base of Triangle: "))
          height = float(input("Enter height of a Triangle: "))
          area_of_the_triangle = (1/2) * base * height
          print(f"The Area of a Triangle is : {area_of_the_triangle}")

def BasicCalculator():
          print("---------------------------------------")
          choice = input("-----------Basic Calculator------------ \n1.Addition(+) \n2.Subtraction(-) \n3.Multiplication(*) \n4.Division(/) \n5.Exponential(^) \nChoice any one of following options: ")
          print("---------------------------------------")
          if choice == "+":
                    a = float(input("Enter a: "))
                    b = float(input("Enter b: "))
                    sum = lambda a,b: a+b
                    print(f"the Sum of {a} and {b} is: {sum(a,b)}")
          elif choice == "-":
                    c = float(input("Enter a: "))
                    d = float(input("Enter b: "))
                    sub = lambda c,d: c-d
                    print(f"The Subtraction of {c} and {d} is: {sub(c,d)}")
          elif choice == "*":
                    a = float(input("Enter a: "))
                    b = float(input("Enter b: "))
                    mult = lambda a,b: a*b
                    print(f"The Multiplication of {a} and {b} is: {mult(a,b)}")
          elif choice == "/":
                    a = float(input("Enter a: "))
                    b = float(input("Enter b: "))
                    div = lambda a,b: a/b
                    print(f"The Division of {a} and {b} is: {div(a,b)}")
          elif choice == "^":
                    b = float(input("Choose power : "))
                    a = float(input("Enter a number: "))
                    exp = lambda a,b: a**b
                    print(f"The Value of {a} ^ {b} is : {exp(a,b)}") 

while True:
          print("---------------------------------------")
          print("1.Basic Calculator\n2.Area of a Circle \n3.Area of a Triangle \n4.Cirumference Of Circle")
          print("---------------------------------------")
          choice = int(input("Enter choice: "))
          if choice == 1:
                    BasicCalculator()
          elif choice == 2:
                    AreaOfCircle()
          elif choice == 3:
                    AreaOfTriangle()
          elif choice == 4:
                    CirumferenceOfCircle()
          elif choice == 5:
                    print("Exiting!!!")
                    break