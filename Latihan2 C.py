gaji_per_jam = float(input("Masukkan gaji per jam: "))
jam_per_minggu = float(input("Masukkan jumlah jam kerja per minggu: "))
def hitung_keuangan(gaji_per_jam, jam_per_minggu):
    minggu_kerja = 5
    
    pendapatan_sebelum_pajak = gaji_per_jam * jam_per_minggu * minggu_kerja
    pajak = 0.14 * pendapatan_sebelum_pajak
    pendapatan_setelah_pajak = pendapatan_sebelum_pajak - pajak

    biaya_baju_aksesoris = 0.10 * pendapatan_setelah_pajak
    biaya_alat_tulis = 0.01 * pendapatan_setelah_pajak
    sisa_uang = pendapatan_setelah_pajak - (biaya_baju_aksesoris + biaya_alat_tulis)
    sedekah = 0.25 * sisa_uang
    anak_yatim = 0.30 * sedekah
    kaum_dhuafa = 0.70 * sedekah
    
    print("Pendapatan sebelum pajak: Rp",round(pendapatan_sebelum_pajak,2))
    print("Pendapatan setelah pajak: Rp", round(pendapatan_setelah_pajak,2))
    print("Pengeluaran untuk baju dan aksesoris: Rp",round(biaya_baju_aksesoris,2))
    print("Pengeluaran untuk alat tulis: Rp",round(biaya_alat_tulis,2))
    print("Jumlah uang yang disedekahkan: Rp",round(sedekah,2))
    print("Jumlah uang untuk anak yatim: Rp",round(anak_yatim,2))
    print("Jumlah uang untuk kaum dhuafa: Rp",round(kaum_dhuafa,2))

hitung_keuangan(gaji_per_jam, jam_per_minggu)
