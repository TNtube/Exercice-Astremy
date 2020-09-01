# Exo 1
s1 = input()

s2 = input()

print("".join(i if i == j else "x" for i, j in zip(s1, s2)))


# Exo 2
import random

ran = [*range(*map(int, input("(0) ").split()))]

number = random.choice(ran)

print(f"(1) {number} ?")

user = input("(0) ")

while user != "=":
    if user == "+":
        ran = ran[ran.index(number)+1:]
    if user == "-":
        ran = ran[:ran.index(number)]
    number = random.choice(ran)
    print(f"(1) {number} ?")
    user = input("(0) ")
print("Yay !")


# Exo 3
from string import punctuation

print(punctuation)
s = input("Bonjour >")


for i in punctuation:
    s = s.split(i)
    for w, j in enumerate(s):
        if j:
            if j[0] == " ":
                s[w] = s[w][1:]
            if j[-1] == " ":
                s[w] = s[w][:-1]
    s = i.join(s)

print(s)

# Exo 4
letters = input()

words = input().split()

for i in words:
    for j in i:
        if not i.count(j) <= letters.count(j):
            break
    else:
        print(i, end=" ")

# Exo 5
s = '''# Titre 1
## Titre plus gros !
Bonjour à tous
Comment # allez vous ?
## Moi # ça va
#### Nyaaa
'''.split("\n")

for j, l in enumerate(s):
    line = l.split()
    count = 0
    for i, word in enumerate(line):
        if word.count("#") == len(word):
            count += 1
            line[i] = "[" + ((len(word)-1)*"très ").capitalize()
            if line[i] != "[":
                line[i] += "gros|"
            else:
                line[i] += "Gros|"

    s[j] = " ".join(line) + "]"*count

print("\n".join(s))

# Exo 6
s = '''
Bon finalement 17/20 car Lazor et Horus ne sont pas la et je me suis trompé
mais Pim nous a quitté

10/20
Trop d’histoires, les modos sont trop gentils.
'''.split()

tokens = []

for i in s:
    foo = i.split("/")
    if len(foo) - 1 and foo[0].isdigit() and foo[1].isdigit():
        tokens.append(int(foo[0]) * 100 / int(foo[1]))

print(f"Moyenne: {round(sum(tokens) / len(tokens))}%")
tokens = sorted(tokens)
if not len(tokens) % 2:
    med = round((tokens[len(tokens) // 2-1] + tokens[len(tokens) // 2]) / 2)
else:
    med = round(tokens[len(tokens)//2-1])

print(f"Médiane: {med}%")

# Exo 7

s = input()
boo = True
for i in range(len(s)):
    for j, w in enumerate(s):
        if boo:
            if w != "?" and not (j+1)%(i+1):
                if i-1:
                    print(i)
                    boo = False