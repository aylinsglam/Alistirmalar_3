liste=[7,9,1,8,3]
i=0
n=len(liste)
while i<n-1:
    if liste[i]<liste[i+1] :
        i+=1
    else:
        temp=liste[i]
        liste[i]=liste[i+1]
        liste[i+1]=temp
        i=0

print(liste)
    
    
        
