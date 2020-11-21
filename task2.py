arrTanding[]

print("Klub A : ", end="")
A = input()
print("Klub B : ", end="")
B = input()

print("Pertandingan 1 : ", end="")
a = input().split()
arrTanding.append(a)
i=0
while int(arrTanding[i][0])>=0 and int(arrTanding[i][1])>=0:
    print("Pertandingan {} : ".format(i+2), end="")
    a = input().split()
    arrTanding.append(a)
    i = i+1

j=0
while j < i:
    if (int(arrTanding[j][0]) > int(arrTanding[j][1])) :
        print("Hasil {} : {}".format(j+1,A))
    elif (int(arrTanding[j][0])<int(arrTanding[j][1])) :
        print("Hasil {} : {}".format(j+1,B))
    else :
        print("Hasil {} : Draw".format(j+1))
    j = j+1
print("Pertandingan selesai")
