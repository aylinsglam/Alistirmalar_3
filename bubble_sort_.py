liste=[7,3,5,8,2,9,4,15,6]
n=len(liste)
for i in range(1,n-1):
    for j in range(0,n-i):
        if liste[j]>liste[j+1]:
            temp=liste[j]
            liste[j]=liste[j+1]
            liste[j+1]=temp
print(liste)
    
