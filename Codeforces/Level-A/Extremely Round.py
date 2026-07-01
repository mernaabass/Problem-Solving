# Problem: Extremely Round (Codeforces 1766A)
# Tags: Brute force, Implementation
# Link: https://codeforces.com/problemset/problem/1766/A
# Logic: Answer = (length of n - 1) * 9 + first digit of n
t = int(input())
for _ in range(t):
    n_str = input().strip()
    length = len(n_str)
    first_digit = int(n_str[0])
    ans = (length - 1) * 9 + first_digit
    print(ans)