A2 = input( "Input : " )

B2 = len ( A2 )

print ( " Output : " )

for kolom in range( B2 ):

    for baris in range(kolom+1):

        print(A2 [ baris],end="")
    print()
    
for kolom in range( B2 ):

    for baris in range( B2 - kolom - 1):
        
        print(A2 [ baris ],end="")
    print()