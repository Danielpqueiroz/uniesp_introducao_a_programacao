from random import randint

v1 = []
v2 = []

for n in range(10):
    v1.append(randint(0,5))
    v2.append(randint(0,5))

print(v1)
print(v2)


for i in range(len(v1)):
    if v1[i]==v2[i]:
        print(f"O primeiro valor é {v1[i]}, o segundo é {v2[i]} na posição {i}" )

