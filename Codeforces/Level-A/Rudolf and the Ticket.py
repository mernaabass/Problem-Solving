# Problem: Rudolf and the Ticket (Codeforces 1941A)
# Tags: Brute force, Math
# Link: https://codeforces.com/problemset/problem/1941/A
t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    pairs=0
    for coin_b in b:
        for coin_c in c:
            if coin_b + coin_c <= k:
                pairs += 1
    print(pairs)