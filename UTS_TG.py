import numpy as np

# fungsi untuk menghitung matriks konflik
def calculate_conflict_matrix(schedule):
    n = len(schedule)
    conflict_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            if schedule[i][0] == schedule[j][0]:
                conflict_matrix[i][j] = 1
                conflict_matrix[j][i] = 1
            elif schedule[i][1] == schedule[j][1]:
                conflict_matrix[i][j] = 1
                conflict_matrix[j][i] = 1
    return conflict_matrix

# fungsi untuk mengimplementasikan algoritma Welch-Powell
def welch_powell(schedule):
    # Hitung matriks konflik
    conflict_matrix = calculate_conflict_matrix(schedule)
    # Menginisialisasi daftar warna
    colors = [-1] * len(schedule)
    # Menetapkan warna ke simpul
    for i in range(len(schedule)):
        # Temukan warna pertama yang tersedia
        available_colors = list(range(len(schedule)))
        for j in range(len(schedule)):
            if conflict_matrix[i][j] == 1 and colors[j] != -1:
                if colors[j] in available_colors:
                    available_colors.remove(colors[j])
        color = available_colors[0]
        colors[i] = color
    # Urutkan simpul berdasarkan warna
    sorted_vertices = [x for _, x in sorted(zip(colors, schedule))]
    # Kembalikan jadwal yang telah diurutkan
    return sorted_vertices

# Inisialisasi daftar jadwal
schedule = []

# Minta masukan dari pengguna
while True:
    course = input("Masukkan nama mata kuliah (Ketik 'Tampilkan' untuk Menampilkan Hasil): ")
    if course == "Tampilkan":
        break
    day = input ("Masukkan hari ujian (Senin - Jumat): ")
    date= input ("Masukan Tanggal: ")
    month= input("Masukan Bulan  : ")
    year= input ("Masukan Tahun  : ")
    time = input("Masukkan waktu ujian (08.00 - 17.00): ")
    schedule.append((course, day, date, month, year, time))    
    
# Terapkan algoritma Welch-Powell
sorted_schedule = welch_powell(schedule)

# Cetak jadwal ujian optimal
print ("Jadwal ujian yang optimal adalah : ")
for course, day, date, month, year, time in sorted_schedule:
    print(" Mata Kuliah : " + course )
    print(" Hari  : "  +  day + " " + date  + " " + month + " " + year  )
    print(" Waktu : " + time)
