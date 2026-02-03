# Problem: Required Remainder (Codeforces 1374A)
# Tags: Math
# Link: https://codeforces.com/problemset/problem/1374/A
t = int(input())
for _ in range(t):
    x,y,n=map(int,input().split())
    count=(n-y)//x
    k=count*x+y
    print(k)