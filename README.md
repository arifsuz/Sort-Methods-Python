# TUGAS BESAR 2 STRUKTUR DATA | MEMBANDINGKAN METODE SORT

## Penjelasan Kode Bubble Sort Visualized : `TB2_BubbleSort.py`

### Import Modul
- `import random`: Mengimpor modul `random` untuk menghasilkan data acak.
- `import matplotlib.pyplot as plt`: Mengimpor `pyplot` dari `matplotlib` untuk visualisasi data.
- `import matplotlib.animation as animation`: Mengimpor `animation` dari `matplotlib` untuk membuat animasi visualisasi.
- `import easygui`: Mengimpor `easygui` untuk membuat GUI sederhana yang memungkinkan pengguna memasukkan data.
- `import time`: Mengimpor modul `time` untuk mengukur waktu eksekusi.

### Fungsi Bubble Sort Visualized
- Mendefinisikan fungsi `bubble_sort_visualized(arr)` yang menerima array `arr` sebagai parameter:
  - `n = len(arr)`: Mendapatkan panjang array.
  - `steps = []`: Inisialisasi list untuk menyimpan langkah-langkah sorting.
  - Looping luar `for i in range(n)`: Mengakses setiap elemen array.
  - Looping dalam `for j in range(0, n-i-1)`: Membandingkan elemen array.
  - `if arr[j] > arr[j+1]`: Jika elemen saat ini lebih besar dari elemen berikutnya, tukar elemen tersebut.
  - `steps.append(arr.copy())`: Menambahkan salinan array saat ini ke dalam `steps`.
  - `return steps`: Mengembalikan langkah-langkah sorting.

### Fungsi Update Fig
- Mendefinisikan fungsi `update_fig(arr, rects, texts, start_time)` untuk memperbarui visualisasi pada setiap frame:
  - `elapsed_time = time.time() - start_time`: Menghitung waktu yang telah berlalu.
  - Looping untuk memperbarui tinggi dan teks dari setiap batang pada grafik.
  - `ax.set_title(...)`: Memperbarui judul grafik dengan waktu yang telah berlalu.

### Interaksi Pengguna dan Pembuatan Array Acak
- `num_indices = int(easygui.enterbox(...))`: Meminta pengguna memasukkan jumlah indeks.
- `value_range = int(easygui.enterbox(...))`: Meminta pengguna memasukkan batasan nilai maksimum.
- `arr = random.sample(range(1, value_range + 1), num_indices)`: Membuat array acak berdasarkan input pengguna.

### Pengukuran Waktu dan Visualisasi
- `start_time = time.time()`: Menyimpan waktu mulai.
- `steps = bubble_sort_visualized(arr)`: Melakukan bubble sort sambil memvisualisasikannya.
- `end_time = time.time()`: Menyimpan waktu selesai.
- `elapsed_time = end_time - start_time`: Menghitung waktu yang dibutuhkan untuk proses sorting.
- `print(...)`: Mencetak waktu yang dibutuhkan.

### Setup Visualisasi
- `plt.style.use('dark_background')`: Mengatur tema visualisasi menjadi dark background.
- `fig, ax = plt.subplots(...)`: Membuat subplot untuk visualisasi.
- `colors = [plt.cm.viridis(i / len(arr)) for i in range(len(arr))]`: Mengatur warna batang.
- `rects = ax.bar(...)`: Membuat batang pada grafik berdasarkan langkah pertama dari sorting.
- `texts = [ax.text(...) for rect in rects]`: Menambahkan teks pada setiap batang.
- `ax.set_xlim(0, len(arr))`, `ax.set_ylim(0, int(1.1 * max(arr)))`: Mengatur batas x dan y pada grafik.

### Animasi dan Tampilan
- `ani = animation.FuncAnimation(...)`: Membuat animasi dengan memperbarui grafik pada setiap frame.
- `plt.show()`: Menampilkan visualisasi.


## Penjelasan Kode Heap Sort Visualized : `TB2_HeepSort.py`

### Import Modul
- `import random`: Mengimpor modul `random` untuk menghasilkan data acak.
- `import matplotlib.pyplot as plt`: Mengimpor `pyplot` dari `matplotlib` untuk visualisasi data.
- `import matplotlib.animation as animation`: Mengimpor `animation` dari `matplotlib` untuk membuat animasi visualisasi.
- `import easygui`: Mengimpor `easygui` untuk membuat GUI sederhana yang memungkinkan pengguna memasukkan data.
- `import time`: Mengimpor modul `time` untuk mengukur waktu eksekusi.

### Fungsi Heapify
- `def heapify(arr, n, i, steps)`: Mendefinisikan fungsi `heapify` untuk mengatur ulang heap.
  - `largest = i`: Menetapkan indeks awal sebagai elemen terbesar.
  - `left = 2 * i + 1`: Menghitung indeks anak kiri dari elemen saat ini.
  - `right = 2 * i + 2`: Menghitung indeks anak kanan dari elemen saat ini.
  - `if left < n and arr[left] > arr[largest]`: Jika anak kiri lebih besar dari elemen terbesar saat ini, perbarui `largest`.
  - `if right < n and arr[right] > arr[largest]`: Jika anak kanan lebih besar dari `largest`, perbarui `largest`.
  - `if largest != i`: Jika `largest` bukan elemen saat ini, tukar dan lakukan rekursi `heapify`.

### Fungsi Heap Sort Visualized
- `def heap_sort_visualized(arr, steps)`: Mendefinisikan fungsi untuk melakukan heap sort dan visualisasi.
  - `n = len(arr)`: Mendapatkan panjang array.
  - Loop untuk membangun heap.
  - Loop untuk mengekstrak elemen satu per satu dari heap.
  - `steps.append(arr.copy())`: Menambahkan salinan array saat ini ke dalam `steps` setelah setiap pertukaran.

### Fungsi Update Fig
- `def update_fig(arr, rects, texts, start_time)`: Mendefinisikan fungsi untuk memperbarui visualisasi pada setiap frame.
  - `elapsed_time = time.time() - start_time`: Menghitung waktu yang telah berlalu.
  - Loop untuk memperbarui tinggi dan teks dari setiap batang pada grafik.
  - `ax.set_title(...)`: Memperbarui judul grafik dengan waktu yang telah berlalu.

### Interaksi Pengguna dan Pembuatan Array Acak
- Meminta pengguna memasukkan jumlah indeks dan batasan nilai maksimum indeks.
- Membuat array acak berdasarkan input pengguna.

### Pengukuran Waktu dan Visualisasi
- Menyimpan waktu mulai dan selesai.
- Menghitung dan mencetak waktu yang dibutuhkan untuk proses sorting.

### Setup Visualisasi
- Mengatur tema visualisasi menjadi dark background.
- Membuat subplot untuk visualisasi.
- Mengatur warna batang.
- Membuat batang pada grafik berdasarkan langkah pertama dari sorting.
- Menambahkan teks pada setiap batang.
- Mengatur batas x dan y pada grafik.

### Animasi dan Tampilan
- Membuat animasi dengan memperbarui grafik pada setiap frame.
- Menampilkan visualisasi.


## Penjelasan Kode Insertion Sort Visualized : `TB2_InsertionSort.py`

### Import Modul
- `import random`: Mengimpor modul `random` untuk menghasilkan data acak.
- `import matplotlib.pyplot as plt`: Mengimpor `pyplot` dari `matplotlib` untuk visualisasi data.
- `import matplotlib.animation as animation`: Mengimpor `animation` dari `matplotlib` untuk membuat animasi visualisasi.
- `import easygui`: Mengimpor `easygui` untuk membuat GUI sederhana yang memungkinkan pengguna memasukkan data.
- `import time`: Mengimpor modul `time` untuk mengukur waktu eksekusi.

### Fungsi Insertion Sort Visualized
- Mendefinisikan fungsi `insertion_sort_visualized(arr)` yang menerima array `arr` sebagai parameter:
  - `n = len(arr)`: Mendapatkan panjang array.
  - `steps = []`: Inisialisasi list untuk menyimpan langkah-langkah sorting.
  - Looping `for i in range(1, n)`: Mengakses setiap elemen array mulai dari elemen kedua.
  - `key = arr[i]`: Menyimpan elemen saat ini sebagai kunci.
  - `j = i - 1`: Inisialisasi variabel `j` untuk membandingkan elemen sebelumnya.
  - Looping `while j >= 0 and key < arr[j]`: Memindahkan elemen yang lebih besar dari kunci satu posisi ke depan dari posisi saat ini.
  - `arr[j + 1] = key`: Menempatkan kunci pada posisi yang benar.
  - `steps.append(arr.copy())`: Menambahkan salinan array saat ini ke dalam `steps`.
  - `return steps`: Mengembalikan langkah-langkah sorting.

### Fungsi Update Fig
- Mendefinisikan fungsi `update_fig(arr, rects, texts, start_time)` untuk memperbarui visualisasi pada setiap frame:
  - `elapsed_time = time.time() - start_time`: Menghitung waktu yang telah berlalu.
  - Looping untuk memperbarui tinggi dan teks dari setiap batang pada grafik.
  - `ax.set_title(...)`: Memperbarui judul grafik dengan waktu yang telah berlalu.

### Interaksi Pengguna dan Pembuatan Array Acak
- `num_indices = int(easygui.enterbox(...))`: Meminta pengguna memasukkan jumlah indeks.
- `value_range = int(easygui.enterbox(...))`: Meminta pengguna memasukkan batasan nilai maksimum.
- `arr = random.sample(range(1, value_range + 1), num_indices)`: Membuat array acak berdasarkan input pengguna.

### Pengukuran Waktu dan Visualisasi
- `start_time = time.time()`: Menyimpan waktu mulai.
- `steps = insertion_sort_visualized(arr)`: Melakukan insertion sort sambil memvisualisasikannya.
- `end_time = time.time()`: Menyimpan waktu selesai.
- `elapsed_time = end_time - start_time`: Menghitung waktu yang dibutuhkan untuk proses sorting.
- `print(...)`: Mencetak waktu yang dibutuhkan.

### Setup Visualisasi
- `plt.style.use('dark_background')`: Mengatur tema visualisasi menjadi dark background.
- `fig, ax = plt.subplots(...)`: Membuat subplot untuk visualisasi.
- `colors = [plt.cm.viridis(i / len(arr)) for i in range(len(arr))]`: Mengatur warna batang.
- `rects = ax.bar(...)`: Membuat batang pada grafik berdasarkan langkah pertama dari sorting.
- `texts = [ax.text(...) for rect in rects]`: Menambahkan teks pada setiap batang.
- `ax.set_xlim(0, len(arr))`, `ax.set_ylim(0, int(1.1 * max(arr)))`: Mengatur batas x dan y pada grafik.

### Animasi dan Tampilan
- `ani = animation.FuncAnimation(...)`: Membuat animasi dengan memperbarui grafik pada setiap frame.
- `plt.show()`: Menampilkan visualisasi.


## Penjelasan Kode Merge Sort Visualized : `TB2_MergeSort.py`

### Import Modul
- `import random`: Mengimpor modul `random` untuk menghasilkan data acak.
- `import matplotlib.pyplot as plt`: Mengimpor `pyplot` dari `matplotlib` untuk visualisasi data.
- `import matplotlib.animation as animation`: Mengimpor `animation` dari `matplotlib` untuk membuat animasi visualisasi.
- `import easygui`: Mengimpor `easygui` untuk membuat GUI sederhana yang memungkinkan pengguna memasukkan data.
- `import time`: Mengimpor modul `time` untuk mengukur waktu eksekusi.

### Fungsi Merge Sort Visualized
- `def merge_sort_visualized(arr, steps, left=0, right=None)`: Mendefinisikan fungsi untuk melakukan merge sort dan visualisasi.
  - `if right is None`: Jika `right` belum ditentukan, set ke panjang array.
  - `if right - left > 1`: Jika sub-array memiliki lebih dari satu elemen, lanjutkan pembagian.
  - `mid = (left + right) // 2`: Tentukan titik tengah.
  - Rekursif memanggil `merge_sort_visualized` untuk sub-array kiri dan kanan.
  - Memanggil fungsi `merge` untuk menggabungkan sub-array.

### Fungsi Merge
- `def merge(arr, steps, left, mid, right)`: Mendefinisikan fungsi untuk menggabungkan dua sub-array.
  - `L = arr[left:mid]` dan `R = arr[mid:right]`: Membagi array menjadi dua bagian.
  - `i = j = 0` dan `k = left`: Inisialisasi indeks untuk sub-array kiri, kanan, dan array gabungan.
  - Looping untuk membandingkan dan menggabungkan elemen dari kedua sub-array.
  - Menambahkan elemen yang tersisa dari sub-array kiri atau kanan jika ada.
  - `steps.append(arr.copy())`: Menambahkan salinan array saat ini ke dalam `steps` setelah setiap penambahan elemen.

### Fungsi Update Fig
- `def update_fig(arr, rects, texts, start_time)`: Mendefinisikan fungsi untuk memperbarui visualisasi pada setiap frame.
  - Menghitung waktu yang telah berlalu dan memperbarui judul grafik.
  - Looping untuk memperbarui tinggi dan teks dari setiap batang pada grafik.

### Interaksi Pengguna dan Pembuatan Array Acak
- Meminta pengguna memasukkan jumlah indeks dan batasan nilai maksimum indeks.
- Membuat array acak berdasarkan input pengguna.

### Pengukuran Waktu dan Visualisasi
- Menyimpan waktu mulai dan selesai.
- Menghitung dan mencetak waktu yang dibutuhkan untuk proses sorting.

### Setup Visualisasi
- Mengatur tema visualisasi menjadi dark background.
- Membuat subplot untuk visualisasi.
- Mengatur warna batang.
- Membuat batang pada grafik berdasarkan langkah pertama dari sorting.
- Menambahkan teks pada setiap batang.
- Mengatur batas x dan y pada grafik.

### Animasi dan Tampilan#
- Membuat animasi dengan memperbarui grafik pada setiap frame.
- Menampilkan visualisasi.


## Penjelasan Kode Quick Sort Visualized : `TB2_QuickSort.py`

### Import Modul
- `import random`: Mengimpor modul `random` untuk menghasilkan data acak.
- `import matplotlib.pyplot as plt`: Mengimpor `pyplot` dari `matplotlib` untuk visualisasi data.
- `import matplotlib.animation as animation`: Mengimpor `animation` dari `matplotlib` untuk membuat animasi visualisasi.
- `import easygui`: Mengimpor `easygui` untuk membuat GUI sederhana yang memungkinkan pengguna memasukkan data.
- `import time`: Mengimpor modul `time` untuk mengukur waktu eksekusi.

### Fungsi Quick Sort Visualized
- `def quick_sort_visualized(arr, low, high, steps)`: Mendefinisikan fungsi untuk melakukan quick sort dan visualisasi.
  - `if low < high`: Jika indeks rendah lebih kecil dari indeks tinggi, lanjutkan proses.
  - `pi = partition(arr, low, high, steps)`: Memanggil fungsi `partition` untuk mendapatkan indeks pivot.
  - Rekursif memanggil `quick_sort_visualized` untuk sub-array kiri dan kanan dari pivot.

### Fungsi Partition
- `def partition(arr, low, high, steps)`: Mendefinisikan fungsi untuk mempartisi array.
  - `pivot = arr[high]`: Menetapkan elemen terakhir sebagai pivot.
  - `i = low - 1`: Inisialisasi indeks elemen lebih kecil.
  - Loop untuk membandingkan setiap elemen dengan pivot dan melakukan pertukaran jika perlu.
  - Pertukaran elemen pivot ke posisi yang benar.
  - `steps.append(arr.copy())`: Menambahkan salinan array saat ini ke dalam `steps` setelah setiap pertukaran.
  - Mengembalikan indeks pivot.

### Fungsi Update Fig
- `def update_fig(arr, rects, texts, start_time)`: Mendefinisikan fungsi untuk memperbarui visualisasi pada setiap frame.
  - Menghitung waktu yang telah berlalu dan memperbarui judul grafik.
  - Loop untuk memperbarui tinggi dan teks dari setiap batang pada grafik.

### Interaksi Pengguna dan Pembuatan Array Acak
- Meminta pengguna memasukkan jumlah indeks dan batasan nilai maksimum indeks.
- Membuat array acak berdasarkan input pengguna.

### Pengukuran Waktu dan Visualisasi
- Menyimpan waktu mulai dan selesai.
- Menghitung dan mencetak waktu yang dibutuhkan untuk proses sorting.

### Setup Visualisasi
- Mengatur tema visualisasi menjadi dark background.
- Membuat subplot untuk visualisasi.
- Mengatur warna batang.
- Membuat batang pada grafik berdasarkan langkah pertama dari sorting.
- Menambahkan teks pada setiap batang.
- Mengatur batas x dan y pada grafik.

### Animasi dan Tampilan
- Membuat animasi dengan memperbarui grafik pada setiap frame.
- Menampilkan visualisasi.


## Penjelasan Kode Visualisasi Selection Sort : `TB2_SelectionSort.py`

### Import Modul
- `import random`: Mengimpor modul `random` untuk menghasilkan data acak.
- `import matplotlib.pyplot as plt`: Mengimpor `pyplot` dari `matplotlib` untuk visualisasi data.
- `import matplotlib.animation as animation`: Mengimpor `animation` dari `matplotlib` untuk membuat animasi visualisasi.
- `import easygui`: Mengimpor `easygui` untuk membuat GUI sederhana yang memungkinkan pengguna memasukkan data.
- `import time`: Mengimpor modul `time` untuk mengukur waktu eksekusi.

### Fungsi Selection Sort Visualized
- `def selection_sort_visualized(arr)`: Mendefinisikan fungsi untuk melakukan selection sort dan visualisasi.
  - `n = len(arr)`: Menentukan panjang array.
  - `steps = []`: Inisialisasi list untuk menyimpan langkah-langkah visualisasi.
  - Loop untuk setiap elemen di array.
    - `min_idx = i`: Menetapkan indeks minimum saat ini.
    - Loop kedua untuk mencari elemen terkecil di sisa array.
      - Jika elemen lebih kecil ditemukan, perbarui `min_idx`.
    - Tukar elemen saat ini dengan elemen terkecil yang ditemukan.
    - `steps.append(arr.copy())`: Menambahkan salinan array saat ini ke dalam `steps`.
  - Mengembalikan `steps` yang berisi langkah-langkah visualisasi.

### Fungsi Update Fig
- `def update_fig(arr, rects, texts, start_time)`: Mendefinisikan fungsi untuk memperbarui visualisasi pada setiap frame.
  - `elapsed_time = time.time() - start_time`: Menghitung waktu yang telah berlalu.
  - Loop untuk memperbarui tinggi dan teks dari setiap batang pada grafik.
  - `ax.set_title(...)`: Memperbarui judul grafik dengan waktu yang telah berlalu.

### Interaksi Pengguna dan Pembuatan Array Acak
- `num_indices = int(easygui.enterbox(...))`: Meminta pengguna memasukkan jumlah indeks.
- `value_range = int(easygui.enterbox(...))`: Meminta pengguna memasukkan batasan nilai maksimum indeks.
- `arr = random.sample(range(1, value_range + 1), num_indices)`: Membuat array acak berdasarkan input pengguna.

### Pengukuran Waktu dan Visualisasi
- `start_time = time.time()`: Menyimpan waktu mulai.
- `steps = selection_sort_visualized(arr)`: Melakukan selection sort dan menyimpan langkah-langkah visualisasi.
- `end_time = time.time()`: Menyimpan waktu selesai.
- `elapsed_time = end_time - start_time`: Menghitung waktu yang dibutuhkan untuk proses sorting.
- `print(...)`: Mencetak waktu yang dibutuhkan untuk proses sorting.

### Setup Visualisasi
- `plt.style.use('dark_background')`: Mengatur tema visualisasi menjadi dark background.
- `fig, ax = plt.subplots(...)`: Membuat subplot untuk visualisasi.
- `colors = [...]`: Mengatur warna batang berdasarkan panjang array.
- `rects = ax.bar(...)`: Membuat batang pada grafik berdasarkan langkah pertama dari sorting.
- `texts = [...]`: Menambahkan teks pada setiap batang.
- `ax.set_xlim(0, len(arr))` dan `ax.set_ylim(0, int(1.1 * max(arr)))`: Mengatur batas x dan y pada grafik.

### Animasi dan Tampilan
- `ani = animation.FuncAnimation(...)`: Membuat animasi dengan memperbarui grafik pada setiap frame.
- `plt.show()`: Menampilkan visualisasi.
