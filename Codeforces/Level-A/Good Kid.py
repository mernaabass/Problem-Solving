# Problem: Good Kid (Codeforces 1873B)
# Tags: Brute force, Greedy, Math	
# Link: https://codeforces.com/problemset/problem/1873/B
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    product=1
    d=min(a)+1
    flag=False
    for x in a:
        if x==min(a)and flag==False :
            product*=d
            flag =True
        else:
            product*=x   
    print(product)              