# Problem: osu!mania (Codeforces 2009B)
# Tags: Brute Force, Implementation
# Link: https://codeforces.com/problemset/problem/2009/B
t=int(input())
for _ in range(t):
    n=int(input())
    index=[]
    for _ in range(n):
        row=input()
        idx=row.index("#")+1
        index.append(idx)
    print(*index[::-1])            