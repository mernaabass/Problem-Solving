# Problem: Required Remainder (Codeforces 1619A)
# Tags: Implementation, Strings
# Link: https://codeforces.com/problemset/problem/1619/A
t=int(input())
for _ in range(t):
    s=input()
    n=len(s)
    if n%2==0 :
        half=n//2
        if s[:half]==s[half:]:
            print("Yes")
        else:
            print("NO")
    else:
        print("NO")        