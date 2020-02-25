marklist=[]
scorelist=[]
n=int(input())
for i in range(n):
    name=input()
    score=float(input())
    marklist.append([name,score])
    scorelist.append(score)
sorted(scorelist)
x=min(scorelist)
for a in range(n):
    if(x==min(scorelist)):
        scorelist.remove(min(scorelist))
b=min(scorelist)
    
for j,k in sorted(marklist):
    if(k==b):
        print(j)
