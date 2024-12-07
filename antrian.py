import heapq
queue = []
from datetime import datetime, timedelta

antrian = []  
dokter = {}  
rekam_pasien = {} 

def tambah_dokter(nama, poli):
    if poli not in dokter:
        dokter[poli] = []
    dokter[poli].append({"nama": nama, "status": "tersedia"})
    print(f"Dokter {nama} ditambahkan ke poli {poli}.")

def masukan_pasien(nama, status, poli):
    waktu_kedatangan = datetime.now()
    heapq.heappush(antrian, (-status, waktu_kedatangan, poli, nama))
    print(f"Pasien {nama} ditambahkan ke antrian poli {poli} dengan prioritas {status}.")

def process_patient():
    if not antrian:
        print("Antrian kosong.")
        return
    status, waktu_kedatangan, poli, nama = heapq.heappop(antrian)
    doctor = next((d for d in dokter.get(poli, []) if d["status"] == "tersedia"), None)
    if doctor:
        doctor["status"] = "busy"
        rekam_pasien[nama] = {"waktu_kedatangan": waktu_kedatangan, "poli": poli, "status": "In Treatment"}
        print(f"Pasien {nama} sedang dilayani oleh Dr. {doctor['nama']} di poli {poli}.")
    else:
        print(f"Tidak ada dokter tersedia di poli {poli}. Pasien {nama} tetap dalam antrian.")

def perkiraan_waktu_tunggu(poli):
    pasien_menunggu = [p for p in antrian if p[2] == poli]
    waktu_tunggu = 15  # waktu rata-rata per pasien 15 menit
    return len(pasien_menunggu) * waktu_tunggu

def rekam_status_pasien(nama, status):
    if nama in rekam_pasien:
        rekam_pasien[nama]["status"] = status
        print(f"Status pasien {nama} diperbarui menjadi {status}.")
    else:
        print(f"Pasien {nama} tidak ditemukan.")

def tampilkan_antrian():
    if not antrian:
        print("Antrian kosong.")
        return
    print("Antrian pasien:")
    for status, _, poli, nama in sorted(antrian, key=lambda x: (-x[0], x[1])):
        print(f"- {nama} (Poli: {poli}, Prioritas: {-status})")

def tampilkan_dokter():
    if not dokter:
        print("Belum ada dokter yang terdaftar.")
        return
    print("Daftar dokter:")
    for poli, list_dokter in dokter.items():
        print(f"Poli {poli}:")
        for doc in list_dokter:
            print(f"  - Dr. {doc['nama']} ({doc['status']})")

def main():
    while True:
        print("\n=== Manajemen Antrian Pasien ===")
        print("1. Tambah dokter")
        print("2. Tambah pasien")
        print("3. Proses pasien")
        print("4. Hitung waktu tunggu")
        print("5. Rekam status pasien")
        print("6. Tampilkan antrian")
        print("7. Tampilkan dokter")
        print("8. Keluar")
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            nama = input("Nama dokter: ")
            poli = input("Poli: ")
            tambah_dokter(nama, poli)
        elif pilihan == "2":
            nama = input("Nama pasien: ")
            status = int(input("Tingkat urgensi (1-10): "))
            poli = input("Poli: ")
            masukan_pasien(nama, status, poli)
        elif pilihan == "3":
            process_patient()
        elif pilihan == "4":
            poli = input("Poli: ")
            wait_time = perkiraan_waktu_tunggu(poli)
            print(f"Perkiraan waktu tunggu di poli {poli}: {wait_time} menit.")
        elif pilihan == "5":
            nama = input("Nama pasien: ")
            status = input("Status baru: ")
            rekam_status_pasien(nama, status)
        elif pilihan == "6":
            tampilkan_antrian()
        elif pilihan == "7":
            tampilkan_dokter()
        elif pilihan == "8":
            print("Terima kasih telah menggunakan sistem.")
            break
        else:
            print("Opsi tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
