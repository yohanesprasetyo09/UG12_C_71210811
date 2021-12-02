y = int(input("Input : "))
print("Output : ")   

for col in range(1,y+1):

    for row in range(1,y+1):

        if(row == 1) or (col == y) or (row == col):
            print("*",end=" ")
        
        else:
            print(" ", end=" ")
            
    print()