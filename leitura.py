def coletar_dados():
    """
    Coleta os dados de leitura do usuário.
    """
    print("--- Dados sobre o leitor e seus hábitos de leitura ---")
    nome = input("Qual o seu nome? ")
    idade = int(input("Qual a sua idade? "))
    cidade = input("Em qual cidade você mora? ")
    estado = input("Em qual estado? ")
    livros_digitais = int(input("Quantos livros digitais você leu no último ano? "))
    livros_fisicos = int(input("Quantos livros físicos você leu no último ano? "))
    preferencia = input("Qual a sua preferência de leitura (Digital/Físico)? ")
    horas_estudo = float(input("Quantas horas você dedica à leitura para estudo por semana? "))
    horas_lazer = float(input("Quantas horas você dedica à leitura por lazer por semana? "))
    paginas = int(input("Em média, quantas páginas têm os livros que você lê? ")) 

    return {
        "nome": nome,
        "idade": idade,
        "cidade": cidade,
        "estado": estado,
        "livros_digitais": livros_digitais,
        "livros_fisicos": livros_fisicos,
        "total_livros": livros_digitais + livros_fisicos,
        "preferencia": preferencia,
        "horas_estudo": horas_estudo,
        "horas_lazer": horas_lazer,
        "paginas": paginas
    }

def exibir_mensagem(dados):
    """
    Exibe uma mensagem de boas-vindas personalizada.
    """
    print(f"\n--- Olá, {dados['nome']}! ---")
    print(f"É ótimo ver um(a) leitor(a) de {dados['idade']} anos da cidade de {dados['cidade']}, {dados['estado']}.")

    # Sugestão de informação útil baseada na idade e local
    if dados['idade'] < 18:
        print("\nSugestão: Que tal explorar a seção de literatura jovem adulto da biblioteca municipal de "
              f"{dados['cidade']}? Você pode encontrar novas aventuras incríveis por lá!")
    elif 18 <= dados['idade'] <= 25:
        print("\nSugestão: Muitas universidades em seu estado, como as da capital, "
              "oferecem acesso a vastas bibliotecas digitais. Pode ser uma ótima oportunidade para seus estudos!")
    else:
        print(f"\nSugestão: Já pensou em participar de um clube do livro em {dados['cidade']}? "
              "É uma excelente forma de conhecer novas pessoas e descobrir autores fantásticos.")

def estimativa_leitura(total_livros):
    """
    Calcula e exibe uma estimativa de leitura para os próximos 5 anos.
    """
    estimativa = total_livros * 5
    print("\n--- Estimativa de leitura para os próximos 5 anos ---")
    print(f"Mantendo seu ritmo atual, você lerá aproximadamente {estimativa} livros nos próximos 5 anos.")

    if total_livros > 20:
        print("Uau! Você é um leitor e tanto! Continue com esse ritmo impressionante.")
    elif 5 <= total_livros <= 20:
        print("Você tem um ótimo ritmo de leitura. Continue explorando o mundo dos livros!")
    else:
        print("Cada livro é uma jornada. Que tal tentar aumentar um pouco seu ritmo para descobrir ainda mais histórias?")

def calcular_horas_anuais(horas_semanais, tipo):
    """
    Calcula o total de horas anuais dedicadas a um tipo de leitura.
    """
    horas_anuais = horas_semanais * 52
    print(f"\n--- Total de horas de leitura para {tipo.capitalize()} por ano ---")
    print(f"Você dedica aproximadamente {horas_anuais:.2f} horas por ano à leitura para {tipo}.")

def estimativa_paginas(total_livros, paginas_por_livro):
    """
    Estima o total de páginas lidas em um ano.
    """
    paginas_anuais = total_livros * paginas_por_livro
    print("\n--- Total de páginas lidas por ano ---")
    print(f"Com base na sua média, estimamos que você leia cerca de {paginas_anuais} páginas por ano.")
    print("Isso equivale a ler 'Guerra e Paz' (aproximadamente 1225 páginas) "
          f"cerca de {paginas_anuais // 1225} vez(es) por ano!")

def recomendacao(preferencia, nome):
    """
    Uma recomendação baseada na preferência de leitura.
    """
    print(f"\n--- Recomendação com base na sua preferência ---")
    if preferencia.lower() == 'digital':
        print(f"Olá, {nome}! Como você prefere a leitura digital, que tal explorar plataformas como o Kindle Unlimited ou o Skeelo?")
        print("Elas oferecem um catálogo imenso de livros por uma assinatura mensal, o que pode ser perfeito para o seu ritmo!")
    elif preferencia.lower() == 'físico':
        print(f"Olá, {nome}! Já que você ama o cheiro e o toque dos livros físicos, que tal começar uma "
              "pequena biblioteca em casa com seus títulos favoritos?")
        print("Além disso, visitar sebos em sua cidade pode revelar tesouros literários por preços incríveis.")
    else:
        print(f"Olá, {nome}! Ser um leitor que transita entre o físico e o digital é ótimo!")
        print("Aproveite o melhor dos dois mundos: a praticidade dos e-books para o dia a dia e o charme dos livros físicos para os momentos de relaxamento.")

def main():
    """
    Função principal que orquestra o programa.
    """
    # Coleta os dados do usuário
    dados_usuario = coletar_dados()

    # 1 - Mensagem personalizada
    exibir_mensagem(dados_usuario)

    # 2 - Estimativa de leitura
    estimativa_leitura(dados_usuario['total_livros'])

    # 3 - Cálculo de estudo por ano
    calcular_horas_anuais(dados_usuario['horas_estudo'], "estudo")

    # 4 - Cálculo de leituras por lazer por ano
    calcular_horas_anuais(dados_usuario['horas_lazer'], "lazer")

    # 5 - Funções criativas
    estimativa_paginas(dados_usuario['total_livros'], dados_usuario['paginas'])
    recomendacao(dados_usuario['preferencia'], dados_usuario['nome'])

    print("\nObrigado por compartilhar seus hábitos de leitura!")

# Executa o programa
if __name__ == "__main__":
    main()