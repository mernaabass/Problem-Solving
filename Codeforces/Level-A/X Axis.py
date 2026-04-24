# Problem: X Axis (Codeforces 1986A)
# Tags: Brute force, Geometry, Math, Sortings
# Link: https://codeforces.com/problemset/problem/1986/A
t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    ans=max(a,b,c)-min(a,b,c)
    print(ans)