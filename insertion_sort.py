liste=[7,3,5,8,2,9,4,15,6]
n=len(liste)
for i in range(1,n):
    for j in range(0,i):
        if liste[j]>liste[i]:
            temp=liste[i]
            liste[i]=liste[j]
            liste[j]=temp
            
print(liste)
    
