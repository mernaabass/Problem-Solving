# Problem: Increasing (Codeforces 1742B)
# Tags: Greedy, Implementation, Sortings
# Link: https://codeforces.com/problemset/problem/1742/B
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s= set(a)
    if len(s)<len(a):
        print("NO")
    else:
        print("Yes")    