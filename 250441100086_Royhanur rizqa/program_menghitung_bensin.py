print("="*50)
print("program menghitung total biaya bensin dan berapa kali isi bensin untuk sampai ke tujuan")
jarak=int(input("masukkan jarak yang ingin ditempuh(86) :"))#punya saya 86KM
konsumsi_b=float(2.7) #km
kapasitas=int(input("masukkan kapasitas tangki(6) :"))#punya saya 6 liter
harga=int(input("masukkan harga bensin per liter(1086) :")) #punya saya 1086
diskon=500
h_setelah_d=harga-diskon
total_isi_b=jarak/(kapasitas*konsumsi_b) # <----berapa kali isi bensin
total_b=kapasitas*int(total_isi_b)
total_harga=h_setelah_d*total_b
print("jadi total bensin yang dibutuhkan kurang lebih adalah :",(total_b),("liter"))
print("total biaya yang harus dikeluarkan adalah Rp ",int(total_harga),(" dan memerlukan"),int(total_isi_b),("kali isi bensin"))