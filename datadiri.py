print("\n```Data Diri Mahasiswa Kelas 2023D```")

class DataDiri:
    def __init__(self, nama, kelas, nim, jurusan, fakultas, universitas):
        self.nama = nama
        self.kelas = kelas
        self.nim = nim
        self.jurusan = jurusan 
        self.fakultas = fakultas
        self.universitas = universitas

    def start(self):
        print(f"Nama = {self.nama}")
        print(f"Kelas = {self.kelas}")
        print(f"Nim = {self.nim}")
        print(f"Jurusan = {self.jurusan}")
        print(f"Fakultas = {self.fakultas}")
        print(f"Universitas = {self.universitas}")

DataDiri1 = DataDiri("Dwi Wahyu Utami", "2023D", "23091397121", "Manajemen Informatika", "Vokasi", "Universitas Negeri Surabaya.")

DataDiri1.start()
