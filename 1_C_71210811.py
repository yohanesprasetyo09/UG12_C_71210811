#UG12_SOAL1_71210811
angka1 = int(input("Masukkan awal deret : "))

angka2 = int(input("Masukkan akhir deret : "))

x = []

if (angka1 + 1) % 2 == 0:

    for i in range (angka1+1,angka2,2):

        if i % 9 == 0 or i % 11 == 0: continue

        print ( i , end = " " )

else:

    for i in range (angka1 , angka2 , 2):

        if i % 9 == 0 or i % 11 == 0 : continue

        print (i , end = " ")