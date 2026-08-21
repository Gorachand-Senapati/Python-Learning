#Reading a file

# f = open("myfile.txt", "rb") #myfile.txt open for read

# text = f.read()#read function
# print(text)
# f.close()#file closed
# #you not open for write as read give eror
#rb = binary file

#writing a file
# f = open("myfile2.txt", "a") #write and create a file
# f.write('Hello World')
# f.close()#file closed close is good practice to close the file after use without close it will give error sometimes

# with open('myfile2.txt', 'a') as f: #with open not need again close the file after use because with open automatically close the file after use
#     f.write('Hello World\n')
#     f.write('This is a new line.\n')
#     f.write('Appending more text to the file.\n')



# f= open('myfile2.txt','r')
# text = f.read()
# print(f.readline()) #read oneline
# lines = f.readlines() #read all lines and give as a list
# print(lines)

# for line in f:
#     print(line.strip())#eliminate the extra new line after each line because readlines give as a list and each line have new line so we use strip to eliminate the new line
# f.close()

# with open('myfile2.txt', 'r') as f:
#     text = f.read()
#     print(text)



#checking a file is exist or not
import os # import os module to check file exist or not

# if os.path.exists("myfle2.txt"):
#     print("File exist")
# else:
#     print("file not exist")

#delete file

if os.path.exists("myfilde.txt"):
    os.remove("myfile.txt")
    print("file deleted")
else:
    print("file does not exists")