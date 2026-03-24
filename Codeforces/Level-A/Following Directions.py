# Problem: Following Directions (Codeforces 1791B)
# Tags: Geometry, Implementation
# Link: https://codeforces.com/problemset/problem/1791/B
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    x=0
    y=0
    passed_candy=False
    for char in s:
        if char=="U":
            x+=1
        elif char=="D":
            x-=1
        elif char=="R":
            y+=1
        else:
            y-=1
        if x==1 and y==1:
            passed_candy=True
            break
    if passed_candy:
        print("YES") 
    else:
        print("NO")       