#### 1. Array

Array adalah tipe data yang digunakan untuk menyimpan sekumpulan nilai. Nilai-nilai ini dapat diakses dengan menggunakan indeks, yang dimulai dari 0.
Array pada JavaScript:
Mendefinisikan array pada JavaScript, dapat menggunakan tanda kurung siku [] dan menempatkan elemen-elemen yang diinginkan di dalamnya, dipisahkan oleh koma.

- **Inisialisasi**
  Menginisialisasi array kosong
  `let kota = []`

- **Assign Data**
  `kota = ['Bekasi', 'Jakarta', 'Bogor']`
- **Retrieve data**
  Mengakses elemen array menggunakan indeks dalam tanda kurung siku. Contoh mencetak nilai elemen ke-1 dari array, yaitu Jakarta:
  `console.log(kota[1])`

- **Penyisipan data**
  Menggunakan spread operator (...) untuk menambahkan elemen baru ke posisi tertentu dalam array. Contoh:

```javascript
const kotaDiSumatera = ["Padang", "Medan"];
kota = [...kota, ...kotaDiSumatera]; // ['Bekasi', 'Jakarta', 'Bogor', 'Padang', 'Medan']
```

- **Pencarian Data**
  Menggunakan metode `indexOf()` untuk mencari data dan mengembalikan index dari data yang dicari. Contoh:

```javascript
let indexBekasi = myArray.indexOf("Bogor");
console.log(indexBekasi); // 2
```

- **Penambahan index dan data**
  Menggunakan metode `push()` untuk menambahkan elemen baru di akhir array. Contohnya:

```javascript
kota.push("Semarang"); // kota sekarang adalah ['Bekasi', 'Jakarta', 'Bogor', 'Padang', 'Medan', 'Semarang']
```

Untuk menambahkan elemen baru di awal array dapat menggunakan metode `unshift()`. Contoh:

```javascript
kota.unshift("Tanggerang"); // kota sekarang adalah ['Tanggerang', 'Bekasi', 'Jakarta', 'Bogor', 'Padang', 'Medan', 'Semarang']
```

#### 2. Pointer

Pointer adalah variabel yang menyimpan alamat suatu objek dalam memori komputer. Objek ini bisa berupa variabel, array, atau struktur data lainnya. Pointer memungkinkan kita untuk mengakses dan mengubah nilai dari objek tersebut dengan menggunakan alamat memori yang disimpan di dalam pointer.

Untuk mendeklarasikan variabel pointer kita menggunakan tanda asterik / bintang (\*) didepan variabel yang di deklarasikan pada tipe datanya. Contoh:

```cpp
int *pointerk;     // Deklarasi pointer dengan tipe data integer
```

Pointer digunakan dalam berbagai situasi, beberapa diantaranya :

1. Akses dan modifikasi data yang ada di alamat memori tertentu, seperti array, struct, atau variabel yang dideklarasikan di luar fungsi.
2. Pemanggilan fungsi dengan passing parameter berupa pointer, sehingga memungkinkan fungsi untuk mengubah nilai dari variabel yang ada di luar fungsi.
3. Pembuatan dynamic memory allocation, yaitu alokasi memori pada saat runtime.
4. Dalam pemrograman berorientasi objek, pointer digunakan untuk mengakses method dan atribut dari suatu objek.
5. Dalam sistem operasi, pointer digunakan untuk mengakses data dalam kernel atau device driver.
6. Pointer juga digunakan dalam pemrograman paralel untuk mengakses data yang digunakan oleh beberapa thread atau proses.

#### 3. Function

Function adalah sebuah blok kode yang dapat digunakan kembali dalam program. Dengan menggunakan function, kode dapat diorganisir dengan baik dan dapat digunakan kembali tanpa perlu menulis ulang kode yang sama.

Kapan menggunakan function?
Function digunakan ketika ada bagian dari program yang perlu digunakan kembali dalam program, seperti tugas yang sama yang dilakukan dalam beberapa bagian dari program atau kode yang digunakan dalam beberapa file atau modul.

Contoh function yang mengembalikan nilai dalam JavaScript:

```javascript
function tambah(a, b) {
  return a + b;
}

const hasil = tambah(3, 4);
console.log(hasil); // akan menampilkan 7
```

Contoh function yang tidak mengembalikan nilai:

```javascript
function sapa(nama) {
  console.log(`Halo, ${nama}!`);
}

sapa("Andre"); // akan menampilkan "Halo, Andre!" pada console
```

### Class Mahasiswa

```python
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


```
