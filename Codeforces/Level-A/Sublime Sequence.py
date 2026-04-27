# Problem: Sublime Sequence (Codeforces 2148A)
# Tags: Brute force, Hashing, Math
# Link: https://codeforces.com/problemset/problem/2148/A
t=int(input())
for _ in range(t):
    x,n=map(int,input().split())
    if n%2==0:
        print(0)
    else:
        print(x)    
# Another Answer 
# for _ in range(t):
#     x,n=map(int,input().split())
#     if n%2!=0:
#         positive_num=n//2 +1
#     else:
#         positive_num=n//2
#     print(positive_num*x+(n//2)*-x)    