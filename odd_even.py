liste=[4,2,7,8,5,1,3,6,9]
n=len(liste)
if n%2==0: #eleman sayısına göre adım sayısını belirliyorum
    for i in range(0,n-1):
        if i%2==0: #ilk adımı 0 kabul edip çift sayılı adımlarda çift indisli elemanları karşılaştırıyorum
            for j in range(0,n-1,2):
                if liste[j]>liste[j+1]:
                    temp=liste[j]
                    liste[j]=liste[j+1]
                    liste[j+1]=temp
        else:
            for j in range(1,n-1,2):
                if liste[j]>liste[j+1]:
                    temp=liste[j]
                    liste[j]=liste[j+1]
                    liste[j+1]=temp
    print(liste)
elif n%2==1:
    for i in range(0,n):
        if i%2==0:
            for j in range(0,n-1,2):
                if liste[j]>liste[j+1]:
                    temp=liste[j]
                    liste[j]=liste[j+1]
                    liste[j+1]=temp
        else:
            for j in range(1,n-1,2):
                if liste[j]>liste[j+1]:
                    temp=liste[j]
                    liste[j]=liste[j+1]
                    liste[j+1]=temp
    print(liste)
