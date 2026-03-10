# Problem: Jagged Swaps (Codeforces 1896A)
# Tags: Sortings
# Link: https://codeforces.com/problemset/problem/1896/A
# Logic: The first element can never be moved. Thus, it MUST be 1 for the array to be sortable.
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if a[0]==1:
        print("YES")
    else:
        print("NO")    