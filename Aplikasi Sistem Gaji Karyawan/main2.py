#NIP pegawai, Nama pegawai, tahun bekerja, jabatan, tunjangan, gaji pokok, alamat pegawai
import os
list_NIP = ["null"]
list_Nama = ["null"]
list_Mulaikerja = ["null"]
list_Tahunsekarang = ["null"]
list_Lamabekerja = ["null"]
list_Jabatan = ["null"]
list_Tunjangan = ["null"]
list_Gajipokok = ["null"]
list_Gajiditerima = ["null"]
list_Alamat = ["null"]
tunjangan = 0
no_struk = 0
status_input = True

loop_program = True
while loop_program == True:
	os.system("cls")
	print("===================================")
	print("     APLIKASI GAJI KARYAWAN")
	print("===================================")
	print("1.Hitung Gaji Karyawan")
	print("2.List Struk Gaji Karyawan")
	print("3.Keluar")
	login = input("Masukkan Pilihan Anda [1-3] : ")

	if login == "1":
		loop_hitunggaji = True
		while loop_hitunggaji == True:
			print("================================")
			print("    HITUNG GAJI KARYAWAN")
			print("================================")
			print("1.Manager")
			print("2.Senior IT")
			print("3.Staff Admin")
			jabatan = input("Masukkan Jabatan [1-3] : ")
			NIP = input("Masukkan NIP : ")
			nama = input("Masukkan Nama : ")
			mulai_kerja = int(input("Tahun Mulai Bekerja : "))
			tahun_sekarang = int(input("Tahun Menerima Gaji : "))
			lama_bekerja = tahun_sekarang - mulai_kerja
			alamat = input("Alamat : ")

			if jabatan == "1":
				jabatan = "Manager"
				gaji_pokok = 12000000
				if lama_bekerja > 2:
					tunjangan = 1000000
					gaji_pokok = gaji_pokok + tunjangan
			elif jabatan == "2":
				jabatan = "Senior IT"
				gaji_pokok = 9000000
				if lama_bekerja > 1:
					tunjangan = 700000
					gaji_pokok = gaji_pokok + tunjangan
			elif jabatan == "3":
				jabatan = "Staff Admin"
				gaji_pokok = 4200000
				if lama_bekerja > 2:
					tunjangan = 500000
					gaji_pokok = gaji_pokok + tunjangan
			else:
				status_input = False		

			gaji_diterima = gaji_pokok
			if status_input == True:
				os.system("cls")
				print("=============================")
				print("      KONFIRMASI DATA")
				print("=============================")
				print("NIP : ", NIP)
				print("Nama : ", nama)
				print("Jabatan : ", jabatan)
				print("Lama Bekerja : ", lama_bekerja, "Tahun")
				print("Alamat : ", alamat)
				print("Gaji Yang Diterima : ", gaji_diterima)
				dataconfirm = input("\nApakah Data Diatas Sudah Benar [y/t] = ")
				if dataconfirm == "y":
					list_NIP.append(NIP)
					list_Nama.append(nama)
					list_Jabatan.append(jabatan)
					list_Gajiditerima.append(gaji_diterima)
					list_Mulaikerja.append(mulai_kerja)
					list_Tahunsekarang.append(tahun_sekarang)
					list_Lamabekerja.append(lama_bekerja)
					list_Alamat.append(alamat)
					no_struk += 1
					os.system("cls")
					print("No Transaksi : ", no_struk)
					print("Data Telah Tersimpan")
					hitunggaji = input("Ingin Menghitung Ulang [y/t] = ")
					if hitunggaji == "y":
						os.system("cls")
					else:
						loop_hitunggaji = False	
			else:
				os.system("cls")
				print("Data Yang Anda Masukkan Salah, Silahkan Masukkan Kembali")
	elif login == "2":
		loop_riwayat = True
		while loop_riwayat == True:
			os.system("cls")
			print("================================")
			print("RIWAYAT PENERIMAAN GAJI KARYAWAN")
			print("================================")
			input_struk = int(input("Masukkan No Transaksi : "))
			print("")
			print("No Transaksi : ",input_struk)
			print("NIP : ", list_NIP[input_struk])
			print("Nama : ", list_Nama[input_struk])
			print("Jabatan : ", list_Jabatan[input_struk])
			print("Gaji + Tunjangan Yang Diterima : ", list_Gajiditerima[input_struk])
			print("Alamat : ", list_Alamat[input_struk])

			loop_data = input("Ingin Melihat Riwayat Kembali [y/t] : ")

			if loop_data == "t":
				loop_riwayat = False
	else:
		print("")
		print("Program Berakhir")
		loop_program = False