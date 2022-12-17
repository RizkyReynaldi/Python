import os
import array
list_noruang = ["null"]
list_nama = ["null"]
list_nik_penyewa = ["null"]
list_checkin = ["null"]
list_checkout = ["null"]
list_totalbiaya = ["null"]
biaya_perhari = 0
lama_sewa = 0
total_biaya = 0
kode = 0
kode_transaksi = 0
def tampilData():
	print("===========================")
	print("   List Tamu Terdaftar")
	print("===========================")
	kode = int(input("Masukkan No Transaksi : "))
	print("===========================")
	print("No Kamar : ", list_noruang[kode])
	print("Nama : ", list_nama[kode])
	print("NIK : ", list_nik_penyewa[kode])
	print("Checkin : ", list_checkin[kode])
	print("Checkout : ", list_checkout[kode])
	print("Total Transaksi : ", list_totalbiaya[kode])


ulang_program = True
while ulang_program == True:
	os.system("cls")
	print("==============================")
	print("Aplikasi Penyewaan Kamar Hotel")
	print("==============================")
	print("1.Sewa Kamar Hotel")
	print("2.List Ruangan")
	print("3.Keluar")
	option_login = input("Masukkan Pilihan Anda = ")

	if option_login == "1":
		ulang_sewa = True
		while ulang_sewa == True:
			os.system("cls")
			print("=============================")
			print("Masukkan Data Lengkap Penyewa")
			print("=============================")
			nama_penyewa = input("Masukkan Nama Pelanggan : ")
			nik_penyewa = input("Masukkan NIK KTP Pelanggan : ")
			waktu_checkin = input("Tanggal Checkin : ")
			waktu_checkout = input("Tanggal Checkout : ")
			lama_sewa = int(input("Total Hari Sewa : "))
			no_kamar = int(input("No Kamar : "))
			tipe_kamar = input("Tipe Kamar |1,2,3| : ")
			if tipe_kamar == "1":
				tipe_kamar = "Private Room"
				biaya_perhari = 550000
			elif tipe_kamar == "2":
				tipe_kamar = "Superior Room"
				biaya_perhari = 400000
			elif tipe_kamar == "3":
				tipe_kamar = "Standar Room"
				biaya_perhari = 350000
			else:
				biaya_perhari = 0
			os.system("cls")
			print("=========================")
			print("    Konfirmasi Data")
			print("=========================")
			print("No Kamar : ", no_kamar)
			print("Tipe Kamar : ", tipe_kamar)
			print("Nama : ", nama_penyewa)
			print("NIK : ", nik_penyewa)
			print("Checkin : ", waktu_checkin)
			print("Checkout : ", waktu_checkout)
			print("Lama Menginap : ", lama_sewa)
			total_biaya = lama_sewa * biaya_perhari
			print("Total Biaya : ", total_biaya)
			konfirmasi_data = input("Apakah Data Sudah Benar [y/t] ? ")
			if konfirmasi_data == "y":
				list_noruang.append(no_kamar)
				list_nama.append(nama_penyewa)
				list_nik_penyewa.append(nik_penyewa)
				list_checkin.append(waktu_checkin)
				list_checkout.append(waktu_checkout)
				list_totalbiaya.append(total_biaya)
				os.system("cls")
				print("Data Pelanggan Disimpan")
				kode_transaksi = kode_transaksi + 1
				print("Kode Transaksi : ", kode_transaksi)
			option_ulang_sewa = input("Apakah Ingin Masukkan Data Kembali [y/t] ? ")
			if option_ulang_sewa == "t":
				ulang_sewa = False
	elif option_login == "2":
		ulang_list_ruangan = True
		while ulang_list_ruangan == True:
			os.system("cls")
			tampilData()
			option_ulang_list = input("Ingin Lihat List Kembali [y/t] ? ")
			if option_ulang_list == "t":
				ulang_list_ruangan = False
	elif option_login == "3":
		ulang_program = False			