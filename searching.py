def linear_search(numbers, target): # Mencari satu per satu dari awal sampai ketemu
                                    # menggunakan O(n) Linear = semakin banyak data, semkain banyak yang harus dicek
    for i in range(len(numbers)):  # cek setiap indeks dalam daftar numbers

        if numbers [i] == target:  # apakah angka sekarang = angka yang dicari?
            return i               # kalau ketemu, kembalikan index-nya

    return -1  # jika tidak ditemukan, kembalikan -1 (-1 = target tidak ditemukan)

numbers = [5, 2, 4, 1, 3]
result = linear_search(numbers, 4)
print(result)  # Output: 2 (indeks dari angka 4 dalam daftar)

def binary_search(numbers, target): # Mencari dengan membagi dua (harus diurutkan dulu) / "Potong pencarian menjadi setengah terus-menerus"
                                    # Syarat Penting : Data harus sudah terurut  # Menggunakan O(log n) Binary = semakin banyak data, semakin sedikit yang harus dicek
    left = 0 # indeks awal dari daftar numbers
    right = len(numbers) - 1 # indeks akhir dari daftar numbers

    while left <= right:

        middle = (left + right) // 2  # cari indeks tengah dari daftar numbers

        if numbers[middle] == target:
            return middle  # jika ketemu, kembalikan index-nya 

        elif numbers[middle] < target:
            left = middle + 1  # jika angka di tengah < target, maka target pasti ada di sebelah kanan (kiri diabaikan)

        else:
            right = middle - 1  # jika angka di tengah > target, maka target pasti ada di sebelah kiri (kanan diabaikan)

    return -1  # jika tidak ditemukan, kembalikan -1 (-1 = target tidak ditemukan)

numbers = [1, 3, 5, 7, 9, 11, 13, 15]
result = binary_search(numbers, 7)
print(result)  # Output: 3 (indeks dari angka 7 dalam daftar)
# Binary Search lebih efisien daripada Linear Search karena mengurangi jumlah elemen yang harus diperiksa dengan membagi daftar menjadi dua bagian setiap kali.
# Practicing Git branch 