# Pertemuan 11 - Dictionary/Map

**Nama:** Hikmah Azizah

**NIM:** 2225250086

**Kelas:** 3B

## Tujuan
Memahami penggunaan dictionary dalam Python untuk menyimpan, mencari, mengubah, dan menampilkan data.

## Struktur Data
Program menggunakan NIM sebagai key utama. Setiap value berupa dictionary yang berisi nama, kelas, dan nilai mahasiswa.

## Cara Menjalankan
Jalankan perintah berikut melalui terminal VS Code dari folder utama:

```bash
python praktik/data_mahasiswa.py
```

Jika menggunakan `python3`, jalankan:

```bash
python3 praktik/data_mahasiswa.py
```

## Test Case

| Input/Aksi | Hasil yang Diharapkan | Status |
|---|---|---|
| Cari A003 | Data Citra ditampilkan | Berhasil |
| Cari A999 | Data tidak ditemukan | Berhasil |
| Ubah nilai A002 menjadi 82 | Nilai berubah menjadi 82 | Berhasil |
| Tambahkan A006 | Key A006 tersedia | Berhasil |
| Rekap menggunakan items() | Seluruh data tampil | Berhasil |

## Refleksi
Saya mempelajari bahwa dictionary menyimpan data dalam pasangan key-value. Kesalahan yang dapat terjadi adalah KeyError saat mengakses key yang tidak tersedia. Kesalahan tersebut dapat dihindari menggunakan method get() agar program dapat menangani data yang tidak ditemukan.