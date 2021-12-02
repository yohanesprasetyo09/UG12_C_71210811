mapel = [
    ["2 Matematika Teknik", "4 Bhs Indonesia", "6 PKN"],
    ["1 Riset Operasi ", "3 Sistem Operasi", "5 Praktikum INLAN"],
    ["1 IMK", "3 LogMat", "4 Praktekkom"],
    ["2 Sistem Bisnis Data","4 Praktikum Sistem Basisata", "6 INLAN"]
]

x = str(input("Hi Momo, Silahkan Masukkan hari yang ingin Anda telusuri: ")). lower()

if x == "senin":
    print("Hari", x, "Anda tidak ada kelas")
elif x == "selasa":
    for a in mapel[0]:
        print("kelas ke - {}".format(a))
elif x == "rabu":
    for a in mapel[1]:
        print("kelas ke - {}".format(a))
elif x == "kamis":
    for a in mapel[2]:
        print("kelas ke - {}".format(a))
elif x == "jumat":
    for a in mapel[3]:
        print("kelas ke - {}".format(a))