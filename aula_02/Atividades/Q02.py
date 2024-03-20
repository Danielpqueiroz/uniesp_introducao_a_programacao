'''2. Faça um programa que mostre as tabuadas dos números de 1 a 10.'''
for num in range(1,11):
    print()
    print(f"Tabuada do {num}:")
    print()
    for num2 in range (1,11):
        resultado = num *num2
        print(f"   {num} * {num2} = {resultado};")