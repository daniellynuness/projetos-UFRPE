class Personagem:
    """
    A classe Personagem representa um personagem genérico em um jogo.
    Serve como classe base para Heroi e Vilao.
    """
    def __init__(self, nome, idade, vida, ataque=10, defesa=5):
        self.nome = nome
        self.idade = idade
        self.vida = vida
        self.vida_maxima = vida
        self.ataque = ataque
        self.defesa = defesa
        self.inventario = []
        self.status = {}
        self.nivel = 1
        self.experiencia = 0
        
    def atacar(self, alvo):
        """
        Realiza um ataque em outro personagem.
        Retorna o dano causado após cálculo com a defesa.
        """
        dano = max(1, self.ataque - alvo.defesa)
        alvo.receber_dano(dano)
        return dano
        
    def receber_dano(self, dano):
        """
        Recebe dano de um ataque, considerando a defesa.
        """
        self.vida = max(0, self.vida - dano)
        print(f'{self.nome} recebeu {dano} de dano! Vida atual: {self.vida}')
        
    def curar(self, quantidade):
        """
        Recupera vida do personagem até o máximo.
        """
        self.vida = min(self.vida_maxima, self.vida + quantidade)
        print(f'{self.nome} recuperou {quantidade} de vida! Vida atual: {self.vida}')
        
    def adicionar_item(self, item):
        """
        Adiciona um item ao inventário do personagem.
        """
        self.inventario.append(item)
        print(f'{self.nome} obteve {item}!')
        
    def dialogar(self, outro_personagem, mensagem):
        """
        Permite diálogo entre personagens.
        """
        print(f'{self.nome} para {outro_personagem.nome}: "{mensagem}"')
        
    def esta_vivo(self):
        """
        Verifica se o personagem ainda está vivo.
        """
        return self.vida > 0
        
    def ganhar_experiencia(self, quantidade):
        """
        Aumenta a experiência do personagem e sobe de nível se necessário.
        """
        self.experiencia += quantidade
        while self.experiencia >= 100 * self.nivel:
            self.experiencia -= 100 * self.nivel
            self.subir_nivel()
            
    def subir_nivel(self):
        """
        Aumenta o nível do personagem e melhora seus atributos.
        """
        self.nivel += 1
        self.vida_maxima += 20
        self.vida = self.vida_maxima
        self.ataque += 5
        self.defesa += 3
        print(f'{self.nome} subiu para o nível {self.nivel}!')
        
    def __str__(self):
        return f'{self.nome} (Nv.{self.nivel}) - Vida: {self.vida}/{self.vida_maxima}, Ataque: {self.ataque}, Defesa: {self.defesa}'