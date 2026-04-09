# for i in range(1,11):
#     print(i," X 2 =", i*2 )

# for i in range(1,11):
#     print(i," X 3 =", i*3 )
        
# for i in range(1,11):
#     print(i," X 4 =", i*4 )


# table = int(input("Enter table: "))
# for i in range(1,11):
#     print(i," X ",table,"=", i*table )
    


# using for loop create multipul tables
end = int(input("Enter table: "))
for i in range(2, end+1):
    for j in range(1,11):
        print(j," X ",i,"=", j*i )
    print()
