import os
list_mahasiswa = ["null"]
list_jeniskelamin = ["null"]
list_tempattanggallahir = ["null"]
list_notelepon = ["null"]
list_alamat = ["null"]
list_asalsekolah = ["null"]
list_nisn = ["null"]
list_jurusan = ["null"]
kondisi_input = True
no_daftar = 0
ulang_program = "yes"
while ulang_program == "yes":
	os.system('cls')
	print("================================================")
	print("         APLIKASI PENDAFTARAN MAHASISWA")
	print("================================================")
	print("1.Tambahkan Mahasiswa Baru")
	print("2.List Pendaftaran Mahasiswa")
	print("3.Keluar")
	login = input("Masukkan Pilihan Anda (1-3) = ")

	if login == "1":
		ulang_daftar = "yes"
		while ulang_daftar == "yes":
		    print("================================================")
		    print("          Penerimaan Mahasiswa Baru")
		    print("================================================")
		    print("Kode\t\tJurusan         \tBiaya")
		    print("SI\t\tSistem Informasi  \t12000000")
		    print("MJ\t\tManajemen         \t13000000")
		    print("IH\t\tIlmu Hukum        \t15000000")
		    print("AG\t\tAgriBisnis        \t12000000")
		    print("IK\t\tIlmu Komputer     \t12000000")
		    print("TI\t\tTeknik Informatika\t15000000")
		    print("================================================")
		    print("        FORM PENDAFTARAN MAHASISWA BARU")
		    print("================================================\n")

		    #input
		    nama = input("Masukkan Nama = ")
		    kelamin = input("Masukkan Jenis Kelamin = ")
		    tempat_tanggallahir = input("Masukkan Tempat Dan Tanggal Lahir = ")
		    no_telepon = input("Masukkan No Telepon = ")
		    alamat = input("Masukkan Alamat Anda = ")
		    asal_sekolah = input("Asal Sekolah = ")
		    nisn = input("NISN = ")
		    jurusan = input("Masukkan Jurusan Yang Ingin Dipilih (SI, MJ, IH, AG, IK, TI) = ")
		    gelombang = input("Gelombang Ke (1,2,3) = ")

		    if jurusan == "SI":
		    	jurusan = "Sistem Informasi"
		    	biaya = 12000000
		    	if gelombang == "1":
		    		biaya_gelombang = 3000000
		    	elif gelombang == "2":
		    		biaya_gelombang = 4000000
		    	elif gelombang == "3":
		    		biaya_gelombang = 5000000
		    	else:
		    		biaya_gelombang = 0			
		    elif jurusan == "MJ":
		    	jurusan = "Manajemen"
		    	biaya = 13000000
		    	if gelombang == "1":
		    		biaya_gelombang = 3500000
		    	elif gelombang == "2":
		    		biaya_gelombang = 4500000
		    	elif gelombang == "3":
		    		biaya_gelombang = 5000000
		    	else:
		    		biaya_gelombang = 0			
		    elif jurusan == "IH":
		    	jurusan = "Ilmu Hukum"
		    	biaya = 15000000
		    	if gelombang == "1":
		    		biaya_gelombang = 4000000
		    	elif gelombang == "2":
		    		biaya_gelombang = 5000000
		    	elif gelombang == "3":
		    		biaya_gelombang = 6000000
		    	else:
		    		biaya_gelombang = 0			
		    elif jurusan == "AG":
		    	jurusan = "AgriBisnis"
		    	biaya = 12000000
		    	if gelombang == "1":
		    		biaya_gelombang = 3000000
		    	elif gelombang == "2":
		    		biaya_gelombang = 4000000
		    	elif gelombang == "3":
		    		biaya_gelombang = 5000000
		    	else:
		    		biaya_gelombang = 0			
		    elif jurusan == "IK":
		    	jurusan = "Ilmu Komputer"
		    	biaya = 12000000
		    	if gelombang == "1":
		    		biaya_gelombang = 3000000
		    	elif gelombang == "2":
		    		biaya_gelombang = 4000000
		    	elif gelombang == "3":
		    		biaya_gelombang = 5000000
		    	else:
		    		biaya_gelombang = 0			
		    elif jurusan == "TI":
		    	jurusan = "Teknik Informatika"
		    	biaya = 15000000
		    	if gelombang == "1":
		    		biaya_gelombang = 4000000
		    	elif gelombang == "2":
		    		biaya_gelombang = 5000000
		    	elif gelombang == "3":
		    		biaya_gelombang = 6000000
		    	else:
		    		biaya_gelombang = 0			
		    else:
		    	biaya_gelombang = 0
		    	kondisi_input = False

		    if kondisi_input == True:
		    	print("================================================")
		    	print("           DATA YANG ANDA MASUKKAN")
		    	print("================================================")
		    	no_daftar = no_daftar + 1
		    	print("No Pendaftaran Anda = PO",no_daftar)
		    	print("Nama : ", nama)
		    	print("Jenis Kelamin : ", kelamin)
		    	print("Tempat Dan Tanggal Lahir : ", tempat_tanggallahir)
		    	print("No Telepon : ", no_telepon)
		    	print("Alamat : ", alamat)
		    	print("Asal Sekolah : ", asal_sekolah)
		    	print("NISN : ", nisn)
		    	print("Jurusan : ", jurusan)
		    	print("Biaya : ", biaya)
		    	print("Biaya Gelombang: ", biaya_gelombang)
		    	savedata = input("Ingin Menyimpan Data (y/t) = ")
		    	if savedata == "y":
		    		list_mahasiswa.append(nama)
		    		list_jeniskelamin.append(kelamin)
		    		list_tempattanggallahir.append(tempat_tanggallahir)
		    		list_notelepon.append(no_telepon)
		    		list_alamat.append(alamat)
		    		list_asalsekolah.append(asal_sekolah)
		    		list_nisn.append(nisn)
		    		list_jurusan.append(jurusan)
		    		print("Data Tersimpan")
		    	elif savedata == "t":
		    		print("Data Tidak Tersimpan")
		    	pilihan = input("Ingin Memasukkan Data Lagi (y/t) ? ")

		    	if pilihan == "y":
		    		os.system('cls')
		    	elif pilihan == "t":
		    		ulang_daftar = "no"
	elif login == "2":
		os.system('cls')
		print("================================================")
		print("     TAMPILKAN DATA MAHASISWA TERDAFTAR")
		print("================================================")
		no_po = int(input("Masukkan No PO Anda = "))
		print("DATA MAHASISWA")
		print("Nama : ", list_mahasiswa[no_po])
		print("Jenis Kelamin : ", list_jeniskelamin[no_po])
		print("Tempat Dan Tanggal Lahir : ", list_tempattanggallahir[no_po])
		print("No Telepon : ", list_notelepon[no_po])
		print("Alamat : ", list_alamat[no_po])
		print("Asal Sekolah = ", list_asalsekolah[no_po])
		print("NISN = ", list_nisn[no_po])
		print("Jurusan : ", list_jurusan[no_po])

		pilihan_ulangprogram = input("Ingin Melanjutkan (y/t) = ")

		if pilihan_ulangprogram == "y":
			os.system('cls')
		elif pilihan_ulangprogram == "t":
			ulang_program = "no"	
	elif login == "3":
		print("Program Berakhir")
		ulang_program = "no"