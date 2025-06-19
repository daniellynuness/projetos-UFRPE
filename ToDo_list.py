import os

# --- Estrutura de Dados Principal ---
# Uma lista de dicionários, onde cada dicionário representa uma tarefa.
tarefas = []

def limpar_tela():
    """Limpa o terminal para uma melhor visualização."""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    """Exibe o menu principal de opções para o usuário."""
    print("--- Gerenciador de Tarefas ---")
    print("1. Adicionar nova tarefa")
    print("2. Mover tarefa (alterar status)")
    print("3. Excluir tarefa")
    print("4. Sair")
    print("---------------------------------")
    return input("Escolha uma opção: ")

def listar_tarefas():
    """Lista todas as tarefas existentes com um índice numérico."""
    limpar_tela()
    print("--- Lista de Tarefas ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        print("------------------------")
        return False 
    
    for i, tarefa in enumerate(tarefas):
        print(f"{i + 1}. {tarefa['nome']} (Status: {tarefa['status']})")
    print("------------------------")
    return True 

def adicionar_tarefa():
    """Fluxo para adicionar uma ou mais tarefas."""
    while True:
        limpar_tela()
        print("--- Adicionar Nova Tarefa ---")
        nome_tarefa = input("Digite o nome da tarefa (máx 80 caracteres): ")

        # Decisão: Os requisitos foram atendidos?
        if 0 < len(nome_tarefa) <= 80:
            # Processo: Tarefa criada
            nova_tarefa = {
                "nome": nome_tarefa,
                "status": "a fazer"
            }
            tarefas.append(nova_tarefa)
            print("\nTarefa criada com sucesso!")
        else:
            # Fluxo de erro
            print("\nErro: O nome da tarefa não pode estar vazio e deve ter no máximo 80 caracteres.")

        # Decisão: Criar nova tarefa?
        continuar = input("Deseja adicionar outra tarefa? (s/n): ").lower()
        if continuar != 's':
            break

def mover_tarefa():
    """Fluxo para mover uma tarefa, alterando seu status."""
    limpar_tela()
    print("--- Mover Tarefa ---")
    
    # Processo: Listar tarefas existentes
    if not listar_tarefas():
        input("\nPressione Enter para voltar ao menu...")
        return

    try:
        escolha_tarefa = int(input("Digite o número da tarefa que deseja mover: "))
        indice = escolha_tarefa - 1

        # Validação se a tarefa existe
        if 0 <= indice < len(tarefas):
            print("\nQual o novo status?")
            print("1. Executando")
            print("2. Pronta")
            escolha_status = input("Escolha uma opção: ")

            novo_status = ""
            if escolha_status == '1':
                # Decisão (regra de negócio): Verificar limite de tarefas "executando"
                tarefas_executando = sum(1 for t in tarefas if t['status'] == 'executando')
                if tarefas_executando >= 10:
                    print("\nErro: Limite de 10 tarefas em 'executando' atingido.")
                    input("Pressione Enter para continuar...")
                    return
                novo_status = "executando"
            elif escolha_status == '2':
                novo_status = "pronta"
            else:
                print("\nOpção de status inválida.")
                input("Pressione Enter para continuar...")
                return
            
            # Processo: Atualizar status
            tarefas[indice]['status'] = novo_status
            print(f"\nTarefa '{tarefas[indice]['nome']}' movida para '{novo_status}' com sucesso!")
        else:
            print("\nErro: Número da tarefa inválido.")

    except ValueError:
        print("\nErro: Entrada inválida. Por favor, digite um número.")
    
    input("\nPressione Enter para voltar ao menu...")


def excluir_tarefa():
    """Fluxo para excluir uma ou mais tarefas."""
    while True:
        limpar_tela()
        print("--- Excluir Tarefa ---")
        
        # Processo: Listar tarefas existentes
        if not listar_tarefas():
            input("\nPressione Enter para voltar ao menu...")
            break

        try:
            # Decisão: A escolha é válida?
            escolha_tarefa = int(input("Digite o número da tarefa que deseja excluir (ou 0 para voltar): "))
            
            if escolha_tarefa == 0:
                break
                
            indice = escolha_tarefa - 1

            if 0 <= indice < len(tarefas):
                # Processo: Tarefa removida
                tarefa_removida = tarefas.pop(indice)
                print(f"\nTarefa '{tarefa_removida['nome']}' foi removida com sucesso!")
            else:
                print("\nErro: Número da tarefa inválido.")

        except ValueError:
            print("\nErro: Entrada inválida. Por favor, digite um número.")

        # Decisão: Remover outra tarefa?
        continuar = input("Deseja excluir outra tarefa? (s/n): ").lower()
        if continuar != 's':
            break

def main():
    """Função principal que executa o loop do aplicativo."""
    while True:
        limpar_tela()
        escolha = exibir_menu()

        # Decisão: A escolha é válida?
        if escolha == '1':
            adicionar_tarefa()
        elif escolha == '2':
            mover_tarefa()
        elif escolha == '3':
            excluir_tarefa()
        elif escolha == '4':
            # Fim
            print("Saindo do programa. Até mais!")
            break
        else:
            # Erro
            print("\nOpção inválida! Por favor, tente novamente.")
            input("Pressione Enter para continuar...")

# --- Ponto de Entrada do Programa ---
if __name__ == "__main__":
    main()
