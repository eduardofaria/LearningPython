for value in range(1, 3):
    print(value)

print("\n ---------------------------- \n")

numbers = list(range(1, 5))
print(numbers)

print("\n ---------------------------- \n")

impares = list(range(1, 20, 2))
print("Ímpares: ", impares, "\n")
pares = list(range(2, 20, 2))
print("Pares ", pares)

print("\n ---------------------------- \n")

squares = []
for valores in range(1, 11):
    square = valores ** 2
    squares.append(square)
print(squares)

print("\n ---------------------------- \n")

raizes = []
for valores in range(1, 11):
    raizes.append(valores ** 3)
print(raizes)
print("Mínimo: ", min(raizes))
print("Máximo: ", max(raizes))
