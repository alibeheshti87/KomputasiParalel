import multiprocessing

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

def proses_baris(baris_A):
    kolom1 = (baris_A[0] * B[0][0]) + (baris_A[1] * B[1][0]) + (baris_A[2] * B[2][0])
    kolom2 = (baris_A[0] * B[0][1]) + (baris_A[1] * B[1][1]) + (baris_A[2] * B[2][1])
    kolom3 = (baris_A[0] * B[0][2]) + (baris_A[1] * B[1][2]) + (baris_A[2] * B[2][2])
    
    return [kolom1, kolom2, kolom3]

if __name__ == '__main__':
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    with multiprocessing.Pool() as pool:
        hasil = pool.map(proses_baris, A)

    print("Hasil Perkalian Matriks 3x3:")
    for baris in hasil:
        print(baris)
