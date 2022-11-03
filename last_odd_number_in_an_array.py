a=int(input())
n=list(map(int,input().split()))
b=len(n)
oddn=0
evenn=0
for i in range(0,len(n)):
    if(n[i]%2==0):
        evenn=n[i]
    else:
        oddn=n[i]
        
print(oddn)