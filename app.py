# VARIÁVEIS
total = []
totalfem = 0
totalmasc = 0
mediamasc = []

for i in range(15):
    alt = float(input("Digite sua altura: "))
    total.append(alt)
    sexo = input("Qual seu gênero: MASCULINO (M) FEMININO (F): ").upper()

    if sexo == "F":
        totalfem += 1
    elif sexo == "M":
        mediamasc.append(alt)
        totalmasc += 1

# Maior e menor altura do grupo
print(f"A maior altura do grupo é de: {max(total)} m")
print(f"A menor altura do grupo é de: {min(total)} m")

# Média de altura dos homens
if totalmasc > 0:
    media = sum(mediamasc) / totalmasc
    print(f"A média de altura dos homens do grupo é igual a: {media:.2f} m")
else:
    print("Não tem homens no grupo.")

# Quantidade de mulheres
print(f"A quantidade de mulheres no grupo é igual a: {totalfem}")
