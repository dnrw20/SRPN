import re
import traceback

#GLOBAL VARIABLE
global stack                            #used to store input from user
stack = []
global max_value                         #the maximum avaliable output 
max_value = 2200000000
global min_value                        #the minimum available output 
min_value = -220000000
global answer
answer = 0
global random_times
random_times = 0
global random_list
#a list of random numbers to mimic SRPN calculator from moodle 
random_list = [ 1804289383, 846930886, 1681692777, 1714636915,1957747793, 424238335, 719885386, 1649760492, 596516649, 1189641421, 1025202362, 1350490027, 783368690, 1102520059,2044897763, 1967513926, 1365180540, 1540383426, 304089172, 1303455736, 35005211, 521595368,1804289383]

#main operation function
def main_operation():
    global stack
    global answer
    global max_value
    global min_value
    global random_time

    number = input("")

    input_list = re.split('([^0-9])', number)
    if input_list[0] == '' and input_list[1] == '-' and input_list[2]!= '':
        input_list = number.split()
    # used to restrict the stack length
    elif len(stack) > 100:
        try:#if the input is operator it will go to except
            number = int(number) 
            print('Stack overflow.\n')
            main_operation()
        except:
            pass
        
    for element in input_list:
        if element == '#': #programme will be ignoring this operator when user will input #
            break 
        
        elif element == '' or element == ' ':
            continue #if the input is different than #, the operation will continue 

        elif element == '+' or element == '-' or element == '*' or element == '/' or element =='%' or element == '^' :
            basic_operation(element)
        #display stack
        elif element == 'd': #not value 
            for i in stack:
                print (i) 
        #generate random number for random list
        elif element == 'r': #used for the first number from the randon list to mimic the SRPN 
            if len(stack) < 60: #Error handling-stack overflow
                element = random_number(element)
                if element == 'Stack overflow.':
                    print('Stack overflow.\n')
                else:
                    append_into_stack(element)
            else:
                print("Stack overflow.\n")    
        elif element == '=':
            print (stack[-1])
            
        else:
            append_into_stack(element)
        
    #main_operation()


#  '+' '-' '*' '/' '%' to give saturated Reverse Polish Notation answer for every input 

def basic_operation(element):
    global stack
    global answer

    try:

      if element == '+': #for +
        answer = stack.pop() + stack.pop()
        answer = checkValue(answer)
        stack.append(answer)
              
      elif element == '-':
        answer = -stack.pop()+stack.pop()
        answer = checkValue(answer)
        stack.append(answer)
                      
      elif element == '*':
        answer = stack.pop() * stack.pop()
        answer = checkValue(answer)
        stack.append(answer)
                      
      elif element == '/':
        if stack[-1] == 0:
          print('Divide by 0.\n')
        else:
          if stack[-1]*stack[-2] < 0:
            answer = -(-stack.pop(-2)/stack.pop())
          else:
              answer =stack.pop(-2)/stack.pop()
              answer = checkValue(answer)
              stack.append(answer)
                  
      elif element == '%':
        if stack[-2]*stack[-1] < 0:
          answer = -(stack.pop(-2) % stack.pop())
        else:
            answer = stack.pop(-2) % stack.pop()
            answer = checkValue(answer)
            stack.append(answer)
      
      elif element == '^':
        answer = stack.pop(-2)**basic_operation()
        answer = int(answer)
        answer = checkValue(answer)
        stack.append(answer)
    
    except: #Error handling
      print("Stack underflow")

                  
def checkValue(i):#check whether the answer is able to handle saturated input 
    global max_value, min_value
    if i > max_value:
        i = max_value
    elif i < min_value:
        i = min_value
    return i
    
def append_into_stack(i):
    try:
        return stack.append(int(i))
    except:
        print("Unrecognised operator or operand \"" + str(i) + "\". \n") ## Error handling for unrecognised operators
        
def random_number(i):#used for symbol 'r'
    global random_list
    global random_times

    if random_times == 60:
        random_times = 0
        
    try:
        i = random_list[random_times]
        random_times += 1
        return i
    except :
        i = 'Stack overflow.'
        return i
                    
while(True):
    try:
      main_operation()
    except Exception: #error handling 
      traceback.print_exc()      

