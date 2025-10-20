# Os dicionarios que serão usados fora de outras funções para serem globais
veiculos = {}
opçoes_servico = {
    "1": {"FASE": "REVISÃO"},
    "2": {"FASE": "CONSERTO"},
    "3": {"FASE": "AGUARDANDO"},
    "4": {"FASE": "FINALIZADO"}

}


# A função para o usuário navegar entre as opções
def menu():
    while True:
        print("\nBem-vindo ao Menu!")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Pesquisar")
        print("4 - Remover")
        print("5 - Atualizar")
        print("6 - Encerrar Programa")
        opcao = input("Escolha uma opção:\n")

# A parte que valida a resposta do usuário
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            pesquisar()
        elif opcao == "4":
            remover()
        elif opcao == "5":
            atualizar()
        elif opcao == "6":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# A função para que o usuário possa cadastrar


def cadastrar():
    modelo = input("Modelo:\n").upper().strip()
    marca = input("Marca:\n").upper().strip()
    dono = input("Dono:\n").upper().strip()
    placa = input("Placa:\n").upper().strip()
    if placa in veiculos:
        print("Essa placa já está cadastrada. Use a opção de atualizar se quiser modificar os dados.")
        return
    # Sai da função sem cadastrar novamente, visto que placa ja consta no sistema

    print("\n""Serviços disponiveis:""\n" "1 - Revisão""\n" "2 - Conserto""\n" "3 - Aguardando""\n" "4 - Finalizado""\n")
    cod_servico = input("Serviço:\n").upper().strip()

    # Irá percorrer o usuário e caso não tenha o serviço desejado ira retorna "DESCONHECIDO"
    servico = opçoes_servico.get(cod_servico, "DESCONHECIDO")

# Onde será criado o dicionário conforme as informações que o usuário digitou
    veiculos[placa] = {
        "Modelo": modelo,
        "Marca": marca,
        "Dono": dono,
        "Serviço": servico,
        "Valor": "-"
    }
    # Condições para o valor
    if cod_servico in ["1", "2"]:
        valor = input("Digite o preço para esse serviço: R$ ").strip()
        veiculos[placa]["Valor"] = f"R$ {valor}"
        print("Preço adicionado com sucesso!")
    else:
        veiculos[placa]["Valor"] = "-"

    print("\nVeículo cadastrado com sucesso!")


# A função que permite que o usuário visualise quais são os itens cadastrados
def listar():
    print("Veículos cadastrados""\n")
    for placa in veiculos:
        print(f"{placa}: {veiculos[placa]}")

# Uma parte que fornece a leitura de quantos itens há no sistema
    total = len(veiculos)
    print(f"\nTotal de veículos cadastrados: {total}")

    contar_servicos()

# uma função para padronizar o estado que o veículo se encotra(um desafio a mais)

def contar_servicos():
    total_revisao = 0
    total_conserto = 0
    total_aguardando = 0
    total_finalizado = 0

# o for irá percorrer o dicionário e comparar para conseguirmos contar e fornecer dados
    for cod_servicos in veiculos.values():
        if cod_servicos.get("Serviço") == "REVISÃO":
            total_revisao += 1
        elif cod_servicos.get("Serviço") == "CONSERTO":
            total_conserto += 1
        elif cod_servicos.get("Serviço") == "AGUARDANDO":
            total_aguardando += 1
        elif cod_servicos.get("Serviço") == "FINALIZADO":
            total_finalizado += 1
# Exibidos em linhas separadas para melhor visualização
    print(f"Total de veículos em revisão: {total_revisao}")
    print(f"Total de veículos em conserto: {total_conserto}")
    print(f"Total de veículos em aguardando: {total_aguardando}")
    print(f"Total de veículos em finalizado: {total_finalizado}")

# Função para o usuário pesquisar no sistema usando a placa como chave


def pesquisar():
    placa = input(
        "Digite a placa do veículo que deseja buscar.""\n").upper().strip()
    if placa in veiculos:
        print(f"{placa}: {veiculos[placa]}")
    else:
        print("Veículo não cadastrado")

# Função para remoção de itens


def remover():
    placa = input(
        "Digite a placa do veículo que deseja remover:\n").upper().strip()

    if placa in veiculos:
        print(
            f"Veículo com placa {placa}: {veiculos[placa]} removido com sucesso!\n")
        del veiculos[placa]
    else:
        print("Veículo não encontrado.\n")

# Função para a atualização


def atualizar():
    placa = input(
        "Digite a placa do veículo que deseja atualizar:\n").upper().strip()

    if placa in veiculos:
        print("Veículo encontrado.\n")

        # bloco para pedir para o usuário os novos dados q serão adicionados
        modelo = input(
            f"Novo modelo (atual: {veiculos[placa]['Modelo']}):\n").upper().strip()
        marca = input(
            f"Nova marca (atual: {veiculos[placa]['Marca']}):\n").upper().strip()
        dono = input(
            f"Novo dono (atual: {veiculos[placa]['Dono']}):\n").upper().strip()

        print("\nServiços disponíveis:")
        print("1 - Revisão")
        print("2 - Conserto")
        print("3 - Aguardando")
        print("4 - Finalizado\n")

        cod_servico = input(
            f"Novo serviço (atual: {veiculos[placa]['Serviço']}):\n").strip()

        # Irá percorrer o usuário e caso não tenha o serviço desejado ira retorna "DESCONHECIDO"
        novo_servico = opçoes_servico.get(
            cod_servico, {"FASE": "DESCONHECIDO"})

        veiculos[placa]["Modelo"] = modelo
        veiculos[placa]["Marca"] = marca
        veiculos[placa]["Dono"] = dono
        veiculos[placa]["Serviço"] = novo_servico["FASE"]

        # Condições para impedir que o usuário coloque valor onde não deveria
        if cod_servico in ["1", "2"]:
            valor = input(
                f"Novo valor (atual: {veiculos[placa]['Valor']}):\n").strip()
            veiculos[placa]["Valor"] = f"R$ {valor}"
        elif cod_servico["3", "4"]:
            veiculos[placa]["Valor"] = "-"

        print(f"\n{placa}: {veiculos[placa]}")
    else:
        print("\nVeículo não encontrado.")

# Todas as funções há um else para caso o usuário digite um item não existente


def main():
    menu()


if __name__ == "__main__":
    main()
