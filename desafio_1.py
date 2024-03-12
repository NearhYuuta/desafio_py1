def adicionar_contato(agenda, nome, telefone, email, favorito):
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": favorito == "1"
    }
    agenda.append(contato)
    print(f"\nO contato {nome} foi adicionado.")
    return

def ver_contatos(agenda):
    print("\nLista de contatos:")
    for indice, contato in enumerate(agenda, start=1):
        status = '✰' if contato["favorito"] else " "
        nome_contato = contato["nome"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
        print(f"\nContato {indice}:\nNome: {nome_contato}\nTelefone: {telefone_contato}\nEmail: {email_contato}\nFavoritos: [{status}]")
    return

def editar_contato(agenda, indice_contato, novo_nome, novo_numero, novo_email):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(agenda):
        agenda[indice_contato_ajustado]["nome"] = novo_nome
        agenda[indice_contato_ajustado]["telefone"] = novo_numero
        agenda[indice_contato_ajustado]["email"] = novo_email
        print(f"\nO contato {indice_contato} foi atualizado para {novo_nome}, {novo_numero}, {novo_email}")
    else:
        print("Indice de contato invalido")
    return

def favdesfav_contato(agenda, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    nome = agenda[indice_contato_ajustado]["nome"]
    if agenda[indice_contato_ajustado]["favorito"]:
        agenda[indice_contato_ajustado]["favorito"] = False
        print(f"\nO contato de {nome} foi desfavoritado")
    else:
        agenda[indice_contato_ajustado]["favorito"] = True
        print(f"\nO contato de {nome} foi favoritado")
    return

def ver_contatofav(agenda):
    print("\nLista de contatos favoritos:")
    for indice, contato in enumerate(agenda, start=1):
        if contato["favorito"]:
            nome_contato = contato["nome"]
            telefone_contato = contato["telefone"]
            email_contato = contato["email"]
            print(f"\nContato {indice}:\nNome: {nome_contato}\nTelefone: {telefone_contato}\nEmail: {email_contato}")
    return

def apagar_contato(agenda, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    agenda.remove(agenda[indice_contato_ajustado])
    print("Contato removido com sucesso!")

agenda = []

while True:
    print("\nMenu da agenda de contatos.")
    print("1. Adicionar um novo contato.")
    print("2. Visualizar lista de contatos.")
    print("3. Editar contato existente.")
    print("4. Marcar/Desmarcar favorito no contato.")
    print("5. Visualizar contatos favoritados.")
    print("6. Apagar um contato existente.")
    print("7. Encerrar operação")
    escolha = input("\nEscolha uma dessas opções: ")

    if escolha == "1":
        print("\nFaça o que pede a seguir")
        nome = input("Informe o nome do contato: ")
        telefone = int(input("Informe o número do contato: "))
        email = input("Informe o email do contato: ")
        favorito = input("Caso deseje favoritar, digite 1: ")
        adicionar_contato(agenda, nome, telefone, email, favorito)

    elif escolha == "2":
        ver_contatos(agenda)
    
    elif escolha == "3":
        ver_contatos(agenda)
        indice_contato = input("Digite o indice do contado que deseja editar: ")
        novo_nome = input("Digite o novo nome do contato: ")
        novo_numero = input("Digite o novo número do contato: ")
        novo_email = input("Digite o novo email do contato: ")
        editar_contato(agenda, indice_contato, novo_nome, novo_numero, novo_email)

    elif escolha == "4":
        ver_contatos(agenda)
        indice_contato = input("Digite o indice do contado que deseja alterar o favoritado: ")
        favdesfav_contato(agenda, indice_contato)

    elif escolha == "5":
        ver_contatofav(agenda)

    elif escolha == "6":
        ver_contatos(agenda)
        indice_contato = input("Digite o indice do contado que deseja apagar: ")
        apagar_contato(agenda, indice_contato)
        

    elif escolha == "7":
        print("A operação está sendo finalizada")
        break
