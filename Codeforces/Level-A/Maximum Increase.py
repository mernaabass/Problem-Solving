# Problem: Maximum Increase (Codeforces 702A)
# Tags: DP ,Greedy, Implementation
# Link: https://codeforces.com/problemset/problem/702/A
n=int(input())
a=list(map(int,input().split()))
current_len = 1  
max_len = 1      
for i in range(1, n):
    if a[i] > a[i-1]:
        current_len += 1
    else:
        current_len = 1  
    if current_len > max_len:
        max_len = current_len
print(max_len)   