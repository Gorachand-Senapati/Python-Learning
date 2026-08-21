#list

# marks = [98,89,76,'A',7.98] # any type of data store here no problem
# # print(marks, type(marks))

# # #length
# # print(len(marks))
# #index
# # print(marks[4]) # 7.98
# # print(marks[-1]) # 7.98 from last

# #slicing list[st:end]
# print(marks [0:3]) #[98, 89, 76]
# print(marks[-3:]) #[76, 'A', 7.98]
# print(marks[-3:-1]) #[76, 'A']
# print(marks[:3])

# for v in marks:
#     print(v)
 
# marks= [83,89,57,98,87]
#     # list is dynamic mutable you add and change it
# marks.append(80) # add in last
# marks.insert(0,50) #put in any idx
# print(marks)
# marks.clear()
# print(marks)
# print(len(marks))



#tupple -> immutable not change

# marks = (93,93,83,82,75)
# print(marks,type(marks))
# print(marks[3])
# print(marks.count(93))
# # marks[0]=98 # not possible


# set = uniqe item collections
# marks = {93,83,93,83,98,76}
# print(len(marks))
# for i in marks:
#     print(i)


#dictionary -> collection of key and value and dictionary key are unique

# marks = {"Math":80, "Phy":80,"Chem":71,"Bio":74}

# print(marks,type(marks))
# marks["Phy"] =90
# marks["Eng"] =90
# print(marks["Eng"])

# for key in marks:
#     print(key,marks[key])  


    # tupple fast as compare to list bcz of immutable and mutable(add modify so time consume)

emp1 = {"id":101,"name":"Ravi","sal":10000}
emp2 = {"id":102,"name":"Raj","sal":16000}
emp3 = {"id":103,"name":"kavi","sal":10500}
ask = input("Enter emp id: ")
if ask =="101":
    print(emp1)
elif ask =="102":
    print(emp2)
elif ask =="103":
    print(emp3)
else :
    print("Not a employee")