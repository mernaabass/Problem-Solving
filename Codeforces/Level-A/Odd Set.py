# Problem: Odd Set (Codeforces 1542A)
# Tags: Math
# Link: https://codeforces.com/problemset/problem/1542/A
# Logic: A sum is odd ONLY if we add an Odd + Even.So we need exactly 'n' odd numbers and 'n' even numbers.
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    old_count=sum(1 for x in a if x%2!=0)
    if old_count==n:
        print("Yes")
    else:
        print("No")    