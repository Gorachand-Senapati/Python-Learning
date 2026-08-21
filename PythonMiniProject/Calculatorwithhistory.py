HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE,'r') #we read
    lines = file.readlines() # lines read
    if len(lines)==0:
        print("NO history found")
    else:
        # print(lines)
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(HISTORY_FILE,'w') #overwrite past lines are delted
    file.close()
    print('History cleared.')

def save_to_history(equation,result):
    file = open(HISTORY_FILE,'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def claculator(user_input):
    # parts = user_input.split()
    # if(len(parts)!= 3):
    #     print('Invalid input .like 8 + 8')
    #     return
    # num1 = float(parts[0])
    # op=parts[1]
    # num2 = float(parts[2])

    # if op=='+':
    #    result= num1 + num2
    # elif op=='-':
    #    result= num1 - num2
    # elif op=='*':
    #    result= num1 * num2
    # elif op=='/':
    #   if num2 ==0:
    #       print("u can not devide by 0")
    #       return
    #   result=  num1 / num2
    # elif op=='%':
    #    result= num1 % num2
    # else:
    #     print("not valid operator")
    #     return
    try:
        result = eval(user_input)
        if int(result)==result:
                result = int(result)
        print("Result: ", result)
        save_to_history(user_input, result)
    except ZeroDivisionError:
        print("you dont divide by 0")
    except:
        print("invalid calculation")

    

def main():
    print('---SIMPLE CALCULATOR (type history, clear or exist)')

    while True:
        user_input= input("Enter calcution or clear or history exist: ")
        if (user_input == 'exist') :
            print("Good Bye")
            break
        elif user_input == 'history':
            show_history()
        elif user_input =="clear":
            clear_history()
        else:
            claculator(user_input)

  
main()