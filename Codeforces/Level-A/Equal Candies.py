# Problem: Equal Candies (Codeforces 1676B)
# Tags: Greedy, Math, Sortings
# Link: https://codeforces.com/problemset/problem/1676/B
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    candies_eaten=0
    for x in a:
        candies_eaten+=(x-min(a))
    print(candies_eaten)    