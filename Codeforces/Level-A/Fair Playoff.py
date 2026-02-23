# Problem: Fair Playoff (Codeforces 1535A)
# Tags: Brute Force, Implementation
# Link: https://codeforces.com/problemset/problem/1535/A
t=int(input())
for _ in range(t):
    s=list(map(int,input().split()))
    finals1=max(s[0],s[1])
    finals2=max(s[2],s[3])
    last_finals=[finals1,finals2]
    last_finals.sort()
    s.sort()
    if last_finals[1]==s[-1] and last_finals[0]==s[-2]:
        print("YES")
    else:
        print("NO")    