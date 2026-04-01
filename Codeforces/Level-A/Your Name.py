# Problem: Your Name (Codeforces 2167B)
# Tags: Sortings, Strings
# Link: https://codeforces.com/problemset/problem/2167/B
# Logic: Two strings can be rearranged into each other if their sorted versions are identical (Anagram).
q=int(input())
for _ in range(q):
    n=int(input())
    s,t=input().split()
    if sorted(s)==sorted(t):
        print("Yes")
    else:
        print("No")    