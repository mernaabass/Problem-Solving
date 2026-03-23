# Problem: Yogurt Sale (Codeforces 1955A)
# Tags: Math
# Link: https://codeforces.com/problemset/problem/1955/A
# Logic: Group yogurts into pairs, buy pairs at the cheapest rate, and buy any single leftover at the regular rate.
t=int(input())
for _ in range(t):
    n,a,b=map(int,input().split())
    best_pair_prince=min(2*a,b)
    pairs_count=n//2
    singles_count=n%2
    ans=(pairs_count*best_pair_prince)+(singles_count*a)
    print(ans)