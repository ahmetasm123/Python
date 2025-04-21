x = str(input("Type a random word: "))
x = x.lower()

ans1 = "aeıioöuü"
ans3 = 0

for i in x:
    if i in ans1:
        ans3 += 1
print("Total:", str(ans3))