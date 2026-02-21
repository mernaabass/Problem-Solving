# Problem: Minimal Square (Codeforces 1360A)
# Tags: Greedy, Math
# Link: https://codeforces.com/problemset/problem/1360/A
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    
    min_side = min(a, b)
    max_side = max(a, b)
    square_side = max(min_side * 2, max_side)
    print(square_side ** 2)    