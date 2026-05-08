list = [1,2,3,4,5,6]
while True:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    try:
        print(num1/num2)
        print(list[num1])
    except ZeroDivisionError:
        print("A number is not divisable by zero")    
    except:
        print("Index",num1,"is out of range")    
    else:
        print("The Index is correct.",num1)    
    finally:
        print("This block will always be execute")        