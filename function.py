#define the function
# def sum(a,b):
#     return a + b
# result = sum(5, 10) call
# print(result)

# def mul(a,b):
#     print(a*b)

# mul(8,5) #function call


#gst
# def gst(a):
#     print(a+(a*0.18))

# gst(100)
# gst(2050)

# def gst(a):
#     return a+(a*0.18)
# print(gst(100))
# print(gst(200))

# this are userdefind function which we decide

#inbuilt functions are - print, input, type,len

# module function collection of related functions so use import

# import math
# print(dir(math)) #give math related functions

# from math import sqrt //any function import from math for check whats function run the previous
# print(sqrt(9))

# import random
# print(random.random())  #from 0 to 1 random number
# print(random.random()*100) #from 0 to 100 random number
# print(random.randint(1,10))

# vow= ['A','a','e','E','i','I','o','O','u','U']

# word = "Hello World"
# def vowel(word):
#     cnt = 0
#     for i in word:
#         if i in vow:
#             cnt+=1
#     return cnt

# print(vowel(word))

def prime(num):
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime= False
            break

    if(is_prime== True):
        print(num,"is prime")
    else:
        print(num,"is not prime")

prime(9)            
        
   

