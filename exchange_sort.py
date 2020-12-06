liste=[7,3,5,8,2,9,4,15,6]
n=len(liste)
for i in range(0,n-1):
    for j in range(i+1,n):
        if liste[j]<liste[i]:
            temp=liste[i]
            liste[i]=liste[j]
            liste[j]=temp
print(liste)
