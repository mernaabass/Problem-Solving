# Problem: Desorting (Codeforces 1853A)
# Tags: Brute Force ,Greedy, Math
# Link: https://codeforces.com/problemset/problem/1853/A
t=int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    diffs = [a[i+1] - a[i] for i in range(n-1)]
    if min(diffs) < 0:
        print(0)
    else:
        ans = (min(diffs) // 2) + 1
        print(ans)