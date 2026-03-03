# Problem: Square (Codeforces 2167A)
# Tags: Math, Sortings
# Link: https://codeforces.com/problemset/problem/2167/A
t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    if a==b==c==d :
        print("Yes")
    else:
        print("No")    