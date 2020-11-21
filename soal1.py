arrBerat = []
bMin = 0
bMax = 0

def hitungMinMax(arrBerat):
    global bMin, bMax
    # Definisikan Proses Mencari Berat Maximum Dan Minimum
    arrBerat.sort()
    bMin = arrBerat[0]
    bMax = arrBerat[len(arrBerat)-1]
    
def rerata(arrBerat):
    total = 0
    for n in arrBerat:
        total = total + n
    # Definisikan Proses Mencari Rerata Dari Total Berat
    rerata = total / len(arrBerat)

    # Return Hasil Rerata
    return rerata

print('Masukkan Banyak Data Berat Balita :', end=" ")
n = int(input())

for i in range(n):
    print(f'Masukkan Berat Balita Ke-{i+1} :', end=' ')
    # Inisialisasi Input Data Berat
    data = input()
    # Masukkan Data Berat Ke Array (arrBerat)
    arrBerat.insert(i,float(data))

# Panggil procedur hitungMinMax(arrBerat)
hitungMinMax(arrBerat)

# Print Data Minimum, Maximum, dan Rerata Berat
print("Berat Balita Minimum : {0:.2f} kg".format(bMin))
print("Berat Balita Maksimum : {0:.2f} kg".format(bMax))
print("Rerata berat balita : ",round(rerata(arrBerat), 2)," kg")
