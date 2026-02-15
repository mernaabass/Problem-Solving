# Problem: Cover in Water (Codeforces 1900A)
# Tags: Constructive Algorithms, Greedy, Implementation, Strings
# Link: https://codeforces.com/problemset/problem/1900/A
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    if "..." in s:
        print(2)
    else :
        print((s).count("."))    