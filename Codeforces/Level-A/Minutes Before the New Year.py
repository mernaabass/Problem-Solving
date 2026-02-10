# Problem: Minutes Before the New Year (Codeforces 1283A)
# Tags: Math
# Link: https://codeforces.com/problemset/problem/1283/A
t=int(input())
for _ in range(t):
    h,m=map(int,input().split())
    hours_left=24-h
    minutes_left=(hours_left*60)-m
    print(minutes_left)    