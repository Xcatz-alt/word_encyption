#function untuk melakukan prosess enkripsi reverse chiper
def reverse(text):
    #kata yang di enkrispi akan di masukan ke sini
    result = ""  
    #menghitung jumlah kata yang di input
    i = len(text) - 1
    #proses pengulangan panjang kata dan membalikannya
    while i >= 0:   
        result = result + text[i]   
        i = i - 1
    return result

#function untuk melakukan prosess enkripsi caesar chiper
def caesar(text,s):
    #kata yang di enkrispi akan di masukan ke sini
    result = ""
    # menghitung text yang di input
    for i in range(len(text)):
        char = text[i]
        # Enkripsi huruf kapital di text input
        if (char.isupper()):#mengecek jika ada huruf kapital di text yang di input
            result += chr((ord(char) + s-65) % 26 + 65)#angka bisa di ganti agar output enkripsi berbeda
            """
            mengubah dari angka menjadi kata dari jumlah dari odr(char) 
            kemudian di tambah (s) lalu di - 65 lalu di modulo 26 setelah itu di tambah 65 
            kemudian hasil angka di jadikan character/kata dengan chr()
            """
        # enkripsi huruf non kapital di text input
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)#angka bisa di ganti agar hasil output enkripsi berbeda
            """
            mengubah dari angka menjadi kata dari jumlah dari odr(char) 
            kemudian di tambah (s) lalu di - 97 lalu di modulo 26 setelah itu di tambah 97 
            kemudian hasil angka di jadikan character/kata dengan chr()
            """
    return result

cas = False
while True:  #pengulangan prosess input data
    print("======================")
    print("PROGRAM ENKRIPSI")
    print("Athabiq tuah wibisana\n19.01.4295")
    print("======================")
    text = input("Masukan kata: ")
    print("Jenis enkripsi\n1. Reverse Chiper\n2. caesar chiper ")
    Type = input("Pilih jenis enkripsi: ")
    
    if Type == "1":#if jika input(type) 1 maka jalankan perintah
        print("Hasil reverse chiper: ",reverse(text))

    if Type == "2":#if jika input(type) 2 maka jalankan perintah
        s = int(input("Masukan jumlah pergeseran: "))#input jumlah angka pergeseran
        print("Hasil caesar chiper: ",caesar(text,s))
    
    ulang = input("ingin Mengulang?:(Y/N)")#pengulangan jika ingin mengulang program
    if ulang == "N":
        break
    elif ulang == "n":
        break
