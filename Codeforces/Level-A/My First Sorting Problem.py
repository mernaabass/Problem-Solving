# Problem: My First Sorting Problem (Codeforces 1971A)
# Tags: Implementation, Sortings
# Link: https://codeforces.com/problemset/problem/1971/A
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    print(min(x,y),max(x,y))