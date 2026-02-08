# Problem: Vanya and Cubes (Codeforces 1433A)
# Tags: Implementation
# Link: https://codeforces.com/problemset/problem/1433/A
n=int(input())
x=0
cubes=0
while cubes<=n:
    x+=1
    cubes+=x*(x+1)//2
print(x-1)