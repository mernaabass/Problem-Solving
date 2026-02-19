# Problem: Do Not Be Distracted (Codeforces 1520A)
# Tags: Brute force, Implementation
# Link: https://codeforces.com/problemset/problem/1520/A
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    flag = False
    seen=set()
    seen.add(s[0])
    for i in range(1,n) :
        if s[i] in seen and s[i-1]!=s[i]:
                flag=True
                break
        else:
             seen.add(s[i])
    if flag ==True :
        print("No")
    else:
        print("Yes")          
