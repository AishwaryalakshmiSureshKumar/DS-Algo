w1 = input()
w2 = input()

total = 0
for letter in "abcdefghijklmnopqrstuvwxyz":
    if letter in w1 and letter in w2:
        w1.remove(letter)
        w2.remove(letter)
total+=len(w1)+len(w2)
print(total)
