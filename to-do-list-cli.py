import json
import os

FILE = "tugas.json"

def load_tugas():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def simpan_tugas(tugas):
    with open(FILE, "w") as f:
        json.dump(tugas, f, indent=4)

def tambah_tugas(tugas):
    nama = input("Masukkan tugas baru: ")
    tugas.append({"nama": nama, "selesai": False})
    simpan_tugas(tugas)
    print("✅ Tugas ditambahkan!")

def lihat_tugas(tugas):
    if not tugas:
        print("Belum ada tugas nih")
        return
    for i, t in enumerate(tugas, 1):
        status = "✔️" if t["selesai"] else "❌"
        print(f"{i}. {status} {t['nama']}")

def tandai_selesai(tugas):
    lihat_tugas(tugas)
    try:
        no = int(input("Nomor tugas yang selesai: "))
        tugas[no-1]["selesai"] = True
        simpan_tugas(tugas)
        print("🎉 Selamat! Tugas selesai")
    except:
        print("Nomor tidak valid")

def main():
    tugas = load_tugas()
    while True:
        print("\n--- TO DO LIST ---")
        print("1. Lihat Tugas")
        print("2. Tambah Tugas")
        print("3. Tandai Selesai")
        print("4. Keluar")
        pilih = input("Pilih: ")
        
        if pilih == "1": lihat_tugas(tugas)
        elif pilih == "2": tambah_tugas(tugas)
        elif pilih == "3": tandai_selesai(tugas)
        elif pilih == "4": break
        else: print("Pilihan salah")

if __name__ == "__main__":
    main()