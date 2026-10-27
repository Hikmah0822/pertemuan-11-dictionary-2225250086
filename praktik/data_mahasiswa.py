def cari_mahasiswa(data, nim):
    return data.get(nim, "Data tidak ditemukan")


def rata_rata_nilai(data):
    total = sum(m["nilai"] for m in data.values())
    return total / len(data)


data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

# TEST CASE 1: Pencarian NIM tersedia
print("TEST CASE 1: Pencarian A003")
hasil = cari_mahasiswa(data_mahasiswa, "A003")
print(hasil)
print("Status:", "BERHASIL" if hasil["nama"] == "Citra" else "GAGAL")

# TEST CASE 2: Pencarian NIM tidak tersedia
print("\nTEST CASE 2: Pencarian A999")
hasil = cari_mahasiswa(data_mahasiswa, "A999")
print(hasil)
print("Status:", "BERHASIL" if hasil == "Data tidak ditemukan" else "GAGAL")

# TEST CASE 3: Pembaruan nilai A002 menjadi 82
print("\nTEST CASE 3: Pembaruan nilai A002")
data_mahasiswa["A002"]["nilai"] = 82
print("Nilai Budi:", data_mahasiswa["A002"]["nilai"])
print("Status:", "BERHASIL" if data_mahasiswa["A002"]["nilai"] == 82 else "GAGAL")

# TEST CASE 4: Penambahan mahasiswa A006
print("\nTEST CASE 4: Penambahan A006")
data_mahasiswa["A006"] = {
    "nama": "Fani",
    "kelas": "B",
    "nilai": 80
}
print(data_mahasiswa.get("A006", "Data tidak ditemukan"))
print("Status:", "BERHASIL" if "A006" in data_mahasiswa else "GAGAL")

# TEST CASE 5: Rekap seluruh mahasiswa menggunakan items()
print("\nTEST CASE 5: Rekap data mahasiswa")
for nim, data in data_mahasiswa.items():
    print(f"{nim}: {data}")

print("Status:", "BERHASIL" if len(data_mahasiswa) == 6 else "GAGAL")

# Rata-rata nilai seluruh mahasiswa
print("\nRATA-RATA NILAI MAHASISWA")
print(f"{rata_rata_nilai(data_mahasiswa):.2f}")