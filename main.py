# Questao 01
class Guerreiro:
    def __init__(self, nome, pv, atq):
        self.nome = nome
        self.pv = pv
        self.atq = atq
        self.arma = None

    def equipar_arma(self, arma):
        self.arma = arma

    def poder_de_ataque(self):
        dano = self.atq
        if self.arma:
            dano += self.arma.dano
        return dano

    def atacar(self):
        return f"{self.nome} ataca causando {self.poder_de_ataque()} de dano!"

    def __str__(self):
        arma_nome = self.arma.nome if self.arma else "Nenhuma"
        return (
            f"Guerreiro: {self.nome}\n"
            f"PV: {self.pv}\n"
            f"Ataque Base: {self.atq}\n"
            f"Arma: {arma_nome}\n"
            f"Poder de Ataque Total: {self.poder_de_ataque()}"
        )


class Arma:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano


class Pocao:
    def __init__(self, nome, cura):
        self.nome = nome
        self.cura = cura


espada = Arma("Espada Longa", 10)
meu_guerreiro = Guerreiro("Aragorn", 100, 30)
meu_guerreiro.equipar_arma(espada)

# Questao 02
class Mago:
    def __init__(self, nome, pv, atq, poder_magico):
        self.nome = nome
        self.pv = pv
        self.atq = atq
        self.poder_magico = poder_magico
        self.arma = None

    def equipar_arma(self, arma):
        self.arma = arma

    def poder_de_ataque(self):
        dano = self.atq + self.poder_magico
        if self.arma:
            dano += self.arma.dano
        return dano

    def atacar(self):
        return f"{self.nome} conjura uma magia causando {self.poder_de_ataque()} de dano!"

    def __str__(self):
        arma_nome = self.arma.nome if self.arma else "Nenhuma"
        return (
            f"Mago: {self.nome}\n"
            f"PV: {self.pv}\n"
            f"Ataque Base: {self.atq}\n"
            f"Poder Magico: {self.poder_magico}\n"
            f"Arma: {arma_nome}\n"
            f"Poder Total de Ataque: {self.poder_de_ataque()}"
        )

cajado = Arma("Cajado Arcano", 8)
meu_mago = Mago("Gandalf", 80, 10, 20)
meu_mago.equipar_arma(cajado)

# Questao 03
class Arqueiro:
    def __init__(self, nome, pv, atq, destreza):
        self.nome = nome
        self.pv = pv
        self.atq = atq
        self.destreza = destreza
        self.arma = None

    def equipar_arma(self, arma):
        self.arma = arma

    def poder_de_ataque(self):
        dano = self.atq + int(self.destreza * 0.5)
        if self.arma:
            dano += self.arma.dano
        return dano

    def atacar(self):
        return f"{self.nome} dispara uma flecha causando {self.poder_de_ataque()} de dano!"

    def __str__(self):
        arma_nome = self.arma.nome if self.arma else "Nenhuma"
        return (
            f"Arqueiro: {self.nome}\n"
            f"PV: {self.pv}\n"
            f"Ataque Base: {self.atq}\n"
            f"Destreza: {self.destreza}\n"
            f"Arma: {arma_nome}\n"
            f"Poder Total de Ataque: {self.poder_de_ataque()}"
        )

arco = Arma("Arco Elfico", 7)
meu_arqueiro = Arqueiro("Legolas", 70, 12, 18)
meu_arqueiro.equipar_arma(arco)

# Questao 04
class Mob:
    def __init__(self, nome, pv, atq):
        self.nome = nome
        self.pv = pv
        self.atq = atq

    def atacar(self):
        return f"{self.nome} ataca causando {self.atq} de dano!"

    def __str__(self):
        return (
            f"Mob: {self.nome}\n"
            f"PV: {self.pv}\n"
            f"Atq: {self.atq}"
        )

Goblin = Mob("Goblin", pv=30, atq=5)

# Questao 05 ja atendida com __str__ nas classes

# Questao 06 ja atendida com atacar simples

# Questao 07
Espada_Longa = Arma("Espada Longa", 12)
Cajado_Magico = Arma("Cajado Magico", 7)
Arco_Curvado = Arma("Arco Curvado", 9)

# Questao 08
Pocao_de_Vida = Pocao("Pocao de Vida", 50)

# Questao 15 (Inventario adiantado para uso em Personagem)
class Inventario:
    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def remover(self, item):
        if item in self.itens:
            self.itens.remove(item)

    def listar(self):
        return [item.nome for item in self.itens]

    def buscar_primeiro(self, tipo):
        for item in self.itens:
            if isinstance(item, tipo):
                return item
        return None

# Questao 11, 12, 13
class Personagem:
    def __init__(self, nome, pv, atq):
        self.nome = nome
        self._pv = pv
        self._pv_max = pv
        self.atq = atq
        self.arma = None
        self.inventario = Inventario()
        self.habilidades = []

    @property
    def pv(self):
        return self._pv

    @pv.setter
    def pv(self, valor):
        if valor < 0:
            self._pv = 0
        elif valor > self._pv_max:
            self._pv = self._pv_max
        else:
            self._pv = valor

    def equipar_arma(self, arma):
        self.arma = arma

    def poder_de_ataque(self):
        dano = self.atq
        if self.arma:
            dano += self.arma.dano
        return dano

    def receber_dano(self, valor):
        self.pv = self.pv - max(0, valor)
        print(f"{self.nome} recebeu {valor} de dano. PV atual: {self.pv}")

    def atacar(self, alvo):
        variacao = Dado.rolar(4)
        dano = self.poder_de_ataque() + variacao
        print(f"{self.nome} ataca causando {dano} de dano! (sorte {variacao})")
        alvo.receber_dano(dano)

    def esta_vivo(self):
        return self.pv > 0

    def usar_pocao(self, pocao):
        if pocao in self.inventario.itens:
            print(f"{self.nome} usou {pocao.nome} e recuperou {pocao.cura} de vida!")
            self.pv += pocao.cura
            self.inventario.remover(pocao)
        else:
            print("Pocao nao encontrada no inventario!")

    def __str__(self):
        arma_nome = self.arma.nome if self.arma else "Nenhuma"
        return (
            f"Nome: {self.nome}\n"
            f"PV: {self.pv}/{self._pv_max}\n"
            f"Ataque Base: {self.atq}\n"
            f"Arma: {arma_nome}\n"
            f"Poder Total de Ataque: {self.poder_de_ataque()}"
        )

# Questao 18
class Guerreiro(Personagem):
    def atacar(self, alvo):
        print(f"{self.nome} desfere um golpe poderoso!")
        super().atacar(alvo)

class Mago(Personagem):
    def __init__(self, nome, pv, atq, magia):
        super().__init__(nome, pv, atq)
        self.magia = magia

    def poder_de_ataque(self):
        return super().poder_de_ataque() + self.magia

    def atacar(self, alvo):
        print(f"{self.nome} conjura uma bola de fogo!")
        super().atacar(alvo)

class Arqueiro(Personagem):
    def __init__(self, nome, pv, atq, destreza):
        super().__init__(nome, pv, atq)
        self.destreza = destreza

    def poder_de_ataque(self):
        return super().poder_de_ataque() + int(self.destreza * 0.5)

    def atacar(self, alvo):
        print(f"{self.nome} dispara uma flecha precisa!")
        super().atacar(alvo)

# Questao 19
class Monstro:
    def __init__(self, nome, pv, atq):
        self.nome = nome
        self.pv = pv
        self.atq = atq

    def esta_vivo(self):
        return self.pv > 0

    def receber_dano(self, valor):
        self.pv = max(0, self.pv - valor)
        print(f"{self.nome} recebeu {valor} de dano. PV atual: {self.pv}")

    def atacar(self, alvo):
        variacao = Dado.rolar(3)
        dano = self.atq + variacao
        print(f"{self.nome} ataca causando {dano} de dano! (sorte {variacao})")
        alvo.receber_dano(dano)

def criar_goblin():
    return Monstro("Goblin", 30, 5)

# Questao 20 ja atendida com esta_vivo

# Questao 21 em diante
class Habilidade:
    def usar(self, atacante, alvo):
        raise NotImplementedError

class AtaqueForte(Habilidade):
    def usar(self, atacante, alvo):
        variacao = Dado.rolar(6)
        dano = atacante.poder_de_ataque() * 2 + variacao
        print(f"{atacante.nome} usa Ataque Forte causando {dano}! (sorte {variacao})")
        alvo.receber_dano(dano)

class BolaDeFogo(Habilidade):
    def usar(self, atacante, alvo):
        variacao = Dado.rolar(6)
        dano = atacante.poder_de_ataque() + atacante.magia + variacao
        print(f"{atacante.nome} usa Bola de Fogo causando {dano}! (sorte {variacao})")
        alvo.receber_dano(dano)

class Dado:
    _seed = 1234567

    @classmethod
    def set_seed(cls, valor):
        cls._seed = valor

    @classmethod
    def rolar(cls, lados=6):
        cls._seed = (cls._seed * 1103515245 + 12345) % 2147483647
        return cls._seed % lados + 1

class Mago(Mago):
    def __init__(self, nome, pv=80, atq=10, magia=20):
        super().__init__(nome, pv, atq, magia)
        self.habilidades.append(BolaDeFogo())

class Guerreiro(Guerreiro):
    def __init__(self, nome, pv=100, atq=30):
        super().__init__(nome, pv, atq)
        self.habilidades.append(AtaqueForte())

class Arqueiro(Arqueiro):
    def __init__(self, nome, pv=70, atq=12, destreza=18):
        super().__init__(nome, pv, atq, destreza)

class Combatente(Personagem):
    def atacar(self, alvo):
        variacao = Dado.rolar(4)
        dano = self.poder_de_ataque() + variacao
        print(f"{self.nome} ataca causando {dano} de dano!")
        alvo.receber_dano(dano)

class Orc(Monstro):
    def atacar(self, alvo):
        critico = Dado.rolar(10) == 10
        variacao = Dado.rolar(4)
        dano = self.atq + variacao
        if critico:
            dano *= 2
            print(f"{self.nome} acertou um critico!")
        print(f"{self.nome} golpeia causando {dano} de dano!")
        alvo.receber_dano(dano)

class Batalha:
    def __init__(self, combatente_a, combatente_b):
        self.a = combatente_a
        self.b = combatente_b

    def lutar(self):
        atacante, defensor = self.a, self.b
        while atacante.esta_vivo() and defensor.esta_vivo():
            atacante.atacar(defensor)
            atacante, defensor = defensor, atacante
        vencedor = atacante if atacante.esta_vivo() else defensor
        print(f"Vencedor: {vencedor.nome}")
        return vencedor

class BatalhaEmEquipe:
    def __init__(self, equipe1, equipe2):
        self.e1 = equipe1
        self.e2 = equipe2

    def _proximo_vivo(self, equipe):
        for c in equipe:
            if c.esta_vivo():
                return c
        return None

    def lutar(self):
        turno_e1 = True
        while self._proximo_vivo(self.e1) and self._proximo_vivo(self.e2):
            atacante = self._proximo_vivo(self.e1 if turno_e1 else self.e2)
            defensor = self._proximo_vivo(self.e2 if turno_e1 else self.e1)
            if not atacante or not defensor:
                break
            atacante.atacar(defensor)
            turno_e1 = not turno_e1
        vencedora = self.e1 if self._proximo_vivo(self.e1) else self.e2
        nomes = [c.nome for c in vencedora if c.esta_vivo()]
        print(f"Equipe vencedora: {', '.join(nomes)}")
        return vencedora

if __name__ == "__main__":
    # semente diferente a cada execução (usa endereço de um objeto criado na hora)
    Dado.set_seed(id(object()))

    espada_longa = Arma("Espada Longa", 12)
    cajado_magico = Arma("Cajado Magico", 7)
    arco_curvo = Arma("Arco Curvado", 9)
    pocao = Pocao("Pocao de Vida", 50)

    guerreiro = Guerreiro("Aragorn")
    mago = Mago("Gandalf")
    arqueiro = Arqueiro("Legolas")

    guerreiro.equipar_arma(espada_longa)
    mago.equipar_arma(cajado_magico)
    arqueiro.equipar_arma(arco_curvo)
    guerreiro.inventario.adicionar(pocao)

    goblin = criar_goblin()
    orc = Orc("Orc Grandao", 90, 10)

    print(guerreiro)
    Batalha(guerreiro, goblin).lutar()
    guerreiro.usar_pocao(pocao)
    Batalha(mago, orc).lutar()
    BatalhaEmEquipe([guerreiro, arqueiro], [orc, goblin]).lutar()
