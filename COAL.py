def main():
    Escolha1 = int(input(
        "Digite a Sessão desejada:" "\n"
        "1.Calculadora de temperatura" "\n"
        "2.Calculadora comum" "\n"
        "3.Calculadora geral" "\n"))

    if Escolha1 == 1:
        def Cal_Temp():
            C = float(input("Digite a temperatura em Celsius:" "\n"))
            F = 9/5 * C + 32
            K = C + 273.15
            print(f"{C}°C, {F}°F, {K} Kelvins" "\n")
            back = int(input("1.Operação realizada, Deseja voltar ao Menu?" "\n"
                             "2.Sair" "\n"))
            if back == 1:
                main()
        Cal_Temp()

    if Escolha1 == 3:
        def Cal_Geral():
            num1 = float(input("Digite o primeiro número:" "\n"))
            num2 = float(input("Digite o segundo número:" "\n"))
            res1 = num1 + num2
            res2 = num1 - num2
            res3 = num1 * num2
            res4 = num1 / num2
            res5 = num1 // num2
            res6 = num1 % num2
            res7 = num1 ** num2

            print(f'{num1} + {num2} = {res1.__round__(2)}')
            print(f'{num1} - {num2} = {res2.__round__(2)}')
            print(f'{num1} * {num2} = {res3.__round__(2)}')
            print(f'{num1} / {num2} = {res4.__round__(2)}')
            print(f'{num1} // {num2} = {res5.__round__(2)}')
            print(f'{num1} % {num2} = {res6.__round__(2)}')
            print(f'{num1} ** {num2} = {res7.__round__(2)}')
            back = int(input("1.Operação realizada, Deseja voltar ao Menu?" "\n"
                             "2.Sair" "\n"))
            if back == 1:
                main()
        Cal_Geral()

    if Escolha1 == 2:
        def Cal_Com():
            num1 = float(input("Digite o primeiro número:" "\n"))
            num2 = float(input("Digite o segundo número:" "\n"))
            operador = input("digite a operação:" "\n")

            match operador:

                case '+':
                    res = num1 + num2

                case '-':
                    res = num1 - num2

                case '*':
                    res = num1 * num2

                case '/':
                    res = num1 / num2

                case '//':
                    res = num1 // num2

                case '%':
                    res = num1 % num2

                case '**':
                    res = num1 ** num2

            print(f'O resultado é: \n {res.__round__(2)}')
            back = int(input("1.Operação realizada, Deseja voltar ao Menu?" "\n"
                             "2.Sair" "\n"))
            if back == 1:
                main()
        Cal_Com()


main()
