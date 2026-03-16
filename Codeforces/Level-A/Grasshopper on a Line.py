# Problem: Grasshopper on a Line (Codeforces 1837A)
# Tags: Constructive Algorithms, Math
# Link: https://codeforces.com/problemset/problem/1837/A
t=int(input())
for _ in range(t):
    x,k=map(int,input().split())
    if x%k!=0:
        print(1)
        print(x)
    else:
        print(2) 
        print(x-1,1) 
          