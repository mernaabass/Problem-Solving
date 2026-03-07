# Problem: Triple (Codeforces 2094A)
# Tags: Strings
# Link: https://codeforces.com/problemset/problem/2094/A
t=int(input())
for _ in range(t):
    word=input().split()
    print(word[0][0]+word[1][0]+word[2][0])