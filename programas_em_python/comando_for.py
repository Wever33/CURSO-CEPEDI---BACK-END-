
"""
for contador in [1,2,3,4]:
    print(contador+1)
print("-------------------")
for contador in range(9):
    print(contador)
print("-------------------")
for contador in range(2,10):
    print(contador)
print("-------------------")
for contador in range(1,10, 2):
    print(contador)
print("-------------------")
for contador in range(10,2,-2):
    print(contador)

for contador in range(10):
    print("Tenho que estudar")


for contador in range(2,11,2):
    print(f"{contador} é par")

print("-----------------------------")

for contador in range(11):
    if contador % 2 == 0:
        print(f"{contador} é par")
"""


soma = 0
for i in range(1,7):
    termo = 1/i
    soma += termo
    print(f"O termo {i} = {termo:.2f}")
print(f"Soma dos elementos: {soma:.2f}")
