def add():
    a=int(input("enter the 1st number"))
    b=int(input("enter the 2st number"))
    print (f'the addition of two number is {a+b}')


def subtract():
    a=int(input("enter the 1st number"))
    b=int(input("enter the 2st number"))
    print (f'the subtract of two number is {a-b}')


def multiply():
    a=int(input("enter the 1st number"))
    b=int(input("enter the 2st number"))
    print (f'the multiply of two number is {a*b}')

    
def divide():
    a=int(input("enter the 1st number"))
    b=int(input("enter the 2st number"))
    print (f'the divide of two number is {a/b}')
    


while(True):
        print("press 1 for add") 
        print("press 2 for substrac") 
        print("press 3 for multiplay") 
        print("press 4 for divide") 
        print("press 5 for exit the program") 
        
        c=int(input("enter your choise"))

        if c==1:
            add()
        elif c==2:
             subtract()
        elif c==3:
             multiply()
        elif c==4:
             divide()
        elif c==5:
            print("thank you for using calculator :)")
            break
        else:
            print("the site is under construction plese try again aftor some time")

            


