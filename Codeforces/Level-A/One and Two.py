# Problem: One and Two (Codeforces 1788A)
# Tags: Brute Force, Implementation, Math
# Link: https://codeforces.com/problemset/problem/1788/A
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total_twos = a.count(2)
    if total_twos % 2 != 0:
        print(-1)
    else:
        half_twos = total_twos // 2
        current_twos = 0
        for i in range(n):
            if a[i] == 2:
                current_twos += 1
                print(i + 1)
                break