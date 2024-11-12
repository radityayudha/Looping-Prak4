jumlah_mahasiswa = int(input("Banyak Mahasiswa : "))
for mhs in range(1, jumlah_mahasiswa + 1):
    print(f"Mahasiswa ke {mhs}")
    jumlah_mata_kuliah = int(input("Banyak Mata Kuliah yang Diambil: "))

    total_nilai = 0
    for matkul in range(1, jumlah_mata_kuliah + 1):
        nilai = float(input(f"\tInput nilai matkul ke {matkul}: "))
        total_nilai += nilai
    
    rata_rata = total_nilai/jumlah_mata_kuliah
    print(f"\tRata-rata: {rata_rata:.2f}")