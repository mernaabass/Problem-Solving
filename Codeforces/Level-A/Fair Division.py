# Problem: Fair Division (Codeforces 1472B)
# Tags: Dp, Greedy, Math
# Link: https://codeforces.com/problemset/problem/1472/B
# Logic: Total sum must be even. If the target (sum/2) is odd, we must have at least one '1' to handle the remainder.
t=int(input())
for _ in  range(t):
    n=int(input())
    w=list(map(int,input().split()))
    total=sum(w)
    target=total//2
    if total%2!=0:
        print("No")
    elif target %2!=0 and w.count(1)==0:
        print("No")    
    else:
        print("Yes")    