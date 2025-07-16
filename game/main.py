from src.personagens.personagem import Personagem
from src.personagens.heroi import Heroi
from src.personagens.vilao import Vilao
from src.utils.utils import criar_batalha, registrar_evento

def main():
    # Criando heróis
    herois = [
        Heroi('Arthur', 25, 100, 'Guerreiro', ataque=15, defesa=12),
        Heroi('Merlin', 60, 80, 'Mago', ataque=20, defesa=8),
        Heroi('Robin', 30, 90, 'Arqueiro', ataque=18, defesa=10)
    ]
    
    # Criando vilões
    viloes = [
        Vilao('Morgaroth', 100, 150, 'Alta', ataque=18, defesa=15),
        Vilao('Sombrio', 45, 100, 'Média', ataque=15, defesa=12),
        Vilao('Lacaio', 30, 70, 'Baixa', ataque=12, defesa=8)
    ]
    
    # Demonstração de diálogos
    registrar_evento("Início da história")
    viloes[0].provocar(herois[0])
    herois[0].dialogar(viloes[0], "Suas ameaças não me assustam!")
    
    # Demonstração de itens e habilidades
    registrar_evento("Preparação para batalha")
    for heroi in herois:
        heroi.adicionar_item("Poção de Cura")
        heroi.adicionar_item("Amuleto de Proteção")
    
    # Iniciando a batalha
    registrar_evento("Início da grande batalha")
    criar_batalha(herois, viloes)
    
    # Demonstração pós-batalha (se os heróis sobreviverem)
    for heroi in herois:
        if heroi.esta_vivo():
            registrar_evento(f"{heroi.nome} sobreviveu à batalha!")
            if len(heroi.inventario) > 0:
                print(f"Inventário de {heroi.nome}: {', '.join(heroi.inventario)}")


if __name__ == "__main__":
    main()