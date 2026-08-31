def bubble_sort(numbers):  # "Dorong yang terbesar ke belakang" - algoritma pengurutan gelembung

    n = len(numbers)

    for i in range(n):  # menunjukkan berapa kali kita akan melakukan putaran

        swapped = False  # menandai apakah kita telah melakukan pertukaran

        for j in range(0, n - i - 1):  # membandingkan elemen yang bersebelahan

            if numbers[j] > numbers[j + 1]:  # jika elemen saat ini (kiri) lebih besar dari elemen berikutnya (kanan), maka kita menukarnya

                numbers[j], numbers [j + 1] = (
                    numbers[j + 1],
                    numbers[j]
                )

                swapped = True  # menandai bahwa kita telah melakukan pertukaran

        if not swapped: # jika tidak ada pertukaran yang terjadi, maka daftar sudah diurutkan
            break

    return numbers

def selection_sort(numbers):  # "Pilih yang terkecil, lalu taruh di depan" - algoritma pengurutan seleksi

    n = len(numbers)

    for i in range(n):

        min_index = i  # menganggap elemen pertama (saat ini) adalah elemen terkecil

        for j in range(i + 1, n):

            if numbers[j] < numbers[min_index]:  # kalau ternyata menemukan yang lebih kecil, maka kita memperbarui indeks elemen terkecil
                min_index = j  # simpan posisi elemen terkecil yang baru ditemukan

        numbers[i], numbers[min_index] = (  # tukar elemen terkecil ke posisi depan (saat ini (i) dengan elemen terkecil yang ditemukan)
            numbers[min_index],
            numbers[i]
        )

    return numbers

def insertion_sort(numbers):  # "Anggap bagian kiri sudah terurut, lalu masukkan elemen berikutnya ke posisi yang tepat" - algoritma pengurutan sisip

    n = len(numbers)

    for i in range(1, len(numbers)):  # mulai dari elemen kedua (indeks 1) karena kita menganggap elemen pertama (indeks 0) sudah terurut

        key = numbers[i]  # ambil angka yang akan disisipkan ke bagian kiri yang sudah terurut
        j = i - 1 # indeks elemen sebelumnya (saat ini) yang akan dibandingkan dengan elemen berikutnya (key)

        while j >= 0 and numbers[j] > key:  # jika elemen sebelumnya lebih besar dari key, maka kita perlu menggeser elemen tersebut ke kanan untuk memberi ruang bagi key

            numbers[j + 1] = numbers[j]  # geser elemen yang lebih besar ke kanan untuk memberi ruang bagi key
            j -= 1  # pindah ke elemen sebelumnya untuk dibandingkan dengan key

        numbers[j + 1] = key  # sisipkan key ke posisi yang tepat di bagian kiri yang sudah terurut

    return numbers

def merge_sort(numbers): # "Bagi dan taklukkan" - algoritma pengurutan gabungan (memecah data)

    if len(numbers) <= 1:  # kalau tinggal 1 elemen, sudah pasti terurut, jadi berhenti memecah data
        return numbers

    mid = len(numbers) // 2  # membagi daftar menjadi dua bagian (kiri dan kanan)

    left = numbers[:mid]  # ambil elemen dari awal hingga tengah (kiri)
    right = numbers[mid:] # ambil elemen dari tengah hingga akhir (kanan)

    left = merge_sort(left)   # memanggil fungsi merge_sort secara rekursif untuk mengurutkan bagian kiri
    right = merge_sort(right) # memanggil fungsi merge_sort secara rekursif untuk mengurutkan bagian kanan

    return merge(left, right)

def merge(left, right): # fungsi untuk menggabungkan dua daftar yang sudah diurutkan (menggabungkan data)

    result = []  # daftar kosong untuk menyimpan hasil penggabungan

    i = 0  # indeks untuk melacak posisi elemen saat ini di daftar kiri
    j = 0  # indeks untuk melacak posisi elemen saat ini di daftar kanan

    while i < len(left) and j < len(right):  # selama masih ada elemen di kedua daftar

        if left[i] < right[j]:  # jika elemen di daftar kiri lebih
            result.append(left[i])  # tambahkan elemen dari daftar kiri ke hasil penggabungan
            i += 1                    # pindah ke elemen berikutnya di daftar kiri

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def quick_sort(numbers):  # "Pilih pivot, bagi data menjadi dua bagian, lalu urutkan secara rekursif" - algoritma pengurutan cepat

    if len(numbers) <= 1:
        return numbers

    pivot = numbers[len(numbers) // 2]  # pivot = elemen yang dijadikanpatokan untuk membagi data (diambil dari tengah daftar)

    left = [x for x in numbers if x < pivot]  # buat daftar baru yang berisi elemen-elemen yang lebih kecil dari pivot
    middle = [x for x in numbers if x == pivot]  # buat daftar baru yang berisi elemen-elemen yang sama dengan pivot ( dibutuhkan supaya kalau ada elemen yang sama dnegan pivot, angka tsb tidak menyebabkan recursion yg tidak perlu)
    right = [x for x in numbers if x > pivot]  # buat daftar baru yang berisi elemen-elemen yang lebih besar dari pivot
      # list Comprehension digunakan untuk membuat daftar baru berdasarkan kondisi tertentu, dalam hal ini membandingkan setiap elemen dengan pivot.
    return quick_sort(left) + middle + quick_sort(right)  # gabungkan hasil pengurutan dari daftar kiri, elemen pivot, dan daftar kanan
    


numbers = [98, 35, 54, 12, 45]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)

numbers = [12, 7, 35, 21, 9]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)

numbers = [7, 5, 8, 9, 6]
sorted_numbers = insertion_sort(numbers)
print(sorted_numbers)

numbers = [8, 3, 5, 2, 7, 1, 4, 6]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)

numbers = [9, 2, 6, 10, 7, 3, 8, 5, 1, 4]
sorted_numbers = quick_sort(numbers)
print(sorted_numbers)