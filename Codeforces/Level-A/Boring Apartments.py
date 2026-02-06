# Problem: Boring Apartments (Codeforces 1433A)
# Tags: Implementation, Math
# Link: https://codeforces.com/problemset/problem/1433/A
t=int(input())
for _ in range(t):
    s=input()
    digit=int(s[0])
    length=len(s)
    prev_cost=(digit-1)*10
    current_cost=length*(length+1)//2
    print(prev_cost+current_cost)
