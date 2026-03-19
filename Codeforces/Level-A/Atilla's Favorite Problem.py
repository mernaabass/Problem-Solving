# Problem: Atilla's Favorite Problem (Codeforces 1760B)
# Tags: Greedy, Implementation, Strings
# Link: https://codeforces.com/problemset/problem/1760/B
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    index=[]
    for x,y in enumerate(alphabet,start=1):
        if y in s:
            index.append(x)
    print(max(index))        