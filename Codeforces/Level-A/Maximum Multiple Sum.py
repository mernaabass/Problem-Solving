# Problem: Maximum Multiple Sum (Codeforces 1985B)
# Tags: Brute Force, Math, Number Theory
# Link: https://codeforces.com/problemset/problem/1985/B
# Logic: 2 will always give the maximum sum because it has the most multiples, EXCEPT when n=3.
t=int(input())
for _ in range(t):
    n=int(input())
    if n==3 :
        print(3)
    else:
        print(2)    