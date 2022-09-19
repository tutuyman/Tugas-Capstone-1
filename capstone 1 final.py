#Nama Andri Rifky Aditama
#Kelas JCDS jakarta

pasien={
    'ABQ1':{'nama':'Walter', 'gender': 'Pria','umur':'52','penyakit':'Kanker'},
    'HHM3':{'nama':'Chuck','gender': 'Wanita','umur':'58','penyakit':'EHS'},
    'SLM1':{'nama':'Hector','gender': 'Pria', 'umur':'68','penyakit':'Stroke'}
}



def konfirmasi_hapus():
    print('')
    print('Apakah yakin? \n1.Ya\n2.Tidak')
    x=input('Masukan Angka\t:')
    if x=='1':
        return True
    else:
        return False

def ceknopasien1():
    cek=input('Masukan ID pasien\t:').upper()
    if " " in cek:
        print('ID tidak boleh mengandung spasi')
        ceknopasien1()
    else:
        if cek not in pasien.keys() and cek.isalnum() and (not cek.isalpha()) and (not cek.isnumeric()):
            global nopasien
            nopasien=cek.upper()
        elif cek not in pasien.keys() and cek.isnumeric():
            print('ID pasien hanya memiliki angka')
            print('iD pasien harus mengandung huruf dan angka')
            ceknopasien1()
        elif cek not in pasien.keys() and cek.isalpha():
            print('ID pasien hanya memiliki huruf')
            print('ID pasien harus mengandung huruf dan angka')
            ceknopasien1()
        elif cek in pasien.keys():
            print('ID Pasien sudah tersedia\n')
            ceknopasien1()

def ceknopasien2():
    cek=input('Masukan ID pasien\t:').upper()
    if cek in pasien.keys() and cek.isalnum():
        global nopasien
        nopasien=cek.upper()
        # print(nopasien)
    else:
        print('ID Pasien Tidak ada')
        Mengubah()    

def ceknama():
    cek=input('Masukan Nama\t:')
    if cek.replace(" ","").isalpha():
        global nama_tambah
        nama_tambah=cek.title()
    else:
        print("Nama Tidak sesuai format")
        ceknama()

def cekumur():
    cek=input('Masukan umur\t:')
    if cek.isnumeric():
        global umur_tambah
        umur_tambah=cek
    else:
        print('Umur Harus Angka')
        cekumur()

def cekgender():
    print('Gender\t:\n 1. Pria \n 2. Wanita \n ')
    cek=input('Pilih Gender\t:')
    if cek.isnumeric():
        global gen_tambah
        if cek=='1':
            gen_tambah='Pria'
        elif cek=='2':
            gen_tambah='Wanita'
        else:
            print('Harap Masukan Gender yang tesedia')
            cekgender()
    else:
        print('Pilihan bukan angka')
        cekgender()

def MenuUtama():
    print('''
    +Lovelace Medical Center Database+\n
    1. Tampilkan data Pasien
    2. Tambah Pasien
    3. Mengubah Info Pasien
    4. Menghapus Info Pasien
    5. Exit
    ''')
    pilihan = input("Masukkan Pilihan: ")
    if pilihan == '1':
        Menampilkan()
    elif pilihan == '2':
        Menambahkan()
    elif pilihan == '3':
        Mengubah()
    elif pilihan == '4':
        Menghapus()
    elif pilihan == '5':
        print('Sampai Jumpa')   
    else:
        print('Pilihan tidak tersedia')
        MenuUtama()

def Menambahkan(): #untuk menambah data
    print('\n\nMenu Tambah Pasien\n1. Tambah Pasien\n2. Kembali')
    input_user1=input('Masukkan Angka Yang Ingin Dijalankan\t:')
    if input_user1 == "1":
        ceknopasien1()
        ceknama()
        cekgender()
        cekumur()
        global peyakit_tambah
        peyakit_tambah= input('Penyakit\t:').title()
        print("ID\t|Nama\t\t\t|Gender\t|Umur\t|Penyakit")
        print(f"{nopasien}\t|{nama_tambah}\t\t\t|{gen_tambah}\t|{umur_tambah}\t|{peyakit_tambah}")
        print('\nApakah ingin menambah data ini?\n1.Ya\n2.Tidak')
        input_user1 = input("\nMasukkan Angka\t: ")
        if input_user1 == "1":
            pasien.update(
            {nopasien : {
            'nama' : nama_tambah,
            'gender' : gen_tambah,
            'umur' : umur_tambah,
            'penyakit' : peyakit_tambah }
            })
            print('\nPasien Berhasil Ditambah')
            Menambahkan()
        elif input_user1 == "2":
            print('\nData Pasien Tidak Jadi Ditambah')
            Menambahkan()
        else:
            print('\nMasukan sesuai angka yang tersedia')
            Menambahkan()
        
    elif input_user1 == "2":
        print('\nApakah Anda Ingin Ingin Meninggalkan Menu Tambah Pasien?\n1.Ya\n2.Tidak')
        input_user2 = input("Masukkan Angka\t: ")
        if input_user2 == "1":
            MenuUtama()
        elif input_user2 == "2":
            Menambahkan()
        else:
            print('\nMasukan sesuai angka yang tersedia')
            Menambahkan()
        
  

def Mengubah(): #untuk mengupdate data
    print('\n\nMenu Ubah Data Pasien\n1. Ubah Data Pasien\n2. Kembali')
    input_user1=input('Masukkan Angka Yang Ingin Dijalankan\t:')

    if input_user1 == "1":
        ceknopasien2()
        print('ID\t|Nama\t\t\t\t|Gender\t\t|Umur\t|Penyakit')
        print(f"{nopasien}\t|{pasien[nopasien]['nama']}\t\t\t\t|{pasien[nopasien]['gender']}\t\t|{pasien[nopasien]['umur']}\t|{pasien[nopasien]['penyakit']}")
        print('\nApakah Anda Ingin Mengubah Data Ini?\n1.Ya\n2.Tidak')
        input_user1 = input("Masukkan Angka\t: ")
        if input_user1 == "1":
            print('\nNama Kolom Yang Akan Diganti?')
            print('1. Nama\n2. Gender\n3. Umur\n4. Penyakit')
            input_user1 = input("Kolom yang diganti\t:")
            if input_user1 == "1":
                input_nama = input("Masukkan Nama Yang Baru\t:").title()
            elif input_user1 == "2":
                cekgender()
            elif input_user1 == "3":
                cekumur()
            elif input_user1 == "4":
                input_penyakit = input("Masukkan Penyakit\t:").capitalize()
            else:
                print('\nMasukan sesuai angka yang tersedia')
                Mengubah()
        elif input_user1 == "2":
            print('Data diatas tidak jadi diubah')
            Mengubah()
        else:
            print('\nMasukan sesuai angka yang tersedia')
            Mengubah()
        print('\nYakin Ingin Mengubah Data?\n1.Ya\n2.Tidak')         
        input_user2 = input("Masukkan Pilihan: ")
        if input_user1 == "1" and input_user2 == "1":
            pasien[nopasien] = {"nama" : input_nama, "gender" : pasien[nopasien]["gender"], "umur" : pasien[nopasien]["umur"], "penyakit" : pasien[nopasien]["penyakit"]}
            print('\nData Berhasil Diganti')
            Mengubah()
        elif input_user1 == "2" and input_user2 == "1":
            pasien[nopasien] = {"nama" : pasien[nopasien]['nama'], "gender" : gen_tambah, "umur" : pasien[nopasien]["umur"], "penyakit" : pasien[nopasien]["penyakit"]}
            print('\nData Berhasil Diganti')
            Mengubah()
        elif input_user1 == "3" and input_user2 == "1":
            pasien[nopasien] = {"nama" : pasien[nopasien]['nama'], "gender" : pasien[nopasien]["gender"], "umur" : umur_tambah, "penyakit" : pasien[nopasien]["penyakit"]}
            print('\nData Berhasil Diganti')
            Mengubah()
        elif input_user1 == "4" and input_user2 == "1":
            pasien[nopasien] = {"nama" : pasien[nopasien]['nama'], "gender" : pasien[nopasien]["gender"], "umur" : pasien[nopasien]["umur"], "penyakit" : input_penyakit}
            print('\nData Berhasil Diganti')
            Mengubah()
        elif input_user2 == "2":
            print('\nData Tidak Diubah')
            Mengubah()
        else:
            print('\nMasukkan Sesuai Nomor Yang Disediakan')
            Mengubah()

    elif input_user1 == "2":
            print('\nApakah Anda Ingin Ingin Meninggalkan Ubah Data Pasien?\n1.Ya\n2.Tidak')
            input_user3 = input("Masukkan Angka\t: ")
            if input_user3 == "1":
                MenuUtama()
            elif input_user3 == "2":
                Mengubah()
            else:
                print('\nMasukan sesuai angka yang tersedia')
                Mengubah()
    else:
        print('\nMasukan sesuai angka yang tersedia')
        Mengubah()

def Menghapus(): #untuk menghapus data
    print('\n\nMenu Menghapus Pasien\n1. Hapus Pasien\n2. Kembali')
    input_user1=input('\nMasukkan Angka Yang Ingin Dijalankan\t:')
    if input_user1 == "1":
        kode_hapus = input("\nMasukkan Kode pasien: ").upper()
        if kode_hapus in pasien.keys():
            print('ID\t|Nama\t\t\t\t|Gender\t\t|Umur\t|Penyakit')
            print(f"{kode_hapus}\t|{pasien[kode_hapus]['nama']}\t\t\t\t|{pasien[kode_hapus]['gender']}\t\t|{pasien[kode_hapus]['umur']}\t|{pasien[kode_hapus]['penyakit']}")
            if konfirmasi_hapus():
                pasien.pop(kode_hapus)
                print('\nData Berhasil dihapus')
                Menghapus()
            else:
                print('\nData batal dihapus')
                Menghapus()
        else:
            print('\nData tidak ada')
            Menghapus()
    elif input_user1 == "2":
        print('\nApakah Anda Ingin Ingin Meninggalkan Menghapus Pasien?\n1.Ya\n2.Tidak')
        input_user2 = input("Masukkan Angka\t: ")
        if input_user2 == "1":
            MenuUtama()
        elif input_user2 == "2":
            Menghapus()
        else:
            print('\nMasukan sesuai angka yang tersedia')
            Menghapus()
        
    else:
        print('\nMasukan sesuai angka yang tersedia')
        Menghapus()

def Menampilkan(): #untuk menampilkan data
    print('\n\nMenu tampil pasien\n1. Tampilkan seluruh data pasien\n2. Tampilkan data pasien spesifik\n3. Kembali')
    input_user1=input('\nMasukkan Angka Yang Ingin Dijalankan\t:')
    if input_user1 == "1":
        if pasien == {}:
            print('Tidak ada data')
            Menampilkan()
        else:
            print('\nID\t|Nama\t\t\t\t|Gender\t|Umur\t|Penyakit')
            for i in pasien:
                print(f"{i}\t|{pasien[i]['nama']}\t\t\t\t|{pasien[i]['gender']}\t|{pasien[i]['umur']}\t|{pasien[i]['penyakit']}")
            Menampilkan()
    elif input_user1 == "2":
        nopasien=input('Masukan ID pasien\t:').upper()
        if nopasien in pasien.keys() and nopasien.isalnum():
            print('ID\t|Nama\t\t\t\t|Gender\t\t|Umur\t|Penyakit')
            print(f"{nopasien}\t|{pasien[nopasien]['nama']}\t\t\t\t|{pasien[nopasien]['gender']}\t\t|{pasien[nopasien]['umur']}\t|{pasien[nopasien]['penyakit']}")
            Menampilkan()
        else:
            print('\nID pasien tidak ada')
            Menampilkan()
    elif input_user1 == "3":
        print('\nApakah Anda Ingin Ingin Meninggalkan Menu Tampilkan Data?\n1.Ya\n2.Tidak')
        input_user2 = input("Masukkan Angka\t: ")
        if input_user2 == "1":
            MenuUtama()
        elif input_user2 == "2":
            Menampilkan()
        else:
            print('\nMasukan sesuai angka yang tersedia')
            Menampilkan()
    else:
        print('\nMasukan sesuai angka yang tersedia')
        Menampilkan()

MenuUtama()

