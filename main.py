import math

R = 8.314


def menu():
    print("Qual cálculo você deseja realizar:")
    print("1 - Variação da temperatura")
    print("2 - Variação do volume")
    print("3 - Variação da pressão")
    return int(input("Opção: "))


def val_temp():
    n = float(input("Digite o número de mols (n): "))
    Ti = float(input("Digite a temperatura inicial (Ti em K): "))
    Tf = float(input("Digite a temperatura final (Tf em K): "))
    tipo_processo = input("Tipo de processo (V para volume constante, P para pressão constante): ").upper()
    tipo_gas = input("Tipo do gás (M Monoatômico, D Diatônico, P Poliatônico): ").upper()

    if tipo_processo == 'V':
        if tipo_gas == 'M':
            gas = 3.0 / 2.0
        elif tipo_gas == 'D':
            gas = 5.0 / 2.0
        elif tipo_gas == 'P':
            gas = 3
        else:
            print("Tipo de gás inválido!")
            return
        deltaS = n * gas * R * math.log(Tf / Ti)

    elif tipo_processo == 'P':
        if tipo_gas == 'M':
            gas = 5.0 / 2.0
        elif tipo_gas == 'D':
            gas = 7.0 / 2.0
        elif tipo_gas == 'P':
            gas = 4
        else:
            print("Tipo de gás inválido!")
            return
        deltaS = n * gas * R * math.log(Tf / Ti)
    else:
        print("Tipo de processo inválido!")
        return

    print(f"Variação da Entropia (mudança de temperatura): {deltaS:.2f} J/K")


def val_vol():
    n = float(input("Digite o número de mols (n): "))
    Vi = float(input("Digite o volume inicial (Vi em m³): "))
    Vf = float(input("Digite o volume final (Vf em m³): "))

    deltaS = n * R * math.log(Vf / Vi)
    print(f"Variação da Entropia (mudança de volume): {deltaS:.2f} J/K")


def val_press():
    n = float(input("Digite o número de mols (n): "))
    Pi = float(input("Digite a pressão inicial (Pi em Pa): "))
    Pf = float(input("Digite a pressão final (Pf em Pa): "))

    deltaS = -n * R * math.log(Pf / Pi)
    print(f"Variação da Entropia (mudança de pressão): {deltaS:.2f} J/K")


def main():
    print("Programa iniciado")
    opcao = menu()

    if opcao == 1:
        val_temp()
    elif opcao == 2:
        val_vol()
    elif opcao == 3:
        val_press()
    else:
        print("Opção inexistente")


if __name__ == "__main__":
    main()