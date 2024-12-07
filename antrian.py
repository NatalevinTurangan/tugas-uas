import heapq
from datetime import datetime, timedelta

queue = []  
doctors = {}  
patient_records = {} 

def add_doctor(name, poli):
    if poli not in doctors:
        doctors[poli] = []
    doctors[poli].append({"name": name, "status": "available"})
    print(f"Dokter {name} ditambahkan ke poli {poli}.")

def add_patient(name, urgency, poli):
    arrival_time = datetime.now()
    heapq.heappush(queue, (-urgency, arrival_time, poli, name))
    print(f"Pasien {name} ditambahkan ke antrian poli {poli} dengan prioritas {urgency}.")

def process_patient():
    if not queue:
        print("Antrian kosong.")
        return
    urgency, arrival_time, poli, name = heapq.heappop(queue)
    doctor = next((d for d in doctors.get(poli, []) if d["status"] == "available"), None)
    if doctor:
        doctor["status"] = "busy"
        patient_records[name] = {"arrival_time": arrival_time, "poli": poli, "status": "In Treatment"}
        print(f"Pasien {name} sedang dilayani oleh Dr. {doctor['name']} di poli {poli}.")
    else:
        print(f"Tidak ada dokter tersedia di poli {poli}. Pasien {name} tetap dalam antrian.")

def calculate_wait_time(poli):
    waiting_patients = [p for p in queue if p[2] == poli]
    avg_time = 15  # waktu rata-rata per pasien 15 menit
    return len(waiting_patients) * avg_time

def update_patient_status(name, status):
    if name in patient_records:
        patient_records[name]["status"] = status
        print(f"Status pasien {name} diperbarui menjadi {status}.")
    else:
        print(f"Pasien {name} tidak ditemukan.")

def show_queue():
    if not queue:
        print("Antrian kosong.")
        return
    print("Antrian pasien:")
    for urgency, _, poli, name in sorted(queue, key=lambda x: (-x[0], x[1])):
        print(f"- {name} (Poli: {poli}, Prioritas: {-urgency})")

def show_doctors():
    if not doctors:
        print("Belum ada dokter yang terdaftar.")
        return
    print("Daftar dokter:")
    for poli, doc_list in doctors.items():
        print(f"Poli {poli}:")
        for doc in doc_list:
            print(f"  - Dr. {doc['name']} ({doc['status']})")

def main():
    while True:
        print("\n=== Sistem Manajemen Antrian Pasien ===")
        print("1. Tambah dokter")
        print("2. Tambah pasien")
        print("3. Proses pasien")
        print("4. Hitung waktu tunggu")
        print("5. Rekam status pasien")
        print("6. Tampilkan antrian")
        print("7. Tampilkan dokter")
        print("8. Keluar")
        choice = input("Pilih opsi: ")

        if choice == "1":
            name = input("Nama dokter: ")
            poli = input("Poli: ")
            add_doctor(name, poli)
        elif choice == "2":
            name = input("Nama pasien: ")
            urgency = int(input("Tingkat urgensi (1-10): "))
            poli = input("Poli: ")
            add_patient(name, urgency, poli)
        elif choice == "3":
            process_patient()
        elif choice == "4":
            poli = input("Poli: ")
            wait_time = calculate_wait_time(poli)
            print(f"Perkiraan waktu tunggu di poli {poli}: {wait_time} menit.")
        elif choice == "5":
            name = input("Nama pasien: ")
            status = input("Status baru: ")
            update_patient_status(name, status)
        elif choice == "6":
            show_queue()
        elif choice == "7":
            show_doctors()
        elif choice == "8":
            print("Terima kasih telah menggunakan sistem.")
            break
        else:
            print("Opsi tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
