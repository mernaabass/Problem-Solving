# Problem: Word on the Paper (Codeforces 1850C)
# Tags: Implementation, Strings
# Link: https://codeforces.com/problemset/problem/1850/C
t=int(input())
for _ in range(t):
    word=""
    for _ in range(8):
        row=input()
        for char in row:
            if char!=".":
                word+=char
    print(word)            