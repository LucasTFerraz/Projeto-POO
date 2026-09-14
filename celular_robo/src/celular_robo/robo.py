# RoboColetor + QuantidadeValida — enunciado, Seção 2.1.
#
# `Robo` (posição, __init_subclass__/_registro, avancar/girar, estrategia/modo,
# Observer) já vem pronto em robo_base.py — não precisa reescrever, só importar:
#
#   from celular_robo.robo_base import Robo, Coordenada
#
# TODO: implemente aqui.
# - RoboColetor(Robo): reaproveita Coordenada (x, y) por herança — não precisa
#   redeclarar. Adicione o que for específico da coleta (ex.: bandeja).
# - QuantidadeValida: descriptor novo (mesmo protocolo de Coordenada/Percentual
#   em robo_base.py), validando que a quantidade coletada de um item nunca é
#   negativa nem passa do pedido.
# - __str__/__repr__ (robô) e __len__ (bandeja — quantos itens já coletados).
from celular_robo.src.celular_robo.base.robo_base import Robo,Coordenada
from celular_robo.src.celular_robo.excecoes import QualidadeBaixa

class QuantidadeValida:
    def checarQualidade(self,q):
        if q<self.minimo: 
                    raise QualidadeBaixa(f"Qualidade {q} esta abaixo de {self.minimo}")
        elif q>100: 
            raise ValueError(f"valor {q} esta fora do limite maximo 100")
    def __init__(self, minimo):
        if not (self.minimo <= minimo <= 100): raise ValueError(
            f"valor minimo {minimo} esta fora do limite de 0 a 100")
        self.minimo = minimo

    def __set_name__(self, owner, name):
        self.nome_publico = name
        self.nome = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.nome]

    def __set__(self, instance, valor):
        if not (self.minimo <= valor <= 100): raise ValueError(
            f"valor minimo {valor} esta fora do limite de 0 a 100")
             #raise ValueError(
        #     f"{self.nome_publico}={valor} esta "
        #     f"{"abaixo da qualidade aceitavel" if valor<100 else "com valor de qualidade invalido"}")
        instance.__dict__[self.nome] = valor
class RoboColetor(Robo):
    def __init__(self,capacidade = 100,**kwargs):
        super().__init__(**kwargs)
        self.capacidade = capacidade