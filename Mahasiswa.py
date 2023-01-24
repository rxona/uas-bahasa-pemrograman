import json
import jsonpickle

class Matkul:
    def __init__(self):
        self.id = None
        self.nama = None
        self.jumlahSKS = None

class Mahasiswa:
    def __init__(self):
        self.nim = None
        self.nama = None
        self.jk = None
        self.tempatLahir = None
        self.tglLahir = None
        self.fakultas = None
        self.jurusan = None
        self.matkul = []

listMhs = []

jumlahMhs = input('Masukkan jumlah mahasiswa: ')

for i in range(int(jumlahMhs)):
    iS = str(i + 1)
    mhs = Mahasiswa()
    mhs.nim = input('NIM MHS ' + iS + ': ')
    mhs.nama = input('Nama MHS ' + iS + ': ')
    mhs.jk = input('JK MHS ' + iS + ': ')
    mhs.tempatLahir = input('Tempat Lahir MHS ' + iS + ': ')
    mhs.tglLahir = input('Tanggal Lahir MHS ' + iS + ': ')
    mhs.fakultas = input('Fakultas MHS ' + iS + ': ')
    mhs.jurusan = input('Jurusan MHS ' + iS + ': ')
    jmlhMatkul = input('Jumlah Matkul MHS ' + iS + ': ')
    for m in range(int(jmlhMatkul)):
        iM = str(m + 1)
        matkul = Matkul()
        matkul.id = input('ID MK ' + iM +  ' MHS ' + iS + ': ')
        matkul.nama = input('Nama MK ' + iM +  ' MHS ' + iS + ': ')
        matkul.jumlahSKS = input('Jumlah SKS MK ' + iM +  ' MHS ' + iS + ': ')
        mhs.matkul.append(matkul)
    listMhs.append(mhs)

parsed = json.loads(jsonpickle.encode(listMhs))
print(json.dumps(parsed, indent=4))

