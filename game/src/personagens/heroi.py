from src.personagens.personagem import Personagem
import random

class Heroi(Personagem):
    """
    A classe Heroi representa um personagem protagonista com habilidades heroicas.
    """
    def __init__(self, nome, idade, vida, classe, ataque=12, defesa=10):
        super().__init__(nome, idade, vida, ataque, defesa)
        classes_validas = ['Guerreiro', 'Mago', 'Arqueiro']
        if classe not in classes_validas:
            raise ValueError(f"Classe inválida! Escolha entre {classes_validas}")
        self.classe = classe
        self.pocoes_cura = 3
        self.habilidades_especiais = self._definir_habilidades()
        
    def _definir_habilidades(self):
        """
        Define as habilidades especiais baseadas na classe do herói.
        """
        habilidades = {
            'Guerreiro': ['Golpe Heroico', 'Escudo Protetor', 'Grito de Guerra'],
            'Mago': ['Bola de Fogo', 'Barreira Mágica', 'Raio Congelante'],
            'Arqueiro': ['Chuva de Flechas', 'Tiro Preciso', 'Flecha Explosiva']
        }
        return habilidades[self.classe]
        
    def usar_habilidade_especial(self, alvo):
        """
        Usa uma habilidade especial contra o alvo.
        """
        habilidade = random.choice(self.habilidades_especiais)
        print(f'{self.nome} usa {habilidade}!')
        
        if 'Golpe' in habilidade or 'Tiro' in habilidade or 'Bola' in habilidade:
            dano = self.ataque * 2
            alvo.receber_dano(int(dano))
            
        elif 'Escudo' in habilidade or 'Barreira' in habilidade:
            self.defesa *= 2  # Dobra a defesa temporariamente
            print(f'{self.nome} aumentou sua defesa!')
            
        else:  # Habilidades de área/suporte
            dano = self.ataque * 1.5
            alvo.receber_dano(int(dano))
            
    def usar_pocao(self):
        """
        Usa uma poção de cura se disponível.
        """
        if self.pocoes_cura > 0:
            self.pocoes_cura -= 1
            cura = self.vida_maxima // 2
            self.curar(cura)
            print(f'Poções restantes: {self.pocoes_cura}')
        else:
            print(f'{self.nome} não tem mais poções!')
            
    def inspirar(self, aliado):
        """
        Inspira um aliado, aumentando seus atributos temporariamente.
        """
        if isinstance(aliado, Heroi):
            aumento = 5
            aliado.ataque += aumento
            aliado.defesa += aumento
            print(f'{self.nome} inspirou {aliado.nome}! Ataque e defesa aumentados em {aumento}!')
        
    def salvar_refem(self, refem):
        """
        Tenta salvar um refém.
        """
        chance_sucesso = random.random()
        if chance_sucesso > 0.3:  # 70% de chance de sucesso
            print(f'{self.nome} salvou {refem} com sucesso!')
            self.ganhar_experiencia(50)
            return True
        else:
            print(f'{self.nome} falhou em salvar {refem}...')
            return False
            
    def __str__(self):
        return f'Herói: {super().__str__()} | Classe: {self.classe} | Poções: {self.pocoes_cura}'