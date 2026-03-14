# Problem: Honest Coach (Codeforces 1360B)
# Tags: Greedy, Sortings
# Link: https://codeforces.com/problemset/problem/1360/B
t=int(input())
for _ in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    s.sort()
    diff=[s[i+1]-s[i] for i in range(n-1)]
    print(min(diff))