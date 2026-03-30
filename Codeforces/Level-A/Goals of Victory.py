# Problem: Goals of Victory (Codeforces 1877A)
# Tags: Math
# Link: https://codeforces.com/problemset/problem/1877/A
# Logic: The sum of all efficiencies in a tournament is always 0.So the missing efficiency is simply the negative of the sum of the rest.
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    missing_efficiency=-sum(a)
    print(missing_efficiency)