# age = 16
# #after if need to give indentation space block else seen error and give : colone
# if age>=18:
#     print("you are eligible for vote")
#     print("you are adult")
# elif (age<18 and age>11):
#     print("you are not eligible for vote")
#     print("you are teenager")
# else:
#     print("you are not eligible for vote")
#     print("you are child")

# number = input("Enter your marks:")
# marks=int(number)
# if (marks<=100 and marks>80):
#     print("AA")
# elif(marks<=80 and marks>60):
#     print("A")
# elif(marks<=60 and marks>40):
#     print("B")
# else:
#     print("D")

#make a calculator
x = input("Enter a: ")
a=int(x)
b= int(input("Enter b: "))

op = input("Enter operator: ")

if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='*':
    print(a*b)
elif op=='/':
    print(a*b)
elif op=='%':
    print(a%b)
elif op=='**':
    print(a**b)
else:
    print("NOt a operator")
