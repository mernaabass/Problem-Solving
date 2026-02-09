# Problem: Vlad and the Best of Five (Codeforces 1926A)
# Tags: Implementation
# Link: https://codeforces.com/problemset/problem/1926/A
t=int(input())
for _ in range(t):
    s=input()
    if s.count("A")>=3:
        print("A")
    else:
        print("B")    