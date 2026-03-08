# Problem: Floor Number (Codeforces 1426A)
# Tags: Implementation, Math
# Link: https://codeforces.com/problemset/problem/1426/A
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    if n <= 2:
        print(1)
    else:
        remaining_apts = n - 2
        floors_needed = remaining_apts // x
        if remaining_apts % x == 0:
            print(floors_needed + 1)
        else:
            print(floors_needed + 2)