# Problem: Bachgold Problem (Codeforces 749A)
# Tags: Greedy, Implementation, Math, Number Theory
# Link: https://codeforces.com/problemset/problem/749/A
# Logic: Use as many 2s as possible. If odd, use one 3 and the rest 2s.
n=int(input())
k=n//2
print(k)
if n%2==0:
    lst=k*[2]
else:
    lst=(k-1)*[2]+[3]    
print(*lst)    