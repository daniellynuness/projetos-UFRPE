from src.personagens.personagem import Personagem
import random

class Vilao(Personagem):
    """
    A classe Vilao representa um personagem antagonista com habilidades malignas.
    """
    def __init__(self, nome, idade, vida, maldade, ataque=15, defesa=8):
        super().__init__(nome, idade, vida, ataque, defesa)
        niveis_validos = ['Baixa', 'Média', 'Alta']
        if maldade not in niveis_validos:
            raise ValueError(f"Nível de maldade inválido! Escolha entre {niveis_validos}")
        self.maldade = maldade
        self.poderes_das_trevas = ['Maldição', 'Dreno de Vida', 'Explosão Sombria']
        
    def poder_das_trevas(self, alvo):
        """
        Usa um poder aleatório das trevas contra o alvo.
        """
        poder = random.choice(self.poderes_das_trevas)
        print(f'{self.nome} usa {poder} contra {alvo.nome}!')
        
        if poder == 'Maldição':
            dano = self.ataque * 1.5
            alvo.receber_dano(int(dano))
            alvo.status['Amaldiçoado'] = 3  # Dura 3 turnos
            
        elif poder == 'Dreno de Vida':
            dano = self.ataque
            alvo.receber_dano(int(dano))
            self.curar(int(dano / 2))
            
        elif poder == 'Explosão Sombria':
            dano = self.ataque * 2
            alvo.receber_dano(int(dano))
            self.receber_dano(int(dano * 0.2))  # Dano de recuo
            
    def provocar(self, alvo):
        """
        Provoca o alvo com uma mensagem maligna baseada no nível de maldade.
        """
        provocacoes = {
            'Baixa': f"Você não é páreo para mim, {alvo.nome}!",
            'Média': f"Sua derrota será lenta e dolorosa, {alvo.nome}!",
            'Alta': f"Prepare-se para conhecer seu fim, {alvo.nome}! Muhahahaha!"
        }
        self.dialogar(alvo, provocacoes[self.maldade])
        
    def drenar_poder(self, alvo):
        """
        Drena poder do alvo, reduzindo seus atributos temporariamente.
        """
        reducao_ataque = min(5, alvo.ataque // 4)
        reducao_defesa = min(3, alvo.defesa // 4)
        
        alvo.ataque -= reducao_ataque
        alvo.defesa -= reducao_defesa
        
        print(f'{self.nome} drenou o poder de {alvo.nome}!')
        print(f'{alvo.nome} perdeu {reducao_ataque} de ataque e {reducao_defesa} de defesa!')
        
    def __str__(self):
        return f'Vilão: {super().__str__()} | Maldade: {self.maldade}'