# Problem: Problem Generator (Codeforces 1980A)
# Tags: Math
# Link: https://codeforces.com/problemset/problem/1980/A
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=input()
    levels=[ 'A', 'B', 'C', 'D', 'E', 'F','G']
    min_prob=0
    for letter in levels:
        available=a.count(letter)
        if available < m:
            min_prob +=(m-available)
    print(min_prob)        