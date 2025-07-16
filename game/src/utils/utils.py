import random
from typing import List
from src.personagens.personagem import Personagem
from src.personagens.heroi import Heroi
from src.personagens.vilao import Vilao

def criar_batalha(herois: List[Heroi], viloes: List[Vilao]):
    """
    Gerencia uma batalha entre heróis e vilões.
    """
    print("\n=== INÍCIO DA BATALHA ===")
    
    # Lista com todos os personagens vivos
    todos_personagens = herois + viloes
    
    # Enquanto houver pelo menos um herói e um vilão vivos
    turno = 1
    while any(h.esta_vivo() for h in herois) and any(v.esta_vivo() for v in viloes):
        print(f"\n=== Turno {turno} ===")
        
        # Ordenar personagens por nível e um pouco de aleatoriedade
        random.shuffle(todos_personagens)
        todos_personagens.sort(key=lambda x: x.nivel + random.randint(-1, 1), reverse=True)
        
        # Cada personagem vivo age em seu turno
        for personagem in todos_personagens:
            if not personagem.esta_vivo():
                continue
                
            # Se for herói
            if isinstance(personagem, Heroi):
                # Encontra vilões vivos
                viloes_vivos = [v for v in viloes if v.esta_vivo()]
                if not viloes_vivos:
                    break
                    
                alvo = random.choice(viloes_vivos)
                
                # 30% de chance de usar habilidade especial
                if random.random() < 0.3:
                    personagem.usar_habilidade_especial(alvo)
                else:
                    dano = personagem.atacar(alvo)
                    print(f'{personagem.nome} causou {dano} de dano em {alvo.nome}!')
                    
                # Se estiver com pouca vida, chance de usar poção
                if personagem.vida < personagem.vida_maxima * 0.3 and random.random() < 0.7:
                    personagem.usar_pocao()
                    
            # Se for vilão
            elif isinstance(personagem, Vilao):
                # Encontra heróis vivos
                herois_vivos = [h for h in herois if h.esta_vivo()]
                if not herois_vivos:
                    break
                    
                alvo = random.choice(herois_vivos)
                
                # 20% de chance de usar poder das trevas
                if random.random() < 0.2:
                    personagem.poder_das_trevas(alvo)
                else:
                    dano = personagem.atacar(alvo)
                    print(f'{personagem.nome} causou {dano} de dano em {alvo.nome}!')
                    
        # Mostra status dos personagens ao final do turno
        print("\nStatus após o turno:")
        for p in todos_personagens:
            if p.esta_vivo():
                print(f"- {p}")
            else:
                print(f"- {p.nome} foi derrotado!")
                
        turno += 1
        
    # Determina o vencedor
    if any(h.esta_vivo() for h in herois):
        print("\n=== Os Heróis venceram! ===")
        for h in herois:
            if h.esta_vivo():
                h.ganhar_experiencia(100)
    else:
        print("\n=== Os Vilões venceram! ===")

def registrar_evento(evento: str):
    """
    Registra eventos importantes do jogo.
    """
    print(f"\n[EVENTO] {evento}")