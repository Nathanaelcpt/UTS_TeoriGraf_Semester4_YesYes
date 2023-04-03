# Mentukan bagaimana cara menemukan hasil dari jadwal UTS menggunakan Python
# Program ini untuk Jadwal UTS Semester 4

# daftar jadwal UTS
jadwal = {
    'Senin, 03 April 2023': ['Sistem Multimedia'],
    'Selasa, 04 April 2023': ['Pemrograman Basis Data', 'Teori Graf'],
    'Rabu, 05 April 2023': ['Dinamika Kelompok', 'Grafika Komputer dan Pengolahan Citra'],
    'Senin, 10 April 2023': ['Pemrograman Web'],
    'Selasa, 11 April 2023': ['Metode Numerik']
}

# fungsi untuk mencari jadwal UTS berdasarkan tanggal
def cari_jadwal(tanggal):
    if tanggal in jadwal:
        print("Jadwal UTS pada tanggal", tanggal)
        for matkul in jadwal[tanggal]:
            print("- " + matkul)
    else:
        print("Maaf, jadwal UTS pada tanggal", tanggal, "tidak tersedia")

# contoh penggunaan fungsi cari_jadwal
cari_jadwal('Selasa, 04 April 2023')
cari_jadwal('Sabtu, 08 April 2023')
