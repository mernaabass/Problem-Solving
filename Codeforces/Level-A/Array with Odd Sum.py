# Problem: Array with Odd Sum (Codeforces 1296A)
# Tags: Math
# Link: https://codeforces.com/problemset/problem/1296/A
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    odd_count=sum(1 for x in a if x%2!=0)
    even_count=n-odd_count
    if odd_count %2!=0:
        print("YES")
    elif odd_count>0 and even_count>0:
        print("YES")  
    else:
        print("NO")