# Problem: Brain's Photos (Codeforces 707A)
# Tags: Implementation
# Link: https://codeforces.com/problemset/problem/707/A
n,m=map(int,input().split())
colors={"C","M","Y"}   
flag=False
for _ in range(n):
    rows=input().split()   
    for char in rows :
        if char in colors:
            flag=True
            break   
    if flag==True:
        break        
if flag==True:
    print("#Color")
else:
    print("#Black&White")