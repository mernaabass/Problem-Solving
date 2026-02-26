# Problem: Legs (Codeforces 1806A)
# Tags: Binary Search, Math, Ternary Search
# Link: https://codeforces.com/problemset/problem/1996/A
t = int(input())
for _ in range(t):
    n = int(input())
    cows = n // 4
    remainder = n % 4
    chickens = remainder // 2
    print(cows + chickens)