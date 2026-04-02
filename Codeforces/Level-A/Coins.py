# Problem: Coins (Codeforces 1814A)
# Tags: Implementation, Math
# Link: https://codeforces.com/problemset/problem/1814/A
# Logic: If n is even -> YES. If n is odd, k MUST be odd to make it -> YES. Otherwise -> NO.
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    if n%2==0 or k%2!=0:
        print("Yes")
    else:
        print("No")    