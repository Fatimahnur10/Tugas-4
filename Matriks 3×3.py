# Matriks A dan B yang sudah ditentukan
Orde_A = [[2, 4, 1],
           [0, 3, -1],
           [5, 2, 6]]

Orde_B = [[1, 0, 3],
           [4, -1, 2],
           [-2, 5, 1]]

# Memeriksa apakah orde matriks sesuai
if len(Orde_A) != 3 or len(Orde_B) != 3 or len(Orde_A[0]) != 3 or len(Orde_B[0]) != 3:
    print("Matriks tidak dapat dikalikan, pastikan kedua matriks berordo 3x3.")
else:
    # Inisialisasi matriks hasil
    hasil = [[0 for _ in range(3)] for _ in range(3)]

    # Mengalikan matriks A dan B
    for i in range(3):
        for j in range(3):
            hasil[i][j] = sum(Orde_A[i][k] * Orde_B[k][j] for k in range(3))

    # Menampilkan hasil perkalian
    print("Hasil perkalian matriks A dan B adalah:")
    for row in hasil:
        print(row)

print("Selesai")

Output yang dihasilkan 

Hasil perkalian matriks A dan B adalah:
[2, 29, 16]
[0, 15, 5]
[28, 37, 37]
Selesai
