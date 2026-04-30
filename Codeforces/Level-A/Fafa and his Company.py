# Problem: Fafa and his Company (Codeforces 935A)
# Tags: Brute force, Implementation
# Link: https://codeforces.com/problemset/problem/935/A
n=int(input())
ways=0
for l in range (1,(n//2)+1):
    if n%l==0:
        ways+=1
print(ways)        