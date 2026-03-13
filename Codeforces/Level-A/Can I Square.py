# Problem: Can I Square (Codeforces 1915C)
# Tags: Binary Search ,Implementation
# Link: https://codeforces.com/problemset/problem/1915/C
import math
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    total_squares=sum(a)
    root=math.isqrt(total_squares)
    if root*root==total_squares:
        print("Yes")
    else:
        print("No")    