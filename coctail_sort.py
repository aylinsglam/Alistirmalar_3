liste=[15,4,1,3,8,0,7,5,6,10,9,2]
n=len(liste)
for i in range(0,n-1):
    if i%2==0:
        a=i//2
        for j in range(0+a,n-1-a):
            if liste[j]>liste[j+1]:
                temp=liste[j]
                liste[j]=liste[j+1]
                liste[j+1]=temp
    else:
        b=i//2
        for j in range(n-1-a,0+a,-1):
            if liste[j]<liste[j-1]:
                temp=liste[j]
                liste[j]=liste[j-1]
                liste[j-1]=temp
print(liste)
                
        
