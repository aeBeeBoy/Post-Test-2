nama = str(input("Tuliskan Nama Lengkap Anda: "))
nim = int(input("Masukkan NIM Anda: "))
harga = float(input("Masukkan Harga: "))

# diskon setiap gula
gulaku = 0.07
manis_kita= 0.11
gunung_madu = 0.13

# harga diskon
diskon_gulaku = harga * gulaku
diskon_manis_kita = harga * manis_kita
diskon_gunung_madu = harga * gunung_madu

# harga setelah diskon
harga_akhir_gulaku = harga - diskon_gulaku
harga_akhir_manis_kita = harga - diskon_manis_kita
harga_akhir_gunung_madu = harga - diskon_gunung_madu

# output
print(f"{nama} dengan NIM {nim} ingin membeli gula seharga Rp.{harga:,.0f}")
print(f'''
Jika dia membeli Gulaku ia harus membayar Rp.{harga_akhir_gulaku:,.0f} Setelah mendapat diskon 7%
Jika dia membeli Manis Kita ia harus membayar Rp.{harga_akhir_manis_kita:,.0f} Setelah mendapat diskon 11%
Jika dia membeli Gunung Madu ia harus membayar Rp.{harga_akhir_gunung_madu:,.0f} Setelah mendapat diskon 13%
''')