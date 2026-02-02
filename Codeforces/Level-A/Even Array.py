# Problem: Even Array (Codeforces 1367B)
# Tags: Greedy, Math
# Link: https://codeforces.com/problemset/problem/1367/B
t=int(input())
for _ in range(t):
    wrong_evens=0
    wrong_odds=0
    n = int(input())
    a=list(map(int,input().split()))
    for i in range(n) :
        if a[i]%2 !=0 and i %2 ==0:
            wrong_odds += 1
        elif  a[i]%2 ==0 and i %2 !=0:
            wrong_evens += 1
    if wrong_odds ==wrong_evens:
        print(wrong_odds)
    elif wrong_odds!=wrong_evens:
        print("-1")                
