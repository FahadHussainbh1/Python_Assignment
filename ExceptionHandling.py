while True:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a second number: "))
    
    try:
        print(num1/num2)
    except:
        print("A Number is not Divided by Zero, Please try agian")    
