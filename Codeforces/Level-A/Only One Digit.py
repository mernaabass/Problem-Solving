# Problem: Only One Digit (Codeforces 2126A)
# Tags: Brute Force, Implementation, Math
# Link: https://codeforces.com/problemset/problem/2126/A
# Logic: Find the smallest digit in the number x.
t=int(input())
for _ in range(t):
    x=input()
    print(min(x))