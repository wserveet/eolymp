a,b,c=map(int,input().split())
liste=[]
liste.extend([a,b,c]) #5,3,4
liste.sort() # 3,4,5
teref_1 = max(liste)**2
teref_2 = min(liste)**2
teref_3 =liste[1]**2
if teref_1 == teref_2+teref_3 :
    print("YES")
else :
    print("NO")