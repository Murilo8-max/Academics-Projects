lista_prioridade_alta = []
lista_prioridade_media = []
lista_prioridade_baixa = []

for i in range (5):
    opcao = input("Selecione a lista (alta, media, baixa):\n").lower()
    
    item = input("Digite a tarefa:""\n")

    if opcao == "alta":
        lista_prioridade_alta.append(item)
        print(f"item {item} adicionado a lista de prioridade ALTA:")
        print("Lista atual:", lista_prioridade_alta)
    elif opcao == "media":
        lista_prioridade_media.append(item)
        print(f"Item '{item}' adicionado à lista de prioridade MÉDIA.")
        print("Lista atual:", lista_prioridade_media)
        
    elif opcao == "baixa":
        lista_prioridade_baixa.append(item)
        print(f"Item '{item}' adicionado à lista de prioridade BAIXA.")
        print("Lista atual:", lista_prioridade_baixa)
        
    else:
        print("Opção inválida. Tarefa não adicionada.")
        

print("Lista Final""\n")
print("Alta:", lista_prioridade_alta)
print("Média:", lista_prioridade_media)
print("Baixa:", lista_prioridade_baixa)

