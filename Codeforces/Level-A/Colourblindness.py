# Problem: Colourblindness (Codeforces 1722B)
# Tags: Implementation
# Link: https://codeforces.com/problemset/problem/1722/B
t=int(input())
for _ in range(t):
    c=int(input())
    r1=input()
    r2=input()
    if r1.count("R")!=r2.count("R"):
        print("NO")
    else:
        for i in range(c):
            if r1[i]=="R":
                if r1[i]!=r2[i]:
                    print("NO")
                    break
        else:
            print("YES")            
